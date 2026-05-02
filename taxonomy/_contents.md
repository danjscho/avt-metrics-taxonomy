## Contents

**TP — The Technical Pipeline**

- [Audio Capture & Environment](#audio-capture-environment) (9 metrics - 1 Tier 1)
- [ASR / Transcription](#asr-transcription) (14 metrics - 2 Tier 1) *contains Clinical Transcription Accuracy and Demographic Equity Disaggregation families*
- [Diarisation](#diarisation) (9 metrics) *contains Conversation Analysis sub-cluster*
- [Summarisation / NLP](#summarisation-nlp) (24 metrics - 4 Tier 1) *contains Clinical Content Fidelity, Reference-Based Text Similarity, and Medication Safety Thread families*
- [Clinical Coding](#clinical-coding) (11 metrics - 1 Tier 1) *contains Coding Fidelity sub-cluster*
- [Downstream Write-back](#epr-write-back) (7 metrics - 4 Tier 1) *contains Write-back Safety sub-cluster*

**PI — Pipeline Interactions**

- [Partial-Pipeline](#partial-pipeline) (9 metrics)
- [End-to-End Pipeline](#end-to-end-pipeline) (12 metrics)

**HL — The Human Layer**

- [Human Factors & Workflow](#human-factors-workflow) (19 metrics - 3 Tier 1) *contains Post-Generation Correction family and Sociotechnical & Resilience sub-cluster*

**IO — Impact & Outcomes**

- [Patient Experience](#patient-experience) (10 metrics - 1 Tier 1) *contains Patient Clinical Outcomes sub-cluster*
- [Fairness & Equity](#fairness-equity) (8 metrics)

**GV — System Governance**

- [Safety & Governance](#safety-governance) (17 metrics - 6 Tier 1) *contains Longitudinal Drift & Model Contamination sub-cluster*
- [NHS Compliance & Regulatory](#nhs-compliance-regulatory) (10 metrics - 7 Tier 1) *NEW GROUP*
- [Security & Adversarial Robustness](#security-adversarial-robustness) (12 metrics)
- [Privacy & Data Governance](#privacy-data-governance) (12 metrics - 8 Tier 1)
- [Operational](#operational) (10 metrics - 3 Tier 1)
- [Environmental & Sustainability](#environmental-sustainability) (3 metrics) *NEW GROUP*
- [Training & Competency](#training-competency) (5 metrics - 1 Tier 1)
- [Vendor Transparency & Contractual](#vendor-transparency-contractual) (11 metrics - 4 Tier 1)

**ES — Evaluation Science**

- [Meta-evaluation](#meta-evaluation) (9 metrics) *contains the outcomes-evidence pair (ES.ME-8, ES.ME-9) that operationalises the [Outcomes Boundary](#outcomes-boundary)*

**Cross-cutting**

- [Applicability Classification](#applicability-classification) - which metrics are AVT-specific, which apply to any healthcare AI system
- [Standards Mapping](#standards-mapping) - assertion-level mapping to DTAC, DSPT, DCB0129/0160, NHS LLM Evaluation Framework, MHRA SaMD/AIaMD, NICE ESF, FHIR UK Core, CQC, PSIRF, PRSB, and Caldicott Principles
- [Responsible AI Lens](#responsible-ai-lens) - policy-intent view against the DSIT AI Playbook's 10 principles and the six Responsible AI ethical themes
- [Gaps & Proposed Metrics (Roadmap)](#gaps-proposed-metrics-roadmap) - consolidated register of 83 gap candidates from external coverage audits, standards mapping, and Responsible AI lens

*Several groups contain named metric families or sub-clusters. A **metric family** is a group of related metrics measuring facets of a shared construct (e.g. Clinical Content Fidelity groups Hallucination Rate, Omission Rate, Confabulation Detection, Negation Handling Accuracy, and Uncertainty Marker Preservation). Some families are cross-cutting, spanning multiple groups and pipeline layers (e.g. Medication Safety Thread spans Summarisation, Clinical Coding, and Patient Experience). Family framings appear before the first metric of each family and provide parent-construct context. A **sub-cluster** is a thematic grouping within a larger group (e.g. Conversation Analysis within Diarisation covers role identification, code-switching, turn-taking, and addressee recognition). Sub-clusters have italic introductory text before the first metric in the sub-cluster. Neither families nor sub-clusters require separate navigation - they are additive context within the existing group structure.*

---

