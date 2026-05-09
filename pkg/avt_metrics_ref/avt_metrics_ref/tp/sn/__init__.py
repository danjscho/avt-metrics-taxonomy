"""TP.SN — Summarisation / NLP reference implementations.

Currently covers the Reference-Based Text Similarity family:

- TP.SN-1 ROUGE Scores  → :func:`rouge`
- TP.SN-2 BERTScore     → :func:`bertscore` (requires the ``bertscore`` extra)

Both metrics carry catalogue underspecification warnings — they are
*linguistic* similarity measures, not clinical-correctness measures. See
the catalogue entries for the framing; this library only computes the
numbers.
"""

from __future__ import annotations

from .rouge import rouge

__all__ = ["rouge"]


def __getattr__(name: str):
    """Lazy-import ``bertscore`` so the heavy ``bert-score`` dependency is
    only loaded when actually used. Allows ``from avt_metrics_ref.tp.sn
    import bertscore`` without forcing every caller to install the
    optional extra."""
    if name == "bertscore":
        from .bertscore import bertscore as _bertscore

        return _bertscore
    raise AttributeError(f"module 'avt_metrics_ref.tp.sn' has no attribute {name!r}")
