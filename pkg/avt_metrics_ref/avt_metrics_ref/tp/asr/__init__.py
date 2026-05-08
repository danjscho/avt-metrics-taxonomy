"""TP.ASR — ASR / Transcription metrics.

Pilot coverage:
- TP.ASR-1  Word Error Rate (WER)
- TP.ASR-2  Medical Word Error Rate (M-WER) — partial: requires user-supplied
            token classifier; the library wraps jiwer's alignment with a
            weight-matrix dimension.
- TP.ASR-3  Clinical Keyword Error Rate (CK-ER) — partial: requires
            user-supplied keyword extractor; library does the matching.
- TP.ASR-4  Demographic-Disaggregated WER
- TP.ASR-8  Character Error Rate (CER)
- TP.ASR-10 ASR Confidence Calibration (Expected Calibration Error)

Out of pilot scope:
- TP.ASR-5  Speaker-Stratified WER (needs diarisation; requires more
            shape than this pilot is taking on)
- TP.ASR-6  Error Transmission Rate (cross-stage; pipeline-level)
- TP.ASR-7  Real-Time Factor (RTF) (operational, not transcription-quality)
- TP.ASR-9  Out-of-Vocabulary (OOV) Rate
- TP.ASR-11 ASR Confidence Exposure (downstream consumer concern)
- TP.ASR-12 Hallucination-Under-Noise Rate (specialised setup; v0.2+)
- TP.ASR-13 Numeric Accuracy (overlaps with M-WER weighting)
- TP.ASR-14 Punctuation & Capitalisation Accuracy

Metrics that need user-supplied classifiers / extractors / NER models
expose the dependency in their function signature rather than embedding
a specific clinical NER. The library keeps the metric *kernel* and
defers the domain-specific model choice to the caller.
"""

from .wer import wer
from .cer import cer
from .mwer import medical_wer
from .cker import clinical_keyword_error_rate
from .disaggregated import disaggregated_wer
from .calibration import asr_confidence_calibration

__all__ = [
    "wer",
    "cer",
    "medical_wer",
    "clinical_keyword_error_rate",
    "disaggregated_wer",
    "asr_confidence_calibration",
]
