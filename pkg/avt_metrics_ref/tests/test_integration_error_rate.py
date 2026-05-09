"""Tests for TP.WB-2 Integration Error Rate."""

from __future__ import annotations

import pytest

from avt_metrics_ref import integration_error_rate
from avt_metrics_ref.tp.wb.integration_error_rate import (
    IntegrationErrorRateResult,
)


def _err(error_type, severity, epr=None):
    e = {"success": False, "error_type": error_type, "severity": severity}
    if epr is not None:
        e["epr_system"] = epr
    return e


def _ok(epr=None):
    return {"success": True, "epr_system": epr} if epr else {"success": True}


def test_no_errors_meets_sla():
    """All successes → 0% IER, meets-sla."""
    events = [_ok() for _ in range(1000)]
    result = integration_error_rate(events)
    assert isinstance(result, IntegrationErrorRateResult)
    assert result.ier == pytest.approx(0.0)
    assert result.classification == "meets-sla"


def test_per_error_type_breakdown():
    """Three error types each appear in their own sub-rate."""
    events = (
        [_ok() for _ in range(997)]
        + [_err("failed", "moderate")]
        + [_err("partial", "moderate")]
        + [_err("degraded", "benign")]
    )
    result = integration_error_rate(events)
    assert result.n_total == 1000
    assert result.n_errors == 3
    assert result.ier == pytest.approx(0.003)
    assert result.by_error_type["failed"].n == 1
    assert result.by_error_type["partial"].n == 1
    assert result.by_error_type["degraded"].n == 1


def test_critical_event_triggers_escalation():
    """Catalogue: any critical-class event → escalation, regardless of overall rate."""
    events = [_ok() for _ in range(999)] + [_err("partial", "critical")]
    result = integration_error_rate(events)
    assert result.n_critical == 1
    # IER is a tiny 0.001 (= SLA target), but the critical event escalates
    assert result.classification == "escalation-critical"


def test_alert_band_above_sla_no_critical():
    """IER between 1× and 5× target with no critical events → alert-rate."""
    events = [_ok() for _ in range(998)] + [_err("partial", "moderate")] * 2
    result = integration_error_rate(events)
    # IER = 2/1000 = 0.002, between target (0.001) and 5× target (0.005)
    assert result.ier == pytest.approx(0.002)
    assert result.classification == "alert-rate"


def test_pause_trigger_at_5x_sla():
    """Catalogue: aggregate IER > 5 × SLA target → pause trigger."""
    events = [_ok() for _ in range(990)] + [_err("partial", "moderate")] * 10
    result = integration_error_rate(events)
    # IER = 0.01 = 10× SLA target
    assert result.classification == "pause-trigger"


def test_per_epr_breakdown():
    """epr_system key drives per-EPR breakdown."""
    events = [
        _ok("emis"),
        _err("failed", "moderate", "emis"),
        _ok("systmone"),
        _ok("systmone"),
    ]
    result = integration_error_rate(events)
    assert result.by_epr["emis"] == pytest.approx(0.5)
    assert result.by_epr["systmone"] == pytest.approx(0.0)


def test_unknown_error_type_raises():
    bad = {"success": False, "error_type": "weird", "severity": "moderate"}
    with pytest.raises(ValueError, match="error_type"):
        integration_error_rate([bad])


def test_unknown_severity_raises():
    bad = {"success": False, "error_type": "failed", "severity": "spicy"}
    with pytest.raises(ValueError, match="severity"):
        integration_error_rate([bad])


def test_failed_event_must_declare_severity():
    """A failed event without a severity raises (not silently treated as benign)."""
    bad = {"success": False, "error_type": "failed"}
    with pytest.raises(ValueError, match="severity"):
        integration_error_rate([bad])


def test_empty_events_raise():
    with pytest.raises(ValueError, match="at least one"):
        integration_error_rate([])


def test_custom_sla_target():
    """Caller can tighten the SLA target — same events, different verdict."""
    events = [_ok() for _ in range(998)] + [_err("partial", "moderate")] * 2
    # 0.002 IER. Default 0.001 → alert-rate. With target 0.005 → meets-sla.
    relaxed = integration_error_rate(events, sla_target=0.005)
    assert relaxed.classification == "meets-sla"
    # With target 0.0001 (10× stricter) → pause-trigger (0.002 > 5 × 0.0001)
    strict = integration_error_rate(events, sla_target=0.0001)
    assert strict.classification == "pause-trigger"
