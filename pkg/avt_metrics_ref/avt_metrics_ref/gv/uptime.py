"""GV.OP-5 System Availability / Uptime.

Formal Definition (catalogue):

  A = (T_operational - T_down) / T_operational × 100

Effective availability incorporates degraded-performance time:

  A_eff = (T_op - T_down - T_degraded) / T_op × 100

NAS Day Zero SPI threshold: ≥99.5% during consultation hours.
"""

from __future__ import annotations

from typing import NamedTuple

# NAS Day Zero SPI thresholds (percent points). Documented in the catalogue's
# Threshold Reference; encoded here so the function returns a structured
# classification alongside the raw number.
_NAS_TARGET = 99.5
_NAS_PAUSE_BELOW = 99.0  # below this, escalation to deployer-side governance


class AvailabilityResult(NamedTuple):
    """Bundle of per-window availability values + NAS classification.

    Attributes
    ----------
    availability_pct : float
        Raw availability as a percentage in [0, 100].
    effective_availability_pct : float | None
        Availability when degraded time is subtracted from operational
        time. None if no ``degraded_minutes`` was supplied (degraded-time
        accounting is optional).
    classification : str
        One of:

        - ``"meets-target"`` (≥ 99.5%)
        - ``"below-target"`` (99.0% – 99.5%; warning band)
        - ``"escalation"`` (< 99.0%; pause-trigger band)
    target_pct : float
    pause_threshold_pct : float
    """

    availability_pct: float
    effective_availability_pct: float | None
    classification: str
    target_pct: float
    pause_threshold_pct: float


def system_availability(
    operational_minutes: float,
    down_minutes: float,
    *,
    degraded_minutes: float | None = None,
    target_pct: float = _NAS_TARGET,
    pause_threshold_pct: float = _NAS_PAUSE_BELOW,
) -> AvailabilityResult:
    """Compute System Availability / Uptime (GV.OP-5).

    Parameters
    ----------
    operational_minutes : float
        Total minutes the system was supposed to be available (e.g. total
        consultation-hour minutes in the reporting window).
    down_minutes : float
        Minutes during the operational window when the system was down
        (planned + unplanned). Must be ``<= operational_minutes``.
    degraded_minutes : float, optional
        Minutes during the operational window when the system was up but
        operating in a degraded state (slow inference, partial feature
        availability, etc.). When supplied, populates the
        ``effective_availability_pct`` field. Must be
        ``<= operational_minutes - down_minutes``.
    target_pct : float, default 99.5
        Percentage threshold for "meets target" classification. NAS Day
        Zero SPI sets this at 99.5; override only if your local
        calibration justifies a different bar (cf. the Calibration &
        Context principle).
    pause_threshold_pct : float, default 99.0
        Percentage threshold below which the metric should escalate to
        deployer-side governance.

    Returns
    -------
    AvailabilityResult
        The raw availability percentage, the optional degraded-aware
        effective availability, and a NAS-band classification string.

    Raises
    ------
    ValueError
        If ``operational_minutes`` is non-positive, or if down /
        degraded minutes exceed the available operational window.

    Examples
    --------
    >>> result = system_availability(operational_minutes=10000, down_minutes=20)
    >>> round(result.availability_pct, 2)
    99.8
    >>> result.classification
    'meets-target'
    """
    if operational_minutes <= 0:
        raise ValueError(
            f"operational_minutes must be positive; got {operational_minutes}"
        )
    if down_minutes < 0:
        raise ValueError(f"down_minutes must be non-negative; got {down_minutes}")
    if down_minutes > operational_minutes:
        raise ValueError(
            f"down_minutes ({down_minutes}) cannot exceed operational_minutes "
            f"({operational_minutes})"
        )

    availability_pct = (operational_minutes - down_minutes) / operational_minutes * 100.0

    effective_pct: float | None = None
    if degraded_minutes is not None:
        if degraded_minutes < 0:
            raise ValueError(
                f"degraded_minutes must be non-negative; got {degraded_minutes}"
            )
        up_minutes = operational_minutes - down_minutes
        if degraded_minutes > up_minutes:
            raise ValueError(
                f"degraded_minutes ({degraded_minutes}) cannot exceed up time "
                f"({up_minutes})"
            )
        effective_pct = (
            (operational_minutes - down_minutes - degraded_minutes)
            / operational_minutes
            * 100.0
        )

    # Band classification uses raw availability per the NAS SPI definition;
    # effective availability is for diagnostic context, not the SPI gate.
    if availability_pct >= target_pct:
        classification = "meets-target"
    elif availability_pct >= pause_threshold_pct:
        classification = "below-target"
    else:
        classification = "escalation"

    return AvailabilityResult(
        availability_pct=availability_pct,
        effective_availability_pct=effective_pct,
        classification=classification,
        target_pct=target_pct,
        pause_threshold_pct=pause_threshold_pct,
    )
