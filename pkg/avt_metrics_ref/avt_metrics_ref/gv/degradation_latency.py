"""GV.SG-3 Performance Degradation Detection Latency.

Formal Definition (catalogue):

  Detection Latency = t_detection - t_degradation_onset

Reports per-event latency plus a distribution-level summary across all
detected drift events. Catalogue target: detection within 4 weeks of
onset for clinically significant degradation.

The metric assumes the caller has already done the upstream work of
identifying ``(onset, detection)`` event pairs via a sequential drift
detector (CUSUM, Page-Hinkley, etc. — out of scope for this library).
This function operationalises only the *latency* computation, the
distribution summary, and the threshold-met flag.
"""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import NamedTuple

import numpy as np


class LatencyEvent(NamedTuple):
    """Per-event latency breakdown.

    Attributes
    ----------
    onset : datetime
    detection : datetime
    latency : timedelta
    latency_days : float
        Convenience field — ``latency.total_seconds() / 86400``.
    """

    onset: datetime
    detection: datetime
    latency: timedelta
    latency_days: float


class LatencyResult(NamedTuple):
    """Aggregate result across a set of (onset, detection) event pairs.

    Attributes
    ----------
    events : list[LatencyEvent]
    n_events : int
    median_days : float
    p90_days : float
        90th percentile latency in days.
    max_days : float
    target_days : float
        Catalogue target (default 28; override for local calibration).
    pct_within_target : float
        Percentage of events detected within ``target_days``.
    meets_target : bool
        True iff ``pct_within_target >= target_pct_within``.
    target_pct_within : float
    """

    events: list[LatencyEvent]
    n_events: int
    median_days: float
    p90_days: float
    max_days: float
    target_days: float
    pct_within_target: float
    meets_target: bool
    target_pct_within: float


# Catalogue target: detection within 4 weeks of onset.
_DEFAULT_TARGET_DAYS = 28.0
# Calibration starting point: at least 80% of detected drift events should
# fall within the target window. Override for local calibration per the
# Calibration & Context principle. Documented as a starting point, not
# externally cited — the catalogue's target is per-event, not on
# distribution; the 80% bar is a proposed library default for the
# distribution-level summary.
_DEFAULT_TARGET_PCT_WITHIN = 80.0


def degradation_detection_latency(
    onset_timestamps: list[datetime],
    detection_timestamps: list[datetime],
    *,
    target_days: float = _DEFAULT_TARGET_DAYS,
    target_pct_within: float = _DEFAULT_TARGET_PCT_WITHIN,
) -> LatencyResult:
    """Compute Performance Degradation Detection Latency (GV.SG-3).

    Parameters
    ----------
    onset_timestamps : list of datetime
        Per-event time of degradation onset (as identified by the
        upstream drift-detection infrastructure or — for retrospective
        analysis — by the post-hoc investigation that confirmed when
        the degradation actually started).
    detection_timestamps : list of datetime
        Per-event time of detection (when the monitoring system raised
        the alert). Must align positionally with ``onset_timestamps``;
        each detection must be ``>=`` its corresponding onset.
    target_days : float, default 28
        Per-event target latency in days. Catalogue target is "detection
        within 4 weeks of onset for clinically significant degradation".
    target_pct_within : float, default 80
        Distribution-level threshold: the percentage of events that must
        fall within ``target_days`` for the metric to be classified as
        meeting target. Library default — calibrate locally.

    Returns
    -------
    LatencyResult
        Per-event events, distribution summaries (median / p90 / max in
        days), and a meets-target flag.

    Raises
    ------
    ValueError
        If the two lists differ in length, if either is empty, or if
        any detection precedes its onset.

    Examples
    --------
    >>> from datetime import datetime
    >>> onsets = [datetime(2026, 1, 1), datetime(2026, 2, 1)]
    >>> detections = [datetime(2026, 1, 8), datetime(2026, 3, 5)]
    >>> result = degradation_detection_latency(onsets, detections)
    >>> result.n_events
    2
    >>> round(result.median_days, 1) > 0
    True
    """
    if len(onset_timestamps) != len(detection_timestamps):
        raise ValueError(
            f"onset_timestamps and detection_timestamps must be the same length; "
            f"got {len(onset_timestamps)} and {len(detection_timestamps)}"
        )
    if not onset_timestamps:
        raise ValueError("at least one (onset, detection) event pair is required")

    events: list[LatencyEvent] = []
    for onset, detection in zip(onset_timestamps, detection_timestamps):
        if detection < onset:
            raise ValueError(
                f"detection ({detection.isoformat()}) precedes onset "
                f"({onset.isoformat()}); each detection must be >= its onset"
            )
        latency = detection - onset
        events.append(
            LatencyEvent(
                onset=onset,
                detection=detection,
                latency=latency,
                latency_days=latency.total_seconds() / 86400.0,
            )
        )

    days_array = np.array([e.latency_days for e in events])
    median_days = float(np.median(days_array))
    p90_days = float(np.percentile(days_array, 90))
    max_days = float(np.max(days_array))

    within = np.sum(days_array <= target_days)
    pct_within = float(within / len(days_array) * 100.0)
    meets_target = pct_within >= target_pct_within

    return LatencyResult(
        events=events,
        n_events=len(events),
        median_days=median_days,
        p90_days=p90_days,
        max_days=max_days,
        target_days=target_days,
        pct_within_target=pct_within,
        meets_target=meets_target,
        target_pct_within=target_pct_within,
    )
