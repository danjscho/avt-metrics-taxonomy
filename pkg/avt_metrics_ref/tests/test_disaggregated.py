"""Tests for TP.ASR-4 Demographic-Disaggregated WER."""
from __future__ import annotations

import pytest

from avt_metrics_ref import disaggregated_wer


class TestDisaggregatedBasics:
    def test_perfect_no_gap(self):
        samples = [
            {"reference": "the cat sat", "hypothesis": "the cat sat", "group": "A"},
            {"reference": "the dog ran", "hypothesis": "the dog ran", "group": "B"},
        ]
        result = disaggregated_wer(samples)
        assert result["equity_gap"] == 0.0
        assert result["threshold_met"] is True

    def test_gap_breaches_threshold(self):
        samples = [
            {"reference": "the cat sat", "hypothesis": "the cat sat", "group": "A"},
            {"reference": "the cat sat", "hypothesis": "the cat sat", "group": "A"},
            {"reference": "she said hello",
             "hypothesis": "she said yellow", "group": "B"},
        ]
        result = disaggregated_wer(samples, threshold=0.05)
        assert result["equity_gap"] > 0.0
        # B has WER 1/3 ≈ 0.33; A has WER 0; gap > 0.05
        assert result["threshold_met"] is False
        assert result["worst_group"] == "B"
        assert result["best_group"] == "A"

    def test_per_group_sample_sizes(self):
        samples = [
            {"reference": "a b c", "hypothesis": "a b c", "group": "A"},
            {"reference": "d e f", "hypothesis": "d e f", "group": "A"},
            {"reference": "g h i", "hypothesis": "g h j", "group": "B"},
        ]
        result = disaggregated_wer(samples)
        assert result["per_group"]["A"]["n"] == 2
        assert result["per_group"]["B"]["n"] == 1

    def test_aggregate_provided(self):
        samples = [
            {"reference": "a b c", "hypothesis": "a b c", "group": "A"},
            {"reference": "d e f", "hypothesis": "d e g", "group": "B"},
        ]
        result = disaggregated_wer(samples)
        assert "aggregate_wer" in result
        assert 0.0 < result["aggregate_wer"] < 1.0


class TestDisaggregatedConfigurable:
    def test_custom_keys(self):
        samples = [
            {"ref": "the cat sat", "hyp": "the cat sat", "accent": "GB"},
            {"ref": "the cat sat", "hyp": "the cat say", "accent": "US"},
        ]
        result = disaggregated_wer(
            samples, ref_key="ref", hyp_key="hyp", group_key="accent",
        )
        assert "GB" in result["per_group"]
        assert "US" in result["per_group"]

    def test_custom_threshold(self):
        samples = [
            {"reference": "a b c d", "hypothesis": "a b c d", "group": "A"},
            {"reference": "e f g h", "hypothesis": "e f g x", "group": "B"},
        ]
        # B's WER is 0.25 (1/4); use threshold 0.5 to ensure it passes
        result = disaggregated_wer(samples, threshold=0.5)
        assert result["threshold_met"] is True


class TestDisaggregatedEdgeCases:
    def test_empty_samples(self):
        result = disaggregated_wer([])
        assert result["per_group"] == {}
        assert result["equity_gap"] == 0.0
        assert result["worst_group"] is None
        assert result["aggregate_wer"] == 0.0

    def test_missing_key_raises(self):
        samples = [{"reference": "a b c", "hypothesis": "a b c"}]  # no 'group'
        with pytest.raises(KeyError, match="group"):
            disaggregated_wer(samples)

    def test_negative_threshold_raises(self):
        with pytest.raises(ValueError, match="non-negative"):
            disaggregated_wer([], threshold=-0.1)

    def test_single_group(self):
        samples = [
            {"reference": "a b c", "hypothesis": "a b c", "group": "A"},
            {"reference": "d e f", "hypothesis": "d e g", "group": "A"},
        ]
        result = disaggregated_wer(samples)
        assert result["equity_gap"] == 0.0  # only one group → no gap
        assert result["worst_group"] == "A"
        assert result["best_group"] == "A"
