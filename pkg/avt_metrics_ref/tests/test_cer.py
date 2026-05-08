"""Tests for TP.ASR-8 Character Error Rate."""
from __future__ import annotations

import pytest

from avt_metrics_ref import cer


class TestCERBasics:
    def test_identical_strings_zero_error(self):
        assert cer("amoxicillin", "amoxicillin") == 0.0

    def test_one_char_substitution(self):
        # amoxicillin (11 chars) vs amoxycillin (11 chars): 1 char different
        result = cer("amoxicillin", "amoxycillin")
        assert 0.0 < result < 0.2

    def test_returns_float(self):
        assert isinstance(cer("abc", "abd"), float)


class TestCERVsWER:
    def test_cer_lower_than_wer_for_near_miss(self):
        """One char wrong → low CER but high WER (whole word counted as wrong).

        This is the catalogue's claim about why CER complements WER for
        clinical-term near-misses.
        """
        from avt_metrics_ref import wer
        ref = "patient prescribed amoxicillin"
        hyp = "patient prescribed amoxycillin"
        wer_val = wer(ref, hyp)
        cer_val = cer(ref, hyp)
        assert cer_val < wer_val


class TestCERValidation:
    def test_mixed_str_and_list_raises(self):
        with pytest.raises(TypeError, match="both be"):
            cer("a", ["b"])
