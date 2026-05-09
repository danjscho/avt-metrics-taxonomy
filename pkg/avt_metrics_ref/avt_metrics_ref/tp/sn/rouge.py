"""TP.SN-1 ROUGE Scores.

Formal Definition (catalogue): ROUGE-N recall = sum of count_match(gram_n)
divided by sum of count(gram_n) over the reference. ROUGE-L uses the
longest common subsequence. All scores in [0, 1]; higher = greater
overlap. The metric does NOT capture clinical correctness — see the
catalogue underspecification warning at TP.SN-1.

Wraps Google's `rouge-score` reference implementation. Returns a
NamedTuple per metric variant with precision / recall / F1 fields, plus
a corpus-level convenience that averages per-pair F1 scores.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import NamedTuple

from rouge_score import rouge_scorer


class RougeScore(NamedTuple):
    """One ROUGE variant's precision / recall / F1.

    Attributes
    ----------
    precision : float
    recall : float
    f1 : float
    """

    precision: float
    recall: float
    f1: float


class RougeResult(NamedTuple):
    """Bundle of all requested ROUGE variants for a single (ref, hyp) pair.

    Attributes
    ----------
    rouge1 : RougeScore | None
    rouge2 : RougeScore | None
    rougeL : RougeScore | None
        Each may be None if not requested in ``variants``.
    """

    rouge1: RougeScore | None
    rouge2: RougeScore | None
    rougeL: RougeScore | None


_ALL_VARIANTS = ("rouge1", "rouge2", "rougeL")


def rouge(
    reference: str | Sequence[str],
    hypothesis: str | Sequence[str],
    *,
    variants: Sequence[str] = _ALL_VARIANTS,
    use_stemmer: bool = True,
) -> RougeResult | list[RougeResult]:
    """Compute ROUGE scores for a (reference, hypothesis) pair or corpus.

    Parameters
    ----------
    reference : str or sequence of str
        Reference summary(ies). String for a single pair; sequence for
        corpus-level (returns one RougeResult per pair).
    hypothesis : str or sequence of str
        Hypothesis summary(ies); must match the shape of ``reference``.
    variants : sequence of {"rouge1", "rouge2", "rougeL"}, default all three
        Which ROUGE variants to compute.
    use_stemmer : bool, default True
        Apply Porter stemming before n-gram overlap (the standard ROUGE
        configuration). Stemming reduces minor morphological mismatches
        but does not address the metric's clinical-correctness gap.

    Returns
    -------
    RougeResult or list of RougeResult
        Single result for a single pair; list of per-pair results for
        corpus-level inputs. Each RougeResult holds RougeScore namedtuples
        for the requested variants (None for variants not requested).

    Notes
    -----
    See TP.SN-1's underspecification warning in the catalogue. ROUGE
    correlates near-zero with expert clinical judgement of clinical
    summarisation quality. This function exists to make ROUGE *runnable*
    so you can compare against published ROUGE numbers; it should not
    be used as a standalone clinical quality indicator.

    Examples
    --------
    >>> result = rouge(
    ...     "Patient presents with cough and fever.",
    ...     "Patient has cough and fever.",
    ... )
    >>> result.rouge1.f1 > 0.5
    True
    """
    invalid = set(variants) - set(_ALL_VARIANTS)
    if invalid:
        raise ValueError(
            f"unknown ROUGE variant(s): {sorted(invalid)}. "
            f"Supported: {list(_ALL_VARIANTS)}"
        )
    if isinstance(reference, str) != isinstance(hypothesis, str):
        raise TypeError(
            "reference and hypothesis must both be str or both be sequences; "
            f"got {type(reference).__name__} and {type(hypothesis).__name__}"
        )

    scorer = rouge_scorer.RougeScorer(list(variants), use_stemmer=use_stemmer)

    def score_one(ref: str, hyp: str) -> RougeResult:
        raw = scorer.score(ref, hyp)
        return RougeResult(
            rouge1=_to_score(raw, "rouge1") if "rouge1" in variants else None,
            rouge2=_to_score(raw, "rouge2") if "rouge2" in variants else None,
            rougeL=_to_score(raw, "rougeL") if "rougeL" in variants else None,
        )

    if isinstance(reference, str):
        return score_one(reference, hypothesis)  # type: ignore[arg-type]

    if len(reference) != len(hypothesis):  # type: ignore[arg-type]
        raise ValueError(
            f"reference and hypothesis must be the same length; "
            f"got {len(reference)} and {len(hypothesis)}"  # type: ignore[arg-type]
        )
    return [score_one(r, h) for r, h in zip(reference, hypothesis)]


def _to_score(raw: dict, key: str) -> RougeScore:
    """Convert rouge-score's per-variant Score namedtuple into our
    RougeScore (which uses the same field names but is locally owned)."""
    s = raw[key]
    return RougeScore(precision=float(s.precision), recall=float(s.recall), f1=float(s.fmeasure))
