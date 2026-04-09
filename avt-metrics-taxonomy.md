# AVT Metrics Taxonomy

Comprehensive metrics for NHS ambient voice technology assurance — covering the full pipeline from audio capture to clinical record, with formal definitions, code snippets, responsible actors, tiered priority guidance, and novel proposals.

**214 metrics** across **20 groups**, organised in six parts. Includes 4 named metric families, 4 sub-clusters within existing groups, and 15 metrics carrying explicit underspecification warnings that flag specific measurement-science gaps in the published literature. Version 2 incorporates metrics responding to the January–March 2026 NHS guidance suite, the 2025–2026 evaluation science literature (SCRIBE, CREOLA, VeriFact, MedHELM, CHECK), and regulatory developments (FDA PCCP, EU AI Act high-risk provisions).

## How to Use This Taxonomy

This taxonomy is designed to serve multiple audiences — from a practice CSO deploying their first AVT system to a national body designing evaluation infrastructure. The tiering system, cadence labels, and responsible actor assignments are designed to help each reader find the metrics that are relevant, actionable, and appropriately prioritised for their role.

### Priority Tiers

Each metric is assigned to one of three priority tiers. The tier reflects a composite judgement across three dimensions: how consequential the metric is for patient safety, whether it is measurable today with existing tools and data, and what governance burden it imposes on the responsible actor. A metric can be critically important but placed in Tier 3 because the infrastructure to measure it does not yet exist — the tier reflects actionability, not importance.

**🟢 Tier 1 — Minimum Viable Assurance** (42 metrics)

The smallest set of metrics that a deployer cannot responsibly skip. Every metric in Tier 1 meets all three criteria: it addresses a safety-critical or governance-essential function, it is measurable today by the responsible actor without requiring infrastructure that doesn't yet exist, and the burden of measurement is proportionate to the risk it monitors. A deployer operating AVT without measuring these metrics is operating without adequate governance — regardless of the vendor's own quality claims.

**🟡 Tier 2 — Recommended Assurance** (87 metrics)

What a deployer or regional body should measure given reasonable governance capacity and vendor cooperation. Tier 2 metrics are important for comprehensive assurance but either require some vendor cooperation that may need contractual enforcement, involve more resource-intensive measurement methods, or provide granularity that strengthens but is not strictly essential for basic safe operation.

**🔵 Tier 3 — Advanced / Research** (85 metrics)

Metrics that are important for advancing the field but are not actionable at individual deployer level today. Tier 3 metrics fall into this category for one of three reasons: they require national infrastructure that hasn't been built, they require research methods not yet scalable to routine deployment, or they are vendor-proprietary approaches that inform what a national standard should require but cannot be independently replicated. Tier 3 is not 'unimportant' — several Tier 3 metrics address the most fundamental questions about AVT safety. They are Tier 3 because the answer to 'can a CSO do this tomorrow?' is currently no.

### Measurement Cadence

Each metric carries a cadence label indicating how often it should be measured:

**🚪 One-off gate (pre-deployment)** — measured once before go-live as an acceptance criterion. Includes hardware validation, write-back fidelity testing, acoustic environment profiling, and pre-deployment benchmarks. Gate metrics must pass before the system enters clinical use. Some should be re-tested when significant changes occur (new EPR version, hardware change, model update), but they are not continuous monitoring requirements.

**📡 Continuous** — measured on an ongoing basis during operational use, ideally automated. Includes edit rate, time-to-sign, system availability, integration error rate, model version tracking, and the automated self-consistency checks. Continuous metrics should feed into dashboards visible to the clinical lead and CSO. Many can be derived from EPR workflow telemetry without additional clinical effort.

**🔄 Periodic audit** — measured at defined intervals through deliberate assessment activity. Includes hallucination/omission rate audits, error injection testing (quarterly), trust calibration surveys (annually), demographic WER re-testing, and the safety-critical chain of custody trace. Periodic audits require protected time and clinical resource — they are the most expensive cadence and should be scheduled in advance.

The cadence and tier interact: a Tier 1 continuous metric (edit rate) is low-burden and high-value — it should be running from Day Zero. A Tier 2 periodic metric (error injection audit) is higher-burden but provides uniquely valuable data — it should be scheduled quarterly once the system is stable. A Tier 3 periodic metric (clinical decision equivalence) is too resource-intensive for routine deployment but should be performed by national evaluation programmes.

### Responsible Actors

Each metric identifies who should measure it. The same metric may appear under multiple actors with different roles:

**Vendor** — responsible for pre-deployment benchmarking, continuous system telemetry, model version transparency, and security testing. Vendors control the data and infrastructure for many metrics that deployers cannot independently assess (WER, DER, demographic disaggregation, adversarial robustness). Vendor-side metrics should be contractually specified at procurement.

**Deployer** (practice, trust, or provider) — responsible for operational monitoring that occurs at the point of clinical use: edit rates, review behaviour, patient opt-out, training compliance, and periodic clinical note audits. Deployers are the primary actor for human factors metrics because these can only be measured where the human-AI interaction occurs.

**Regional (ICB)** — responsible for cross-practice comparison, deployment equity monitoring, coding drift detection, and CSO capacity oversight. The regional tier exists because some metrics only become meaningful when aggregated across multiple deployer sites — cross-practice variance is invisible to any individual practice.

**National Body** — responsible for infrastructure that enables everyone else's metrics: establishing evaluation standards, creating independent benchmark datasets, defining LFPSE reporting categories, and funding national evaluation programmes. Many Tier 3 metrics would move to Tier 2 or Tier 1 if national infrastructure existed.

**Academic** — responsible for developing and validating new metrics, conducting the resource-intensive evaluations (clinical decision equivalence, chilling effect, skill attenuation), and providing independent evidence that is not conflicted by vendor or deployer interests.

A metric listed under 'Vendor, Deployer' typically means the vendor must provide the data or infrastructure, and the deployer must use it for governance — for example, model version tracking requires the vendor to log versions but the deployer to monitor for changes and trigger re-evaluation.

### Adapting to Local Context

Tier assignments reflect a general assessment of priority and actionability. Local context should adjust them:

A practice with a high proportion of EAL (English as Additional Language) patients should treat demographic-disaggregated WER as Tier 1 rather than Tier 2 — the equity risk is elevated for their population. A practice using AVT for multi-party consultations (interpreter-mediated, family present) should treat multi-party robustness as Tier 1 because they are routinely operating in a scenario most systems are not validated for. A practice where clinicians have been customising prompt templates should treat template underspecification and template injection vulnerability as Tier 1 because the safety case may have been invalidated by modifications. An ICB with AVT deployed across practices of varying digital maturity should prioritise cross-practice variance and deployment equity.

The principle is: if a Tier 2 or Tier 3 metric addresses a risk that is elevated in your specific context, promote it. The tiers are a starting point, not a ceiling.

A trust with multiple AVT platforms deployed across different services should prioritise Cross-Platform Fairness Consistency as Tier 1 rather than Tier 3 — the fairness concern of different patients receiving different documentation quality depending on which service happens to use which vendor is elevated for multi-platform deployments even where each platform individually performs acceptably on single-axis fairness metrics. For an integrated care system with genuinely uniform platform deployment this metric is Tier 3; for one with a mixed AVT portfolio it is Tier 1.

### ⚠️ Field-wide resource constraint

> **Only two public benchmark datasets exist for ambient scribe evaluation: ACI Bench and PriMock.** This is not a minor inconvenience. It is the single biggest structural limitation on the operationalisation of nearly every metric in this taxonomy.
>
> Inter-rater reliability is rarely reported in published AVT evaluation studies, and where it is reported, clinical experts show significant disagreement — which means the notion of a stable "gold standard" against which to measure automated metrics is itself empirically fragile. A metric that claims high correlation with expert judgment can only be as reliable as the experts themselves are with each other, and current evidence suggests that ceiling is lower than published figures imply.
>
> The practical consequences for readers of this taxonomy are three-fold:
>
> **First, cross-vendor comparisons are usually not what they appear to be.** When two vendors both claim "95% M-WER" or "97% confabulation detection", they have almost certainly used different reference datasets, different significance ontologies, different inter-rater reliability thresholds, and different evaluation protocols. Direct comparison is not meaningful. The honest position is that procurement decisions based on vendor-reported performance metrics are currently closer to vibes-based assessment than to scientific comparison — and making that visible is part of what this taxonomy is for.
>
> **Second, the field-wide cost of every unvalidated metric is high.** Because there is no shared infrastructure for validation, every deployer or researcher who wants to use a metric meaningfully must rebuild the validation locally at their own cost. This creates enormous duplication and prevents any given metric from accumulating the cross-study evidence base that would make it trustworthy. ROUGE is the canonical example — it is used almost universally in clinical NLG evaluation despite published evidence that it correlates essentially not at all with clinical judgment, because the alternative would require locally-validated replacement metrics that nobody has resources to build.
>
> **Third, this is the single highest-leverage infrastructure intervention the NHS could make.** A national investment in shared clinical encounter datasets — with multi-annotator ground truth across specialties, accents, consultation types, and clinical complexity levels — would transform operationally what nearly every metric in this taxonomy can deliver. It would make vendor-reported metrics comparable for the first time. It would make validation studies tractable for small research groups. It would make the underspecification warnings throughout this taxonomy progressively less necessary as empirical evidence replaces informed speculation. There is no individual deployer, no individual vendor, and no individual academic group that can solve this at the scale required; it is a national body responsibility.
>
> **What deployers should do in the interim.** Until shared infrastructure exists, three working practices help make the limitation manageable rather than invisible: (1) always document the reference dataset, protocol, and inter-rater reliability conditions used when reporting any metric from this taxonomy; (2) treat cross-vendor comparison of self-reported metrics with explicit scepticism in procurement documentation; (3) prefer metrics in the taxonomy that are computable against the deployer's own data (Edit Rate, Time-to-Sign Distribution, the NHS Compliance metrics, Concept Extraction Concordance) over those that require reference datasets the deployer does not have, because the former are at least internally consistent even where cross-site comparison is difficult.

## Summary

### By Priority Tier

- **🟢 Tier 1 — Minimum Viable Assurance**: 42 metrics — what every deployer must measure to operate safely
- **🟡 Tier 2 — Recommended Assurance**: 87 metrics — recommended with reasonable governance capacity
- **🔵 Tier 3 — Advanced / Research**: 85 metrics — advanced, research, or requires infrastructure that doesn't yet exist

### By Maturity

- **Established**: 54 metrics
- **Emerging**: 48 metrics
- **Vendor-Proprietary**: 4 metrics
- **Proposed / Novel**: 108 metrics

### By Metric Family

Some groups contain named metric families — clusters of related metrics that measure facets of a shared construct. Family framings appear before the first metric of each family.

- **Clinical Content Fidelity** (Summarisation / NLP): 5 metrics — hallucination, omission, confabulation, negation, uncertainty
- **Post-Generation Correction** (Human Factors & Workflow): 4 metrics — edit rate, type, location, pattern
- **Clinical Transcription Accuracy** (ASR / Transcription): 3 metrics — WER, M-WER, CK-ER
- **Reference-Based Text Similarity** (Summarisation / NLP): 2 metrics — ROUGE, BERTScore
- **Unaffiliated**: 200 metrics — the remainder, not currently grouped into a named family

### By Underspecification Warning

15 existing metrics in the taxonomy carry explicit flags indicating specific measurement-science gaps. Readers should treat these as calls for caution rather than for avoidance.

- **⚠️ Tier A — No established methodology**: 3 metrics
  - Off-Label Use Detection Rate (Safety & Governance)
  - Trust Halo Decay Rate (Human Factors & Workflow)
  - Note Review Fatigue Trajectory (Human Factors & Workflow)
- **⚠️ Tier B — Concept defined, no AVT-specific validation**: 7 metrics
  - Hallucination Rate (Summarisation / NLP)
  - Medical WER (ASR / Transcription)
  - Clinical Keyword Error Rate (ASR / Transcription)
  - Cognitive Load Assessment (Human Factors & Workflow)
  - Trust Calibration Survey (Human Factors & Workflow)
  - Automation Bias Detection (Human Factors & Workflow)
  - Clinical Decision Equivalence (End-to-End Pipeline)
- **⚠️ Tier C — Technically defined, clinical validity unproven or disproven**: 5 metrics
  - ROUGE Scores (Summarisation / NLP)
  - BERTScore (Summarisation / NLP)
  - LLM-as-a-Judge (PDSQI-9 Proxy) (Summarisation / NLP)
  - Diarisation Error Rate (Diarisation)
  - Demographic-Disaggregated WER (ASR / Transcription)

## Tier 1 — Minimum Viable Assurance (Quick Reference)

The smallest set of metrics that a deployer cannot responsibly skip. All are measurable today with existing tools, data, and governance capacity.

**Tier 1 expanded substantially with the January–March 2026 NHS guidance suite.** Nine metrics moved into Tier 1 or were added as new Tier 1 entries reflecting compliance requirements that did not exist when the taxonomy was first drafted: the NHS Compliance & Regulatory cluster (Patient Dissent Recording, Verbal Notification, AI-Generated Content Labelling, AVT Supplier Registry, ICB Engagement, Clinical Safety Case, DPIA Template, Audio Time-to-Deletion, Transcript Retention) plus Code Hallucination Rate. For NHS deployers, the shape of Day Zero minimum assurance has changed materially since early-2025 vendor procurement; re-assess existing deployments against the expanded Tier 1 set.

### Tier 1 by Responsible Actor

**Deployer** (36 metrics)

- 🚪 **Microphone & Hardware Validation** — Basic pre-deployment hardware check. No AVT should go live without confirming capture hardware meets minimum specifications. Measurable today by any deployer.
- 🔄 **Hallucination Rate** ⚠️ — Core safety metric. NAS Day Zero SPI with <2% review and ≥5% pause thresholds. Every deployer must measure this through periodic clinical audit even if methodology is manual. *See underspecification warning in full entry — the term has no universally accepted definition and reported rates across the literature span 1–67% due largely to methodological differences. Document the specific subtype taxonomy and reference dataset used.*
- 🔄 **Omission Rate** — Arguably more dangerous than hallucination because omissions are invisible to the reviewer. Must be included in periodic clinical note audit alongside hallucination rate.
- 🔄 **Negation Handling Accuracy** — Safety-critical and well-documented LLM failure mode. Should be tested pre-deployment and periodically re-audited. Negation errors directly cause clinical harm.
- 🔄 **Uncertainty Marker Preservation** — Safety-critical: certainty inflation creates false diagnostic confidence in the record. Should be tested with adversarial cases as part of pre-deployment and periodic audit.
- 🚪 **Write-back Fidelity** — Highest-priority pre-deployment gate. A hallucinated allergy written to the EPR allergy field is a system-level safety failure that propagates to every future clinical decision. Must test per EPR system before go-live.
- 📡 **Integration Error Rate** — Standard integration monitoring. Automated, low-burden, and catches data pipeline failures that directly affect patient records.
- 🚪 **Field Mapping Accuracy** — Safety-critical pre-deployment test. Wrong-field placement of safety-critical content (allergies, medications) bypasses downstream safety mechanisms entirely.
- 🚪 **Update vs Append Behaviour** — Safety-critical pre-deployment test. Must be tested per EPR system before go-live. Overwriting existing safety-critical data is a patient safety event.
- 📡 **Edit Rate (% Notes Edited)** — Primary continuous complacency indicator. Deployer-measurable from EPR workflow data. NAS Day Zero SPI. The single most important human factors metric — trajectory reveals automation bias before incidents occur.
- 📡 **Review-Before-Signing Rate** — NAS Day Zero SPI with ≥95% threshold and <85% pause trigger. Deployer-measurable from EPR workflow telemetry. Directly monitors whether human oversight is functioning.
- 📡 **Time-to-Sign Distribution** — Deployer-measurable from EPR data. The tail of very-fast approvals (<5 seconds for complex notes) is the safety-critical population. Distribution analysis detects rubber-stamping patterns.
- 📡 **Safety Performance Indicators with Thresholds (DSCMS)** — The governance mechanism that converts metrics into action. Without pre-defined thresholds and escalation paths, metrics are information without teeth. Every Tier 1 metric needs an SPI wrapper.
- 📡 **Adverse Event / Incident Rate (LFPSE)** — Established national reporting. The ultimate lagging indicator — by the time this metric moves, harm has occurred. Needs dedicated LFPSE category for AI/AVT incidents.
- 📡 **Assurance Debt Accumulation Rate** — The honest governance metric. Every deployer will accumulate it. Making it visible, tracked, and managed prevents governance theatre.
- 📡 **Patient Opt-Out Rate** — Deployer-measurable from practice records. Low-burden continuous monitoring. Rising rates signal trust issues. Demographic disaggregation reveals consent model equity.
- 📡 **Documentation Time per Consultation** — Most widely measured benefit metric. Tells you nothing about safety but essential for demonstrating value proposition. Must be reported alongside quality metrics.
- 📡 **Adoption Rate & Selective Use Patterns** — Basic deployment tracking. Selective adoption patterns (avoiding AVT for complex cases) reveal practical system boundaries and are diagnostically valuable.
- 📡 **Near-Miss Reporting Rate** — Essential leading indicator. Should be Tier 1 because it's the early warning system that LFPSE is the lagging indicator of. Requires lightweight reporting infrastructure.
- 📡 **Hazard Log Completeness** — Regulatory requirement under DCB0129. Tier 1 because it's a compliance obligation, not a recommendation. Should be linked to operational monitoring.
- 📡 **Audio Retention Compliance** — UK GDPR storage limitation requirement. Non-compliance is a regulatory breach. Deployer must verify vendor retention practices align with DPIA.
- 📡 **Consent Verification Accuracy** — CQC Mythbuster 109 requires patients to be informed. Process compliance is measurable today. Understanding gap is harder but periodic survey is feasible.
- 🚪 **Cross-Border Data Transfer Compliance** — Legal compliance requirement. Must be assessed at procurement. Non-compliance is a regulatory breach.
- 🚪 **Subject Access Request Fulfilment** — Legal compliance requirement. Must be tested before go-live to confirm vendor supports SAR fulfilment workflow.
- 🚪 **Right to Erasure Compliance** — Legal compliance requirement. Must be tested before go-live to understand erasure scope and limitations.
- 📡 **Clinician Training Completion Rate** — Governance requirement. No clinician should use AVT without completing required training. Binary compliance metric — 100% is the only acceptable target.
- 📡 **Sub-Processor Transparency** — Legal compliance requirement under UK GDPR Article 28. Must be assessed at procurement and monitored for changes.
- 🚪 **AVT Supplier Registry Listing Verification** — Procurement gate with trivial verification cost. Must be confirmed before deployment and re-verified at contract renewal. Non-listed vendors should not be deployed.
- 🚪 **ICB Engagement Documentation** — Pre-deployment compliance gate under CIO/CCIO guidance v2. Documented evidence of regional engagement required before go-live. Absence indicates governance process breakdown.
- 🔄 **Clinical Safety Case Completeness** — DCB0129/0160 regulatory requirement. The 2025 FOI finding that many NHS digital health deployments lack compliant safety cases makes active monitoring essential, not optional.
- 🚪 **DPIA Template Completion Rate** — UK GDPR Article 35 legal requirement. Use of the NHSE March 2026 template enables cross-deployment comparison and ensures mandatory considerations aren't missed.
- 📡 **Patient Dissent Recording Rate** — Per-encounter compliance with the requirement to document and respect objections. Distinct from aggregate opt-out: opt-out is a blanket choice; dissent recording is procedural integrity at the point of care. Target 100%.
- 🔄 **Verbal Notification Compliance** — Proportion of AVT consultations where verbal notification was delivered at session start. The compliance metric behind the consent model. Periodic audit via patient survey or recording sample.
- 📡 **AI-Generated Content Labelling Compliance** — Every AI-generated entry must carry the mandatory SNOMED suffix. Automated verification is trivial; non-compliance breaks downstream audit and safety investigation.
- 📡 **Audio Time-to-Deletion** — NHSE IG guidance March 2026 requires deletion after summary sign-off. Measurement makes the policy operational rather than assertive. Must verify deletion in primary storage, caches, and backups.
- 📡 **Transcript Retention Compliance** — Parallel to audio deletion but often treated as less sensitive despite being higher-risk (structured, searchable, readily consumable). Explicit retention policy required; compliance measurable continuously.

**Vendor** (20 metrics)

- 🚪 **Hallucination-Under-Noise Rate** — Critical pre-deployment test. Whisper-based systems are documented to hallucinate from silence — this must be tested before clinical use. Tier 1 because the failure mode is well-documented and the test is straightforward.
- 🚪 **Numeric Accuracy** — Safety-critical and underspecified by current vendor reporting. Should be a Day Zero acceptance criterion. Numeric errors are disproportionately dangerous and should be reported separately from general WER.
- 🔄 **Hallucination Rate** ⚠️ — Core safety metric. NAS Day Zero SPI with <2% review and ≥5% pause thresholds. Every deployer must measure this through periodic clinical audit even if methodology is manual. *See underspecification warning in full entry — the term has no universally accepted definition and reported rates across the literature span 1–67% due largely to methodological differences. Document the specific subtype taxonomy and reference dataset used.*
- 🔄 **Omission Rate** — Arguably more dangerous than hallucination because omissions are invisible to the reviewer. Must be included in periodic clinical note audit alongside hallucination rate.
- 🔄 **Negation Handling Accuracy** — Safety-critical and well-documented LLM failure mode. Should be tested pre-deployment and periodically re-audited. Negation errors directly cause clinical harm.
- 🔄 **Uncertainty Marker Preservation** — Safety-critical: certainty inflation creates false diagnostic confidence in the record. Should be tested with adversarial cases as part of pre-deployment and periodic audit.
- 📡 **Code Hallucination Rate** — Zero-tolerance metric. Any non-zero rate indicates architectural failure in generation constraints. Vendor must demonstrate 0% pre-deployment and maintain continuous monitoring. A vendor who cannot achieve zero has unconstrained code generation, which is a procurement red flag.
- 🚪 **Write-back Fidelity** — Highest-priority pre-deployment gate. A hallucinated allergy written to the EPR allergy field is a system-level safety failure that propagates to every future clinical decision. Must test per EPR system before go-live.
- 📡 **Integration Error Rate** — Standard integration monitoring. Automated, low-burden, and catches data pipeline failures that directly affect patient records.
- 🚪 **Field Mapping Accuracy** — Safety-critical pre-deployment test. Wrong-field placement of safety-critical content (allergies, medications) bypasses downstream safety mechanisms entirely.
- 🚪 **Update vs Append Behaviour** — Safety-critical pre-deployment test. Must be tested per EPR system before go-live. Overwriting existing safety-critical data is a patient safety event.
- 📡 **Model Version Tracking** — Foundation for all continuous assurance. Without knowing which model version produced which output, no performance change is interpretable. Must be contractually required.
- 📡 **System Availability / Uptime** — Standard SLA monitoring. NAS Day Zero SPI (≥99.5%). Automated, zero-burden continuous metric.
- 📡 **Audio Retention Compliance** — UK GDPR storage limitation requirement. Non-compliance is a regulatory breach. Deployer must verify vendor retention practices align with DPIA.
- 🚪 **Cross-Border Data Transfer Compliance** — Legal compliance requirement. Must be assessed at procurement. Non-compliance is a regulatory breach.
- 🚪 **Subject Access Request Fulfilment** — Legal compliance requirement. Must be tested before go-live to confirm vendor supports SAR fulfilment workflow.
- 🚪 **Right to Erasure Compliance** — Legal compliance requirement. Must be tested before go-live to understand erasure scope and limitations.
- 📡 **Model Change Notification Compliance** — Should be a contractual requirement in NHS procurement. The three-layer surveillance model depends on it. Without vendor notification, governance is reactive.
- 📡 **Incident Disclosure Compliance** — Should be a contractual requirement. Without timely incident disclosure, deployers cannot respond to vendor-side security issues.
- 📡 **Sub-Processor Transparency** — Legal compliance requirement under UK GDPR Article 28. Must be assessed at procurement and monitored for changes.

**Regional (ICB)** (2 metrics)

- 📡 **Safety Performance Indicators with Thresholds (DSCMS)** — The governance mechanism that converts metrics into action. Without pre-defined thresholds and escalation paths, metrics are information without teeth. Every Tier 1 metric needs an SPI wrapper.
- 📡 **Assurance Debt Accumulation Rate** — The honest governance metric. Every deployer will accumulate it. Making it visible, tracked, and managed prevents governance theatre.

**National Body** (1 metrics)

- 📡 **Adverse Event / Incident Rate (LFPSE)** — Established national reporting. The ultimate lagging indicator — by the time this metric moves, harm has occurred. Needs dedicated LFPSE category for AI/AVT incidents.

---

## Contents

**Part A — The Technical Pipeline**

- [Audio Capture & Environment](#audio-capture-environment) (9 metrics — 1 Tier 1)
- [ASR / Transcription](#asr-transcription) (14 metrics — 2 Tier 1) *contains Clinical Transcription Accuracy family*
- [Diarisation](#diarisation) (9 metrics) *contains Conversation Analysis sub-cluster*
- [Summarisation / NLP](#summarisation-nlp) (24 metrics — 4 Tier 1) *contains Clinical Content Fidelity and Reference-Based Text Similarity families*
- [Clinical Coding](#clinical-coding) (12 metrics — 1 Tier 1)
- [EPR Write-back](#epr-write-back) (7 metrics — 4 Tier 1)

**Part B — Pipeline Interactions**

- [Partial-Pipeline](#partial-pipeline) (9 metrics)
- [End-to-End Pipeline](#end-to-end-pipeline) (12 metrics)

**Part C — The Human Layer**

- [Human Factors & Workflow](#human-factors-workflow) (20 metrics — 3 Tier 1) *contains Post-Generation Correction family and Sociotechnical & Resilience sub-cluster*

**Part D — Impact & Outcomes**

- [Patient Experience](#patient-experience) (10 metrics — 1 Tier 1) *contains Patient Clinical Outcomes sub-cluster*
- [Fairness & Equity](#fairness-equity) (8 metrics)

**Part E — System Governance**

- [Safety & Governance](#safety-governance) (17 metrics — 6 Tier 1) *contains Longitudinal Drift & Model Contamination sub-cluster*
- [NHS Compliance & Regulatory](#nhs-compliance-regulatory) (10 metrics — 7 Tier 1) *NEW GROUP*
- [Security & Adversarial Robustness](#security-adversarial-robustness) (11 metrics)
- [Privacy & Data Governance](#privacy-data-governance) (11 metrics — 7 Tier 1)
- [Operational](#operational) (9 metrics — 3 Tier 1)
- [Environmental & Sustainability](#environmental-sustainability) (3 metrics) *NEW GROUP*
- [Training & Competency](#training-competency) (5 metrics — 1 Tier 1)
- [Vendor Transparency & Contractual](#vendor-transparency-contractual) (8 metrics — 3 Tier 1)

**Part F — Evaluation Science**

- [Meta-evaluation](#meta-evaluation) (7 metrics)

*Several groups contain named metric families or sub-clusters. A **metric family** is a group of related metrics measuring facets of a shared construct (e.g. Clinical Content Fidelity groups Hallucination Rate, Omission Rate, Confabulation Detection, Negation Handling Accuracy, and Uncertainty Marker Preservation). Family framings appear before the first metric of each family and provide parent-construct context. A **sub-cluster** is a thematic grouping within a larger group (e.g. Conversation Analysis within Diarisation covers role identification, code-switching, turn-taking, and addressee recognition). Sub-clusters have italic introductory text before the first metric in the sub-cluster. Neither families nor sub-clusters require separate navigation — they are additive context within the existing group structure.*

---

# Part A — The Technical Pipeline

## Audio Capture & Environment

*The physical layer before ASR. Microphone quality, acoustic conditions, and environmental factors that condition everything downstream.*

**Tier breakdown**: 🟢 1 Tier 1 · 🟡 4 Tier 2 · 🔵 4 Tier 3

### 🟡 Signal-to-Noise Ratio (SNR) Monitoring

Continuous measurement of audio input quality. SNR below threshold degrades ASR accuracy unpredictably — the system may continue producing confident-looking but degraded output without alerting the clinician.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Standard audio engineering; applied to AVT quality assurance |

**Why this tier?**

> Valuable continuous quality signal but requires audio analysis tooling most deployers don't have. Vendor should provide.

**Formal Definition**

```
SNR = 10 × log₁₀(P_signal / P_noise) in dB. Measured per consultation segment. Thresholds: >20dB = good; 10–20dB = acceptable with quality warning; <10dB = AVT should warn or pause. Report distribution across encounters, not just mean.
```

**Code: SNR estimation from audio**

```python
import numpy as np
import librosa

def estimate_snr(audio_path, sr=16000, frame_length=2048):
    """Estimate SNR using voice activity detection."""
    y, sr = librosa.load(audio_path, sr=sr)
    
    # Simple energy-based VAD
    energy = librosa.feature.rms(y=y, frame_length=frame_length)[0]
    threshold = np.percentile(energy, 30)  # bottom 30% = noise
    
    noise_frames = energy[energy < threshold]
    signal_frames = energy[energy >= threshold]
    
    noise_power = np.mean(noise_frames**2) if len(noise_frames) > 0 else 1e-10
    signal_power = np.mean(signal_frames**2) if len(signal_frames) > 0 else 1e-10
    
    snr_db = 10 * np.log10(signal_power / noise_power)
    
    return {
        "snr_db": round(snr_db, 1),
        "quality": "good" if snr_db > 20 else "acceptable" if snr_db > 10 else "poor",
        "alert": snr_db < 10,
        "recommendation": "Consider pausing AVT" if snr_db < 10 else None
    }
```

**Limitations**

> Simple energy-based SNR is a crude proxy — overlapping speech, reverberation, and non-stationary noise complicate measurement. Clinical environments have complex acoustic profiles.

**Novel Thinking / Implications**

> 💡 The system should degrade gracefully: if SNR drops below threshold mid-consultation, the AVT should flag the note as potentially degraded rather than producing output with false confidence. This is an architectural requirement — the AVT should know when its own input quality is insufficient.

---

### 🔵 Voice Activity Detection (VAD) Accuracy

Accuracy of detecting when speech is occurring vs silence/noise. VAD errors cause missed speech (content lost) or false activations (noise processed as speech, potentially generating hallucinated content from non-speech audio).

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard speech processing; critical for clinical AVT given variable environment |

**Why this tier?**

> Vendor-side pre-deployment testing. Deployers cannot independently assess VAD performance.

**Formal Definition**

```
VAD Precision = |true_speech_detected| / |all_detected_as_speech|. VAD Recall = |true_speech_detected| / |all_actual_speech|. False activation rate FAR = |noise_detected_as_speech| / |total_noise_duration|. Clinical risk: low recall → content loss; low precision → noise-induced hallucination.
```

**Limitations**

> VAD accuracy is environment-dependent. A VAD validated in quiet rooms may perform poorly with background conversation, equipment noise, or telephone audio.

**Novel Thinking / Implications**

> 💡 False activations are the underappreciated risk: if the VAD activates on background TV, corridor conversation, or equipment alarms, the ASR processes non-clinical audio. The summariser then has to decide what to do with transcribed noise — which may look like clinical content and get included in the note.

---

### 🟡 Acoustic Environment Profiling

Characterisation of the deployment acoustic environment against the vendor's validated acoustic conditions. Gap between validated and actual environment = unquantified risk.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Proposed — extends validated use envelope concept to acoustic conditions |

**Why this tier?**

> Deployer should characterise their acoustic environment at setup to confirm it falls within the vendor's validated conditions.

**Formal Definition**

```
Profile vector: [SNR_typical, reverberation_time_RT60, background_noise_type, speaker_distance_range, microphone_type]. Validated envelope V = vendor's tested conditions. Environment gap G = distance(actual_profile, V). G > threshold → environment outside validated envelope.
```

**Limitations**

> Acoustic conditions vary within a single practice (different rooms, open/closed doors, time of day). Point-in-time profiling may not capture the full range.

**Novel Thinking / Implications**

> 💡 This is the acoustic equivalent of the compound boundary risk model. A system validated with a lapel mic at 30cm in a quiet room may be deployed with a desk mic at 1.5m in a busy practice with a door open to the waiting room. Each acoustic parameter crossing the validated boundary compounds risk — and unlike clinical domain boundaries, acoustic boundaries are invisible to governance processes.

---

### 🔵 Bystander Voice Detection Rate

Ability to detect and flag speech from individuals who have not consented to AVT processing: patients in adjacent rooms, reception staff audible through walls, family members who arrive mid-consultation without being informed.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Patient Experience |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Identified in NHSE IG guidance on ambient scribing privacy implications; CQC Mythbuster 109 context |

**Why this tier?**

> Technology for reliable bystander detection does not yet exist. Important research direction but not actionable today.

**Formal Definition**

```
Detection rate = |bystander_speech_detected| / |total_bystander_speech|. False positive rate = |participant_speech_flagged_as_bystander| / |total_participant_speech|. Requires speaker enrolment or real-time speaker count monitoring.
```

**Limitations**

> Technically challenging — requires distinguishing expected speakers from unexpected ones without prior voice enrolment. Current diarisation can count speakers but cannot determine consent status.

**Novel Thinking / Implications**

> 💡 This sits at the intersection of audio capture, privacy, and consent. UK GDPR requires lawful basis for processing personal data — bystander speech captured and processed by AVT has no consent basis. The NHSE IG guidance (March 2026) flags this but provides no technical solution. A detection-and-redaction pipeline for non-consented speech would be architecturally significant.

---

### 🟢 Microphone & Hardware Validation

Verification that the capture hardware meets minimum specifications for the AVT system. Includes microphone frequency response, placement distance, device compatibility, and Bluetooth/connectivity reliability.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard audio hardware validation; vendor deployment requirements |

**Why this tier?**

> Basic pre-deployment hardware check. No AVT should go live without confirming capture hardware meets minimum specifications. Measurable today by any deployer.

**Formal Definition**

```
Hardware compliance checklist: (1) Frequency response 100Hz–8kHz minimum; (2) Sensitivity within vendor spec; (3) Placement within validated distance range; (4) Connectivity uptime >99.9% during sessions. Binary pass/fail per criterion.
```

**Limitations**

> Point-in-time test. Hardware degrades, batteries die mid-consultation, Bluetooth drops. Continuous hardware health monitoring is rarely implemented.

---

### 🔵 Speaker Overlap Rate

Proportion of audio time with simultaneous speech from multiple speakers. Common in real consultations (interruptions, agreement utterances, talking over) and most ASR/diarisation systems handle overlap poorly — often dropping content from one speaker entirely.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard speech processing; particularly relevant for clinical consultations |

**Why this tier?**

> Vendor pre-deployment characterisation. Deployers cannot easily measure but should understand whether their consultation style falls within the validated overlap range.

**Formal Definition**

```
Overlap Rate = T_overlap / T_total_speech, where T_overlap is the duration where >=2 speakers are simultaneously active. Report distribution across encounters. High overlap rates indicate the system is operating in conditions most benchmarks don't cover.
```

**Limitations**

> Overlap detection itself can be inaccurate. Some legitimate consultation patterns (back-channelling 'mmhm', agreement) are technically overlap but don't represent meaningful content loss.

**Novel Thinking / Implications**

> 💡 Real consultations have 5-15% overlap rates depending on style. A vendor benchmarking on scripted dyadic dialogue may report excellent performance that doesn't translate to spontaneous clinical interaction. Overlap rate should be a procurement question — what conditions was the system validated under?

---

### 🟡 Audio Clipping / Saturation Rate

Frequency of audio level exceeding the dynamic range of the capture system, causing waveform distortion. Different from SNR — clipping is a hardware/gain issue that destroys content even in quiet environments. Commonly caused by mic too close, gain set too high, or sudden loud sounds.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard audio engineering |

**Why this tier?**

> Vendor should monitor and alert. Deployer should be notified when clipping rates exceed threshold so hardware/positioning can be corrected.

**Formal Definition**

```
Clipping Rate = N_clipped_samples / N_total_samples, where clipped samples are those at or beyond the maximum amplitude (typically +/-32767 for 16-bit). Threshold for alert: >0.1% sustained over 1 second indicates significant content degradation.
```

**Code: Clipping detection**

```python
import numpy as np

def detect_clipping(audio_samples, threshold_pct=0.1):
    max_val = 32767
    near_clip = np.abs(audio_samples) >= (max_val * 0.99)
    clip_pct = (np.sum(near_clip) / len(audio_samples)) * 100
    return {
        'clipping_pct': round(clip_pct, 3),
        'alert': clip_pct > threshold_pct,
        'recommendation': 'Reduce mic gain or distance' if clip_pct > threshold_pct else None
    }
```

**Limitations**

> Modern AVT systems often use automatic gain control which masks clipping. The metric may be invisible to deployers unless the vendor exposes raw audio quality telemetry.

**Novel Thinking / Implications**

> 💡 A clipped consonant in a drug name destroys recognition deterministically. Unlike SNR-related errors which are probabilistic, clipping creates hard content loss that no downstream processing can recover.

---

### 🟡 Codec & Sampling Rate Compliance

Whether audio meets minimum bit depth and sample rate specifications for the AVT system. Telephone audio at 8kHz degrades ASR significantly compared to 16kHz studio quality. Compressed codecs (e.g. heavily lossy Bluetooth audio) introduce artifacts.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard audio engineering; vendor minimum specifications |

**Why this tier?**

> Automated check per encounter. Should be enforced architecturally — non-compliant audio should be flagged before processing.

**Formal Definition**

```
Compliance check per encounter: (1) sample_rate >= vendor_minimum (typically 16kHz); (2) bit_depth >= vendor_minimum (typically 16-bit); (3) codec in approved_codecs. Binary pass/fail per criterion. Non-compliant audio should trigger pre-processing warning or rejection.
```

**Limitations**

> Telephone consultations are increasingly common in NHS practice but most AVT systems are validated on 16kHz+ audio. The mismatch is often invisible until accuracy degrades.

**Novel Thinking / Implications**

> 💡 Telephone consultations are a hidden boundary risk. A practice using AVT for in-person consultations and then extending to telephone is operating outside the validated codec envelope. The system may produce confident-looking output of much lower accuracy.

---

### 🔵 Microphone Drift Detection

Detection of gradual hardware degradation over time: declining battery performance, mechanical wear, positioning shift, accumulated debris, Bluetooth interference patterns. Different from initial validation — this catches problems that develop after deployment.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Proposed — extends hardware validation to ongoing monitoring |

**Why this tier?**

> Conceptually valuable but requires telemetry infrastructure most vendors don't provide. Better suited for vendor-side implementation.

**Formal Definition**

```
Track baseline audio quality metrics (SNR, frequency response, noise floor) over time. Drift = significant deviation from baseline established at hardware validation. Alert if SNR drops >5dB from baseline or frequency response shifts >10%.
```

**Limitations**

> Requires establishing per-device baselines and tracking longitudinally. Most AVT systems treat hardware as a black box.

**Novel Thinking / Implications**

> 💡 Hardware degrades silently. A wireless lapel mic that worked perfectly at deployment may have degraded battery contacts six months later, producing intermittent dropout that the clinician doesn't notice but that affects ASR accuracy. Drift detection is proactive maintenance — catching the problem before it causes a clinical incident.

---

## ASR / Transcription

*Audio → text. Foundational accuracy everything depends on.*

**Tier breakdown**: 🟢 2 Tier 1 · 🟡 6 Tier 2 · 🔵 4 Tier 3

### Family: Clinical Transcription Accuracy

> **Parent construct** — how accurately the ASR layer transcribes the source audio, with clinical significance weighting that reflects the asymmetric cost of errors on clinical vs non-clinical content.
>
> The next three metrics form one family of increasing clinical sophistication. Treating them as separate unrelated metrics obscures the progression: each one answers the same fundamental question — *how many words did the ASR get wrong, and how bad were the wrong ones?* — at a different level of clinical awareness.
>
> **Three implementation levels of one construct:**
>
> 1. **Raw WER** — all word errors weighted equally. A misheard "the" counts the same as a misheard drug name. Technically rigorous and widely reported, but clinically uninformative because a 5% WER could be safe or dangerous depending on which words are wrong. Acceptable as a technical benchmark and for cross-system comparison on common test sets; inadequate as a clinical safety indicator.
>
> 2. **Medical WER (M-WER)** — errors weighted by whether the token belongs to a clinically significant class (drug names, dosages, diagnoses, safety-critical terminology). Reveals whether the system preserves the content that matters most, independent of filler and non-clinical speech accuracy. Abridge's **Medical Term Recall (MTR)** and DeepScribe's **Medical Word Hit Rate** are functionally equivalent implementations of the same underlying construct, even though they are reported under different names — a vendor reporting MTR is reporting the same thing as a vendor reporting M-WER, with different clinical term lists and weighting schemes. The **⚠️ Underspecification Warning** applies: no standardised clinical significance ontology exists, so cross-vendor M-WER comparison is not currently meaningful.
>
> 3. **Clinical Keyword Error Rate (CK-ER)** — binary per clinical keyword: was each safety-critical term captured correctly, yes or no? A more actionable variant of M-WER that can run as an automated guardrail on every encounter. Better suited to continuous monitoring than to benchmarking because its sensitivity depends entirely on the keyword dictionary used.
>
> **Cross-vendor comparability problem.** All three tiers suffer from the same fundamental issue: **without a standardised clinical term list or significance ontology, vendor-reported values are not directly comparable**. A vendor claiming 95% M-WER against one term list is not comparable to another vendor claiming 95% against a different term list. Cross-vendor procurement comparisons should either use a nationally standardised term list (which does not yet exist for NHS) or explicitly require the vendor to publish their term list and provenance alongside the reported value. This is a candidate area for NHS England or equivalent national body specification work — a canonical clinical term list mapped to SNOMED safety-critical concept classes would make the family's metrics meaningful as procurement signals for the first time.
>
> **How this family relates to other ASR metrics in the taxonomy.** Three ASR metrics sit outside this family because they measure different things:
>
> - **Character Error Rate (CER)** is orthogonal — it measures error rate at character level rather than word level, and is used to detect subword errors in medical terminology (e.g. "amoxicillin" vs "amoxycillin") that WER at the word level misses.
> - **Demographic-Disaggregated WER** and **Speaker-Stratified WER** are disaggregation axes that can be applied to any of the three metrics in this family. You can compute raw WER disaggregated by accent, or M-WER disaggregated by speaker role, etc.
> - **Numeric Accuracy** is a category-specific extension that measures accuracy on numbers (dosages, dates, vital signs). Treat it as a mandatory companion metric to Clinical Transcription Accuracy because numeric errors have outsized clinical consequences.
>
> **Metrics in this family:**
> - 🟡 **Word Error Rate (WER)** — level 1, raw. Necessary as a technical benchmark; insufficient alone for clinical safety.
> - 🔵 **Medical Word Error Rate (M-WER)** — level 2, significance-weighted. Reveals whether clinical content is preserved. Underspecified pending a standardised ontology.
> - 🔵 **Clinical Keyword Error Rate (CK-ER)** — level 3, per-keyword binary. Usable as an automated guardrail on every encounter. Underspecified pending a standardised keyword dictionary.

---

### 🟡 Word Error Rate (WER)

Standard ASR accuracy metric. Treats all word errors equally — a misheard 'the' counts the same as a misheard drug name.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard ASR literature; used in SCRIBE framework (Wang et al. 2025) |

**Why this tier?**

> Vendor should provide pre-deployment. Deployers should request but cannot independently measure without ground-truth transcripts.

**Formal Definition**

```
WER = (S + D + I) / N, where S = substitutions, D = deletions, I = insertions, N = total words in reference transcript. Computed via minimum edit distance (Levenshtein) alignment between hypothesis and reference. Values > 1.0 are possible when insertions exceed reference length.
```

**Code: WER via jiwer**

```python
from jiwer import wer, process_words

reference = "the patient reports chest pain radiating to left arm"
hypothesis = "the patient reports chess pain radiating to left hand"

error_rate = wer(reference, hypothesis)
# error_rate = 0.2 (2 substitutions / 10 words)

# For corpus-level WER across multiple utterances:
out = process_words(references_list, hypotheses_list)
corpus_wer = out.wer  # macro-averaged across utterances
```

**References**

- **NIST scoring toolkit**: [SCTK — NIST Speech Recognition Scoring Toolkit](https://github.com/usnistgov/SCTK)
- **Original**: Woodard & Nelson (1982), NBS Report

**Limitations**

> Clinically uninformative — does not weight by clinical significance. A 5% WER could be safe or dangerous depending on which words are wrong.

*See also: Medical WER (M-WER), Clinical Keyword Error Rate (CK-ER) — all members of the Clinical Transcription Accuracy family. Raw WER is level 1 of the family; the other two add clinical weighting but require a standardised significance ontology that does not yet exist.*

---

### 🔵 Medical Word Error Rate (M-WER)

Weighted WER where errors on clinically significant tokens carry higher penalty. Requires a clinical significance ontology to define token weights.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, National Body |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Proposed in OxonFair extension analysis |

**Why this tier?**

> No standardised clinical significance ontology exists. Requires national body to define weighting standard before it becomes actionable.

**Formal Definition**

```
M-WER = Σ(wᵢ · eᵢ) / Σ(wᵢ), where wᵢ is the clinical significance weight for token i, and eᵢ ∈ {0,1} indicates whether token i was incorrectly transcribed. Weights assigned from clinical ontology: safety-critical tokens (drug names, dosages, allergies) receive w >> 1; filler words receive w ≈ 0.1.
```

**Code: M-WER weighted computation**

```python
import numpy as np
from jiwer import process_words

# Clinical significance weights by SNOMED concept class
WEIGHTS = {
    "drug_name": 10.0, "dosage": 10.0,
    "allergy": 8.0, "diagnosis": 7.0,
    "red_flag_symptom": 9.0, "anatomy": 5.0,
    "filler": 0.1, "default": 1.0,
}

def classify_token(token, clinical_ner_model):
    """Map token to clinical significance class via NER."""
    entity = clinical_ner_model.predict(token)
    return WEIGHTS.get(entity, WEIGHTS["default"])

def medical_wer(ref_tokens, hyp_tokens, ner_model):
    """Compute weighted Medical WER."""
    weighted_errors = 0.0
    weighted_total = 0.0
    for i, ref_token in enumerate(ref_tokens):
        w = classify_token(ref_token, ner_model)
        weighted_total += w
        if i >= len(hyp_tokens) or ref_token != hyp_tokens[i]:
            weighted_errors += w
    return weighted_errors / weighted_total if weighted_total > 0 else 0
```

**References**

- **Concept origin**: Proposed in OxonFair healthcare voice fairness extension analysis
- **Related**: [Semantic Word Error Rate for clinical ASR (Li et al. 2022)](https://arxiv.org/abs/2207.13135)

**Limitations**

> No standardised clinical significance ontology exists. Weight assignment is inherently subjective.

**⚠️ Underspecification Warning (Tier B — no standardised weighting ontology)**

> M-WER requires a weighting ontology defining the clinical significance of token classes. **No such ontology is standardised for NHS or international use.** Abridge's Medical Term Recall (MTR) and DeepScribe's Medical Word Hit Rate are functionally equivalent implementations that use different proprietary term lists and different weighting schemes — so a vendor claiming "95% MTR" cannot be directly compared with another claiming "95% M-WER". A national body standard mapping SNOMED safety-critical concept classes to weight values would make vendor benchmarks comparable and is a candidate for NHS England or equivalent commissioning. Until then, require vendors to disclose (a) their term list and provenance, (b) the weighting scheme, and (c) the reference dataset used for M-WER computation. Refuse to compare M-WER values across vendors without this disclosure.

**Novel Thinking / Implications**

> 💡 A national body could define a standardised M-WER weighting ontology mapped to SNOMED safety-critical concept classes, making vendor benchmarks comparable.

*See also: Word Error Rate (WER), Clinical Keyword Error Rate (CK-ER) — all members of the Clinical Transcription Accuracy family. Abridge's Medical Term Recall (MTR) and DeepScribe's Medical Word Hit Rate are functionally equivalent implementations of this metric reported under different names; a vendor reporting any of these is reporting the same construct with different term lists.*

---

### 🔵 Clinical Keyword Error Rate (CK-ER)

Focused accuracy for high-stakes clinical terminology. Binary: was the keyword captured correctly or not?

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Derived from OxonFair healthcare voice fairness analysis |

**Why this tier?**

> Proposed automated guardrail. Technically feasible but requires curated keyword dictionaries and clinical NER infrastructure not yet available.

**Formal Definition**

```
CK-ER = 1 - (|K_correct| / |K_reference|), where K_reference = clinical keywords in reference (identified by NER), K_correct = subset correctly captured. Partial matches use Levenshtein similarity threshold δ ≥ 0.85.
```

**Code: CK-ER guardrail check**

```python
from medcat.cat import CAT
from Levenshtein import ratio as lev_ratio

cat = CAT.load_model_pack("path/to/medcat_model.zip")
SIMILARITY_THRESHOLD = 0.85

def extract_clinical_keywords(text):
    doc = cat.get_entities(text)
    return {ent["source_value"].lower(): ent
            for ent in doc["entities"].values()
            if ent["types"] in {"drug","dosage","allergy","diagnosis"}}

def clinical_keyword_error_rate(reference, hypothesis):
    ref_kw = extract_clinical_keywords(reference)
    hyp_kw = extract_clinical_keywords(hypothesis)
    if not ref_kw: return 0.0
    correct = sum(1 for kw in ref_kw
                  if any(lev_ratio(kw, h) >= SIMILARITY_THRESHOLD
                         for h in hyp_kw))
    return 1.0 - (correct / len(ref_kw))
```

**References**

- **Clinical NER**: [MedCAT: Medical Concept Annotation Tool](https://github.com/CogStack/MedCAT)

**Limitations**

> Requires ground-truth keyword annotation. Keyword list must be maintained as terminology evolves.

**⚠️ Underspecification Warning (Tier B — same standardisation gap as M-WER)**

> CK-ER depends on a clinical significance ontology defining which terms are keywords — no standardised ontology exists. The vendor or deployer implementing CK-ER chooses which terms count, and the resulting metric is only as good as that choice. Different keyword lists produce materially different CK-ER values for the same system, which prevents cross-vendor comparison and makes local benchmarks difficult to interpret. This metric sits in the same standardisation gap as M-WER: it is conceptually sound but requires national body specification of a canonical keyword ontology mapped to SNOMED safety-critical concept classes before it can be reported in a comparable way. In the interim, document the keyword dictionary used and its provenance when reporting CK-ER.

**Novel Thinking / Implications**

> 💡 Could run as automated post-transcription guardrail on every encounter without human review.

*See also: Word Error Rate (WER), Medical WER (M-WER) — all members of the Clinical Transcription Accuracy family. CK-ER is the most actionable variant — binary per keyword, suited to running as an automated guardrail — but is most sensitive to the choice of keyword dictionary.*

---

### 🟡 Demographic-Disaggregated WER

WER by accent group, first language, age band, and speech characteristics. NAS proposes max 5pp gap across groups.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, National Body |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | NAS framework Day Zero SPIs; NHSE IG guidance (March 2026) |

**Why this tier?**

> NAS framework requirement. Should be requested from vendor at procurement and re-tested periodically. Essential for equity assurance but requires demographic test data.

**Formal Definition**

```
For each demographic group g ∈ G, compute WER_g independently. Equity gap Δ = max(WER_g) - min(WER_g). NAS threshold: Δ < 0.05 (5 percentage points). Use bootstrap CIs given small group sizes.
```

**Code: Disaggregated WER with equity gap**

```python
import pandas as pd
from jiwer import wer
import numpy as np

def disaggregated_wer(df, ref_col, hyp_col, demo_col):
    results = {}
    for group, gdf in df.groupby(demo_col):
        refs = gdf[ref_col].tolist()
        hyps = gdf[hyp_col].tolist()
        results[group] = {"wer": wer(refs, hyps), "n": len(gdf)}
    wer_vals = [r["wer"] for r in results.values()]
    equity_gap = max(wer_vals) - min(wer_vals)
    return {
        "per_group": results,
        "equity_gap": equity_gap,
        "threshold_met": equity_gap < 0.05,  # NAS 5pp
        "worst_group": max(results, key=lambda g: results[g]["wer"]),
    }
```

**References**

- **ASR bias**: [Koenecke et al. (2020) — Racial disparities in automated speech recognition, PNAS](https://doi.org/10.1073/pnas.1915768117)
- **NAS framework**: NAS Day Zero SPIs; NHSE IG guidance (March 2026)

**Limitations**

> Vendors control test datasets. No independent UK-representative speech corpus exists at scale.

**⚠️ Underspecification Warning (Tier C — well-defined structure, ad hoc categorisation)**

> Published demographic WER reporting uses ad-hoc accent categorisation that has been systematically critiqued. A FAccT 2024 paper identified race-based, geography-based, and native/non-native categories as poor proxies for the actual acoustic variation that affects ASR performance — they are demographically convenient but phonologically arbitrary. No standardised maximum acceptable disparity threshold exists across the field; the NAS 5 percentage point target is a proposed rather than evidence-based threshold. For NHS context, a defensible taxonomy must include at minimum: British regional accents (with meaningful sub-categorisation), South Asian English varieties (distinct from "Indian English" as a single category), West African English, Caribbean English, and Eastern European English — none of which are consistently present in vendor-reported demographic WER data. The accompanying **Accent Taxonomy Standardisation** metric (Fairness & Equity) assesses whether the categorisation itself is defensible before the disaggregation numbers become meaningful.

**Novel Thinking / Implications**

> 💡 A national independent speech corpus reflecting NHS patient demographics would make vendor-reported demographic WER meaningful rather than self-assessed.

---

### 🔵 Speaker-Stratified WER

Separate WER for clinician vs patient speech. Patient speech is more diagnostically important and typically harder to transcribe.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | OxonFair extension analysis |

**Why this tier?**

> Novel proposal. Requires accurate diarisation as prerequisite and speaker-labelled ground truth that rarely exists.

**Formal Definition**

```
Given diarised transcript with speaker labels, compute WER independently per role. Clinical risk asymmetry ratio R = WER_patient / WER_clinician. R > 1.0 means the clinically riskier speech is less accurately captured.
```

**References**

- **Concept origin**: Identified in OxonFair extension analysis

**Limitations**

> Requires accurate diarisation as prerequisite.

**Novel Thinking / Implications**

> 💡 Misheard patient speech is more dangerous than misheard clinician speech. Speaker-stratified reporting would expose this asymmetry.

---

### 🟡 Error Transmission Rate

Proportion of ASR transcription errors that survive into the final clinical note. Distinct from end-to-end accuracy because it isolates the ASR→NLP propagation step — a system with high raw WER but strong contextual inference in the summariser can have a low transmission rate, while a system with low WER and literal summarisation can still transmit every error it makes.

|Dimension              |Value                                                                  |
|-----------------------|-----------------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                                 |
|**Measurement Cadence**|Periodic audit                                                         |
|**Pipeline Layer**     |ASR + Summarisation                                                    |
|**Assurance Question** |Fidelity & Accuracy                                                    |
|**Measurement Method** |Computational                                                          |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                         |
|**Responsible Actors** |Vendor                                                                 |
|**Maturity**           |Emerging                                                               |
|**Outcome Type**       |Proximal                                                               |
|**Source**             |Anderson et al., Mayo Clinic Proceedings Digital Health, 2025 (OHSU 5-platform study found 19.5% transmission rate)|

**Why this tier?**

> Vendor metric requiring intermediate output access. Measurable when raw transcript and final note are both available for comparison. Valuable diagnostic because it distinguishes ASR-bottleneck systems from summarisation-bottleneck systems — the intervention is completely different in each case.

**Formal Definition**

```
ETR = |ASR_errors_present_in_final_note| / |ASR_errors_in_raw_transcript|. ETR = 0 means the summariser corrects every ASR error (unlikely). ETR = 1 means the summariser transmits every error unchanged. ETR > 1 is possible if summariser amplification adds errors beyond the ASR baseline. Compute per error category (numeric, drug name, negation, demographic) — the overall rate obscures category-specific failure modes.
```

**Limitations**

> Requires access to raw transcript and final note with alignment between the two. Not all vendors expose the intermediate transcript. Error categorisation requires NER infrastructure.

**Novel Thinking / Implications**

> 💡 The OHSU finding that 19.5% of ASR errors reach the final note suggests the summariser provides meaningful but imperfect error correction. The more interesting question is *which* errors transmit: if safety-critical errors transmit at higher rates than stylistic errors, the summariser is learning the wrong patterns. Transmission rate disaggregated by error category is more useful than the aggregate.

### 🟡 Real-Time Factor (RTF)

Processing speed relative to audio duration. RTF < 1.0 = faster than real-time.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard ASR performance metric |

**Why this tier?**

> Vendor provides. Useful for operational monitoring but not safety-critical in isolation.

**Formal Definition**

```
RTF = T_processing / T_audio. For streaming ASR, report both first-token latency and full-utterance RTF.
```

**Limitations**

> Measures speed, not quality.

---

### 🟡 Character Error Rate (CER)

Character-level edit distance between reference and hypothesis. More sensitive than WER for medical terminology where subword errors are common: 'amoxicillin' vs 'amoxycillin' has WER=1 but CER=1/12. Particularly important for drug names, anatomical terms, and proper nouns.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard ASR literature |

**Why this tier?**

> Vendor should report alongside WER. Useful for identifying systems that struggle specifically with medical terminology spelling.

**Formal Definition**

```
CER = (S_c + D_c + I_c) / N_c, where S_c, D_c, I_c are character-level substitutions, deletions, insertions, and N_c is total characters in reference. Computed via character-level Levenshtein alignment. CER < WER typically because partial matches contribute fewer errors.
```

**Code: CER via jiwer**

```python
from jiwer import cer

reference = 'patient prescribed amoxicillin 500mg'
hypothesis = 'patient prescribed amoxycillin 500mg'

# WER would be 1/5 = 0.20 (one word wrong)
char_error_rate = cer(reference, hypothesis)
# CER ~ 0.027 (1 char wrong out of 37)
```

**References**

- **CER vs WER**: Standard ASR literature; particularly relevant for morphologically rich domains

**Limitations**

> CER and WER measure different things — neither is universally better. CER can underweight serious errors (a wrong drug name with similar spelling has low CER but high clinical risk).

**Novel Thinking / Implications**

> 💡 CER and WER should be reported together. A system with low WER but high CER is making many minor errors; a system with high WER but low CER is making fewer but more substantial errors. The clinical implications differ.

---

### 🟡 Out-of-Vocabulary (OOV) Rate

Proportion of tokens the ASR model doesn't recognise as valid vocabulary. New drug names, novel diagnoses, proper nouns, and recently approved medications are systematically OOV in older models. High OOV rate predicts systematic clinical accuracy gaps.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard speech recognition literature |

**Why this tier?**

> Should be re-tested when dm+d updates and when model versions change. Vendors should commit to maintenance schedule for vocabulary currency.

**Formal Definition**

```
OOV Rate = |tokens_not_in_vocab| / |total_tokens|. Compute against the ASR's lexicon. For end-to-end neural ASR, OOV manifests as decomposition into subword units which may produce nonsense. Track per encounter and per clinical category (drugs, diagnoses, procedures).
```

**Limitations**

> End-to-end neural ASR systems don't have explicit vocabularies — OOV is harder to define. Subword tokenisation means any word can be 'represented' but may not be transcribed correctly.

**Novel Thinking / Implications**

> 💡 Newly approved drugs (every quarter, MHRA approves new medicines) are by definition OOV until the model is updated. A model trained two years ago will systematically fail on the latest oncology agents, biologics, and recently licensed treatments. OOV rate against the current dm+d should be a procurement question.

---

### 🟡 ASR Confidence Calibration

Whether the ASR's stated confidence scores correlate with actual accuracy. A poorly-calibrated ASR that reports 95% confidence on 70%-accurate output is dangerous because downstream consumers (summariser, clinician) trust the output inappropriately.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Machine learning calibration literature |

**Why this tier?**

> Vendor should test and report. Confidence calibration is a prerequisite for confidence-based filtering and human review routing.

**Formal Definition**

```
For each confidence bin b in [0.5, 0.6, ..., 1.0], compute actual_accuracy(b) = correct_predictions(b) / total_predictions(b). Calibration Error = sum |b - actual_accuracy(b)| weighted by bin frequency. Perfect calibration: ECE = 0. Reliable systems: ECE < 0.05.
```

**References**

- **Calibration**: [Guo et al. (2017) — On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599)

**Limitations**

> Modern neural ASR systems are typically miscalibrated (overconfident). Calibration can be improved post-hoc but most vendors don't expose confidence scores at all.

**Novel Thinking / Implications**

> 💡 If confidence scores are exposed and well-calibrated, downstream systems can route low-confidence segments for human review. If they're miscalibrated or absent, the AVT cannot signal its own uncertainty — which means the clinician must assume everything is equally reliable.

---

### 🟡 ASR Confidence Exposure

Whether the ASR system exposes per-token or per-segment confidence scores to downstream consumers — both the summariser and the clinician reviewing. Different from the existing ASR Confidence Calibration metric, which asks whether confidence scores are *accurate*. Exposure asks whether they are *available at all*. Well-calibrated confidence locked inside the vendor's infrastructure provides no downstream benefit.

|Dimension              |Value                                                           |
|-----------------------|----------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                          |
|**Measurement Cadence**|One-off gate                                                    |
|**Pipeline Layer**     |ASR / Transcription                                             |
|**Assurance Question** |Safety                                                          |
|**Measurement Method** |Human Review                                                    |
|**Lifecycle Phases**   |Pre-deployment                                                  |
|**Responsible Actors** |Vendor                                                          |
|**Maturity**           |Proposed / Novel                                                |
|**Outcome Type**       |Proximal                                                        |
|**Source**             |Derived from Abridge Linked Evidence architecture; confidence-based routing literature|

**Why this tier?**

> Pre-deployment architectural question. Should be a procurement requirement for any AVT system where confidence-based review routing or uncertainty display is intended. Without exposure, the rest of the confidence-based safety architecture cannot be built.

**Formal Definition**

```
Exposure assessed on three levels: (1) Internal — confidence scores exist but are not exposed; (2) Downstream — confidence scores passed to summariser for internal use; (3) Clinician-visible — low-confidence segments highlighted in the review interface. Target: Level 3 for any safety-critical deployment. Binary per level; report highest level achieved.
```

**Limitations**

> End-to-end neural ASR systems may produce confidence scores that are poorly calibrated (see existing ASR Confidence Calibration metric). Exposure without calibration can be actively misleading — a clinician seeing "95% confidence" on a 70%-accurate segment has worse situational awareness than a clinician seeing no score at all.

**Novel Thinking / Implications**

> 💡 Confidence display is the architectural prerequisite for intelligent review. A reviewer who can see which words or segments the system is uncertain about can focus their attention there. A reviewer looking at a flat wall of text must review everything equally — which in practice means reviewing nothing carefully. Clinician-visible confidence should be a standard AVT interface element, not an advanced feature.

### 🟢 Hallucination-Under-Noise Rate

Rate at which the ASR generates plausible-sounding but fabricated text when fed noise, silence, or non-speech audio. Whisper is famously prone to this — it can produce coherent-looking transcriptions of pure silence. A distinct failure mode from substitution errors that creates content from nothing.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Koenecke et al. 2024 'Careless Whisper'; specific to neural end-to-end ASR architectures |

**Why this tier?**

> Critical pre-deployment test. Whisper-based systems are documented to hallucinate from silence — this must be tested before clinical use. Tier 1 because the failure mode is well-documented and the test is straightforward.

**Formal Definition**

```
Test corpus: known non-speech audio (silence, music, environmental noise, foreign language). Hallucination Rate = |outputs_containing_text| / |test_samples|. Severity weighted: spurious clinical content (drug names, symptoms) is more dangerous than spurious filler.
```

**References**

- **Whisper hallucinations**: [Koenecke et al. (2024) — Careless Whisper: Speech-to-Text Hallucination Harms](https://arxiv.org/abs/2402.08021)

**Limitations**

> Different from general hallucination rate at the summarisation layer. Specifically tests ASR architectural failure on silence/noise inputs.

**Novel Thinking / Implications**

> 💡 This is a specific architectural failure mode of neural ASR systems trained on aligned speech-text pairs. When fed audio that doesn't contain speech, they don't output silence — they output their best guess at what speech might have been there. The clinical implication: pauses in consultations, brief silences, or background noise can produce fabricated clinical content. Should be a hard pre-deployment test.

---

### 🟢 Numeric Accuracy

Accuracy specifically on numbers: dosages, dates, vital signs, lab values, durations. Numbers fail differently from words and have outsized clinical importance. '15mg' vs '50mg' is a tenfold dosing error invisible to standard WER weighting.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Identified as critical gap in clinical ASR evaluation |

**Why this tier?**

> Safety-critical and underspecified by current vendor reporting. Should be a Day Zero acceptance criterion. Numeric errors are disproportionately dangerous and should be reported separately from general WER.

**Formal Definition**

```
Numeric Accuracy = |numbers_correctly_transcribed| / |numbers_in_reference|. Compute separately for: integers, decimals, units (mg/g/ml/mcg), dates, ranges. Critical sub-metric: dosage accuracy (numeric value AND unit correct).
```

**Limitations**

> Requires NER to identify numeric tokens in reference and hypothesis. Spoken numbers are particularly error-prone ('fifteen' vs 'fifty', 'point five' vs 'five').

**Novel Thinking / Implications**

> 💡 The dosage error case is the canonical clinical AI safety nightmare. A standard WER calculation treats '15mg' and '50mg' as equally wrong as 'the' becoming 'a' — they're not. Numeric accuracy should be reported separately and a single dosage error should trigger immediate review of the entire encounter.

---

### 🔵 Punctuation & Capitalisation Accuracy

Accuracy of sentence boundary detection, punctuation, and capitalisation. Affects readability and downstream NLP. Misplaced sentence boundaries can completely change clinical meaning: 'no chest pain. Shortness of breath' vs 'no chest pain, shortness of breath' have different clinical implications.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard ASR post-processing literature |

**Why this tier?**

> Vendor responsibility. Important for downstream NLP quality but harder to attribute clinical impact directly.

**Formal Definition**

```
Sentence boundary F1 = harmonic mean of precision and recall on sentence boundaries. Punctuation accuracy = |correct_punctuation_marks| / |total_punctuation_in_reference|. Capitalisation accuracy = |correct_case_decisions| / |total_words|.
```

**Limitations**

> Punctuation in clinical speech is often ambiguous — clinicians don't speak in clearly punctuated sentences. Reference annotations are themselves variable.

**Novel Thinking / Implications**

> 💡 Sentence boundary errors propagate into summarisation as compounded meaning changes. A misplaced full stop can split a single clinical concept across two summarised statements, or merge two distinct concepts into one.

---

## Diarisation

*Who said what. Attribution errors cascade into summarisation.*

**Tier breakdown**: 🟡 3 Tier 2 · 🔵 1 Tier 3

### 🟡 Diarisation Error Rate (DER)

Proportion of audio time with incorrect speaker labels. Combines missed speech, false alarm, and speaker confusion.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Diarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | SCRIBE framework; standard diarisation literature |

**Why this tier?**

> Vendor pre-deployment metric. Deployer should request results, especially for multi-party scenarios relevant to their clinical context.

**Formal Definition**

```
DER = (FA + MISS + SPKR_ERR) / TOTAL. FA = false alarm time, MISS = missed speech, SPKR_ERR = speaker confusion. Optionally with 0.25s collar tolerance. NIST md-eval is the standard scorer.
```

**Code: DER via pyannote**

```python
from pyannote.metrics.diarization import DiarizationErrorRate

metric = DiarizationErrorRate(collar=0.25)
der = metric(reference_annotation, hypothesis_annotation)
# Returns: {'diarization error rate': 0.12,
#            'false alarm': 0.03,
#            'missed detection': 0.04,
#            'confusion': 0.05}
```

**References**

- **Scoring tool**: [dscore — Python NIST md-eval](https://github.com/nryant/dscore)
- **SCRIBE**: [Wang et al. (2025) — npj Digital Medicine](https://doi.org/10.1038/s41746-025-01449-w)

**Limitations**

> Challenging in multi-party consultations. Most benchmarks assume two speakers.

**⚠️ Underspecification Warning (Tier C — standard methodology, absent clinical context)**

> DER has a rigorous technical definition (NIST RT evaluation protocol) and established general benchmarks (AMI ~7.2%, CALLHOME ~12.4%), but **no clinical-specific benchmarks exist** for the multi-party consultations routinely encountered in NHS practice. No validated link has been established between DER and downstream clinical documentation quality — a low DER does not guarantee accurate speaker attribution on clinically significant utterances, and a moderate DER may be acceptable if the errors concentrate on non-clinical content. Word-level DER (WDER) is more clinically relevant than time-based DER but is rarely reported by vendors. Require WDER from vendors and request reporting stratified by utterance type: clinician instruction, patient symptom report, family contextual information, medication discussion. The aggregate DER number in isolation is technically correct but clinically uninterpretable.

---

### 🟡 Speaker Attribution Accuracy

Percentage of utterances assigned to correct speaker. Misattributed medication instructions directly cause prescribing errors.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Diarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | SCRIBE framework |

**Why this tier?**

> Vendor pre-deployment. Safety-critical for medication attribution but deployer cannot independently measure.

**Formal Definition**

```
SAA = |U_correct| / |U_total|. Unlike DER (time-based), SAA is utterance-based. Compute separately for medication-related utterances: SAA_med.
```

**References**

- **SCRIBE**: [Wang et al. (2025)](https://doi.org/10.1038/s41746-025-01449-w)

**Limitations**

> Multi-party scenarios poorly benchmarked.

**Novel Thinking / Implications**

> 💡 Medication instruction misattribution (patient reports vs clinician prescribes) deserves separate measurement as a safety-critical sub-class.

---

### 🟡 Speaker Count Accuracy

Does the system correctly identify how many speakers are present? Particularly important for distinguishing 2-speaker (validated) from 3+-speaker (out-of-envelope) consultations. Over-counting fragments single speakers; under-counting merges distinct speakers.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Diarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard diarisation evaluation |

**Why this tier?**

> Vendor pre-deployment metric. Important for any deployer routinely operating with multi-party consultations.

**Formal Definition**

```
Speaker Count Accuracy = |encounters_with_correct_count| / |total_encounters|. Detailed: |estimated_speakers - actual_speakers|. Mean Absolute Error preferred over binary accuracy.
```

**Limitations**

> Speaker count is often unknown in advance and itself estimated. Multiple ground truth annotators may disagree on speaker count for marginal cases.

**Novel Thinking / Implications**

> 💡 Speaker count is the gateway to multi-party robustness. If the system thinks there are 2 speakers when there are actually 3 (interpreter, family member), the third speaker's content is misattributed to one of the others — silently changing the clinical meaning of utterances.

---

### 🔵 Speaker Boundary Precision

Temporal accuracy of where one speaker stops and another starts. Affects attribution at turn boundaries — words at the edge of a turn may be attributed to the wrong speaker.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Diarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard diarisation literature |

**Why this tier?**

> Vendor research metric. Important for understanding diarisation quality but not directly actionable by deployers.

**Formal Definition**

```
Boundary Precision = mean temporal error (ms) between predicted and actual speaker change points. Report as distribution. NIST scoring uses 250ms collar; tighter collars expose boundary precision better.
```

**Limitations**

> Precise boundary annotation is labour-intensive. Inter-annotator agreement on exact boundaries is itself imperfect.

**Novel Thinking / Implications**

> 💡 Boundary errors are the most common cause of speaker attribution errors at turn boundaries. The first or last word of a turn is the most likely to be misattributed — and often these are the words that carry clinical meaning ('yes' to a question about symptoms, 'no' to a question about allergies).

---

---

### Conversation Analysis sub-cluster

*Multi-role identification, code-switching, turn-taking in overlap, addressee recognition, and clinically weighted attribution. Extends the existing diarisation metrics (which focus on speaker counts and boundaries) into the semantics of multi-party clinical dialogue.*

---

### 🟡 Speaker Role Identification F1

Accuracy of classifying speakers into clinical roles — clinician, patient, family member, nurse, interpreter, student — rather than just distinguishing anonymous speakers. Distinct from the existing Speaker Attribution Accuracy metric, which measures whether an utterance is assigned to the correct speaker *given that roles are known*. Role identification is the prerequisite step.

|Dimension              |Value                                                                |
|-----------------------|---------------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                               |
|**Measurement Cadence**|One-off gate                                                         |
|**Pipeline Layer**     |Diarisation                                                          |
|**Assurance Question** |Safety                                                               |
|**Measurement Method** |Computational                                                        |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                       |
|**Responsible Actors** |Vendor                                                               |
|**Maturity**           |Emerging                                                             |
|**Outcome Type**       |Proximal                                                             |
|**Source**             |mpathic.ai clinical ASR benchmark 2025; extends standard diarisation |

**Why this tier?**

> Safety-relevant whenever AVT is used outside simple dyadic consultations. Interpreter-mediated, family-present, and multidisciplinary scenarios are common in NHS practice. Role identification errors cause medication attribution errors and epistemic status inversions (patient reports vs clinician observes).

**Formal Definition**

```
Per-role precision, recall, and F1. Role set R ⊇ {clinician, patient, family_member, nurse, interpreter, student, other}. F1_macro = mean F1 across roles. Report per-role breakdown because aggregate hides minority-role failures (interpreter role is often the lowest-performing and the most safety-critical for attribution). Require minimum 0.90 F1 for clinician and patient roles; 0.80 for other identified roles.
```

**Limitations**

> Role identification often relies on content cues (who asks questions, who describes symptoms) rather than voice characteristics, which means errors correlate with atypical consultations — exactly where they matter most. Role-labelled ground truth is rarely available in clinical speech corpora.

**Novel Thinking / Implications**

> 💡 Role identification is more forgiving than individual speaker identification in one sense (you don't need to track specific individuals across sessions) but less forgiving in another (the consequences of confusing roles are semantic, not just attributional). A system that confuses "clinician" with "family member" in an interpreter-mediated consultation can end up attributing medication instructions to the wrong party.

---

### 🟡 Code-Switching Detection Rate

Accuracy of detecting within-utterance language switching — a speaker moving between English and another language mid-sentence or across turns. Common in NHS consultations with EAL patients and interpreter-mediated encounters. Code-switching confounds ASR because most systems are trained on single-language audio and may transcribe the non-English segments as phonetically similar English, or drop them entirely.

|Dimension              |Value                                                 |
|-----------------------|------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                |
|**Measurement Cadence**|One-off gate                                          |
|**Pipeline Layer**     |ASR / Transcription                                   |
|**Assurance Question** |Fairness & Equity                                     |
|**Measurement Method** |Computational                                         |
|**Lifecycle Phases**   |Pre-deployment                                        |
|**Responsible Actors** |Vendor                                                |
|**Maturity**           |Established                                           |
|**Outcome Type**       |Proximal                                              |
|**Source**             |IJCAI-22 multi-party conversation survey; multilingual ASR literature|

**Why this tier?**

> Vendor pre-deployment characterisation. Important for any NHS deployment serving linguistically diverse populations. Should be a procurement question for practices with significant EAL populations.

**Formal Definition**

```
Per utterance with code-switching: (1) detected that switching occurred (binary); (2) correctly identified the secondary language (classification); (3) transcribed both-language segments accurately. Detection Rate = |correctly_detected_switches| / |total_switches|. Transcription Accuracy Post-Switch = per-language WER for non-English segments.
```

**Limitations**

> Requires evaluation data with annotated code-switching, which is rare. Most clinical speech corpora are monolingual. NHS-representative multilingual clinical speech does not exist as a public benchmark.

**Novel Thinking / Implications**

> 💡 Code-switching is a genuine equity dimension distinct from accent. A patient with fluent English who occasionally uses terms from their first language for culturally specific concepts (family roles, traditional remedies, culturally defined symptoms) should have those terms captured, not erased. A system that silently drops non-English tokens is performing lossy documentation with equity implications — and the clinician reviewing the note has no signal that anything was lost.

---

### 🟡 Turn-Taking Accuracy in Overlap

Accuracy of attributing words spoken during overlapping speech — when two or more speakers are simultaneously active. The existing Speaker Overlap Rate metric measures how much overlap occurs; this metric measures how well the system handles it when it does. Most ASR+diarisation pipelines degrade substantially in overlap, with one speaker's content being dropped or merged into the other.

|Dimension              |Value                                          |
|-----------------------|-----------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                         |
|**Measurement Cadence**|One-off gate                                   |
|**Pipeline Layer**     |ASR + Diarisation                              |
|**Assurance Question** |Fidelity & Accuracy                            |
|**Measurement Method** |Computational                                  |
|**Lifecycle Phases**   |Pre-deployment                                 |
|**Responsible Actors** |Vendor                                         |
|**Maturity**           |Established                                    |
|**Outcome Type**       |Proximal                                       |
|**Source**             |ACL SIGDIAL 2023; standard overlap-aware ASR literature|

**Why this tier?**

> Vendor pre-deployment metric. Important for consultations with interruptions, family participation, or MDT discussions. Deployers should request overlap-specific evaluation results as part of procurement.

**Formal Definition**

```
TTA-O = |words_correctly_attributed_in_overlap| / |total_words_in_overlap|. Report alongside speaker overlap rate to contextualise. Compare with TTA-NonOverlap to quantify overlap-specific degradation: Overlap Degradation = TTA-NonOverlap - TTA-O. Values > 10 percentage points indicate the system handles overlap poorly.
```

**Limitations**

> Ground truth for overlapping speech is labour-intensive to annotate. Gold-standard transcripts of overlap often disagree among annotators. Detection of overlap segments is itself error-prone.

**Novel Thinking / Implications**

> 💡 Real clinical consultations contain 5-15% overlap. If the system handles overlap poorly and simply attributes the whole overlap to one speaker, the content from the "losing" speaker is silently dropped. A patient's quiet objection during a clinician's explanation ("but I can't afford that") may be lost entirely, with neither the clinician nor the review process aware it happened.

---

### 🔵 Clinical-Perspective HEWER (cpHEWER)

Hypothesis-Error Word Error Rate weighted by clinical importance of the utterance speaker-and-content combination. An error on a clinician's medication instruction is weighted much higher than an equivalent error on a family member's small-talk contribution. Introduced in the mpathic.ai benchmark as a clinically-aware alternative to standard diarisation error rate.

|Dimension              |Value                                       |
|-----------------------|--------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research              |
|**Measurement Cadence**|One-off gate                                |
|**Pipeline Layer**     |ASR + Diarisation                           |
|**Assurance Question** |Safety                                      |
|**Measurement Method** |Computational                               |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit              |
|**Responsible Actors** |Vendor, Academic                            |
|**Maturity**           |Emerging                                    |
|**Outcome Type**       |Proximal                                    |
|**Source**             |mpathic.ai clinical ASR benchmark 2025      |

**Why this tier?**

> Research metric. Requires both role-labelled ground truth and a clinical importance ontology — neither of which is standardised. Conceptually valuable but not operationally ready for routine deployment assessment.

**Formal Definition**

```
cpHEWER = Σ(w(role, content) × error(i)) / Σ w(role, content), where w is the clinical importance weight for the (speaker role, content type) combination. Weight matrix: clinician medication instruction = 10.0; clinician safety-netting = 10.0; patient red-flag symptom = 9.0; patient history = 5.0; family contextual information = 3.0; small talk = 0.1. Matrix requires clinical consensus.
```

**Limitations**

> Weight matrix is inherently subjective. No standardised matrix exists. Requires accurate role identification as prerequisite — compounds with Speaker Role Identification F1 errors. Benchmark datasets with the required role-and-content annotation do not exist at scale.

**Novel Thinking / Implications**

> 💡 cpHEWER is the diarisation-layer equivalent of Medical WER at the transcription layer: both attempt to weight errors by clinical consequence rather than treating all errors equally. The same standardisation gap applies — without a nationally agreed weight matrix, every vendor's cpHEWER number means something different. This is a candidate for national body specification work.

---

### 🔵 Addressee Recognition Accuracy

In multi-party consultations, correctly identifying who the speaker is addressing — the patient, a specific family member, another clinician, or the room at large. Affects the pragmatic interpretation of utterances: "you should stop smoking" addressed to the patient is a clinical instruction; addressed to a family member present it is different content entirely.

|Dimension              |Value                                            |
|-----------------------|-------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                   |
|**Measurement Cadence**|One-off gate                                     |
|**Pipeline Layer**     |Diarisation                                      |
|**Assurance Question** |Fidelity & Accuracy                              |
|**Measurement Method** |Computational                                    |
|**Lifecycle Phases**   |Pre-deployment                                   |
|**Responsible Actors** |Vendor, Academic                                 |
|**Maturity**           |Proposed / Novel                                 |
|**Outcome Type**       |Proximal                                         |
|**Source**             |Multi-party dialogue research; pragmatics literature|

**Why this tier?**

> Research frontier. No current AVT system explicitly models addressee. Academic research area — cannot be deployed in routine assessment today.

**Formal Definition**

```
For each utterance u in multi-party encounter: addressee(u) ∈ {patient, family_member_1, family_member_2, clinician, room}. Accuracy = |correctly_identified_addressee| / |total_utterances_in_multi_party_segments|. Requires turn-level annotation of addressee identity.
```

**Limitations**

> Addressee is often ambiguous even to humans — clinicians frequently address statements to "the room" without a specific target. Annotation inter-rater reliability is low. Technical solutions require multimodal input (gaze, body orientation) not available from audio alone.

**Novel Thinking / Implications**

> 💡 Addressee recognition is the pragmatic layer above speaker attribution. When a clinician turns to a family member and says "make sure she takes these at the same time each day", the instruction is for the family member, not the patient. If the AVT attributes this to the patient, the resulting note reads as a patient-directed instruction that the patient may not have even heard clearly. This kind of pragmatic misattribution is invisible to diarisation error rate but directly affects clinical documentation accuracy.

## Summarisation / NLP

*Transcript → clinical note. Where most safety-critical evaluation science concentrates.*

**Tier breakdown**: 🟢 4 Tier 1 · 🟡 8 Tier 2 · 🔵 8 Tier 3

### Family: Reference-Based Text Similarity

> **Parent construct** — the family of metrics that compare generated text to a reference text and report a similarity score. Technically rigorous; clinically weak.
>
> The next two metrics are the most widely reported automated metrics in the clinical NLG literature, and the most dangerously misleading when used in isolation. Grouping them makes explicit what the published evidence has shown repeatedly: **reference-based text similarity is a poor proxy for clinical quality in ambient scribe evaluation.**
>
> **Two implementations, one underlying limitation.** ROUGE and BERTScore differ in their matching algorithms — ROUGE uses n-gram overlap, BERTScore uses contextual embedding similarity — but they share the same fundamental weakness: they measure how closely the generated text resembles a reference text, not whether it represents clinical reality. A note can be clinically accurate while differing substantially from the reference (because the reference itself is one of many valid ways to document the encounter), or clinically wrong while closely matching the reference (because the reference was itself generated from a flawed transcript).
>
> **The published evidence is clear and damning.** Three specific findings from peer-reviewed clinical evaluation studies should govern how these metrics are used:
>
> - **ROUGE-L achieved a Kendall-Tau of 0.080** with human expert clinical judgment on clinical diagnosis generation — indistinguishable from random for practical purposes (ar5iv 2305.17364). Croxford et al. (2025, npj Digital Medicine) confirmed this pattern in clinical summarisation evaluation.
> - **Catastrophic failure modes for ROUGE** were documented with Spearman ρ between −0.66 and −0.77 in some medical contexts — meaning higher ROUGE scores actively correlated with *worse* human judgments.
> - **BERTScore-R achieved Pearson 0.62 with omission rate** (Croxford et al. 2025), which is materially better than ROUGE but still insufficient as a standalone quality indicator, and the correlation is with one specific error type rather than with overall clinical quality.
>
> The root cause is the same for both: string matching (ROUGE) and semantic similarity (BERTScore) penalise clinically valid paraphrase and reward surface overlap regardless of clinical meaning.
>
> **Why the family still exists in the taxonomy.** These metrics retain value in three specific roles: (1) technical benchmarking and regression testing during model development, where the goal is to detect regression in string or semantic overlap against a stable reference; (2) minimum-floor screening at pre-deployment, where a system scoring very badly on both is unlikely to be clinically adequate even if passing is not sufficient; (3) cross-model comparison where the reference is held constant, which controls for the reference-dependence problem. None of these roles justify using the family as the primary quality indicator in deployed clinical assurance.
>
> **The architectural rule.** Reference-based similarity metrics must be reported alongside a validated clinical instrument — PDSQI-9, CREOLA error taxonomy, or an LLM-as-a-Judge protocol that has been subjected to bias quantification. They must never be reported in isolation as evidence of clinical quality. A vendor reporting ROUGE or BERTScore as their primary or only quality metric should be treated as a procurement red flag: either they do not understand the measurement-science gap in their own field, or they are choosing the metric that flatters their system regardless of clinical relevance. Neither is compatible with NHS clinical deployment.
>
> **Metrics in this family:**
> - 🟡 **ROUGE Scores** — n-gram overlap. Technically rigorous; Kendall-Tau 0.080 with clinical judgment. Retain for benchmarking only.
> - 🔵 **BERTScore** — contextual embedding similarity. Better than ROUGE (Pearson 0.62 with omission rate) but still insufficient alone.

---

### 🟡 ROUGE Scores

N-gram overlap between generated and reference text. Demonstrably inadequate for clinical safety evaluation.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Lin 2004; inadequacy shown by Croxford et al. 2025 |

**Why this tier?**

> Vendor provides. Necessary but demonstrably insufficient alone. Should be a minimum floor, not a primary quality indicator.

**Formal Definition**

```
ROUGE-N recall = Σ Count_match(gram_n) / Σ Count(gram_n) over reference. ROUGE-L uses longest common subsequence. All range [0,1]; higher = greater overlap. Does NOT capture clinical correctness.
```

**Code: ROUGE with clinical caveat**

```python
from rouge_score import rouge_scorer

scorer = rouge_scorer.RougeScorer(
    ['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)

reference = """Patient presents with 3-day history of productive
cough, fever 38.5C. Started amoxicillin 500mg TDS for 5 days."""
hypothesis = """Patient has had a cough for 3 days with fever.
Prescribed antibiotics."""

scores = scorer.score(reference, hypothesis)
# NOTE: hypothesis omits specific drug name and dose —
# a safety-critical omission — but still scores ~0.58 ROUGE-1.
# This is exactly why ROUGE is insufficient for clinical eval.
```

**References**

- **Original**: [Lin (2004) — ROUGE: A Package for Automatic Evaluation of Summaries](https://aclanthology.org/W04-1013/)
- **Inadequacy**: Croxford et al. (2025) — LLM-as-Judge outperforms ROUGE/BERTScore

**Limitations**

> Measures lexical overlap, not clinical accuracy. Continued use as primary vendor marketing metric is a red flag.

**⚠️ Underspecification Warning (Tier C — technically rigorous, clinically invalid)**

> Published evidence demonstrates near-zero correlation between ROUGE and human clinical judgment in clinical summarisation evaluation. Croxford et al. (2025, npj Digital Medicine) reported ROUGE-L Kendall-Tau of just 0.080 with expert clinician scoring on clinical diagnosis generation — indistinguishable from random for practical purposes. A separate investigation of automated metrics for medical note generation (ar5iv 2305.17364) documented catastrophic failure modes with Spearman ρ between −0.66 and −0.77 in some medical contexts, meaning higher ROUGE scores actively correlated with worse human judgments. The root cause is that string matching penalises clinically valid paraphrase and rewards surface overlap regardless of clinical meaning. **ROUGE must not be used as a standalone clinical quality indicator.** Retain only for technical benchmarking, and always report alongside a validated clinical instrument (PDSQI-9, CREOLA, or LLM-as-a-Judge with bias quantification).

**Novel Thinking / Implications**

> 💡 Necessary but not sufficient pre-deployment screen. Tells you almost nothing about clinical safety.

*See also: BERTScore — both members of the Reference-Based Text Similarity family. Both metrics measure surface or semantic similarity to a reference text, not clinical quality. Always report alongside a validated clinical instrument (PDSQI-9, CREOLA, or LLM-as-a-Judge with bias quantification).*

---

### 🔵 BERTScore

Semantic similarity via contextual embeddings. More meaning-aware than ROUGE but still linguistic, not clinical.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Zhang et al. 2020; Croxford et al. 2025 |

**Why this tier?**

> Research metric. Shown to correlate poorly with clinical quality judgements. Adds little beyond ROUGE for practical assurance.

**Formal Definition**

```
Token-level cosine similarity between contextual embeddings. Precision, Recall, F1 computed via greedy matching with optional IDF weighting. Layer selection affects results.
```

**Code: BERTScore with clinical model**

```python
from bert_score import score

P, R, F1 = score(
    cands=[hypothesis], refs=[reference],
    model_type="microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract",
    lang="en")
# F1 tensor — higher = more semantically similar
# BUT: semantic similarity ≠ clinical correctness
```

**References**

- **Paper**: [Zhang et al. (2020) — BERTScore](https://arxiv.org/abs/1904.09675)

**Limitations**

> Linguistic similarity ≠ clinical correctness. Correlates poorly with clinician judgements.

**⚠️ Underspecification Warning (Tier C — better than ROUGE but insufficient alone)**

> BERTScore-R achieves approximately Pearson 0.62 correlation with omission rate in clinical summarisation (Croxford et al. 2025) — materially better than ROUGE but still inadequate as a standalone clinical quality indicator. The underlying limitation is the same as ROUGE: semantic similarity is not clinical correctness. A note can be semantically close to the reference while missing a clinically critical element, or semantically distant while conveying the same clinical meaning through appropriate medical abstraction. BERTScore is useful as one input to a multi-metric assessment but should never be reported as the primary quality finding. Pair with PDSQI-9 or an LLM-as-a-Judge protocol that has been subjected to bias quantification.

*See also: ROUGE Scores — both members of the Reference-Based Text Similarity family. BERTScore is materially better than ROUGE as a text similarity metric but shares the fundamental limitation: semantic closeness to a reference is not clinical correctness. Always report alongside a validated clinical instrument.*

---

### 🟡 PDSQI-9 (Physician Documentation Quality Instrument)

Nine-item validated rubric. Gold standard for human evaluation — now automatable via LLM-as-a-Judge.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Stetson et al.; Croxford et al. 2025 |

**Why this tier?**

> Validated gold-standard rubric. Resource-intensive without LLM automation. Recommended for periodic audit (quarterly sample).

**Formal Definition**

```
Nine dimensions scored 1–5 Likert: Up-to-date, Accurate, Thorough, Useful, Organised, Comprehensible, Succinct, Synthesised, Internally consistent. Composite = mean across dimensions. Published IRR: ICC 0.43–0.68.
```

**References**

- **Instrument**: [Stetson et al. (2012) — PDSQI-9, JAMIA](https://doi.org/10.1197/jamia.M2248)
- **LLM automation**: Croxford et al. (2025) — GPT-o3-mini ICC 0.818

**Limitations**

> Resource-intensive without LLM automation. NHS-context validation of automated scoring needed.

**Novel Thinking / Implications**

> 💡 GPT-o3-mini ICC 0.818 opens automated PDSQI-9 at scale — needs independent NHS validation.

---

### 🟡 CREOLA Error Taxonomy Scores

Structured error categories: omission, addition, incorrect — with sub-types. 12,999 annotated sentences. Now underpins Tortus automated guardrails.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Deployer, Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Asgari et al. 2025 (Tortus/GOSH). Now underpins automated guardrails. |

**Why this tier?**

> Most granular UK-origin error taxonomy. Recommended for deployers with access to CREOLA platform or equivalent structured review.

**Formal Definition**

```
Hierarchical taxonomy: L1 — Omission, Addition, Incorrect. L2 sub-types: Omission → {key finding, medication, allergy, plan}; Addition → {unsupported claim, confabulated detail, inferred}; Incorrect → {wrong value, wrong attribution, wrong timing}. Each sentence gets error vector. Aggregate: rate per category, severity-weighted composite.
```

**References**

- **CREOLA**: Asgari et al. (2025) — Tortus / Great Ormond Street Hospital

**Limitations**

> Developed in secondary care paediatrics. Primary care transferability needs validation.

**Novel Thinking / Implications**

> 💡 CREOLA's transition from evaluation instrument to automated guardrail shows the evaluation-to-guardrail pipeline other vendors should replicate.

---

### Family: Clinical Content Fidelity

> **Parent construct** — whether the generated note faithfully represents the clinical content of the source consultation.
>
> The next five metrics measure different facets of a single underlying construct. Treating them as unrelated obscures three important things: the existence of distinct error subtypes with different clinical implications, the difference between factuality and faithfulness, and the reason that aggregate rates can mask serious category-specific failures.
>
> **Subtypes are not substitutes.** The CREOLA framework (Asgari et al., npj Digital Medicine 2025) and the AutoscriberValidate analysis (medRxiv 2026) identify at least five distinct error subtypes within this family, each with different clinical implications and different mitigations:
>
> - **Fabrication** — completely invented clinical content with no basis in the source. CREOLA data attribute 43% of observed hallucinations to this subtype. Fictional examination findings are the canonical example. Most dangerous.
> - **Context conflation** — content misattributed between different parts of the conversation or between speakers, e.g. one patient's symptom attributed to another's discussion in a multi-encounter session. Compounds diarisation errors.
> - **Incorrect negation** — polarity reversal of a clinical assertion, e.g. "no chest pain" rendered as "chest pain". Measured by the dedicated Negation Handling Accuracy metric in this family. Directly causes clinical harm via phantom allergies, eliminated presenting symptoms, and inverted medication instructions.
> - **Speculation or inference beyond source** — plausible but unverifiable content that extends beyond what was discussed, e.g. adding a likely diagnosis the clinician never stated. The summariser is exercising clinical judgment it shouldn't.
> - **Certainty inflation** — clinician uncertainty markers ("possibly", "consistent with", "rule out") stripped from the note, converting hedged observations into definitive statements. Measured by the Uncertainty Marker Preservation metric in this family.
>
> Subtypes have different root causes (ASR vs LLM vs diarisation) and different mitigations. An aggregate "hallucination rate" of 2% means very different things if 90% of the errors are speculation vs if 90% are fabrications.
>
> **Factuality and faithfulness are distinct dimensions within the family.** Factuality is world-correctness: does the statement match clinical reality? Faithfulness is source-correctness: does the statement match what was discussed? A note can be factually correct but unfaithful (the summariser inferred a correct diagnosis the clinician never stated) or faithful but factually incorrect (the summariser accurately captured the clinician's mistake). For ambient scribes, **faithfulness is the primary assurance concern** because the scribe's job is to represent the consultation, not to exercise clinical judgment. A system that silently corrects clinician errors or adds information the clinician did not state has exceeded its safe operating scope regardless of whether the resulting statement is factually true.
>
> **Recommendation for measurement.** When measuring content fidelity in periodic audit, require subtype reporting rather than aggregate rate only. A single headline number hides the distribution that matters for intervention. Vendors reporting only aggregate rates should be asked to provide the CREOLA subtype breakdown or equivalent.
>
> **Metrics in this family:**
> - 🟢 **Hallucination Rate** — the aggregate rate of generated content unsupported by source. Entry point to the family. *See underspecification warning re: definitional instability.*
> - 🟢 **Omission Rate** — the silent killer. Arguably more dangerous than hallucination because omissions are invisible to the reviewer looking at a clean-looking note.
> - 🔵 **Confabulation Detection (Support × Severity)** — vendor-proprietary two-axis approach (Abridge) that stratifies by evidence support and clinical severity. Methodologically superior where available.
> - 🟢 **Negation Handling Accuracy** — measures the Incorrect Negation subtype as a dedicated metric because of its direct clinical harm potential.
> - 🟢 **Uncertainty Marker Preservation** — measures the Certainty Inflation subtype as a dedicated metric because certainty inflation is the more dangerous direction of epistemic drift.

---

### 🟢 Hallucination Rate

Proportion of generated content unsupported by source. Currently defined inconsistently across vendors.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Continuous, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Various; Tortus 1.47% per sentence |

**Why this tier?**

> Core safety metric. NAS Day Zero SPI with <2% review and ≥5% pause thresholds. Every deployer must measure this through periodic clinical audit even if methodology is manual.

**Formal Definition**

```
HR = |S_unsupported| / |S_total|, where S_total = atomic propositions in generated note, S_unsupported = subset not evidentially supported by source transcript. Severity: benign (formatting), moderate (non-safety addition), critical (fabricated clinical content).
```

**Code: Hallucination detection via NLI**

```python
from transformers import pipeline

nli = pipeline("text-classification",
               model="microsoft/deberta-v3-large-mnli")

def check_hallucination(source, generated_sentences):
    results = []
    for sent in generated_sentences:
        verdict = nli(f"{source} [SEP] {sent}", truncation=True)
        label = verdict[0]["label"]
        results.append({
            "sentence": sent,
            "supported": label == "ENTAILMENT",
            "flag": label in ("NEUTRAL", "CONTRADICTION"),
        })
    hr = sum(1 for r in results if r["flag"]) / len(results)
    return hr, results
# NOTE: NLI is coarse — doesn't distinguish benign
# formatting from dangerous clinical fabrication.
```

**References**

- **Tortus data**: 1.47% per sentence (Asgari et al. 2025)
- **Abridge**: Support × severity matrix (Oberst et al. 2024/2025)

**Limitations**

> Definition varies. No standard severity weighting.

**⚠️ Underspecification Warning (Tier B — conceptually central, definitionally unstable)**

> The term "hallucination" has no universally accepted operational definition in clinical NLG. The CREOLA framework (Asgari et al., npj Digital Medicine 2025) explicitly identifies this ambiguity as a fundamental measurement challenge. Reported rates across the published literature range from 1–3% in deployed ambient scribe studies to 43–67% in adversarial LLM clinical benchmarks — a span that largely reflects methodological differences rather than true performance variation. Only two public reference datasets exist for AVT hallucination evaluation (ACI Bench, PriMock), which limits cross-study comparability. Promising recent work: the CHECK framework (arXiv 2506.11129) reduced hallucination from 31% to 0.3% using information-theoretic classification with AUC 0.95–0.96 and is a candidate standard for operational definition. Until a consensus definition emerges, require reporting of: (a) the specific subtype taxonomy used (CREOLA or equivalent); (b) inter-rater reliability on the taxonomy; (c) the reference dataset; (d) the severity classification scheme.

**Novel Thinking / Implications**

> 💡 NAS proposes <2% major hallucination Day Zero SPI, ≥5% pause trigger. 'Major' needs operational definition.

*See also: Omission Rate, Confabulation Detection, Negation Handling Accuracy, Uncertainty Marker Preservation — all members of the Clinical Content Fidelity family. The CREOLA subtype taxonomy (Fabrication / Context Conflation / Incorrect Negation / Speculation / Certainty Inflation) provides the structural decomposition.*

---

### 🟢 Omission Rate

Clinically relevant source content absent from note. More dangerous than hallucination — omissions are invisible to the reviewer.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Tortus 3.45%; CREOLA taxonomy |

**Why this tier?**

> Arguably more dangerous than hallucination because omissions are invisible to the reviewer. Must be included in periodic clinical note audit alongside hallucination rate.

**Formal Definition**

```
OR = |P_missing| / |P_reference|. P_reference = clinically relevant propositions in source. Clinical relevance per CREOLA: key findings, medications, allergies, plan elements, safety-netting, red-flags are mandatory.
```

**References**

- **Tortus**: 3.45% omission rate (Asgari et al. 2025)

**Limitations**

> Harder to detect than hallucination. Automated detection at scale unsolved.

**Novel Thinking / Implications**

> 💡 The silent killer. A clean-looking note gives no cue something is missing. Argues for source-linked evidence as structural safeguard.

*See also: Hallucination Rate, Confabulation Detection, Negation Handling Accuracy, Uncertainty Marker Preservation — all members of the Clinical Content Fidelity family. Omission is the faithfulness failure that cannot be detected without source-linked evidence (see Linked Evidence / Provenance Tracing).*

---

### 🔵 Confabulation Detection (Support × Severity)

Two-axis classification: evidential support × clinical severity. Abridge model achieves 97% detection. Produces risk matrix, not single rate.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Vendor-Proprietary |
| **Outcome Type** | Proximal |
| **Source** | Abridge whitepaper (50,000+ training examples) |

**Why this tier?**

> Vendor-proprietary (Abridge). Methodologically superior two-axis approach but not independently implementable. Informs what a national standard should require.

**Formal Definition**

```
Each proposition p classified on: Support(p) ∈ {Fully Supported, Partially Supported, Unsupported, Contradicted} × Severity(p) ∈ {Benign, Moderate, Critical}. Risk R(p) = Support_weight × Severity_weight. Safety-critical quadrant: {Unsupported ∨ Contradicted} × {Critical}.
```

**References**

- **Abridge**: Oberst, Liang, Lipton (2024/2025) — 97% vs GPT-4o 82%

**Limitations**

> Proprietary. Not independently validated.

**Novel Thinking / Implications**

> 💡 Two-axis approach is methodologically superior. National standard should mandate dimensional approach even if implementation varies.

*See also: Hallucination Rate, Omission Rate, Negation Handling Accuracy, Uncertainty Marker Preservation — all members of the Clinical Content Fidelity family. The Support × Severity axes formalise what the aggregate Hallucination Rate metric leaves implicit.*

---

### 🔵 VeriFact Factual Verification

Automated EHR fact-checking via RAG + LLM-as-a-Judge. 92.7% agreement with clinicians (exceeds inter-clinician 88.5%). Open-source, locally deployable.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | LLM-as-Judge |
| **Lifecycle Phases** | Continuous, Periodic Audit |
| **Responsible Actors** | Deployer, National Body |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Chung et al., Stanford, Jan 2025; NEJM AI |

**Why this tier?**

> Most credible path to automated continuous monitoring but requires local EHR integration (FHIR R4 read access) and NHS-context validation. National pilot candidate.

**Formal Definition**

```
(1) Decompose text into atomic propositions (Llama 3.1 70B); (2) Retrieve EHR facts via BGE-M3 embeddings + Qdrant; (3) Classify each: Supported / Not Supported / Not Addressed. Validated: 100 MIMIC-III patients, 13,070 statements.
```

**Code: VeriFact conceptual pipeline**

```python
# https://github.com/philipchung/verifact

# Step 1: Decompose into atomic propositions
from verifact.decompose import PropDecomposer
decomposer = PropDecomposer(model="llama-3.1-70b")
props = decomposer.decompose(clinical_text)

# Step 2: Retrieve EHR evidence
from verifact.retrieve import EHRRetriever
retriever = EHRRetriever(
    embedding_model="BAAI/bge-m3",
    vector_db="qdrant",
    ehr_data=patient_records)

# Step 3: Classify each proposition
from verifact.verify import FactVerifier
verifier = FactVerifier(model="llama-3.1-70b")
for prop in props:
    evidence = retriever.retrieve(prop, top_k=5)
    result = verifier.classify(prop, evidence)
    # -> "Supported" | "Not Supported" | "Not Addressed"
```

**References**

- **NEJM AI**: [Chung et al. (2025) — VeriFact](https://ai.nejm.org/doi/full/10.1056/AIdbp2500418)
- **Code**: [GitHub — philipchung/verifact](https://github.com/philipchung/verifact)

**Limitations**

> Validated on MIMIC-III (US ICU). NHS primary care transferability untested. Requires FHIR R4 read access.

**Novel Thinking / Implications**

> 💡 Most credible path to automated continuous faithfulness monitoring. Open-source = no vendor dependency. National pilot would generate first independent continuous accuracy data.

---

### 🟡 LLM-as-a-Judge (PDSQI-9 Proxy)

Reasoning LLMs scoring documentation at 27× speed (22s vs 600s). Enables 100% note evaluation.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | LLM-as-Judge |
| **Lifecycle Phases** | Continuous, Periodic Audit |
| **Responsible Actors** | Deployer, National Body |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Croxford et al. 2025 |

**Why this tier?**

> 27× speed improvement enables practical scale. Recommended for deployers with API access. Needs NHS-context validation of scoring calibration.

**Formal Definition**

```
Reasoning LLM prompted with PDSQI-9 rubric scores each note on 9 dimensions. ICC = 0.818 (o3-mini) vs 0.43 (human-human). Non-reasoning models achieve substantially lower agreement.
```

**References**

- **Study**: Croxford et al. (2025) — npj Digital Medicine

**Limitations**

> One LLM evaluating another = correlated failure modes. Evaluation LLM should be different model family.

**⚠️ Underspecification Warning (Tier C — high measured reliability, unknown validity)**

> LLM-as-a-Judge has documented biases that are rarely quantified in published deployment: position bias (prefers the first response in pairwise comparison), verbosity bias (prefers longer responses), self-enhancement bias (prefers outputs from the same model family as the judge), and fine-grained scoring unreliability (inconsistent discrimination at the high end of Likert scales). The headline Croxford et al. (2025) finding of GPT-o3-mini achieving ICC 0.818 with human evaluators on PDSQI-9 should be read alongside a separate Rwanda clinical LLM evaluation study that found LLM judges correlated more strongly with non-expert than expert annotators — apparent reliability that may reflect alignment with a particular class of evaluator rather than with clinical ground truth. This is the most uncomfortable possibility in automated evaluation: high ICC with humans that does not generalise to correctness. Any deployment relying on LLM-as-a-Judge for safety-relevant decisions should run the proposed **LLM-Judge Bias Quantification** metric (see Meta-evaluation section) and document residual uncertainty before treating judge outputs as substitutes for expert review.

**Novel Thinking / Implications**

> 💡 27× speed enables 100% evaluation. But meta-problem: correlated blindspots between evaluator and evaluated.

---

### 🔵 MedHELM LLM-Jury

121 tasks, 22 subcategories. LLM-jury ICC 0.47 exceeds clinician-clinician 0.43. Capability gate, not deployment evidence.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | LLM-as-Judge |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor, National Body |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Bedi et al., Stanford CRFM, May 2025 |

**Why this tier?**

> Research benchmark for pre-deployment capability gating. Vendor responsibility. Value is as minimum capability floor, not deployment safety evidence.

**Formal Definition**

```
Holistic Evaluation of Language Models for Medicine. LLM-jury: panel of LLMs independently scores, aggregated via majority/mean. Available via Microsoft MedEvals on Azure AI Foundry.
```

**References**

- **Paper**: [Bedi et al. (2025) — MedHELM, Stanford CRFM](https://arxiv.org/abs/2505.23802)

**Limitations**

> Benchmarks ≠ deployment. MEDIC knowledge-execution gap is the critical caveat.

**Novel Thinking / Implications**

> 💡 Value is as minimum capability gate, not deployment safety evidence.

---

### 🔵 MEDIC Cross-Examination

One LLM interrogates another to detect hallucinations without references. Identifies the 'knowledge-execution gap'.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | LLM-as-Judge |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Kanithi et al. 2025 |

**Why this tier?**

> Research framework. Knowledge-execution gap finding is important but MEDIC methodology is not yet deployable outside research settings.

**Formal Definition**

```
Examiner LLM probes claims in target output, evaluates consistency. Knowledge-execution gap KE = benchmark_accuracy - operational_accuracy.
```

**References**

- **Paper**: Kanithi et al. (2025) — MEDIC

**Limitations**

> Correlated blindspots possible.

**Novel Thinking / Implications**

> 💡 Knowledge-execution gap: exam performance ≠ operational performance. Pre-deployment benchmarks are structurally insufficient.

---

### 🟡 Linked Evidence / Provenance Tracing

Every text span linked to source audio. Architectural safety property — transforms review from 'looks right?' to 'is this supported?'

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Vendor-Proprietary |
| **Outcome Type** | Proximal |
| **Source** | Abridge Linked Evidence |

**Why this tier?**

> Architectural safety property. Should be a procurement requirement — provenance tracing transforms review quality. Vendor must provide.

**Formal Definition**

```
For each span sᵢ, mapping M(sᵢ) → {(t_start, t_end)}. Requirements: Coverage (every span has ≥1 link), Relevance (linked segments contain evidence), Accessibility (≤2 interactions to inspect).
```

**References**

- **Abridge**: Abridge Linked Evidence architecture

**Limitations**

> Proprietary. Requires audio retention. Depends on clinician usage.

**Novel Thinking / Implications**

> 💡 National standard should require provenance tracing as architectural requirement.

---

### 🔵 SCRIBE Framework Composite

First comprehensive multi-modal AVT evaluation: simulation + computational + human + LLM. Minimum standard for pre-deployment.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Academic, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Wang et al. 2025 (Duke/MedStar) |

**Why this tier?**

> Comprehensive research framework. Should be the aspiration for pre-deployment evaluation but requires simulation infrastructure no NHS deployer currently has.

**Formal Definition**

```
Four modalities: (1) Simulated encounters with ground truth; (2) Computational metrics on outputs; (3) Structured clinician review; (4) LLM evaluation. Composite requires passing all four — no single modality compensates for another.
```

**References**

- **Paper**: [Wang et al. (2025) — SCRIBE, npj Digital Medicine](https://doi.org/10.1038/s41746-025-01449-w)

**Limitations**

> Complex to implement. Research framework, not deployable toolkit.

**Novel Thinking / Implications**

> 💡 Demonstrates no single modality is sufficient. Should be minimum pre-deployment standard.

---

### 🟡 Template Modification Underspecification Score

INSYTE underspecification delta when clinicians modify AVT templates. Every modification potentially invalidates the safety case.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer, Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | INSYTE analysis; DCB0129 gap |

**Why this tier?**

> Relevant whenever deployers allow template customisation. Must monitor if templates are configurable — every modification potentially invalidates the safety case.

**Formal Definition**

```
For default template T₀ with INSYTE underspecification U₀, modified template T' with U': ΔU = U' - U₀. If ΔU > threshold, modified template exits validated safety envelope → re-evaluation required under DCB0129.
```

**References**

- **INSYTE**: INSYTE autonomy classification — DCB0129 structural gap

**Limitations**

> Not yet operationalised for routine use.

**Novel Thinking / Implications**

> 💡 Hidden risk vector: template customisation as feature, but every modification potentially invalidates safety case.

---

### 🟢 Negation Handling Accuracy

Does the summary correctly preserve negations? 'No chest pain' vs 'chest pain' is a clinically critical distinction that LLMs commonly mishandle, particularly when negation is far from the negated concept.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Clinical NLP literature; identified as systematic LLM failure mode |

**Why this tier?**

> Safety-critical and well-documented LLM failure mode. Should be tested pre-deployment and periodically re-audited. Negation errors directly cause clinical harm.

**Formal Definition**

```
For each negated concept in reference: Negation Preserved = (concept appears in summary) AND (negation marker correctly attached). Negation Accuracy = |correctly_negated| / |total_negations|. Failure modes: dropped negation (becomes positive), added negation (becomes negative), wrong scope.
```

**References**

- **Negation in clinical NLP**: ConText algorithm (Harkema et al.); standard clinical NLP problem

**Limitations**

> Negation detection itself is imperfect. Clinical negation has subtleties: hedged negation ('unlikely to be'), conditional negation ('if no improvement'), historical negation ('previously denied').

**Novel Thinking / Implications**

> 💡 Negation handling is the single most clinically dangerous LLM failure mode. A summary that drops 'no' from 'no allergies' creates a phantom allergy. A summary that adds 'no' to 'has chest pain' eliminates a presenting symptom. Both can cause direct harm. This deserves dedicated testing with adversarially constructed test cases — sentences specifically designed to challenge negation handling.

*See also: Hallucination Rate, Omission Rate, Confabulation Detection, Uncertainty Marker Preservation — all members of the Clinical Content Fidelity family. Negation failure is one subtype (Incorrect Negation) made explicit as a dedicated metric because of its direct clinical harm potential.*

---

### 🟡 Temporal Accuracy

Preservation of when things happened. 'Patient had chest pain three weeks ago' vs 'patient has chest pain' is the difference between historical and presenting complaint. LLMs frequently collapse temporal markers when summarising.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Clinical NLP literature on temporal expression extraction |

**Why this tier?**

> Important clinical distinction but harder to measure than negation. Requires temporal expression annotation. Should be part of periodic audit.

**Formal Definition**

```
For each temporal expression in reference: Temporal Accuracy = (time reference present in summary) AND (temporal relationship preserved). Categories: absolute time (dates), relative time (days/weeks ago), duration (for X days), tense (present/past/historical).
```

**Limitations**

> Temporal expressions are diverse and ambiguous. 'Recently' can mean different things in different clinical contexts.

**Novel Thinking / Implications**

> 💡 Temporal collapse is a subtle but dangerous failure mode. 'Patient had a heart attack five years ago' becoming 'patient has had a heart attack' loses the time information that distinguishes acute from historical. The clinical implications differ entirely. This is particularly relevant for problem list management — historical conditions should not be coded as active.

---

### 🟡 Temporal Event Ordering Accuracy

Accuracy of reconstructing the chronological sequence of clinical events from non-linear conversation. Patients rarely describe symptoms in temporal order — they jump between current symptoms, historical episodes, family history, and future concerns. The summary must impose a coherent timeline. Distinct from the existing Temporal Accuracy metric, which covers tense and time-marker preservation at the sentence level; this metric covers event sequencing across the whole note.

|Dimension              |Value                                                   |
|-----------------------|--------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                  |
|**Measurement Cadence**|Periodic audit                                          |
|**Pipeline Layer**     |Summarisation                                           |
|**Assurance Question** |Safety                                                  |
|**Measurement Method** |Hybrid                                                  |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                          |
|**Responsible Actors** |Vendor, Deployer                                        |
|**Maturity**           |Emerging                                                |
|**Outcome Type**       |Proximal                                                |
|**Source**             |i2b2 2012 temporal challenge (F1 0.876 state of art); clinical temporal reasoning literature|

**Why this tier?**

> Important clinical reasoning dimension. Established benchmark methodology exists (i2b2). Periodic audit feasible with annotated test cases.

**Formal Definition**

```
Given a set of clinical events E extracted from source, and their true temporal ordering T_ref, compute the summary's inferred ordering T_hyp. Accuracy = Kendall's tau between T_ref and T_hyp. Report: pairwise ordering accuracy (what proportion of event pairs are correctly ordered), plus anchor events accuracy (events with absolute timestamps correctly placed).
```

**Limitations**

> Ground truth temporal annotation is labour-intensive. Some event orderings are legitimately ambiguous (patient doesn't remember). Automated temporal extraction for evaluation adds its own error.

**Novel Thinking / Implications**

> 💡 Event ordering is the difference between "patient had MI, then developed chest pain" and "patient developed chest pain, then had MI". Same events, completely different clinical meaning. Summarisation LLMs frequently collapse temporal structure when compressing, producing notes where causality is implied by proximity rather than by explicit ordering.

### 🟡 Quantifier Preservation

Preservation of clinical qualifiers: 'occasional', 'frequent', 'constant', 'mild', 'moderate', 'severe', 'intermittent'. LLMs often drop or paraphrase these, losing diagnostic information that affects clinical reasoning.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Identified as systematic LLM summarisation failure mode |

**Why this tier?**

> Important quality dimension that current metrics don't capture. Periodic audit recommended. Annotated test cases would be straightforward to construct.

**Formal Definition**

```
For each quantifier in reference: Quantifier Preservation = (quantifier present in summary) OR (semantically equivalent quantifier present). Track: dropped quantifiers, paraphrased quantifiers (acceptable), replaced quantifiers (unacceptable — changes severity).
```

**Limitations**

> Quantifier semantics are imprecise. Clinical training varies in how quantifiers are interpreted.

**Novel Thinking / Implications**

> 💡 'Occasional headaches' becoming 'headaches' loses the frequency information that distinguishes a normal variant from a clinical concern. 'Severe' becoming 'present' eliminates the severity assessment. These dropped qualifiers compound across the note — by the end, the clinical picture has been subtly distorted in ways that affect downstream decisions.

---

### 🟡 Medication Attribute Extraction F1

Per-attribute accuracy for each component of a medication reference: drug name, dose, route, frequency, duration, indication, and start/stop dates. Each attribute is scored independently with its own F1. The medication as a whole is only fully correct if all attributes are correct — and aggregate medication accuracy masks systematic attribute-level failures (e.g. systems that get drug names right but frequencies wrong).

|Dimension              |Value                                                        |
|-----------------------|-------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                       |
|**Measurement Cadence**|Periodic audit                                               |
|**Pipeline Layer**     |Summarisation                                                |
|**Assurance Question** |Safety                                                       |
|**Measurement Method** |Computational                                                |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                               |
|**Responsible Actors** |Vendor                                                       |
|**Maturity**           |Established                                                  |
|**Outcome Type**       |Proximal                                                     |
|**Source**             |n2c2 shared task benchmarks (attribute-level F1 >0.92 for strong systems)|

**Why this tier?**

> Established methodology. Should be a standard vendor pre-deployment metric. Periodic re-testing captures drug vocabulary currency.

**Formal Definition**

```
For each medication mention m with attributes A = {name, dose, route, frequency, duration, indication}: per-attribute precision and recall against reference. Composite: full-match rate = |medications_all_attributes_correct| / |total_medications|. Safety-critical: dose accuracy and frequency accuracy should be reported with CIs; any system below 0.95 on these should not deploy without enhanced review.
```

**Limitations**

> Requires NER infrastructure mapping to dm+d and SNOMED medication concepts. Annotation is labour-intensive. Free-text dosing instructions ("take as needed", "titrate to response") are harder to score than structured doses.

**Novel Thinking / Implications**

> 💡 Aggregate medication accuracy is a misleading single number. A system with 95% medication accuracy could be getting drug names right 99% of the time and doses right 92% of the time — and the 8% dose error rate is the safety-critical finding. Attribute-level breakdown is necessary for safety assurance.

### 🟢 Uncertainty Marker Preservation

Does the summary maintain clinician diagnostic uncertainty ('possibly', 'suggestive of', 'consistent with', 'rule out', 'unlikely to be') rather than collapsing to definitive statements? Loss of uncertainty markers creates false certainty in the record.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Clinical NLP hedging/uncertainty literature |

**Why this tier?**

> Safety-critical: certainty inflation creates false diagnostic confidence in the record. Should be tested with adversarial cases as part of pre-deployment and periodic audit.

**Formal Definition**

```
For each uncertainty marker in reference: Marker Preservation = (uncertainty marker present in summary) AND (epistemic level preserved). Failure modes: certainty inflation (uncertain -> certain), certainty deflation (certain -> uncertain), marker substitution (changes epistemic meaning).
```

**Limitations**

> Uncertainty markers are subtle and easily missed by both humans and machines. The boundary between hedged and unhedged statements is fuzzy.

**Novel Thinking / Implications**

> 💡 Certainty inflation is the more dangerous direction. When 'possibly viral, consider antibiotics if no improvement' becomes 'viral, no antibiotics needed' the clinical management plan is fundamentally altered. The summariser has effectively made a diagnostic decision that the clinician explicitly hedged on. This connects to epistemic status preservation but is more granular.

*See also: Hallucination Rate, Omission Rate, Confabulation Detection, Negation Handling Accuracy — all members of the Clinical Content Fidelity family. Certainty Inflation is the subtype most likely to cause diagnostic anchoring in downstream clinicians reading the note.*

---

### 🟡 Medication Event Classification

Classification of medication *actions* discussed in a consultation: start, stop, increase, decrease, continue, hold, restart, allergy/contraindication. Distinct from medication attribute extraction, which captures what the medication is; event classification captures what is being *done* with it. A medication mentioned as "we'll stop this one" is not the same as "we'll keep this one" — the attributes may be identical but the clinical action is opposite.

|Dimension              |Value                                              |
|-----------------------|---------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                             |
|**Measurement Cadence**|Periodic audit                                     |
|**Pipeline Layer**     |Summarisation                                      |
|**Assurance Question** |Safety                                             |
|**Measurement Method** |Computational                                      |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                     |
|**Responsible Actors** |Vendor                                             |
|**Maturity**           |Established                                        |
|**Outcome Type**       |Proximal                                           |
|**Source**             |n2c2 2018 shared task on medication event classification|

**Why this tier?**

> Established methodology. Safety-critical because event misclassification directly causes prescribing errors. Should be standard vendor pre-deployment reporting.

**Formal Definition**

```
For each medication event discussed: classification into {start, stop, increase, decrease, continue, hold, restart, contraindication, refuse}. Multiclass F1 per class. Safety-critical confusions: start↔stop and increase↔decrease are the most dangerous failure modes. Report confusion matrix, not just aggregate accuracy.
```

**Limitations**

> Implicit medication events (not explicitly stated but inferred from context) are harder to classify than explicit statements. Conditional events ("stop this if symptoms worsen") require understanding conditional structure.

**Novel Thinking / Implications**

> 💡 The start↔stop confusion is the canonical AVT safety nightmare. A consultation discussion of "we're going to stop your warfarin and start apixaban instead" that is silently inverted by the summariser produces a note that documents starting warfarin and stopping apixaban — both incorrect, both dangerous, and neither flagged by attribute-level accuracy metrics. Event classification should be a mandatory safety gate.

### 🔵 Style & Format Consistency

Does the system produce notes in the same structure each time? Inconsistency increases cognitive load for review and makes it harder for clinicians to develop efficient review patterns.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Human factors literature on documentation consistency |

**Why this tier?**

> Quality of life metric. Important for review efficiency but not safety-critical.

**Formal Definition**

```
Structural similarity across notes from the same template/configuration. Section presence consistency, ordering consistency, formatting consistency (bullet vs prose, headers, etc.). Report as variance metric across encounters.
```

**Limitations**

> Some legitimate variation is desirable — different consultations need different structures. Distinguishing legitimate variation from inappropriate inconsistency is judgement-based.

**Novel Thinking / Implications**

> 💡 Cognitive load research shows that consistent visual structure dramatically improves review efficiency. A note that always has 'History' followed by 'Examination' followed by 'Plan' allows clinicians to develop scanning patterns. A note that varies its structure forces re-orientation each time, increasing review time and reducing review quality.

---

### 🔵 Length Appropriateness

Over-summarisation (losing detail) vs under-summarisation (verbatim transcript). Should be calibrated to consultation complexity — a 5-minute follow-up needs less than a 30-minute new patient assessment.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Identified as quality dimension not captured by accuracy metrics |

**Why this tier?**

> Continuous statistical monitoring is feasible but interpretation is context-dependent. Better suited for trend monitoring than threshold-based alerting.

**Formal Definition**

```
Length Ratio = note_length / consultation_duration. Appropriateness = correlation between length ratio and consultation complexity (measured by SNOMED concept count, problem count, or clinician complexity rating). Outliers (very short or very long for complexity) indicate calibration issues.
```

**Limitations**

> Appropriate length is subjective and varies by clinical context, specialty, and individual clinician preference.

**Novel Thinking / Implications**

> 💡 Over-summarisation is a quiet failure mode — the note looks clean but has lost necessary detail. Under-summarisation produces verbatim transcripts that defeat the purpose of AVT. Both can be detected statistically: a system that produces 200-word notes for both 5-minute and 30-minute consultations is not adapting appropriately.

---

---

### 🟡 Stigmatising Language Replication Rate

Proportion of AI-generated notes that reproduce biased or stigmatising language patterns learned from training data. Distinct from the existing Cultural & Linguistic Appropriateness metric, which covers broader sensitivity issues. This metric specifically tracks whether the system has learned to generate language like "drug-seeking", "non-compliant", "frequent flyer", "difficult patient" — terms which research shows appear disproportionately in notes about specific patient populations.

|Dimension              |Value                                                                       |
|-----------------------|----------------------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                                      |
|**Measurement Cadence**|Periodic audit                                                              |
|**Pipeline Layer**     |Summarisation                                                               |
|**Assurance Question** |Fairness & Equity                                                           |
|**Measurement Method** |Computational                                                               |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                              |
|**Responsible Actors** |Vendor, Deployer                                                            |
|**Maturity**           |Proposed / Novel                                                            |
|**Outcome Type**       |Distal                                                                      |
|**Source**             |Barcelona et al., JAMA Network Open 2025 (Black patients 2.54× odds of negative descriptors)|

**Why this tier?**

> Important fairness dimension, measurable today with a keyword/phrase dictionary plus contextual classification. Should be a standard vendor pre-deployment check and periodic audit.

**Formal Definition**

```
Stigmatising Language Rate = |notes_containing_stigmatising_terms| / |total_notes|. Dictionary based on published clinical language audit studies, updated periodically. Categories: non-adherence framing, drug-seeking framing, effort/character judgment, difficulty framing, dismissive framing. Disaggregate by patient demographics to detect bias amplification: Bias Ratio = rate_in_minority_population / rate_in_majority_population. Bias Ratio > 1.2 indicates disparate application.
```

**Code: Stigmatising language detection**

```python
STIGMATISING_LEXICON = {
    "non_adherence": ["non-compliant", "non-adherent", "refuses to",
                       "failed to comply", "poor compliance"],
    "drug_seeking": ["drug-seeking", "drug seeking", "narcotic seeking",
                      "opioid seeking"],
    "difficulty": ["difficult patient", "frequent flyer", "high utiliser",
                    "heartsink", "demanding"],
    "effort_judgment": ["not trying", "unmotivated", "poorly motivated",
                         "refuses to engage"],
    "dismissive": ["claims", "alleges", "reports pain but",
                    "supposedly", "apparently"],
}

def stigmatising_language_rate(notes, demographic_col=None):
    results = {"total": 0, "flagged": 0, "by_category": {},
               "by_demographic": {}}
    for note in notes:
        results["total"] += 1
        note_flagged = False
        for category, terms in STIGMATISING_LEXICON.items():
            if any(term in note["text"].lower() for term in terms):
                results["by_category"].setdefault(category, 0)
                results["by_category"][category] += 1
                note_flagged = True
        if note_flagged:
            results["flagged"] += 1
            if demographic_col and demographic_col in note:
                d = note[demographic_col]
                results["by_demographic"].setdefault(d, 0)
                results["by_demographic"][d] += 1
    results["rate"] = results["flagged"] / results["total"]
    return results
```

**Limitations**

> Dictionary-based detection misses novel stigmatising phrasings and over-flags legitimate uses (e.g. "non-adherent" may be clinically accurate in some contexts). Context-aware classification would be stronger but requires a trained classifier.

**Novel Thinking / Implications**

> 💡 AVT systems trained on legacy clinical notes have learned the biases present in those notes. When the same system generates notes for similar patient presentations, it reproduces the patterns. This is a quiet failure mode: the AI is faithfully reproducing exactly the language patterns the profession is trying to move away from. Detection is a necessary first step; mitigation requires vendor-side intervention in training data curation.

## Clinical Coding

*SNOMED/Read code assignment. Individual care + population data quality.*

**Tier breakdown**: 🟡 2 Tier 2 · 🔵 2 Tier 3

### 🟡 SNOMED Code Accuracy

AI-suggested code correctness. Precision, recall, and F1 reported separately for diagnosis, medication, procedure codes.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Clinical Coding |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Day Zero Baseline, Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard clinical audit; NAS baselines |

**Why this tier?**

> Standard clinical audit. Recommended at Day Zero baseline and quarterly thereafter. Deployer-measurable with existing audit skills.

**Formal Definition**

```
Precision = |C_correct ∩ C_generated| / |C_generated|. Recall = |C_correct ∩ C_generated| / |C_reference|. F1 = harmonic mean. Report per code category.
```

**References**

- **SNOMED CT**: [SNOMED International](https://www.snomed.org/)

**Limitations**

> Requires clinician audit. Small samples.

---

### 🟡 SNOMED CT Concept Mapping Accuracy

Accuracy of the mapping from extracted clinical entities in free-text to the correct SNOMED CT concept ID. Distinct from the existing SNOMED Code Accuracy metric, which measures whether the assigned code is clinically correct. Concept mapping measures whether the system correctly resolves "chest pain" to the correct SNOMED concept (29857009 — chest pain) rather than a near-miss concept (102588006 — chest discomfort). The boundary between correct and near-miss is where most mapping errors occur.

|Dimension              |Value                                                                    |
|-----------------------|-------------------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                                   |
|**Measurement Cadence**|Periodic audit                                                           |
|**Pipeline Layer**     |Clinical Coding                                                          |
|**Assurance Question** |Fidelity & Accuracy                                                      |
|**Measurement Method** |Computational                                                            |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                           |
|**Responsible Actors** |Vendor                                                                   |
|**Maturity**           |Established                                                              |
|**Outcome Type**       |Proximal                                                                 |
|**Source**             |NLP2FHIR pipeline literature; John Snow Labs FHIR-Ready AI; MedCAT benchmarks|

**Why this tier?**

> Vendor pre-deployment metric. Should be reported alongside SNOMED Code Accuracy. Essential for NHS interoperability as ambient scribes increasingly drive structured data entry.

**Formal Definition**

```
For each extracted clinical mention m: mapping function M(m) → SNOMED concept ID. Accuracy = |correctly_mapped| / |total_mentions|. Additional measures: (a) Exact Match Rate — mapped to exactly the reference concept; (b) Hierarchical Match Rate — mapped to an ancestor or descendant within 2 levels of reference; (c) Semantic Type Match Rate — mapped to correct semantic category. Report all three because acceptable mapping depth depends on context.
```

**Limitations**

> "Correct" mapping is context-dependent — sometimes a more general concept is preferable to an over-specific one. Ground truth annotation requires SNOMED expertise. NHS-specific subset mappings add complexity (not all SNOMED concepts are in the UK Edition).

**Novel Thinking / Implications**

> 💡 Concept mapping is where most structured data failures occur in ambient scribes. The surface text can look correct while the underlying code points to a subtly different concept. A clinician reviewing the free-text note won't notice that the coded entry resolves to "chest discomfort" rather than "chest pain" — but the downstream analytics, safety alerts, and QOF calculations will.

### 🟡 ICD-10 / ICD-11 Full-Specificity Precision

Precision of ICD coding at maximum digit specificity, reported separately from category-level accuracy. Performance typically degrades sharply at full specificity compared to 3-character category level. The Hybrid-Code v2 framework reported 93% accuracy at 3-character level but only 82% at full specificity — the difference representing systematic specificity errors that aggregate metrics hide.

|Dimension              |Value                                       |
|-----------------------|--------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                      |
|**Measurement Cadence**|Periodic audit                              |
|**Pipeline Layer**     |Clinical Coding                             |
|**Assurance Question** |Fidelity & Accuracy                         |
|**Measurement Method** |Computational                               |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit              |
|**Responsible Actors** |Vendor                                      |
|**Maturity**           |Emerging                                    |
|**Outcome Type**       |Proximal                                    |
|**Source**             |Hybrid-Code v2 (arXiv 2512.23743); WHO ICD-11 implementation guidance|

**Why this tier?**

> Vendor pre-deployment. Should be reported at multiple specificity levels (3-char, 4-char, full). Important for secondary care deployment and research data quality.

**Formal Definition**

```
Report precision at each specificity level independently: P_3char, P_4char, P_full. Specificity Degradation = P_3char - P_full. Values > 10 percentage points indicate the system systematically fails at high specificity. For ICD-11, which has more granular specificity than ICD-10, report per specificity depth.
```

**Limitations**

> Full-specificity coding requires clinical judgement that may exceed what is documented in the consultation. Some codes are legitimately unreachable from the source material — the consultation didn't contain enough information. Distinguishing unreachable codes from model errors requires careful reference construction.

**Novel Thinking / Implications**

> 💡 Over-specific coding is a form of clinical hallucination: the system generates specificity that wasn't present in the source. Under-specific coding is information loss. Both are quality issues, and they require different interventions. Reporting only aggregate accuracy conflates them.

### 🟡 OPCS-4 Procedure Coding Accuracy

Accuracy of OPCS-4 procedure code assignment from consultation documentation. NHS-specific — the OPCS-4 classification (Office of Population Censuses and Surveys, 4th revision) is the mandatory procedure coding standard for NHS secondary care. **No published AI benchmarks currently exist for OPCS-4 coding** despite it being essential for NHS deployment.

|Dimension              |Value                                         |
|-----------------------|----------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                        |
|**Measurement Cadence**|Periodic audit                                |
|**Pipeline Layer**     |Clinical Coding                               |
|**Assurance Question** |Fidelity & Accuracy                           |
|**Measurement Method** |Computational                                 |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                |
|**Responsible Actors** |Vendor                                        |
|**Maturity**           |Proposed / Novel                              |
|**Outcome Type**       |Proximal                                      |
|**Source**             |NHS Digital OPCS-4 coding standards; gap identified in published AVT literature|

**Why this tier?**

> Critical for NHS secondary care deployment. Should be a procurement requirement but cannot currently be assessed against published benchmarks — deployers must require vendor evidence on their specific cases.

**Formal Definition**

```
Precision, Recall, F1 at OPCS-4 code level. Specificity breakdown: chapter level (first character), category (first 2 characters), sub-category (3 characters), full code. Report per clinical chapter because procedure complexity varies dramatically (codes in Chapter V — Nervous System — are harder than Chapter W — Bones & Joints).
```

**Limitations**

> No public NHS-representative benchmark dataset for OPCS-4 coding exists. Vendors must construct their own evaluation, which creates comparability problems. Ground truth annotation requires specialist NHS coding expertise.

**Novel Thinking / Implications**

> 💡 The absence of any published OPCS-4 AI benchmark is itself a diagnostic finding about the state of the field. Ambient scribe vendors focused on the US market optimise for ICD-10 and CPT; NHS-specific standards are an afterthought. This is a strong argument for NHS England to commission a national OPCS-4 benchmark dataset as infrastructure investment — without it, NHS secondary care AVT deployment is operating without evidence.

### 🟡 dm+d Medication Coding Accuracy

Accuracy of Dictionary of Medicines and Devices (dm+d) coding for medications discussed in consultations. NHS-specific — dm+d is the mandatory NHS medication terminology, maintained by NHS BSA, and essential for medication safety, interoperability, and prescribing workflows. **Like OPCS-4, no published AI benchmarks exist for dm+d coding**.

|Dimension              |Value                                                     |
|-----------------------|----------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                    |
|**Measurement Cadence**|Periodic audit                                            |
|**Pipeline Layer**     |Clinical Coding                                           |
|**Assurance Question** |Safety                                                    |
|**Measurement Method** |Computational                                             |
|**Lifecycle Phases**   |Pre-deployment, Continuous                                |
|**Responsible Actors** |Vendor                                                    |
|**Maturity**           |Proposed / Novel                                          |
|**Outcome Type**       |Proximal                                                  |
|**Source**             |NHS BSA dm+d standard; gap identified in published AVT literature|

**Why this tier?**

> Safety-critical for any AVT writing medication data back to the EPR. Should be a procurement requirement with vendor attestation. Monitoring required as dm+d is updated quarterly — a model trained against an old version will systematically fail on newer medications.

**Formal Definition**

```
Per medication mention: correct mapping to dm+d VMP (Virtual Medicinal Product), AMP (Actual Medicinal Product), VMPP (Virtual Medicinal Product Pack), or AMPP (Actual Medicinal Product Pack) depending on the level required by the EPR write-back. Currency Check: proportion of reference medications that exist in the current dm+d release. Drift = proportion of codes generated that no longer exist in the current dm+d release.
```

**Limitations**

> Mapping from spoken medication name to dm+d concept involves disambiguation (brand vs generic, different strengths, different formulations). Spoken names rarely contain enough specificity to uniquely identify a dm+d code without additional context.

**Novel Thinking / Implications**

> 💡 dm+d is updated quarterly. Any AVT system with a static model is by definition accumulating vocabulary drift against the current standard. A system trained two years ago has approximately eight releases of drift. Currency should be a contractual requirement — vendors should commit to a maximum acceptable drift against the live dm+d.

---

### 🟢 Code Hallucination Rate

Rate at which the system generates codes that do not exist in the target code set. Distinct from all other coding error metrics because a non-existent code is not a "wrong" code — it is a structural error. The code looks valid syntactically but resolves to nothing. The Hybrid-Code v2 framework explicitly targeted "zero-hallucination coding" because this failure mode is both detectable and unambiguously wrong.

|Dimension              |Value                                                |
|-----------------------|-----------------------------------------------------|
|**Priority Tier**      |🟢 Tier 1 — Minimum Viable                            |
|**Measurement Cadence**|Continuous                                           |
|**Pipeline Layer**     |Clinical Coding                                      |
|**Assurance Question** |Safety                                               |
|**Measurement Method** |Computational                                        |
|**Lifecycle Phases**   |Pre-deployment, Continuous                           |
|**Responsible Actors** |Vendor, Deployer                                     |
|**Maturity**           |Emerging                                             |
|**Outcome Type**       |Proximal                                             |
|**Source**             |Hybrid-Code v2 (arXiv 2512.23743) — neuro-symbolic verification approach|

**Why this tier?**

> Architecturally preventable failure mode — there is no reason a production system should generate non-existent codes. Should be a hard zero-tolerance metric validated pre-deployment and monitored continuously. Automated detection is trivial (lookup against the code set).

**Formal Definition**

```
Code Hallucination Rate = |generated_codes_not_in_target_code_set| / |total_generated_codes|. Target: 0.0. Any non-zero value indicates architectural failure — the system should be constrained to generate only valid codes via lookup or constrained decoding. Report per code set (SNOMED, ICD, OPCS-4, dm+d) because constraint enforcement may vary.
```

**Code: Code hallucination check**

```python
def code_hallucination_rate(generated_codes, code_set):
    """
    Returns rate of codes that don't exist in the target code set.
    Should be 0 for any production system.
    """
    valid_codes = set(code_set)
    hallucinated = [c for c in generated_codes if c not in valid_codes]
    rate = len(hallucinated) / len(generated_codes) if generated_codes else 0
    return {
        "rate": rate,
        "hallucinated_codes": hallucinated,
        "alert": rate > 0,
        "severity": "CRITICAL" if rate > 0 else "OK"
    }
```

**Limitations**

> Requires current version of the target code set for lookup. Code set updates may temporarily create false positives (newly valid codes that haven't propagated). Does not detect codes that exist but are clinically wrong — that's captured by SNOMED Code Accuracy.

**Novel Thinking / Implications**

> 💡 This is a zero-tolerance metric. A non-existent code in a clinical record is a data quality failure that breaks downstream systems. The correct architectural response is constrained generation — the system should be structurally unable to produce a code outside the target code set. Any vendor reporting a non-zero hallucination rate is implicitly admitting that their generation is unconstrained, which is a procurement red flag.

### 🟡 Coding Inflation Detection

Systematic upcoding monitoring via SPC. In NHS, primary risk is data quality corruption of epidemiological data, QOF, and population health.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Clinical Coding |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Regional (ICB), National Body |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Source** | US payer countermeasures; NHS risk analysis |

**Why this tier?**

> Regional (ICB) monitoring using SPC on coding distributions. Requires pre-AVT baseline. National data integrity implication.

**Formal Definition**

```
SPC on pre/post-AVT code distributions. Track: code density (avg codes/encounter), severity shift, novel code rate. Flag if >2σ from baseline for ≥4 weeks (Western Electric rules).
```

**Code: SPC-based coding drift**

```python
import numpy as np

def coding_drift_spc(pre_counts, post_counts):
    mu = np.mean(pre_counts)
    sigma = np.std(pre_counts, ddof=1)
    ucl = mu + 3 * sigma  # upper control limit
    uwl = mu + 2 * sigma  # upper warning limit
    alerts = []
    for i, val in enumerate(post_counts):
        if val > ucl:
            alerts.append({"week": i+1, "rule": "3σ_breach"})
        if i >= 7 and all(v > mu for v in post_counts[i-7:i+1]):
            alerts.append({"week": i+1, "rule": "8_consecutive"})
    return {"baseline_mean": mu, "alerts": alerts}
```

**Limitations**

> NHS coding incentives differ from US.

**Novel Thinking / Implications**

> 💡 Risk is data quality: systematically different codes corrupt epidemiological data, QOF, population health analytics.

---

### 🟡 E/M Level Shift Monitoring

Monitoring of shifts in Evaluation & Management (E/M) coding levels pre- and post-AVT deployment. In US settings, E/M level shift has been a primary revenue impact channel; in NHS settings, the equivalent concern is SNOMED specificity shift and its effect on QOF, Hospital Episode Statistics, and population health analytics. Extension of the existing Coding Inflation Detection metric with a specific focus on tariff-relevant code distributions.

|Dimension              |Value                                                                                |
|-----------------------|-------------------------------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                                               |
|**Measurement Cadence**|Continuous                                                                           |
|**Pipeline Layer**     |Clinical Coding                                                                      |
|**Assurance Question** |Safety                                                                               |
|**Measurement Method** |Computational                                                                        |
|**Lifecycle Phases**   |Day Zero Baseline, Continuous                                                        |
|**Responsible Actors** |Regional (ICB), National Body                                                        |
|**Maturity**           |Emerging                                                                             |
|**Outcome Type**       |Distal                                                                               |
|**Source**             |npj Digital Medicine policy brief (Nature s41746-025-02272-z) — documented 3.0→4.1 diagnoses/encounter post-AVT|

**Why this tier?**

> Regional (ICB) and national monitoring. Deployers cannot assess population-level shifts from their own data alone. Requires pre/post AVT baseline and cross-practice aggregation.

**Formal Definition**

```
For each coding level or tariff-relevant category: compute pre-AVT baseline distribution and post-AVT distribution. Shift Index = KL divergence or earth-mover's distance between distributions. Flag categories with shift > 0.1 (magnitude calibrated to historical coding drift). Disaggregate by demographic and clinical complexity to identify selective amplification.
```

**Limitations**

> Requires pre-AVT baseline of sufficient duration (minimum 12 months) for seasonal pattern stability. Confounded with independent coding policy changes, QOF updates, and training interventions. Attribution to AVT specifically requires quasi-experimental design.

**Novel Thinking / Implications**

> 💡 The US evidence (14% HCC capture increase, 11% wRVU increase) is alarming because it's unclear whether the shift represents more complete capture (legitimate) or documentation-driven inflation (governance failure). In the NHS context, the same ambiguity applies: are we seeing better coding, or AVT-driven drift that will corrupt epidemiological data? Without monitoring, the distinction is invisible and the data integrity risk is absorbed silently.

### 🟡 Coding Equity Index

Whether AVT-driven changes in coding distribution are equitably spread across patient demographics or systematically benefit some populations more than others. If AVT improves coding completeness more for majority populations than for minority populations, it widens existing inequalities in data quality and downstream resource allocation.

|Dimension              |Value                                                 |
|-----------------------|------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                |
|**Measurement Cadence**|Periodic audit                                        |
|**Pipeline Layer**     |Clinical Coding                                       |
|**Assurance Question** |Fairness & Equity                                     |
|**Measurement Method** |Computational                                         |
|**Lifecycle Phases**   |Periodic Audit                                        |
|**Responsible Actors** |Regional (ICB), National Body                         |
|**Maturity**           |Proposed / Novel                                      |
|**Outcome Type**       |Distal                                                |
|**Source**             |Extension of existing Deployment Equity Index to coding dimension|

**Why this tier?**

> Regional or national responsibility. Requires demographic-linked coding data aggregated across practices. Important equity dimension currently invisible in AVT evaluation.

**Formal Definition**

```
For each coding category: compute the pre/post AVT change ratio per demographic group. Equity Ratio = max(change_ratio across groups) / min(change_ratio across groups). Values > 1.5 indicate disparate impact. Specifically monitor: condition coding completeness, severity coding, and comorbidity capture by ethnicity, age, deprivation, and EAL status.
```

**Limitations**

> Demographic-linked coding analysis requires data aggregation that may raise information governance concerns. Small group sizes at practice level require regional aggregation. Attribution to AVT specifically needs controls for confounders.

**Novel Thinking / Implications**

> 💡 If AVT makes the documented patient population look healthier for some demographics and more accurately unwell for others, the resource allocation implications compound existing health inequalities. This is an equity dimension that the existing taxonomy's fairness metrics don't capture — they focus on AVT accuracy across demographics, not on AVT's effect on the resulting data about those demographics.

### 🔵 wRVU / Tariff Impact Attribution

Attribution of workload or tariff-relevant coding changes to AVT specifically, separated from concurrent changes (training, policy updates, case mix shifts). Quasi-experimental methodology required. In NHS context, applies to PbR tariffs, QOF achievement, and secondary care activity-based funding.

|Dimension              |Value                                        |
|-----------------------|---------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research               |
|**Measurement Cadence**|Periodic audit                               |
|**Pipeline Layer**     |Clinical Coding                              |
|**Assurance Question** |Meta-evaluation                              |
|**Measurement Method** |Hybrid                                       |
|**Lifecycle Phases**   |Periodic Audit                               |
|**Responsible Actors** |Regional (ICB), National Body, Academic     |
|**Maturity**           |Proposed / Novel                             |
|**Outcome Type**       |Distal                                       |
|**Source**             |Extends E/M Level Shift Monitoring with causal attribution methodology|

**Why this tier?**

> Research-grade metric requiring quasi-experimental design. National or academic responsibility. Not routinely measurable at deployer level.

**Formal Definition**

```
Using difference-in-differences or synthetic control methodology: compare coding/tariff trajectories of AVT-adopting practices against matched non-adopting practices over the same period. Attribution Coefficient = (ΔAVT - ΔControl) / ΔControl. Positive values indicate AVT-driven shift; magnitude indicates size of effect. Confidence intervals essential given small sample sizes in practice-level comparisons.
```

**Limitations**

> Practice selection into AVT is not random — early adopters may differ systematically from non-adopters. Matching methodology is contested. Small sample sizes at practice level undermine statistical power.

**Novel Thinking / Implications**

> 💡 This is the metric that answers the governance question: is AVT making the coded data more accurate or more inflated? Without this attribution, every observed coding shift is ambiguous. National evaluation programmes are the only plausible venue for doing this properly — individual deployers cannot.

### 🔵 Code Specificity Index

Whether suggested codes are at appropriate hierarchy level. SNOMED has multiple specificity levels for the same concept; AI may default to over-general (loses detail) or over-specific (introduces false precision) codes inappropriately.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Clinical Coding |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | SNOMED CT hierarchy semantics; clinical audit methodology |

**Why this tier?**

> Requires clinical judgement and SNOMED hierarchy expertise. Suitable for periodic clinical audit.

**Formal Definition**

```
For each suggested code, compute hierarchical distance from clinically appropriate code. Specificity Index = mean signed distance: positive = over-specific, negative = over-general, zero = appropriate. Track distribution across coding categories.
```

**Limitations**

> Defining 'appropriate' specificity requires clinical judgement. The same condition may warrant different specificity in different contexts (e.g. primary care vs specialist).

**Novel Thinking / Implications**

> 💡 Over-specific coding is the more insidious problem: AI may code 'chest pain' as 'precordial chest pain' when the patient simply said 'pain in my chest'. The over-specific code carries information that wasn't in the source — a form of coded hallucination. Under-specific coding loses information but is more obviously a quality issue.

---

### 🔵 Code Suggestion Latency

Time from note generation to code suggestion availability. Affects coding workflow integration — if coding suggestions arrive too late, clinicians have moved on to the next patient and won't engage with them.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Clinical Coding |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard latency metric |

**Why this tier?**

> Operational metric. Important for adoption but not safety-critical.

**Formal Definition**

```
Latency = t_codes_available - t_note_generated. Report distribution. Threshold: P95 < 30 seconds for in-consultation review; < 5 minutes for next-patient batch review.
```

**Limitations**

> Latency requirements depend on workflow integration model.

---

## EPR Write-back

*Data to permanent record. Where errors become patient safety events.*

**Tier breakdown**: 🟢 4 Tier 1 · 🟡 1 Tier 2

### 🟢 Write-back Fidelity

Data transfer accuracy to EPR structured fields. Where errors become patient safety events — hallucinated allergy in allergy field propagates to all future decisions.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | EPR Write-back |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Critical gap — no standardised FHIR R4 write-back in NHS primary care |

**Why this tier?**

> Highest-priority pre-deployment gate. A hallucinated allergy written to the EPR allergy field is a system-level safety failure that propagates to every future clinical decision. Must test per EPR system before go-live.

**Formal Definition**

```
Fidelity(d,f) = 1 if content correct AND target field correct. Report per category: (a) free-text, (b) coded diagnoses, (c) medications, (d) allergies, (e) problem list. Categories c-e are safety-critical.
```

**References**

- **IM1**: NHS IM1 interface assurance

**Limitations**

> Integration-specific: must test per EPR (EMIS, SystmOne, Epic).

**Novel Thinking / Implications**

> 💡 Highest-priority pre-deployment gate. Hallucination in free text is bad; hallucinated allergy in allergy field is system-level safety failure.

---

### 🟢 Integration Error Rate

AVT-to-EPR pipeline failures: failed writes, partial writes, timeouts, truncation.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | EPR Write-back |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard integration monitoring; IM1 requirements |

**Why this tier?**

> Standard integration monitoring. Automated, low-burden, and catches data pipeline failures that directly affect patient records.

**Formal Definition**

```
IER = (N_failed + N_partial + N_degraded) / N_total. SLA target: IER < 0.001.
```

**Limitations**

> Soft failures harder to detect than hard failures.

---

### 🟢 Field Mapping Accuracy

Does content land in the correct EPR field even when content is correct? A correctly transcribed allergy written to the free-text consultation field rather than the allergies field is a system failure with safety implications — the allergy won't trigger drug interaction checks.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | EPR Write-back |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Identified as distinct failure mode within write-back |

**Why this tier?**

> Safety-critical pre-deployment test. Wrong-field placement of safety-critical content (allergies, medications) bypasses downstream safety mechanisms entirely.

**Formal Definition**

```
For each clinical item: Mapping Accuracy = (item correctly identified) AND (mapped to correct EPR field). Distinct from content accuracy. Categories: allergies, medications, problems, observations, free-text. Critical failures: safety-critical content in non-safety-critical fields.
```

**Limitations**

> Requires clear ground truth on which field each item should land in. Some items legitimately belong in multiple fields.

**Novel Thinking / Implications**

> 💡 This is distinct from write-back fidelity. Fidelity asks 'is the content correct?' Field mapping asks 'is it in the right place?' Both can fail independently. An allergy correctly transcribed but written to the consultation note rather than the allergy list is a silent failure — the content is technically present but won't trigger downstream safety checks like drug interaction warnings.

---

### 🟢 Update vs Append Behaviour

Does the system correctly handle existing structured data? Overwriting an existing allergy list vs appending to it has different safety implications. Overwriting can erase critical historical information; inappropriate appending can create duplicates and inconsistencies.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | EPR Write-back |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Identified as safety-critical EPR integration behaviour |

**Why this tier?**

> Safety-critical pre-deployment test. Must be tested per EPR system before go-live. Overwriting existing safety-critical data is a patient safety event.

**Formal Definition**

```
For each structured data update: behaviour in {overwrite, append, merge, skip}. Correctness depends on context. Critical failures: overwriting with less complete data, appending duplicates that cause alert fatigue, skipping legitimate updates.
```

**Limitations**

> Correct behaviour is context-dependent and varies by EPR system. Each EPR has different conventions for structured data updates.

**Novel Thinking / Implications**

> 💡 The classic failure: AVT writes 'allergies: penicillin' to a patient who already has 'penicillin, sulpha, aspirin' in their allergy list. If the system overwrites, the patient loses two allergies from their record — a direct patient safety event. Pre-deployment testing must include scenarios with existing structured data, not just clean-slate consultations.

---

### 🟡 Write-back Rollback Capability

When errors are detected, can the write-back be reversed cleanly? Particularly important for coded data that triggers downstream processes (alerts, prescribing rules, audit trails).

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | EPR Write-back |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Identified as essential for incident response |

**Why this tier?**

> Pre-deployment assessment of EPR integration. Affects incident response capability.

**Formal Definition**

```
Rollback capability assessed against: (1) Time window for clean rollback; (2) Audit trail of original vs corrected values; (3) Downstream system notification of correction; (4) Patient communication if relevant. Binary capability with sub-criteria.
```

**Limitations**

> True rollback may be impossible once data has propagated to downstream systems (national records, secondary uses).

**Novel Thinking / Implications**

> 💡 When an AVT error is discovered after the note has been signed and written to the EPR, the recovery process matters. Some EPR systems make correction easy (visible audit trail, version history); others make it nearly impossible (correction creates a new entry but the original persists). This affects how quickly and cleanly errors can be addressed when discovered through periodic audit.

---

### 🟡 FHIR R4 Resource Conformance Rate

Validated conformance of generated structured data against FHIR R4 profiles. FHIR is increasingly the interoperability standard for NHS EPRs; systems that produce technically parseable but profile-non-conformant resources create silent integration failures downstream. The ADS/Harvard SPIE 2025 study reported 95% data field retention via FHIR vs ~70% for legacy formats — but retention is not the same as profile conformance.

|Dimension              |Value                                    |
|-----------------------|-----------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                   |
|**Measurement Cadence**|Continuous                               |
|**Pipeline Layer**     |EPR Write-back                           |
|**Assurance Question** |Fidelity & Accuracy                      |
|**Measurement Method** |Computational                            |
|**Lifecycle Phases**   |Pre-deployment, Continuous               |
|**Responsible Actors** |Vendor                                   |
|**Maturity**           |Established                              |
|**Outcome Type**       |Proximal                                 |
|**Source**             |FHIR R4 validation tooling; SPIE 14009E 2025 interoperability study|

**Why this tier?**

> Established methodology with open-source validators. Vendor pre-deployment requirement. Should be reported per FHIR profile used (UK Core, INTEROPen, local).

**Formal Definition**

```
For each generated FHIR resource: validate against the applicable profile using the official HL7 FHIR validator. Conformance Rate = |resources_passing_validation| / |total_resources|. Stratify by resource type (Condition, MedicationStatement, AllergyIntolerance, Observation) — failures often cluster in specific resource types. Target: 100% on safety-critical resource types.
```

**Limitations**

> Conformance to a profile does not guarantee clinical correctness — a valid but wrong medication code passes validation. Profile requirements may be under-specified for some NHS use cases.

**Novel Thinking / Implications**

> 💡 Profile conformance is a necessary but not sufficient condition for interoperability. The existing Write-back Fidelity metric measures whether content is correct; this metric measures whether the structural container is valid. Both can fail independently. A system that produces valid-but-wrong FHIR is dangerous; a system that produces right-but-invalid FHIR will fail to write-back silently.

---

### 🔵 openEHR Archetype Conformance

Conformance of generated clinical data against openEHR archetypes for NHS trusts using openEHR-based EPR platforms. Less widespread than FHIR in UK primary care but relevant for specific secondary care deployments (particularly in mental health trusts and specialised services).

|Dimension              |Value                                     |
|-----------------------|------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research            |
|**Measurement Cadence**|Continuous                                |
|**Pipeline Layer**     |EPR Write-back                            |
|**Assurance Question** |Fidelity & Accuracy                       |
|**Measurement Method** |Computational                             |
|**Lifecycle Phases**   |Pre-deployment, Continuous                |
|**Responsible Actors** |Vendor                                    |
|**Maturity**           |Established                               |
|**Outcome Type**       |Proximal                                  |
|**Source**             |openEHR Foundation standards; Clinical Knowledge Manager archetype library|

**Why this tier?**

> Deployment context-specific. Tier 3 for most deployers but Tier 2 or even Tier 1 for trusts using openEHR-based platforms — context adjustment per the "Adapting to Local Context" section.

**Formal Definition**

```
For each generated composition: validate against the applicable openEHR archetype(s) and template(s). Report: archetype conformance rate (structural), terminology binding conformance (codes map to required terminology subset), cardinality compliance. Must validate both the composition structure and the path-based data bindings.
```

**Limitations**

> openEHR archetype validation tooling is less mature than FHIR validation. Archetype maintenance varies by trust. Cross-trust conformance may require different archetype versions.

**Novel Thinking / Implications**

> 💡 The UK has bifurcated EPR infrastructure: primary care is standardising on FHIR-based interoperability, while parts of secondary care (particularly the Code4Health-aligned trusts) have significant openEHR investment. AVT vendors focused on primary care may simply not support openEHR, making them structurally unsuitable for some secondary care deployments. This should be a procurement question rather than a post-contract discovery.

# Part B — Pipeline Interactions

## Partial-Pipeline

*Metrics spanning adjacent pipeline stages. Error interactions between components that single-stage metrics miss.*

**Tier breakdown**: 🟡 3 Tier 2 · 🔵 6 Tier 3

### 🔵 Speaker-Attributed Transcript Accuracy

Combined ASR + diarisation: was the right text assigned to the right person? Neither WER nor DER alone captures this — a transcript can have low WER and low DER but still misattribute a critical utterance.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR + Diarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Identified as compound metric gap — neither WER nor DER alone captures this |

**Why this tier?**

> Novel compound metric exposing multiplicative degradation invisible to WER or DER alone. Requires aligned utterance-level ground truth with both text and speaker labels.

**Formal Definition**

```
SATA = |utterances where text correct AND speaker correct| / |total utterances|. Spans ASR (was the text right?) and diarisation (was the speaker right?). A correct transcription misattributed to the wrong speaker is as dangerous as a wrong transcription. Component decomposition: if WER and DER errors are independent, SATA ≈ (1-WER) × (1-SAE), exposing multiplicative degradation invisible to either metric alone.
```

**Code: Speaker-attributed accuracy**

```python
def speaker_attributed_accuracy(utterances):
    """
    Each utterance: {ref_text, hyp_text, ref_speaker, hyp_speaker}
    Both text AND speaker must be correct for a 'pass'.
    """
    correct = 0
    for u in utterances:
        text_ok = u["ref_text"].strip().lower() == u["hyp_text"].strip().lower()
        spk_ok = u["ref_speaker"] == u["hyp_speaker"]
        if text_ok and spk_ok:
            correct += 1
    sata = correct / len(utterances) if utterances else 0
    return {
        "sata": round(sata, 4),
        "text_only_accuracy": round(
            sum(1 for u in utterances
                if u["ref_text"].strip().lower() == u["hyp_text"].strip().lower())
            / len(utterances), 4),
        "speaker_only_accuracy": round(
            sum(1 for u in utterances
                if u["ref_speaker"] == u["hyp_speaker"])
            / len(utterances), 4),
        "compound_gap": "multiplicative" 
            if sata < min(
                sum(1 for u in utterances if u["ref_text"].strip().lower()==u["hyp_text"].strip().lower())/len(utterances),
                sum(1 for u in utterances if u["ref_speaker"]==u["hyp_speaker"])/len(utterances)
            ) else "additive"
    }
```

**Limitations**

> Requires aligned utterance-level ground truth with both text and speaker labels. Most benchmarks provide one or the other.

**Novel Thinking / Implications**

> 💡 This is the first point where component metrics compound. Vendors reporting WER and DER separately can mask combined degradation. A system with 5% WER and 5% DER could have 10% speaker-attributed errors if the error populations overlap, or up to 10% if they don't. Only this combined metric reveals the actual risk.

---

### 🟡 Multi-Party Conversation Robustness

Combined ASR + diarisation degradation when >2 speakers present: interpreter, family member, student, MDT. Most benchmarks assume dyadic (2-speaker) encounters.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR + Diarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Identified in NHS consultation pattern analysis — interpreter-mediated, family-present, and MDT consultations are common |

**Why this tier?**

> Vendor should test and publish performance curves by speaker count. Deployers with frequent multi-party consultations (interpreters, MDT) should request this data.

**Formal Definition**

```
Robustness(n) = SATA(n speakers) / SATA(2 speakers). Values < 1.0 indicate multi-party degradation. Report per n = {2, 3, 4, 5+}. NHS consultations frequently involve 3+ parties.
```

**Limitations**

> Test scenarios with >2 speakers are expensive to construct and annotate. Real NHS multi-party audio is rarely available for benchmarking.

**Novel Thinking / Implications**

> 💡 This is the 'validated use envelope' question in acoustic form. If the system was benchmarked on 2-speaker consultations, any multi-party use is technically off-label. Vendors should publish performance curves by speaker count.

---

### 🔵 Information Extraction Yield

Spans ASR + summarisation: what proportion of clinically relevant content in source audio survives through transcription AND into the generated note? Captures the combined loss from ASR errors and summarisation omissions.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | ASR + Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Identified as structural gap — component metrics don't capture cross-stage information loss |

**Why this tier?**

> Requires expert annotation of source audio — expensive. Best suited for national evaluation programme or academic pilot.

**Formal Definition**

```
IEY = |clinical_items_in_note| / |clinical_items_in_audio|. Clinical items identified by expert annotation of source audio. IEY decomposes: IEY = Yield_ASR × Yield_summarisation. If ASR drops a drug name AND summarisation doesn't compensate, the loss multiplies.
```

**Code: Information extraction yield**

```python
def information_extraction_yield(
    audio_items: list[str],     # expert-annotated clinical items from audio
    transcript_items: list[str], # clinical items found in transcript
    note_items: list[str]        # clinical items found in final note
):
    """
    Two-stage yield: audio→transcript→note.
    Items matched via clinical concept normalisation.
    """
    yield_asr = len(set(audio_items) & set(transcript_items)) / len(audio_items)
    yield_summ = len(set(transcript_items) & set(note_items)) / len(transcript_items) if transcript_items else 0
    yield_e2e = len(set(audio_items) & set(note_items)) / len(audio_items)

    return {
        "yield_asr": round(yield_asr, 3),
        "yield_summarisation": round(yield_summ, 3),
        "yield_end_to_end": round(yield_e2e, 3),
        "compound_loss": round(1 - yield_e2e, 3),
        "loss_attribution": {
            "lost_at_asr": round(1 - yield_asr, 3),
            "lost_at_summarisation": round(yield_asr - yield_e2e, 3),
        }
    }
```

**Limitations**

> Requires expert annotation of source audio to establish ground truth clinical items. Expensive and subjective.

**Novel Thinking / Implications**

> 💡 The key insight: summarisation can sometimes compensate for ASR errors (inferring the right drug from context), or it can amplify them (hallucinating a plausible but wrong drug to fill the gap). IEY captures both — the net yield is what matters clinically.

---

### 🔵 Noise-to-Note Resilience

Spans ASR + summarisation: how gracefully does the final note quality degrade as audio quality worsens? Tests whether the summarisation layer can compensate for degraded transcription.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR + Summarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Proposed for pre-deployment testing — NHS clinical environments have variable acoustics |

**Why this tier?**

> Vendor pre-deployment testing across controlled noise levels. Deployer cannot easily measure but should request test results for relevant acoustic conditions.

**Formal Definition**

```
Resilience(SNR) = NoteQuality(SNR) / NoteQuality(clean). Tested across audio quality levels: clean, mild noise (SNR 20dB), moderate (10dB), severe (5dB), masked speech. Graceful degradation: resilience > 0.8 at moderate noise.
```

**Limitations**

> Requires controlled audio degradation testing which is rarely part of vendor validation. Real-world noise profiles (NHS waiting rooms, home visits, telephone) vary widely.

**Novel Thinking / Implications**

> 💡 NHS environments are acoustically diverse: GP consulting rooms, telephone consultations, home visits, hospital wards. A system validated in a quiet room may fail in a busy practice. Noise resilience should be part of the validated use envelope.

---

### 🔵 Epistemic Status Preservation

Spans diarisation + summarisation: does the note correctly distinguish what was reported by the patient vs observed by the clinician vs inferred by the AI? 'Patient reports headache' vs 'headache noted' vs 'headache' have different clinical meanings.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Diarisation + Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Identified as critical clinical documentation quality dimension not captured by existing metrics |

**Why this tier?**

> Novel metric at intersection of diarisation and summarisation. Clinically significant but measurement methodology not yet standardised.

**Formal Definition**

```
For each clinical assertion a in the note, epistemic status E(a) ∈ {patient-reported, clinician-observed, inferred, unknown}. Preservation rate = |assertions with correct E| / |total assertions|. Requires correct speaker attribution (diarisation) feeding into summarisation that maintains the distinction.
```

**Code: Epistemic status classification**

```python
EPISTEMIC_MARKERS = {
    "patient_reported": [
        "patient reports", "patient states", "patient describes",
        "complains of", "says", "reports", "history of"
    ],
    "clinician_observed": [
        "on examination", "observed", "noted", "found",
        "examination reveals", "O/E"
    ],
    "inferred": [
        "likely", "possibly", "consistent with",
        "suggestive of", "probable"
    ]
}

def classify_epistemic_status(assertion: str) -> str:
    text = assertion.lower()
    for status, markers in EPISTEMIC_MARKERS.items():
        if any(m in text for m in markers):
            return status
    return "unknown"  # no marker = ambiguous

def epistemic_preservation_rate(ref_assertions, gen_assertions):
    """Compare epistemic status in reference vs generated note."""
    correct = 0
    for ref, gen in zip(ref_assertions, gen_assertions):
        if classify_epistemic_status(ref) == classify_epistemic_status(gen):
            correct += 1
    return correct / len(ref_assertions) if ref_assertions else 0
```

**Limitations**

> Epistemic status annotation requires clinical expertise. Automated classification via markers is crude — many assertions lack explicit markers.

**Novel Thinking / Implications**

> 💡 This is clinically significant: 'patient reports chest pain' documents subjective experience; 'chest pain' in the note without qualification implies objective finding. If diarisation misattributes patient speech to clinician, the summariser may strip the 'reports' qualifier, silently changing the epistemic status. This compounds two different error types into a clinical safety risk invisible to either WER or hallucination rate.

---

### 🔵 Diarisation-Stratified WER

WER computed separately for each speaker after diarisation. Captures the compound effect of diarisation errors on per-speaker accuracy measurement. A speaker whose utterances are frequently misattributed will have artificially inflated WER even if the underlying ASR is accurate.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR + Diarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Compound metric exposing diarisation impact on ASR measurement |

**Why this tier?**

> Research-grade compound metric. Useful for vendor system improvement but not deployer-actionable.

**Formal Definition**

```
For each speaker s: WER_s = standard WER on utterances correctly attributed to speaker s. Compare with global WER: if WER_s >> WER_global for some speaker, diarisation errors are degrading per-speaker accuracy.
```

**Limitations**

> Requires aligned reference with both transcription and speaker labels.

**Novel Thinking / Implications**

> 💡 Reveals whether ASR errors are systematic or attribution artifacts. If patient WER is much higher than clinician WER, the question becomes: is patient speech harder to transcribe, or are patient utterances being attributed to the clinician (which would put them in the 'wrong' WER calculation)?

---

### 🟡 Concept Extraction Concordance

Spans summarisation + coding: do the SNOMED codes match the clinical concepts in the free-text note? An internal consistency check that doesn't need source audio — the note and its codes should agree.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation + Coding |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Proposed as automated internal consistency check — no ground truth needed |

**Why this tier?**

> Uniquely valuable: automated self-consistency check requiring no ground truth. Can run on every encounter. Orphan codes (coded but not in text) are strong hallucination signals.

**Formal Definition**

```
Concordance = |concepts_in_text ∩ concepts_in_codes| / |concepts_in_text ∪ concepts_in_codes|. Discordance types: (a) coded but not in text (orphan code); (b) in text but not coded (missing code). Both are quality signals with different risk profiles.
```

**Code: Text-code concordance check**

```python
from medcat.cat import CAT

cat = CAT.load_model_pack("medcat_snomed_model.zip")

def concept_concordance(note_text: str, assigned_codes: set[str]):
    """
    Compare NER-extracted concepts from free text
    against assigned SNOMED codes.
    """
    doc = cat.get_entities(note_text)
    text_concepts = {
        ent["cui"] for ent in doc["entities"].values()
        if ent["acc"] > 0.7  # confidence threshold
    }

    overlap = text_concepts & assigned_codes
    orphan_codes = assigned_codes - text_concepts  # coded but not in text
    missing_codes = text_concepts - assigned_codes  # in text but not coded

    concordance = len(overlap) / len(text_concepts | assigned_codes) if (text_concepts | assigned_codes) else 1.0

    return {
        "concordance": round(concordance, 3),
        "orphan_codes": list(orphan_codes),   # potential hallucinated codes
        "missing_codes": list(missing_codes),  # potential coding omissions
        "alert": len(orphan_codes) > 0         # orphans are higher risk
    }
```

**Limitations**

> NER extraction quality limits accuracy. Some codes are legitimately more specific than free-text descriptions.

**Novel Thinking / Implications**

> 💡 This is uniquely valuable because it requires no ground truth — it's a self-consistency check that can run on every encounter. An orphan code (coded but not mentioned in text) is a strong signal for hallucinated coding. A missing code (mentioned but not coded) is a completeness gap. Both can be detected without human review.

---

### 🔵 End-of-Utterance Timing Accuracy

Whether the system correctly identifies where an utterance ends. Affects both diarisation (turn boundaries) and summarisation (sentence boundaries). Misalignment causes content fragmentation across utterances or merging of distinct utterances.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR + Diarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard speech processing metric |

**Why this tier?**

> Vendor research metric. Affects multiple downstream stages.

**Formal Definition**

```
EOU Timing Error = mean temporal error (ms) between predicted and actual utterance boundaries. Different from speaker boundary precision — EOU timing is within-speaker pauses that should/shouldn't be treated as utterance breaks.
```

**Limitations**

> Defining 'correct' utterance boundaries is itself contested. Conversational speech doesn't always have clean utterance breaks.

**Novel Thinking / Implications**

> 💡 EOU errors propagate: a missed boundary causes two utterances to merge, which then have to be diarised as one (potentially with conflicting speakers) and summarised as one (potentially conflating two clinical concepts).

---

### 🟡 Structured/Free-Text Consistency

Spans summarisation + write-back: does the coded allergy entry agree with allergies mentioned in the free-text note? Does the medication list match medications discussed in the narrative?

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation + Write-back |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Identified as post-write-back automated safety check |

**Why this tier?**

> Automated post-write-back guardrail requiring no ground truth. If structured allergy field disagrees with narrative text, something has gone wrong. Deployer-implementable.

**Formal Definition**

```
For each structured field category f ∈ {allergies, medications, diagnoses}: Consistency(f) = |items_in_structured(f) ∩ items_in_freetext| / |items_in_structured(f) ∪ items_in_freetext|. Inconsistencies: (a) in structured but not free text — unexplained entries; (b) in free text but not structured — missed structuring.
```

**Limitations**

> Requires NER capable of matching free-text mentions to structured field entries. Partial mentions (e.g. 'penicillin allergy' in text vs SNOMED allergy code) need fuzzy matching.

**Novel Thinking / Implications**

> 💡 This is a post-write-back guardrail that can run automatically. If the allergy field says 'penicillin' but the note never mentions penicillin, something has gone wrong — either the note omitted it (summarisation failure) or the structured entry is hallucinated (coding/write-back failure). Either way, it needs review.

---

## End-to-End Pipeline

*Source audio → final clinical record. The clinically meaningful question: did the right information reach the right place?*

**Tier breakdown**: 🟡 4 Tier 2 · 🔵 7 Tier 3

### 🔵 Source-to-Record Concordance

End-to-end: comparing original consultation audio directly against the final EPR entry, bypassing all intermediate representations. This is what actually matters for patient safety.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Proposed as the ultimate AVT safety metric — captures cumulative pipeline effect |

**Why this tier?**

> The ultimate safety metric but requires expert annotation of source audio. Best suited for national evaluation programme. Periodic deployer sampling (e.g. 10 encounters/quarter) is feasible but resource-intensive.

**Formal Definition**

```
SRC = |clinical_items(audio) ∩ clinical_items(EPR)| / |clinical_items(audio)|. Unlike component metrics, SRC captures cumulative loss AND cumulative gain (contextual inference by the summariser). Must be measured per safety-critical category: medications, allergies, diagnoses, plan.
```

**Code: Source-to-record concordance framework**

```python
def source_to_record_concordance(
    audio_clinical_items: dict,   # expert-annotated from audio
    epr_clinical_items: dict,     # extracted from final EPR entry
    categories=("medications","allergies","diagnoses","plan","red_flags")
):
    """
    End-to-end: did what was said reach the record?
    Per-category concordance with safety weighting.
    """
    results = {}
    safety_weights = {
        "medications": 10, "allergies": 10,
        "diagnoses": 7, "plan": 5, "red_flags": 10
    }
    weighted_score = 0
    total_weight = 0

    for cat in categories:
        audio = set(audio_clinical_items.get(cat, []))
        epr = set(epr_clinical_items.get(cat, []))
        if not audio:
            continue
        preserved = audio & epr
        lost = audio - epr       # in audio, not in record
        added = epr - audio      # in record, not in audio

        cat_concordance = len(preserved) / len(audio)
        w = safety_weights.get(cat, 1)
        weighted_score += cat_concordance * w
        total_weight += w

        results[cat] = {
            "concordance": round(cat_concordance, 3),
            "preserved": list(preserved),
            "lost": list(lost),         # safety-critical omissions
            "added": list(added),       # potential hallucinations
        }

    results["weighted_overall"] = round(weighted_score / total_weight, 3) if total_weight else 0
    return results
```

**Limitations**

> Requires expert annotation of source audio as ground truth. Expensive and labour-intensive. Cannot scale to continuous monitoring without automation (which doesn't yet exist for audio→clinical-item extraction).

**Novel Thinking / Implications**

> 💡 This is the metric the entire field should be targeting but almost nobody measures. Every other metric is a proxy for this one. VeriFact gets close by checking against existing EHR, but source-to-record concordance checks against what was actually said — a fundamentally stronger test. A national benchmark programme could fund periodic SRC audits as the definitive AVT safety assessment.

---

### 🔵 Cumulative Information Yield

The positive framing of source-to-record concordance: what proportion of the clinical information present in the source audio successfully survives the entire pipeline and appears in the final EPR record. Where Source-to-Record Concordance measures preservation rate (how much was preserved), Cumulative Information Yield measures the distributional yield across clinical categories — so it exposes systematic category bias (e.g. a system that yields 95% on medications but 60% on psychosocial content).

|Dimension              |Value                                                                            |
|-----------------------|---------------------------------------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                                                   |
|**Measurement Cadence**|Periodic audit                                                                   |
|**Pipeline Layer**     |End-to-End                                                                       |
|**Assurance Question** |Safety                                                                           |
|**Measurement Method** |Hybrid                                                                           |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                                   |
|**Responsible Actors** |Academic, National Body                                                          |
|**Maturity**           |Proposed / Novel                                                                 |
|**Outcome Type**       |Distal                                                                           |
|**Source**             |Extension of existing Source-to-Record Concordance with categorical yield decomposition|

**Why this tier?**

> Resource-intensive evaluation requiring expert annotation of source audio, organised into categorical yield rather than binary preservation. Best suited for national evaluation programme. Per-category reporting reveals systematic content bias invisible to aggregate preservation metrics.

**Formal Definition**

```
For each clinical category c ∈ C = {medications, allergies, diagnoses, symptoms, plan, safety_netting, social_context, psychosocial, red_flags}: Yield(c) = |items_in_c_present_in_record| / |items_in_c_in_source|. Composite: Yield_weighted = Σ w_c × Yield(c), where w_c are clinical importance weights. Report per-category breakdown alongside composite — the aggregate obscures category bias.
```

**Limitations**

> Categorical annotation of source audio is even more labour-intensive than binary annotation. Category boundaries are contested (is "stopped smoking 5 years ago" social context or relevant history?). Weight assignment for the composite is subjective.

**Novel Thinking / Implications**

> 💡 The most common finding in ambient scribe evaluation is systematic yield bias toward clinical content the model recognises as "medical" (medications, symptoms, diagnoses) and away from content it treats as peripheral (social context, psychosocial factors, patient concerns that don't map to a code). This bias is invisible to concordance metrics that treat all clinical items equally — but it has direct consequences for patient-centred care and safeguarding. Per-category yield reporting makes the bias visible and actionable.

### 🔵 Error Propagation / Cascade Analysis

End-to-end: tracking how a single upstream error amplifies or gets corrected through subsequent stages. An ASR misrecognition could be caught by the summariser (correction) or cascade into wrong coding and wrong EPR entry (amplification).

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Proposed — analogous to fault propagation analysis in safety engineering |

**Why this tier?**

> Requires controlled error injection and intermediate output access. Vendor-side testing or academic research. Deployers cannot perform without vendor cooperation.

**Formal Definition**

```
For each error e introduced at stage s: Propagation(e) ∈ {corrected, preserved, amplified}. Cascade Factor CF = Σ errors_in_final / Σ errors_at_source. CF < 1 = net error correction; CF > 1 = net error amplification. Report per error type and per stage transition.
```

**Code: Error cascade tracking**

```python
def trace_error_cascade(
    injected_errors: list[dict],  # {stage, error_type, content}
    stage_outputs: dict            # {stage_name: output_text}
):
    """
    Track injected errors through pipeline stages.
    Requires controlled error injection at specific stages.
    """
    STAGES = ["asr", "diarisation", "summarisation", "coding", "writeback"]
    cascade_results = []

    for error in injected_errors:
        trace = {"source": error, "fate": []}
        for stage in STAGES[STAGES.index(error["stage"])+1:]:
            output = stage_outputs[stage]
            if error_persists(error["content"], output):
                if error_amplified(error["content"], output):
                    trace["fate"].append({"stage": stage, "status": "amplified"})
                else:
                    trace["fate"].append({"stage": stage, "status": "preserved"})
            else:
                trace["fate"].append({"stage": stage, "status": "corrected"})
                break  # error corrected, stop tracing

        trace["final_status"] = trace["fate"][-1]["status"] if trace["fate"] else "source_only"
        cascade_results.append(trace)

    cf = sum(1 for r in cascade_results if r["final_status"] != "corrected") / len(cascade_results)
    return {"cascade_factor": round(cf, 3), "traces": cascade_results}
```

**Limitations**

> Requires controlled error injection and intermediate output access. Most vendors treat the pipeline as a black box.

**Novel Thinking / Implications**

> 💡 This is the AVT equivalent of fault propagation analysis in traditional safety engineering. The cascade factor tells you whether the multi-stage architecture is net-safe (CF < 1, stages catch each other's errors) or net-dangerous (CF > 1, errors compound). A vendor claiming their summariser 'compensates for ASR errors' should demonstrate CF < 1 with data.

---

### 🟡 Safety-Critical Information Chain of Custody

End-to-end per-item trace for highest-risk content: did this specific allergy survive ASR → diarisation → summarisation → coding → EPR field? A per-item trace, not a statistical rate.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Proposed — analogous to chain-of-custody in evidence management and traceability in safety-critical systems |

**Why this tier?**

> Quarterly CSO audit: pick 10 safety-critical items from sampled consultations, trace each through pipeline. Manual but feasible. Directly tests whether the system preserves what matters most.

**Formal Definition**

```
For each safety-critical item i ∈ {allergies, medications, dosages, red-flags}: Custody(i) = [present_at_ASR, present_at_diarisation, present_at_summary, present_at_coding, present_at_EPR]. Complete chain: all TRUE. Broken chain: identify break point.
```

**Code: Chain of custody trace**

```python
def chain_of_custody(item: str, stage_outputs: dict) -> dict:
    """
    Trace a safety-critical item through every pipeline stage.
    Returns the chain status and break point if applicable.
    """
    STAGES = ["transcript", "diarised_transcript", "summary",
              "coded_entries", "epr_record"]
    chain = {}
    break_point = None

    for stage in STAGES:
        present = item_present(item, stage_outputs.get(stage, ""))
        chain[stage] = present
        if not present and break_point is None:
            break_point = stage

    return {
        "item": item,
        "chain_complete": all(chain.values()),
        "chain": chain,
        "break_point": break_point,
        "risk_level": "critical" if break_point in ["coded_entries", "epr_record"]
                      else "high" if break_point in ["summary"]
                      else "medium" if break_point else "none"
    }

# Example: trace penicillin allergy through pipeline
result = chain_of_custody(
    item="penicillin allergy",
    stage_outputs={
        "transcript": "...allergic to penicillin...",
        "diarised_transcript": "PATIENT: ...allergic to penicillin...",
        "summary": "Allergies: penicillin",
        "coded_entries": "91936005 | Allergy to penicillin",
        "epr_record": "Allergy field: Penicillin"
    }
)
```

**Limitations**

> Requires access to intermediate outputs (transcript, diarised transcript, summary, codes) — most vendors expose only the final note. Per-item tracing is manual without automation.

**Novel Thinking / Implications**

> 💡 This is the audit methodology that a CSO should be able to perform. Pick 10 safety-critical items from a sample of consultations and trace each through the pipeline. If any chain breaks, you know exactly where the system fails. This should be a Day Zero acceptance test and a quarterly audit procedure.

---

### 🔵 Compound Demographic Performance

End-to-end: demographic performance gap measured at the final output, not just at ASR. ASR bias against an accent might be corrected by summarisation (context inference) or amplified (hallucination to fill gaps).

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, National Body |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Proposed — extends demographic-disaggregated WER to end-to-end measurement |

**Why this tier?**

> Extends demographic WER to end-to-end measurement. Requires demographic-linked evaluation at final output level. National programme candidate.

**Formal Definition**

```
For demographic group g: E2E_gap = Quality(g_majority) - Quality(g_minority) measured on final note quality, not intermediate WER. Compare: E2E_gap vs ASR_gap. If E2E_gap > ASR_gap: pipeline amplifies bias. If E2E_gap < ASR_gap: pipeline partially compensates.
```

**Limitations**

> Requires demographic-linked evaluation data at the final output level, not just ASR. Even more resource-intensive than disaggregated WER.

**Novel Thinking / Implications**

> 💡 The critical question: does the pipeline as a whole reduce or amplify demographic disparities? A system could have biased ASR but fair summarisation (compensating), or fair ASR but biased summarisation (introducing new disparities). Only end-to-end demographic measurement reveals the net effect.

---

### 🔵 Semantic Drift Accumulation

End-to-end: measuring cumulative meaning transformation across stages. Each stage subtly transforms meaning — 'occasional chest tightness on stairs' → 'chest pain on exertion'. Each individual transformation may be defensible; the cumulative drift may not be.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Proposed — inspired by signal processing concept of cumulative distortion |

**Why this tier?**

> Research metric. Embedding-based similarity is a crude proxy for clinical meaning preservation. Conceptually important but not operationally ready.

**Formal Definition**

```
Drift(audio, note) = 1 - SemanticSimilarity(meaning(audio), meaning(note)). Decompose per stage: Drift_total = Σ Drift(stage_n, stage_n+1). Track: local_drift (each stage) vs cumulative_drift (end-to-end). If cumulative >> Σ local: drift interactions are non-linear.
```

**Code: Semantic drift measurement**

```python
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def measure_semantic_drift(stage_texts: dict) -> dict:
    """
    Measure meaning transformation between pipeline stages.
    stage_texts: ordered dict of {stage_name: text}
    """
    stages = list(stage_texts.keys())
    embeddings = {s: model.encode(t) for s, t in stage_texts.items()}

    # Per-stage drift (adjacent stages)
    local_drifts = {}
    for i in range(len(stages)-1):
        s1, s2 = stages[i], stages[i+1]
        cos_sim = np.dot(embeddings[s1], embeddings[s2]) / (
            np.linalg.norm(embeddings[s1]) * np.linalg.norm(embeddings[s2]))
        local_drifts[f"{s1}→{s2}"] = round(1 - cos_sim, 4)

    # End-to-end drift
    e2e_sim = np.dot(embeddings[stages[0]], embeddings[stages[-1]]) / (
        np.linalg.norm(embeddings[stages[0]]) * np.linalg.norm(embeddings[stages[-1]]))

    return {
        "local_drifts": local_drifts,
        "cumulative_drift": round(1 - e2e_sim, 4),
        "sum_local": round(sum(local_drifts.values()), 4),
        "non_linearity": round((1-e2e_sim) - sum(local_drifts.values()), 4),
        "alert": (1 - e2e_sim) > 0.3  # calibrate threshold
    }
```

**Limitations**

> Embedding-based similarity is a crude proxy for clinical meaning preservation. Two texts can be semantically distant but clinically equivalent (appropriate medical abstraction) or semantically close but clinically different (subtle dosage change).

**Novel Thinking / Implications**

> 💡 Not all drift is bad — 'occasional tightness going upstairs' → 'exertional chest pain' is appropriate medical abstraction. The question is whether the drift preserves clinical decision-relevance. A clinically-aware drift metric would weight drift on safety-critical elements higher than drift on contextual description.

---

### 🟡 Pipeline Non-Determinism / Reproducibility

End-to-end: if you re-process the same audio, do you get the same output? Each stochastic component introduces variance. Compound variance could mean the same consultation produces materially different notes on different runs.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Proposed — standard practice in safety-critical software testing but not yet applied to AVT pipelines |

**Why this tier?**

> Vendor should test: process same audio N times, verify safety-critical items are identical across runs. Deployer should request results. Non-deterministic safety items = deployment blocker.

**Formal Definition**

```
Process same audio N times (N ≥ 10). Reproducibility R = mean pairwise similarity across N outputs. Variance V = 1 - R. Safety-critical reproducibility: R_safety = proportion of runs where all safety-critical items (medications, allergies) are identical across all outputs.
```

**Code: Reproducibility testing**

```python
from itertools import combinations

def test_reproducibility(audio_path: str, pipeline, n_runs: int = 10):
    """
    Process same audio N times, measure output variance.
    """
    outputs = [pipeline.process(audio_path) for _ in range(n_runs)]

    # Pairwise similarity
    pairs = list(combinations(range(n_runs), 2))
    similarities = [
        text_similarity(outputs[i], outputs[j])
        for i, j in pairs
    ]

    # Safety-critical item consistency
    safety_items_per_run = [
        extract_safety_items(out)  # medications, allergies, diagnoses
        for out in outputs
    ]
    # All runs must agree on safety items
    safety_consistent = all(
        s == safety_items_per_run[0]
        for s in safety_items_per_run
    )

    return {
        "mean_similarity": round(np.mean(similarities), 4),
        "min_similarity": round(min(similarities), 4),
        "variance": round(1 - np.mean(similarities), 4),
        "safety_items_consistent": safety_consistent,
        "n_unique_medication_sets": len(set(
            frozenset(s.get("medications", []))
            for s in safety_items_per_run
        )),
        "alert": not safety_consistent
    }
```

**Limitations**

> Computationally expensive (N × full pipeline runs). Temperature=0 doesn't guarantee determinism with batched inference. Some variation may be acceptable for non-safety content.

**Novel Thinking / Implications**

> 💡 If the same consultation produces different medication lists on different runs, the system is fundamentally unsuitable for safety-critical use regardless of its average accuracy. Safety-critical reproducibility (identical safety items across all runs) should be a hard pre-deployment gate, not a soft recommendation.

---

### 🔵 Error Attribution Analysis

End-to-end: when an error appears in the final output, which stage introduced it? Essential for improvement but requires intermediate output logging most vendors don't expose.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Proposed — analogous to root cause analysis in incident investigation |

**Why this tier?**

> Requires vendor to expose intermediate outputs. Essential for systematic improvement but most vendors treat the pipeline as a black box.

**Formal Definition**

```
For each error e in final output: Attribution(e) = stage s where e first appears OR where correct content was last present. If e not in transcript → ASR error. If in transcript but not in summary → summarisation error. Requires full intermediate output chain.
```

**Limitations**

> Requires vendors to expose intermediate outputs (raw transcript, diarised transcript, pre-coding summary). Most treat the pipeline as a black box. Contractual transparency requirements needed.

**Novel Thinking / Implications**

> 💡 Without error attribution, you can't improve the system rationally. Is the hallucination rate driven by ASR feeding garbled text to the summariser, or by the summariser inventing content from clean transcript? The intervention is completely different. Vendors should be contractually required to provide intermediate output access for error attribution audits.

---

### 🔵 Clinical Decision Equivalence

End-to-end: does the final note support the same clinical decisions a clinician present at the consultation would make? The ultimate distal outcome metric connecting documentation to patient safety.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Academic, National Body |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Proposed — the ultimate validity test for clinical documentation |

**Why this tier?**

> Gold-standard distal outcome metric. Extremely resource-intensive (blinded clinician decision comparison). National research programme candidate.

**Formal Definition**

```
Present note to blinded clinician(s). Clinician makes clinical decisions (diagnosis, plan, prescribing) based solely on note. Compare with decisions of clinician who observed original consultation. Equivalence = |decisions_matching| / |total_decisions|. Per category: diagnostic, therapeutic, safety-netting, follow-up.
```

**Limitations**

> Extremely resource-intensive: requires blinded clinical decision-making from multiple clinicians. Inter-clinician variation in decision-making adds noise. Simulated decisions may not reflect real-world behaviour.

**⚠️ Underspecification Warning (Tier B — conceptually essential, operationally impractical)**

> Clinical Decision Equivalence is conceptually the most important metric in the taxonomy for distal outcome validation — it directly tests whether AVT-generated notes support the same clinical decisions as direct observation, which is what AVT ultimately needs to do to be safe. But measurement methodology is extremely resource-intensive: blinded clinical decision-making from multiple clinicians per case, inter-clinician variation adding noise, simulated decision contexts differing from real-world behaviour under time pressure. No validated protocol exists. No threshold for "adequate equivalence" has been established. Best interpreted as a target for national or academic evaluation programmes rather than deployer-level assessment. When operationalised, the study design must specify: (a) number of clinicians per case and selection criteria; (b) blinding methodology and how information leakage is prevented; (c) decision categories assessed (diagnostic, therapeutic, safety-netting, follow-up); (d) agreement metric (kappa, per-category accuracy, weighted agreement); (e) clinical complexity stratification; (f) handling of inter-clinician disagreement in the ground-truth condition.

**Novel Thinking / Implications**

> 💡 This is the metric that closes the proximal-distal gap. If a note produced by AVT leads to the same clinical decisions as direct observation, the documentation is functionally safe regardless of WER, ROUGE, or any other proxy metric. This should be the gold-standard validation for any AVT claiming clinical deployment readiness.

---

### 🟡 Full-Pipeline Latency Budget

End-to-end: total time from consultation end to note availability in EPR, broken down by stage. Not just ASR RTF — the full wait before a clinician can review.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Proposed as operational metric — RTF alone doesn't capture full workflow impact |

**Why this tier?**

> Operational metric deployers can measure: time from consultation end to note availability. Directly affects review quality — if note arrives after next patient, review suffers.

**Formal Definition**

```
L_total = Σ L_stage for stages ∈ {ASR, diarisation, summarisation, coding, write-back, EPR rendering}. Report: L_total distribution (P50, P95, P99). Per-stage breakdown identifies bottlenecks. Clinical constraint: L_total should be < time between consultations.
```

**Limitations**

> End-to-end latency depends on infrastructure (network, cloud processing, EPR API speed) not just AI model performance.

**Novel Thinking / Implications**

> 💡 If the note isn't available before the next patient arrives, the clinician either reviews it later (losing context) or doesn't review it at all (rubber-stamping). Latency directly affects the quality of human oversight. The pipeline latency budget should be a deployment acceptance criterion.

---

### 🟡 Pipeline Failure Recovery

When one stage fails (e.g. diarisation crashes), what does the system produce? Graceful degradation vs catastrophic failure. Most metrics assume the pipeline runs to completion — but partial failures are common in production.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Standard fault tolerance testing applied to AVT pipelines |

**Why this tier?**

> Important pre-deployment safety test. Vendor responsibility but should be a procurement question.

**Formal Definition**

```
For each pipeline stage, simulate failure and assess: (1) Does the system produce output? (2) Is the output flagged as degraded? (3) Is the failure logged? (4) Is the clinician notified? Score: graceful = output produced, flagged, logged, notified.
```

**Limitations**

> Requires controlled failure injection at specific pipeline stages. Most vendors test happy path more than failure modes.

**Novel Thinking / Implications**

> 💡 The dangerous failure mode is silent degradation: the pipeline produces output that looks normal but is built on a failed component. A diarisation failure could cause all speech to be attributed to the clinician — producing a confident-looking note with completely wrong attribution. The clinician reviewing the note has no signal that anything went wrong. Pre-deployment testing must include controlled failure injection.

---

### 🔵 Round-Trip Information Loss

If the AVT-generated note were used to reconstruct the original consultation, how much would be lost? An information-theoretic complement to source-to-record concordance — measures total information preserved through the pipeline.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Information theory applied to clinical documentation |

**Why this tier?**

> Research metric. Theoretically interesting but not operationally measurable at scale.

**Formal Definition**

```
Round-Trip Loss = 1 - I(audio; note) / H(audio), where I is mutual information and H is entropy. In practice: have a clinician attempt to answer specific questions about the consultation using only the note vs the full audio; compare answer accuracy.
```

**Limitations**

> Theoretical metric; practical measurement is approximate. Information loss is not always bad — appropriate medical abstraction is loss in the technical sense.

**Novel Thinking / Implications**

> 💡 Different from source-to-record concordance because it asks about all information, not just clinical items. Includes contextual information that may matter for safeguarding, family dynamics, patient understanding — content that AVT systems systematically strip but that clinicians sometimes rely on.

---

# Part C — The Human Layer

## Human Factors & Workflow

*The human in the loop. Whether oversight actually functions or erodes over time.*

**Tier breakdown**: 🟢 3 Tier 1 · 🟡 5 Tier 2 · 🔵 7 Tier 3

### Family: Post-Generation Correction

> **Parent construct** — what clinicians do to AI-generated notes between generation and sign-off, and what that behaviour tells us about both AI quality and human oversight.
>
> The next four metrics all measure human correction of AI output but at different levels of resolution. Treating them as independent metrics misses the fact that they form a four-tier family, where each tier adds diagnostic depth at the cost of additional measurement infrastructure. A deployer with limited governance capacity can start at the first tier and add tiers as maturity grows.
>
> **Four tiers of increasing resolution:**
>
> 1. **Binary — was the note edited at all?** Cheapest to collect from EPR workflow telemetry. System-level monitoring metric. Useful for trending but clinically uninformative in isolation — a low edit rate can mean excellent AI or inadequate review, and only triangulation with other metrics distinguishes them. This is the Edit Rate metric.
>
> 2. **Magnitude — how much was edited?** Measured via edit distance (Levenshtein, TER, HTER, or compression-based). Adds signal about the scale of correction effort. Critical refinement: distinguish **semantic edits** (changing clinical meaning — adding a missed symptom, correcting a drug name) from **stylistic edits** (formatting, phrasing preference). Compression-based edit distance (arXiv 2024) has been shown to correlate better with actual human effort than raw Levenshtein because it captures the structural nature of the change. Magnitude is implicit in the Edit Type Classification metric, which decomposes edits into categories that map to magnitude.
>
> 3. **Effort and locus — what kind of work, and where in the note?** Measured via Edit Type Classification (additions / deletions / modifications / structural) and Edit Location Distribution (which sections of the note attract the most edits). Tells you which failure modes are active: predominantly additions indicate an omission problem; predominantly deletions indicate a hallucination problem; concentration in the "plan" section indicates the AI extracts facts well but struggles with clinical reasoning. This is where the family becomes diagnostic rather than just descriptive.
>
> 4. **Longitudinal pattern — how is the behaviour changing over time?** The Edit-Pattern Monitoring at Scale metric (Abridge, across 1M+ encounters per week) captures fleet-wide edit dynamics and is the most scalable quality signal currently available — but it is locked inside one vendor's proprietary infrastructure. The open research question is whether similar pattern monitoring can be built as an open standard.
>
> **A severity taxonomy for edits.** Not all edits carry equal weight. Adapted from CREOLA and edit-pattern disclosures, edits fall into four severity categories:
>
> - **Safety-critical correction** — fixing a fabricated medication, corrected allergy, reversed negation, or wrong dose. These are the edits that prevent harm.
> - **Clinical addition** — adding a missed symptom, examination finding, or plan element. Quality improvement, not harm prevention.
> - **Stylistic preference** — clinician preference for phrasing, structure, or formatting. Often the majority of edits by count but the minority by safety value.
> - **Structural reorganisation** — moving content between sections, consolidating or splitting points. Quality improvement.
>
> Aggregate edit rate treats all four categories equally. A system with a 30% edit rate consisting mostly of safety-critical corrections is in much worse state than a system with a 60% edit rate consisting mostly of stylistic preference — but the raw numbers invert the assessment. Edit Type Classification is the metric in this family that makes severity visible.
>
> **The complacency trajectory.** The family has a temporal dimension that individual measurements miss. At Day Zero, edit rate is a quality signal — higher rates mean more errors being caught. Over months, as clinicians develop trust in the system, edit rate declines — but the decline could reflect either improving AI or increasing complacency, and distinguishing them requires triangulation. This is why Edit Rate is a Tier 1 continuous metric but must be read alongside Review-Before-Signing Rate, Time-to-Sign Distribution, and periodic Automation Bias Detection error injection. Edit rate alone is an ambiguous signal; the family is diagnostic.
>
> **Metrics in this family:**
> - 🟢 **Edit Rate (% Notes Edited)** — tier 1 binary. The entry point; cheapest and most widely measured. Must be triangulated to interpret.
> - 🟡 **Edit Type Classification** — tier 3 diagnostic decomposition. Reveals failure mode (omission-dominant vs hallucination-dominant vs stylistic).
> - 🟡 **Edit Location Distribution** — tier 3 locus analysis. Reveals which sections of the note the AI handles well vs poorly.
> - 🔵 **Edit-Pattern Monitoring at Scale** — tier 4 longitudinal fleet-level monitoring. Vendor-proprietary; informs what a national standard should require of all vendors.

---

### 🟢 Edit Rate (% Notes Edited)

Percentage of AI notes edited before approval. At Day Zero: quality signal. Declining trajectory: primary complacency indicator.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Day Zero Baseline, Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Abridge; NAS; Stanford framework |

**Why this tier?**

> Primary continuous complacency indicator. Deployer-measurable from EPR workflow data. NAS Day Zero SPI. The single most important human factors metric — trajectory reveals automation bias before incidents occur.

**Formal Definition**

```
ER(t) = |N_edited(t)| / |N_total(t)|. Complacency signal: dER/dt < 0 sustained ≥4 weeks without AI accuracy improvement. Alert: ER drops >15pp from baseline within 3 months.
```

**Code: Edit rate complacency detection**

```python
import pandas as pd
from scipy.stats import linregress

def detect_complacency(weekly_rates, baseline_weeks=4):
    df = pd.DataFrame(weekly_rates, columns=["week","rate"])
    baseline = df[df.week <= baseline_weeks]["rate"].mean()
    alerts = []
    for i in range(baseline_weeks, len(df)-3):
        window = df.iloc[i:i+4]
        slope, _, _, p, _ = linregress(window["week"], window["rate"])
        current = window["rate"].iloc[-1]
        if slope < -0.02 and p < 0.1 and baseline - current > 0.15:
            alerts.append({
                "week": int(window["week"].iloc[-1]),
                "current": round(current, 3),
                "action": "COMPLACENCY_REVIEW"})
    return {"baseline": round(baseline,3), "alerts": alerts}
```

**References**

- **Abridge**: Abridge edit-pattern methodology
- **NAS**: NAS Day Zero SPI

**Limitations**

> Ambiguous alone: low rate = good AI or poor review. Requires triangulation.

**Novel Thinking / Implications**

> 💡 Trajectory matters more than absolute value. 60% → 15% in 3 months should trigger review regardless of AI accuracy.

*See also: Edit Type Classification, Edit Location Distribution, Edit-Pattern Monitoring at Scale — all members of the Post-Generation Correction family. Edit Rate is the binary entry point; the other metrics add diagnostic depth. Interpret alongside Review-Before-Signing Rate and Time-to-Sign Distribution to distinguish improving AI from increasing complacency.*

---

### 🟡 Edit Type Classification

Categorising edits: additions (omission fix), deletions (hallucination fix), modifications, structural. Distribution diagnoses failure mode.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Abridge; DeepScore |

**Why this tier?**

> More granular than edit rate — diagnoses failure mode (additions = omission problem, deletions = hallucination problem). Requires NLP classification but adds substantial diagnostic value.

**Formal Definition**

```
Type(e) ∈ {Addition, Deletion, Modification, Structural}. P_add >> P_del → omission-dominant; P_del >> P_add → hallucination-dominant. Track over time to assess model updates.
```

**References**

- **Abridge**: 1M+ encounters/week
- **DeepScore**: 135,900 notes

**Limitations**

> Automated classification requires NLP.

**Novel Thinking / Implications**

> 💡 Mostly additions = omission problem; mostly deletions = hallucination problem.

*See also: Edit Rate, Edit Location Distribution, Edit-Pattern Monitoring at Scale — all members of the Post-Generation Correction family. Type classification is where the family becomes diagnostic rather than just descriptive: predominantly additions indicate an omission-dominant failure mode; predominantly deletions indicate a hallucination-dominant mode.*

---

### 🟢 Review-Before-Signing Rate

Notes demonstrably reviewed before sign-off. NAS: ≥95% threshold, <85% pause trigger.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | NAS Day Zero SPI; Stanford |

**Why this tier?**

> NAS Day Zero SPI with ≥95% threshold and <85% pause trigger. Deployer-measurable from EPR workflow telemetry. Directly monitors whether human oversight is functioning.

**Formal Definition**

```
RBS = |N_reviewed| / |N_total|. N_reviewed = notes with edit events, scroll events, or dwell > T_min. T_min = max(15s, 3s × word_count/100).
```

**References**

- **NAS**: ≥95% threshold, <85% pause trigger

**Limitations**

> Scrolling ≠ meaningful review.

**Novel Thinking / Implications**

> 💡 EPR should enforce architecturally: minimum dwell-time before approve activates.

---

### 🟢 Time-to-Sign Distribution

Duration between generation and approval. Model as distribution — tail of very-fast approvals is safety-critical.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | EPR workflow data; Stanford principles |

**Why this tier?**

> Deployer-measurable from EPR data. The tail of very-fast approvals (<5 seconds for complex notes) is the safety-critical population. Distribution analysis detects rubber-stamping patterns.

**Formal Definition**

```
TTS = t_approve - t_generated. Report: median, P5, P10, P90. Normalise: TTS_norm = TTS / word_count. Flag: TTS_norm < 0.5s/word suggests rubber-stamping.
```

**Code: Time-to-sign analysis**

```python
import numpy as np

def analyse_tts(data):  # list of {seconds, word_count}
    tts = np.array([d["seconds"] for d in data])
    wc = np.array([d["word_count"] for d in data])
    tts_norm = tts / np.maximum(wc, 1)
    return {
        "median_s": float(np.median(tts)),
        "p5_s": float(np.percentile(tts, 5)),
        "rubber_stamp_pct": float(np.mean(tts_norm < 0.5) * 100),
        "alert": bool(np.percentile(tts_norm, 5) < 0.3)}
```

**Limitations**

> Context-dependent. Must normalise by length/complexity.

**Novel Thinking / Implications**

> 💡 The tail of very-fast approvals is the safety-critical population.

---

### 🔵 Edit-Pattern Monitoring at Scale

Cross-system edit analysis (1M+/week, 150+ systems). Most scalable quality signal — locked inside one vendor.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Vendor-Proprietary |
| **Outcome Type** | Proximal |
| **Source** | Abridge whitepaper |

**Why this tier?**

> Vendor-proprietary (Abridge). Scale advantage creates a data moat. Informs what a national standard should require all vendors to provide.

**Formal Definition**

```
Aggregate across N systems: system-level distribution, edit type by specialty/template, temporal trends, outlier detection (>2σ from fleet mean). Uses anytime-valid sequential testing.
```

**References**

- **Abridge**: Oberst, Liang, Lipton (2024/2025)

**Limitations**

> Proprietary. Scale creates data moat.

**Novel Thinking / Implications**

> 💡 National standard should require standardised edit-pattern reporting from all vendors.

*See also: Edit Rate, Edit Type Classification, Edit Location Distribution — all members of the Post-Generation Correction family. Pattern monitoring operates at the fleet level to detect shifts invisible to any single deployer; informs what a national standard should require all vendors to provide.*

---

### 🟡 Automation Bias Detection (Error Injection)

Deliberately seeded errors to test clinician catch rate. The only metric directly measuring human oversight. All others are proxies.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Regional (ICB) |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Proposed in NAS framework |

**Why this tier?**

> The only metric that directly tests human oversight. Quarterly error injection audit. Ethically complex but feasible with appropriate safeguards. Should be Tier 1 aspiration for mature deployers.

**Formal Definition**

```
Inject known errors at rate r (e.g. 1 in 50) with defined severity. Detection Rate DR = |E_caught| / |E_injected| per severity. Oversight Effectiveness OE = Σ(severity_weight × DR) / Σ(weight). Must intercept before EPR write-back.
```

**References**

- **Analogy**: Laboratory EQA proficiency testing (NEQAS)

**Limitations**

> Ethical complexity. Must ensure errors intercepted before permanent record.

**⚠️ Underspecification Warning (Tier B — strong concept, ad hoc protocols)**

> Automation bias is well-defined conceptually (Parasuraman & Manzey, *Human Factors* 2010) but measurement protocols in clinical AI remain ad hoc. Most published studies use vignette-based designs comparing diagnostic accuracy with and without AI assistance; there is no standardised measurement protocol for production AVT systems operating under real clinical time pressure. No consensus exists on acceptable automation bias rate thresholds — one computational pathology study reported a 7% rate without specifying whether that was concerning or within expected bounds for the task. An active RCT (NCT07328815) is testing nudge interventions but results are not yet available. Until standardised production protocols emerge, document explicitly: (a) the injection methodology (how errors are generated), (b) the injection rate, (c) the severity distribution of injected errors, (d) the detection criteria (what counts as "caught"), (e) the timing of assessment. Changes to any of these make values incomparable across audits.

**Novel Thinking / Implications**

> 💡 Only metric directly measuring oversight function. Quarterly error injection with known difficulty thresholds.

---

### 🟡 Edit Location Distribution

Where in the note do clinicians make edits? Concentration in specific sections (history, examination, plan) reveals which sections the AI handles poorly. A diagnostic that complements edit type classification.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Extends edit-pattern monitoring with structural awareness |

**Why this tier?**

> Diagnostic enhancement to edit rate monitoring. Identifies which sections need more reviewer attention.

**Formal Definition**

```
For each note section s: Edit Density(s) = |edits_in_s| / |words_in_s|. Compare across sections. Sections with edit density >> average have systematic AI quality issues. Track over time to assess model improvement.
```

**Limitations**

> Requires consistent note structure for meaningful comparison.

**Novel Thinking / Implications**

> 💡 Reveals systematic quality patterns invisible to aggregate edit rate. If clinicians always edit the 'plan' section but rarely edit 'history', the AI is good at extracting facts but poor at synthesising clinical reasoning. This guides where vendor improvement should focus and where clinicians should pay particular attention during review.

*See also: Edit Rate, Edit Type Classification, Edit-Pattern Monitoring at Scale — all members of the Post-Generation Correction family. Locus analysis complements type classification: what kind of edit combined with where in the note identifies specific failure modes that either dimension alone would miss.*

---

### 🟡 Trust Calibration Survey

Clinician confidence vs actual accuracy. Overconfidence = automation bias risk. Gap between stated and behavioural trust is itself a metric.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Day Zero Baseline, Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Human factors literature; NAS framework |

**Why this tier?**

> Survey-based. Useful triangulation with behavioural metrics. Annual measurement tracks trust-behaviour gap evolution.

**Formal Definition**

```
Trust Calibration Gap TCG(c) = Stated_Trust(c) - Actual_Accuracy(c). TCG > 0 = overconfidence (dangerous). TCG < 0 = underconfidence (adoption barrier).
```

**References**

- **Trust in automation**: Lee & See (2004)

**Limitations**

> Self-report bias. Must triangulate with behavioural metrics.

**⚠️ Underspecification Warning (Tier B — concept defined, no AVT-validated instrument)**

> Multiple candidate instruments exist for trust calibration in clinical AI (TIAS, HATAS, AITI-H), but **none are validated specifically for ambient scribe contexts**. A 2024 Dokkyo Medical University review concluded that there are currently no accurate and objective measures available for evaluating trust calibration in clinical AI deployments. No thresholds exist for defining "appropriately calibrated" trust, and no empirical integration has been established between subjective trust measures and behavioural proxies (edit rate, review time, error detection) that would allow triangulation. Adapt TIAS or HATAS for AVT context as an interim measure, document the adaptation explicitly, and flag the absence of formal validation when reporting results. Pair with the existing behavioural complacency indicators (Edit Rate, Time-to-Sign, Review-Before-Signing) rather than relying on the survey instrument alone.

**Novel Thinking / Implications**

> 💡 'I always check carefully' + 5-second approval = trust calibration gap requiring architectural intervention.

---

### 🟡 Re-record / Abandonment Rate

Frequency of clinicians abandoning AVT mid-consultation and starting again, or abandoning the AVT-generated note entirely and writing manually. Strong dissatisfaction signal indicating either technical failure or fundamental quality issues.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Identified as strong dissatisfaction signal |

**Why this tier?**

> Strong leading indicator of system problems. Should trigger immediate investigation when rates rise.

**Formal Definition**

```
Re-record Rate = |consultations_with_restart| / |total_consultations|. Abandonment Rate = |notes_discarded_and_rewritten| / |total_notes|. Both should be near zero in steady state. Sudden increases indicate system regression.
```

**Limitations**

> Requires EPR workflow telemetry to detect restarts and abandonments. Some legitimate restart cases (technical issues) need to be distinguished from quality-driven restarts.

**Novel Thinking / Implications**

> 💡 Re-record rate is the canary in the coal mine. When clinicians start restarting consultations or abandoning notes, something has gone fundamentally wrong — either the system has degraded or the workflow is broken. This is a leading indicator that should trigger immediate investigation, not routine review.

---

### 🔵 Cognitive Load Assessment

Mental effort for review. Target: 'effortful but efficient' — enough to catch errors, not so much that time savings disappear.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | NASA-TLX adapted for clinical documentation review |

**Why this tier?**

> Research metric. NASA-TLX adaptation is established but adds burden. Physiological measures are research-only.

**Formal Definition**

```
Adapted NASA-TLX: Mental Demand, Temporal Demand, Effort, Frustration, Trust Burden. Each 0-100. Target CL: 30-60 (below = disengagement, above = no benefit).
```

**References**

- **NASA-TLX**: [NASA Task Load Index](https://humansystems.arc.nasa.gov/groups/TLX/)

**Limitations**

> Self-report. Adds burden.

**⚠️ Underspecification Warning (Tier B — generic validation, no AVT-specific calibration)**

> NASA-TLX is validated generically with acceptable individual-setting ICC of 0.71–0.81 (lower for group settings). However, for AVT specifically: no subscale selection protocol exists, no consensus on measurement timing (during encounter / immediately after charting / end of day / end of week), no documentation-specific adaptation of the instrument, and no established thresholds for "acceptable" cognitive load in AVT review tasks. The 60.7% reduction in composite cognitive load reported in a 2024 Abridge study is a point estimate with no reference scale for clinical interpretation — "60% less" of an undefined baseline is not directly actionable. Use NASA-TLX as an interim measure, specify the timing and subscale selection used, and avoid comparing raw scores across studies that use different protocols. The proposed **Verification Burden** metric (Human Factors & Workflow) is intended to capture a more specific construct that may ultimately prove more actionable than global cognitive load.

**Novel Thinking / Implications**

> 💡 Optimal load is non-obvious: too low = disengagement, too high = no benefit.

---

### 🔵 Inter-Clinician Edit Variance

Do different clinicians edit the same AI output similarly? High variance suggests either ambiguous AI output (different clinicians read it differently) or inconsistent quality standards across clinicians. Both are governance issues.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Extends inter-rater reliability concepts to AVT review |

**Why this tier?**

> Research-grade metric requiring controlled study. Important for understanding review reliability but not routine measurement.

**Formal Definition**

```
For sample of identical AI outputs reviewed by multiple clinicians: variance in edit count, edit type distribution, and edit content. Inter-rater reliability metrics on edit decisions.
```

**Limitations**

> Requires controlled study with multiple clinicians reviewing same outputs. Difficult to operationalise in routine practice.

**Novel Thinking / Implications**

> 💡 If Clinician A always edits the AI output extensively and Clinician B never edits it, the issue might be either clinician (one is too critical, the other is too lax) or the AI (the output is ambiguous). Inter-clinician variance reveals whether the review function is consistent — a prerequisite for meaningful aggregate metrics.

---

### 🔵 Clinical Documentation Skill Attenuation

Longitudinal ability to document without AI. Sleeper risk — if a generation trains with AVT, baseline capability degrades.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Aviation skill degradation literature |

**Why this tier?**

> Long-term longitudinal study. Effects take years to manifest. Important for workforce planning but not actionable at individual deployer level.

**Formal Definition**

```
Annual: clinicians document N simulated encounters without AI, scored via PDSQI-9. SA(t) = PDSQI9_noAI(t) - PDSQI9_noAI(t-1). Negative SA = attenuation. Compare trainees against pre-AVT cohort norms.
```

**References**

- **Aviation analogy**: Casner & Schooler (2014) — pilot skill degradation

**Limitations**

> Long-term study. Hard to isolate AVT as cause.

**Novel Thinking / Implications**

> 💡 Medical education bodies should be tracking this now.

---

### 🔵 Cognitive Offloading Rate

Proportion of clinicians who report relying on AI for content recall ('I don't need to remember, the AI will catch it'). Different from automation bias — this is active delegation rather than passive trust. Predicts skill attenuation.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Cognitive offloading literature; distinct from automation bias |

**Why this tier?**

> Research metric. Important for understanding workforce impact but not routine measurement.

**Formal Definition**

```
Survey-based: 'I rely on the AVT system to capture details I might otherwise need to remember during consultations' (5-point Likert). Offloading Rate = proportion answering 'agree' or 'strongly agree'. Track over time to detect increasing dependence.
```

**Limitations**

> Self-report bias. Clinicians may not be aware of their own cognitive offloading.

**Novel Thinking / Implications**

> 💡 Offloading is the precursor to skill attenuation. When clinicians actively delegate cognitive functions to the AI, they stop practicing those functions, which then atrophy. This is the mechanism by which AVT could degrade clinical workforce capability over time. Tracking offloading provides an early signal before measurable skill loss occurs.

---

### 🔵 Trust Halo Decay Rate

Whether initial high trust persists after errors. Absent decay = dangerous over-trust. Trust halo drives off-label scope creep.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Trust halo effect analysis |

**Why this tier?**

> Research metric requiring longitudinal measurement. Conceptually important for understanding off-label use drivers but not operationally measurable at scale.

**Formal Definition**

```
Longitudinal T(t). After error at t_e, decay rate λ = -dT/dt for t > t_e. Healthy: λ > 0 (appropriate recalibration). Dangerous: λ ≈ 0 (trust unchanged despite evidence).
```

**Limitations**

> Longitudinal measurement required.

**⚠️ Underspecification Warning (Tier A — no validated measurement in clinical AI)**

> The trust halo effect is well-established in cognitive psychology but has **not been operationalised for clinical AI or AVT specifically**. The concept substantially overlaps with automation bias, and the empirical boundary between the two constructs is not established — it is unclear whether they should be measured as distinct phenomena or as facets of a common over-reliance construct. No validation studies exist. No measurement instruments have been adapted from cognitive psychology to the clinical AI context. Two viable paths forward: (a) define a specific experimental paradigm (e.g. testing whether positive experience with transcription accuracy transfers uncritically to trust in clinical summarisation accuracy, which is a different capability) and build validation evidence from there, or (b) fold the construct into the broader automation bias / over-reliance family until the measurement science matures enough to distinguish it meaningfully. Until one of these is done, any reported values should carry explicit acknowledgement of the definitional uncertainty.

**Novel Thinking / Implications**

> 💡 Trust halo → off-label use: over-trust drives scope creep. The halo is the mechanism; off-label use is the consequence.

---

### 🔵 Note Review Fatigue Trajectory

Review quality degradation over a clinical session. The 9am note review may be different from the 5pm note review, and AVT may amplify end-of-session fatigue effects by adding documentation review burden to existing clinical fatigue.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Clinical fatigue research applied to AVT review |

**Why this tier?**

> Research metric. Important workforce safety question but not routinely measurable.

**Formal Definition**

```
Track review quality metrics (time-to-sign, edit rate, error detection in injection audits) by time-of-day and session position. Fatigue Slope = degradation rate per hour into session. Significant negative slope indicates fatigue effects.
```

**Limitations**

> Confounded with case mix variation (afternoon clinics may have different complexity). Requires careful statistical controls.

**⚠️ Underspecification Warning (Tier A — underlying concept unoperationalised)**

> The broader concept of attention drift across a clinician's reviewing session has **no operationalised definition in AVT literature**. The Cognitive Drift Index (Frontiers in Neuroscience 2025) measures information consumers' judgment shifts in unrelated domains, not clinician review vigilance. A 2026 KevinMD essay described "the slow erosion of clinical humility" qualitatively but offered no measurement approach. No published study has established a detection methodology, thresholds, or relationship to patient safety outcomes. Proposed interim operationalisation for this taxonomy — to be treated as a working definition pending empirical validation — is a composite of (a) declining review time per note over a session, (b) reduced edit rate trajectory within sessions, and (c) reduced error detection rate in periodic injection testing stratified by time-of-session. This proposal has not been validated; deployers using it should document the operational definition applied and treat results as exploratory rather than diagnostic.

**Novel Thinking / Implications**

> 💡 If review quality degrades through the session, the safety implications are significant: the last patients of the day get the least rigorous oversight. AVT systems designed assuming consistent reviewer attention are operating outside that assumption for a meaningful fraction of consultations. This argues for fatigue-aware workflow design — perhaps requiring more thorough review for end-of-session notes, or rotating review responsibility.

---

---

### Sociotechnical & Resilience sub-cluster

*Systems-level constructs drawn from FRAM, Safety-II, and resilience engineering. These metrics assess the clinician-AVT joint cognitive system rather than AVT alone, and capture dimensions that standard human factors metrics miss — the gap between intended and actual practice, the hidden cost of verification, and the capacity to handle unexpected situations.*

---

### 🔵 Work-as-Imagined vs Work-as-Done Gap

The gap between how AVT is intended to be used (per procedures, training, and governance documentation) and how it is actually used in clinical practice. A construct from Hollnagel's FRAM methodology and the Safety-II tradition. Subsumes and generalises the existing Off-Label Use Detection metric — not every WAI/WAD gap is off-label, and not every adaptation is a safety problem, but the gap itself is diagnostically valuable.

|Dimension              |Value                                                                  |
|-----------------------|-----------------------------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                                         |
|**Measurement Cadence**|Periodic audit                                                         |
|**Pipeline Layer**     |Cross-cutting                                                          |
|**Assurance Question** |Safety                                                                 |
|**Measurement Method** |Hybrid                                                                 |
|**Lifecycle Phases**   |Periodic Audit                                                         |
|**Responsible Actors** |Deployer, Academic                                                     |
|**Maturity**           |Proposed / Novel                                                       |
|**Outcome Type**       |Distal                                                                 |
|**Source**             |Hollnagel FRAM methodology; JMIR 2026 SEIPS-based AVT evaluations      |

**Why this tier?**

> Research-grade metric requiring ethnographic observation and structured interview methodology. Not routinely measurable at deployer level. Academic or national evaluation programme responsibility.

**Formal Definition**

```
Three-step methodology: (1) Document WAI from training materials, SOPs, vendor guidance, and governance policies; (2) Observe WAD through shadowing, workflow analysis, and semi-structured clinician interviews; (3) Gap analysis — categorise deviations as {beneficial adaptation, neutral workaround, latent risk, active hazard}. Report gap count per category and exemplar descriptions rather than a single scalar — the qualitative detail is what supports intervention.
```

**Limitations**

> Ethnographic methods are resource-intensive and subjective. WAI is itself often poorly documented. Observer effects shape observed behaviour. Generalisation across practices is limited.

**Novel Thinking / Implications**

> 💡 Every complex sociotechnical system has a WAI/WAD gap — procedures can never fully specify practice. The Safety-II insight is that adaptations are not automatically failures; they are often what makes the system work at all. The diagnostic question is not "is there a gap?" (there always is) but "which gaps indicate genuine risk vs which indicate necessary adaptation that should be formalised back into WAI?" This metric surfaces the question; human judgment answers it.

---

### 🟡 Verification Burden

The additional workload created by the need to verify AI-generated content against clinical reality — reading the note, cross-checking against the conversation, identifying errors, making corrections. Distinct from the existing Cognitive Load Assessment metric, which measures total effort. Verification burden is specifically the checking overhead that exists only because the output needs checking. A well-calibrated AVT system minimises this burden; a poorly-calibrated one shifts documentation time into verification time and may eliminate the apparent efficiency gain.

|Dimension              |Value                                                               |
|-----------------------|--------------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                              |
|**Measurement Cadence**|Periodic audit                                                      |
|**Pipeline Layer**     |Cross-cutting                                                       |
|**Assurance Question** |Human Factors                                                       |
|**Measurement Method** |Hybrid                                                              |
|**Lifecycle Phases**   |Day Zero Baseline, Periodic Audit                                   |
|**Responsible Actors** |Deployer, Academic                                                  |
|**Maturity**           |Emerging                                                            |
|**Outcome Type**       |Proximal                                                            |
|**Source**             |JMIR 2026 e86166 SEIPS-based evaluation; GOSH Phase 4 TimeCat data  |

**Why this tier?**

> Conceptually important — distinguishes apparent efficiency gain from actual efficiency gain — but requires time-motion observation methodology (TimeCat or equivalent). Day Zero baseline plus periodic re-measurement supports trajectory analysis.

**Formal Definition**

```
VB = t_review + t_correction + t_cross_reference, measured per consultation. Baseline pre-AVT: equivalent activities (proofreading own notes, referencing structured fields). Net Verification Cost = VB_AVT - VB_pre-AVT. Efficiency gain = (t_documentation_pre - t_documentation_AVT) - Net Verification Cost. A genuinely efficient system has positive net gain after accounting for verification burden.
```

**Limitations**

> TimeCat or equivalent time-motion methodology is labour-intensive. Verification activities are often interleaved with other work and hard to isolate. Self-report on verification time is unreliable because the activity is partly automatic.

**Novel Thinking / Implications**

> 💡 The marketing claim "AVT saves 3 minutes of documentation time per consultation" is meaningless without verification burden accounting. A system that saves 3 minutes of typing but adds 4 minutes of verification has negative net efficiency — and research suggests this scenario is common early in deployment before clinicians develop efficient review patterns. Verification burden should be reported alongside every documentation time saving claim, or the claim should not be reported at all.

---

### 🔵 Resilience Capacities Assessment

Structured assessment of the clinician-AVT joint cognitive system against the four Safety-II resilience capacities: **responding** to unexpected events, **monitoring** for signs of degradation, **learning** from experience, and **anticipating** future challenges. From Hollnagel's resilience engineering framework. Applied not to AVT alone but to the combined human-machine system as it operates in context.

|Dimension              |Value                                                             |
|-----------------------|------------------------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                                    |
|**Measurement Cadence**|Periodic audit                                                    |
|**Pipeline Layer**     |Cross-cutting                                                     |
|**Assurance Question** |Safety                                                            |
|**Measurement Method** |Hybrid                                                            |
|**Lifecycle Phases**   |Periodic Audit                                                    |
|**Responsible Actors** |Deployer, National Body, Academic                                 |
|**Maturity**           |Proposed / Novel                                                  |
|**Outcome Type**       |Distal                                                            |
|**Source**             |Hollnagel Safety-II; FRAM methodology; resilience engineering literature|

**Why this tier?**

> Research framework applied at system level. Not a routine metric. National or academic responsibility for maturing the methodology into deployable assessment.

**Formal Definition**

```
Four capacity dimensions scored via structured scenario-based assessment and qualitative evaluation:
(1) Responding — when an AVT failure occurs mid-consultation (crash, silent degradation, wrong-patient data), how does the clinician-system respond? Recovery time, recovery completeness, downstream impact.
(2) Monitoring — what signals does the system provide that allow the clinician to detect degradation? Are those signals attended to in practice?
(3) Learning — when errors are discovered, how is that learning captured and integrated into future work? (Links to Hazard Log Completeness and Training Material Currency)
(4) Anticipating — does the deployer identify and prepare for foreseeable challenges (model updates, regulatory changes, novel failure modes)?
Score each capacity 1–5 with narrative justification. Composite is a profile, not a single number.
```

**Limitations**

> Assessment is qualitative and requires trained evaluators. Framework originally developed for complex sociotechnical systems (healthcare, aviation); application to AVT specifically is novel. Scoring inter-rater reliability has not been established for this application.

**Novel Thinking / Implications**

> 💡 Traditional safety metrics are Safety-I: counting failures and aiming for zero. Resilience metrics are Safety-II: assessing the capacity to handle failures that will inevitably occur. An AVT deployment with zero recorded incidents but weak resilience capacities is brittle — the first real test will reveal the gap. This metric family complements rather than replaces the incident-based metrics in Safety & Governance.

---

### 🟡 AI-Off Performance Test

Scheduled exercises where clinicians document a clinical encounter without AVT assistance, and the resulting documentation is assessed for quality against baseline standards. Provides an operational implementation of the existing Clinical Documentation Skill Attenuation concept — instead of inferring skill degradation longitudinally, directly measure current unassisted capability. Also doubles as business continuity assurance: can the clinical team function if AVT is unavailable?

|Dimension              |Value                                                                                                 |
|-----------------------|------------------------------------------------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                                                                |
|**Measurement Cadence**|Periodic audit                                                                                        |
|**Pipeline Layer**     |Cross-cutting                                                                                         |
|**Assurance Question** |Human Factors                                                                                         |
|**Measurement Method** |Hybrid                                                                                                |
|**Lifecycle Phases**   |Day Zero Baseline, Periodic Audit                                                                     |
|**Responsible Actors** |Deployer                                                                                              |
|**Maturity**           |Proposed / Novel                                                                                      |
|**Outcome Type**       |Distal                                                                                                |
|**Source**             |Operationalisation of existing Clinical Documentation Skill Attenuation metric; Lancet Gastroenterology 2025 endoscopist AI-off study (ADR fell 28.4%→22.4% when AI removed)|

**Why this tier?**

> Operationally feasible for any deployer willing to commit protected time. More actionable than longitudinal skill attenuation measurement because it provides current state data. Should be scheduled at Day Zero baseline and repeated annually.

**Formal Definition**

```
Protocol: (1) Schedule defined exercises where clinicians document simulated or real consultations without AVT; (2) Documentation is scored using PDSQI-9 or equivalent validated instrument; (3) Score is compared against the clinician's pre-AVT baseline (if available) and against peer benchmarks. Trajectory Metric = score_current - score_baseline. Cohort Analysis: compare clinicians trained with AVT from day one against those who learned without it.
```

**Limitations**

> Protected time is expensive. Simulated consultations differ from real consultations. Clinicians who know they are being assessed may perform differently. Pre-AVT baseline is often not available for individual clinicians.

**Novel Thinking / Implications**

> 💡 The endoscopy AI-off finding (adenoma detection rate falling from 28.4% to 22.4% when AI was removed after a period of AI use) is the first robust real-world evidence of clinical deskilling from AI dependency. For ambient scribes, the equivalent question is whether clinicians lose the ability to write a clinically complete note unassisted after a period of AVT use. This is testable today. The business continuity case — can the practice function during a vendor outage? — is almost sufficient reason to run the test regardless of the deskilling question.

# Part D — Impact & Outcomes

## Patient Experience

*Direct impact on the individual patient: consent, disclosure, therapeutic relationship.*

**Tier breakdown**: 🟢 1 Tier 1 · 🔵 5 Tier 3

### 🟢 Patient Opt-Out Rate

Percentage declining AVT. Disaggregate by demographics to reveal equity issues in consent model.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Patient Experience |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | NAS SPI; CQC Mythbuster 109 |

**Why this tier?**

> Deployer-measurable from practice records. Low-burden continuous monitoring. Rising rates signal trust issues. Demographic disaggregation reveals consent model equity.

**Formal Definition**

```
OOR = |P_optout| / |P_offered|. χ² test for independence between opt-out and demographic group. Significant association = inequitable consent model.
```

**References**

- **CQC**: Mythbuster 109: implied consent sufficient but patients must be informed

**Limitations**

> Low opt-out ≠ informed consent.

**Novel Thinking / Implications**

> 💡 Higher opt-out in specific demographics = equity issue in consent model, not just preference.

---

### 🔵 Patient-Perceived Accuracy

When patients are shown their AVT-generated notes, do they recognise the consultation? Distinct from clinician-judged accuracy — patients may identify omissions or distortions that clinicians miss because they were the speakers.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Patient Experience |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Patient-centred care evaluation methodology |

**Why this tier?**

> Important but resource-intensive. Best suited for periodic structured study rather than routine measurement.

**Formal Definition**

```
Patient survey after note generation: 'Does this note accurately reflect our conversation?' (5-point Likert, plus free-text comments). Accuracy Rate = proportion answering 'accurate' or 'very accurate'. Comments analysed for systematic complaint patterns.
```

**Limitations**

> Requires patient access to notes and willingness to provide feedback. Patient understanding of clinical documentation conventions varies.

**Novel Thinking / Implications**

> 💡 Patients are the only assessor who knows what was actually said in the consultation from their own perspective. They notice when their concerns were minimised, when the clinician's interpretation differs from their own, and when emotional content was stripped. With patient access to records becoming standard (NHS App), patient-perceived accuracy is increasingly important for trust in the clinical record.

---

### 🔵 Emotional Content Preservation

Does the note capture the patient's emotional state when clinically relevant? AVT systems trained on standard clinical notes may strip affective content that matters for mental health, end-of-life care, safeguarding, and complex consultations.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Patient Experience |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Identified gap in clinical AI evaluation — affective content is systematically deprioritised |

**Why this tier?**

> Critical for specific clinical contexts (mental health, palliative care, safeguarding) but not universally applicable.

**Formal Definition**

```
For consultations involving emotional content (annotated): proportion of clinically relevant emotional markers preserved in summary. Categories: distress, grief, fear, ambivalence, hope. Required for: mental health, end-of-life, safeguarding, life-limiting illness consultations.
```

**Limitations**

> Emotional content annotation is subjective. Different clinical contexts have different requirements for affective documentation.

**Novel Thinking / Implications**

> 💡 AVT systems trained on standard primary care notes have learned that emotional content is rarely documented. When deployed in mental health, palliative care, or safeguarding contexts, this learned behaviour becomes a serious gap. The patient who said 'I just don't know how I'll cope' deserves to have that documented — but the AI may strip it as non-clinical content.

---

### 🔵 Cultural & Linguistic Appropriateness

Does the note use language that respects the patient's cultural and linguistic context? Important for shared records that patients can access. Includes avoiding stigmatising language and respecting how patients describe their own conditions.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Patient Experience |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Patient-centred care literature; growing concern with patient access to records |

**Why this tier?**

> Important quality dimension but requires structured audit by appropriate reviewers.

**Formal Definition**

```
Audit for: (1) stigmatising language ('drug-seeking', 'non-compliant', 'frequent flyer'); (2) cultural assumptions; (3) translation of patient's own terms into clinical jargon when patient access is enabled. Proportion of notes flagged in audit.
```

**Limitations**

> Cultural appropriateness is highly context-dependent. Audit requires diverse reviewers.

**Novel Thinking / Implications**

> 💡 AVT systems trained on legacy clinical notes may perpetuate language patterns that are inappropriate when patients can read their own records. The language that was acceptable when notes were clinician-only is sometimes unacceptable when notes are shared. This is a quiet failure mode — the AI is faithfully reproducing patterns from its training data that need to change.

---

### 🔵 Chilling Effect Assessment

Whether AVT suppresses sensitive disclosures. Most under-researched risk — population-level safety issue if record becomes systematically biased.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Patient Experience |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | NHSE LLM framework gap analysis |

**Why this tier?**

> The most under-researched AVT risk but extremely difficult to measure — detecting information that wasn't shared. Requires carefully designed qualitative research.

**Formal Definition**

```
Disclosure Rate Ratio DRR = DR_AVT / DR_noAVT for sensitive categories (mental health, substance use, sexual health, domestic abuse). DRR < 1.0 = chilling effect. Mixed-methods: quantitative + qualitative.
```

**Limitations**

> Detecting information not shared requires careful qualitative research.

**Novel Thinking / Implications**

> 💡 If AVT suppresses sensitive disclosures, the record becomes systematically biased — missing exactly the information that matters most.

---

### 🔵 Therapeutic Relationship Impact

How AVT affects consultation quality. Net impact depends on whether review is in-consultation or post-consultation.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Patient Experience |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Consultation quality literature |

**Why this tier?**

> Subjective, context-dependent. Positive novelty effect masks longer-term changes. Research priority but not routine deployer measurement.

**Formal Definition**

```
Multi-dimensional: (1) PCQ-18 adapted; (2) Clinician engagement scale; (3) Eye contact ratio; (4) Consultation duration. Pre/post crossover design.
```

**Limitations**

> Novelty effect may mask long-term changes.

**Novel Thinking / Implications**

> 💡 Marketed as freeing clinicians, but review-before-signing creates new post-consultation task. Workflow design determines the outcome.

---

---

### Patient Clinical Outcomes sub-cluster

*Direct addressing of the Coiera & Fraile-Navarro (JMIR Med Inform February 2026) critique that the AVT evaluation field measures proximal metrics and assumes they correlate with patient outcomes. This sub-cluster makes the distal outcome measurement explicit.*

---

### 🟡 Full Attentiveness Rate

Proportion of consultation time during which the clinician is fully attentive to the patient, measured objectively rather than through self-report. Distinct from the existing Therapeutic Relationship Impact metric, which captures subjective perception. Stults et al. (2025) reported an increase from 57.9% to 93.0% with ambient AI — a large effect size that, if reproducible, represents one of the strongest AVT benefit signals currently available.

|Dimension              |Value                                                           |
|-----------------------|----------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                          |
|**Measurement Cadence**|Periodic audit                                                  |
|**Pipeline Layer**     |Cross-cutting                                                   |
|**Assurance Question** |Patient Experience                                              |
|**Measurement Method** |Passive Observational                                           |
|**Lifecycle Phases**   |Day Zero Baseline, Periodic Audit                               |
|**Responsible Actors** |Deployer, Academic                                              |
|**Maturity**           |Emerging                                                        |
|**Outcome Type**       |Proximal                                                        |
|**Source**             |Stults et al. 2025 (57.9%→93.0% improvement with ambient AI)     |

**Why this tier?**

> Observable with time-motion methodology (TimeCat or equivalent). Day Zero baseline enables pre/post comparison. Important for establishing genuine patient experience improvement rather than self-reported improvement.

**Formal Definition**

```
Full Attentiveness = t_eye_contact + t_active_listening + t_direct_engagement / t_total_consultation. Measured via TimeCat observation, video analysis, or (where accepted by patients) automated gaze tracking. Baseline pre-AVT vs post-AVT comparison. Report as distribution across consultations, not just mean — the clinically relevant improvement is often in the tail (consultations where the clinician was previously heavily divided between patient and screen).
```

**Limitations**

> Observation methodology is labour-intensive. Observer effects change clinician behaviour. Eye contact patterns are culturally variable and not always a valid proxy for attention. Patient consent required for video or automated tracking.

**Novel Thinking / Implications**

> 💡 This is probably the strongest candidate for a positive AVT benefit metric that isn't subject to the Coiera critique. Unlike documentation time saved (which says nothing about patient outcome), attentiveness is directly related to the therapeutic alliance, to patient disclosure, and to shared decision-making. If the Stults et al. finding is reproducible, it becomes the primary argument for AVT adoption on quality-of-care grounds rather than efficiency grounds.

---

### 🔵 Patient Comprehension of AI-Generated Summaries

When AI-generated clinical summaries are shared with patients (via NHS App, patient portals, or printed after-visit summaries), do patients actually understand them? Distinct from the existing Patient-Perceived Accuracy metric, which measures recognition ("does this match our conversation?"). Comprehension measures whether the patient can correctly state what the summary says about their condition, medications, and next steps.

|Dimension              |Value                                                                    |
|-----------------------|-------------------------------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                                           |
|**Measurement Cadence**|Periodic audit                                                           |
|**Pipeline Layer**     |Summarisation                                                            |
|**Assurance Question** |Patient Experience                                                       |
|**Measurement Method** |Survey                                                                   |
|**Lifecycle Phases**   |Periodic Audit                                                           |
|**Responsible Actors** |Deployer, Academic                                                       |
|**Maturity**           |Proposed / Novel                                                         |
|**Outcome Type**       |Distal                                                                   |
|**Source**             |Health literacy research; growing relevance as patient access to records expands|

**Why this tier?**

> Important as patient-facing summaries become routine. Research-grade measurement methodology required. Best suited for periodic structured study.

**Formal Definition**

```
Patient Comprehension Test: after receiving an AI-generated summary, patient is asked structured questions about: (1) primary diagnosis or problem identified; (2) medications prescribed and their purpose; (3) follow-up actions required; (4) warning signs requiring re-contact. Comprehension Rate = |correctly_answered_questions| / |total_questions|. Disaggregate by health literacy level, age, language, and education to detect differential comprehension.
```

**Limitations**

> Requires patient time and willingness. Cultural and language barriers affect comprehension measurement itself. Summaries generated for clinical purposes may use language appropriate for clinicians but inaccessible to patients — this is a separable design question from AVT accuracy.

**Novel Thinking / Implications**

> 💡 With NHS App access making records patient-facing by default, AI-generated summaries written in clinical language become a health literacy barrier. A summary that is technically correct but uses "dyspnoea" instead of "breathlessness" is accurate from an AVT evaluation standpoint but opaque to the patient. Comprehension measurement should drive a design choice: should AVT generate two versions (clinical record + patient summary) or one version written for both audiences?

---

### 🔵 Downstream Diagnostic Accuracy

Whether clinicians making subsequent decisions based on AVT-generated notes arrive at the same diagnostic and management conclusions they would have reached if they had access to the original consultation. Measured through controlled clinical reasoning studies where clinicians work from AVT notes vs verbatim transcripts vs direct observation. The distal outcome metric Coiera & Fraile-Navarro argue is missing from current AVT evaluation.

|Dimension              |Value                                                             |
|-----------------------|------------------------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                                    |
|**Measurement Cadence**|Periodic audit                                                    |
|**Pipeline Layer**     |End-to-End                                                        |
|**Assurance Question** |Safety                                                            |
|**Measurement Method** |Human Review                                                      |
|**Lifecycle Phases**   |Periodic Audit                                                    |
|**Responsible Actors** |Academic, National Body                                           |
|**Maturity**           |Proposed / Novel                                                  |
|**Outcome Type**       |Distal                                                            |
|**Source**             |Coiera & Fraile-Navarro, JMIR Med Inform February 2026            |

**Why this tier?**

> Gold-standard distal outcome metric. Extremely resource-intensive. National research programme responsibility. Complements the existing Clinical Decision Equivalence metric by focusing specifically on diagnostic rather than management decisions.

**Formal Definition**

```
Blinded multi-clinician study design: same clinical case presented in three conditions — (a) clinician observes consultation directly, (b) clinician reads AVT-generated note, (c) clinician reads verbatim transcript. Each clinician makes diagnostic and differential diagnostic choices. Downstream Diagnostic Accuracy = agreement between conditions. Primary metric: κ between AVT condition and direct observation condition. Secondary metric: discrepancies stratified by clinical complexity.
```

**Limitations**

> Very expensive — requires multiple blinded clinicians per case, clinical reasoning time, and careful study design. Inter-clinician variation in diagnostic reasoning adds noise. Simulated decision-making may not reflect real-world behaviour under time pressure.

**Novel Thinking / Implications**

> 💡 This is the metric that answers the question "does AVT preserve the clinical signal?" If clinicians reading AVT-generated notes make different diagnostic decisions than clinicians who observed the original consultation, all the proximal metrics (WER, edit rate, documentation time) are at best partially informative and at worst misleading. The Coiera critique is that the field has been measuring proxies and assuming they correlate with this — without evidence. This metric is the evidence.

---

### 🔵 Medication Error Rate Differential

Pre/post AVT comparison of medication errors at the practice or trust level, including wrong-drug, wrong-dose, wrong-frequency, allergy-related, and interaction-related errors. The ultimate distal outcome that medication documentation accuracy ultimately serves. If AVT improves medication documentation (per attribute-level metrics) but medication errors don't decrease, the documentation improvement is not reaching the patient.

|Dimension              |Value                                                                |
|-----------------------|---------------------------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                                       |
|**Measurement Cadence**|Periodic audit                                                       |
|**Pipeline Layer**     |End-to-End                                                           |
|**Assurance Question** |Safety                                                               |
|**Measurement Method** |Hybrid                                                               |
|**Lifecycle Phases**   |Day Zero Baseline, Periodic Audit                                    |
|**Responsible Actors** |National Body, Academic                                              |
|**Maturity**           |Proposed / Novel                                                     |
|**Outcome Type**       |Distal                                                               |
|**Source**             |Coiera critique; patient safety outcome literature; LFPSE medication categories|

**Why this tier?**

> Longitudinal outcome metric requiring substantial baseline period and statistical controls. Not routinely measurable at single-practice level. National or regional evaluation responsibility.

**Formal Definition**

```
Medication Error Rate = |medication_errors_reported| / |total_prescriptions|, stratified by error type and severity. Differential = (rate_post_AVT - rate_pre_AVT) / rate_pre_AVT. Requires: (1) minimum 12-month pre-AVT baseline; (2) consistent reporting culture across periods; (3) adjustment for concurrent interventions. Use difference-in-differences against matched non-AVT controls where possible.
```

**Limitations**

> Medication errors are under-reported; reporting rates vary with safety culture; attribution to AVT requires careful controls. Low baseline rates mean large populations needed for statistical power.

**Novel Thinking / Implications**

> 💡 This closes the loop between AVT documentation accuracy and patient safety outcomes. The implicit theory of change for AVT safety is: better documentation → fewer medication errors → safer patients. Each link in that chain is assumed but not measured. This metric tests the final link directly. If it shows no effect, the proximal metrics need re-examination; if it shows effect, the proximal metrics are validated as meaningful safety signals.

## Fairness & Equity

*Population-level justice: demographic performance, deployment equity, domain coverage.*

**Tier breakdown**: 🟡 2 Tier 2 · 🔵 3 Tier 3

### 🟡 Deployment Equity Index

Whether AVT creates two-tier documentation quality across practices. Track against deprivation indices.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Regional (ICB), National Body |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | NHSE LLM framework wider impact |

**Why this tier?**

> Regional (ICB) monitoring. Track AVT deployment against deprivation indices. Commissioning equity question. Requires cross-organisational data.

**Formal Definition**

```
Correlation r(AVT_deployed, IMD_decile). Positive correlation = deployment inequity. Target: access independent of deprivation (r ≈ 0).
```

**Limitations**

> Requires cross-organisational data.

**Novel Thinking / Implications**

> 💡 If adoption correlates with affluence, technology amplifies inequalities.

---

### 🟡 Accent Taxonomy Standardisation

Meta-metric assessing whether demographic-disaggregated WER uses a sociolinguistically informed accent taxonomy appropriate for NHS populations, rather than ad-hoc or inappropriate categorisations. The FAccT 2024 critique of ASR accent categorisation highlighted that race-based, geography-based, and native/non-native categories are systematically flawed proxies for the actual acoustic variation that affects ASR performance. For NHS deployment, a meaningful taxonomy must cover British regional accents, South Asian English varieties, West African English, Caribbean English, Eastern European English, and other varieties representative of NHS patient populations.

|Dimension              |Value                                                         |
|-----------------------|--------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                        |
|**Measurement Cadence**|One-off gate                                                  |
|**Pipeline Layer**     |ASR / Transcription                                           |
|**Assurance Question** |Fairness & Equity                                             |
|**Measurement Method** |Human Review                                                  |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                |
|**Responsible Actors** |Vendor, National Body                                         |
|**Maturity**           |Proposed / Novel                                              |
|**Outcome Type**       |Proximal                                                      |
|**Source**             |FAccT 2024 critique of ASR accent categorisation; sociolinguistics literature|

**Why this tier?**

> Prerequisite for meaningful fairness assessment. Without a defensible taxonomy, Demographic-Disaggregated WER numbers are not comparable across vendors and may hide rather than reveal bias.

**Formal Definition**

```
Assessment against criteria: (1) Sociolinguistic validity — categories correspond to identifiable phonological communities, not political or racial groupings; (2) NHS relevance — categories include varieties actually present in NHS patient populations; (3) Sample adequacy — each category has sufficient evaluation data for stable WER estimation; (4) Documentation — categorisation methodology is transparent and replicable. Binary pass/fail per criterion; composite = all four must pass.
```

**Limitations**

> Sociolinguistic categorisation is itself contested. Any taxonomy makes choices that can be critiqued. The alternative — no categorisation — is worse because it hides all disparities.

**Novel Thinking / Implications**

> 💡 The hardest form of bias to fix is bias that cannot be measured, and ad-hoc accent categorisation produces unmeasurable bias. An NHS-specific accent taxonomy is infrastructure that would benefit every deployed AVT system — a national body responsibility that would pay for itself quickly. Without it, every vendor's Demographic-Disaggregated WER is self-reported against self-chosen categories, and independent verification is impossible.

### 🟡 Clinical Domain Performance Variance

Accuracy variation across specialties and complexity. Compound boundary risk: degradation multiplies across dimensions.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Compound boundary risk model |

**Why this tier?**

> Vendor should test across clinical domains. Deployers extending beyond primary care should request domain-specific performance data.

**Formal Definition**

```
Accuracy A(d) per clinical domain d. PV = Var(A(d)). Compound risk: performance in untested (domain, population, setting) degrades as product of boundary crossings.
```

**Limitations**

> All-domain testing impractical. Risk-based prioritisation needed.

**Novel Thinking / Implications**

> 💡 System tested in adult primary care urban England ≠ safe for paediatric ENT rural Wales.

---

### 🔵 Intersectional Performance

Accuracy at the intersection of demographic dimensions (e.g. elderly EAL women). Single-axis disaggregation misses compound disadvantage — a system may perform adequately on each dimension separately but fail badly at intersections.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor, National Body |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Intersectionality literature applied to AI fairness |

**Why this tier?**

> Important fairness dimension but requires large demographic-linked datasets and careful statistical analysis.

**Formal Definition**

```
For each intersection of demographic categories (age x ethnicity x language x gender x deprivation): compute accuracy if sample size permits. Identify worst-performing intersections. Compare with single-axis metrics to detect compound disadvantage.
```

**Limitations**

> Sample sizes at intersections may be too small for reliable measurement. Requires substantial demographic-linked evaluation data.

**Novel Thinking / Implications**

> 💡 An elderly, EAL, female patient with limited health literacy may be at the worst-case intersection for AVT accuracy — yet single-axis metrics for elderly, EAL, female, and low-literacy patients may all look acceptable individually. Intersectional analysis reveals this compound disadvantage. Required by population health equity but rarely measured.

---

### 🔵 Intersectional Compound Fairness Score

Extension of the existing Intersectional Performance metric using the FAIR-MED Compound Fairness Score methodology. Where Intersectional Performance measures accuracy at each demographic intersection, Compound Fairness Score calculates whether disadvantage compounds multiplicatively or additively — that is, whether the intersection performs worse than would be predicted by adding the individual demographic disadvantages.

|Dimension              |Value                                                                                |
|-----------------------|-------------------------------------------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                                                       |
|**Measurement Cadence**|Periodic audit                                                                       |
|**Pipeline Layer**     |Cross-cutting                                                                        |
|**Assurance Question** |Fairness & Equity                                                                    |
|**Measurement Method** |Computational                                                                        |
|**Lifecycle Phases**   |Periodic Audit                                                                       |
|**Responsible Actors** |Vendor, National Body, Academic                                                      |
|**Maturity**           |Emerging                                                                             |
|**Outcome Type**       |Distal                                                                               |
|**Source**             |FAIR-MED: Bias Detection and Fairness Evaluation in Healthcare Focused XAI (Springer 2025)|

**Why this tier?**

> Research-grade methodology requiring substantial demographic-linked data. National evaluation or vendor pre-deployment. Complements rather than replaces single-axis fairness metrics.

**Formal Definition**

```
For demographic axes A₁, A₂, ..., Aₙ with performance gaps gap(Aᵢ): expected intersection gap under additive model = Σ gap(Aᵢ); actual intersection gap = observed gap at intersection ∩Aᵢ. Compound Fairness Score CFS = actual_gap / expected_additive_gap. CFS > 1 indicates multiplicative compounding (intersection is worse than sum of parts); CFS ≈ 1 indicates additive; CFS < 1 indicates sub-additive. Multiplicative compounding is the warning signal for worst-case population failures.
```

**Limitations**

> Requires large enough samples at every demographic intersection for stable estimation — often infeasible for rare intersections. Additive model assumption may not hold even in fair systems. Interpretation is statistical rather than mechanistic.

**Novel Thinking / Implications**

> 💡 Single-axis fairness can miss compound disadvantage entirely. A system that performs acceptably on "elderly", "EAL", "female", and "low literacy" as separate categories may perform catastrophically on the intersection. The compound fairness score tests whether this is happening and quantifies how bad it is. For NHS populations where intersectional disadvantage is the rule rather than the exception, single-axis metrics alone are insufficient.

### 🔵 Rare Presentation Handling

Accuracy on uncommon clinical presentations vs common ones. Long-tail performance matters disproportionately for diagnostic safety — the rare presentation that's missed is the most dangerous one to miss.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Long-tail performance analysis from machine learning literature |

**Why this tier?**

> Important but requires evaluation data spanning the long tail of clinical presentations.

**Formal Definition**

```
Stratify test data by presentation frequency. Compute accuracy for: common (top 10% of presentations), moderate (10-50%), rare (50-95%), very rare (bottom 5%). Long-tail Performance Ratio = accuracy_rare / accuracy_common.
```

**Limitations**

> Requires large evaluation dataset with rare presentations. Sample sizes for very rare conditions may be too small for reliable measurement.

**Novel Thinking / Implications**

> 💡 AVT systems trained on common presentations will perform best on common presentations and worst on rare ones. But rare presentations are exactly where clinical decision support matters most — the unusual case that benefits from accurate documentation. Long-tail performance should be a procurement question, not just average performance.

---

### 🔵 Health Literacy Performance Variation

Does AVT performance vary with patient health literacy level? Medically sophisticated patients use clinical terminology that ASR handles well; patients describing symptoms in lay terms may be harder to transcribe and summarise accurately.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Health literacy and equity research |

**Why this tier?**

> Important equity dimension but conceptually and methodologically novel.

**Formal Definition**

```
Compare accuracy on: (1) patients using clinical terminology; (2) patients using lay terms for the same conditions. Performance Gap = accuracy_clinical_terms - accuracy_lay_terms. Significant gap indicates the system rewards health literacy — an equity concern.
```

**Limitations**

> Health literacy is hard to measure. Distinguishing 'lay terms' from 'clinical terms' is not always clean.

**Novel Thinking / Implications**

> 💡 If AVT performs better when patients use clinical language, the system rewards health literacy and disadvantages patients who describe symptoms in everyday terms. This compounds existing health inequalities — the patients who already face barriers to healthcare get less accurate documentation as well. This is an equity dimension that single-axis demographic metrics miss.

---

---

### 🔵 Cross-Platform Fairness Consistency

Whether fairness properties are consistent across multiple AVT platforms deployed within the same ICB or trust. Differential bias between vendors is itself an equity concern — if Practice A uses Vendor X (which performs well on majority populations but poorly on minority populations) and Practice B uses Vendor Y (with the opposite bias profile), patients experience different quality of documentation depending on which practice happens to serve them.

|Dimension              |Value                                                              |
|-----------------------|-------------------------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                                     |
|**Measurement Cadence**|Periodic audit                                                     |
|**Pipeline Layer**     |Cross-cutting                                                      |
|**Assurance Question** |Fairness & Equity                                                  |
|**Measurement Method** |Computational                                                      |
|**Lifecycle Phases**   |Periodic Audit                                                     |
|**Responsible Actors** |Regional (ICB), National Body                                      |
|**Maturity**           |Proposed / Novel                                                   |
|**Outcome Type**       |Distal                                                             |
|**Source**             |Extension of existing Cross-Practice Variance Coefficient into equity dimension|

**Why this tier?**

> Regional or national metric. Requires cross-vendor evaluation on equivalent test data. Only meaningful where multiple platforms are deployed across an integrated care system.

**Formal Definition**

```
For each vendor v in the ICB's deployed platforms: compute demographic-disaggregated performance profile P_v. Cross-Platform Fairness Consistency = variance of P_v across vendors for each demographic group. High variance = patients experience differential fairness depending on which practice (and which vendor) they attend. Report per demographic group; worst-case group determines the equity-consistency floor for the ICB.
```

**Limitations**

> Requires standardised test data available for use against multiple vendors — which currently doesn't exist for NHS. Vendors may resist independent cross-comparison. Aggregation across practices raises information governance questions.

**Novel Thinking / Implications**

> 💡 The current NHS AVT landscape allows ICBs to have multiple vendors deployed across their patch. If those vendors have different fairness profiles, the ICB is effectively running an uncontrolled experiment where patient outcomes depend on which GP they happened to register with. This is invisible to single-vendor fairness metrics and can only be detected by cross-platform comparison. Commissioning should consider fairness consistency as a portfolio-level property, not just a single-vendor property.

# Part E — System Governance

## Safety & Governance

*Cross-cutting safety monitoring, model tracking, incident reporting, and governance infrastructure.*

**Tier breakdown**: 🟢 6 Tier 1 · 🟡 5 Tier 2 · 🔵 2 Tier 3

### 🟢 Model Version Tracking

Logging which model version produces each output. Foundation for all continuous metrics — without it, performance changes are uninterpretable.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Keyes et al., Stanford, Dec 2025 |

**Why this tier?**

> Foundation for all continuous assurance. Without knowing which model version produced which output, no performance change is interpretable. Must be contractually required.

**Formal Definition**

```
Per inference: log model_id, model_version, timestamp, config_hash. On change (v_old → v_new), monitoring window W with duration Δt calibrated for statistical power ≥0.8.
```

**References**

- **Stanford**: [Keyes et al. (2025)](https://arxiv.org/abs/2512.09048)

**Limitations**

> Not contractually mandated in most NHS procurement.

**Novel Thinking / Implications**

> 💡 Three-layer surveillance: detected nationally (contractual), evaluated regionally (benchmark), monitored locally (edit-pattern shift).

---

### 🟡 Model Update Impact Score

Standardised before/after on update. Governance: vendor notifies → regional benchmark → local monitoring.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Regional (ICB) |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | NAS + Stanford frameworks |

**Why this tier?**

> Triggered by model version changes. Requires vendor notification and deployer/regional benchmark suite. The three-layer surveillance model depends on this.

**Formal Definition**

```
Impact IS = Σ w_m × (metric_new - metric_old) / metric_old. Mandatory re-evaluation if IS < -0.05 on any safety metric.
```

**References**

- **NAS**: Three-layer surveillance
- **Stanford**: [Keyes et al. (2025)](https://arxiv.org/abs/2512.09048)

**Limitations**

> Requires vendor notification + deployer benchmark capacity.

**Novel Thinking / Implications**

> 💡 Benchmark suite should be nationally standardised for cross-site comparison.

---

### Longitudinal Drift & Model Contamination sub-cluster

*Addresses the temporal dimension of model assurance that the current taxonomy handles only partially. Where the existing Model Version Tracking and Model Update Impact Score metrics cover notified changes, these metrics cover silent drift, contamination of future training pipelines by AI-generated content, and the regulatory frameworks (FDA PCCP, NICE ESF 2022 AI updates) that increasingly require pre-specified change control plans.*

---

### 🟡 Performance Degradation Detection Latency

Time delay between the onset of model performance degradation and its detection by the monitoring infrastructure. Distinct from the existing Model Update Impact Score, which measures the effect of notified updates at a known switchover point. This metric addresses silent degradation — performance decay that occurs without any vendor notification or identifiable event, from causes including data drift, infrastructure changes, or subtle model updates that are not disclosed.

|Dimension              |Value                                                              |
|-----------------------|-------------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                             |
|**Measurement Cadence**|Continuous                                                         |
|**Pipeline Layer**     |Cross-cutting                                                      |
|**Assurance Question** |Safety                                                             |
|**Measurement Method** |Computational                                                      |
|**Lifecycle Phases**   |Continuous                                                         |
|**Responsible Actors** |Regional (ICB), National Body                                      |
|**Maturity**           |Proposed / Novel                                                   |
|**Outcome Type**       |Proximal                                                           |
|**Source**             |NICE Evidence Standards Framework 2022 AI-specific updates; drift detection literature|

**Why this tier?**

> Regional or national monitoring because detection requires aggregation across sites — single-practice data lacks statistical power to distinguish drift from noise. The detection infrastructure is the binding constraint; the metric itself is straightforward once infrastructure exists.

**Formal Definition**

```
Detection Latency = t_detection - t_degradation_onset. Requires: (1) continuous measurement of sentinel metrics against a stable reference; (2) statistical drift detection (CUSUM, Page-Hinkley, or equivalent sequential testing); (3) pre-specified threshold for declaring drift. Report Latency distribution across detected drift events. Target: detection within 4 weeks of onset for clinically significant degradation.
```

**Limitations**

> Requires stable reference benchmarks that don't drift with the model. Small drift signals are hidden by consultation case-mix variation. Attribution of detected drift to model changes vs environmental changes is often ambiguous.

**Novel Thinking / Implications**

> 💡 Silent degradation is the failure mode that notified update monitoring cannot catch. A vendor pushing incremental improvements, a cloud infrastructure change that affects inference behaviour, or gradual model quality decay from training data drift — none of these trigger Model Version Tracking but all can cause clinically significant performance change. Detection latency is the metric that tells you whether your monitoring would actually catch a silent failure before it caused harm. A system with excellent monitoring coverage but 6-month detection latency is operationally fragile.

---

### 🟡 Retraining Trigger Threshold Specification

Pre-defined, quantitative criteria specifying the conditions under which a model must be retrained or recalibrated. Required by FDA Predetermined Change Control Plans (PCCP, December 2024) for AI-enabled medical devices, and aligned with NICE ESF 2022's AI-specific requirements. Distinct from the existing Model Update Impact Score (which measures impact of executed updates) — this metric assesses whether the trigger logic for when updates should occur is even specified.

|Dimension              |Value                                                             |
|-----------------------|------------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                            |
|**Measurement Cadence**|One-off gate                                                      |
|**Pipeline Layer**     |Cross-cutting                                                     |
|**Assurance Question** |Safety                                                            |
|**Measurement Method** |Human Review                                                      |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                    |
|**Responsible Actors** |Vendor                                                            |
|**Maturity**           |Emerging                                                          |
|**Outcome Type**       |Proximal                                                          |
|**Source**             |FDA PCCP guidance (December 2024); NICE ESF 2022 AI-specific additions|

**Why this tier?**

> Vendor procurement assessment. Should be a Day Zero contractual requirement for any AVT system operating in a regulatory environment that expects PCCP-equivalent change control.

**Formal Definition**

```
Assessment against specification criteria: (1) Performance thresholds pre-specified for retraining triggers (e.g. "if clinically significant WER on sentinel test exceeds 8%, retrain"); (2) Trigger metrics are quantifiable and automatically monitored; (3) Governance process for executing the trigger is documented; (4) Rollback plan exists if retraining degrades rather than improves performance. Binary per criterion; full compliance requires all four.
```

**Limitations**

> Well-specified trigger thresholds can still be wrong. Pre-specification often treats the retraining decision as a simple threshold crossing when in practice it requires judgment. Vendor specification is self-reported unless independently audited.

**Novel Thinking / Implications**

> 💡 The FDA PCCP framework represents a regulatory shift from "approve the specific model" to "approve the change control process that governs model evolution". For AVT, where continuous improvement is assumed, this shift is essential — but only works if the change control process is specified, auditable, and followed. A vendor without a PCCP-equivalent framework is effectively promising that their model will never need updating, or that updating decisions will be made ad hoc. Neither is credible for a production clinical system.

---

### 🔵 AI-Generated Data Contamination Rate

The proportion of training or fine-tuning data that is itself AI-generated clinical content — either directly (notes written by earlier versions of the same AVT system used to train successors) or indirectly (clinical records that have been shaped by AI suggestions even where the final text was human-edited). Known in the machine learning literature as "model autophagy disorder" or "MAD". A medRxiv 2026 study of iterative training on AI-generated clinical content reported vocabulary collapse of 98.9% by generation 4 and effective disappearance of rare clinical findings.

|Dimension              |Value                                                                                            |
|-----------------------|-------------------------------------------------------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                                                                   |
|**Measurement Cadence**|Periodic audit                                                                                   |
|**Pipeline Layer**     |Cross-cutting                                                                                    |
|**Assurance Question** |Safety                                                                                           |
|**Measurement Method** |Human Review                                                                                     |
|**Lifecycle Phases**   |Periodic Audit                                                                                   |
|**Responsible Actors** |Vendor, National Body                                                                            |
|**Maturity**           |Emerging                                                                                         |
|**Outcome Type**       |Distal                                                                                           |
|**Source**             |medRxiv 2026 model autophagy study; Shumailov et al. curse of recursion literature             |

**Why this tier?**

> Systemic risk affecting the entire AVT ecosystem. Cannot be measured by any individual deployer. National body responsibility — and specifically a question that the NHS should pose to any vendor who fine-tunes on deployed clinical data.

**Formal Definition**

```
Contamination Rate = |training_examples_derived_from_AI_generated_content| / |total_training_examples|. Direct contamination: training data includes AI-generated clinical notes. Indirect contamination: training data includes human-approved notes that were initially AI-drafted (where the AI fingerprint remains). Assessment methodology: (1) vendor attestation of training data provenance; (2) statistical detection of AI fingerprints in training corpora; (3) vocabulary drift analysis comparing successive model generations on stable held-out test sets.
```

**Limitations**

> Detecting AI-generated content in training data is an unsolved problem — watermarking proposals are not yet standardised. Vendor attestation is self-reported. Longitudinal monitoring requires visibility into vendor training pipelines that is rarely contractually granted.

**Novel Thinking / Implications**

> 💡 Every NHS trust deploying AVT is a data generation site. If vendors fine-tune on deployed clinical data (a common practice for improvement), NHS content flows back into the training pipeline. Over multiple training cycles, this creates a feedback loop where the model is increasingly trained on its own output — the vocabulary collapse and rare-event disappearance finding becomes a direct patient safety risk because rare clinical presentations are exactly where documentation accuracy matters most. This is the AVT-specific version of what the ML literature calls "the curse of recursion", and it's a systemic risk that requires national-level intervention rather than deployer-level monitoring.

---

### 🔵 Concept Drift in Clinical Notes

Statistical detection of drift in the distribution of clinical concepts present in AI-generated notes over time. Concept drift can occur for legitimate reasons (true population shifts, new conditions, changed coding practice) or problematic reasons (model degradation, training data contamination, prompt drift). The metric doesn't distinguish legitimate from problematic — that requires human judgment — but it makes drift visible so it can be investigated.

|Dimension              |Value                                                    |
|-----------------------|----------------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                            |
|**Measurement Cadence**|Continuous                                                |
|**Pipeline Layer**     |Cross-cutting                                             |
|**Assurance Question** |Meta-evaluation                                           |
|**Measurement Method** |Computational                                             |
|**Lifecycle Phases**   |Continuous                                                |
|**Responsible Actors** |Regional (ICB), National Body, Academic                   |
|**Maturity**           |Proposed / Novel                                          |
|**Outcome Type**       |Distal                                                    |
|**Source**             |Concept drift literature from ML monitoring applied to clinical NLG|

**Why this tier?**

> Requires statistical infrastructure and cross-site aggregation for meaningful signal. National or regional responsibility.

**Formal Definition**

```
For each reference time window W_ref and comparison window W_t: compute the distribution of SNOMED concepts (or other structured clinical categories) present in AI-generated notes. Drift = KL divergence or earth mover's distance between distributions. Threshold for investigation: drift > 2σ from historical seasonal variation. Report per concept category — aggregate drift obscures category-specific shifts. Specifically monitor: rare diagnoses, psychosocial content, safety-netting language, safeguarding flags.
```

**Limitations**

> Distinguishing concept drift from case-mix drift requires population-level context. Seasonal variation (respiratory conditions in winter, mental health referrals in January) creates baseline noise. Rare concepts have high variance even without true drift.

**Novel Thinking / Implications**

> 💡 The most worrying drift signal is concepts that progressively disappear — safeguarding language, mental health content, social context — because the disappearance may indicate the model has learned to deprioritise these categories over time through training data feedback loops. If an AVT system in year 3 documents less psychosocial content than the same system in year 1 despite similar patient populations, something has shifted in what the system considers "clinical content worth recording". This is exactly the kind of drift that aggregate performance metrics cannot detect.

### 🔵 Probabilistic Risk Quantification (P₁/P₂)

Medical device safety paradigm for LLMs. First quantitative risk analysis: P₁ from 2.0×10⁻⁸ to 2.6×10⁻⁴.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Source** | medRxiv, Nov 2025 |

**Why this tier?**

> Research methodology. First published PRA for LLM-SaMD. Important for DCB0129 maturity but requires clinical harm pathway modelling that doesn't yet exist for AVT.

**Formal Definition**

```
P₁ = P(hazardous output | normal use). P₂ = P(harm | hazardous output). Risk R = P₁ × P₂ × Severity. P₂ requires clinical harm pathway modelling with probability attenuation at each stage.
```

**References**

- **Preprint**: medRxiv, Nov 2025 — 14 open-source LLMs

**Limitations**

> Validated on open-source only. Commercial AVT = black box.

**Novel Thinking / Implications**

> 💡 For DCB0129: translating error rates into P₁/P₂ makes safety cases quantitative, not just qualitative.

---

### 🔵 DeepScore (Defect-Free Rate)

Two-tier: Major Defect-Free Rate + Critical Defect-Free Rate. 135,900 notes. Sound approach but proprietary definitions.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Vendor-Proprietary |
| **Outcome Type** | Proximal |
| **Source** | DeepScribe |

**Why this tier?**

> Vendor-proprietary (DeepScribe). Sound two-tier severity approach but proprietary definitions prevent cross-vendor comparison.

**Formal Definition**

```
MDFR = |N_no_major| / |N_total|. CDFR = |N_no_critical| / |N_total|. Vendor-specific severity definitions — not aligned to external standard.
```

**References**

- **DeepScore**: DeepScribe, arXiv Sept 2024

**Limitations**

> Proprietary severity definitions. Human QA in enterprise tier conflates AI + human performance.

**Novel Thinking / Implications**

> 💡 CREOLA taxonomy is best candidate for common severity framework.

---

### 🟢 Safety Performance Indicators with Thresholds (DSCMS)

Metrics + thresholds + escalation = governance. A metric without a threshold is information; with a threshold and action it becomes governance.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer, Regional (ICB) |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | DSCMS methodology in NAS framework |

**Why this tier?**

> The governance mechanism that converts metrics into action. Without pre-defined thresholds and escalation paths, metrics are information without teeth. Every Tier 1 metric needs an SPI wrapper.

**Formal Definition**

```
For SPI s: measurement M(s), threshold T(s), action A(s). If M(s) > T(s) for duration d → trigger A(s). Tiered: Review / Pause / Suspend.
```

**References**

- **DSCMS**: Dynamic Safety Case Management System

**Limitations**

> Threshold-setting is judgemental.

**Novel Thinking / Implications**

> 💡 Every metric here should be assessable for SPI candidacy.

---

### 🟡 Off-Label Use Detection Rate

AVT use outside validated contexts. Well-intentioned scope creep — each boundary crossing compounds risk.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Compound boundary risk model; NHSE LLM framework |

**Why this tier?**

> Deployer monitoring. Technically feasible if the validated use envelope is machine-readable. Detects well-intentioned scope creep that compounds boundary risk.

**Formal Definition**

```
Validated envelope V = set of (domain, type, population, setting) tuples. Boundary distance BD(e) = dimensions where encounter e falls outside V. OLR = |{e: BD>0}| / |E_total|. BD > 2 → immediate CSO review.
```

**References**

- **Compound risk**: Compound boundary risk model

**Limitations**

> Requires clear validated envelope definition.

**⚠️ Underspecification Warning (Tier A — no established methodology)**

> Off-label use of AVT has **no established detection methodology** in the published literature. The concept borrows from pharmaceutical regulation, but AVT "indicated use" boundaries are rarely defined precisely enough to determine when specific use is off-label. A 2025 Morgan Lewis legal analysis highlighted the liability risk but provided no detection framework. No use-case taxonomy exists to define intended vs off-label boundaries. No monitoring approach has been proposed in peer-reviewed literature. This metric requires definitional work before operational implementation is possible: deployers should, in collaboration with vendors, specify the validated use envelope (specialties, patient populations, acuity levels, languages, consultation modes) and build usage-pattern monitoring against that envelope rather than attempting to measure "off-label use" as an isolated concept. Consider operationalising as the proposed **Work-as-Imagined vs Work-as-Done Gap** metric (Human Factors & Workflow) which provides a more structured framework for detecting adaptation, workaround, and scope creep.

**Novel Thinking / Implications**

> 💡 Automated detection feasible if validated envelope is machine-readable.

---

### 🟢 Adverse Event / Incident Rate (LFPSE)

National patient safety reporting. Ultimate lagging indicator. No specific LFPSE category for AI/AVT incidents exists.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer, National Body |
| **Maturity** | Established |
| **Outcome Type** | Distal |
| **Source** | LFPSE national reporting |

**Why this tier?**

> Established national reporting. The ultimate lagging indicator — by the time this metric moves, harm has occurred. Needs dedicated LFPSE category for AI/AVT incidents.

**Formal Definition**

```
IR = N_incidents / N_encounters. Stratify by severity. Currently no LFPSE taxonomy code for AI/AVT — coded under general documentation errors.
```

**References**

- **LFPSE**: NHS Learn From Patient Safety Events

**Limitations**

> Massive under-reporting. No specific AI/AVT category. Unknown denominator.

**Novel Thinking / Implications**

> 💡 Dedicated LFPSE reporting category needed for this to function as national signal.

---

### 🟡 Cross-Practice Variance Coefficient

Performance variation across practices within ICB. High variance = context-dependent performance. Justifies regional assurance tier.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Regional (ICB) |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Multi-level assurance framework |

**Why this tier?**

> Regional (ICB) metric. Justifies the regional assurance tier. Requires standardised metrics collection across practices.

**Formal Definition**

```
CV_m = σ(m across practices) / μ(m). High CV (>0.3) = context-dependent. ANOVA to identify drivers: practice size, demographics, template, clinician experience.
```

**Limitations**

> Requires standardised collection across practices.

**Novel Thinking / Implications**

> 💡 Same AVT, different quality = contextual difference. That's deployer responsibility, not vendor's.

---

### 🟢 Assurance Debt Accumulation Rate

Gap between required and completed assurance. The honest metric — better visible and managed than hidden until incident.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer, Regional (ICB) |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Multi-level assurance framework |

**Why this tier?**

> The honest governance metric. Every deployer will accumulate it. Making it visible, tracked, and managed prevents governance theatre.

**Formal Definition**

```
AD(t) = |A_due(t)| - |A_completed(t)|. Decompose: clinical audit, SPI review, training refresh, patient feedback, model update check.
```

**Limitations**

> Requires defined schedule. Risk of checkbox compliance.

**Novel Thinking / Implications**

> 💡 '3 overdue audits and 2 unresolved SPI breaches' is more useful than 'everything is fine.'

---

### 🟢 Near-Miss Reporting Rate

Incidents caught by clinician review before reaching the EPR. The leading indicator that LFPSE rate is the lagging indicator of. A high near-miss rate with low LFPSE rate suggests the human review layer is functioning; a low near-miss rate may indicate either an excellent system or inadequate review.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Patient safety leading vs lagging indicator literature |

**Why this tier?**

> Essential leading indicator. Should be Tier 1 because it's the early warning system that LFPSE is the lagging indicator of. Requires lightweight reporting infrastructure.

**Formal Definition**

```
Near-Miss Rate = |errors_caught_in_review| / |total_AI_outputs|. Track separately from LFPSE incidents (errors that reached the record). Healthy ratio: high near-miss rate, low LFPSE rate. Concerning ratio: low near-miss rate, any LFPSE incidents.
```

**Limitations**

> Requires clinicians to actively report near-misses, which is often under-reported in busy clinical practice.

**Novel Thinking / Implications**

> 💡 The leading indicator: by the time LFPSE moves, harm has occurred. Near-miss reporting catches errors before they cause harm — but only if there's a low-friction reporting mechanism and a no-blame culture. The ratio of near-miss to actual incidents is itself diagnostic of safety culture.

---

### 🟡 Time-to-Correct

When an AVT error is detected, how quickly is it corrected and the lessons disseminated? Measures the responsiveness of the governance loop from detection to action.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Standard incident response metric applied to AVT |

**Why this tier?**

> Important operational governance metric. Requires structured incident tracking.

**Formal Definition**

```
Time-to-Correct = t_correction_implemented - t_error_detected. Track per error severity. Critical errors: target < 24 hours. Major errors: target < 1 week. Includes: error correction in record, communication to other clinicians, model/template adjustment if applicable.
```

**Limitations**

> Requires structured incident tracking. 'Correction' may have multiple stages with different completion times.

**Novel Thinking / Implications**

> 💡 A long time-to-correct means errors persist in the system and may affect multiple patients before resolution. This is operationally important — a single error is bad, but a single error that took 3 weeks to correct is a governance failure.

---

### 🟡 SPI Escalation Response Time

When an SPI threshold is breached, how quickly does the governance response actually occur? Measures whether the SPI framework is operationally functional or just a paper exercise.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer, Regional (ICB) |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Operational extension of DSCMS SPI framework |

**Why this tier?**

> Important governance functionality test. Requires SPI monitoring infrastructure to be in place.

**Formal Definition**

```
Escalation Response Time = t_governance_action - t_SPI_breach. Track per escalation level (review trigger, pause trigger). Target: review actions within 48 hours, pause actions within 4 hours. Note: pause should be automatic, not requiring human action.
```

**Limitations**

> Requires automated SPI monitoring and structured escalation tracking. Most current implementations are manual.

**Novel Thinking / Implications**

> 💡 An SPI framework that takes a week to respond to a breach is not protecting anyone. The whole point of pre-defined thresholds with escalation paths is to enable rapid response. Measuring response time reveals whether the framework is operationally functional or governance theatre.

---

### 🟢 Hazard Log Completeness

DCB0129 requires a hazard log. Is it actually maintained and updated as new failure modes are discovered operationally? A static hazard log written at deployment and never updated is a compliance failure with safety implications.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | DCB0129 compliance requirement |

**Why this tier?**

> Regulatory requirement under DCB0129. Tier 1 because it's a compliance obligation, not a recommendation. Should be linked to operational monitoring.

**Formal Definition**

```
Hazard Log Currency = (date_of_last_update - today) in days. Hazard Coverage = |operationally_observed_failure_modes_in_log| / |total_observed_failure_modes|. Currency target: updated within 30 days of any new failure mode discovery.
```

**References**

- **DCB0129**: DCB0129 hazard log requirement

**Limitations**

> Requires connecting operational monitoring to hazard log update process — often disconnected in current practice.

**Novel Thinking / Implications**

> 💡 DCB0129 hazard logs are often written once at deployment and forgotten. As operational monitoring discovers new failure modes (through edit pattern analysis, near-miss reporting, incident investigation), these should be added to the hazard log with mitigations. A hazard log that hasn't been updated in 6 months is either a perfect system or a compliance failure — and almost certainly the latter.

---

# Part E — System Governance

## NHS Compliance & Regulatory

*Process compliance metrics against defined external requirements, distinct from the safety performance metrics in the Safety & Governance group. Most entries here are binary or near-binary — the deployer is compliant or they are not — and most Tier 1 assignments reflect legal or guidance requirements that cannot be responsibly skipped regardless of clinical performance.*

*The group was added to the taxonomy in response to the January–March 2026 NHS guidance suite: NHSE IG guidance on ambient scribing (March 2026), the NHSE AVT Supplier Registry (launched January 2026), and CIO/CCIO guidance v2 (January 2026). Taken together these documents defined a discrete compliance surface that is operationally distinct from clinical safety governance and that deserves its own cluster rather than being scattered across Safety & Governance and Privacy & Data Governance.*

*The group also contains two international regulatory metrics (FDA PCCP-Equivalent Pre-Defined Acceptance Criteria, EU AI Act Event Logging Compliance) because vendor compliance cascades across jurisdictions — an AVT vendor with EU market exposure will typically apply EU AI Act requirements uniformly across their product rather than maintaining jurisdiction-specific variants, which means UK deployments inherit EU requirements through vendor compliance regardless of whether they would otherwise apply.*

*Legal and statutory privacy metrics that pre-date the 2026 NHS guidance (Subject Access Request Fulfilment, Right to Erasure, Cross-Border Data Transfer Compliance, Sub-Processor Transparency) remain in the Privacy & Data Governance group to preserve the legal-basis cluster there. The split between "privacy legal requirements" and "NHS compliance process requirements" is analytical rather than hierarchical — a deployer is obliged to meet both, and neither group has precedence over the other.*

**Tier breakdown**: 🟢 7 Tier 1 · 🟡 3 Tier 2 · 🔵 0 Tier 3

---

### 🟢 Patient Dissent Recording Rate

Per-encounter rate at which patient objections or dissent to AVT use are recorded and respected. Distinct from the existing Patient Opt-Out Rate, which is aggregate and applies at the registration or consent level. Patient Dissent Recording is the per-encounter process compliance metric: when a patient objects at the point of care, is that objection documented, is AVT actually paused for that encounter, and is the objection respected in subsequent encounters without re-litigation.

|Dimension              |Value                                                  |
|-----------------------|--------------------------------------------------------|
|**Priority Tier**      |🟢 Tier 1 — Minimum Viable                              |
|**Measurement Cadence**|Continuous                                              |
|**Pipeline Layer**     |Cross-cutting                                           |
|**Assurance Question** |Patient Experience                                      |
|**Measurement Method** |Passive Observational                                   |
|**Lifecycle Phases**   |Continuous                                              |
|**Responsible Actors** |Deployer                                                |
|**Maturity**           |Established                                             |
|**Outcome Type**       |Proximal                                                |
|**Source**             |NHSE IG guidance on ambient scribing (March 2026)       |

**Why this tier?**

> Direct compliance requirement under NHSE IG guidance. Deployer-measurable from workflow records. Binary compliance — a patient dissent not recorded and respected is a regulatory and ethical failure.

**Formal Definition**

```
Recording Rate = |dissent_events_with_recorded_and_respected_objection| / |total_dissent_events|. Target: 100%. Sub-metrics: (a) dissent documentation rate (was it recorded?); (b) dissent respect rate (was AVT paused?); (c) dissent persistence rate (was it respected in subsequent encounters?). Any sub-metric below 100% indicates compliance failure.
```

**Limitations**

> Detection of dissent events requires clinician reporting or structured capture in the EPR workflow. Silent non-compliance (clinician uses AVT despite patient objection) is invisible to passive observation.

**Novel Thinking / Implications**

> 💡 This is the per-encounter teeth behind the aggregate opt-out metric. Opt-out gives the patient a blanket choice; dissent recording ensures the choice is honoured at each specific consultation where it matters. The two metrics measure different things: opt-out measures consent model acceptance; dissent recording measures procedural integrity at the point of care. Both are necessary for a coherent consent architecture.

---

### 🟢 Verbal Notification Compliance

Proportion of AVT-using consultations where verbal notification was delivered to the patient at session start, as required by NHSE IG guidance (March 2026). Consent model in NHS primary care relies on informing patients before AVT activation, but the "informing" step is often poorly observed in busy practice. This metric measures the actual delivery of notification, not just the existence of a notification policy.

|Dimension              |Value                                                    |
|-----------------------|----------------------------------------------------------|
|**Priority Tier**      |🟢 Tier 1 — Minimum Viable                                |
|**Measurement Cadence**|Periodic audit                                            |
|**Pipeline Layer**     |Cross-cutting                                             |
|**Assurance Question** |Patient Experience                                        |
|**Measurement Method** |Hybrid                                                    |
|**Lifecycle Phases**   |Day Zero Baseline, Periodic Audit                         |
|**Responsible Actors** |Deployer                                                  |
|**Maturity**           |Established                                               |
|**Outcome Type**       |Proximal                                                  |
|**Source**             |NHSE IG guidance on ambient scribing (March 2026); CQC Mythbuster 109 context|

**Why this tier?**

> Direct compliance requirement. Measurable via patient survey sampling, consultation audit, or (with appropriate consent) recording sampling. Binary compliance — notification either happened or it didn't.

**Formal Definition**

```
Compliance Rate = |consultations_with_verbal_notification_delivered| / |total_AVT_consultations|. Measurement methods in order of increasing rigour: (a) clinician self-report at end of session; (b) patient survey sampling asking whether notification was delivered; (c) audit of audio recordings (where retention allows) for notification language. Target: 100%. Values below 95% indicate systematic compliance failure requiring intervention.
```

**Limitations**

> Self-report over-estimates compliance. Patient recall is imperfect. Audio audit is resource-intensive and depends on retention policies that may conflict with data minimisation.

**Novel Thinking / Implications**

> 💡 The gap between policy and practice on patient notification is the compliance equivalent of the consent understanding gap. A practice can have a 100% notification policy and a 60% actual notification rate — and the 40% gap is where the consent model breaks down. Periodic audit is the only way to know which side of the gap a deployer is on. A practice that refuses to audit is implicitly choosing not to know.

---

### 🟢 AI-Generated Content Labelling Compliance

Automated verification that AI-generated clinical record entries carry the mandatory SNOMED suffix identifying them as AVT output (e.g. "Audio Dictation 24771000000105" per NHSE guidance). Required for downstream systems to distinguish AI-generated content from clinician-authored content — essential for audit, safety investigation, and future training data curation.

|Dimension              |Value                                                     |
|-----------------------|-----------------------------------------------------------|
|**Priority Tier**      |🟢 Tier 1 — Minimum Viable                                 |
|**Measurement Cadence**|Continuous                                                 |
|**Pipeline Layer**     |EPR Write-back                                             |
|**Assurance Question** |Meta-evaluation                                            |
|**Measurement Method** |Computational                                              |
|**Lifecycle Phases**   |Pre-deployment, Continuous                                 |
|**Responsible Actors** |Vendor, Deployer                                           |
|**Maturity**           |Established                                                |
|**Outcome Type**       |Proximal                                                   |
|**Source**             |NHSE IG guidance on ambient scribing (March 2026)          |

**Why this tier?**

> Automated compliance check with trivial implementation cost. Should be a pre-deployment gate and continuous monitoring metric. Non-compliance is both a governance failure and a downstream data quality problem.

**Formal Definition**

```
Labelling Rate = |AI_generated_entries_with_correct_suffix| / |total_AI_generated_entries|. Target: 100%. Zero-tolerance — every AI-generated entry must be labelled. Automated verification is feasible because the suffix is a fixed SNOMED concept that either appears or doesn't. Report non-compliance instances for immediate remediation.
```

**Code: Labelling compliance check**

```python
AVT_LABEL_SUFFIX = "24771000000105"  # Audio Dictation SNOMED concept

def check_labelling_compliance(epr_entries):
    """
    Verify every AI-generated entry carries the mandatory suffix.
    """
    ai_entries = [e for e in epr_entries if e.get("source") == "AVT"]
    compliant = [e for e in ai_entries
                 if AVT_LABEL_SUFFIX in e.get("content", "")
                 or e.get("label_code") == AVT_LABEL_SUFFIX]
    non_compliant = [e for e in ai_entries if e not in compliant]
    return {
        "rate": len(compliant) / len(ai_entries) if ai_entries else 1.0,
        "non_compliant_count": len(non_compliant),
        "non_compliant_entries": non_compliant,
        "alert": len(non_compliant) > 0,
        "severity": "CRITICAL" if non_compliant else "OK"
    }
```

**Limitations**

> Assumes the vendor's write-back system supports the suffix — some EPR integrations strip metadata fields that don't map to native EPR structures. The suffix location (free-text vs metadata) affects automated detection methodology.

**Novel Thinking / Implications**

> 💡 Without reliable labelling, every downstream system that consumes clinical records is operating without knowing which content is AI-generated. This matters for: safety investigation (was the error in a human-written or AI-generated entry?); training data curation (if AI-generated records are fed back into training, the labelling is necessary to detect and exclude them); audit trails (which clinicians rely on AI assistance and how frequently). Non-labelling is an infrastructure failure with cascading consequences.

---

### 🟢 AVT Supplier Registry Listing Verification

Procurement and ongoing verification that the deployed AVT system is listed on the NHS England AVT Supplier Registry and remains listed throughout the deployment lifecycle. The Registry (launched January 2026) is the NHS-level mechanism for self-certified minimum standards, and registry status is expected to become a procurement precondition.

|Dimension              |Value                                                 |
|-----------------------|------------------------------------------------------|
|**Priority Tier**      |🟢 Tier 1 — Minimum Viable                             |
|**Measurement Cadence**|Continuous                                            |
|**Pipeline Layer**     |Cross-cutting                                         |
|**Assurance Question** |Safety                                                |
|**Measurement Method** |Human Review                                          |
|**Lifecycle Phases**   |Pre-deployment, Continuous                            |
|**Responsible Actors** |Deployer, Vendor                                      |
|**Maturity**           |Established                                           |
|**Outcome Type**       |Proximal                                              |
|**Source**             |NHSE AVT Supplier Registry (January 2026)             |

**Why this tier?**

> Procurement gate with trivial verification cost. Should be confirmed at procurement and re-verified at contract renewal and on notification of vendor compliance events.

**Formal Definition**

```
Listing Verification: at procurement, confirm vendor is on the live Registry. Quarterly re-verification during deployment. Binary: listed or not listed. Where not listed, deployment should not proceed (pre-deployment) or should trigger formal risk review (during deployment). Also track: date of most recent vendor compliance attestation, scope of attested compliance (which AVT products are covered).
```

**Limitations**

> Registry is self-certified — listing indicates vendor attestation rather than independent verification. Listing scope may not cover all deployed AVT modules from a vendor with multiple products.

**Novel Thinking / Implications**

> 💡 The Registry's value depends on NHS bodies treating listing as a procurement precondition. If deployments proceed with non-listed vendors, the Registry becomes advisory rather than normative and loses its governance function. Making Registry verification a Tier 1 metric supports the norm that listing is expected — and creates visible data on deployment-to-listing alignment that can inform Registry policy over time.

---

### 🟢 ICB Engagement Documentation

Documented evidence that the deployer engaged with their ICB digital team (or equivalent regional body) before AVT deployment, as required by the CIO/CCIO guidance (v2, January 2026). The ICB engagement requirement exists to prevent uncoordinated deployment across an integrated care system and to ensure regional intelligence about AVT risks and mitigations is applied consistently.

|Dimension              |Value                                                       |
|-----------------------|-------------------------------------------------------------|
|**Priority Tier**      |🟢 Tier 1 — Minimum Viable                                   |
|**Measurement Cadence**|One-off gate                                                 |
|**Pipeline Layer**     |Cross-cutting                                                |
|**Assurance Question** |Meta-evaluation                                              |
|**Measurement Method** |Human Review                                                 |
|**Lifecycle Phases**   |Pre-deployment                                               |
|**Responsible Actors** |Deployer, Regional (ICB)                                     |
|**Maturity**           |Established                                                  |
|**Outcome Type**       |Proximal                                                     |
|**Source**             |CIO/CCIO guidance v2 (January 2026); NHS CIO priority notification|

**Why this tier?**

> Pre-deployment compliance requirement. Should be a documented gate before go-live. Failure indicates a governance process breakdown that deserves immediate correction.

**Formal Definition**

```
Engagement documentation includes: (1) formal notification to ICB digital team dated before go-live; (2) ICB response acknowledging notification; (3) any conditions or recommendations from ICB on file. Binary compliance: all three present = compliant. Missing ICB response is a flag for follow-up, not automatic non-compliance, because ICB capacity constraints may prevent timely response.
```

**Limitations**

> ICB engagement quality varies — some ICBs have mature digital teams providing substantive review; others acknowledge notifications without meaningful engagement. Documentation presence does not guarantee engagement quality.

**Novel Thinking / Implications**

> 💡 ICB engagement is the mechanism that prevents NHS AVT deployment from being a series of disconnected practice-level decisions with no regional coordination. It only works if it is actually happening — and practices deploying AVT without ICB engagement are a visible symptom of governance friction, ICB capacity constraints, or deployment urgency overriding process. Tracking the metric is a diagnostic tool for that friction as much as it is a compliance check.

---

### 🟢 Clinical Safety Case Completeness

Existence, currency, and coverage of a formal DCB0129/0160 clinical safety case for the AVT deployment. Distinct from the existing Hazard Log Completeness metric, which covers log currency. Safety Case Completeness is the broader document: hazard identification, risk analysis, mitigations, residual risk acceptance, and governance arrangements. A 2025 FOI-based study (PubMed 41172285) found widespread non-compliance with DCB0129 requirements among NHS digital health deployments.

|Dimension              |Value                                                                                            |
|-----------------------|-------------------------------------------------------------------------------------------------|
|**Priority Tier**      |🟢 Tier 1 — Minimum Viable                                                                        |
|**Measurement Cadence**|Periodic audit                                                                                   |
|**Pipeline Layer**     |Cross-cutting                                                                                    |
|**Assurance Question** |Safety                                                                                           |
|**Measurement Method** |Human Review                                                                                     |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                                                   |
|**Responsible Actors** |Deployer                                                                                         |
|**Maturity**           |Established                                                                                      |
|**Outcome Type**       |Proximal                                                                                         |
|**Source**             |DCB0129/0160 regulatory requirement; PubMed 41172285 FOI study of NHS digital safety standard compliance|

**Why this tier?**

> Direct regulatory requirement. Non-compliance is both a legal and a safety issue. The 2025 FOI study found widespread non-compliance, making this a known high-risk area requiring active monitoring.

**Formal Definition**

```
Completeness assessed against DCB0129 standard sections: (1) safety management system; (2) hazard identification; (3) hazard analysis and evaluation; (4) hazard control; (5) hazard log; (6) safety case report; (7) safety incident management; (8) issue resolution. Each section binary (present and current / missing or out-of-date). Full compliance requires all sections. Currency: major update triggered by significant system change, model version change, or new hazard identification.
```

**Limitations**

> Compliance with structure does not guarantee quality of content. Safety cases are often written to satisfy the standard rather than to genuinely analyse system safety — the "compliance theatre" problem. External independent review is the only reliable check.

**Novel Thinking / Implications**

> 💡 The 2025 FOI finding that many NHS digital health deployments lack DCB0129 compliance is a structural warning about regulatory enforcement gaps. AVT deployment is happening faster than safety case development in many places. Making Safety Case Completeness a Tier 1 metric both highlights the compliance obligation and creates visible data on how widespread the gap is — which is itself a governance intervention.

---

### 🟢 DPIA Template Completion Rate

Proportion of AVT deployments using the NHS-provided March 2026 DPIA template with all mandatory sections completed. Data Protection Impact Assessment is required under UK GDPR Article 35 for high-risk processing, and AVT meets the high-risk threshold. The NHSE template provides standardised structure — but the template only helps if it's actually used and completed.

|Dimension              |Value                                                 |
|-----------------------|------------------------------------------------------|
|**Priority Tier**      |🟢 Tier 1 — Minimum Viable                             |
|**Measurement Cadence**|Periodic audit                                        |
|**Pipeline Layer**     |Cross-cutting                                         |
|**Assurance Question** |Safety                                                |
|**Measurement Method** |Human Review                                          |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                        |
|**Responsible Actors** |Deployer                                              |
|**Maturity**           |Established                                           |
|**Outcome Type**       |Proximal                                              |
|**Source**             |UK GDPR Article 35; NHSE IG guidance template (March 2026)|

**Why this tier?**

> Legal requirement. Pre-deployment gate. Template completion is measurable and binary.

**Formal Definition**

```
Completion Rate = |deployments_with_complete_DPIA_using_template| / |total_AVT_deployments|. Template mandatory sections: processing description, lawful basis, data flows, risks identified, mitigations, residual risk acceptance, DPO sign-off, review schedule. Each section binary; complete DPIA requires all sections. Review cadence: minimum annually or on significant processing change.
```

**Limitations**

> Template compliance doesn't guarantee substantive risk analysis. "Completed" DPIAs that list "no residual risks identified" for a novel AVT deployment are likely inadequate regardless of template adherence.

**Novel Thinking / Implications**

> 💡 The NHSE template provides common structure across deployments, which has three benefits: (1) makes comparison possible across sites, (2) ensures mandatory considerations aren't missed, (3) creates an evidence base for national-level risk analysis. Template non-use isn't necessarily non-compliance with UK GDPR (bespoke DPIAs can be legitimate) but it loses the aggregation benefit. Tracking template use rate is a proxy for how consistently the governance infrastructure is being built.

---

### 🟡 DSPA Status

Existence and currency of Data Sharing/Processing Agreements with all data processors involved in AVT operation. UK GDPR Article 28 requires written agreements with processors, and cloud-hosted AVT typically involves multiple processors (primary vendor, cloud provider, model provider, annotation services). Related to the existing Sub-Processor Transparency metric but specifically focuses on the contractual agreements rather than the disclosure of sub-processors.

|Dimension              |Value                                         |
|-----------------------|----------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                        |
|**Measurement Cadence**|Periodic audit                                |
|**Pipeline Layer**     |Cross-cutting                                 |
|**Assurance Question** |Safety                                        |
|**Measurement Method** |Human Review                                  |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                |
|**Responsible Actors** |Deployer, Vendor                              |
|**Maturity**           |Established                                   |
|**Outcome Type**       |Proximal                                      |
|**Source**             |UK GDPR Article 28; NHS data protection guidance|

**Why this tier?**

> Legal compliance requirement. Annual audit recommended. Slightly lower tier than DPIA because absence of DSPA is more commonly an oversight than a structural governance failure — but still a legal requirement.

**Formal Definition**

```
DSPA Status per processor: (a) agreement in place (binary); (b) agreement currency (signed within last 2 years or since last significant change); (c) agreement covers all processing activities actually performed by that processor; (d) UK GDPR Article 28 mandatory clauses present. Full compliance requires all four per processor. Aggregate metric: |processors_fully_compliant| / |total_processors|.
```

**Limitations**

> Agreement existence doesn't guarantee processor compliance with the agreement. Cross-border processors may have limited enforceability. Complex sub-processor chains make coverage verification difficult.

**Novel Thinking / Implications**

> 💡 DSPAs are where the legal rubber meets the road. A deployer with a DPIA but no DSPAs has documented the risks without contractually binding the processors to manage them. This is a common gap because DPIAs are visible in NHS audit processes while DSPAs are often handled by legal departments outside the IG team's line of sight.

---

### 🟡 FDA PCCP-Equivalent Pre-Defined Acceptance Criteria

Whether the vendor has pre-specified quantitative acceptance criteria that any model update must meet before being deployed to production. FDA Predetermined Change Control Plans (finalised December 2024) require this for US-market medical device AI. Even in UK-only deployments, it matters because: (1) EU-market vendors cascade similar requirements through the EU AI Act, and (2) the existence of pre-defined acceptance criteria is a proxy for mature change control regardless of regulatory jurisdiction.

|Dimension              |Value                                                   |
|-----------------------|---------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                   |
|**Measurement Cadence**|One-off gate                                             |
|**Pipeline Layer**     |Cross-cutting                                            |
|**Assurance Question** |Safety                                                   |
|**Measurement Method** |Human Review                                             |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                           |
|**Responsible Actors** |Vendor                                                   |
|**Maturity**           |Emerging                                                 |
|**Outcome Type**       |Proximal                                                 |
|**Source**             |FDA PCCP guidance (December 2024); EU AI Act Article 15; NICE ESF 2022 AI updates|

**Why this tier?**

> Procurement assessment. Should be standard due diligence for any AVT acquisition. Vendors without PCCP-equivalent frameworks are a higher governance risk.

**Formal Definition**

```
Assessment against criteria: (1) Performance acceptance thresholds pre-specified and quantitative; (2) Regression test suite defined and maintained; (3) Fairness/equity criteria included in acceptance testing; (4) Rollback procedure specified if update fails acceptance post-deployment; (5) Documentation of acceptance decisions available for audit. Binary per criterion; full compliance = all five.
```

**Limitations**

> Vendors may claim PCCP equivalence without independent verification. The substantive quality of acceptance criteria matters more than their existence — a criterion like "WER not more than 20% worse" technically exists but provides no meaningful safety floor.

**Novel Thinking / Implications**

> 💡 PCCP is a structural shift in how AI medical devices are regulated — from approving specific models to approving the change control process. For AVT specifically, this is essential because continuous model improvement is expected, and ad-hoc change control makes every update a regulatory event. NHS procurement should treat PCCP-equivalent frameworks as the baseline expectation, not a differentiator, even though the formal PCCP framework applies to US-market devices.

---

### 🟡 EU AI Act Event Logging Compliance

Compliance with EU AI Act Article 12 automatic event logging requirements for high-risk AI systems. High-risk provisions became effective August 2026. Applies to any AVT vendor with EU market exposure, and cascades into UK deployment because vendors typically apply the strictest applicable regulatory regime uniformly across their product rather than maintaining jurisdiction-specific variants.

|Dimension              |Value                                              |
|-----------------------|----------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                              |
|**Measurement Cadence**|Continuous                                          |
|**Pipeline Layer**     |Cross-cutting                                       |
|**Assurance Question** |Safety                                              |
|**Measurement Method** |Computational                                       |
|**Lifecycle Phases**   |Pre-deployment, Continuous                          |
|**Responsible Actors** |Vendor                                              |
|**Maturity**           |Emerging                                            |
|**Outcome Type**       |Proximal                                            |
|**Source**             |EU AI Act Article 12 (high-risk provisions effective August 2026)|

**Why this tier?**

> Vendor-side regulatory requirement. Deployer should verify event logging infrastructure exists and receive logs for foreseeable-misuse investigation. Important for incident investigation capability.

**Formal Definition**

```
Event logging must capture: (1) period of use (start, duration, stop per session); (2) reference database used; (3) input data that led to output; (4) natural persons involved in verification of output. Logging must be automatic, not opt-in. Retention period specified in vendor policy and aligned with EU AI Act minimums. Deployer verification: can the vendor provide a complete event log for any given encounter on request within a reasonable timeframe?
```

**Limitations**

> Full logging creates large data volumes and storage costs. Logging of input data conflicts with data minimisation principles — resolving this requires careful policy design. Deployer verification is manual and sample-based.

**Novel Thinking / Implications**

> 💡 Event logging is the infrastructure that supports retrospective incident investigation. Without it, when an AVT error causes harm six months after the fact, the investigation has nothing to work with — the clinician may not remember the encounter, the patient certainly won't remember the AI's behaviour, and the vendor has no logs to reconstruct what happened. The EU AI Act requirement is essentially mandating the infrastructure for forensic investigation of AI clinical systems, which is a governance improvement regardless of jurisdiction.

## Security & Adversarial Robustness

*Resistance to intentional manipulation: prompt injection, jailbreaking, adversarial audio, data poisoning, and the architectural defences against them.*

**Tier breakdown**: 🟡 6 Tier 2 · 🔵 3 Tier 3

### 🟡 Prompt Injection Resistance Rate

Resistance to adversarial spoken commands designed to manipulate the summarisation output. A patient or third party speaking phrases like 'ignore previous instructions' or 'add to the note that the patient has no allergies' could alter clinical documentation.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Mindgard/Heidi Health and Doctronic jailbreak disclosures (March 2026); adversarial ML literature |

**Why this tier?**

> Vendor pre-deployment and periodic red-team testing. No standardised clinical prompt injection test suite exists but the Mindgard disclosures make this non-optional.

**Formal Definition**

```
Resistance Rate = 1 - (|successful_injections| / |attempted_injections|). Test suite: spoken prompt injections across categories: (a) instruction override, (b) content insertion, (c) content suppression, (d) format manipulation. Must be tested at ASR level (does the injection survive transcription?) and summarisation level (does it alter output?).
```

**References**

- **Mindgard**: Mindgard/Heidi Health jailbreak disclosure (March 2026)
- **Architecture**: Safety-critical properties must be enforced at architecture level, not prompt level

**Limitations**

> Adversarial attack surfaces evolve continuously. Static test suites become stale. Red-teaming requires ongoing investment. No standardised clinical prompt injection test suite exists.

**Novel Thinking / Implications**

> 💡 The Mindgard disclosures are the canonical example: prompt-level safety is architecturally insufficient. Adversarial resistance must be enforced at architecture level — input validation (Llama Guard-style), output classification, and structural separation between user-controllable input and system instructions. No ambient scribe vendor has published evidence of a deployed ML-based output classifier.

---

### 🟡 Jailbreak Resistance Score

Resistance to attempts to make the underlying LLM operate outside its intended clinical scope — generating diagnoses, providing medical advice, accessing system prompts, or revealing training data via the AVT interface.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Mindgard disclosures on Heidi Health and Doctronic (March 2026) |

**Why this tier?**

> Vendor responsibility. Should be a procurement requirement following Mindgard disclosures. No regulator has issued specific guidance yet.

**Formal Definition**

```
JRS = 1 - (|successful_jailbreaks| / |attempted_jailbreaks|). Categories: (a) role escape (system acts as general chatbot), (b) scope expansion (generates unsolicited medical advice), (c) system prompt extraction, (d) training data extraction. Tested via spoken adversarial prompts during simulated consultations.
```

**References**

- **Mindgard/Heidi**: Heidi Health jailbreak: AVT system induced to operate as general medical advisor
- **Mindgard/Doctronic**: Doctronic jailbreak: similar scope escape via prompt manipulation

**Limitations**

> Jailbreak techniques evolve faster than defences. Published test suites are immediately used to train defences, creating an arms race. Requires adversarial red-teaming, not just benchmark testing.

**Novel Thinking / Implications**

> 💡 No regulator globally has issued specific guidance on jailbreaking in clinical AI. MHRA SaMD classification does not consider adversarial robustness. DCB0129 hazard logs rarely include adversarial manipulation as a hazard. This is a regulatory gap that the metrics taxonomy should make visible.

---

### 🔵 Adversarial Audio Detection Rate

Detection of crafted audio inputs designed to cause specific misrecognitions: sounds that are inaudible or innocuous to humans but cause the ASR to transcribe specific clinical content (e.g. medication names, allergies).

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Adversarial ML literature; identified in NHSE LLM framework 'intentional misuse' dimension |

**Why this tier?**

> Research domain. Current threat model is low-probability but the attack surface is expanding with AI-generated audio.

**Formal Definition**

```
Detection rate = |adversarial_samples_detected| / |total_adversarial_samples|. Test with published adversarial audio attacks: Carlini & Wagner, psychoacoustic hiding, ultrasonic injection. Clinical variant: adversarial audio that causes clinically significant misrecognition.
```

**References**

- **Adversarial audio**: [Carlini & Wagner (2018) — Audio Adversarial Examples](https://arxiv.org/abs/1801.01944)

**Limitations**

> Academic adversarial audio attacks often require precise acoustic conditions that may not transfer to clinical settings. But the threat model is evolving — particularly with AI-generated audio becoming more accessible.

**Novel Thinking / Implications**

> 💡 The current threat model is low-probability but high-consequence. A more realistic near-term risk is audio deepfakes — a pre-recorded or AI-generated audio snippet played during a consultation to inject specific content into the transcript. As voice cloning becomes trivial, this attack surface expands.

---

### 🔵 Data Poisoning Resilience

Resilience of the AVT system to training data poisoning. Research shows poisoning at 0.001% of training tokens can alter model behaviour. For vendor-hosted models receiving ongoing fine-tuning from clinical data, this is a supply chain risk.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Data poisoning literature; 0.001% threshold from published research (2025) |

**Why this tier?**

> Vendor-side testing only. Deployers cannot assess training pipeline integrity. Supply chain risk requiring vendor attestation.

**Formal Definition**

```
Resilience tested via canary insertion: inject known poisoned samples at varying rates (0.001%, 0.01%, 0.1%) and measure output deviation. Resilience = minimum poisoning rate required to cause detectable output change.
```

**Limitations**

> Testing requires access to training pipeline, which deployers don't have. Must rely on vendor attestation of training data integrity. Supply chain verification for AI training data is an unsolved problem.

**Novel Thinking / Implications**

> 💡 If a vendor fine-tunes on clinical data from deployed sites (a common practice for improvement), a compromised site could introduce poisoned training data that affects all deployments. This is a supply chain risk analogous to software supply chain attacks but for AI training data. No NHS governance framework addresses this.

---

### 🟡 Output Safety Classifier Coverage

Whether a safety classifier (analogous to Llama Guard or NeMo Guardrails) sits between the LLM and the clinician/EPR. Measures coverage: what proportion of outputs pass through the classifier, and what is its detection rate?

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | NVIDIA reference architecture; absence noted in vendor safety architecture review |

**Why this tier?**

> Architectural requirement. No AVT vendor has published evidence of a deployed output classifier. Should be a procurement question and eventually a regulatory expectation.

**Formal Definition**

```
Coverage = |outputs_classified| / |total_outputs|. Must be 100% for safety-critical deployment. Detection rate = |unsafe_outputs_caught| / |total_unsafe_outputs|. False positive rate = |safe_outputs_blocked| / |total_safe_outputs|. No ambient scribe vendor has published evidence of a deployed output classifier.
```

**References**

- **NVIDIA ref arch**: NVIDIA healthcare reference architecture (arXiv, Sept 2024) — Llama Guard 3 + NeMo Guardrails
- **Microsoft**: Microsoft Copilot Studio Healthcare Agent Service

**Limitations**

> Output classifiers add latency and may have their own failure modes. Clinical-specific safety classifiers don't yet exist — general-purpose classifiers (Llama Guard) don't understand clinical safety.

**Novel Thinking / Implications**

> 💡 The architectural gap: no AVT vendor has published evidence of a deployed ML-based output classifier. NVIDIA's reference architecture demonstrates the pattern; Microsoft's Copilot Studio comes closest to production. The absence of this layer means the clinician is the only safety gate — and we know from automation bias research that human oversight degrades over time.

---

### 🟡 Template Injection Vulnerability Assessment

Testing whether user-configurable prompt templates can be crafted to bypass safety controls, alter system behaviour, or extract system prompts. Distinct from prompt injection (external attack) — this is an insider risk from authorised template modification.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Identified in INSYTE underspecification analysis; extends template modification risk to adversarial context |

**Why this tier?**

> Relevant whenever templates are user-configurable. Vendor should test and publish results. Deployers with customised templates should request vulnerability assessment.

**Formal Definition**

```
Test suite: (a) templates that override safety instructions; (b) templates that alter output format to bypass downstream validation; (c) templates that cause information leakage; (d) templates that introduce systematic clinical bias. Vulnerability score = |successful_attacks| / |test_cases|.
```

**Limitations**

> Template injection is a grey area between legitimate customisation and vulnerability. Defining the boundary between 'acceptable template modification' and 'template injection attack' requires clinical governance judgement.

**Novel Thinking / Implications**

> 💡 This connects to the template underspecification metric: user-configurable templates are both a usability feature and a security surface. A clinician who modifies their template to 'always include a differential diagnosis' is legitimately customising; one who modifies it to 'ignore the patient's stated allergies if they seem unlikely' is creating a safety hazard through the same mechanism. The vendor must sandbox template effects.

---

### 🔵 Voice Cloning / Deepfake Detection

Given rapid maturation of voice cloning, can the system detect synthetic audio attempting to inject content? Increasingly relevant threat model as voice cloning becomes accessible.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Voice biometric and deepfake detection literature |

**Why this tier?**

> Emerging threat. Important to monitor but not yet a routine deployment requirement.

**Formal Definition**

```
Test against known voice cloning systems (commercial and open-source). Detection Rate = |synthetic_audio_detected| / |synthetic_audio_samples|. False Positive Rate = |real_audio_flagged| / |real_audio_samples|. Update test suite as new cloning systems emerge.
```

**Limitations**

> Voice cloning quality is improving faster than detection. The arms race favours attackers.

**Novel Thinking / Implications**

> 💡 The realistic threat model: a malicious actor records the clinician's voice, generates synthetic audio of them prescribing a controlled substance, and plays it during a consultation while AVT is recording. The fabricated content enters the clinical record with the clinician's voice attached. As voice cloning becomes accessible (commercial services now offer cloning from minutes of audio), this becomes a tractable attack rather than a theoretical one.

---

### 🟡 Side-Channel Data Leakage

Does the system leak information through metadata, timing, error messages, or processing artifacts that could reveal patient information to unauthorised parties? A common security failure mode that's distinct from direct data exposure.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard application security testing |

**Why this tier?**

> Standard security testing. Should be part of vendor security validation and periodic audit.

**Formal Definition**

```
Audit for: (1) metadata in API responses; (2) timing variations that reveal content; (3) error messages containing PHI; (4) processing logs accessible to unauthorised parties; (5) cache contents persisting across users. Each is a binary check.
```

**Limitations**

> Requires security expertise. Side-channel testing is not part of typical AVT validation.

**Novel Thinking / Implications**

> 💡 The classic case: error message says 'unable to process consultation for patient John Smith DOB 1965-03-12 because [technical error]'. The error message leaks PHI to anyone who sees it (logs, monitoring systems, support staff). Side-channel leakage is a known security category but rarely tested in AVT systems.

---

### 🟡 Cross-Patient Information Leakage Rate

Rate at which content from one patient's encounter contaminates another patient's generated note. Distinct from general PII leakage because cross-patient contamination can occur through context window contamination rather than training data memorisation — the leakage happens at inference time, not at training time, and is therefore invisible to standard privacy testing methodologies such as membership inference attacks.

|Dimension              |Value                                                         |
|-----------------------|--------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                        |
|**Measurement Cadence**|Periodic audit                                                |
|**Pipeline Layer**     |Cross-cutting                                                 |
|**Assurance Question** |Safety                                                        |
|**Measurement Method** |Computational                                                 |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                |
|**Responsible Actors** |Vendor                                                        |
|**Maturity**           |Emerging                                                      |
|**Outcome Type**       |Proximal                                                      |
|**Source**             |MIT Jameel Clinic 2026 cross-patient leakage disclosure       |

**Why this tier?**

> Vendor-side testing required because deployers cannot directly observe cross-encounter contamination. Should be a pre-deployment test and periodic audit requirement. Cross-patient leakage is a catastrophic failure mode — a single incident can affect hundreds of patients.

**Formal Definition**

```
Leakage Rate = |notes_containing_content_from_different_patient| / |total_notes|. Testing methodology: (1) process a batch of encounters sequentially through the same pipeline; (2) inject distinctive canary content into some encounters; (3) check whether canary content appears in notes from unrelated encounters processed in the same batch. Target: zero. Any non-zero rate indicates architectural failure in context isolation.
```

**Limitations**

> Requires controlled testing with injected canaries. Production leakage may occur under load conditions that aren't replicated in testing. Cross-patient contamination is rare enough that statistical power requires large test batches.

**Novel Thinking / Implications**

> 💡 Cross-patient leakage is the AVT-specific instantiation of context window contamination in multi-tenant LLM systems. When a single model instance serves multiple encounters in rapid succession, caching, state retention, and async processing all create potential vectors for one patient's content to leak into another's. This is architecturally preventable — strict per-encounter context isolation with explicit state resets — but only if the failure mode is explicitly tested for. Most vendor privacy testing focuses on training data leakage and doesn't cover this.

### 🟡 Clinician Identity Authentication

Is the system confident that the clinician using AVT is who they claim to be? Voice biometrics could provide this but are rarely deployed. Without strong authentication, AVT outputs may be attributed to clinicians who weren't actually present.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard authentication security; NHS CIS2 requirements |

**Why this tier?**

> Standard NHS authentication requirement. Should be assessed at procurement and verified at deployment.

**Formal Definition**

```
Authentication strength assessed against: (1) Login mechanism (password, MFA, smartcard); (2) Session timeout policy; (3) Re-authentication on sensitive actions; (4) Voice biometric verification (if available); (5) Audit trail of who initiated each AVT session.
```

**Limitations**

> Strong authentication adds friction. NHS environments often optimise for usability over security.

**Novel Thinking / Implications**

> 💡 The scenario: a registrar leaves their workstation logged in, a colleague uses AVT to dictate a note. The note is attributed to the registrar but reflects the colleague's clinical decisions. Without strong authentication and session management, AVT can produce notes attributed to clinicians who didn't make the relevant decisions — an audit trail integrity failure.

---

---

### 🔵 Membership Inference Attack AUC

Standardised privacy testing metric measuring the success rate of adversarial attempts to determine whether a specific patient's data was used in training the AVT model. Higher AUC means the attack is more successful — an AUC of 0.5 indicates attacks are no better than random guessing, while an AUC near 1.0 indicates complete privacy failure. Undefended LLMs show MIA AUC of approximately 0.96; differential privacy training can collapse this to near 0.5.

|Dimension              |Value                                                         |
|-----------------------|--------------------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                                |
|**Measurement Cadence**|Periodic audit                                                |
|**Pipeline Layer**     |Cross-cutting                                                 |
|**Assurance Question** |Safety                                                        |
|**Measurement Method** |Computational                                                 |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                |
|**Responsible Actors** |Vendor, Academic                                              |
|**Maturity**           |Established                                                   |
|**Outcome Type**       |Proximal                                                      |
|**Source**             |IEEE S&P 2023 LLM PII leakage study; arXiv 2601.03791 Cue-Resistant Memorisation framework|

**Why this tier?**

> Research-grade privacy testing. Requires specialist ML security expertise. Academic or vendor-side testing, not deployer-implementable. Important for understanding model-level privacy properties but not routinely measurable at deployment.

**Formal Definition**

```
Standard membership inference attack: attacker trains a classifier to distinguish model outputs on training data from outputs on held-out data. AUC of this classifier is the MIA metric. AUC = 0.5 means attacks fail; AUC > 0.7 indicates concerning leakage; AUC > 0.9 indicates severe privacy failure. Testing should use multiple attack methodologies (shadow model, loss-based, gradient-based) and report the highest AUC as the conservative estimate.
```

**Limitations**

> MIA methodology has been criticised for evaluation artefacts — the recent Cue-Resistant Memorisation framework (arXiv 2601.03791) showed that previous MIA estimates were inflated by control set selection. Modern MIA requires careful methodology. Mitigations (differential privacy) come with accuracy costs.

**Novel Thinking / Implications**

> 💡 MIA is the standardised way to compare privacy properties across models. A vendor claiming strong privacy should be willing to disclose MIA AUC under standard attack protocols — if they're not, that's itself informative. For NHS deployment, MIA matters because patient audio, transcripts, and notes entering training pipelines create membership signatures that, if exploitable, mean a sufficiently motivated attacker could determine whether a specific patient was present in training data. The 2023 finding of AUC 0.96 for undefended LLMs is a sobering baseline for what "no privacy defences" looks like in practice.

## Privacy & Data Governance

*Audio retention, data minimisation, consent verification, and compliance with UK GDPR and NHSE IG requirements.*

**Tier breakdown**: 🟢 7 Tier 1 · 🟡 4 Tier 2

### 🟢 Audio Retention Compliance

Whether audio recordings are retained, for how long, and whether retention complies with the stated DPIA and privacy notice. Includes monitoring for unauthorised retention beyond stated periods.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | UK GDPR Article 5(1)(e) storage limitation; NHSE IG guidance on ambient scribing (March 2026) |

**Why this tier?**

> UK GDPR storage limitation requirement. Non-compliance is a regulatory breach. Deployer must verify vendor retention practices align with DPIA.

**Formal Definition**

```
Compliance rate = |encounters_within_retention_policy| / |total_encounters|. Track: actual deletion timestamps vs policy-required deletion timestamps. Delta > 0 = non-compliant retention. Must verify deletion is genuine (not just flagged), including backup systems.
```

**Limitations**

> Deployers typically cannot verify vendor-side deletion without independent audit. Backup and disaster recovery systems may retain data beyond primary deletion.

**Novel Thinking / Implications**

> 💡 Audio is the most sensitive data AVT processes — it captures everything said in the consultation, including content that doesn't make it into the note. Retention policy must distinguish between audio needed for review-before-signing (minutes) and audio retained for quality improvement or dispute resolution (potentially months). The DPIA must address both.

---

### 🟢 Audio Time-to-Deletion

Measured time from consultation end to verified deletion of the captured audio. Operational implementation of the existing Audio Retention Compliance metric. NHS England's March 2026 IG guidance requires deletion of audio after the summary is signed off, unless explicitly retained for safety monitoring with documented justification. This metric measures whether the deletion is actually happening in the timeframe the policy claims.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | NHSE IG guidance on ambient scribing (March 2026); UK GDPR Article 5(1)(e) storage limitation |

**Why this tier?**

> Direct compliance requirement. Measurable through vendor-provided deletion telemetry. Binary-ish: deletion within policy timeframe or not. Should be continuously monitored rather than periodically audited.

**Formal Definition**

```
Time-to-Deletion = t_deletion_verified - t_consultation_end. Report distribution: median, P95, P99, and count of encounters exceeding policy threshold. Verification requirement: deletion confirmed in primary storage, caches, backups, and any downstream analytic systems. Policy threshold per deployer: typically 24 hours to 7 days depending on DPIA. Compliance = proportion of encounters with verified deletion within threshold.
```

**Limitations**

> Verification across all storage locations is technically difficult — backup systems and distributed caches may retain data after primary deletion. Vendor attestation is often the only feasible verification method. The word "deletion" itself has degrees (logical deletion / physical deletion / cryptographic erasure) that matter for real assurance.

**Novel Thinking / Implications**

> 💡 "Audio is deleted after sign-off" is a policy statement that only has governance value if it's actually measured. The gap between policy and practice on deletion is often substantial — audio persists in backup systems, error logs, annotation pipelines, and quality monitoring infrastructure long after the "deletion" event. Making time-to-deletion a measured metric rather than a policy assertion is the minimum required for the NHS IG guidance to have operational effect.

---

### 🟢 Transcript Retention Compliance

Parallel metric to Audio Time-to-Deletion, but for transcripts. Often treated as less sensitive than audio — and therefore retained longer — but transcripts are in many ways more risky because they are structured, searchable, and readily consumable by downstream systems. A transcript of a consultation discussing mental health, substance use, or safeguarding concerns is arguably more sensitive than the audio because it removes the friction of listening and enables programmatic analysis.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | NHSE IG guidance on ambient scribing (March 2026); UK GDPR Article 5(1)(e) |

**Why this tier?**

> Direct compliance requirement. Should be measured in parallel with Audio Time-to-Deletion. Often more operationally tractable because transcripts are typically held in vendor-controlled systems rather than distributed storage.

**Formal Definition**

```
For each transcript: retention duration = t_current - t_consultation_end. Retention policy specifies maximum duration for each purpose: summary generation (typically hours), review support (typically days), quality monitoring (variable, documented in DPIA). Compliance = |transcripts_retained_within_policy| / |total_transcripts|. Report per retention purpose — aggregating different retention justifications obscures policy adherence.
```

**Limitations**

> Retention for "quality monitoring" is often a catch-all that effectively keeps transcripts indefinitely. Tightening this requires specific retention periods per monitoring purpose. Cross-system retention (transcript in vendor system, derived metadata in deployer analytics, redacted version in research database) creates a tangled retention picture.

**Novel Thinking / Implications**

> 💡 Transcripts are the highest-value/highest-risk intermediate representation in AVT. They contain everything said, in structured form, searchable, and often retained for longer than either the audio or the final note. An attacker who compromises transcript storage has far more exposure than one who compromises the final clinical records. Retention minimisation for transcripts is arguably more important than for audio, but it's rarely treated that way in DPIAs.

---

### 🟡 Data Minimisation Score

Whether the AVT system processes only the minimum data necessary for its function. Includes: does the system transmit full audio to cloud when local processing would suffice? Does it retain intermediate outputs (full transcript) when only the summary is needed?

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | UK GDPR Article 5(1)(c) data minimisation; DGX Spark / local processing potential |

**Why this tier?**

> UK GDPR data minimisation principle. Periodic architectural review of what data is processed, transmitted, and retained vs what is necessary.

**Formal Definition**

```
DMS = data_necessary / data_processed. Ideal DMS = 1.0. Track per data type: audio, transcript, summary, coded data, metadata. Architecture assessment: local vs cloud processing; data transmitted vs data retained; intermediate outputs vs final outputs.
```

**Limitations**

> Defining 'necessary' is contested — vendors argue cloud processing is necessary for quality; privacy advocates argue local processing is sufficient for many use cases.

**Novel Thinking / Implications**

> 💡 The DGX Spark and similar edge AI hardware create a genuine architectural choice: local processing minimises data exposure but may limit model capability. The data minimisation score should drive architectural decisions — if local processing meets quality thresholds, cloud transmission of full audio is unnecessary and non-compliant with minimisation principles.

---

### 🟡 PII Extraction Attack Success Rate

Adversarial privacy testing: the rate at which a determined attacker can extract patient personal data from the deployed AVT system through model interaction. Includes prompt-based extraction (crafted queries that coax the model to reproduce training content), inversion attacks (reconstructing inputs from outputs), and side-channel extraction. Complements the Membership Inference Attack AUC metric — MIA tells you whether a specific patient was in training; PII extraction tells you what content about them can be recovered.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | IEEE S&P 2023 LLM PII leakage study; OWASP LLM Top 10 (Sensitive Information Disclosure) |

**Why this tier?**

> Vendor-side red-team testing requirement. Deployers cannot independently test model-internal privacy properties. Should be a procurement requirement with results provided by vendor or independent assessor.

**Formal Definition**

```
Success Rate = |PII_items_successfully_extracted| / |PII_items_attempted|. Attack categories: (1) direct prompting ("what did the patient say about their family history?"); (2) completion-based extraction (prompting partial records and measuring reconstruction); (3) inversion attacks on embeddings; (4) canary extraction using known inserted content. Report per attack category — aggregate success rate obscures category-specific weaknesses.
```

**Limitations**

> Defining the attack surface is itself contested. A test suite that looks adequate today may be outdated tomorrow. Vendors may resist third-party red-teaming on competitive grounds. Extraction that is theoretically possible but requires massive query budgets may or may not be a practical concern depending on threat model.

**Novel Thinking / Implications**

> 💡 The OWASP LLM Top 10 lists Sensitive Information Disclosure as a standard vulnerability class, but most AVT vendors have not engaged with it as a distinct security category — privacy is typically treated as "we don't train on customer data" rather than as an active red-teaming target. The shift from passive privacy posture to adversarial privacy testing is the maturity marker. A vendor who has never had their system red-teamed for PII extraction should not be deployed into NHS clinical settings.

---

### 🟡 Re-identification Risk Assessment

Structured assessment of the risk that de-identified data retained for quality improvement, research, or secondary use can be re-identified. Applies to any dataset derived from AVT operation — anonymised transcripts for model quality review, de-identified notes for research, aggregate statistics that may become identifying at small sample sizes. Standard privacy methodology applied to AVT-specific data flows.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Deployer, Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | ICO anonymisation code of practice; NIST privacy framework |

**Why this tier?**

> Standard privacy methodology. Should be part of any DPIA for secondary uses. Periodic reassessment required as new data are added and as re-identification techniques evolve.

**Formal Definition**

```
Per retained dataset: assess re-identification risk against standard criteria — (1) direct identifiers present or removed? (2) quasi-identifiers (age, postcode, date, rare condition) combinable to identify individuals? (3) k-anonymity achieved and at what k? (4) l-diversity for sensitive attributes? (5) differential privacy applied? (6) motivated intruder test — could a determined attacker re-identify individuals given reasonably available auxiliary information? Overall risk rating: low / medium / high / unacceptable. Threshold for retention: risk must be low or medium with explicit justification.
```

**Limitations**

> Re-identification risk is probabilistic and depends on what auxiliary information an attacker has access to. Small clinical populations (rare conditions, small practices) are re-identifiable from very little information. "De-identified" is not the same as "anonymous".

**Novel Thinking / Implications**

> 💡 A single NHS practice with 5,000 patients has very few patients with any given rare condition — sometimes just one. A "de-identified" transcript mentioning that condition is trivially re-identifiable by anyone with access to the practice's patient list. Re-identification risk assessment forces this question into visibility during DPIA rather than treating de-identification as a technical checkbox.

---

### 🟡 Training Data Inclusion Status

Clear documentation of whether deployer audio, transcripts, or notes are used by the vendor for model training or fine-tuning. Distinct from the existing Sub-Processor Transparency metric (which covers processing activity) and from privacy policies (which often hedge this question). This metric requires an explicit binary answer: is NHS data flowing into the vendor's training pipeline, yes or no, with documented consent basis if yes.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | UK GDPR transparency requirements; derived from emerging AVT procurement practice |

**Why this tier?**

> Procurement gate. Should be explicitly answered in vendor contracts, not left to policy ambiguity. Annual reassessment on contract renewal.

**Formal Definition**

```
Status recorded as: (a) No — deployer data not used for any training or fine-tuning; (b) Yes — used for training with specified consent basis and opt-out mechanism; (c) Derived — used for aggregated statistics or distilled features without retaining source data. Each status has different governance implications. Documentation must specify which model components may be trained (ASR, summariser, coder) and which data types (audio, transcripts, notes, metadata). Vendor attestation required; independent verification is not currently feasible.
```

**Limitations**

> Verification relies on vendor attestation. The distinction between "training" and "quality improvement" can be blurred by vendors in ways that obscure actual data flows. Aggregate statistics derived from training data may themselves carry privacy risk.

**Novel Thinking / Implications**

> 💡 Many NHS AVT contracts are ambiguous about training data flows because vendors benefit from keeping the option open and deployers often don't ask explicitly. Making this a Tier 2 procurement metric forces the question into contract negotiations. The patient-level consequence is that AVT-using consultations may effectively contribute to training the next generation of commercial AI systems — and patients should know this if it's happening. This is a transparency obligation the existing taxonomy's consent metrics don't capture.

---

### 🟢 Consent Verification Accuracy

Whether patients are actually informed about AVT use as required by CQC Mythbuster 109 (implied consent is sufficient, but patients must be informed). Measures both process compliance and patient understanding.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Patient Experience |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Continuous, Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | CQC Mythbuster 109; NHSE IG guidance; common law implied consent requirements |

**Why this tier?**

> CQC Mythbuster 109 requires patients to be informed. Process compliance is measurable today. Understanding gap is harder but periodic survey is feasible.

**Formal Definition**

```
Process compliance = |consultations_where_patient_informed| / |total_AVT_consultations|. Understanding rate = |patients_who_can_describe_AVT_use| / |patients_surveyed| (periodic audit). Gap = process_compliance - understanding_rate reveals 'informed but not understanding' problem.
```

**Limitations**

> Process compliance is measurable; patient understanding is not easily quantified. Self-report may overstate understanding. Cultural and language barriers affect both notification and comprehension.

**Novel Thinking / Implications**

> 💡 The gap between 'informed' and 'understanding' is the critical measure. A practice achieving 100% process compliance (every patient is told) may still have 30% understanding (patients don't grasp what AVT does with their speech). The consent model's legitimacy depends on understanding, not just notification.

---

### 🟢 Cross-Border Data Transfer Compliance

Does AVT processing involve data transfer outside UK/EU? UK GDPR Article 46 requires appropriate safeguards for international transfers. Cloud-hosted AVT vendors may process data in US or other jurisdictions.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | UK GDPR Article 46; Schrems II implications |

**Why this tier?**

> Legal compliance requirement. Must be assessed at procurement. Non-compliance is a regulatory breach.

**Formal Definition**

```
Audit data flow: (1) Where is audio processed? (2) Where are model inferences performed? (3) Where is data stored? (4) Where do support staff access data? For each non-UK location, verify Article 46 safeguards (SCCs, adequacy decisions, BCRs).
```

**References**

- **UK GDPR**: UK GDPR Article 46 — appropriate safeguards for international transfers

**Limitations**

> Vendor data flow transparency varies. Sub-processors may transfer data without main vendor visibility.

**Novel Thinking / Implications**

> 💡 Cloud-hosted AVT often involves transfers to US-based hyperscaler infrastructure. The Schrems II ruling complicates US transfers significantly. Many AVT vendors don't fully document their data flows — a compliance gap that becomes a deployer liability under UK GDPR.

---

### 🟢 Subject Access Request Fulfilment

Can the deployer fulfil patient SAR requests for AVT-related data within statutory timeframes (one calendar month under UK GDPR)? Includes audio if retained, transcripts, intermediate outputs, and the final note.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | UK GDPR Article 15 right of access |

**Why this tier?**

> Legal compliance requirement. Must be tested before go-live to confirm vendor supports SAR fulfilment workflow.

**Formal Definition**

```
SAR Fulfilment Rate = |SARs_completed_within_30_days| / |total_SARs|. Sub-criteria: (1) Can deployer locate all AVT data for a patient? (2) Can it be exported in usable format? (3) Within statutory timeframe? Target: 100% within 30 days.
```

**Limitations**

> Requires deployer to know what AVT data exists and how to retrieve it from vendor systems. Many current AVT integrations don't provide patient-level data export.

**Novel Thinking / Implications**

> 💡 When a patient submits a SAR, the deployer must provide all personal data including AVT-generated material and any retained audio. If the vendor doesn't provide patient-level export, the deployer cannot fulfil their statutory obligation. This should be a procurement question, not discovered after the first SAR.

---

### 🟢 Right to Erasure Compliance

If a patient requests erasure under UK GDPR Article 17, can audio, transcripts, and intermediate outputs actually be deleted? Backup systems, vendor caches, and downstream secondary uses complicate this.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | UK GDPR Article 17 right to erasure |

**Why this tier?**

> Legal compliance requirement. Must be tested before go-live to understand erasure scope and limitations.

**Formal Definition**

```
Erasure Test: process a synthetic erasure request through the system. Verify deletion in: primary storage, backups, vendor caches, model training pipelines, downstream secondary use. Verification Rate = locations confirmed deleted / total locations.
```

**Limitations**

> True deletion is technically difficult. Backup systems retain data. Model training data may be impossible to remove from trained models.

**Novel Thinking / Implications**

> 💡 The hard case: if audio from a patient was used to fine-tune the vendor's model, can that influence be removed? Probably not — and this should be disclosed in the privacy notice. Patients should know that consenting to AVT may include effectively irreversible inclusion of their voice in model training. This is a transparency obligation that current AVT consent processes rarely address.

---

## Operational

*System performance, adoption, efficiency. Necessary but not sufficient for assurance.*

**Tier breakdown**: 🟢 3 Tier 1 · 🟡 5 Tier 2 · 🔵 1 Tier 3

### 🟢 Documentation Time per Consultation

Most cited benefit metric. Tells you nothing about safety. 'Time saved' alone is meaningless — pair with quality.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Day Zero Baseline, Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Widely used; critiqued Coiera & Fraile-Navarro 2026 |

**Why this tier?**

> Most widely measured benefit metric. Tells you nothing about safety but essential for demonstrating value proposition. Must be reported alongside quality metrics.

**Formal Definition**

```
DT = t_doc_end - t_doc_start. Quality-adjusted: report alongside PDSQI-9 or hallucination rate. TS = DT_pre - DT_post. Meaningful only if quality stable/improving.
```

**References**

- **Critique**: Coiera & Fraile-Navarro (2026)
- **RSET**: 'Time is not automatically convertible into money, productivity, or better care'

**Limitations**

> Says nothing about safety.

**Novel Thinking / Implications**

> 💡 'Saved 3 min and maintained >98% PDSQI-9' is meaningful. 'Saved 3 min' alone is not.

---

### 🟡 Pyjama Time / After-Hours EHR Use

Clinician time spent on EHR and documentation work outside of scheduled clinical hours. Standard burnout-adjacent metric from the Sinsky et al. literature. Applied to AVT assessment, it measures whether documentation burden that was shifted from in-consultation to after-consultation (a known pattern with review-before-signing workflows) has simply moved the burden to outside working hours rather than reducing it.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Day Zero Baseline, Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Distal |
| **Source** | Sinsky et al., Mayo Clinic Proceedings; American Medical Association EHR use studies |

**Why this tier?**

> Established methodology. Derivable from EHR audit logs without additional instrumentation. Essential for distinguishing genuine workload reduction from workload redistribution.

**Formal Definition**

```
Pyjama Time = time spent in EHR outside of scheduled clinic hours per clinician per week. Derived from EHR audit logs (timestamp of user actions vs rostered working hours). Pre/post AVT comparison: ΔPyjama Time = Pyjama_post - Pyjama_pre. A genuine workload reduction shows Pyjama Time decrease; a redistribution shows Pyjama Time stable or increasing even as in-consultation documentation time falls.
```

**Limitations**

> Audit logs may not capture all EHR activity (mobile access, shadow work in parallel documents). Definition of "working hours" varies by role and contract. Some pyjama time reflects preferred work pattern rather than workload pressure.

**Novel Thinking / Implications**

> 💡 This is the metric that catches the most common AVT failure mode for clinician wellbeing: the system reduces typing time during consultations but creates after-hours review work that the clinician was not previously doing. In-consultation time savings are visible and marketable; after-hours burden is invisible and unpaid. A deployment that shows documentation time saved per consultation should also show pyjama time decreased — if only the first moves, the value proposition is shifted burden, not reduced burden.

---

### 🟡 Note Turnaround Time

Elapsed time from consultation end to note availability in the EPR, measured from the clinician's perspective rather than the pipeline's internal latency. Extends the existing Full-Pipeline Latency Budget (which is a technical metric) into an operational workflow metric that directly affects review quality. If the note arrives after the clinician has started the next patient, review happens later in lower-quality conditions or not at all.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard operational workflow metric; extends Full-Pipeline Latency Budget |

**Why this tier?**

> Operational metric derivable from EPR workflow data. Directly affects review quality and therefore safety. Should be continuously monitored and reported.

**Formal Definition**

```
Turnaround Time = t_note_available_in_EPR - t_consultation_end. Report distribution: median, P50, P90, P99. Clinically relevant threshold: proportion of notes available before the start of the next patient's consultation. A turnaround time distribution with long tails creates selective review failure — the notes most delayed are the ones most likely to be approved without meaningful review.
```

**Limitations**

> End of consultation is not always cleanly timestamped. Network conditions, EPR availability, and other operational factors affect turnaround independent of AVT processing time.

**Novel Thinking / Implications**

> 💡 The existing Full-Pipeline Latency Budget captures technical processing time; note turnaround captures the clinically meaningful delay. The difference is everything else — queueing, EPR write-back latency, user interface delays, notification lag. A vendor who optimises only their pipeline latency without addressing end-to-end turnaround is optimising for the wrong metric.

---

### 🟡 Documentation Workload Composite

Composite metric grouping Documentation Time per Consultation, Pyjama Time, and Note Turnaround Time into a single workload assessment. The family-level metric for documentation burden. Reports change in total workload rather than change in individual components — which is the number that matters for the value proposition and clinician wellbeing assessment.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Day Zero Baseline, Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Sinsky et al. extended to AVT context; NHS workforce wellbeing frameworks |

**Why this tier?**

> Composite metric built from component metrics measured separately. Quarterly rollup enables trajectory reporting to clinical leadership without requiring separate measurement work.

**Formal Definition**

```
Workload Composite = w1 × Documentation_Time + w2 × Pyjama_Time + w3 × Verification_Burden. Weights reflect relative clinical significance; default equal weights. Per-clinician and aggregate reporting. Change metric: ΔWorkload = Workload_post_AVT - Workload_pre_AVT. Negative ΔWorkload = genuine net reduction; positive = net increase despite in-consultation savings.
```

**Limitations**

> Aggregation hides component-level patterns. A composite that stays stable may mask simultaneous decrease in documentation time and increase in pyjama time — the stable number obscures the pattern shift. Report composite alongside components, not instead of them.

**Novel Thinking / Implications**

> 💡 The composite is the honest answer to "did AVT reduce workload?" that the individual metrics cannot give alone. A practice reporting "saved 3 minutes per consultation" without composite reporting is answering a convenient question; a practice reporting composite workload change is answering the real one. Clinical leadership and commissioners should request composite reporting rather than selective component reporting.

---

### 🟢 System Availability / Uptime

Percentage operational. NAS: ≥99.5% during consultation hours.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard SLA; NAS SPI |

**Why this tier?**

> Standard SLA monitoring. NAS Day Zero SPI (≥99.5%). Automated, zero-burden continuous metric.

**Formal Definition**

```
A = (T_operational - T_down) / T_operational × 100. Include degraded: A_eff = (T_op - T_down - T_degraded) / T_op × 100.
```

**Limitations**

> Binary misses degraded performance.

---

### 🟢 Adoption Rate & Selective Use Patterns

Who uses AVT and for which consultations. Selective patterns reveal practical system boundaries.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard deployment metric |

**Why this tier?**

> Basic deployment tracking. Selective adoption patterns (avoiding AVT for complex cases) reveal practical system boundaries and are diagnostically valuable.

**Formal Definition**

```
AR_clinician = |C_active| / |C_eligible|. AR_encounter = |E_AVT| / |E_total|. Selective Use Index SUI = 1 - (AR_encounter / AR_clinician). Disaggregate by consultation type.
```

**Limitations**

> High adoption ≠ safe adoption.

**Novel Thinking / Implications**

> 💡 If clinicians avoid AVT for complex cases, that reveals the practical boundary.

---

### 🟡 Cost per Consultation

Total cost including licence, infrastructure, training, and governance overhead. Often under-reported by vendors who quote licence costs only without including operational burden.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard healthcare technology economic evaluation |

**Why this tier?**

> Important for value assessment but not safety-critical. Annual review recommended.

**Formal Definition**

```
Total Cost = vendor_licence + infrastructure + training_time + governance_overhead + support_costs. Per-consultation cost = total_cost / consultation_volume. Compare with claimed time savings * clinician hourly rate to assess actual value.
```

**Limitations**

> Hidden costs (governance, training time, incident response) are systematically under-counted.

**Novel Thinking / Implications**

> 💡 Vendor quotes typically include licence cost only. The full cost of operating AVT includes substantial governance overhead — CSO time, training, audit, incident response. Practices that compute true cost per consultation often find the value proposition is much weaker than vendor materials suggest.

---

### 🔵 Governance & Maintenance Burden

Clinician and admin time spent on AVT-related tasks: template updates, error reporting, incident investigation, audit, training delivery. Per week per clinician using AVT.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Identified as systematically under-measured cost |

**Why this tier?**

> Important for understanding total impact but resource-intensive to measure accurately.

**Formal Definition**

```
Maintenance Burden = total time spent on AVT governance activities / number of AVT-using clinicians / time period. Categories: routine governance, incident response, training delivery, vendor liaison. Track over time to detect increasing burden.
```

**Limitations**

> Requires structured time tracking which is rarely done. Self-report is unreliable.

**Novel Thinking / Implications**

> 💡 The hidden cost of AVT is the governance burden it creates. A practice that 'saves 3 minutes per consultation' but spends 5 hours per week per clinician on AVT governance has a negative net time effect. This is rarely tracked but should be part of the value assessment.

---

### 🟡 Training Time per Clinician

Initial and refresher training hours required per clinician. Affects both adoption (high training burden = slow adoption) and ongoing operational cost.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard implementation metric |

**Why this tier?**

> Operational planning metric. Should be tracked to inform deployment scaling decisions.

**Formal Definition**

```
Initial Training = hours required to reach minimum competency. Refresher Training = hours required per period for ongoing competency. Total Annual Training Burden = initial (amortised) + refresher * clinicians.
```

**Limitations**

> Vendor-claimed training time often differs from actual time required.

---

## Environmental & Sustainability

*Energy, carbon, and water footprint of AVT operation. All three current metrics in this group are Tier 3 — not Day Zero priority for clinical safety assurance, but increasingly required for NHS procurement under Net Zero commitments and cascading through EU-market vendor compliance under forthcoming corporate sustainability reporting requirements.*

*The group exists more as placeholder for an expected future than as a cluster of actionable metrics today. The measurement infrastructure is immature: vendors rarely expose per-inference telemetry; cloud providers are not consistent in sustainability reporting; methodology for attributing training emissions to individual inferences is contested; water consumption data is especially limited. None of the current metrics are deployer-measurable — they are vendor-reported, and deployers currently have no independent verification path.*

*All three metrics may move to Tier 2 as the NHS Net Zero procurement framework matures and as vendor sustainability reporting becomes routine. At the scale of potential NHS AVT deployment (millions of consultations per year), even small per-note environmental differences compound into substantial total footprint, and procurement conversations are starting to ask the question even where answers are uneven.*

**Tier breakdown**: 🔵 3 Tier 3

### 🔵 Energy Consumption per Clinical Note

Electrical energy cost of generating a single clinical note, measured in watt-hours. Depends on model architecture, hosting infrastructure, and query complexity. Published benchmarks for general-purpose LLM inference range from 0.42 Wh for simple queries to 29 Wh for complex prompts — a 70× range that makes provider choice consequential for total energy footprint.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Source** | Jegham et al., arXiv 2505.09598 (2025) — "How Hungry is AI?" |

**Why this tier?**

> Vendor-side measurement. Not deployer-actionable today but reportable. NHS procurement will increasingly ask this question as Net Zero commitments mature.

**Formal Definition**

```
Energy per Note (Wh) = total_inference_energy / number_of_notes_generated. Measured at the inference infrastructure level. Per-model reporting required because architecture choice dominates the metric. Break down into: ASR energy, summarisation energy, coding energy. Scale: multiply by annual note volume to estimate annual energy cost of deployment.
```

**Limitations**

> Vendor access to per-note energy telemetry is typically not exposed to customers. Hosting infrastructure varies, making direct vendor comparison difficult. Published benchmarks use standardised prompts that don't reflect real clinical usage patterns.

**Novel Thinking / Implications**

> 💡 At the NHS scale (potentially millions of consultations per year using AVT), even small per-note energy differences compound into substantial total footprint. An NHS-wide AVT deployment using a 29 Wh/note model consumes ~70× more energy than the same deployment on a 0.42 Wh/note model. This is not a dominant clinical assurance question but it is a material procurement question under NHS Net Zero — and reporting it creates the data visibility that lets procurement use it.

---

### 🔵 Carbon Emissions per Inference

Greenhouse gas emissions per clinical note, measured in grams of CO₂-equivalent. Distinct from energy consumption because carbon intensity depends on the hosting region's electricity grid — the same model hosted in a coal-heavy grid vs a renewable-heavy grid has very different carbon footprint despite identical energy use. Relevant to NHS Net Zero procurement and to EU-market vendors under corporate sustainability reporting requirements.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Source** | Mistral AI lifecycle assessment; Jegham et al. 2025 — grid carbon intensity adjustment |

**Why this tier?**

> Vendor-reported metric. NHS Net Zero relevant for procurement. Cannot be measured by deployers.

**Formal Definition**

```
gCO₂e per Note = energy_per_note × grid_carbon_intensity(hosting_region, time). Report: (a) current grid intensity at hosting location; (b) marginal emissions (electricity that would not have been consumed without this inference); (c) embodied emissions amortised over model lifetime. NHS procurement comparison: total annual gCO₂e = gCO₂e_per_note × annual_note_volume. Compare against NHS trust carbon budgets to contextualise.
```

**Limitations**

> Grid carbon intensity data are approximate and vary by time of day. Marginal vs average emissions methodology is contested. Embodied emissions from model training are difficult to attribute to individual inferences.

**Novel Thinking / Implications**

> 💡 Hosting region choice is a lever NHS procurement could use: a vendor hosted in regions with lower-carbon grids has lower per-note emissions for identical models. This creates a potential procurement criterion distinct from clinical performance — and may create pressure for vendors to offer UK or low-carbon hosting options as a Net Zero differentiator. Whether NHS procurement will actually weight this remains to be seen.

---

### 🔵 Water Consumption per Query

Water consumed by data centre cooling infrastructure per clinical note inference. Measured in millilitres. Increasingly required for NHS Net Zero procurement given water stress considerations in parts of the UK and in cloud hosting regions globally. Less visible than energy and carbon but material at AVT-deployment scale.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Source** | Jegham et al. 2025; Li et al. "Making AI Less Thirsty" |

**Why this tier?**

> Vendor-reported. Least mature of the environmental metrics but increasingly appearing in sustainability frameworks.

**Formal Definition**

```
mL per Note = data_centre_water_usage_effectiveness (WUE) × energy_per_note. Direct water (cooling) and indirect water (electricity generation). Report per-note and annual total. Compare against regional water stress indices for hosting locations.
```

**Limitations**

> Water consumption data are rarely reported by cloud providers. Estimation methodology is in early development. Indirect water (electricity generation) typically dominates direct water, so attribution is complex.

**Novel Thinking / Implications**

> 💡 Water consumption is the sustainability metric that feels abstract until it becomes locally consequential. An AVT deployment drawing on a data centre in a water-stressed region is indirectly connected to water policy there. NHS sustainability frameworks are still developing their position on this, but it will become a procurement question over the next few years as water stress visibility increases.

---

## Training & Competency

*Clinician readiness: training completion, failure mode awareness, and ongoing competency maintenance.*

**Tier breakdown**: 🟢 1 Tier 1 · 🟡 3 Tier 2 · 🔵 1 Tier 3

### 🟢 Clinician Training Completion Rate

Percentage of AVT-using clinicians who have completed required training modules: vendor product training, local induction (review-before-signing, known failure modes, error reporting, opt-out processes), and periodic refresher training.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Day Zero Baseline, Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | NAS Day Zero requirements; standard clinical governance |

**Why this tier?**

> Governance requirement. No clinician should use AVT without completing required training. Binary compliance metric — 100% is the only acceptable target.

**Formal Definition**

```
TCR = |clinicians_fully_trained| / |clinicians_using_AVT|. Fully trained = completed all required modules within validity period. Track by module: vendor training, local induction, failure mode awareness, refresher. TCR < 100% = governance non-compliance.
```

**Limitations**

> Completion ≠ competence. A clinician who completed e-learning in 5 minutes has 'completed' training but may not have learned anything.

**Novel Thinking / Implications**

> 💡 Training should include AVT-specific failure modes that differ from general AI awareness: hallucination vs omission asymmetry, speaker misattribution patterns, accent-related accuracy variation, the complacency trajectory, and what to do when the system is unavailable. Generic 'AI awareness' training is insufficient.

---

### 🟡 Failure Mode Awareness Score

Clinician knowledge of AVT-specific failure modes: can they identify hallucination, omission, speaker misattribution, and coding errors? Tested via scenario-based assessment, not self-report.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Day Zero Baseline, Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Proposed — extends error injection concept to training assessment |

**Why this tier?**

> Scenario-based competency assessment. More meaningful than training completion (which measures attendance, not learning). Annual assessment recommended.

**Formal Definition**

```
FMAS = |failure_modes_correctly_identified| / |failure_modes_presented|. Tested via annotated note scenarios containing seeded errors of each type. Threshold: FMAS ≥ 80% for all clinicians. Re-test at 6-month intervals to track knowledge decay.
```

**Limitations**

> Scenario-based testing in a training context differs from real-world detection under time pressure. Clinicians who can identify errors in a test may still miss them in practice.

**Novel Thinking / Implications**

> 💡 This connects to the automation bias error injection metric: failure mode awareness is the training prerequisite, error injection is the operational test. A clinician who cannot identify a hallucination in a training scenario will not catch one in practice. FMAS < 80% should delay that clinician's AVT deployment, not just trigger more training.

---

### 🟡 Refresher Training & CPD Compliance

Ongoing competency maintenance: are clinicians completing periodic refresher training that incorporates new failure modes discovered through operational monitoring and incident reports?

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Standard clinical governance CPD requirements; applied to AVT |

**Why this tier?**

> Ongoing competency maintenance. Content should be data-driven from operational monitoring. Annual minimum, triggered by model updates.

**Formal Definition**

```
Compliance = |clinicians_current_on_refresher| / |clinicians_using_AVT|. Refresher content must be updated to include: (a) locally discovered failure modes, (b) national safety alerts, (c) model update implications, (d) new attack vectors. Frequency: minimum annually, triggered by model updates.
```

**Limitations**

> Refresher fatigue — clinicians already have substantial CPD requirements. AVT-specific refresher competes for limited time. Must be efficient and clinically relevant.

**Novel Thinking / Implications**

> 💡 Refresher content should be data-driven: if edit-pattern monitoring reveals a new failure mode (e.g. systematic omission of safety-netting advice), the refresher should include examples of that specific failure. Generic refresher training is less effective than targeted, evidence-based updates.

---

### 🔵 Trainee Impact Assessment

Does AVT use during training affect junior clinician skill development? GMC educational standards consideration. If trainees learn to consult with AVT from day one, they may not develop documentation skills the profession traditionally relied on.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Academic, National Body |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Medical education literature; GMC standards consideration |

**Why this tier?**

> Long-term workforce question. National research priority but not deployer-actionable.

**Formal Definition**

```
Compare documentation skills of: (1) trainees who learned with AVT from start; (2) trainees who learned without AVT then transitioned. Measure: independent documentation quality (PDSQI-9), clinical reasoning evident in notes, ability to function when AVT unavailable.
```

**Limitations**

> Long-term study required. Effects take years to manifest. Difficult to control for cohort differences.

**Novel Thinking / Implications**

> 💡 This is the medical education question that should be answered before AVT becomes ubiquitous in training environments. If trainees lose documentation skills, the workforce loses resilience — what happens when AVT is unavailable, malfunctioning, or contraindicated? Medical Royal Colleges should be tracking this.

---

### 🟡 Training Material Currency

Is training content updated to reflect newly discovered failure modes from operational monitoring? Static training that doesn't incorporate lessons from incidents misses opportunities to prevent recurrence.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Standard training governance |

**Why this tier?**

> Operational governance metric. Should be tracked as part of incident-to-training feedback loop.

**Formal Definition**

```
Training Currency = days since last update of training materials. Coverage of recent failure modes: |recent_failure_modes_covered_in_training| / |recent_failure_modes_identified|. Target: training updated within 90 days of any new failure mode discovery.
```

**Limitations**

> Requires connection between operational monitoring and training update process — often disconnected.

**Novel Thinking / Implications**

> 💡 Training that doesn't evolve with operational experience is a missed opportunity. When a new failure mode is discovered (e.g. systematic omission of safety-netting in a particular context), the training should be updated within weeks, not years.

---

## Vendor Transparency & Contractual

*Whether vendors provide the access, telemetry, and transparency needed for independent assurance. The meta-prerequisite for most other metrics.*

**Tier breakdown**: 🟢 3 Tier 1 · 🟡 4 Tier 2 · 🔵 1 Tier 3

### 🟢 Model Change Notification Compliance

Whether the vendor notifies deployers of model updates before deployment, with sufficient detail to assess impact. Stanford framework finding: 'many vendors do not yet provide the access or telemetry necessary.'

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Stanford monitoring framework; three-layer surveillance model |

**Why this tier?**

> Should be a contractual requirement in NHS procurement. The three-layer surveillance model depends on it. Without vendor notification, governance is reactive.

**Formal Definition**

```
Compliance rate = |updates_notified_before_deployment| / |total_updates_deployed|. Notification quality: must include (a) what changed, (b) expected impact on outputs, (c) validation results on clinical benchmarks. Lead time: minimum 14 days before production deployment for major updates.
```

**References**

- **Stanford**: [Keyes et al. (2025) — Stanford monitoring framework](https://arxiv.org/abs/2512.09048)

**Limitations**

> Vendor compliance is only verifiable if independent monitoring can detect undisclosed model changes — which requires model version tracking infrastructure.

**Novel Thinking / Implications**

> 💡 This should be a contractual requirement in NHS procurement, not a voluntary practice. The three-layer surveillance model depends on it: national detection → regional evaluation → local monitoring. Without vendor notification, the entire surveillance chain is reactive rather than proactive.

---

### 🟡 Telemetry Provision Completeness

Whether the vendor provides the operational data needed for deployer-side monitoring: per-inference logging, confidence scores, model version per output, intermediate outputs for error attribution, and demographic performance data.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Stanford monitoring framework; identified as prerequisite for most continuous monitoring metrics |

**Why this tier?**

> The meta-prerequisite: without adequate telemetry, most continuous monitoring metrics are unmeasurable. Should be a procurement gate.

**Formal Definition**

```
Completeness = |telemetry_fields_provided| / |telemetry_fields_required|. Required fields: model_version, inference_timestamp, processing_latency, confidence_scores, token_count, error_flags. Desired: intermediate_outputs, demographic_performance, edit_pattern_data. Track provision consistency (uptime of telemetry feed).
```

**References**

- **Stanford**: ['Many vendors do not yet provide the access or telemetry necessary'](https://arxiv.org/abs/2512.09048)

**Limitations**

> Vendors may resist due to commercial sensitivity or technical cost. Telemetry provision must be contractually specified — voluntary provision is unreliable.

**Novel Thinking / Implications**

> 💡 This is the meta-metric: without adequate telemetry, most other continuous monitoring metrics are unmeasurable. Telemetry provision completeness should be a procurement gate — if a vendor cannot provide minimum telemetry, the system cannot be governed, and deployment should not proceed.

---

### 🔵 Benchmark & Evaluation Data Accessibility

Whether the vendor provides access to benchmarking infrastructure: test datasets, evaluation scripts, baseline results, and the ability for deployers to run independent evaluations.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Proposed — vendors currently self-evaluate with proprietary benchmarks |

**Why this tier?**

> Aspirational. Vendors self-evaluate on proprietary benchmarks. National NHS AVT benchmark suite would transform assurance but doesn't yet exist.

**Formal Definition**

```
Accessibility score across dimensions: (a) test dataset availability, (b) evaluation script reproducibility, (c) baseline result transparency, (d) deployer ability to run independent benchmarks, (e) third-party audit access. Binary per dimension; composite = sum/5.
```

**Limitations**

> Vendors argue test datasets contain proprietary or sensitive data. Standardised NHS-specific benchmarks don't yet exist. Third-party evaluation infrastructure requires investment.

**Novel Thinking / Implications**

> 💡 The fundamental transparency problem: vendors evaluate their own systems on their own benchmarks and report their own results. Independent evaluation requires benchmark accessibility. A national NHS AVT benchmark suite — with standardised test encounters, ground truth annotations, and evaluation scripts — would transform the assurance landscape from vendor self-assessment to independent verification.

---

### 🟡 Audit Trail Completeness

Whether the system maintains a complete, tamper-evident audit trail from audio input to EPR output — sufficient for retrospective incident investigation, complaint resolution, and regulatory inspection.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Clinical record governance requirements; applied to AI-generated documentation |

**Why this tier?**

> Governance requirement for retrospective investigation. Must balance investigability with data minimisation. Should be specified at procurement.

**Formal Definition**

```
Completeness = audit trail covers all stages (audio capture → ASR → diarisation → summarisation → coding → write-back → clinician review → approval) with timestamps, versions, and actor identification at each stage. Tamper evidence: cryptographic hashing or append-only logging. Retention: aligned with clinical record retention (minimum 8 years, 25 years for paediatrics).
```

**Limitations**

> Audit trail retention conflicts with data minimisation (UK GDPR). Retaining intermediate outputs for 8+ years is a significant storage and privacy commitment. Must balance investigability with minimisation.

**Novel Thinking / Implications**

> 💡 If a patient safety incident occurs 5 years after an AVT-generated note was approved, can the investigation reconstruct what happened? Without an audit trail covering the full pipeline, the answer is no. But retaining full audio for 8 years raises profound privacy questions. The governance challenge is defining what must be retained (metadata, version IDs, edit history) vs what should be deleted (raw audio, full transcript).

---

### 🟢 Incident Disclosure Compliance

Does the vendor disclose security incidents, model failures, and known issues to deployers in a timely manner? Includes both incidents at the vendor and incidents discovered at other deployer sites that may affect this deployer.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard security incident disclosure practice |

**Why this tier?**

> Should be a contractual requirement. Without timely incident disclosure, deployers cannot respond to vendor-side security issues.

**Formal Definition**

```
Disclosure Timeliness = t_disclosed - t_incident_known_by_vendor. Disclosure Completeness = |required_information_provided| / |required_information_categories|. Required: incident description, affected functionality, mitigation, recommended actions.
```

**Limitations**

> Vendor incentives often favour minimising disclosure. Requires contractual specification.

**Novel Thinking / Implications**

> 💡 When a security incident occurs at the vendor (e.g. the Mindgard jailbreak disclosures), affected deployers need to know quickly to assess their own exposure. Vendors often delay disclosure or provide minimal information. Contractual specification of disclosure timeframes and content is necessary.

---

### 🟡 Exit & Data Portability Provisions

When a deployer terminates their contract, can they export their data, audit trails, and configurations in usable formats? Vendor lock-in is a governance risk that affects switching costs and competitive procurement.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard procurement practice; lock-in risk analysis |

**Why this tier?**

> Procurement assessment. Important for avoiding lock-in but not safety-critical.

**Formal Definition**

```
Portability assessed across: (1) Patient data export (audio, transcripts, notes); (2) Audit trail export; (3) Configuration/template export; (4) Quality metrics history; (5) Format usability (open formats vs proprietary). Each binary; composite score.
```

**Limitations**

> Vendor incentives oppose portability. Often only addressed in contract negotiations, not standard offerings.

**Novel Thinking / Implications**

> 💡 The lock-in problem: once a practice has years of AVT data in one vendor's system, switching becomes prohibitive. Exit provisions must be specified at procurement, not discovered when termination is needed. Should be a procurement requirement.

---

### 🟢 Sub-Processor Transparency

Does the vendor disclose all third parties with access to data: cloud providers, model providers, annotation services, support contractors? UK GDPR Article 28 requires this. Each sub-processor is a potential data exposure point.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | UK GDPR Article 28 |

**Why this tier?**

> Legal compliance requirement under UK GDPR Article 28. Must be assessed at procurement and monitored for changes.

**Formal Definition**

```
Audit vendor's sub-processor list against actual data access. Completeness = |disclosed_subprocessors| / |actual_subprocessors|. Verification: review data flow diagrams, cloud architecture, support contracts. Each sub-processor should have its own data protection assessment.
```

**References**

- **UK GDPR**: UK GDPR Article 28 — processor obligations including sub-processor disclosure

**Limitations**

> Vendors often have complex, evolving sub-processor arrangements. Disclosure may not be complete or up-to-date.

**Novel Thinking / Implications**

> 💡 Each sub-processor is a data processing entity that must comply with UK GDPR. If the vendor uses an undisclosed sub-processor (e.g. an offshore annotation service), this is both a compliance failure and a potential security risk. Disclosure should be a contractual requirement with notification obligations for changes.

---

### 🟡 Intermediate Output Access

Whether the vendor provides contractual access to intermediate pipeline outputs — the raw transcript, the diarised transcript, the pre-coding summary, the model-internal confidence scores — rather than exposing only the final note. Prerequisite for the existing Error Attribution Analysis metric, and necessary for meaningful incident investigation. Without intermediate outputs, when an error is discovered in the final note, the investigation cannot determine which pipeline stage introduced it.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Prerequisite for existing Error Attribution Analysis metric; Stanford monitoring framework |

**Why this tier?**

> Procurement gate. Should be contractually specified. Required for any deployer intending to run Error Attribution Analysis, Chain of Custody traces, or Safety-Critical Information Chain of Custody (which is Tier 2 in the existing taxonomy but depends on intermediate output access to be executable).

**Formal Definition**

```
Access assessed across stages: (1) raw ASR transcript; (2) diarised transcript with speaker labels; (3) pre-summarisation processing outputs; (4) generated summary before coding; (5) coding suggestions before selection; (6) final output; (7) model confidence scores per stage. Access granularity: on-demand for individual encounters (required for incident investigation); bulk export for audit (required for Error Attribution Analysis); real-time streaming (optional, useful for monitoring). Binary per stage; target is full access to stages 1–6 on demand, with confidence scores (7) as advanced capability.
```

**Limitations**

> Vendors resist intermediate output access on commercial grounds — the intermediate outputs reveal pipeline architecture and model choices. Contractual access may be granted at high cost or with usage restrictions. Without independent verification, deployers cannot confirm that the "intermediate outputs" provided are authentic rather than reconstructions.

**Novel Thinking / Implications**

> 💡 Many of the highest-value metrics in this taxonomy — Error Attribution Analysis, Source-to-Record Concordance, Safety-Critical Information Chain of Custody, Error Cascade Analysis — depend on intermediate output access that vendors rarely provide. Making this a procurement gate creates pressure for vendors to either provide access or compete on terms with those who do. Without contractual intermediate output access, most sophisticated assurance metrics are theoretical rather than operational.

---

# Part F — Evaluation Science

## Meta-evaluation

*Are we measuring what matters? Structural critique of proximal vs distal outcomes and evaluation science itself.*

**Tier breakdown**: 🟡 1 Tier 2 · 🔵 6 Tier 3

### 🔵 Proximal vs Distal Outcome Distinction

The most important structural critique: measuring easy things and assuming they correlate with hard things. Require causal logic models.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | National Body, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Source** | Coiera & Fraile-Navarro 2026; NIHR RSET |

**Why this tier?**

> Structural critique of the evaluation field. Not a metric to implement but a framework for assessing all other metrics. National/academic responsibility.

**Formal Definition**

```
Proximal P = {WER, edit_rate, doc_time}. Distal D = {safety events, care quality, patient outcomes}. For each pᵢ, require causal model: pᵢ → [mechanism] → dⱼ with evidence. Burden on vendors/deployers to demonstrate P→D.
```

**References**

- **Editorial**: Coiera & Fraile-Navarro (2026) — JMIR Med Inform
- **RSET**: NIHR RSET Phase 1

**Limitations**

> Distal outcomes slow to manifest, hard to attribute.

**Novel Thinking / Implications**

> 💡 National evaluation standard should require explicit causal logic models with burden of proof on vendors.

---

### 🔵 Inter-Rater Reliability Baseline

Clinician agreement ceiling. VeriFact exceeds it (92.7% vs 88.5%). When automated metrics beat humans, what does that mean?

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Academic |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | VeriFact; MedHELM |

**Why this tier?**

> Research calibration baseline. Essential for interpreting automated metrics but an academic activity, not a deployer responsibility.

**Formal Definition**

```
Cohen's κ (k=2) or Fleiss' κ (k>2). ICC(2,1) for continuous ratings. VeriFact: 92.7% vs 88.5% inter-clinician. MedHELM: ICC 0.47 vs 0.43.
```

**References**

- **VeriFact**: [Chung et al. (2025)](https://ai.nejm.org/doi/full/10.1056/AIdbp2500418)
- **MedHELM**: [Bedi et al. (2025)](https://arxiv.org/abs/2505.23802)

**Limitations**

> Clinicians don't agree with each other. Any metric inherits this ceiling.

**Novel Thinking / Implications**

> 💡 When automated metric exceeds inter-clinician agreement: better than humans, or systematically biased in a correlated way?

---

### 🔵 Metric Interaction Analysis

Do the metrics in the taxonomy correlate or conflict? A system optimised for low edit rate might achieve it through over-summarisation that increases omission rate. Multi-metric monitoring requires understanding interactions.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | National Body, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Multi-metric evaluation literature |

**Why this tier?**

> Research-grade meta-analysis. National body responsibility.

**Formal Definition**

```
For each pair of metrics (m1, m2): compute correlation across deployments. Identify: (1) reinforcing pairs (improving both); (2) trade-off pairs (optimising one degrades the other); (3) confounded pairs (apparent correlation but distinct causes).
```

**Limitations**

> Requires data across multiple deployments to identify systematic interactions. Single-deployer analysis is underpowered.

**Novel Thinking / Implications**

> 💡 Without interaction analysis, governance can drive perverse outcomes. A practice told to reduce edit rate might pressure clinicians to edit less — but the AI hasn't improved, so the underlying error rate is unchanged. Edit rate goes down, hallucination rate goes up. This is the kind of failure that interaction analysis catches.

---

### 🟡 Goodhart's Law Monitoring

When a metric becomes a target, does it cease to be a good measure? Specifically tracking whether metrics are being gamed — optimised in ways that satisfy the metric without achieving the underlying goal.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Regional (ICB) |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Goodhart's Law applied to clinical AI metrics |

**Why this tier?**

> Important meta-governance check. Should be part of periodic audit to ensure metrics remain meaningful.

**Formal Definition**

```
For each Tier 1 metric: identify gaming strategies that could satisfy the metric without improving safety. Audit for evidence of gaming. Examples: edit rate gaming via no-op edits; review-before-signing gaming via auto-scroll; opt-out gaming via not informing patients.
```

**Limitations**

> Gaming detection is itself a research problem. Sophisticated gaming may be undetectable.

**Novel Thinking / Implications**

> 💡 Every metric in this taxonomy is potentially gameable. Edit rate can be gamed by trivial edits. Review-before-signing can be gamed by auto-scrolling. The question isn't whether gaming will happen but whether the governance framework detects and addresses it. Periodic audit should specifically look for gaming patterns, not just metric values.

---

### 🔵 Coverage Gap Analysis

What failure modes are not captured by any metric in the taxonomy? Periodic review of incidents to identify metric blindspots. The taxonomy itself must evolve as new failure modes emerge.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | National Body, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Standard safety engineering coverage analysis |

**Why this tier?**

> Meta-governance responsibility. National body should maintain the taxonomy as new failure modes emerge.

**Formal Definition**

```
For each incident or near-miss: identify which metrics would have detected it. Coverage Gap = |incidents_undetected_by_taxonomy| / |total_incidents|. Drives taxonomy evolution: gaps indicate new metrics needed.
```

**Limitations**

> Requires structured incident analysis and taxonomy maintenance process.

**Novel Thinking / Implications**

> 💡 The taxonomy is not static. As AVT evolves and new failure modes emerge, the taxonomy must evolve to cover them. Coverage gap analysis is the mechanism for this evolution — every incident should prompt the question 'would our metrics have caught this?' If not, that's a gap to fill.

---

### 🔵 LLM-Judge Bias Quantification

Systematic measurement of known biases in LLM-as-a-Judge evaluation: position bias (prefers first response in pairwise comparison), verbosity bias (prefers longer responses), self-enhancement bias (prefers outputs from the same model family), and fine-grained scoring unreliability (inconsistent discrimination at high score ranges). Required for interpreting LLM-Judge metrics responsibly. The Croxford et al. 2025 study found GPT-o3-mini achieving ICC 0.818 with human evaluators on PDSQI-9 — but a separate Rwanda clinical LLM evaluation study found LLM judges correlated more strongly with non-expert than expert annotators, indicating that apparent reliability may reflect alignment with a particular class of evaluator rather than with ground truth.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Academic, National Body |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Croxford et al. 2025 (npj Digital Medicine); Rwanda clinical LLM evaluation study |

**Why this tier?**

> Research-grade meta-evaluation. Academic and national body responsibility. Not routinely performed but necessary for anyone relying on LLM-as-a-Judge outputs for safety-critical decisions.

**Formal Definition**

```
Bias tests: (1) Position bias — reverse pairwise ordering and measure agreement with original judgment (perfect judge = 100% consistency under reversal); (2) Verbosity bias — compare judgments on pairs matched on quality but varying in length; (3) Self-enhancement — test judge on outputs from its own model family vs other families; (4) Score range reliability — measure inter-rater agreement at high scores (e.g. 4 vs 5 on Likert) vs across full range. Composite: bias-adjusted reliability = raw reliability corrected for each bias type.
```

**Limitations**

> Bias testing requires carefully constructed adversarial test sets. Results don't transfer across judge models or domains. Bias adjustments are approximations, not corrections.

**Novel Thinking / Implications**

> 💡 The Rwanda finding is the uncomfortable one: LLM judges may correlate well with human evaluators while correlating poorly with ground truth. This is the worst failure mode for evaluation — apparent reliability that validates a biased assessment. Any deployment relying on LLM-as-a-Judge for safety decisions (not just for efficiency) needs to have run bias quantification and documented the residual uncertainty. Otherwise the high ICC number is theatrical rather than informative.

---

### 🔵 Automated-Human Metric Concordance

Systematic measurement of how well automated metrics correlate with expert human evaluation across deployments. Meta-metric that validates (or invalidates) the automated metrics themselves. Without concordance measurement, automated metrics are running on the assumption that they track what human experts would measure — but the ROUGE Kendall-Tau finding of 0.080 with human clinical judgment (Croxford et al. 2025) shows that assumption can be wildly wrong.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | National Body, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Source** | Standard meta-evaluation methodology; Croxford et al. 2025 (ROUGE Kendall-Tau 0.080) |

**Why this tier?**

> Meta-evaluation requiring paired automated and human assessment data. National evaluation programme responsibility. Establishes the evidence base for treating automated metrics as trustworthy proxies.

**Formal Definition**

```
For each automated metric m in deployed use: collect a sample of N encounters scored by both m and by expert human evaluators using a validated instrument (e.g. PDSQI-9, CREOLA taxonomy). Compute correlation (Pearson, Spearman, Kendall's tau). Concordance Threshold: metric is "adequate as proxy" only if correlation > 0.5. Metrics with correlation < 0.3 should not be used as standalone quality indicators regardless of technical sophistication. Report concordance per metric with confidence intervals.
```

**Limitations**

> Requires paired human-automated scoring, which is expensive. Inter-human agreement is itself imperfect, creating a ceiling on achievable concordance. Results may not transfer across deployment contexts (a metric that concords well in primary care may fail in secondary care).

**Novel Thinking / Implications**

> 💡 This is the metric that polices the other metrics. Without concordance data, the taxonomy's automated metrics are running on an unverified assumption that they measure what human experts measure. The ROUGE finding is the canonical example of that assumption failing — a metric in widespread use has essentially zero correlation with clinical judgment and is used anyway because it's easy to compute. Periodic concordance measurement should be a national evaluation programme responsibility, and any metric with concordance < 0.3 should be explicitly flagged in the taxonomy as inadequate as a standalone indicator.

---
