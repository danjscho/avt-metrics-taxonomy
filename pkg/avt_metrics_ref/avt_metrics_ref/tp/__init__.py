"""TP cluster — Technical Pipeline (audio capture → downstream write-back).

Library coverage:

- ``tp.asr`` — TP.ASR group (WER, M-WER, CK-ER, demographic-disaggregated
  WER, CER, ASR confidence calibration). Full operationalisable subset
  of the group.
- ``tp.sn`` — TP.SN group, Reference-Based Text Similarity family only
  (ROUGE, BERTScore). The rest of TP.SN (Hallucination Rate, Omission
  Rate, LLM-Judge family, etc.) requires human-rater or LLM-call
  pipelines that this library does not yet abstract.
- ``tp.wb`` — TP.WB-2 Integration Error Rate. Other TP.WB metrics
  (write-back fidelity, field mapping accuracy, update vs append
  behaviour) need a per-EPR adapter pattern this library has not yet
  committed to.

Other TP groups (audio capture, diarisation, clinical coding) are out
of scope for the current release.
"""
