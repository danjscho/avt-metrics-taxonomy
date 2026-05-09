"""HL.HF-3a Review-Before-Signing Rate.

Formal Definition (catalogue):

  RBS = |N_reviewed| / |N_total|
  N_reviewed = notes with edit events, scroll events, or dwell > T_min
  T_min = max(15s, 3s × word_count / 100)

NAS Day Zero SPI: ≥ 95% target, < 85% pause trigger.

Catalogue makes joint reporting with HL.HF-3b mandatory — RBS alone is
ambiguous; pair with `time_to_sign_distribution` for the rubber-stamping
signal.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any, NamedTuple

# NAS Day Zero SPI bands.
_NAS_TARGET_PCT = 95.0
_NAS_PAUSE_BELOW_PCT = 85.0


class ReviewBeforeSigningResult(NamedTuple):
    """Aggregate RBS breakdown.

    Attributes
    ----------
    n_notes : int
    n_reviewed : int
        Notes that received at least one review-event signal (edit, scroll,
        or above-threshold dwell).
    rbs_pct : float
        ``n_reviewed / n_notes * 100``.
    by_clinician : dict[str, float]
        Per-clinician RBS in % when ``clinician_id`` is in the events.
    classification : str
        ``"meets-target"`` (RBS ≥ 95%), ``"below-target"`` (85–95%, NAS
        warning band), or ``"pause-trigger"`` (RBS < 85%, NAS pause).
    target_pct : float
    pause_threshold_pct : float
    """

    n_notes: int
    n_reviewed: int
    rbs_pct: float
    by_clinician: dict[str, float]
    classification: str
    target_pct: float
    pause_threshold_pct: float


def review_before_signing_rate(
    events: Iterable[Mapping[str, Any]],
    *,
    word_count_key: str = "word_count",
    edit_events_key: str = "edit_events",
    scroll_events_key: str = "scroll_events",
    dwell_seconds_key: str = "dwell_seconds",
    clinician_key: str | None = "clinician_id",
    target_pct: float = _NAS_TARGET_PCT,
    pause_threshold_pct: float = _NAS_PAUSE_BELOW_PCT,
) -> ReviewBeforeSigningResult:
    """Compute Review-Before-Signing Rate (HL.HF-3a).

    Parameters
    ----------
    events : iterable of mappings
        One event per AI-generated note. Each event should provide:

        - ``word_count`` (int) — word count of the note (drives the
          per-note T_min threshold).
        - ``edit_events`` (int) — count of keystroke/text-mutation events
          between AVT generation and signature.
        - ``scroll_events`` (int) — count of viewport movements within the
          note body.
        - ``dwell_seconds`` (float) — total foreground dwell time on the
          note (seconds).
        - ``clinician_id`` (any hashable; optional) — for per-clinician
          breakdown.

        A note counts as reviewed if any of: ``edit_events > 0``,
        ``scroll_events > 0``, or ``dwell_seconds >= T_min``.
    word_count_key, edit_events_key, scroll_events_key, dwell_seconds_key, clinician_key : str
        Override the default key names.
    target_pct : float, default 95
        NAS target percentage. Override for local calibration.
    pause_threshold_pct : float, default 85
        NAS pause-trigger percentage.

    Returns
    -------
    ReviewBeforeSigningResult

    Raises
    ------
    ValueError
        If no events supplied.

    Examples
    --------
    >>> events = [
    ...     {"word_count": 100, "edit_events": 3, "scroll_events": 2, "dwell_seconds": 60},
    ...     {"word_count": 100, "edit_events": 0, "scroll_events": 0, "dwell_seconds": 5},
    ... ]
    >>> result = review_before_signing_rate(events)
    >>> result.n_reviewed
    1
    """
    events_list = list(events)
    if not events_list:
        raise ValueError("at least one event is required")

    n_notes = len(events_list)
    n_reviewed = 0
    per_clinician_counts: dict[str, list[int]] = {}

    for ev in events_list:
        wc = int(ev.get(word_count_key, 0))
        edits = int(ev.get(edit_events_key, 0))
        scrolls = int(ev.get(scroll_events_key, 0))
        dwell = float(ev.get(dwell_seconds_key, 0.0))
        # T_min from the catalogue: max(15s, 3s × word_count / 100).
        t_min = max(15.0, 3.0 * wc / 100.0)
        reviewed = edits > 0 or scrolls > 0 or dwell >= t_min
        if reviewed:
            n_reviewed += 1
        if clinician_key:
            cid = ev.get(clinician_key)
            if cid is not None:
                per_clinician_counts.setdefault(str(cid), [0, 0])
                per_clinician_counts[str(cid)][1] += 1
                if reviewed:
                    per_clinician_counts[str(cid)][0] += 1

    rbs_pct = n_reviewed / n_notes * 100.0
    by_clinician = {
        cid: r / t * 100.0
        for cid, (r, t) in per_clinician_counts.items()
        if t > 0
    }

    if rbs_pct >= target_pct:
        classification = "meets-target"
    elif rbs_pct >= pause_threshold_pct:
        classification = "below-target"
    else:
        classification = "pause-trigger"

    return ReviewBeforeSigningResult(
        n_notes=n_notes,
        n_reviewed=n_reviewed,
        rbs_pct=rbs_pct,
        by_clinician=by_clinician,
        classification=classification,
        target_pct=target_pct,
        pause_threshold_pct=pause_threshold_pct,
    )
