## Contents

**TP — The Technical Pipeline**

- [Audio Capture & Environment](#audio-capture-environment) (9 metrics — 1 Tier 1)
- [ASR / Transcription](#asr-transcription) (14 metrics — 3 Tier 1) *contains Clinical Transcription Accuracy and Demographic Equity Disaggregation families*
- [Diarisation](#diarisation) (9 metrics) *contains Conversation Analysis sub-cluster*
- [Summarisation / NLP](#summarisation-nlp) (24 metrics — 4 Tier 1) *contains Clinical Content Fidelity, Reference-Based Text Similarity, and Medication Safety Thread families*
- [Clinical Coding](#clinical-coding) (11 metrics — 1 Tier 1) *contains Coding Fidelity sub-cluster*
- [Downstream Write-back](#downstream-write-back) (8 metrics — 5 Tier 1) *contains PRSB Semantic Completeness & Write-back Fidelity family and Write-back Safety sub-cluster*

**PI — Pipeline Interactions**

- [Partial-Pipeline](#partial-pipeline) (9 metrics)
- [End-to-End Pipeline](#end-to-end-pipeline) (12 metrics)

**HL — The Human Layer**

- [Human Factors & Workflow](#human-factors-workflow) (19 metrics — 3 Tier 1) *contains Post-Generation Correction family and Sociotechnical & Resilience sub-cluster*

**IO — Impact & Outcomes**

- [Patient Experience](#patient-experience) (10 metrics — 1 Tier 1) *contains Patient Clinical Outcomes sub-cluster*
- [Fairness & Equity](#fairness-equity) (8 metrics — 1 Tier 1)

**GV — System Governance**

- [Safety & Governance](#safety-governance) (18 metrics — 7 Tier 1) *contains Longitudinal Drift & Model Contamination sub-cluster*
- [NHS Compliance & Regulatory](#nhs-compliance-regulatory) (14 metrics — 10 Tier 1) *contains members of the NHSE IG Attestation family*
- [Security & Adversarial Robustness](#security-adversarial-robustness) (12 metrics)
- [Privacy & Data Governance](#privacy-data-governance) (18 metrics — 10 Tier 1) *contains members of the NHSE IG Attestation family*
- [Operational](#operational) (10 metrics — 3 Tier 1)
- [Environmental & Sustainability](#environmental-sustainability) (3 metrics)
- [Training & Competency](#training-competency) (5 metrics — 1 Tier 1)
- [Vendor Transparency & Contractual](#vendor-transparency-contractual) (14 metrics — 7 Tier 1) *contains members of the NHSE IG Attestation family*

**ES — Evaluation Science**

- [Meta-evaluation](#meta-evaluation) (9 metrics — 1 Tier 1) *contains the outcomes-evidence pair (ES.ME-8, ES.ME-9) that operationalises the [Outcomes Boundary](#outcomes-boundary)*

**Cross-cutting**

- [Applicability Classification](#applicability-classification) — which metrics are AVT-specific, which apply to any healthcare AI system
- [Families](families.md) — eight named cross-construct groupings consolidated to one canonical home
- [Layers of Defence](layers-of-defence.md) — Prevention / Detection / Limitation framing applied per metric
- [Failure Pathways](failure-pathways.md) — three concrete failure-mode archetypes plus a day-by-day worked timeline
- [AI-Substrate Classification](ai-substrate.md) — five-class derived cut (Pre-AI / AI-Substrate / Post-AI / AI-Mediated Workflow / AI-Agnostic Governance)
- [Dimensions Overview](dimensions-overview.md) — what each per-metric dimension means and how it differs from neighbouring cuts
- [Standards Mapping](#standards-mapping) — assertion-level mapping to thirteen frameworks: DTAC, DSPT, DCB0129/0160, NHS LLM Evaluation Framework, NHS T.E.S.T., MHRA SaMD/AIaMD, NICE ESF, FHIR UK Core, CQC, PSIRF, PRSB, Caldicott Principles, and the NHS England AVT Self-Certified Supplier Registry
- [Responsible AI Lens](#responsible-ai-lens) — policy-intent view against the DSIT AI Playbook's 10 principles and the six Responsible AI ethical themes
- [Gaps & Proposed Metrics (Roadmap)](#gaps-proposed-metrics-roadmap) — 74 outstanding candidates plus 17 promoted-in-earlier-releases rows preserved as historical record at §7

*Several groups contain named metric families or sub-clusters. A **metric family** is a group of related metrics measuring facets of a shared construct (e.g. Clinical Content Fidelity groups Hallucination Rate, Omission Rate, Confabulation Detection, Negation Handling Accuracy, and Uncertainty Marker Preservation). Some families are cross-cutting, spanning multiple groups and pipeline layers (e.g. Medication Safety Thread spans Summarisation, Clinical Coding, and Patient Experience; NHSE IG Attestation spans Compliance & Regulatory, Privacy & Data Governance, and Vendor Transparency). Family framings live on the canonical [Families](families.md) page (since v5.5.0); per-metric `*See also: ... family*` italics on individual metric bodies cross-reference back to the family page. A **sub-cluster** is a thematic grouping within a larger group (e.g. Conversation Analysis within Diarisation covers role identification, code-switching, turn-taking, and addressee recognition). Sub-clusters have italic introductory text before the first metric in the sub-cluster. Neither families nor sub-clusters require separate navigation — they are additive context within the existing group structure.*

---
