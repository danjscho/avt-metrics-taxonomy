"""Tests for HL.HF-1 Edit Rate."""

from __future__ import annotations

import pytest

from avt_metrics_ref import edit_rate
from avt_metrics_ref.hl.edit_rate import EditRateResult


def test_basic_aggregate_rate():
    """4 notes, 3 edited → 75% ER."""
    events = [
        {"edited": True},
        {"edited": False},
        {"edited": True},
        {"edited": True},
    ]
    result = edit_rate(events)
    assert isinstance(result, EditRateResult)
    assert result.n_notes == 4
    assert result.n_edited == 3
    assert result.edit_rate_pct == pytest.approx(75.0)


def test_no_severity_no_breakdown():
    """Without edit_severity keys, severity-stratified rates are None."""
    events = [{"edited": True}, {"edited": False}]
    result = edit_rate(events)
    assert result.safety_critical_rate_pct is None
    assert result.stylistic_rate_pct is None


def test_severity_stratified_rates():
    """Safety-critical and stylistic rates pulled out of severity field."""
    events = [
        {"edited": True, "edit_severity": "safety_critical"},
        {"edited": True, "edit_severity": "clinically_meaningful"},
        {"edited": True, "edit_severity": "stylistic"},
        {"edited": False},
    ]
    result = edit_rate(events)
    # 3/4 substantive (every "edited:True" counts toward headline ER)
    assert result.edit_rate_pct == pytest.approx(75.0)
    assert result.safety_critical_rate_pct == pytest.approx(25.0)  # 1/4
    assert result.stylistic_rate_pct == pytest.approx(25.0)  # 1/4


def test_per_clinician_breakdown():
    """clinician_id key drives per-clinician ER."""
    events = [
        {"edited": True, "clinician_id": "A"},
        {"edited": False, "clinician_id": "A"},
        {"edited": True, "clinician_id": "B"},
        {"edited": True, "clinician_id": "B"},
    ]
    result = edit_rate(events)
    assert result.by_clinician["A"] == pytest.approx(50.0)
    assert result.by_clinician["B"] == pytest.approx(100.0)


def test_no_baseline_classification():
    """Without baseline_pct, we either say 'inadequate-review' (ER < 30%
    in early deployment) or 'no-baseline-supplied'."""
    high_er = edit_rate([{"edited": True}, {"edited": True}, {"edited": False}])  # 67%
    assert high_er.classification == "no-baseline-supplied"

    low_er = edit_rate(
        [{"edited": False}] * 9 + [{"edited": True}]  # 10%
    )
    assert low_er.classification == "inadequate-review"


def test_baseline_meets():
    """Current ER close to baseline → meets-baseline."""
    events = [{"edited": True}] * 6 + [{"edited": False}] * 4  # 60% ER
    result = edit_rate(events, baseline_pct=65.0)
    assert result.classification == "meets-baseline"


def test_baseline_complacency_alert():
    """Drop > 15pp from baseline triggers complacency-alert."""
    events = [{"edited": True}] * 4 + [{"edited": False}] * 6  # 40% ER
    result = edit_rate(events, baseline_pct=60.0)  # drop = 20pp
    assert result.classification == "complacency-alert"


def test_baseline_pause_trigger():
    """ER < 50% of baseline triggers pause."""
    events = [{"edited": True}] * 2 + [{"edited": False}] * 8  # 20% ER
    result = edit_rate(events, baseline_pct=50.0)  # 20% < 25% (50% of 50%)
    assert result.classification == "pause-trigger"


def test_empty_events_raise():
    with pytest.raises(ValueError, match="at least one"):
        edit_rate([])
