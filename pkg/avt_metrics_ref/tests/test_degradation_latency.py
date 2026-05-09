"""Tests for GV.SG-3 Performance Degradation Detection Latency."""

from __future__ import annotations

from datetime import datetime

import pytest

from avt_metrics_ref import degradation_detection_latency
from avt_metrics_ref.gv.degradation_latency import LatencyResult


def test_single_event_latency():
    """One pair: latency = detection - onset, in days."""
    onsets = [datetime(2026, 1, 1)]
    detections = [datetime(2026, 1, 8)]  # 7 days later
    result = degradation_detection_latency(onsets, detections)
    assert isinstance(result, LatencyResult)
    assert result.n_events == 1
    assert result.events[0].latency_days == pytest.approx(7.0)
    assert result.median_days == pytest.approx(7.0)
    assert result.max_days == pytest.approx(7.0)


def test_meets_target_when_all_within_window():
    """All detections within 4 weeks → meets target."""
    onsets = [datetime(2026, 1, 1), datetime(2026, 2, 1), datetime(2026, 3, 1)]
    detections = [
        datetime(2026, 1, 8),  # 7 days
        datetime(2026, 2, 15),  # 14 days
        datetime(2026, 3, 22),  # 21 days
    ]
    result = degradation_detection_latency(onsets, detections)
    assert result.pct_within_target == pytest.approx(100.0)
    assert result.meets_target is True


def test_misses_target_when_distribution_tails():
    """Mostly fast detection but with a 60-day tail event drops the
    pct-within-target below the 80% library default."""
    onsets = [datetime(2026, 1, 1)] * 5
    detections = [
        datetime(2026, 1, 8),
        datetime(2026, 1, 15),
        datetime(2026, 1, 22),
        datetime(2026, 3, 2),  # 60 days — outside target
        datetime(2026, 3, 9),  # 67 days — outside target
    ]
    result = degradation_detection_latency(onsets, detections)
    # 3/5 within 28-day target → 60% < 80% default
    assert result.pct_within_target == pytest.approx(60.0)
    assert result.meets_target is False


def test_p90_picks_up_tail():
    """p90 isolates the tail latency."""
    from datetime import timedelta

    onset = datetime(2026, 1, 1)
    onsets = [onset] * 10
    # 9 fast detections (1 day) + one tail (50 days)
    detections = [onset + timedelta(days=d) for d in [1, 1, 1, 1, 1, 1, 1, 1, 1, 50]]
    result = degradation_detection_latency(onsets, detections)
    # 90th percentile should be much higher than median for this distribution
    assert result.median_days <= 1.5
    assert result.p90_days >= 5.0  # reflects the tail


def test_detection_before_onset_raises():
    onsets = [datetime(2026, 1, 8)]
    detections = [datetime(2026, 1, 1)]
    with pytest.raises(ValueError, match="precedes onset"):
        degradation_detection_latency(onsets, detections)


def test_mismatched_lengths_raise():
    with pytest.raises(ValueError, match="same length"):
        degradation_detection_latency(
            [datetime(2026, 1, 1)], [datetime(2026, 1, 1), datetime(2026, 1, 2)]
        )


def test_empty_input_raises():
    with pytest.raises(ValueError, match="at least one"):
        degradation_detection_latency([], [])


def test_custom_target_days():
    """Caller can override the catalogue default 28-day target."""
    onsets = [datetime(2026, 1, 1)]
    detections = [datetime(2026, 1, 10)]  # 9 days
    # With a 7-day target, this misses
    strict = degradation_detection_latency(onsets, detections, target_days=7)
    assert strict.target_days == 7
    assert strict.pct_within_target == pytest.approx(0.0)
    # With a 14-day target, it meets
    relaxed = degradation_detection_latency(onsets, detections, target_days=14)
    assert relaxed.pct_within_target == pytest.approx(100.0)


def test_custom_target_pct_within():
    """Caller can override the 80% library default for the distribution-
    level threshold."""
    onsets = [datetime(2026, 1, 1)] * 4
    detections = [
        datetime(2026, 1, 8),
        datetime(2026, 1, 15),
        datetime(2026, 1, 22),
        datetime(2026, 3, 1),  # outside 28-day target
    ]
    # 3/4 = 75% within target; default 80% → fails
    default = degradation_detection_latency(onsets, detections)
    assert default.meets_target is False
    # With a 70% bar → passes
    permissive = degradation_detection_latency(
        onsets, detections, target_pct_within=70.0
    )
    assert permissive.meets_target is True
