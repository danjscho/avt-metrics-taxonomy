"""Tests for TP.ASR-3 Clinical Keyword Error Rate."""
from __future__ import annotations

import pytest

from avt_metrics_ref import clinical_keyword_error_rate


def _naive_extractor(text: str) -> list[str]:
    """Test extractor — checks for known clinical terms."""
    keywords = [
        "amoxicillin", "amoxycillin", "warfarin", "paracetamol",
        "asthma", "diabetes", "anaphylaxis",
    ]
    return [k for k in keywords if k in text.lower()]


class TestCKERBasics:
    def test_identical_zero_error(self):
        result = clinical_keyword_error_rate(
            "patient has asthma and takes amoxicillin",
            "patient has asthma and takes amoxicillin",
            extractor=_naive_extractor,
        )
        assert result["cker"] == 0.0

    def test_no_keywords_in_reference(self):
        """If extractor returns no reference keywords, CK-ER is 0 by convention."""
        result = clinical_keyword_error_rate(
            "the cat sat on the mat",
            "the cat sat on the mat",
            extractor=_naive_extractor,
        )
        assert result["cker"] == 0.0
        assert len(result["ref_keywords"]) == 0

    def test_full_keyword_loss(self):
        """All ref keywords missing → CK-ER = 1.0."""
        result = clinical_keyword_error_rate(
            "patient has asthma and takes warfarin",
            "patient is fine",  # no clinical keywords detected
            extractor=_naive_extractor,
        )
        assert result["cker"] == 1.0
        assert len(result["missing"]) == 2


class TestCKERSimilarity:
    def test_near_match_with_default_threshold(self):
        """amoxicillin/amoxycillin should match at threshold 0.85."""
        result = clinical_keyword_error_rate(
            "took amoxicillin",
            "took amoxycillin",  # 1 char different
            extractor=_naive_extractor,
        )
        # Both keywords are extracted; amoxicillin in ref, amoxycillin in hyp.
        # Levenshtein ratio ~0.91 — should match at 0.85 threshold.
        assert result["cker"] == 0.0
        assert result["matched"] == 1

    def test_strict_threshold_catches_near_miss(self):
        """At threshold 0.99, near-misses should fail."""
        result = clinical_keyword_error_rate(
            "took amoxicillin",
            "took amoxycillin",
            extractor=_naive_extractor,
            similarity_threshold=0.99,
        )
        assert result["cker"] == 1.0
        assert "amoxicillin" in result["missing"]


class TestCKERValidation:
    def test_threshold_out_of_range_raises(self):
        with pytest.raises(ValueError, match=r"\[0, 1\]"):
            clinical_keyword_error_rate(
                "took amoxicillin",
                "took amoxicillin",
                extractor=_naive_extractor,
                similarity_threshold=1.5,
            )

    def test_negative_threshold_raises(self):
        with pytest.raises(ValueError, match=r"\[0, 1\]"):
            clinical_keyword_error_rate(
                "took amoxicillin",
                "took amoxicillin",
                extractor=_naive_extractor,
                similarity_threshold=-0.1,
            )
