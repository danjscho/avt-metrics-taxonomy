"""TP.ASR-1 Word Error Rate (WER).

Formal Definition (catalogue): WER = (S + D + I) / N where S, D, I are
substitutions, deletions, insertions in the optimal Levenshtein
alignment between hypothesis and reference, and N is the number of
words in the reference. Corpus-level WER is macro-averaged across
utterances (jiwer's default convention).

Wraps `jiwer.wer` and `jiwer.process_words`.
"""

from __future__ import annotations

from collections.abc import Sequence

import jiwer


def wer(
    reference: str | Sequence[str],
    hypothesis: str | Sequence[str],
    *,
    return_breakdown: bool = False,
) -> float | dict:
    """Compute Word Error Rate (TP.ASR-1).

    Parameters
    ----------
    reference : str or sequence of str
        Reference transcript(s). String for single-utterance; sequence
        for corpus-level.
    hypothesis : str or sequence of str
        Hypothesis transcript(s). Must match `reference` shape.
    return_breakdown : bool, default False
        If True, return a dict with ``wer``, ``substitutions``, ``deletions``,
        ``insertions``, and ``hits`` populated from the alignment.
        If False, return the WER as a float.

    Returns
    -------
    float or dict
        WER in [0, 1]. May exceed 1.0 if insertions outpace reference length
        (per the catalogue Limitations note).

    Examples
    --------
    >>> wer("the patient reports chest pain", "the patient reports chess pain")
    0.2
    >>> result = wer("the patient reports chest pain",
    ...              "the patient reports chess pain", return_breakdown=True)
    >>> result["substitutions"]
    1
    """
    if isinstance(reference, str) != isinstance(hypothesis, str):
        raise TypeError(
            "reference and hypothesis must both be str or both be sequences; "
            f"got {type(reference).__name__} and {type(hypothesis).__name__}"
        )

    if not return_breakdown:
        return float(jiwer.wer(reference, hypothesis))

    # process_words returns a dataclass with .wer, .substitutions, etc.
    out = jiwer.process_words(reference, hypothesis)
    return {
        "wer": float(out.wer),
        "substitutions": int(out.substitutions),
        "deletions": int(out.deletions),
        "insertions": int(out.insertions),
        "hits": int(out.hits),
    }
