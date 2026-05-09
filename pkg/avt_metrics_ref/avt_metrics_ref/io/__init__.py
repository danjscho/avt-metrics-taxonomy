"""IO cluster — Impact & Outcomes.

Library coverage so far: IO.FE-1 Deployment Equity Index. The catalogue's
IO.FE family (Demographic Equity Disaggregation) shares a common
operationalisation pattern — disaggregate a deployment / coverage rate
across demographic axes, surface the equity gap. This shape composes
with `disaggregated_wer` (TP.ASR-4) and any future demographic-
disaggregated metrics.
"""

from __future__ import annotations

from .deployment_equity import deployment_equity_index

__all__ = ["deployment_equity_index"]
