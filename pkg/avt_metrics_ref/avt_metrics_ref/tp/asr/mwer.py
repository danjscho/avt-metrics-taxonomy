"""TP.ASR-2 Medical Word Error Rate (M-WER).

Formal Definition (catalogue): WER weighted by clinical-significance class
of each reference token. Different token classes (drug names, dosages,
allergies, anatomy, fillers, etc.) carry different weights so that errors
on safety-critical terms count more heavily than fillers.

Implementation note: the catalogue's snippet for this metric is explicitly
illustrative pseudocode (uses position-based comparison rather than
edit-distance alignment) to keep focus on the weight-matrix dimension.
This implementation composes `jiwer.process_words` for the actual
alignment with a user-supplied per-token classifier callable.

The user supplies the classifier because a production-quality clinical
NER is a domain-specific choice (MedCAT, scispaCy, custom regex, etc.)
that this library doesn't take a position on. The classifier signature
is a token (str) → class label (str); the library handles the weight
lookup and the alignment-aware computation.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping

import jiwer


# Default weights for common clinical-significance classes. Callers can
# override per-class or supply a fully custom mapping. These are
# *starting points* — calibrate to your deployment context, do not
# treat as canonical.
DEFAULT_WEIGHTS: Mapping[str, float] = {
    "drug_name": 10.0,
    "dosage": 10.0,
    "allergy": 8.0,
    "diagnosis": 7.0,
    "red_flag_symptom": 9.0,
    "anatomy": 5.0,
    "filler": 0.1,
    "default": 1.0,
}


def medical_wer(
    reference: str,
    hypothesis: str,
    classifier: Callable[[str], str],
    *,
    weights: Mapping[str, float] = DEFAULT_WEIGHTS,
) -> dict:
    """Compute Medical WER (TP.ASR-2).

    Composes jiwer's edit-distance alignment with a per-token weight
    derived from a user-supplied classifier.

    Parameters
    ----------
    reference : str
        Reference transcript.
    hypothesis : str
        Hypothesis transcript.
    classifier : callable
        Function taking a token (str) and returning a class label (str).
        The class label is looked up in `weights` to determine the
        per-token weight; tokens whose class isn't in `weights` use the
        ``"default"`` weight.
    weights : mapping, optional
        Per-class weight lookup. Falls back to `DEFAULT_WEIGHTS` and
        requires a ``"default"`` key for unmapped classes.

    Returns
    -------
    dict with keys:
        - ``mwer``: weighted error rate in [0, ∞)
        - ``weighted_errors``: sum of weights for misaligned reference tokens
        - ``weighted_total``: sum of weights for all reference tokens
        - ``per_class_errors``: per-class error count (unweighted)
        - ``per_class_total``: per-class reference-token count

    Notes
    -----
    Honest scope: this implementation aligns at the word level (jiwer's
    default tokenisation). Domain-specific tokenisation (treating "500mg"
    as one token vs three) is the caller's responsibility — supply
    pre-tokenised text if needed.

    Examples
    --------
    >>> def simple_classifier(token):
    ...     if token in {"amoxicillin", "paracetamol"}: return "drug_name"
    ...     if token.endswith("mg"): return "dosage"
    ...     return "default"
    >>> result = medical_wer(
    ...     "patient prescribed amoxicillin 500mg",
    ...     "patient prescribed amoxycillin 500mg",
    ...     classifier=simple_classifier,
    ... )
    >>> result["mwer"] > 0.0
    True
    """
    if "default" not in weights:
        raise ValueError(
            "weights mapping must include a 'default' key for tokens whose "
            "classifier output isn't otherwise listed"
        )

    out = jiwer.process_words(reference, hypothesis)
    # process_words gives us alignments. We need: for each reference token,
    # was it correctly recognised, and what's its weight?
    # alignments is a list of lists (one per pair); for single-string input
    # it's a single-element list.
    alignments = out.alignments[0]
    refs_tokens = out.references[0]

    weighted_errors = 0.0
    weighted_total = 0.0
    per_class_errors: dict[str, int] = {}
    per_class_total: dict[str, int] = {}

    for chunk in alignments:
        # chunk has type ('equal' | 'substitute' | 'delete' | 'insert')
        # and ref_start_idx / ref_end_idx attributes (and hyp_*).
        chunk_type = chunk.type
        # Skip pure insertions — they have no reference token.
        if chunk_type == "insert":
            continue
        for ref_idx in range(chunk.ref_start_idx, chunk.ref_end_idx):
            token = refs_tokens[ref_idx]
            cls = classifier(token)
            w = weights.get(cls, weights["default"])
            weighted_total += w
            per_class_total[cls] = per_class_total.get(cls, 0) + 1
            if chunk_type != "equal":
                weighted_errors += w
                per_class_errors[cls] = per_class_errors.get(cls, 0) + 1

    mwer = weighted_errors / weighted_total if weighted_total > 0 else 0.0

    return {
        "mwer": float(mwer),
        "weighted_errors": float(weighted_errors),
        "weighted_total": float(weighted_total),
        "per_class_errors": per_class_errors,
        "per_class_total": per_class_total,
    }
