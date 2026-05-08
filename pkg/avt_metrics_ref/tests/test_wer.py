"""Tests for TP.ASR-1 Word Error Rate."""
from __future__ import annotations

import pytest

from avt_metrics_ref import wer


class TestWERBasics:
    def test_identical_strings_zero_error(self):
        assert wer("the patient", "the patient") == 0.0

    def test_one_substitution(self):
        # 5 reference words, 1 substituted
        result = wer(
            "the patient reports chest pain",
            "the patient reports chess pain",
        )
        assert result == pytest.approx(0.2)

    def test_one_deletion(self):
        # "pain" deleted: 4 ref words, 1 missing
        result = wer("reports chest pain now", "reports chest now")
        assert result == pytest.approx(0.25)

    def test_one_insertion(self):
        # extra word inserted in hypothesis: 3 ref words, 1 insertion
        result = wer("chest pain reported", "chest pain reported promptly")
        assert result == pytest.approx(1 / 3)

    def test_returns_float(self):
        assert isinstance(wer("a b c", "a b d"), float)


class TestWERCorpus:
    def test_corpus_level_macro_average(self):
        refs = ["the cat sat", "the dog ran", "the bird flew"]
        hyps = ["the cat sat", "the dog walked", "the bird flew"]
        # Across the corpus: 9 ref words total, 1 substitution
        # jiwer's wer is a macro average across utterances
        result = wer(refs, hyps)
        assert 0.0 < result < 1.0

    def test_perfect_corpus(self):
        refs = ["the cat sat", "the dog ran"]
        hyps = ["the cat sat", "the dog ran"]
        assert wer(refs, hyps) == 0.0


class TestWERBreakdown:
    def test_breakdown_returns_dict(self):
        result = wer("the patient", "the patient", return_breakdown=True)
        assert isinstance(result, dict)
        assert "wer" in result
        assert "substitutions" in result
        assert "deletions" in result
        assert "insertions" in result
        assert "hits" in result

    def test_breakdown_substitutions(self):
        result = wer(
            "patient reports chest pain",
            "patient reports chess pain",
            return_breakdown=True,
        )
        assert result["substitutions"] == 1
        assert result["deletions"] == 0
        assert result["insertions"] == 0
        assert result["hits"] == 3


class TestWERValidation:
    def test_mixed_str_and_list_raises(self):
        with pytest.raises(TypeError, match="both be"):
            wer("a string", ["a", "list"])

    def test_mixed_list_and_str_raises(self):
        with pytest.raises(TypeError, match="both be"):
            wer(["a", "list"], "a string")
