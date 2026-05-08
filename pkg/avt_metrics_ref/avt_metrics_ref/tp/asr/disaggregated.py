"""TP.ASR-4 Demographic-Disaggregated WER.

Formal Definition (catalogue): WER computed separately for each demographic
group (accent, language, age band, sex, ethnicity, deprivation quintile,
speech characteristics), then the gap quantified. NAS framework proposes
maximum 5 percentage-point gap across groups as a starting threshold.

This is the load-bearing fairness metric for ASR — aggregate WER hides
demographic variation that has direct equity implications.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from .wer import wer as _wer


def disaggregated_wer(
    samples: Sequence[Mapping[str, Any]],
    *,
    ref_key: str = "reference",
    hyp_key: str = "hypothesis",
    group_key: str = "group",
    threshold: float = 0.05,
) -> dict:
    """Compute demographic-disaggregated WER (TP.ASR-4).

    Parameters
    ----------
    samples : sequence of mappings
        Each item is a dict-like with reference, hypothesis, and group label.
        Keys are configurable via the *_key parameters.
    ref_key : str, default "reference"
        Key in each sample for the reference transcript.
    hyp_key : str, default "hypothesis"
        Key in each sample for the hypothesis transcript.
    group_key : str, default "group"
        Key in each sample for the demographic group label.
    threshold : float, default 0.05
        Maximum acceptable WER gap across groups. The default 0.05
        (5 percentage points) is the NAS framework starting point —
        calibrate to your context.

    Returns
    -------
    dict with keys:
        - ``per_group``: mapping of group label → {"wer": float, "n": int}
        - ``equity_gap``: max(WER) - min(WER) across groups
        - ``threshold``: the threshold parameter (echoed back)
        - ``threshold_met``: bool — whether equity_gap < threshold
        - ``worst_group``: group label with highest WER
        - ``best_group``: group label with lowest WER
        - ``aggregate_wer``: corpus-level WER across all samples (for
          comparison with the disaggregated view)

    Notes
    -----
    Per-group sample sizes vary in the wild — small groups produce noisy
    WER estimates. The returned ``per_group["n"]`` exposes the sample
    size so callers can apply their own minimum-n filter before
    interpreting the gap. The library doesn't enforce a minimum because
    that decision is deployment-context-dependent.

    The "group" label is opaque to the library — passing accent codes,
    language codes, age bands, intersection labels, or anything else is
    fine as long as the key matches across samples.

    Examples
    --------
    >>> samples = [
    ...     {"reference": "the cat sat", "hypothesis": "the cat sat", "group": "A"},
    ...     {"reference": "the dog ran", "hypothesis": "the dog ran", "group": "A"},
    ...     {"reference": "she said hello", "hypothesis": "she said yellow", "group": "B"},
    ... ]
    >>> result = disaggregated_wer(samples)
    >>> result["per_group"]["A"]["wer"]
    0.0
    >>> result["per_group"]["B"]["wer"] > 0.0
    True
    """
    if threshold < 0:
        raise ValueError(f"threshold must be non-negative, got {threshold}")

    if not samples:
        return {
            "per_group": {},
            "equity_gap": 0.0,
            "threshold": threshold,
            "threshold_met": True,
            "worst_group": None,
            "best_group": None,
            "aggregate_wer": 0.0,
        }

    # Group up
    grouped: dict[Any, list[tuple[str, str]]] = {}
    for s in samples:
        try:
            ref = s[ref_key]
            hyp = s[hyp_key]
            group = s[group_key]
        except KeyError as e:
            raise KeyError(
                f"sample missing required key {e}. Each sample needs "
                f"'{ref_key}', '{hyp_key}', and '{group_key}'."
            ) from None
        grouped.setdefault(group, []).append((ref, hyp))

    # Per-group WER
    per_group: dict[Any, dict[str, float | int]] = {}
    for group, pairs in grouped.items():
        refs = [p[0] for p in pairs]
        hyps = [p[1] for p in pairs]
        per_group[group] = {
            "wer": _wer(refs, hyps),
            "n": len(pairs),
        }

    # Aggregate
    all_refs = [s[ref_key] for s in samples]
    all_hyps = [s[hyp_key] for s in samples]
    aggregate = _wer(all_refs, all_hyps)

    wer_vals = [g["wer"] for g in per_group.values()]
    equity_gap = max(wer_vals) - min(wer_vals)
    worst = max(per_group, key=lambda g: per_group[g]["wer"])
    best = min(per_group, key=lambda g: per_group[g]["wer"])

    return {
        "per_group": per_group,
        "equity_gap": float(equity_gap),
        "threshold": float(threshold),
        "threshold_met": bool(equity_gap < threshold),
        "worst_group": worst,
        "best_group": best,
        "aggregate_wer": float(aggregate),
    }
