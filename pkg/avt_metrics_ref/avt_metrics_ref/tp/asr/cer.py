"""TP.ASR-8 Character Error Rate (CER).

Formal Definition (catalogue): CER = (S + D + I) / N at the character
level. Useful for languages without clear word boundaries and for
catching near-miss substitutions that WER counts as full word errors
(e.g. "amoxicillin" vs "amoxycillin" — one character wrong, one full
word wrong by WER).

Wraps `jiwer.cer`.
"""

from __future__ import annotations

from collections.abc import Sequence

import jiwer


def cer(
    reference: str | Sequence[str],
    hypothesis: str | Sequence[str],
) -> float:
    """Compute Character Error Rate (TP.ASR-8).

    Parameters
    ----------
    reference : str or sequence of str
        Reference transcript(s).
    hypothesis : str or sequence of str
        Hypothesis transcript(s). Must match `reference` shape.

    Returns
    -------
    float
        CER in [0, 1]. May exceed 1.0 in the same edge case as WER.

    Examples
    --------
    >>> cer("amoxicillin 500mg", "amoxycillin 500mg")
    0.058823529411764705
    """
    if isinstance(reference, str) != isinstance(hypothesis, str):
        raise TypeError(
            "reference and hypothesis must both be str or both be sequences; "
            f"got {type(reference).__name__} and {type(hypothesis).__name__}"
        )
    return float(jiwer.cer(reference, hypothesis))
