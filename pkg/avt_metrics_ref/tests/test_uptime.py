"""Tests for GV.OP-5 System Availability / Uptime."""

from __future__ import annotations

import pytest

from avt_metrics_ref import system_availability
from avt_metrics_ref.gv.uptime import AvailabilityResult


def test_perfect_uptime():
    """Zero downtime → 100% availability, meets-target classification."""
    result = system_availability(operational_minutes=10000, down_minutes=0)
    assert isinstance(result, AvailabilityResult)
    assert result.availability_pct == pytest.approx(100.0)
    assert result.classification == "meets-target"
    assert result.effective_availability_pct is None


def test_meets_nas_target():
    """0.2% downtime → 99.8%, meets the NAS 99.5% target."""
    result = system_availability(operational_minutes=10000, down_minutes=20)
    assert result.availability_pct == pytest.approx(99.8)
    assert result.classification == "meets-target"


def test_below_target_band():
    """Availability between 99.0 and 99.5 lands in the warning band."""
    # 99.3% — below 99.5 target, above 99.0 pause threshold
    result = system_availability(operational_minutes=10000, down_minutes=70)
    assert 99.0 <= result.availability_pct < 99.5
    assert result.classification == "below-target"


def test_escalation_band():
    """Availability below 99.0% triggers escalation band."""
    result = system_availability(operational_minutes=10000, down_minutes=200)
    assert result.availability_pct < 99.0
    assert result.classification == "escalation"


def test_degraded_time_lowers_effective_availability():
    """Degraded-time accounting reduces effective availability below raw."""
    result = system_availability(
        operational_minutes=10000, down_minutes=10, degraded_minutes=40
    )
    # Raw: (10000 - 10) / 10000 = 99.9
    # Effective: (10000 - 10 - 40) / 10000 = 99.5
    assert result.availability_pct == pytest.approx(99.9)
    assert result.effective_availability_pct == pytest.approx(99.5)
    # Classification still uses raw availability
    assert result.classification == "meets-target"


def test_zero_operational_window_raises():
    with pytest.raises(ValueError, match="must be positive"):
        system_availability(operational_minutes=0, down_minutes=0)


def test_negative_down_minutes_raises():
    with pytest.raises(ValueError, match="non-negative"):
        system_availability(operational_minutes=100, down_minutes=-1)


def test_down_exceeds_operational_raises():
    with pytest.raises(ValueError, match="cannot exceed"):
        system_availability(operational_minutes=100, down_minutes=200)


def test_degraded_exceeds_up_time_raises():
    with pytest.raises(ValueError, match="cannot exceed"):
        # Up time = 100 - 10 = 90; degraded > up time should fail.
        system_availability(operational_minutes=100, down_minutes=10, degraded_minutes=95)


def test_custom_thresholds_override_defaults():
    """Caller can override the NAS-default 99.5/99.0 thresholds."""
    # 99.7% availability with a stricter custom 99.9% target
    result = system_availability(
        operational_minutes=10000,
        down_minutes=30,
        target_pct=99.9,
        pause_threshold_pct=99.5,
    )
    assert result.availability_pct == pytest.approx(99.7)
    assert result.classification == "below-target"
    assert result.target_pct == 99.9
    assert result.pause_threshold_pct == 99.5
