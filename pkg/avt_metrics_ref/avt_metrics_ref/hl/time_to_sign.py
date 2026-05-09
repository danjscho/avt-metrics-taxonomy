"""HL.HF-3b Time-to-Sign Distribution.

Formal Definition (catalogue):

  TTS = t_approve - t_generated
  TTS_norm = TTS / word_count

Catalogue's Operational Specification mandates distribution reporting:
P5, P10, median, P90 of TTS *and* TTS_norm. Single-number reporting
(mean alone) is not Tier 1 sufficient.

Rubber-stamping flag: TTS_norm < 0.5s/word suggests rubber-stamping.
The catalogue's worked example also flags very-fast approvals
(< 5s for complex notes). Both signals computed here.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from datetime import datetime, timedelta
from typing import Any, NamedTuple

import numpy as np

# Catalogue thresholds (proposed-as-starting-points; see TP.HF-3b
# Trigger Conditions for the full provenance).
_RUBBER_STAMP_TTS_NORM_S_PER_WORD = 0.5
_VERY_FAST_TTS_S = 5.0  # absolute threshold for any note
_LONG_NOTE_WORDS = 200  # complex/long-note threshold


class TimeToSignDistribution(NamedTuple):
    """TTS distribution + rubber-stamping signals.

    Attributes
    ----------
    n_notes : int
    median_seconds : float
    p5_seconds : float
    p10_seconds : float
    p90_seconds : float
    median_seconds_per_word : float
        TTS_norm = TTS / word_count (median across notes).
    p5_seconds_per_word : float
    n_rubber_stamp_flag : int
        Notes with TTS_norm < 0.5s/word.
    n_very_fast_long_note : int
        Notes with word_count > ``long_note_words`` AND TTS < 5s
        (worked example: rubber-stamping a complex note).
    rubber_stamp_pct : float
        n_rubber_stamp_flag / n_notes * 100.
    """

    n_notes: int
    median_seconds: float
    p5_seconds: float
    p10_seconds: float
    p90_seconds: float
    median_seconds_per_word: float
    p5_seconds_per_word: float
    n_rubber_stamp_flag: int
    n_very_fast_long_note: int
    rubber_stamp_pct: float


def time_to_sign_distribution(
    events: Iterable[Mapping[str, Any]],
    *,
    generated_at_key: str = "generated_at",
    approved_at_key: str = "approved_at",
    word_count_key: str = "word_count",
    rubber_stamp_threshold_s_per_word: float = _RUBBER_STAMP_TTS_NORM_S_PER_WORD,
    very_fast_threshold_s: float = _VERY_FAST_TTS_S,
    long_note_words: int = _LONG_NOTE_WORDS,
) -> TimeToSignDistribution:
    """Compute Time-to-Sign Distribution (HL.HF-3b).

    Parameters
    ----------
    events : iterable of mappings
        One event per AI-generated note. Required keys:

        - ``generated_at`` (datetime) — when AVT note became visible.
        - ``approved_at`` (datetime) — when clinician signed.
        - ``word_count`` (int > 0) — word count of the note.
    generated_at_key, approved_at_key, word_count_key : str
        Override the default key names.
    rubber_stamp_threshold_s_per_word : float, default 0.5
        TTS_norm threshold below which a note is flagged as
        rubber-stamping (per the catalogue's Formal Definition).
    very_fast_threshold_s : float, default 5
        Absolute TTS threshold below which any note is flagged for the
        "very-fast on long note" signal.
    long_note_words : int, default 200
        Word-count threshold above which the very-fast flag fires when
        TTS < ``very_fast_threshold_s``.

    Returns
    -------
    TimeToSignDistribution
        Distribution percentiles + rubber-stamping signals.

    Raises
    ------
    ValueError
        If no events supplied, if any approval precedes its generation,
        or if any word_count is non-positive.

    Examples
    --------
    >>> from datetime import datetime, timedelta
    >>> g = datetime(2026, 5, 9, 10, 0)
    >>> events = [
    ...     {"generated_at": g, "approved_at": g + timedelta(seconds=120), "word_count": 100},
    ...     {"generated_at": g, "approved_at": g + timedelta(seconds=60), "word_count": 100},
    ... ]
    >>> result = time_to_sign_distribution(events)
    >>> result.n_notes
    2
    """
    events_list = list(events)
    if not events_list:
        raise ValueError("at least one event is required")

    tts_seconds: list[float] = []
    tts_norm: list[float] = []
    n_rubber_stamp = 0
    n_very_fast_long = 0

    for ev in events_list:
        gen: datetime = ev[generated_at_key]
        app: datetime = ev[approved_at_key]
        wc = int(ev.get(word_count_key, 0))
        if wc <= 0:
            raise ValueError(f"word_count must be positive; got {wc}")
        if app < gen:
            raise ValueError(
                f"approved_at ({app.isoformat()}) precedes generated_at "
                f"({gen.isoformat()})"
            )
        delta: timedelta = app - gen
        secs = delta.total_seconds()
        tts_seconds.append(secs)
        norm = secs / wc
        tts_norm.append(norm)
        if norm < rubber_stamp_threshold_s_per_word:
            n_rubber_stamp += 1
        if wc > long_note_words and secs < very_fast_threshold_s:
            n_very_fast_long += 1

    secs_arr = np.array(tts_seconds)
    norm_arr = np.array(tts_norm)
    n_notes = len(events_list)

    return TimeToSignDistribution(
        n_notes=n_notes,
        median_seconds=float(np.median(secs_arr)),
        p5_seconds=float(np.percentile(secs_arr, 5)),
        p10_seconds=float(np.percentile(secs_arr, 10)),
        p90_seconds=float(np.percentile(secs_arr, 90)),
        median_seconds_per_word=float(np.median(norm_arr)),
        p5_seconds_per_word=float(np.percentile(norm_arr, 5)),
        n_rubber_stamp_flag=n_rubber_stamp,
        n_very_fast_long_note=n_very_fast_long,
        rubber_stamp_pct=n_rubber_stamp / n_notes * 100.0,
    )
