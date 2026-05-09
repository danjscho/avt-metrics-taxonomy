"""HL cluster — Human Layer.

Library coverage: HL.HF Tier 1 telemetry triplet — Edit Rate (HL.HF-1),
Review-Before-Signing Rate (HL.HF-3a), Time-to-Sign Distribution
(HL.HF-3b). All three read structured per-encounter EPR / AVT telemetry
and emit per-period rates with NAS-band classifications.

The catalogue specifies that HL.HF-3a and HL.HF-3b should be reported
*jointly* — the conjunction is the rubber-stamping signal. This library
returns the per-metric numbers; the caller is responsible for the
conjunction analysis (or use :func:`rubber_stamping_signal` for the
worked example).
"""

from __future__ import annotations

from .edit_rate import edit_rate
from .review_before_signing import review_before_signing_rate
from .time_to_sign import time_to_sign_distribution

__all__ = [
    "edit_rate",
    "review_before_signing_rate",
    "time_to_sign_distribution",
]
