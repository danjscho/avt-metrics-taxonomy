"""avt-metrics-ref — reference implementations for the AVT Metrics Taxonomy.

This is a **prototype-for-discussion** companion library to the AVT Metrics
Taxonomy (https://danjscho.github.io/avt-metrics-taxonomy/). The pilot
covers the TP.ASR cluster only. The catalogue itself remains the canonical
source of metric definitions; this library is one possible operationalisation
of those definitions, made runnable so deployers can compute the metrics
on their own data.

Important:
- The functions here implement the catalogue's Formal Definitions but cannot
  guarantee that any given input/output behaviour matches every reasonable
  reading of those definitions. Verify before relying on the numbers in
  contractual or academic contexts.
- The library does NOT provide datasets, pre-trained models, clinical
  decision support, or anything else outside the metric computation itself.
  See the README for the full scope statement.
- See `disclaimer()` for the runtime-callable framing.

Versioning:
- Package version (`__version__`) is independent of the catalogue version
  (`__catalogue_version__`). The package follows SemVer; the catalogue
  follows the convention documented in `taxonomy/_versioning.md`.
- A package version of `0.x.0` signals alpha; the major version stays 0
  while the package is itself prototype-shaped.
"""

__version__ = "0.1.0"

# The catalogue version this release was authored against. Bumped when a
# catalogue release modifies a TP.ASR Formal Definition or adds a new
# TP.ASR metric that this library should cover.
__catalogue_version__ = "v5.5.5"

# Curated public surface — kept narrow on purpose. Helpers and internal
# tooling are not exported.
from .tp.asr import (
    wer,
    cer,
    medical_wer,
    clinical_keyword_error_rate,
    disaggregated_wer,
    asr_confidence_calibration,
)

__all__ = [
    "__version__",
    "__catalogue_version__",
    "disclaimer",
    # TP.ASR cluster
    "wer",
    "cer",
    "medical_wer",
    "clinical_keyword_error_rate",
    "disaggregated_wer",
    "asr_confidence_calibration",
]


def disclaimer() -> str:
    """Return the prototype-status framing as a string.

    Callable rather than printed-on-import so library users can decide
    when (or whether) to surface it. Recommended: include in any
    publication, dashboard, or contract that cites the package output.
    """
    return (
        f"avt-metrics-ref v{__version__} — prototype-for-discussion companion "
        f"to AVT Metrics Taxonomy {__catalogue_version__}. Not validated for "
        f"production decisions, clinical decision support, or contractual "
        f"thresholds. See https://danjscho.github.io/avt-metrics-taxonomy/ "
        f"for the canonical catalogue and the prototype-status framing."
    )
