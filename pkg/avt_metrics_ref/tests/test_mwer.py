"""Tests for TP.ASR-2 Medical WER."""
from __future__ import annotations

import pytest

from avt_metrics_ref import medical_wer
from avt_metrics_ref.tp.asr.mwer import DEFAULT_WEIGHTS


def _drug_classifier(token: str) -> str:
    """Test classifier — covers a few common terms."""
    drugs = {"amoxicillin", "amoxycillin", "paracetamol", "warfarin"}
    if token.lower() in drugs:
        return "drug_name"
    if token.endswith("mg"):
        return "dosage"
    if token.lower() in {"the", "a", "and", "of"}:
        return "filler"
    return "default"


class TestMWERBasics:
    def test_identical_zero_error(self):
        result = medical_wer(
            "the patient took amoxicillin",
            "the patient took amoxicillin",
            classifier=_drug_classifier,
        )
        assert result["mwer"] == 0.0

    def test_drug_substitution_high_weighted_error(self):
        """A drug substitution should outweigh a filler error."""
        # 1 drug error
        drug_err = medical_wer(
            "took amoxicillin",
            "took warfarin",
            classifier=_drug_classifier,
        )
        # 1 filler error
        filler_err = medical_wer(
            "the patient",
            "a patient",
            classifier=_drug_classifier,
        )
        assert drug_err["mwer"] > filler_err["mwer"]

    def test_per_class_breakdown(self):
        result = medical_wer(
            "took amoxicillin 500mg",
            "took warfarin 500mg",
            classifier=_drug_classifier,
        )
        assert result["per_class_errors"]["drug_name"] == 1
        assert result["per_class_total"]["drug_name"] == 1
        # dosage was correct
        assert result["per_class_total"]["dosage"] == 1
        assert result["per_class_errors"].get("dosage", 0) == 0


class TestMWERWeights:
    def test_custom_weights(self):
        custom = {"drug_name": 100.0, "default": 1.0}
        result = medical_wer(
            "took amoxicillin",
            "took warfarin",
            classifier=_drug_classifier,
            weights=custom,
        )
        # weighted_errors = 100.0 (1 drug error * weight 100)
        # weighted_total = 1.0 (default for "took") + 100.0 (drug)
        assert result["weighted_errors"] == 100.0
        assert result["weighted_total"] == pytest.approx(101.0)

    def test_missing_default_raises(self):
        bad_weights = {"drug_name": 10.0}  # no "default" key
        with pytest.raises(ValueError, match="default"):
            medical_wer(
                "took amoxicillin",
                "took warfarin",
                classifier=_drug_classifier,
                weights=bad_weights,
            )

    def test_default_weights_have_default(self):
        # Sanity check: the shipped DEFAULT_WEIGHTS has "default"
        assert "default" in DEFAULT_WEIGHTS


class TestMWERReturnShape:
    def test_returns_required_keys(self):
        result = medical_wer(
            "took amoxicillin",
            "took warfarin",
            classifier=_drug_classifier,
        )
        for key in (
            "mwer",
            "weighted_errors",
            "weighted_total",
            "per_class_errors",
            "per_class_total",
        ):
            assert key in result
