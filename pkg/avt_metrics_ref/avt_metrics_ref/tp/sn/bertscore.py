"""TP.SN-2 BERTScore.

Formal Definition (catalogue): token-level cosine similarity between
contextual embeddings; precision / recall / F1 computed via greedy
matching with optional IDF weighting. Layer selection affects results.
Range [0, 1] (after the standard rescaling); higher = more semantically
similar.

Wraps the ``bert-score`` Python package. The dependency is heavyweight
(loads a HuggingFace transformer model on first use), so it lives behind
the ``bertscore`` extra:

    pip install 'avt-metrics-ref[bertscore]'

See TP.SN-2's underspecification warning in the catalogue. Semantic
similarity is materially better than ROUGE but still not clinical
correctness — pair with a validated clinical instrument.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import NamedTuple


class BertScoreResult(NamedTuple):
    """Per-pair BERTScore precision / recall / F1, plus model + layer.

    Attributes
    ----------
    precision : float
    recall : float
    f1 : float
    model : str
        The transformer model used (e.g. ``microsoft/deberta-xlarge-mnli``).
    num_layers : int | None
        Layer index used (None = the package default for the model).
    """

    precision: float
    recall: float
    f1: float
    model: str
    num_layers: int | None


# Default model is the bert-score package default (current as of v0.3.13);
# the catalogue snippet uses BiomedNLP-BiomedBERT but that's a demonstration
# of in-domain models, not a prescription. We let callers override.
_DEFAULT_MODEL = "microsoft/deberta-xlarge-mnli"


def bertscore(
    references: Sequence[str],
    hypotheses: Sequence[str],
    *,
    model_type: str = _DEFAULT_MODEL,
    num_layers: int | None = None,
    lang: str = "en",
    idf: bool = False,
    rescale_with_baseline: bool = False,
    verbose: bool = False,
) -> list[BertScoreResult]:
    """Compute BERTScore for a corpus of (reference, hypothesis) pairs.

    Parameters
    ----------
    references : sequence of str
        Reference summary(ies).
    hypotheses : sequence of str
        Hypothesis summary(ies); must match ``references`` length.
    model_type : str, default ``microsoft/deberta-xlarge-mnli``
        HuggingFace model identifier for the contextual embedding. The
        catalogue snippet uses an in-domain biomedical model
        (``microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract``); for
        clinical-text evaluation an in-domain model is generally
        preferable. Layer selection (``num_layers``) interacts with model
        choice and materially affects scores.
    num_layers : int or None, default None
        Hidden-state layer to extract embeddings from. None = package
        default for the chosen model.
    lang : str, default "en"
        Language code; informs the package's default model selection
        (only used when ``model_type`` is not specified).
    idf : bool, default False
        Whether to apply IDF weighting across the supplied corpus.
        Requires a corpus of more than one pair to be useful.
    rescale_with_baseline : bool, default False
        Apply baseline rescaling per the bert-score package docs (subtracts
        the package's pre-computed random-pair baseline so scores cluster
        around 0 instead of around 0.85). Useful for interpretability.
    verbose : bool, default False
        Forwarded to bert-score (prints model loading progress).

    Returns
    -------
    list of BertScoreResult
        One BertScoreResult per (reference, hypothesis) pair.

    Raises
    ------
    ImportError
        If the ``bert-score`` package is not installed. Install via
        ``pip install 'avt-metrics-ref[bertscore]'`` or
        ``pip install bert-score``.
    ValueError
        If references and hypotheses have different lengths.

    Notes
    -----
    First call loads a transformer model (≥1.5 GB for the default
    DeBERTa). Subsequent calls in the same Python session reuse the
    cached model. For batch evaluation, prefer one large call over many
    small calls.
    """
    try:
        from bert_score import score as _bs_score  # type: ignore[import-not-found]
    except ImportError as exc:  # pragma: no cover — exercised only in environments without the extra
        raise ImportError(
            "bertscore() requires the 'bert-score' package. "
            "Install with: pip install 'avt-metrics-ref[bertscore]'"
        ) from exc

    if len(references) != len(hypotheses):
        raise ValueError(
            f"references and hypotheses must be the same length; "
            f"got {len(references)} and {len(hypotheses)}"
        )

    p, r, f1 = _bs_score(
        cands=list(hypotheses),
        refs=list(references),
        model_type=model_type,
        num_layers=num_layers,
        lang=lang,
        idf=idf,
        rescale_with_baseline=rescale_with_baseline,
        verbose=verbose,
    )

    return [
        BertScoreResult(
            precision=float(p[i].item()),
            recall=float(r[i].item()),
            f1=float(f1[i].item()),
            model=model_type,
            num_layers=num_layers,
        )
        for i in range(len(references))
    ]
