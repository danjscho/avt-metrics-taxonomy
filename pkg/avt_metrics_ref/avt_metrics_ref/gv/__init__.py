"""GV cluster — System Governance.

Most GV metrics are process-attestation (DPIA completion, board oversight,
clinical safety case) and have no computational kernel — those are
deliberately out of scope for this library, which only operationalises
the subset of metrics that reduce to a function call.

Layout convention: GV is a flat namespace (no per-group sub-package) until
multiple functions accumulate within the same group. When that happens
the relevant module is promoted to a sub-package. This is a deliberately
lighter shape than `tp.asr` / `tp.sn` because GV computational kernels are
sparser.

Coverage:

- GV.OP-5 System Availability / Uptime → :func:`system_availability`
- GV.SG-3 Performance Degradation Detection Latency → :func:`degradation_detection_latency`
"""

from __future__ import annotations

from .degradation_latency import degradation_detection_latency
from .uptime import system_availability

__all__ = [
    "system_availability",
    "degradation_detection_latency",
]
