"""Tests for IO.FE-1 Deployment Equity Index."""

from __future__ import annotations

import pytest

from avt_metrics_ref import deployment_equity_index
from avt_metrics_ref.io.deployment_equity import DeploymentEquityResult


def test_strong_positive_correlation_flags_inequity():
    """Deployment rises with affluence (decile 1 = most deprived) →
    positive r → inequity-flagged."""
    rates = {1: 0.10, 2: 0.15, 3: 0.20, 4: 0.30, 5: 0.40,
             6: 0.50, 7: 0.60, 8: 0.70, 9: 0.80, 10: 0.90}
    result = deployment_equity_index(rates)
    assert isinstance(result, DeploymentEquityResult)
    assert result.pearson_r > 0.95
    assert result.direction == "inequity"
    assert result.classification == "inequity-flagged"


def test_strong_negative_correlation_pro_equity():
    """Deployment higher in more-deprived deciles → negative r → pro-equity."""
    rates = {1: 0.90, 2: 0.85, 3: 0.80, 4: 0.70, 5: 0.60,
             6: 0.50, 7: 0.40, 8: 0.30, 9: 0.20, 10: 0.15}
    result = deployment_equity_index(rates)
    assert result.pearson_r < -0.9
    assert result.direction == "pro-equity"
    assert result.classification == "inequity-flagged"


def test_zero_correlation_meets_target():
    """Flat deployment across deciles → r ≈ 0 → meets-target."""
    rates = {d: 0.50 for d in range(1, 11)}
    result = deployment_equity_index(rates)
    assert result.pearson_r == pytest.approx(0.0)
    assert result.classification == "meets-target"
    assert result.direction == "neutral"


def test_alert_band_small_correlation():
    """|r| in [0.10, 0.30) → alert. Build a noisy dataset where the
    underlying trend is small relative to the noise."""
    # Hand-picked rates with high noise and only a tiny upward drift —
    # produces r ≈ 0.14, comfortably inside the alert band.
    rates = {1: 0.50, 2: 0.55, 3: 0.50, 4: 0.45, 5: 0.55,
             6: 0.50, 7: 0.45, 8: 0.55, 9: 0.50, 10: 0.55}
    result = deployment_equity_index(rates)
    # Hand-checked: this configuration produces r in the alert band.
    assert 0.10 <= abs(result.pearson_r) < 0.30, (
        f"Test data drifted; got r={result.pearson_r:.3f}. "
        "If pearson math is fine, regenerate test data."
    )
    assert result.classification == "alert"


def test_too_few_buckets_raise():
    """Pearson r needs ≥ 3 buckets to be meaningful."""
    with pytest.raises(ValueError, match="at least 3 buckets"):
        deployment_equity_index({1: 0.5, 2: 0.5})


def test_non_finite_axis_raises():
    with pytest.raises(ValueError, match="bucket axis values"):
        deployment_equity_index({1: 0.5, 2: 0.5, float("inf"): 0.5})


def test_non_finite_rate_raises():
    with pytest.raises(ValueError, match="deployment rates"):
        deployment_equity_index({1: 0.5, 2: 0.5, 3: float("nan")})


def test_constant_rate_returns_zero_r():
    """If rates don't vary, correlation is undefined; library returns r=0."""
    rates = {1: 0.5, 2: 0.5, 3: 0.5, 4: 0.5}
    result = deployment_equity_index(rates)
    assert result.pearson_r == 0.0
    assert result.classification == "meets-target"


def test_custom_bands():
    """Caller can override the alert / inequity-flagged thresholds. Both
    bands must move together so the ladder remains zero < alert
    < flagged."""
    rates = {1: 0.40, 2: 0.45, 3: 0.50, 4: 0.55, 5: 0.60}  # r ≈ 1
    # Relax both bands above 1.0 so even a perfect correlation is treated
    # as meets-target (silly but exercises the override).
    relaxed = deployment_equity_index(
        rates, target_r_zero_band=1.01, alert_r_band=1.02
    )
    assert relaxed.classification == "meets-target"
    # Tighten the zero-band below the actual r so the same data crosses
    # into "alert", and tighten alert_r_band above r so it doesn't roll
    # into "inequity-flagged".
    alert_only = deployment_equity_index(
        rates, target_r_zero_band=0.5, alert_r_band=1.01
    )
    assert alert_only.classification == "alert"
