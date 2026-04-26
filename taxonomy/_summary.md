## Summary

### By Priority Tier

- **🟢 Tier 1 - Minimum Viable Assurance**: 43 metrics - what every deployer must measure to operate safely
- **🟡 Tier 2 - Recommended Assurance**: 96 metrics - recommended with reasonable governance capacity
- **🔵 Tier 3 - Advanced / Research**: 79 metrics - advanced, research, or requires infrastructure that doesn't yet exist

### By Maturity

- **Established**: 54 metrics
- **Emerging**: 48 metrics
- **Vendor-Proprietary**: 4 metrics
- **Proposed / Novel**: 108 metrics

### By Metric Family

Some groups contain named metric families - clusters of related metrics that measure facets of a shared construct. Family framings appear before the first metric of each family.

- **Clinical Content Fidelity** (Summarisation / NLP): 5 metrics - hallucination, omission, confabulation, negation, uncertainty
- **Post-Generation Correction** (Human Factors & Workflow): 4 metrics - edit rate, type, location, pattern
- **Clinical Transcription Accuracy** (ASR / Transcription): 3 metrics - WER, M-WER, CK-ER
- **Reference-Based Text Similarity** (Summarisation / NLP): 2 metrics - ROUGE, BERTScore
- **Medication Safety Thread** (cross-cutting: Summarisation / NLP → Clinical Coding → Patient Experience): 4 metrics - attribute extraction, event classification, dm+d coding, medication error differential
- **Demographic Equity Disaggregation** (cross-cutting: ASR → Clinical Coding → End-to-End → Fairness & Equity): 7 metrics - demographic WER, speaker-stratified WER, coding equity, compound demographic, accent taxonomy, intersectional performance, compound fairness
- **Unaffiliated**: 191 metrics - the remainder, not currently grouped into a named family

### By Underspecification Warning

15 existing metrics in the taxonomy carry explicit flags indicating specific measurement-science gaps. Readers should treat these as calls for caution rather than for avoidance.

- **⚠️ Tier A - No established methodology**: 3 metrics
  - Off-Label Use Detection Rate (Safety & Governance)
  - Trust Halo Decay Rate (Human Factors & Workflow)
  - Note Review Fatigue Trajectory (Human Factors & Workflow)
- **⚠️ Tier B - Concept defined, no AVT-specific validation**: 7 metrics
  - Hallucination Rate (Summarisation / NLP)
  - Medical WER (ASR / Transcription)
  - Clinical Keyword Error Rate (ASR / Transcription)
  - Cognitive Load Assessment (Human Factors & Workflow)
  - Trust Calibration Survey (Human Factors & Workflow)
  - Automation Bias Detection (Human Factors & Workflow)
  - Clinical Decision Equivalence (End-to-End Pipeline)
- **⚠️ Tier C - Technically defined, clinical validity unproven or disproven**: 5 metrics
  - ROUGE Scores (Summarisation / NLP)
  - BERTScore (Summarisation / NLP)
  - LLM-as-a-Judge (PDSQI-9 Proxy) (Summarisation / NLP)
  - Diarisation Error Rate (Diarisation)
  - Demographic-Disaggregated WER (ASR / Transcription)

