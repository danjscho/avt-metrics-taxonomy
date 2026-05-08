"""TP.ASR-3 Clinical Keyword Error Rate (CK-ER).

Formal Definition (catalogue): proportion of reference *clinical keywords*
(extracted by a domain NER) that don't appear in the hypothesis with at
least a configurable similarity threshold. Unlike WER which scores every
word equally, CK-ER restricts evaluation to safety-critical clinical terms.

The user supplies the keyword extractor; the library does the matching
with a Levenshtein-ratio similarity check (default threshold 0.85, matching
the catalogue's illustrative snippet).
"""

from __future__ import annotations

from collections.abc import Callable, Iterable


def _levenshtein_ratio(a: str, b: str) -> float:
    """Return Levenshtein similarity ratio in [0, 1].

    Implementation note: avoids the optional `Levenshtein` dependency
    (mentioned in the catalogue snippet) so the library stays lightweight.
    Computes ratio = (len(a) + len(b) - distance) / (len(a) + len(b)).
    """
    if a == b:
        return 1.0
    if not a or not b:
        return 0.0

    # Standard Levenshtein with two-row optimisation.
    a, b = a.lower(), b.lower()
    if len(a) < len(b):
        a, b = b, a
    previous = list(range(len(b) + 1))
    for i, ca in enumerate(a, start=1):
        current = [i] + [0] * len(b)
        for j, cb in enumerate(b, start=1):
            cost = 0 if ca == cb else 1
            current[j] = min(
                previous[j] + 1,         # deletion
                current[j - 1] + 1,      # insertion
                previous[j - 1] + cost,  # substitution
            )
        previous = current
    distance = previous[-1]
    total = len(a) + len(b)
    return (total - distance) / total if total > 0 else 1.0


def clinical_keyword_error_rate(
    reference: str,
    hypothesis: str,
    extractor: Callable[[str], Iterable[str]],
    *,
    similarity_threshold: float = 0.85,
) -> dict:
    """Compute Clinical Keyword Error Rate (TP.ASR-3).

    Parameters
    ----------
    reference : str
        Reference transcript.
    hypothesis : str
        Hypothesis transcript.
    extractor : callable
        Function taking text (str) and returning an iterable of clinical
        keywords (each a str). Domain-specific NER choice (MedCAT,
        scispaCy, etc.) is left to the caller.
    similarity_threshold : float, default 0.85
        Levenshtein similarity ratio above which a hypothesis-side
        keyword is considered to match a reference-side keyword. The
        catalogue uses 0.85 as the illustrative starting point.

    Returns
    -------
    dict with keys:
        - ``cker``: error rate in [0, 1]
        - ``ref_keywords``: set of reference keywords (lowercased)
        - ``hyp_keywords``: set of hypothesis keywords (lowercased)
        - ``matched``: count of reference keywords that found a similarity
          match in the hypothesis
        - ``missing``: list of reference keywords with no match

    Examples
    --------
    >>> def naive_extractor(text):
    ...     drugs = ["amoxicillin", "paracetamol", "warfarin"]
    ...     return [d for d in drugs if d in text.lower()]
    >>> result = clinical_keyword_error_rate(
    ...     "prescribed amoxicillin and paracetamol",
    ...     "prescribed amoxycillin and paracetamol",
    ...     extractor=naive_extractor,
    ... )
    >>> 0.0 <= result["cker"] <= 1.0
    True
    """
    if not 0.0 <= similarity_threshold <= 1.0:
        raise ValueError(
            f"similarity_threshold must be in [0, 1], got {similarity_threshold}"
        )

    ref_kw = {k.lower() for k in extractor(reference)}
    hyp_kw = {k.lower() for k in extractor(hypothesis)}

    if not ref_kw:
        return {
            "cker": 0.0,
            "ref_keywords": ref_kw,
            "hyp_keywords": hyp_kw,
            "matched": 0,
            "missing": [],
        }

    matched = 0
    missing: list[str] = []
    for kw in ref_kw:
        if any(_levenshtein_ratio(kw, h) >= similarity_threshold for h in hyp_kw):
            matched += 1
        else:
            missing.append(kw)

    cker = 1.0 - (matched / len(ref_kw))

    return {
        "cker": float(cker),
        "ref_keywords": ref_kw,
        "hyp_keywords": hyp_kw,
        "matched": matched,
        "missing": sorted(missing),
    }
