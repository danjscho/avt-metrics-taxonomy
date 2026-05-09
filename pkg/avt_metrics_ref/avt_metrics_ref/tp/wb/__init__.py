"""TP.WB — Downstream Write-back.

Library coverage so far: TP.WB-2 Integration Error Rate. Other TP.WB
metrics (write-back fidelity, field mapping accuracy, update vs append
behaviour) need a per-EPR adapter pattern this library has not yet
committed to.
"""

from __future__ import annotations

from .integration_error_rate import integration_error_rate

__all__ = ["integration_error_rate"]
