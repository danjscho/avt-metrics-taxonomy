"""Tests for HL.HF-3a Review-Before-Signing Rate."""

from __future__ import annotations

import pytest

from avt_metrics_ref import review_before_signing_rate
from avt_metrics_ref.hl.review_before_signing import ReviewBeforeSigningResult


def _ev(word_count=100, edits=0, scrolls=0, dwell=0.0, clinician=None):
    """Convenience event builder."""
    e = {
        "word_count": word_count,
        "edit_events": edits,
        "scroll_events": scrolls,
        "dwell_seconds": dwell,
    }
    if clinician is not None:
        e["clinician_id"] = clinician
    return e


def test_edit_event_counts_as_reviewed():
    """A note with any edit event is reviewed regardless of dwell time."""
    events = [_ev(edits=1, dwell=0)]
    result = review_before_signing_rate(events)
    assert isinstance(result, ReviewBeforeSigningResult)
    assert result.n_reviewed == 1
    assert result.rbs_pct == pytest.approx(100.0)


def test_scroll_event_counts_as_reviewed():
    events = [_ev(scrolls=1, dwell=0)]
    result = review_before_signing_rate(events)
    assert result.n_reviewed == 1


def test_dwell_above_t_min_counts_as_reviewed():
    """T_min for a 100-word note = max(15, 3) = 15s. 16s passes."""
    events = [_ev(word_count=100, dwell=16.0)]
    result = review_before_signing_rate(events)
    assert result.n_reviewed == 1


def test_dwell_below_t_min_not_reviewed():
    """T_min for a 100-word note = 15s. 14s fails — no other signals."""
    events = [_ev(word_count=100, dwell=14.0)]
    result = review_before_signing_rate(events)
    assert result.n_reviewed == 0


def test_t_min_scales_with_long_notes():
    """T_min for a 1000-word note = 3 × 1000/100 = 30s. 16s now fails."""
    events = [_ev(word_count=1000, dwell=16.0)]
    result = review_before_signing_rate(events)
    assert result.n_reviewed == 0  # 16 < 30


def test_t_min_floor_for_short_notes():
    """T_min floor is 15s; a 50-word note still needs 15s, not 1.5s."""
    short_dwell = [_ev(word_count=50, dwell=2.0)]
    assert review_before_signing_rate(short_dwell).n_reviewed == 0
    long_dwell = [_ev(word_count=50, dwell=16.0)]
    assert review_before_signing_rate(long_dwell).n_reviewed == 1


def test_meets_target_band():
    """RBS ≥ 95% → meets-target."""
    events = [_ev(edits=1) for _ in range(19)] + [_ev(dwell=0)]  # 95%
    result = review_before_signing_rate(events)
    assert result.rbs_pct == pytest.approx(95.0)
    assert result.classification == "meets-target"


def test_below_target_band():
    """RBS in 85–95% range → below-target."""
    events = [_ev(edits=1) for _ in range(9)] + [_ev(dwell=0)]  # 90%
    result = review_before_signing_rate(events)
    assert result.classification == "below-target"


def test_pause_trigger_band():
    """RBS < 85% → pause-trigger."""
    events = [_ev(edits=1) for _ in range(8)] + [_ev(dwell=0)] * 2  # 80%
    result = review_before_signing_rate(events)
    assert result.classification == "pause-trigger"


def test_per_clinician_breakdown():
    events = [
        _ev(edits=1, clinician="A"),
        _ev(edits=1, clinician="A"),
        _ev(dwell=0, clinician="B"),
        _ev(edits=1, clinician="B"),
    ]
    result = review_before_signing_rate(events)
    assert result.by_clinician["A"] == pytest.approx(100.0)
    assert result.by_clinician["B"] == pytest.approx(50.0)


def test_custom_thresholds():
    """Caller can override the NAS 95/85 thresholds."""
    events = [_ev(edits=1) for _ in range(8)] + [_ev(dwell=0)] * 2  # 80%
    # With a stricter 99/90 calibration → still pause-trigger
    strict = review_before_signing_rate(events, target_pct=99, pause_threshold_pct=90)
    assert strict.classification == "pause-trigger"
    # With a relaxed 70/60 calibration → meets-target
    relaxed = review_before_signing_rate(events, target_pct=70, pause_threshold_pct=60)
    assert relaxed.classification == "meets-target"


def test_empty_events_raise():
    with pytest.raises(ValueError, match="at least one"):
        review_before_signing_rate([])
