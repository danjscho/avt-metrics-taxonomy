"""TP.WB-2 Integration Error Rate.

Formal Definition (catalogue):

  IER = (N_failed + N_partial + N_degraded) / N_total
  SLA target: IER < 0.001

The catalogue mandates per-error-type reporting (failed / partial /
degraded as separate sub-rates), per-EPR stratification, and severity
classification (critical / moderate / benign). This library returns
all four cuts so the headline IER is reported alongside the failure-
pattern breakdown the catalogue requires.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from collections.abc import Iterable, Mapping
from typing import Any, NamedTuple

# Catalogue SLA target (from the Formal Definition); per-error-type
# starting points proposed in v3.7. Override per the Calibration & Context
# principle.
_DEFAULT_SLA_TARGET = 0.001


class IntegrationErrorBreakdown(NamedTuple):
    """Per-error-type sub-rate.

    Attributes
    ----------
    n : int
        Count of events at this error class.
    rate : float
        ``n / total`` (proportion, not percent).
    """

    n: int
    rate: float


class IntegrationErrorRateResult(NamedTuple):
    """Aggregate IER + per-error-type / per-severity / per-EPR breakdown.

    Attributes
    ----------
    n_total : int
        Total write-back attempts.
    n_errors : int
        ``n_failed + n_partial + n_degraded``.
    ier : float
        Aggregate IER (proportion in [0, 1]).
    by_error_type : dict[str, IntegrationErrorBreakdown]
        Per-error-type breakdown for ``"failed"``, ``"partial"``,
        ``"degraded"``.
    n_critical : int
        Count of error events classified as ``critical`` severity (the
        safety leading indicator). Catalogue zero-tolerance.
    n_moderate : int
    n_benign : int
    by_epr : dict[str, float]
        Per-EPR IER (when ``epr_system`` was supplied on events). Empty
        dict otherwise.
    classification : str
        One of ``"meets-sla"`` (IER ≤ target AND no critical events),
        ``"alert-rate"`` (IER > target but no critical events),
        ``"escalation-critical"`` (any critical-class event detected, per
        catalogue's "alert on any critical-class event"), or
        ``"pause-trigger"`` (IER > 5 × target).
    sla_target : float
    """

    n_total: int
    n_errors: int
    ier: float
    by_error_type: dict[str, IntegrationErrorBreakdown]
    n_critical: int
    n_moderate: int
    n_benign: int
    by_epr: dict[str, float]
    classification: str
    sla_target: float


_ERROR_TYPES = ("failed", "partial", "degraded")
_SEVERITIES = ("critical", "moderate", "benign")


def integration_error_rate(
    events: Iterable[Mapping[str, Any]],
    *,
    success_key: str = "success",
    error_type_key: str = "error_type",
    severity_key: str = "severity",
    epr_system_key: str | None = "epr_system",
    sla_target: float = _DEFAULT_SLA_TARGET,
) -> IntegrationErrorRateResult:
    """Compute Integration Error Rate (TP.WB-2).

    Parameters
    ----------
    events : iterable of mappings
        One event per write-back attempt. Required key:

        - ``success`` (bool) — True if the write-back was a complete,
          conformant target-EPR record.

        Required when ``success`` is False:

        - ``error_type`` — one of ``"failed"`` / ``"partial"`` /
          ``"degraded"``. Other values raise.
        - ``severity`` — one of ``"critical"`` / ``"moderate"`` /
          ``"benign"``.

        Optional:

        - ``epr_system`` — string identifier (EMIS, SystmOne, Epic, …).
          When supplied, drives the per-EPR breakdown the catalogue
          mandates.
    success_key, error_type_key, severity_key, epr_system_key : str
        Override default key names.
    sla_target : float, default 0.001
        Catalogue SLA target. Override for local calibration.

    Returns
    -------
    IntegrationErrorRateResult

    Raises
    ------
    ValueError
        If no events supplied; if a failed event has an unknown
        error_type or severity; if the events imply ``n_total == 0``.

    Examples
    --------
    >>> events = [
    ...     {"success": True},
    ...     {"success": True},
    ...     {"success": False, "error_type": "partial", "severity": "moderate"},
    ... ]
    >>> result = integration_error_rate(events)
    >>> result.ier
    0.3333333333333333
    >>> result.by_error_type["partial"].n
    1
    """
    events_list = list(events)
    if not events_list:
        raise ValueError("at least one event is required")

    n_total = len(events_list)
    error_counts: Counter[str] = Counter()
    severity_counts: Counter[str] = Counter()
    by_epr_counts: dict[str, list[int]] = defaultdict(lambda: [0, 0])  # [errors, total]

    for ev in events_list:
        success = bool(ev.get(success_key, False))
        if epr_system_key:
            epr = ev.get(epr_system_key)
            if epr is not None:
                by_epr_counts[str(epr)][1] += 1
                if not success:
                    by_epr_counts[str(epr)][0] += 1
        if success:
            continue
        et = ev.get(error_type_key)
        if et not in _ERROR_TYPES:
            raise ValueError(
                f"event with success=False must declare error_type in "
                f"{_ERROR_TYPES}; got {et!r}"
            )
        sev = ev.get(severity_key)
        if sev not in _SEVERITIES:
            raise ValueError(
                f"event with success=False must declare severity in "
                f"{_SEVERITIES}; got {sev!r}"
            )
        error_counts[et] += 1
        severity_counts[sev] += 1

    n_errors = sum(error_counts.values())
    ier = n_errors / n_total

    by_error_type = {
        et: IntegrationErrorBreakdown(n=error_counts.get(et, 0), rate=error_counts.get(et, 0) / n_total)
        for et in _ERROR_TYPES
    }
    by_epr = {
        epr: errs / total for epr, (errs, total) in by_epr_counts.items() if total > 0
    }

    n_critical = severity_counts.get("critical", 0)
    n_moderate = severity_counts.get("moderate", 0)
    n_benign = severity_counts.get("benign", 0)

    if n_critical > 0:
        classification = "escalation-critical"
    elif ier > 5 * sla_target:
        classification = "pause-trigger"
    elif ier > sla_target:
        classification = "alert-rate"
    else:
        classification = "meets-sla"

    return IntegrationErrorRateResult(
        n_total=n_total,
        n_errors=n_errors,
        ier=ier,
        by_error_type=by_error_type,
        n_critical=n_critical,
        n_moderate=n_moderate,
        n_benign=n_benign,
        by_epr=by_epr,
        classification=classification,
        sla_target=sla_target,
    )
