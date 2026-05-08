"""TP.ASR-10 ASR Confidence Calibration.

Formal Definition (catalogue): the model's confidence scores on each
output should match its empirical accuracy. A calibrated ASR system
that says it's 0.9-confident on a token is correct ~90% of the time;
miscalibration is when stated confidence systematically diverges from
empirical correctness.

This module computes Expected Calibration Error (ECE) using fixed-width
binning, the standard approach (Guo et al. 2017, "On Calibration of
Modern Neural Networks", though the pre-AVT origins go further back).
"""

from __future__ import annotations

from collections.abc import Sequence

import numpy as np


def asr_confidence_calibration(
    confidences: Sequence[float],
    correctness: Sequence[bool | int],
    *,
    n_bins: int = 10,
) -> dict:
    """Compute ASR confidence calibration via Expected Calibration Error
    (TP.ASR-10).

    Parameters
    ----------
    confidences : sequence of float
        Per-token (or per-utterance) ASR confidence in [0, 1].
    correctness : sequence of bool or int
        Per-token correctness (1/True for correct, 0/False for wrong).
        Must be the same length as `confidences`.
    n_bins : int, default 10
        Number of equal-width bins on [0, 1].

    Returns
    -------
    dict with keys:
        - ``ece``: Expected Calibration Error in [0, 1]
        - ``mce``: Maximum Calibration Error (worst single-bin gap)
        - ``per_bin``: list of dicts, one per bin, each with
          ``range``, ``count``, ``mean_confidence``, ``mean_accuracy``,
          ``gap``
        - ``n``: total sample count

    Notes
    -----
    Empty bins contribute 0 to ECE (skipped) but still appear in
    ``per_bin`` so downstream code can render full reliability diagrams.

    Bin boundaries follow the standard "[0, 1/n), [1/n, 2/n), ..., [1-1/n, 1]"
    convention with the rightmost bin closed-on-both-sides.

    Examples
    --------
    >>> # Perfect calibration: confidence == accuracy
    >>> result = asr_confidence_calibration(
    ...     confidences=[0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.0],
    ...     correctness=[1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    ... )
    >>> result["ece"] < 0.05
    True
    """
    if n_bins < 1:
        raise ValueError(f"n_bins must be >= 1, got {n_bins}")
    if len(confidences) != len(correctness):
        raise ValueError(
            f"confidences and correctness must have the same length; got "
            f"{len(confidences)} and {len(correctness)}"
        )

    n = len(confidences)
    if n == 0:
        return {
            "ece": 0.0,
            "mce": 0.0,
            "per_bin": [],
            "n": 0,
        }

    confs = np.asarray(confidences, dtype=float)
    accs = np.asarray(correctness, dtype=float)

    if np.any((confs < 0.0) | (confs > 1.0)):
        raise ValueError("confidences must be in [0, 1]")

    # Bin edges
    edges = np.linspace(0.0, 1.0, n_bins + 1)
    per_bin = []
    ece = 0.0
    mce = 0.0
    for i in range(n_bins):
        lo, hi = edges[i], edges[i + 1]
        if i == n_bins - 1:
            mask = (confs >= lo) & (confs <= hi)
        else:
            mask = (confs >= lo) & (confs < hi)
        count = int(mask.sum())
        if count == 0:
            per_bin.append(
                {
                    "range": (float(lo), float(hi)),
                    "count": 0,
                    "mean_confidence": None,
                    "mean_accuracy": None,
                    "gap": None,
                }
            )
            continue
        mean_conf = float(confs[mask].mean())
        mean_acc = float(accs[mask].mean())
        gap = abs(mean_conf - mean_acc)
        per_bin.append(
            {
                "range": (float(lo), float(hi)),
                "count": count,
                "mean_confidence": mean_conf,
                "mean_accuracy": mean_acc,
                "gap": float(gap),
            }
        )
        ece += (count / n) * gap
        if gap > mce:
            mce = gap

    return {
        "ece": float(ece),
        "mce": float(mce),
        "per_bin": per_bin,
        "n": n,
    }
