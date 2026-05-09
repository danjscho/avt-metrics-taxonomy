"""Tests for TP.SN-2 BERTScore.

The bert-score dependency is heavyweight (transformer model load + GPU
optional). These tests skip if the package isn't installed; they only
run when the user has opted in via the ``bertscore`` extra.
"""

from __future__ import annotations

import importlib.util

import pytest

bertscore_available = importlib.util.find_spec("bert_score") is not None
pytestmark = pytest.mark.skipif(
    not bertscore_available,
    reason="bert-score not installed (install with `pip install 'avt-metrics-ref[bertscore]'`)",
)


def test_import_path():
    """`bertscore` is reachable via the lazy attribute on tp.sn but not
    forced into the top-level namespace import."""
    from avt_metrics_ref.tp.sn import bertscore as bs

    assert callable(bs)


def test_returns_one_result_per_pair():
    """Sanity test only — we don't pin BERTScore numbers because they
    drift across model / package versions; pinned tests live in the
    golden-corpus test once it lands (Phase 6 of plan-reference-library)."""
    from avt_metrics_ref.tp.sn import bertscore

    refs = ["the patient has chest pain", "the patient has fever"]
    hyps = ["patient reports chest discomfort", "the patient is febrile"]
    # Use a small fast model for the test rather than the default DeBERTa-XL.
    results = bertscore(
        refs,
        hyps,
        model_type="distilbert-base-uncased",
        num_layers=5,
    )
    assert len(results) == 2
    for r in results:
        # F1 in [0, 1] for normal (non-rescaled) BERTScore output.
        assert 0.0 <= r.f1 <= 1.0
        assert r.model == "distilbert-base-uncased"
        assert r.num_layers == 5


def test_mismatched_lengths_raise():
    from avt_metrics_ref.tp.sn import bertscore

    with pytest.raises(ValueError, match="same length"):
        bertscore(["a", "b"], ["only one"])


def test_lazy_import_when_extra_missing(monkeypatch):
    """If bert_score is not installed, calling bertscore() raises a
    helpful ImportError. We simulate the missing package by clearing
    sys.modules and shadowing the import lookup."""
    import sys

    from avt_metrics_ref.tp.sn import bertscore as bs

    # Pretend bert_score is unimportable for the duration of this test.
    real_bert_score = sys.modules.pop("bert_score", None)
    try:
        monkeypatch.setattr(
            "importlib.util.find_spec",
            lambda name: None if name == "bert_score" else importlib.util.find_spec(name),
        )

        # Force the function's local `from bert_score import score` to fail.
        # Easiest reliable mechanism: shadow bert_score with a sentinel that
        # raises ImportError when accessed.
        class _ImportFail:
            def __getattr__(self, _):
                raise ImportError("simulated missing bert_score")

        monkeypatch.setitem(sys.modules, "bert_score", _ImportFail())

        # Re-import the module so the inner function-local import sees the patched module.
        # (The function imports bert_score lazily inside the call, so no reload needed.)
        with pytest.raises(ImportError, match="bert-score"):
            bs(["a"], ["b"])
    finally:
        # Restore the real module if it existed.
        if real_bert_score is not None:
            sys.modules["bert_score"] = real_bert_score
        else:
            sys.modules.pop("bert_score", None)
