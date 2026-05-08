"""Tests for TP.ASR-10 ASR Confidence Calibration."""
from __future__ import annotations

import pytest

from avt_metrics_ref import asr_confidence_calibration


class TestCalibrationBasics:
    def test_perfect_calibration(self):
        """Confidence == accuracy → ECE near 0."""
        # 100 samples at confidence 0.9, 90 correct → perfect calibration
        confs = [0.9] * 100
        corrs = [1] * 90 + [0] * 10
        result = asr_confidence_calibration(confs, corrs, n_bins=10)
        assert result["ece"] < 0.01

    def test_overconfident_systematic(self):
        """High confidence + low accuracy → high ECE."""
        # All claim 0.9 confidence; only half are correct
        confs = [0.9] * 100
        corrs = [1] * 50 + [0] * 50
        result = asr_confidence_calibration(confs, corrs, n_bins=10)
        assert result["ece"] > 0.3  # gap of 0.4 in the bin

    def test_underconfident_systematic(self):
        """Low confidence + high accuracy → also high ECE."""
        confs = [0.3] * 100
        corrs = [1] * 95 + [0] * 5
        result = asr_confidence_calibration(confs, corrs, n_bins=10)
        assert result["ece"] > 0.5

    def test_mce_captures_worst_bin(self):
        """MCE = max single-bin gap."""
        confs = [0.05] * 50 + [0.95] * 50
        corrs = [1] * 50 + [0] * 50  # bin 0 at gap 0.95, bin 9 at gap 0.95
        result = asr_confidence_calibration(confs, corrs, n_bins=10)
        # MCE should be very high since both extreme bins are maximally wrong
        assert result["mce"] > 0.9


class TestCalibrationPerBin:
    def test_per_bin_count(self):
        confs = [0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95]
        corrs = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
        result = asr_confidence_calibration(confs, corrs, n_bins=10)
        # one sample per bin
        for b in result["per_bin"]:
            assert b["count"] == 1

    def test_empty_bin_has_none_metrics(self):
        # All samples in bin [0.9, 1.0]
        confs = [0.95, 0.99]
        corrs = [1, 1]
        result = asr_confidence_calibration(confs, corrs, n_bins=10)
        # First 9 bins should be empty
        for b in result["per_bin"][:9]:
            assert b["count"] == 0
            assert b["mean_confidence"] is None
            assert b["mean_accuracy"] is None
            assert b["gap"] is None
        # Last bin populated
        assert result["per_bin"][-1]["count"] == 2

    def test_per_bin_range(self):
        confs = [0.5]
        corrs = [1]
        result = asr_confidence_calibration(confs, corrs, n_bins=2)
        # Bin 0: [0, 0.5), Bin 1: [0.5, 1]
        assert result["per_bin"][0]["range"] == (0.0, 0.5)
        assert result["per_bin"][1]["range"] == (0.5, 1.0)


class TestCalibrationValidation:
    def test_mismatched_lengths_raises(self):
        with pytest.raises(ValueError, match="same length"):
            asr_confidence_calibration([0.5, 0.6], [1])

    def test_confidence_out_of_range_raises(self):
        with pytest.raises(ValueError, match=r"\[0, 1\]"):
            asr_confidence_calibration([0.5, 1.5], [1, 0])

    def test_zero_bins_raises(self):
        with pytest.raises(ValueError, match=">= 1"):
            asr_confidence_calibration([0.5], [1], n_bins=0)

    def test_empty_input(self):
        result = asr_confidence_calibration([], [])
        assert result["ece"] == 0.0
        assert result["n"] == 0
