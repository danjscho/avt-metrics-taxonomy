"""Golden-corpus regression tests.

A small synthetic corpus (`tests/data/golden_corpus.jsonl`, 8 pairs
across 4 speaker-group labels) with pinned numerical results for every
implemented metric. The corpus is deliberately tiny and synthetic — it
is not designed to be statistically meaningful or clinically realistic.
Its job is to detect *silent metric output drift* when a dependency
updates: if jiwer changes its averaging convention, or rouge-score
changes its stemming behaviour, these pinned numbers will move and the
diff will surface the change deliberately.

When intentionally changing a metric's behaviour, run the corpus
manually and update the pinned numbers in the same commit; treat
unintended diffs as a red flag rather than a fixture-update task.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from avt_metrics_ref import (
    cer,
    disaggregated_wer,
    rouge,
    system_availability,
    wer,
)

# Tolerance: 1e-9 catches any meaningful drift while absorbing the last
# bit of float noise. We use approx() rather than == so the pinned
# numbers can be regenerated and compared without bit-exact friction.
_TOL = 1e-9

CORPUS_PATH = Path(__file__).parent / "data" / "golden_corpus.jsonl"


@pytest.fixture(scope="module")
def corpus():
    with CORPUS_PATH.open() as f:
        return [json.loads(line) for line in f if line.strip()]


def test_corpus_has_expected_shape(corpus):
    """8 pairs across 4 speaker groups, two pairs per group."""
    assert len(corpus) == 8
    groups = {p["speaker_group"] for p in corpus}
    assert groups == {"british-rp", "scottish", "general-american", "south-asian"}
    for p in corpus:
        assert {"id", "speaker_group", "reference", "hypothesis"} <= set(p.keys())


def test_aggregate_wer_pinned(corpus):
    refs = [p["reference"] for p in corpus]
    hyps = [p["hypothesis"] for p in corpus]
    # Pinned: 3 substitutions + 1 deletion across 77 reference words = 4/77.
    # Updated mechanically when adding/removing pairs from the corpus.
    assert wer(refs, hyps) == pytest.approx(0.03896103896103896, abs=_TOL)


def test_aggregate_cer_pinned(corpus):
    refs = [p["reference"] for p in corpus]
    hyps = [p["hypothesis"] for p in corpus]
    assert cer(refs, hyps) == pytest.approx(0.02360515021459227, abs=_TOL)


def test_per_pair_wer_pinned(corpus):
    """Identity pairs score 0; substitution-only pairs score the
    expected error rate per the catalogue's WER formula."""
    expected = {
        "g01": 0.0,
        "g02": 0.0,
        "g03": 0.0,
        "g04": 1 / 11,  # 1 substitution / 11 ref words ("inhaler" → "puffer")
        "g05": 0.0,
        "g06": 1 / 9,  # 1 substitution / 9 ref words ("palpitations" → "papitations")
        "g07": 1 / 10,  # 1 deletion / 10 ref words ("once")
        "g08": 0.0,
    }
    for pair in corpus:
        actual = wer(pair["reference"], pair["hypothesis"])
        assert actual == pytest.approx(expected[pair["id"]], abs=_TOL), (
            f"WER drift on {pair['id']}: got {actual}, expected {expected[pair['id']]}"
        )


def test_disaggregated_wer_pinned(corpus):
    """Disaggregated WER's per-group breakdown + equity gap are pinned.
    The 'general-american' group has the worst per-group WER because
    g06's substitution lands in the smaller of its two pairs."""
    result = disaggregated_wer(corpus, group_key="speaker_group")
    assert result["aggregate_wer"] == pytest.approx(0.03896103896103896, abs=_TOL)
    assert result["worst_group"] == "general-american"
    assert result["best_group"] == "british-rp"
    expected_per_group = {
        "british-rp": 0.0,
        "scottish": 0.047619047619047616,  # 1 sub / 21 ref words across two pairs
        "general-american": 0.0625,  # 1 sub / 16 ref words across two pairs
        "south-asian": 0.047619047619047616,  # 1 deletion / 21 ref words
    }
    for group, pinned in expected_per_group.items():
        assert result["per_group"][group]["wer"] == pytest.approx(pinned, abs=_TOL)
        assert result["per_group"][group]["n"] == 2
    # Equity gap = worst - best = 0.0625 - 0 = 0.0625 → just over the
    # default 0.05 threshold, so threshold_met should be False.
    assert result["equity_gap"] == pytest.approx(0.0625, abs=_TOL)
    assert result["threshold_met"] is False


def test_rouge_pinned_on_partial_overlap(corpus):
    """The three corpus pairs with non-trivial substitution have pinned
    ROUGE-1 / ROUGE-L F1 scores. Identity pairs trivially hit 1.0 and
    aren't worth pinning here (covered by test_rouge.py)."""
    by_id = {p["id"]: p for p in corpus}
    expected = {
        "g04": (0.9090909090909091, 0.9090909090909091),  # rouge1.f1, rougeL.f1
        "g06": (0.8888888888888888, 0.8888888888888888),
        "g07": (0.9473684210526315, 0.9473684210526315),
    }
    for pid, (r1_f1, rL_f1) in expected.items():
        result = rouge(by_id[pid]["reference"], by_id[pid]["hypothesis"])
        assert result.rouge1.f1 == pytest.approx(r1_f1, abs=_TOL), (
            f"ROUGE-1 drift on {pid}"
        )
        assert result.rougeL.f1 == pytest.approx(rL_f1, abs=_TOL), (
            f"ROUGE-L drift on {pid}"
        )


def test_system_availability_pinned():
    """GV.OP-5 doesn't take corpus input but is pinned here so the
    classification bands are exercised by the regression suite."""
    # 99.8% — meets target
    r = system_availability(operational_minutes=10000, down_minutes=20)
    assert r.availability_pct == pytest.approx(99.8, abs=_TOL)
    assert r.classification == "meets-target"

    # 99.3% — below target band
    r = system_availability(operational_minutes=10000, down_minutes=70)
    assert r.availability_pct == pytest.approx(99.3, abs=_TOL)
    assert r.classification == "below-target"

    # 98.0% — escalation band
    r = system_availability(operational_minutes=10000, down_minutes=200)
    assert r.availability_pct == pytest.approx(98.0, abs=_TOL)
    assert r.classification == "escalation"
