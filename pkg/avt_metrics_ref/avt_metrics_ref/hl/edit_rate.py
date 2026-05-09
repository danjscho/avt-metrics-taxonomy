"""HL.HF-1 Edit Rate (% Notes Edited).

Formal Definition (catalogue):

  ER(t) = |N_edited(t)| / |N_total(t)|

Caller supplies a per-note event stream; library aggregates over the
period and returns:

- The aggregate substantive-edit rate.
- A per-clinician breakdown (when ``clinician_id`` is supplied).
- Optional severity-stratified rates: ``substantive`` (default headline
  metric, reported as ER), ``safety_critical`` (leading indicator
  reported separately), and ``stylistic`` (excluded from headline ER
  but reported for completeness).

The catalogue's complacency signal (sustained drop > 15pp over 4 weeks)
and pause trigger (ER < 50% of baseline for 4 weeks) are deployment-
context-dependent trajectories — operationalising them requires a
baseline window the library does not store. Compute baseline once
across a 4-week sample and pass it back as ``baseline_pct`` to get the
classification.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from collections.abc import Iterable, Mapping
from typing import Any, NamedTuple

# Catalogue starting points. Override per the Calibration & Context principle.
_DAY_ZERO_BASELINE_FLOOR_PCT = 30.0  # ER below 30% in week 1 = inadequate-review flag
_DAY_ZERO_BASELINE_CEILING_PCT = 80.0
_PAUSE_FRACTION_OF_BASELINE = 0.5  # ER < 50% of baseline for 4 weeks
_COMPLACENCY_DROP_PP = 15.0  # > 15pp drop sustained ≥ 4 weeks


class EditRateResult(NamedTuple):
    """Aggregate edit-rate breakdown.

    Attributes
    ----------
    n_notes : int
    n_edited : int
        Notes with at least one substantive edit (default classification).
    edit_rate_pct : float
        ``n_edited / n_notes * 100``. Headline ER per the catalogue's
        Operational Specification (substantive edits only).
    safety_critical_rate_pct : float | None
        ``n_safety_critical / n_notes * 100`` when severity classification
        was supplied; otherwise ``None``.
    stylistic_rate_pct : float | None
        ``n_stylistic / n_notes * 100`` when severity classification was
        supplied; otherwise ``None``.
    by_clinician : dict[str, float]
        Per-clinician headline ER (in %) when ``clinician_id`` is in the
        events; empty dict otherwise.
    classification : str
        One of ``"meets-day-zero-baseline"`` (30–80% in early-deployment
        sense, OR a healthy stable-state distance from the supplied
        baseline), ``"inadequate-review"`` (ER < 30% suggests clinicians
        aren't reviewing), ``"pause-trigger"`` (ER fell below 50% of the
        supplied ``baseline_pct``, sustained-window analysis is the
        caller's responsibility), or ``"no-baseline-supplied"``.
    """

    n_notes: int
    n_edited: int
    edit_rate_pct: float
    safety_critical_rate_pct: float | None
    stylistic_rate_pct: float | None
    by_clinician: dict[str, float]
    classification: str


def edit_rate(
    events: Iterable[Mapping[str, Any]],
    *,
    edited_key: str = "edited",
    severity_key: str | None = "edit_severity",
    clinician_key: str | None = "clinician_id",
    baseline_pct: float | None = None,
) -> EditRateResult:
    """Compute Edit Rate (HL.HF-1).

    Parameters
    ----------
    events : iterable of mappings
        One event per AI-generated note. Required key: ``edited``
        (boolean). Optional keys: ``edit_severity`` (one of
        ``"safety_critical"`` / ``"clinically_meaningful"`` /
        ``"stylistic"``; absence treated as substantive but unclassified
        so the headline ER counts the note); ``clinician_id`` (any
        hashable, used for per-clinician breakdown).
    edited_key, severity_key, clinician_key : str
        Override the default key names.
    baseline_pct : float, optional
        Per-clinician (or per-deployment) baseline ER from the first
        4 weeks of live use, in percent. When supplied, classification
        compares the current ER to the baseline; when None,
        classification reports ``"no-baseline-supplied"`` and the caller
        should compute a baseline from the first 4 weeks of data.

    Returns
    -------
    EditRateResult
        Aggregate ER, optional severity-stratified rates, per-clinician
        breakdown, and a NAS-band classification.

    Raises
    ------
    ValueError
        If no events supplied.

    Examples
    --------
    >>> events = [
    ...     {"edited": True, "edit_severity": "clinically_meaningful"},
    ...     {"edited": False},
    ...     {"edited": True, "edit_severity": "stylistic"},
    ...     {"edited": True, "edit_severity": "safety_critical"},
    ... ]
    >>> result = edit_rate(events)
    >>> result.n_notes
    4
    """
    events_list = list(events)
    if not events_list:
        raise ValueError("at least one event is required")

    n_notes = len(events_list)
    by_severity: Counter[str] = Counter()
    n_edited = 0
    by_clinician_counts: dict[str, list[int]] = defaultdict(lambda: [0, 0])  # [edited, total]

    for ev in events_list:
        edited = bool(ev.get(edited_key, False))
        if edited:
            n_edited += 1
            severity = ev.get(severity_key) if severity_key else None
            if severity:
                by_severity[severity] += 1
        if clinician_key:
            cid = ev.get(clinician_key)
            if cid is not None:
                by_clinician_counts[str(cid)][1] += 1
                if edited:
                    by_clinician_counts[str(cid)][0] += 1

    edit_rate_pct = n_edited / n_notes * 100.0
    safety_critical_pct: float | None = None
    stylistic_pct: float | None = None
    if by_severity:
        safety_critical_pct = by_severity.get("safety_critical", 0) / n_notes * 100.0
        stylistic_pct = by_severity.get("stylistic", 0) / n_notes * 100.0

    by_clinician = {
        cid: edited / total * 100.0
        for cid, (edited, total) in by_clinician_counts.items()
        if total > 0
    }

    classification = _classify(edit_rate_pct, baseline_pct)

    return EditRateResult(
        n_notes=n_notes,
        n_edited=n_edited,
        edit_rate_pct=edit_rate_pct,
        safety_critical_rate_pct=safety_critical_pct,
        stylistic_rate_pct=stylistic_pct,
        by_clinician=by_clinician,
        classification=classification,
    )


def _classify(er_pct: float, baseline_pct: float | None) -> str:
    """Map ER to a NAS-band classification.

    The catalogue has two regimes:

    1. Day-zero baseline window (no baseline supplied yet): ER between
       30% and 80% is healthy; below 30% in early deployment flags
       inadequate review.
    2. Steady state (baseline supplied): ER below 50% of baseline,
       sustained ≥ 4 weeks, is a pause trigger. The library checks the
       per-window number; sustained-window analysis is the caller's job.
    """
    if baseline_pct is None:
        if er_pct < _DAY_ZERO_BASELINE_FLOOR_PCT:
            return "inadequate-review"
        return "no-baseline-supplied"

    if er_pct < _PAUSE_FRACTION_OF_BASELINE * baseline_pct:
        return "pause-trigger"
    if er_pct < baseline_pct - _COMPLACENCY_DROP_PP:
        return "complacency-alert"
    return "meets-baseline"
