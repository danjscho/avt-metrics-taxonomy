"""Tests for TP.SN-1 ROUGE."""

from __future__ import annotations

import pytest

from avt_metrics_ref import rouge
from avt_metrics_ref.tp.sn.rouge import RougeResult, RougeScore


def test_identical_strings_score_1():
    """Identical reference and hypothesis should score 1.0 on every variant."""
    text = "Patient presents with cough and fever."
    result = rouge(text, text)
    assert isinstance(result, RougeResult)
    assert result.rouge1 is not None
    assert result.rouge1.precision == pytest.approx(1.0)
    assert result.rouge1.recall == pytest.approx(1.0)
    assert result.rouge1.f1 == pytest.approx(1.0)
    assert result.rouge2.f1 == pytest.approx(1.0)
    assert result.rougeL.f1 == pytest.approx(1.0)


def test_disjoint_strings_score_0():
    """Strings with no token overlap should score 0."""
    result = rouge("alpha beta gamma", "xxxxx yyyyy zzzzz")
    assert result.rouge1.f1 == pytest.approx(0.0)
    assert result.rouge2.f1 == pytest.approx(0.0)
    assert result.rougeL.f1 == pytest.approx(0.0)


def test_partial_overlap_intermediate_score():
    """A hypothesis with partial overlap scores between 0 and 1."""
    result = rouge(
        "Patient presents with cough and fever.",
        "Patient has cough and fever.",
    )
    assert 0.0 < result.rouge1.f1 < 1.0
    # rouge1 is unigram overlap; at least "patient", "cough", "fever" overlap
    assert result.rouge1.f1 > 0.5


def test_clinically_unsafe_omission_still_scores_high():
    """Catalogue's worked example: a clinically-critical omission still scores
    moderately on ROUGE because string overlap is preserved. This is the
    failure mode that motivates the underspecification warning at TP.SN-1."""
    reference = (
        "Patient presents with 3-day history of productive cough, fever 38.5C. "
        "Started amoxicillin 500mg TDS for 5 days."
    )
    hypothesis = (
        "Patient has had a cough for 3 days with fever. Prescribed antibiotics."
    )
    result = rouge(reference, hypothesis)
    # The hypothesis omits the drug name + dose — clinically unsafe — but
    # ROUGE-1 is still substantial because surface tokens overlap.
    assert result.rouge1.f1 > 0.3


def test_variants_subset():
    """Caller can request only some variants; others come back as None."""
    result = rouge("hello world", "hello world", variants=("rouge1",))
    assert result.rouge1 is not None
    assert result.rouge2 is None
    assert result.rougeL is None


def test_unknown_variant_raises():
    with pytest.raises(ValueError, match="unknown ROUGE variant"):
        rouge("a", "b", variants=("rouge9",))


def test_corpus_level_returns_per_pair_list():
    refs = ["hello world", "patient has fever"]
    hyps = ["hello there", "patient has cough"]
    result = rouge(refs, hyps)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(isinstance(r, RougeResult) for r in result)


def test_mismatched_corpus_lengths_raise():
    with pytest.raises(ValueError, match="same length"):
        rouge(["a", "b"], ["a"])


def test_mixed_str_and_sequence_inputs_raise():
    with pytest.raises(TypeError, match="both be str or both be sequences"):
        rouge("a string", ["a list"])


def test_stemmer_default_handles_minor_morphology():
    """Default stemmer collapses 'fevers' / 'fever' to the same stem."""
    with_stem = rouge("the patient has fevers", "the patient has fever", use_stemmer=True)
    without_stem = rouge("the patient has fevers", "the patient has fever", use_stemmer=False)
    # With stemming, the rouge1 F1 should be higher (or equal) — fever ≈ fevers.
    assert with_stem.rouge1.f1 >= without_stem.rouge1.f1


def test_rouge_score_namedtuple_fields():
    """Public RougeScore type exposes precision / recall / f1 fields."""
    s = RougeScore(precision=0.8, recall=0.6, f1=0.685)
    assert s.precision == 0.8
    assert s.recall == 0.6
    assert s.f1 == 0.685
