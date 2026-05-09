"""Tests for HL.HF-3b Time-to-Sign Distribution."""

from __future__ import annotations

from datetime import datetime, timedelta

import pytest

from avt_metrics_ref import time_to_sign_distribution
from avt_metrics_ref.hl.time_to_sign import TimeToSignDistribution

_BASE = datetime(2026, 5, 9, 10, 0)


def _ev(seconds_to_sign, word_count=100):
    return {
        "generated_at": _BASE,
        "approved_at": _BASE + timedelta(seconds=seconds_to_sign),
        "word_count": word_count,
    }


def test_distribution_basics():
    """Three notes at 30s, 60s, 90s → median 60, p5 ~31, p90 ~87."""
    events = [_ev(30), _ev(60), _ev(90)]
    result = time_to_sign_distribution(events)
    assert isinstance(result, TimeToSignDistribution)
    assert result.n_notes == 3
    assert result.median_seconds == pytest.approx(60.0)


def test_per_word_normalisation():
    """TTS_norm = TTS / word_count. 60s / 100 words = 0.6 s/word."""
    events = [_ev(60, word_count=100)]
    result = time_to_sign_distribution(events)
    assert result.median_seconds_per_word == pytest.approx(0.6)


def test_rubber_stamp_flag_default_threshold():
    """A 100-word note signed in 30s → 0.3 s/word, below 0.5 default → flagged."""
    events = [_ev(30, word_count=100), _ev(60, word_count=100)]
    result = time_to_sign_distribution(events)
    assert result.n_rubber_stamp_flag == 1
    assert result.rubber_stamp_pct == pytest.approx(50.0)


def test_rubber_stamp_threshold_overridable():
    """Caller can tighten or relax the rubber-stamp threshold."""
    events = [_ev(40, word_count=100)]  # 0.4 s/word
    relaxed = time_to_sign_distribution(events, rubber_stamp_threshold_s_per_word=0.3)
    assert relaxed.n_rubber_stamp_flag == 0
    strict = time_to_sign_distribution(events, rubber_stamp_threshold_s_per_word=0.5)
    assert strict.n_rubber_stamp_flag == 1


def test_very_fast_long_note_flag():
    """A 300-word note signed in 3s → very-fast on a long note."""
    events = [_ev(3, word_count=300)]
    result = time_to_sign_distribution(events)
    assert result.n_very_fast_long_note == 1


def test_very_fast_only_fires_on_long_notes():
    """A 50-word note signed in 3s should NOT trigger the very-fast-long flag
    because the note is short. (It will still trigger the rubber-stamp flag
    via the per-word threshold.)"""
    events = [_ev(3, word_count=50)]
    result = time_to_sign_distribution(events)
    assert result.n_very_fast_long_note == 0


def test_p5_picks_up_lower_tail():
    """Distribution percentiles work — p5 sits below the median."""
    # Mostly slow signing, with a couple of very fast outliers.
    events = [_ev(s, word_count=100) for s in [120, 100, 90, 80, 70, 60, 50, 40, 5, 3]]
    result = time_to_sign_distribution(events)
    assert result.p5_seconds < result.median_seconds


def test_approval_before_generation_raises():
    bad = {
        "generated_at": _BASE + timedelta(seconds=10),
        "approved_at": _BASE,
        "word_count": 50,
    }
    with pytest.raises(ValueError, match="precedes generated_at"):
        time_to_sign_distribution([bad])


def test_zero_word_count_raises():
    bad = {
        "generated_at": _BASE,
        "approved_at": _BASE + timedelta(seconds=60),
        "word_count": 0,
    }
    with pytest.raises(ValueError, match="word_count must be positive"):
        time_to_sign_distribution([bad])


def test_empty_events_raise():
    with pytest.raises(ValueError, match="at least one"):
        time_to_sign_distribution([])
