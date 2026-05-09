"""IO.FE-1 Deployment Equity Index.

Formal Definition (catalogue):

  Correlation r(AVT_deployed, IMD_decile)
  Positive correlation = deployment inequity. Target: r ≈ 0.

The catalogue specifies a Pearson correlation between deployment-rate
and a deprivation index (IMD decile in NHS context). This library
generalises slightly: any ordered axis (IMD decile; rurality decile;
demographic-quartile rank) can be passed in alongside per-bucket
deployment counts; the function returns the Pearson correlation plus
a band classification.

The "deployment rate" can be expressed as:

- Absolute deployment count per bucket (callers want raw counts)
- Per-capita rate per bucket (callers should pre-divide by population)
- Coverage proportion per bucket (callers want a 0-1 ratio)

The function takes the rate as already-computed; deciding what the
right per-bucket rate definition is for a given deployment is a
calibration decision that does not belong in the library.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import NamedTuple

import numpy as np

# Catalogue target: r ≈ 0 (deployment access independent of deprivation).
# Library starting points for band classification — proposed-as-starting-points,
# not externally cited. Override per the Calibration & Context principle.
_TARGET_R_ZERO_BAND = 0.10  # |r| < 0.10 = effectively no correlation
_ALERT_R_BAND = 0.30  # |r| in [0.10, 0.30] = small but measurable
# Above 0.30 in either direction = inequity-alert band


class DeploymentEquityResult(NamedTuple):
    """Deployment equity classification.

    Attributes
    ----------
    pearson_r : float
        Pearson correlation between deployment_rate and the axis values.
        Positive r = higher deployment in higher axis values (e.g. higher
        deployment in less-deprived deciles, which is a deployment inequity).
    n_buckets : int
        Number of buckets the correlation was computed across.
    direction : str
        ``"pro-equity"`` (negative r — deployment higher in more-deprived
        deciles, or whichever direction makes sense for the axis),
        ``"inequity"`` (positive r — deployment lower in more-deprived
        deciles), or ``"neutral"`` (|r| within the zero-band).
    classification : str
        ``"meets-target"`` (|r| < 0.10), ``"alert"`` (0.10 ≤ |r| < 0.30),
        or ``"inequity-flagged"`` (|r| ≥ 0.30).
    """

    pearson_r: float
    n_buckets: int
    direction: str
    classification: str


def deployment_equity_index(
    bucket_to_rate: Mapping[float | int, float],
    *,
    target_r_zero_band: float = _TARGET_R_ZERO_BAND,
    alert_r_band: float = _ALERT_R_BAND,
) -> DeploymentEquityResult:
    """Compute Deployment Equity Index (IO.FE-1).

    Parameters
    ----------
    bucket_to_rate : mapping of {axis_value: deployment_rate}
        Axis value (e.g. IMD decile 1 through 10, or rurality quartile)
        mapped to a deployment rate. The "rate" can be any numeric
        value the caller wants to test for equity (raw count,
        per-capita rate, coverage proportion); the correlation is
        scale-invariant.

        For IMD use the convention that **decile 1 = most deprived** and
        decile 10 = least deprived (the ONS convention). With this
        convention, a positive Pearson correlation between decile and
        deployment rate signals deployment inequity (more-deprived areas
        getting less AVT).
    target_r_zero_band : float, default 0.10
        |r| < this is classified as ``"meets-target"`` (effectively no
        correlation).
    alert_r_band : float, default 0.30
        |r| in ``[zero_band, alert_band)`` is ``"alert"``;
        |r| ≥ ``alert_band`` is ``"inequity-flagged"``.

    Returns
    -------
    DeploymentEquityResult

    Raises
    ------
    ValueError
        If fewer than 3 buckets supplied (Pearson r is degenerate /
        meaningless on smaller samples), or if any bucket value or rate
        is non-finite.

    Examples
    --------
    >>> # IMD deciles 1 (most deprived) → 10 (least deprived); deployment
    >>> # rate rises with affluence — classic inequity.
    >>> rates = {1: 0.10, 2: 0.15, 3: 0.20, 4: 0.30, 5: 0.40,
    ...          6: 0.50, 7: 0.60, 8: 0.70, 9: 0.80, 10: 0.90}
    >>> result = deployment_equity_index(rates)
    >>> result.pearson_r > 0.9
    True
    >>> result.classification
    'inequity-flagged'
    >>> result.direction
    'inequity'
    """
    if len(bucket_to_rate) < 3:
        raise ValueError(
            f"need at least 3 buckets to compute Pearson correlation; "
            f"got {len(bucket_to_rate)}"
        )

    xs = np.array(list(bucket_to_rate.keys()), dtype=float)
    ys = np.array(list(bucket_to_rate.values()), dtype=float)

    if not np.all(np.isfinite(xs)):
        raise ValueError("all bucket axis values must be finite numbers")
    if not np.all(np.isfinite(ys)):
        raise ValueError("all deployment rates must be finite numbers")

    # If either axis has zero variance (all values identical), correlation
    # is undefined. Treat as r=0 (no signal); upstream code can interpret.
    if np.std(xs) == 0 or np.std(ys) == 0:
        r = 0.0
    else:
        r = float(np.corrcoef(xs, ys)[0, 1])

    if abs(r) < target_r_zero_band:
        classification = "meets-target"
        direction = "neutral"
    else:
        if abs(r) < alert_r_band:
            classification = "alert"
        else:
            classification = "inequity-flagged"
        # Direction: positive r with IMD-decile convention (1=most deprived,
        # 10=least) means deployment rises with decile → less in deprived areas
        # → inequity. Library-level naming is convention-neutral; the caller
        # interprets direction against their axis convention. We document the
        # IMD case in the function docstring; here we just report the sign.
        direction = "inequity" if r > 0 else "pro-equity"

    return DeploymentEquityResult(
        pearson_r=r,
        n_buckets=len(bucket_to_rate),
        direction=direction,
        classification=classification,
    )
