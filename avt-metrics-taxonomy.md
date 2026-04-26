# AVT Metrics Taxonomy

> **Draft - v3.5, 2026-04-25.** This taxonomy is under active review and has not yet been stakeholder-approved. Content, tier assignments, gap analysis, and cross-references may change before public release. It is shared openly so that early feedback can shape the content, but it should not yet be cited as a settled standard.

Comprehensive metrics for NHS ambient voice technology assurance - covering the full pipeline from audio capture to clinical record, with formal definitions, code snippets, responsible actors, tiered priority guidance, and novel proposals.

**216 metrics** across **20 groups**, organised in six parts. Includes 4 named metric families, 4 sub-clusters within existing groups, and 15 metrics carrying explicit underspecification warnings that flag specific measurement-science gaps in the published literature. Version 3 incorporates metrics responding to the January–March 2026 NHS guidance suite, the 2025–2026 evaluation science literature (SCRIBE, CREOLA, VeriFact, MedHELM, CHECK), and regulatory developments (FDA PCCP, EU AI Act high-risk provisions). v3.3 added an explicit [Outcomes Boundary](#outcomes-boundary) statement (this taxonomy assures deployment safety, not clinical-outcome validation) and a structured Reference Standard / Operational Specification / Threshold Guidance pattern with ⚠️ Provenance preludes on nine Tier 1 metrics. v3.4 extended the pattern to 13 Tier 1 metrics (adding the operational/proxy class), promoted the convention to machine-enforced via two new `audit.py` checks, and published the full TIGHT / LOOSE / SURROGATE classification of the remaining 30 Tier 1 metrics. v3.5 lands the two highest-value tightening waves identified in that classification: 8 compliance/governance core metrics (Wave 1) and 4 privacy-chain metrics (Wave 2). The pattern is now applied to **25 of 43 Tier 1 metrics**.

## How to Use This Taxonomy

This taxonomy is designed to serve multiple audiences - from a practice CSO deploying their first AVT system to a national body designing evaluation infrastructure. The tiering system, cadence labels, and responsible actor assignments are designed to help each reader find the metrics that are relevant, actionable, and appropriately prioritised for their role.

### Priority Tiers

Each metric is assigned to one of three priority tiers. The tier reflects a composite judgement across three dimensions: how consequential the metric is for patient safety, whether it is measurable today with existing tools and data, and what governance burden it imposes on the responsible actor. A metric can be critically important but placed in Tier 3 because the infrastructure to measure it does not yet exist - the tier reflects actionability, not importance.

**🟢 Tier 1 - Minimum Viable Assurance** (43 metrics)

The smallest set of metrics that a deployer cannot responsibly skip. Every metric in Tier 1 meets all three criteria: it addresses a safety-critical or governance-essential function, it is measurable today by the responsible actor without requiring infrastructure that doesn't yet exist, and the burden of measurement is proportionate to the risk it monitors. A deployer operating AVT without measuring these metrics is operating without adequate governance - regardless of the vendor's own quality claims.

**🟡 Tier 2 - Recommended Assurance** (92 metrics)

What a deployer or regional body should measure given reasonable governance capacity and vendor cooperation. Tier 2 metrics are important for comprehensive assurance but either require some vendor cooperation that may need contractual enforcement, involve more resource-intensive measurement methods, or provide granularity that strengthens but is not strictly essential for basic safe operation.

**🔵 Tier 3 - Advanced / Research** (79 metrics)

Metrics that are important for advancing the field but are not actionable at individual deployer level today. Tier 3 metrics fall into this category for one of three reasons: they require national infrastructure that hasn't been built, they require research methods not yet scalable to routine deployment, or they are vendor-proprietary approaches that inform what a national standard should require but cannot be independently replicated. Tier 3 is not 'unimportant' - several Tier 3 metrics address the most fundamental questions about AVT safety. They are Tier 3 because the answer to 'can a CSO do this tomorrow?' is currently no.

### Measurement Cadence

Each metric carries a cadence label indicating how often it should be measured:

**🚪 One-off gate (pre-deployment)** - measured once before go-live as an acceptance criterion. Includes hardware validation, write-back fidelity testing, acoustic environment profiling, and pre-deployment benchmarks. Gate metrics must pass before the system enters clinical use. Some should be re-tested when significant changes occur (new EPR version, hardware change, model update), but they are not continuous monitoring requirements.

**📡 Continuous** - measured on an ongoing basis during operational use, ideally automated. Includes edit rate, time-to-sign, system availability, integration error rate, model version tracking, and the automated self-consistency checks. Continuous metrics should feed into dashboards visible to the clinical lead and CSO. Many can be derived from EPR workflow telemetry without additional clinical effort.

**🔄 Periodic audit** - measured at defined intervals through deliberate assessment activity. Includes hallucination/omission rate audits, error injection testing (quarterly), trust calibration surveys (annually), demographic WER re-testing, and the safety-critical chain of custody trace. Periodic audits require protected time and clinical resource - they are the most expensive cadence and should be scheduled in advance.

The cadence and tier interact: a Tier 1 continuous metric (edit rate) is low-burden and high-value - it should be running from Day Zero. A Tier 2 periodic metric (error injection audit) is higher-burden but provides uniquely valuable data - it should be scheduled quarterly once the system is stable. A Tier 3 periodic metric (clinical decision equivalence) is too resource-intensive for routine deployment but should be performed by national evaluation programmes.

### Responsible Actors

Each metric identifies who should measure it. The same metric may appear under multiple actors with different roles:

**Vendor** - responsible for pre-deployment benchmarking, continuous system telemetry, model version transparency, and security testing. Vendors control the data and infrastructure for many metrics that deployers cannot independently assess (WER, DER, demographic disaggregation, adversarial robustness). Vendor-side metrics should be contractually specified at procurement.

**Deployer** (practice, trust, or provider) - responsible for operational monitoring that occurs at the point of clinical use: edit rates, review behaviour, patient opt-out, training compliance, and periodic clinical note audits. Deployers are the primary actor for human factors metrics because these can only be measured where the human-AI interaction occurs.

**Regional (ICB)** - responsible for cross-practice comparison, deployment equity monitoring, coding drift detection, and CSO capacity oversight. The regional tier exists because some metrics only become meaningful when aggregated across multiple deployer sites - cross-practice variance is invisible to any individual practice.

**National Body** - responsible for infrastructure that enables everyone else's metrics: establishing evaluation standards, creating independent benchmark datasets, defining LFPSE reporting categories, and funding national evaluation programmes. Many Tier 3 metrics would move to Tier 2 or Tier 1 if national infrastructure existed.

**Academic** - responsible for developing and validating new metrics, conducting the resource-intensive evaluations (clinical decision equivalence, chilling effect, skill attenuation), and providing independent evidence that is not conflicted by vendor or deployer interests.

A metric listed under 'Vendor, Deployer' typically means the vendor must provide the data or infrastructure, and the deployer must use it for governance - for example, model version tracking requires the vendor to log versions but the deployer to monitor for changes and trigger re-evaluation.

### Reference IDs

Each metric carries a unique reference ID in the format `{Part}.{Group}-{Number}` - for example, `TP.AC-1` is the first metric in Audio Capture within The Technical Pipeline. Reference IDs appear in both the metric heading and the dimensions table.

**Part abbreviations:**

| Abbreviation | Part |
|-------------|------|
| TP | The Technical Pipeline |
| PI | Pipeline Interactions |
| HL | The Human Layer |
| IO | Impact & Outcomes |
| GV | System Governance |
| ES | Evaluation Science |

**Group abbreviations:**

| Abbreviation | Group | Part |
|-------------|-------|------|
| AC | Audio Capture & Environment | TP |
| ASR | ASR / Transcription | TP |
| DI | Diarisation | TP |
| SN | Summarisation / NLP | TP |
| CC | Clinical Coding | TP |
| WB | EPR Write-back | TP |
| PP | Partial-Pipeline | PI |
| E2E | End-to-End Pipeline | PI |
| HF | Human Factors & Workflow | HL |
| PX | Patient Experience | IO |
| FE | Fairness & Equity | IO |
| SG | Safety & Governance | GV |
| CR | NHS Compliance & Regulatory | GV |
| SC | Security & Adversarial Robustness | GV |
| PD | Privacy & Data Governance | GV |
| OP | Operational | GV |
| EN | Environmental & Sustainability | GV |
| TC | Training & Competency | GV |
| VT | Vendor Transparency & Contractual | GV |
| ME | Meta-evaluation | ES |

### Tightened Tier 1 metrics (Reference Standard / Operational Specification / Threshold Guidance)

A subset of Tier 1 metrics carry three additional sub-blocks beyond the standard Formal Definition: **Reference Standard** (what counts as ground truth and how reliability is established), **Operational Specification** (concrete decisions about measurement window, population, mandatory breakdowns, and aggregation rule), and **Threshold Guidance** (pre-deployment gate, continuous-monitoring alert, pause / escalation trigger). Where a metric carries these sub-blocks, the Operational Specification is what your vendor must comply with at procurement, and the Threshold Guidance is what triggers escalation post-deployment.

Each Threshold Guidance block opens with a ⚠️ **Provenance** line distinguishing thresholds **derived from a cited source** (e.g. NAS Day Zero SPI, UK GDPR storage limitation, NHSE IG guidance) from those **proposed in v3.3 as starting points**. The starting-point numbers are deliberate suggestions calibrated against the metric's clinical-safety logic, not externally validated values; they require local calibration against deployment context (specialty mix, consultation length, vendor reference dataset, DPIA risk appetite) before contractual use. Treat the Operational Specification as the structural commitment a vendor must meet; treat the Threshold Guidance numbers as the conversation starter, not the answer.

**Twenty-five Tier 1 metrics** carry this pattern as of v3.5 (up from 13 at v3.4): the v3.3 / v3.4 cohorts (safety, compliance, operational/proxy classes) plus v3.5's two waves — Wave 1 compliance/governance core (GV.CR-5 ICB Engagement, GV.CR-6 Clinical Safety Case, GV.CR-7 DPIA, GV.TC-1 Training Completion, GV.VT-1 Model Change Notification, GV.VT-5 Incident Disclosure, GV.VT-7 Sub-Processor Transparency, GV.SG-14 Near-Miss Reporting) and Wave 2 privacy-chain (GV.PD-2 Audio Time-to-Deletion, GV.PD-8 Consent Verification, GV.PD-10 SAR Fulfilment, GV.PD-11 Right to Erasure). The remaining 18 Tier 1 metrics fall into three groups per `archive/v3.3-tier1-classification.md`: 8 already classified TIGHT (no tightening planned — the pattern would be structural cleanup not substance), 6 candidates for v3.6+ pipeline narrow tightening (TP.ASR-12, TP.ASR-13, TP.WB-2, TP.WB-3, TP.WB-4, TP.SN-20), and 5 deferred-pattern-may-not-fit metrics (GV.OP-6, GV.SG-9, GV.SG-11, GV.SG-13, HL.HF-3). The current tightening status is auto-emitted by `taxonomy/audit.py` — rely on the audit output rather than this prose for current state.

### Adapting to Local Context

Tier assignments reflect a general assessment of priority and actionability. Local context should adjust them:

A practice with a high proportion of EAL (English as Additional Language) patients should treat demographic-disaggregated WER as Tier 1 rather than Tier 2 - the equity risk is elevated for their population. A practice using AVT for multi-party consultations (interpreter-mediated, family present) should treat multi-party robustness as Tier 1 because they are routinely operating in a scenario most systems are not validated for. A practice where clinicians have been customising prompt templates should treat template underspecification and template injection vulnerability as Tier 1 because the safety case may have been invalidated by modifications. An ICB with AVT deployed across practices of varying digital maturity should prioritise cross-practice variance and deployment equity.

The principle is: if a Tier 2 or Tier 3 metric addresses a risk that is elevated in your specific context, promote it. The tiers are a starting point, not a ceiling.

A trust with multiple AVT platforms deployed across different services should prioritise Cross-Platform Fairness Consistency as Tier 1 rather than Tier 3 - the fairness concern of different patients receiving different documentation quality depending on which service happens to use which vendor is elevated for multi-platform deployments even where each platform individually performs acceptably on single-axis fairness metrics. For an integrated care system with genuinely uniform platform deployment this metric is Tier 3; for one with a mixed AVT portfolio it is Tier 1.

### ⚠️ Field-wide resource constraint

> **Only two public benchmark datasets exist for ambient scribe evaluation: ACI Bench and PriMock.** This is not a minor inconvenience. It is the single biggest structural limitation on the operationalisation of nearly every metric in this taxonomy.
>
> Inter-rater reliability is rarely reported in published AVT evaluation studies, and where it is reported, clinical experts show significant disagreement - which means the notion of a stable "gold standard" against which to measure automated metrics is itself empirically fragile. A metric that claims high correlation with expert judgment can only be as reliable as the experts themselves are with each other, and current evidence suggests that ceiling is lower than published figures imply.
>
> The practical consequences for readers of this taxonomy are three-fold:
>
> **First, cross-vendor comparisons are usually not what they appear to be.** When two vendors both claim "95% M-WER" or "97% confabulation detection", they have almost certainly used different reference datasets, different significance ontologies, different inter-rater reliability thresholds, and different evaluation protocols. Direct comparison is not meaningful. The honest position is that procurement decisions based on vendor-reported performance metrics are currently closer to vibes-based assessment than to scientific comparison - and making that visible is part of what this taxonomy is for.
>
> **Second, the field-wide cost of every unvalidated metric is high.** Because there is no shared infrastructure for validation, every deployer or researcher who wants to use a metric meaningfully must rebuild the validation locally at their own cost. This creates enormous duplication and prevents any given metric from accumulating the cross-study evidence base that would make it trustworthy. ROUGE is the canonical example - it is used almost universally in clinical NLG evaluation despite published evidence that it correlates essentially not at all with clinical judgment, because the alternative would require locally-validated replacement metrics that nobody has resources to build.
>
> **Third, this is the single highest-leverage infrastructure intervention the NHS could make.** A national investment in shared clinical encounter datasets - with multi-annotator ground truth across specialties, accents, consultation types, and clinical complexity levels - would transform operationally what nearly every metric in this taxonomy can deliver. It would make vendor-reported metrics comparable for the first time. It would make validation studies tractable for small research groups. It would make the underspecification warnings throughout this taxonomy progressively less necessary as empirical evidence replaces informed speculation. There is no individual deployer, no individual vendor, and no individual academic group that can solve this at the scale required; it is a national body responsibility.
>
> **What deployers should do in the interim.** Until shared infrastructure exists, three working practices help make the limitation manageable rather than invisible: (1) always document the reference dataset, protocol, and inter-rater reliability conditions used when reporting any metric from this taxonomy; (2) treat cross-vendor comparison of self-reported metrics with explicit scepticism in procurement documentation; (3) prefer metrics in the taxonomy that are computable against the deployer's own data (Edit Rate, Time-to-Sign Distribution, the NHS Compliance metrics, Concept Extraction Concordance) over those that require reference datasets the deployer does not have, because the former are at least internally consistent even where cross-site comparison is difficult.

## Summary

### By Priority Tier

- **🟢 Tier 1 - Minimum Viable Assurance**: 43 metrics - what every deployer must measure to operate safely
- **🟡 Tier 2 - Recommended Assurance**: 94 metrics - recommended with reasonable governance capacity
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

## Tier 1 - Minimum Viable Assurance (Quick Reference)

The smallest set of metrics that a deployer cannot responsibly skip. All are measurable today with existing tools, data, and governance capacity.

**Tier 1 expanded substantially with the January–March 2026 NHS guidance suite.** Nine metrics moved into Tier 1 or were added as new Tier 1 entries reflecting compliance requirements that did not exist when the taxonomy was first drafted: the NHS Compliance & Regulatory cluster (Patient Dissent Recording, Verbal Notification, AI-Generated Content Labelling, AVT Supplier Registry, ICB Engagement, Clinical Safety Case, DPIA Template, Audio Time-to-Deletion, Transcript Retention) plus Code Hallucination Rate. For NHS deployers, the shape of Day Zero minimum assurance has changed materially since early-2025 vendor procurement; re-assess existing deployments against the expanded Tier 1 set.

### Tier 1 by Responsible Actor

**Deployer** (36 metrics)

- 🚪 **Microphone & Hardware Validation** - Basic pre-deployment hardware check. No AVT should go live without confirming capture hardware meets minimum specifications. Measurable today by any deployer.
- 🔄 **Hallucination Rate** ⚠️ - Core safety metric. NAS Day Zero SPI with <2% review and ≥5% pause thresholds. Every deployer must measure this through periodic clinical audit even if methodology is manual. *See underspecification warning in full entry - the term has no universally accepted definition and reported rates across the literature span 1–67% due largely to methodological differences. Document the specific subtype taxonomy and reference dataset used.*
- 🔄 **Omission Rate** - Arguably more dangerous than hallucination because omissions are invisible to the reviewer. Must be included in periodic clinical note audit alongside hallucination rate.
- 🔄 **Negation Handling Accuracy** - Safety-critical and well-documented LLM failure mode. Should be tested pre-deployment and periodically re-audited. Negation errors directly cause clinical harm.
- 🔄 **Uncertainty Marker Preservation** - Safety-critical: certainty inflation creates false diagnostic confidence in the record. Should be tested with adversarial cases as part of pre-deployment and periodic audit.
- 🚪 **Write-back Fidelity** - Highest-priority pre-deployment gate. A hallucinated allergy written to the EPR allergy field is a system-level safety failure that propagates to every future clinical decision. Must test per EPR system before go-live.
- 📡 **Integration Error Rate** - Standard integration monitoring. Automated, low-burden, and catches data pipeline failures that directly affect patient records.
- 🚪 **Field Mapping Accuracy** - Safety-critical pre-deployment test. Wrong-field placement of safety-critical content (allergies, medications) bypasses downstream safety mechanisms entirely.
- 🚪 **Update vs Append Behaviour** - Safety-critical pre-deployment test. Must be tested per EPR system before go-live. Overwriting existing safety-critical data is a patient safety event.
- 📡 **Edit Rate (% Notes Edited)** - Primary continuous complacency indicator. Deployer-measurable from EPR workflow data. NAS Day Zero SPI. The single most important human factors metric - trajectory reveals automation bias before incidents occur.
- 📡 **Review-Before-Signing Rate** - NAS Day Zero SPI with ≥95% threshold and <85% pause trigger. Deployer-measurable from EPR workflow telemetry. Directly monitors whether human oversight is functioning.
- 📡 **Time-to-Sign Distribution** - Deployer-measurable from EPR data. The tail of very-fast approvals (<5 seconds for complex notes) is the safety-critical population. Distribution analysis detects rubber-stamping patterns.
- 📡 **Safety Performance Indicators with Thresholds (DSCMS)** - The governance mechanism that converts metrics into action. Without pre-defined thresholds and escalation paths, metrics are information without teeth. Every Tier 1 metric needs an SPI wrapper.
- 📡 **Adverse Event / Incident Rate (LFPSE)** - Established national reporting. The ultimate lagging indicator - by the time this metric moves, harm has occurred. Needs dedicated LFPSE category for AI/AVT incidents.
- 📡 **Assurance Debt Accumulation Rate** - The honest governance metric. Every deployer will accumulate it. Making it visible, tracked, and managed prevents governance theatre.
- 📡 **Patient Opt-Out Rate** - Deployer-measurable from practice records. Low-burden continuous monitoring. Rising rates signal trust issues. Demographic disaggregation reveals consent model equity.
- 📡 **Documentation Time per Consultation** - Most widely measured benefit metric. Tells you nothing about safety but essential for demonstrating value proposition. Must be reported alongside quality metrics.
- 📡 **Adoption Rate & Selective Use Patterns** - Basic deployment tracking. Selective adoption patterns (avoiding AVT for complex cases) reveal practical system boundaries and are diagnostically valuable.
- 📡 **Near-Miss Reporting Rate** - Essential leading indicator. Should be Tier 1 because it's the early warning system that LFPSE is the lagging indicator of. Requires lightweight reporting infrastructure.
- 📡 **Hazard Log Completeness** - Regulatory requirement under DCB0129. Tier 1 because it's a compliance obligation, not a recommendation. Should be linked to operational monitoring.
- 📡 **Audio Retention Compliance** - UK GDPR storage limitation requirement. Non-compliance is a regulatory breach. Deployer must verify vendor retention practices align with DPIA.
- 📡 **Consent Verification Accuracy** - CQC Mythbuster 109 requires patients to be informed. Process compliance is measurable today. Understanding gap is harder but periodic survey is feasible.
- 🚪 **Cross-Border Data Transfer Compliance** - Legal compliance requirement. Must be assessed at procurement. Non-compliance is a regulatory breach.
- 🚪 **Subject Access Request Fulfilment** - Legal compliance requirement. Must be tested before go-live to confirm vendor supports SAR fulfilment workflow.
- 🚪 **Right to Erasure Compliance** - Legal compliance requirement. Must be tested before go-live to understand erasure scope and limitations.
- 📡 **Clinician Training Completion Rate** - Governance requirement. No clinician should use AVT without completing required training. Binary compliance metric - 100% is the only acceptable target.
- 📡 **Sub-Processor Transparency** - Legal compliance requirement under UK GDPR Article 28. Must be assessed at procurement and monitored for changes.
- 🚪 **AVT Supplier Registry Listing Verification** - Procurement gate with trivial verification cost. Must be confirmed before deployment and re-verified at contract renewal. Non-listed vendors should not be deployed.
- 🚪 **ICB Engagement Documentation** - Pre-deployment compliance gate under CIO/CCIO guidance v2. Documented evidence of regional engagement required before go-live. Absence indicates governance process breakdown.
- 🔄 **Clinical Safety Case Completeness** - DCB0129/0160 regulatory requirement. The 2025 FOI finding that many NHS digital health deployments lack compliant safety cases makes active monitoring essential, not optional.
- 🚪 **DPIA Template Completion Rate** - UK GDPR Article 35 legal requirement. Use of the NHSE March 2026 template enables cross-deployment comparison and ensures mandatory considerations aren't missed.
- 📡 **Patient Dissent Recording Rate** - Per-encounter compliance with the requirement to document and respect objections. Distinct from aggregate opt-out: opt-out is a blanket choice; dissent recording is procedural integrity at the point of care. Target 100%.
- 🔄 **Verbal Notification Compliance** - Proportion of AVT consultations where verbal notification was delivered at session start. The compliance metric behind the consent model. Periodic audit via patient survey or recording sample.
- 📡 **AI-Generated Content Labelling Compliance** - Every AI-generated entry must carry the mandatory SNOMED suffix. Automated verification is trivial; non-compliance breaks downstream audit and safety investigation.
- 📡 **Audio Time-to-Deletion** - NHSE IG guidance March 2026 requires deletion after summary sign-off. Measurement makes the policy operational rather than assertive. Must verify deletion in primary storage, caches, and backups.
- 📡 **Transcript Retention Compliance** - Parallel to audio deletion but often treated as less sensitive despite being higher-risk (structured, searchable, readily consumable). Explicit retention policy required; compliance measurable continuously.

**Vendor** (20 metrics)

- 🚪 **Hallucination-Under-Noise Rate** - Critical pre-deployment test. Whisper-based systems are documented to hallucinate from silence - this must be tested before clinical use. Tier 1 because the failure mode is well-documented and the test is straightforward.
- 🚪 **Numeric Accuracy** - Safety-critical and underspecified by current vendor reporting. Should be a Day Zero acceptance criterion. Numeric errors are disproportionately dangerous and should be reported separately from general WER.
- 🔄 **Hallucination Rate** ⚠️ - Core safety metric. NAS Day Zero SPI with <2% review and ≥5% pause thresholds. Every deployer must measure this through periodic clinical audit even if methodology is manual. *See underspecification warning in full entry - the term has no universally accepted definition and reported rates across the literature span 1–67% due largely to methodological differences. Document the specific subtype taxonomy and reference dataset used.*
- 🔄 **Omission Rate** - Arguably more dangerous than hallucination because omissions are invisible to the reviewer. Must be included in periodic clinical note audit alongside hallucination rate.
- 🔄 **Negation Handling Accuracy** - Safety-critical and well-documented LLM failure mode. Should be tested pre-deployment and periodically re-audited. Negation errors directly cause clinical harm.
- 🔄 **Uncertainty Marker Preservation** - Safety-critical: certainty inflation creates false diagnostic confidence in the record. Should be tested with adversarial cases as part of pre-deployment and periodic audit.
- 📡 **Code Hallucination Rate** - Zero-tolerance metric. Any non-zero rate indicates architectural failure in generation constraints. Vendor must demonstrate 0% pre-deployment and maintain continuous monitoring. A vendor who cannot achieve zero has unconstrained code generation, which is a procurement red flag.
- 🚪 **Write-back Fidelity** - Highest-priority pre-deployment gate. A hallucinated allergy written to the EPR allergy field is a system-level safety failure that propagates to every future clinical decision. Must test per EPR system before go-live.
- 📡 **Integration Error Rate** - Standard integration monitoring. Automated, low-burden, and catches data pipeline failures that directly affect patient records.
- 🚪 **Field Mapping Accuracy** - Safety-critical pre-deployment test. Wrong-field placement of safety-critical content (allergies, medications) bypasses downstream safety mechanisms entirely.
- 🚪 **Update vs Append Behaviour** - Safety-critical pre-deployment test. Must be tested per EPR system before go-live. Overwriting existing safety-critical data is a patient safety event.
- 📡 **Model Version Tracking** - Foundation for all continuous assurance. Without knowing which model version produced which output, no performance change is interpretable. Must be contractually required.
- 📡 **System Availability / Uptime** - Standard SLA monitoring. NAS Day Zero SPI (≥99.5%). Automated, zero-burden continuous metric.
- 📡 **Audio Retention Compliance** - UK GDPR storage limitation requirement. Non-compliance is a regulatory breach. Deployer must verify vendor retention practices align with DPIA.
- 🚪 **Cross-Border Data Transfer Compliance** - Legal compliance requirement. Must be assessed at procurement. Non-compliance is a regulatory breach.
- 🚪 **Subject Access Request Fulfilment** - Legal compliance requirement. Must be tested before go-live to confirm vendor supports SAR fulfilment workflow.
- 🚪 **Right to Erasure Compliance** - Legal compliance requirement. Must be tested before go-live to understand erasure scope and limitations.
- 📡 **Model Change Notification Compliance** - Should be a contractual requirement in NHS procurement. The three-layer surveillance model depends on it. Without vendor notification, governance is reactive.
- 📡 **Incident Disclosure Compliance** - Should be a contractual requirement. Without timely incident disclosure, deployers cannot respond to vendor-side security issues.
- 📡 **Sub-Processor Transparency** - Legal compliance requirement under UK GDPR Article 28. Must be assessed at procurement and monitored for changes.

**Regional (ICB)** (2 metrics)

- 📡 **Safety Performance Indicators with Thresholds (DSCMS)** - The governance mechanism that converts metrics into action. Without pre-defined thresholds and escalation paths, metrics are information without teeth. Every Tier 1 metric needs an SPI wrapper.
- 📡 **Assurance Debt Accumulation Rate** - The honest governance metric. Every deployer will accumulate it. Making it visible, tracked, and managed prevents governance theatre.

**National Body** (1 metrics)

- 📡 **Adverse Event / Incident Rate (LFPSE)** - Established national reporting. The ultimate lagging indicator - by the time this metric moves, harm has occurred. Needs dedicated LFPSE category for AI/AVT incidents.

---

## Contents

**Part A - The Technical Pipeline**

- [Audio Capture & Environment](#audio-capture-environment) (9 metrics - 1 Tier 1)
- [ASR / Transcription](#asr-transcription) (14 metrics - 2 Tier 1) *contains Clinical Transcription Accuracy and Demographic Equity Disaggregation families*
- [Diarisation](#diarisation) (9 metrics) *contains Conversation Analysis sub-cluster*
- [Summarisation / NLP](#summarisation-nlp) (24 metrics - 4 Tier 1) *contains Clinical Content Fidelity, Reference-Based Text Similarity, and Medication Safety Thread families*
- [Clinical Coding](#clinical-coding) (12 metrics - 1 Tier 1) *contains Coding Fidelity sub-cluster*
- [EPR Write-back](#epr-write-back) (7 metrics - 4 Tier 1) *contains Write-back Safety sub-cluster*

**Part B - Pipeline Interactions**

- [Partial-Pipeline](#partial-pipeline) (9 metrics)
- [End-to-End Pipeline](#end-to-end-pipeline) (12 metrics)

**Part C - The Human Layer**

- [Human Factors & Workflow](#human-factors-workflow) (19 metrics - 3 Tier 1) *contains Post-Generation Correction family and Sociotechnical & Resilience sub-cluster*

**Part D - Impact & Outcomes**

- [Patient Experience](#patient-experience) (10 metrics - 1 Tier 1) *contains Patient Clinical Outcomes sub-cluster*
- [Fairness & Equity](#fairness-equity) (8 metrics)

**Part E - System Governance**

- [Safety & Governance](#safety-governance) (17 metrics - 6 Tier 1) *contains Longitudinal Drift & Model Contamination sub-cluster*
- [NHS Compliance & Regulatory](#nhs-compliance-regulatory) (10 metrics - 7 Tier 1) *NEW GROUP*
- [Security & Adversarial Robustness](#security-adversarial-robustness) (11 metrics)
- [Privacy & Data Governance](#privacy-data-governance) (11 metrics - 7 Tier 1)
- [Operational](#operational) (9 metrics - 3 Tier 1)
- [Environmental & Sustainability](#environmental-sustainability) (3 metrics) *NEW GROUP*
- [Training & Competency](#training-competency) (5 metrics - 1 Tier 1)
- [Vendor Transparency & Contractual](#vendor-transparency-contractual) (8 metrics - 3 Tier 1)

**Part F - Evaluation Science**

- [Meta-evaluation](#meta-evaluation) (9 metrics) *contains the outcomes-evidence pair (ES.ME-8, ES.ME-9) that operationalises the [Outcomes Boundary](#outcomes-boundary)*

**Cross-cutting**

- [Applicability Classification](#applicability-classification) - which metrics are AVT-specific, which apply to any healthcare AI system
- [Standards Mapping](#standards-mapping) - assertion-level mapping to DTAC, DSPT, DCB0129/0160, NHS LLM Evaluation Framework, MHRA SaMD/AIaMD, NICE ESF, FHIR UK Core, CQC, PSIRF, PRSB, and Caldicott Principles
- [Responsible AI Lens](#responsible-ai-lens) - policy-intent view against the DSIT AI Playbook's 10 principles and the six Responsible AI ethical themes
- [Gaps & Proposed Metrics (Roadmap)](#gaps-proposed-metrics-roadmap) - consolidated register of 83 gap candidates from external coverage audits, standards mapping, and Responsible AI lens

*Several groups contain named metric families or sub-clusters. A **metric family** is a group of related metrics measuring facets of a shared construct (e.g. Clinical Content Fidelity groups Hallucination Rate, Omission Rate, Confabulation Detection, Negation Handling Accuracy, and Uncertainty Marker Preservation). Some families are cross-cutting, spanning multiple groups and pipeline layers (e.g. Medication Safety Thread spans Summarisation, Clinical Coding, and Patient Experience). Family framings appear before the first metric of each family and provide parent-construct context. A **sub-cluster** is a thematic grouping within a larger group (e.g. Conversation Analysis within Diarisation covers role identification, code-switching, turn-taking, and addressee recognition). Sub-clusters have italic introductory text before the first metric in the sub-cluster. Neither families nor sub-clusters require separate navigation - they are additive context within the existing group structure.*

---

## Applicability Classification

This section classifies each metric by whether it is specific to Ambient Voice Technology (AVT) or applicable to healthcare AI systems more broadly. The classification helps readers identify which parts of the taxonomy are transferable to other clinical AI contexts (diagnostic imaging AI, predictive analytics, clinical decision support) and which are meaningful only in the context of an audio-to-clinical-record pipeline.

### Classification Values

- **AVT-Specific** - the metric is meaningful only in the context of an audio capture, speech recognition, or speaker attribution pipeline. Removing the audio layer removes the need for the metric entirely. *Example: Signal-to-Noise Ratio Monitoring measures audio input quality - irrelevant to a text-based clinical AI system.*

- **General Healthcare AI** - the metric applies to any clinical AI system regardless of input modality. The definition, measurement method, and assurance question are independent of whether the system processes audio, text, images, or structured data. *Example: Consent Verification Accuracy applies equally to an ambient scribe, a diagnostic imaging AI, or an EHR predictive model.*

- **AVT-Contextualised** - the underlying concept is general (applicable to any clinical AI) but the specific definition, threshold, or measurement method in this taxonomy is tuned for AVT. Adapting the metric to another modality would require redefining the formal definition while preserving the assurance question. *Example: Hallucination Rate measures fabricated content in AI output - a general concern - but the formal definition here references transcript-to-note fidelity, speaker attribution errors, and audio-derived confabulation, which are AVT-specific failure modes.*

### Summary

| Classification | Count | Percentage |
|----------------|-------|------------|
| AVT-Specific | 48 | 22% |
| AVT-Contextualised | 77 | 36% |
| General Healthcare AI | 91 | 42% |
| **Total** | **216** | **100%** |

### By Part

| Part | AVT-Specific | AVT-Contextualised | General Healthcare AI | Total |
|------|-------------|--------------------|--------------------|-------|
| A - Technical Pipeline | 33 | 42 | 0 | 75 |
| B - Pipeline Interactions | 8 | 13 | 0 | 21 |
| C - The Human Layer | 0 | 16 | 3 | 19 |
| D - Impact & Outcomes | 1 | 6 | 11 | 18 |
| E - System Governance | 6 | 0 | 68 | 74 |
| F - Evaluation Science | 0 | 0 | 9 | 9 |
| **Total** | **48** | **77** | **91** | **216** |


### Full Classification

#### Part A - The Technical Pipeline

**Audio Capture & Environment** (9 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| TP.AC-1 | Signal-to-Noise Ratio (SNR) Monitoring | 🟡 Tier 2 | AVT-Specific |
| TP.AC-2 | Voice Activity Detection (VAD) Accuracy | 🔵 Tier 3 | AVT-Specific |
| TP.AC-3 | Acoustic Environment Profiling | 🟡 Tier 2 | AVT-Specific |
| TP.AC-4 | Bystander Voice Detection Rate | 🔵 Tier 3 | AVT-Specific |
| TP.AC-5 | Microphone & Hardware Validation | 🟢 Tier 1 | AVT-Specific |
| TP.AC-6 | Speaker Overlap Rate | 🔵 Tier 3 | AVT-Specific |
| TP.AC-7 | Audio Clipping / Saturation Rate | 🟡 Tier 2 | AVT-Specific |
| TP.AC-8 | Codec & Sampling Rate Compliance | 🟡 Tier 2 | AVT-Specific |
| TP.AC-9 | Microphone Drift Detection | 🔵 Tier 3 | AVT-Specific |

**ASR / Transcription** (14 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| TP.ASR-1 | Word Error Rate (WER) | 🟡 Tier 2 | AVT-Specific |
| TP.ASR-2 | Medical Word Error Rate (M-WER) | 🔵 Tier 3 | AVT-Specific |
| TP.ASR-3 | Clinical Keyword Error Rate (CK-ER) | 🔵 Tier 3 | AVT-Specific |
| TP.ASR-4 | Demographic-Disaggregated WER | 🟡 Tier 2 | AVT-Specific |
| TP.ASR-5 | Speaker-Stratified WER | 🔵 Tier 3 | AVT-Specific |
| TP.ASR-6 | Error Transmission Rate | 🟡 Tier 2 | AVT-Specific |
| TP.ASR-7 | Real-Time Factor (RTF) | 🟡 Tier 2 | AVT-Specific |
| TP.ASR-8 | Character Error Rate (CER) | 🟡 Tier 2 | AVT-Specific |
| TP.ASR-9 | Out-of-Vocabulary (OOV) Rate | 🟡 Tier 2 | AVT-Specific |
| TP.ASR-10 | ASR Confidence Calibration | 🟡 Tier 2 | AVT-Specific |
| TP.ASR-11 | ASR Confidence Exposure | 🟡 Tier 2 | AVT-Specific |
| TP.ASR-12 | Hallucination-Under-Noise Rate | 🟢 Tier 1 | AVT-Specific |
| TP.ASR-13 | Numeric Accuracy | 🟢 Tier 1 | AVT-Specific |
| TP.ASR-14 | Punctuation & Capitalisation Accuracy | 🔵 Tier 3 | AVT-Specific |

**Diarisation** (9 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| TP.DI-1 | Diarisation Error Rate (DER) | 🟡 Tier 2 | AVT-Specific |
| TP.DI-2 | Speaker Attribution Accuracy | 🟡 Tier 2 | AVT-Specific |
| TP.DI-3 | Speaker Count Accuracy | 🟡 Tier 2 | AVT-Specific |
| TP.DI-4 | Speaker Boundary Precision | 🔵 Tier 3 | AVT-Specific |
| TP.DI-5 | Speaker Role Identification F1 | 🟡 Tier 2 | AVT-Specific |
| TP.DI-6 | Code-Switching Detection Rate | 🟡 Tier 2 | AVT-Specific |
| TP.DI-7 | Turn-Taking Accuracy in Overlap | 🟡 Tier 2 | AVT-Specific |
| TP.DI-8 | Clinical-Perspective HEWER (cpHEWER) | 🔵 Tier 3 | AVT-Specific |
| TP.DI-9 | Addressee Recognition Accuracy | 🔵 Tier 3 | AVT-Specific |

**Summarisation / NLP** (24 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| TP.SN-1 | ROUGE Scores | 🟡 Tier 2 | AVT-Contextualised |
| TP.SN-2 | BERTScore | 🔵 Tier 3 | AVT-Contextualised |
| TP.SN-3 | PDSQI-9 (Physician Documentation Quality Instrument) | 🟡 Tier 2 | AVT-Contextualised |
| TP.SN-4 | CREOLA Error Taxonomy Scores | 🟡 Tier 2 | AVT-Contextualised |
| TP.SN-5 | Hallucination Rate | 🟢 Tier 1 | AVT-Contextualised |
| TP.SN-6 | Omission Rate | 🟢 Tier 1 | AVT-Contextualised |
| TP.SN-7 | Confabulation Detection (Support × Severity) | 🔵 Tier 3 | AVT-Contextualised |
| TP.SN-8 | VeriFact Factual Verification | 🔵 Tier 3 | AVT-Contextualised |
| TP.SN-9 | LLM-as-a-Judge (PDSQI-9 Proxy) | 🟡 Tier 2 | AVT-Contextualised |
| TP.SN-10 | MedHELM LLM-Jury | 🔵 Tier 3 | AVT-Contextualised |
| TP.SN-11 | MEDIC Cross-Examination | 🔵 Tier 3 | AVT-Contextualised |
| TP.SN-12 | Linked Evidence / Provenance Tracing | 🟡 Tier 2 | AVT-Contextualised |
| TP.SN-13 | SCRIBE Framework Composite | 🔵 Tier 3 | AVT-Specific |
| TP.SN-14 | Template Modification Underspecification Score | 🟡 Tier 2 | AVT-Contextualised |
| TP.SN-15 | Negation Handling Accuracy | 🟢 Tier 1 | AVT-Contextualised |
| TP.SN-16 | Temporal Accuracy | 🟡 Tier 2 | AVT-Contextualised |
| TP.SN-17 | Temporal Event Ordering Accuracy | 🟡 Tier 2 | AVT-Contextualised |
| TP.SN-18 | Quantifier Preservation | 🟡 Tier 2 | AVT-Contextualised |
| TP.SN-19 | Medication Attribute Extraction F1 | 🟡 Tier 2 | AVT-Contextualised |
| TP.SN-20 | Uncertainty Marker Preservation | 🟢 Tier 1 | AVT-Contextualised |
| TP.SN-21 | Medication Event Classification | 🟡 Tier 2 | AVT-Contextualised |
| TP.SN-22 | Style & Format Consistency | 🔵 Tier 3 | AVT-Contextualised |
| TP.SN-23 | Length Appropriateness | 🔵 Tier 3 | AVT-Contextualised |
| TP.SN-24 | Stigmatising Language Replication Rate | 🟡 Tier 2 | AVT-Contextualised |

**Clinical Coding** (12 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| TP.CC-1 | SNOMED Code Accuracy | 🟡 Tier 2 | AVT-Contextualised |
| TP.CC-2 | SNOMED CT Concept Mapping Accuracy | 🟡 Tier 2 | AVT-Contextualised |
| TP.CC-3 | ICD-10 / ICD-11 Full-Specificity Precision | 🟡 Tier 2 | AVT-Contextualised |
| TP.CC-4 | OPCS-4 Procedure Coding Accuracy | 🟡 Tier 2 | AVT-Contextualised |
| TP.CC-5 | dm+d Medication Coding Accuracy | 🟡 Tier 2 | AVT-Contextualised |
| TP.CC-6 | Code Hallucination Rate | 🟢 Tier 1 | AVT-Contextualised |
| TP.CC-7 | Coding Inflation Detection | 🟡 Tier 2 | AVT-Contextualised |
| TP.CC-8 | E/M Level Shift Monitoring | 🟡 Tier 2 | AVT-Contextualised |
| TP.CC-9 | Coding Equity Index | 🟡 Tier 2 | AVT-Contextualised |
| TP.CC-10 | wRVU / Tariff Impact Attribution | 🔵 Tier 3 | AVT-Contextualised |
| TP.CC-11 | Code Specificity Index | 🔵 Tier 3 | AVT-Contextualised |
| TP.CC-12 | Code Suggestion Latency | 🔵 Tier 3 | AVT-Contextualised |

**EPR Write-back** (7 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| TP.WB-1 | Write-back Fidelity | 🟢 Tier 1 | AVT-Contextualised |
| TP.WB-2 | Integration Error Rate | 🟢 Tier 1 | AVT-Contextualised |
| TP.WB-3 | Field Mapping Accuracy | 🟢 Tier 1 | AVT-Contextualised |
| TP.WB-4 | Update vs Append Behaviour | 🟢 Tier 1 | AVT-Contextualised |
| TP.WB-5 | Write-back Rollback Capability | 🟡 Tier 2 | AVT-Contextualised |
| TP.WB-6 | FHIR R4 Resource Conformance Rate | 🟡 Tier 2 | AVT-Contextualised |
| TP.WB-7 | openEHR Archetype Conformance | 🔵 Tier 3 | AVT-Contextualised |

#### Part B - Pipeline Interactions

**Partial-Pipeline** (9 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| PI.PP-1 | Speaker-Attributed Transcript Accuracy | 🔵 Tier 3 | AVT-Specific |
| PI.PP-2 | Multi-Party Conversation Robustness | 🟡 Tier 2 | AVT-Specific |
| PI.PP-3 | Information Extraction Yield | 🔵 Tier 3 | AVT-Contextualised |
| PI.PP-4 | Noise-to-Note Resilience | 🔵 Tier 3 | AVT-Specific |
| PI.PP-5 | Epistemic Status Preservation | 🔵 Tier 3 | AVT-Contextualised |
| PI.PP-6 | Diarisation-Stratified WER | 🔵 Tier 3 | AVT-Specific |
| PI.PP-7 | Concept Extraction Concordance | 🟡 Tier 2 | AVT-Contextualised |
| PI.PP-8 | End-of-Utterance Timing Accuracy | 🔵 Tier 3 | AVT-Specific |
| PI.PP-9 | Structured/Free-Text Consistency | 🟡 Tier 2 | AVT-Contextualised |

**End-to-End Pipeline** (12 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| PI.E2E-1 | Source-to-Record Concordance | 🔵 Tier 3 | AVT-Contextualised |
| PI.E2E-2 | Cumulative Information Yield | 🔵 Tier 3 | AVT-Contextualised |
| PI.E2E-3 | Error Propagation / Cascade Analysis | 🔵 Tier 3 | AVT-Specific |
| PI.E2E-4 | Safety-Critical Information Chain of Custody | 🟡 Tier 2 | AVT-Contextualised |
| PI.E2E-5 | Compound Demographic Performance | 🔵 Tier 3 | AVT-Contextualised |
| PI.E2E-6 | Semantic Drift Accumulation | 🔵 Tier 3 | AVT-Specific |
| PI.E2E-7 | Pipeline Non-Determinism / Reproducibility | 🟡 Tier 2 | AVT-Contextualised |
| PI.E2E-8 | Error Attribution Analysis | 🔵 Tier 3 | AVT-Contextualised |
| PI.E2E-9 | Clinical Decision Equivalence | 🔵 Tier 3 | AVT-Contextualised |
| PI.E2E-10 | Full-Pipeline Latency Budget | 🟡 Tier 2 | AVT-Contextualised |
| PI.E2E-11 | Pipeline Failure Recovery | 🟡 Tier 2 | AVT-Contextualised |
| PI.E2E-12 | Round-Trip Information Loss | 🔵 Tier 3 | AVT-Specific |

#### Part C - The Human Layer

**Human Factors & Workflow** (19 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| HL.HF-1 | Edit Rate (% Notes Edited) | 🟢 Tier 1 | AVT-Contextualised |
| HL.HF-2 | Edit Type Classification | 🟡 Tier 2 | AVT-Contextualised |
| HL.HF-3 | Review-Before-Signing Rate | 🟢 Tier 1 | AVT-Contextualised |
| HL.HF-4 | Time-to-Sign Distribution | 🟢 Tier 1 | AVT-Contextualised |
| HL.HF-5 | Edit-Pattern Monitoring at Scale | 🔵 Tier 3 | AVT-Contextualised |
| HL.HF-6 | Automation Bias Detection (Error Injection) | 🟡 Tier 2 | AVT-Contextualised |
| HL.HF-7 | Edit Location Distribution | 🟡 Tier 2 | AVT-Contextualised |
| HL.HF-8 | Trust Calibration Survey | 🟡 Tier 2 | AVT-Contextualised |
| HL.HF-9 | Re-record / Abandonment Rate | 🟡 Tier 2 | AVT-Contextualised |
| HL.HF-10 | Cognitive Load Assessment | 🔵 Tier 3 | AVT-Contextualised |
| HL.HF-11 | Inter-Clinician Edit Variance | 🔵 Tier 3 | AVT-Contextualised |
| HL.HF-12 | Clinical Documentation Skill Attenuation | 🔵 Tier 3 | AVT-Contextualised |
| HL.HF-13 | Cognitive Offloading Rate | 🔵 Tier 3 | AVT-Contextualised |
| HL.HF-14 | Trust Halo Decay Rate | 🔵 Tier 3 | AVT-Contextualised |
| HL.HF-15 | Note Review Fatigue Trajectory | 🔵 Tier 3 | AVT-Contextualised |
| HL.HF-16 | Work-as-Imagined vs Work-as-Done Gap | 🔵 Tier 3 | General Healthcare AI |
| HL.HF-17 | Verification Burden | 🟡 Tier 2 | AVT-Contextualised |
| HL.HF-18 | Resilience Capacities Assessment | 🔵 Tier 3 | General Healthcare AI |
| HL.HF-19 | AI-Off Performance Test | 🟡 Tier 2 | General Healthcare AI |


#### Part D - Impact & Outcomes

**Patient Experience** (10 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| IO.PX-1 | Patient Opt-Out Rate | 🟢 Tier 1 | AVT-Contextualised |
| IO.PX-2 | Patient-Perceived Accuracy | 🔵 Tier 3 | AVT-Contextualised |
| IO.PX-3 | Emotional Content Preservation | 🔵 Tier 3 | AVT-Contextualised |
| IO.PX-4 | Cultural & Linguistic Appropriateness | 🔵 Tier 3 | General Healthcare AI |
| IO.PX-5 | Chilling Effect Assessment | 🔵 Tier 3 | AVT-Contextualised |
| IO.PX-6 | Therapeutic Relationship Impact | 🔵 Tier 3 | AVT-Contextualised |
| IO.PX-7 | Full Attentiveness Rate | 🟡 Tier 2 | AVT-Contextualised |
| IO.PX-8 | Patient Comprehension of AI-Generated Summaries | 🔵 Tier 3 | General Healthcare AI |
| IO.PX-9 | Downstream Diagnostic Accuracy | 🔵 Tier 3 | General Healthcare AI |
| IO.PX-10 | Medication Error Rate Differential | 🔵 Tier 3 | General Healthcare AI |

**Fairness & Equity** (8 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| IO.FE-1 | Deployment Equity Index | 🟡 Tier 2 | General Healthcare AI |
| IO.FE-2 | Accent Taxonomy Standardisation | 🟡 Tier 2 | AVT-Specific |
| IO.FE-3 | Clinical Domain Performance Variance | 🟡 Tier 2 | General Healthcare AI |
| IO.FE-4 | Intersectional Performance | 🔵 Tier 3 | General Healthcare AI |
| IO.FE-5 | Intersectional Compound Fairness Score | 🔵 Tier 3 | General Healthcare AI |
| IO.FE-6 | Rare Presentation Handling | 🔵 Tier 3 | General Healthcare AI |
| IO.FE-7 | Health Literacy Performance Variation | 🔵 Tier 3 | General Healthcare AI |
| IO.FE-8 | Cross-Platform Fairness Consistency | 🔵 Tier 3 | General Healthcare AI |

#### Part E - System Governance

**Safety & Governance** (17 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| GV.SG-1 | Model Version Tracking | 🟢 Tier 1 | General Healthcare AI |
| GV.SG-2 | Model Update Impact Score | 🟡 Tier 2 | General Healthcare AI |
| GV.SG-3 | Performance Degradation Detection Latency | 🟡 Tier 2 | General Healthcare AI |
| GV.SG-4 | Retraining Trigger Threshold Specification | 🟡 Tier 2 | General Healthcare AI |
| GV.SG-5 | AI-Generated Data Contamination Rate | 🔵 Tier 3 | General Healthcare AI |
| GV.SG-6 | Concept Drift in Clinical Notes | 🔵 Tier 3 | General Healthcare AI |
| GV.SG-7 | Probabilistic Risk Quantification (P₁/P₂) | 🔵 Tier 3 | General Healthcare AI |
| GV.SG-8 | DeepScore (Defect-Free Rate) | 🔵 Tier 3 | General Healthcare AI |
| GV.SG-9 | Safety Performance Indicators with Thresholds (DSCMS) | 🟢 Tier 1 | General Healthcare AI |
| GV.SG-10 | Off-Label Use Detection Rate | 🟡 Tier 2 | General Healthcare AI |
| GV.SG-11 | Adverse Event / Incident Rate (LFPSE) | 🟢 Tier 1 | General Healthcare AI |
| GV.SG-12 | Cross-Practice Variance Coefficient | 🟡 Tier 2 | General Healthcare AI |
| GV.SG-13 | Assurance Debt Accumulation Rate | 🟢 Tier 1 | General Healthcare AI |
| GV.SG-14 | Near-Miss Reporting Rate | 🟢 Tier 1 | General Healthcare AI |
| GV.SG-15 | Time-to-Correct | 🟡 Tier 2 | General Healthcare AI |
| GV.SG-16 | SPI Escalation Response Time | 🟡 Tier 2 | General Healthcare AI |
| GV.SG-17 | Hazard Log Completeness | 🟢 Tier 1 | General Healthcare AI |

**NHS Compliance & Regulatory** (10 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| GV.CR-1 | Patient Dissent Recording Rate | 🟢 Tier 1 | General Healthcare AI |
| GV.CR-2 | Verbal Notification Compliance | 🟢 Tier 1 | General Healthcare AI |
| GV.CR-3 | AI-Generated Content Labelling Compliance | 🟢 Tier 1 | General Healthcare AI |
| GV.CR-4 | AVT Supplier Registry Listing Verification | 🟢 Tier 1 | AVT-Specific |
| GV.CR-5 | ICB Engagement Documentation | 🟢 Tier 1 | General Healthcare AI |
| GV.CR-6 | Clinical Safety Case Completeness | 🟢 Tier 1 | General Healthcare AI |
| GV.CR-7 | DPIA Template Completion Rate | 🟢 Tier 1 | General Healthcare AI |
| GV.CR-8 | DSPA Status | 🟡 Tier 2 | General Healthcare AI |
| GV.CR-9 | FDA PCCP-Equivalent Pre-Defined Acceptance Criteria | 🟡 Tier 2 | General Healthcare AI |
| GV.CR-10 | EU AI Act Event Logging Compliance | 🟡 Tier 2 | General Healthcare AI |

**Security & Adversarial Robustness** (11 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| GV.SC-1 | Prompt Injection Resistance Rate | 🟡 Tier 2 | General Healthcare AI |
| GV.SC-2 | Jailbreak Resistance Score | 🟡 Tier 2 | General Healthcare AI |
| GV.SC-3 | Adversarial Audio Detection Rate | 🔵 Tier 3 | AVT-Specific |
| GV.SC-4 | Data Poisoning Resilience | 🔵 Tier 3 | General Healthcare AI |
| GV.SC-5 | Output Safety Classifier Coverage | 🟡 Tier 2 | General Healthcare AI |
| GV.SC-6 | Template Injection Vulnerability Assessment | 🟡 Tier 2 | General Healthcare AI |
| GV.SC-7 | Voice Cloning / Deepfake Detection | 🔵 Tier 3 | AVT-Specific |
| GV.SC-8 | Side-Channel Data Leakage | 🟡 Tier 2 | General Healthcare AI |
| GV.SC-9 | Cross-Patient Information Leakage Rate | 🟡 Tier 2 | General Healthcare AI |
| GV.SC-10 | Clinician Identity Authentication | 🟡 Tier 2 | General Healthcare AI |
| GV.SC-11 | Membership Inference Attack AUC | 🔵 Tier 3 | General Healthcare AI |

**Privacy & Data Governance** (11 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| GV.PD-1 | Audio Retention Compliance | 🟢 Tier 1 | AVT-Specific |
| GV.PD-2 | Audio Time-to-Deletion | 🟢 Tier 1 | AVT-Specific |
| GV.PD-3 | Transcript Retention Compliance | 🟢 Tier 1 | AVT-Specific |
| GV.PD-4 | Data Minimisation Score | 🟡 Tier 2 | General Healthcare AI |
| GV.PD-5 | PII Extraction Attack Success Rate | 🟡 Tier 2 | General Healthcare AI |
| GV.PD-6 | Re-identification Risk Assessment | 🟡 Tier 2 | General Healthcare AI |
| GV.PD-7 | Training Data Inclusion Status | 🟡 Tier 2 | General Healthcare AI |
| GV.PD-8 | Consent Verification Accuracy | 🟢 Tier 1 | General Healthcare AI |
| GV.PD-9 | Cross-Border Data Transfer Compliance | 🟢 Tier 1 | General Healthcare AI |
| GV.PD-10 | Subject Access Request Fulfilment | 🟢 Tier 1 | General Healthcare AI |
| GV.PD-11 | Right to Erasure Compliance | 🟢 Tier 1 | General Healthcare AI |

**Operational** (9 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| GV.OP-1 | Documentation Time per Consultation | 🟢 Tier 1 | General Healthcare AI |
| GV.OP-2 | Pyjama Time / After-Hours EHR Use | 🟡 Tier 2 | General Healthcare AI |
| GV.OP-3 | Note Turnaround Time | 🟡 Tier 2 | General Healthcare AI |
| GV.OP-4 | Documentation Workload Composite | 🟡 Tier 2 | General Healthcare AI |
| GV.OP-5 | System Availability / Uptime | 🟢 Tier 1 | General Healthcare AI |
| GV.OP-6 | Adoption Rate & Selective Use Patterns | 🟢 Tier 1 | General Healthcare AI |
| GV.OP-7 | Cost per Consultation | 🟡 Tier 2 | General Healthcare AI |
| GV.OP-8 | Governance & Maintenance Burden | 🔵 Tier 3 | General Healthcare AI |
| GV.OP-9 | Training Time per Clinician | 🟡 Tier 2 | General Healthcare AI |

**Environmental & Sustainability** (3 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| GV.EN-1 | Energy Consumption per Clinical Note | 🔵 Tier 3 | General Healthcare AI |
| GV.EN-2 | Carbon Emissions per Inference | 🔵 Tier 3 | General Healthcare AI |
| GV.EN-3 | Water Consumption per Query | 🔵 Tier 3 | General Healthcare AI |

**Training & Competency** (5 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| GV.TC-1 | Clinician Training Completion Rate | 🟢 Tier 1 | General Healthcare AI |
| GV.TC-2 | Failure Mode Awareness Score | 🟡 Tier 2 | General Healthcare AI |
| GV.TC-3 | Refresher Training & CPD Compliance | 🟡 Tier 2 | General Healthcare AI |
| GV.TC-4 | Trainee Impact Assessment | 🔵 Tier 3 | General Healthcare AI |
| GV.TC-5 | Training Material Currency | 🟡 Tier 2 | General Healthcare AI |

**Vendor Transparency & Contractual** (8 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| GV.VT-1 | Model Change Notification Compliance | 🟢 Tier 1 | General Healthcare AI |
| GV.VT-2 | Telemetry Provision Completeness | 🟡 Tier 2 | General Healthcare AI |
| GV.VT-3 | Benchmark & Evaluation Data Accessibility | 🔵 Tier 3 | General Healthcare AI |
| GV.VT-4 | Audit Trail Completeness | 🟡 Tier 2 | General Healthcare AI |
| GV.VT-5 | Incident Disclosure Compliance | 🟢 Tier 1 | General Healthcare AI |
| GV.VT-6 | Exit & Data Portability Provisions | 🟡 Tier 2 | General Healthcare AI |
| GV.VT-7 | Sub-Processor Transparency | 🟢 Tier 1 | General Healthcare AI |
| GV.VT-8 | Intermediate Output Access | 🟡 Tier 2 | General Healthcare AI |

#### Part F - Evaluation Science

**Meta-evaluation** (9 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| ES.ME-1 | Proximal vs Distal Outcome Distinction | 🔵 Tier 3 | General Healthcare AI |
| ES.ME-2 | Inter-Rater Reliability Baseline | 🔵 Tier 3 | General Healthcare AI |
| ES.ME-3 | Metric Interaction Analysis | 🔵 Tier 3 | General Healthcare AI |
| ES.ME-4 | Goodhart's Law Monitoring | 🟡 Tier 2 | General Healthcare AI |
| ES.ME-5 | Coverage Gap Analysis | 🔵 Tier 3 | General Healthcare AI |
| ES.ME-6 | LLM-Judge Bias Quantification | 🔵 Tier 3 | General Healthcare AI |
| ES.ME-7 | Automated-Human Metric Concordance | 🔵 Tier 3 | General Healthcare AI |
| ES.ME-8 | Outcome Evidence Commitment Status | 🟡 Tier 2 | General Healthcare AI |
| ES.ME-9 | Causal Model Operationalisation | 🟡 Tier 2 | General Healthcare AI |

## Standards Mapping

This section maps the taxonomy's 214 metrics against twelve NHS/regulatory frameworks to help deployers, vendors, and assurance teams identify which metrics satisfy which compliance obligations. For each framework, individual criteria or assertions are mapped to specific taxonomy metrics.

Where a standard criterion has no corresponding taxonomy metric, this is flagged as a **gap**. Where the taxonomy provides coverage beyond the standard's scope, this is noted as **taxonomy extends**.

---

### DTAC (Digital Technology Assessment Criteria) v2.0

DTAC is the NHS assessment framework for digital health technologies. It has four assessed sections (C1–C4) and one comparative section (D1). DTAC v2.0 (February 2026) explicitly names Ambient Voice Technologies as potentially requiring additional assurance beyond DTAC.

#### C1 - Clinical Safety

| DTAC Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| C1.1.1 | Software / AI as Medical Device classification | *Process criterion - no metric equivalent; informs scope* | - |
| C1.2.2 | DCB0129 Clinical Risk Management compliance | Clinical Safety Case Completeness | 🟢 1 |
| C1.2.3 | Clinical risk management system detail | Hazard Log Completeness | 🟢 1 |
| C1.2.4 | Clinical Safety Case Report and Hazard Log | Clinical Safety Case Completeness, Hazard Log Completeness | 🟢 1 |
| C1.2.5 | Named Clinical Safety Officer | *Process criterion - no metric equivalent* | - |

**Taxonomy extends:** Safety Performance Indicators with Thresholds (DSCMS), Adverse Event / Incident Rate (LFPSE), Near-Miss Reporting Rate, Probabilistic Risk Quantification (P₁/P₂) - the taxonomy provides ongoing safety monitoring metrics that DTAC does not assess.

#### C2 - Data Protection

| DTAC Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| C2.1 | DSPT compliance | DSPA Status | 🟡 2 |
| C2.2.1 | ICO registration | *Process criterion - no metric equivalent* | - |
| C2.2.2 | Data Protection Impact Assessment | DPIA Template Completion Rate | 🟢 1 |
| C2.2.3 | Transparency information / privacy notice | Patient Dissent Recording Rate, Verbal Notification Compliance | 🟢 1 |
| C2.2.4 | Terms and conditions | *Process criterion - no metric equivalent* | - |
| C2.2.5 | Data storage and processing location | Cross-Border Data Transfer Compliance | 🟢 1 |
| C2.2.6 | Cross-border legislative compliance | Cross-Border Data Transfer Compliance | 🟢 1 |

**Taxonomy extends:** Audio Retention Compliance, Audio Time-to-Deletion, Transcript Retention Compliance, Data Minimisation Score, Right to Erasure Compliance, Subject Access Request Fulfilment, Consent Verification Accuracy - extensive AVT-specific privacy metrics beyond DTAC's data protection scope.

#### C3 - Technical Security

| DTAC Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| C3.1 | Cyber Essentials certification | *Certification criterion - no metric equivalent* | - |
| C3.3 | Penetration testing (OWASP top 10) | Prompt Injection Resistance Rate, Jailbreak Resistance Score, Template Injection Vulnerability Assessment | 🟡 2 |
| C3.4 | Software Security Code of Practice | Output Safety Classifier Coverage | 🟡 2 |
| C3.5 | Multi-factor authentication | Clinician Identity Authentication | 🟡 2 |
| C3.6 | Logging and reporting | Audit Trail Completeness, EU AI Act Event Logging Compliance | 🟡 2 |

**Taxonomy extends:** Adversarial Audio Detection Rate, Data Poisoning Resilience, Voice Cloning / Deepfake Detection, Side-Channel Data Leakage, Cross-Patient Information Leakage Rate, Membership Inference Attack AUC - AVT-specific adversarial robustness metrics beyond DTAC's general security scope.

#### C4 - Interoperability

| DTAC Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| C4.1.1 | API interoperability standards | FHIR R4 Resource Conformance Rate, openEHR Archetype Conformance | 🟡 2 / 🔵 3 |
| C4.1.2 | Open API documentation | *Process criterion - no metric equivalent* | - |
| C4.2.1 | NHS number for patient identification | Field Mapping Accuracy (EPR integration) | 🟢 1 |
| C4.2.2 | PDS / local record integration | Integration Error Rate | 🟢 1 |

**Taxonomy extends:** Write-back Fidelity, Update vs Append Behaviour, Write-back Rollback Capability, Structured/Free-Text Consistency - the taxonomy has extensive EPR write-back safety metrics that go far beyond DTAC's interoperability questions.

#### D1 - Usability and Accessibility

| DTAC Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| D1.1 | User journey / care pathway fit | Work-as-Imagined vs Work-as-Done Gap | 🔵 3 |
| D1.2 | User testing | Trust Calibration Survey, Full Attentiveness Rate | 🟡 2 |
| D1.3 | Accessible Information Standard | *Gap - no accessibility metric in taxonomy* | - |
| D1.4.1 | WCAG 2.2 AA compliance | *Gap - no accessibility metric in taxonomy* | - |
| D1.5 | Service availability | System Availability / Uptime | 🟢 1 |

**Gaps:** The taxonomy has no web accessibility (WCAG) or Accessible Information Standard metrics. These are relevant for AVT user interfaces but not for the clinical AI pipeline itself.

---

### DSPT (Data Security and Protection Toolkit) - NDG Standards

DSPT v8 uses 10 National Data Guardian Data Security Standards with assertions and evidence items. This mapping covers the Category 2 (IT Supplier) variant, which is most relevant to AVT vendors. Only assertions with AI/AVT-relevant content are mapped.

#### Standard 1 - Personal Confidential Data

| DSPT Assertion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| 1.1.1 | ICO registration | *Process criterion - no metric equivalent* | - |
| 1.1.2 | Documented personal data holdings | Data Minimisation Score, Training Data Inclusion Status | 🟡 2 |
| 1.1.3 | Privacy information published | Verbal Notification Compliance, Patient Dissent Recording Rate | 🟢 1 |
| 1.1.6 | Consent to share reviewed | Consent Verification Accuracy | 🟢 1 |
| 1.2.2 | Handling objection to processing | Patient Opt-Out Rate, Patient Dissent Recording Rate | 🟢 1 |
| 1.2.3 | Subject access request process | Subject Access Request Fulfilment | 🟢 1 |
| 1.2.4 | National data opt-out compliance | *Does not apply to AVT processing for individual care (NHSE IG guidance Mar-2026). NDOO applies only to secondary uses (research, planning, commissioning).* | - |
| 1.3.5 | Data security risk register | Assurance Debt Accumulation Rate | 🟢 1 |
| 1.3.7 | Data protection by design | Data Minimisation Score, PII Extraction Attack Success Rate | 🟡 2 |
| 1.3.8 | DPIA process linked to risk management | DPIA Template Completion Rate | 🟢 1 |
| 1.4.1 | Records management including retention | Audio Retention Compliance, Transcript Retention Compliance, Audio Time-to-Deletion | 🟢 1 |

> **Note on the National Data Opt-Out (assertion 1.2.4):** NHS England's March 2026 IG guidance for ambient scribing is explicit that the NDOO does *not* apply when AVT is used for individual care. It applies only to secondary uses of confidential patient information (research, planning, commissioning). Deployers must not configure AVT to suppress use based on NDOO flags; patient-level AVT opt-out and per-encounter dissent are separate mechanisms, measured by IO.PX-1 Patient Opt-Out Rate and GV.CR-1 Patient Dissent Recording Rate respectively.

#### Standard 2 - Staff Responsibilities

| DSPT Assertion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| 2.2.1 | Contracts contain data security requirements | *Process criterion - no metric equivalent* | - |

#### Standard 3 - Training

| DSPT Assertion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| 3.1.1 | Training needs analysis | Training Material Currency | 🟡 2 |
| 3.1.2 | Training activities implemented | Clinician Training Completion Rate | 🟢 1 |
| 3.1.3 | Evaluation of training | Failure Mode Awareness Score | 🟡 2 |
| 3.2.1 | IG/cyber prioritised by board | *Process criterion - no metric equivalent* | - |

#### Standard 4 - Managing Access

| DSPT Assertion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| 4.2.3 | Logs retained and searchable | Audit Trail Completeness | 🟡 2 |
| 4.3.2 | Users/systems authenticated before access | Clinician Identity Authentication | 🟡 2 |
| 4.4.1 | Privileged account logs tamper-proof | Audit Trail Completeness | 🟡 2 |
| 4.5.3 | MFA enforced on remote/privileged access | Clinician Identity Authentication | 🟡 2 |

#### Standard 5 - Process Reviews

| DSPT Assertion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| 5.1.1 | Root cause analysis after incidents | Time-to-Correct, Adverse Event / Incident Rate (LFPSE) | 🟡 2 / 🟢 1 |

#### Standard 6 - Responding to Incidents

| DSPT Assertion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| 6.1.1 | Incidents reported by staff | Near-Miss Reporting Rate, Adverse Event / Incident Rate (LFPSE) | 🟢 1 |
| 6.1.2 | Board informed of reportable breaches | SPI Escalation Response Time | 🟡 2 |
| 6.1.3 | Affected individuals informed | Incident Disclosure Compliance | 🟢 1 |
| 6.3.3 | Proportionate monitoring for security events | Performance Degradation Detection Latency, Output Safety Classifier Coverage | 🟡 2 |

#### Standard 7 - Continuity Planning

| DSPT Assertion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| 7.1.2 | Service continuity during incidents | Pipeline Failure Recovery, System Availability / Uptime | 🟡 2 / 🟢 1 |
| 7.3.4 | Backups of essential service data | Write-back Rollback Capability | 🟡 2 |

#### Standard 8 - Unsupported Systems

| DSPT Assertion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| 8.1.1 | Software asset tracking | Model Version Tracking | 🟢 1 |
| 8.3.1 | System update frequency | Model Update Impact Score, Model Change Notification Compliance | 🟡 2 / 🟢 1 |

#### Standard 9 - IT Protection

| DSPT Assertion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| 9.2.1 | Annual penetration test | Prompt Injection Resistance Rate, Jailbreak Resistance Score | 🟡 2 |
| 9.3.1 | Web applications protected (OWASP) | Template Injection Vulnerability Assessment | 🟡 2 |
| 9.3.6 | Data in transit protected | Cross-Border Data Transfer Compliance | 🟢 1 |
| 9.5.11 | Software per Security Code of Practice | Output Safety Classifier Coverage | 🟡 2 |

#### Standard 10 - Accountable Suppliers

| DSPT Assertion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| 10.1.1 | Supplier list with risk identification | Sub-Processor Transparency, AVT Supplier Registry Listing Verification | 🟢 1 |
| 10.2.1 | Supplier certification | AVT Supplier Registry Listing Verification | 🟢 1 |
| 10.2.4 | Outsourced service security | Sub-Processor Transparency | 🟢 1 |

---

### DCB0129 / DCB0160 - Clinical Risk Management Standards

DCB0129 applies to manufacturers of health IT systems; DCB0160 applies to deploying organisations. Both follow the same clinical safety lifecycle. This mapping shows which taxonomy metrics provide evidence for each lifecycle stage.

#### Stage 1: Clinical Risk Management System

| Requirement | Actor | Taxonomy Metrics | Tier |
|-------------|-------|-----------------|------|
| Appoint Clinical Safety Officer | Manufacturer / Deployer | Clinical Safety Case Completeness (evidences CSO sign-off) | 🟢 1 |
| Document Clinical Risk Management Plan | Manufacturer / Deployer | *Process artefact - no metric equivalent* | - |
| Define risk management scope | Manufacturer / Deployer | Coverage Gap Analysis (identifies where measurement is absent) | 🔵 3 |

#### Stage 2: Hazard Identification

| Requirement | Actor | Taxonomy Metrics | Tier |
|-------------|-------|-----------------|------|
| Systematic hazard identification | Both | Hazard Log Completeness | 🟢 1 |
| Consider intended use and foreseeable misuse | Both | Off-Label Use Detection Rate | 🟡 2 |
| Document hazards in Hazard Log | Both | Hazard Log Completeness | 🟢 1 |
| Consider failure modes | Both | Error Propagation / Cascade Analysis, Pipeline Failure Recovery | 🔵 3 / 🟡 2 |
| Consider interactions with other systems | Both | Integration Error Rate, Structured/Free-Text Consistency | 🟢 1 / 🟡 2 |
| Consider user interface issues | Both | Automation Bias Detection (Error Injection), Trust Calibration Survey | 🟡 2 |

**Taxonomy extends for AVT-specific hazards:**
- Hallucination Rate, Omission Rate (content fabrication/loss)
- Speaker Attribution Accuracy (misattribution)
- Write-back Fidelity, Field Mapping Accuracy (EPR integration failures)
- Code Hallucination Rate (non-existent code generation)
- Bystander Voice Detection Rate (consent/privacy failures)

#### Stage 3: Risk Assessment

| Requirement | Actor | Taxonomy Metrics | Tier |
|-------------|-------|-----------------|------|
| Severity × likelihood risk estimation | Both | Probabilistic Risk Quantification (P₁/P₂), Safety Performance Indicators with Thresholds (DSCMS) | 🔵 3 / 🟢 1 |
| Risk classification (acceptable → unacceptable) | Both | Assurance Debt Accumulation Rate (tracks tolerable risk accumulation) | 🟢 1 |
| Record initial and residual risk | Both | Hazard Log Completeness | 🟢 1 |

#### Stage 4: Risk Control

| Requirement | Actor | Taxonomy Metrics | Tier |
|-------------|-------|-----------------|------|
| Inherent safety by design | Manufacturer | Code Hallucination Rate (constrained generation = inherent safety) | 🟢 1 |
| Protective measures within system | Manufacturer | Output Safety Classifier Coverage, Prompt Injection Resistance Rate | 🟡 2 |
| Information for safety (warnings, guidance) | Manufacturer | Uncertainty Marker Preservation, ASR Confidence Exposure | 🟢 1 / 🟡 2 |
| Verify risk control effectiveness | Both | All Tier 1 metrics collectively evidence risk control effectiveness | 🟢 1 |
| Ensure no new hazards from controls | Both | Metric Interaction Analysis | 🔵 3 |

#### Stage 5: Clinical Safety Case

| Requirement | Actor | Taxonomy Metrics | Tier |
|-------------|-------|-----------------|------|
| Clinical Safety Case Report | Both | Clinical Safety Case Completeness | 🟢 1 |
| Residual risk summary | Both | Assurance Debt Accumulation Rate | 🟢 1 |
| Release decision sign-off | Both | *Process criterion - no metric equivalent* | - |

#### Stage 6: Monitoring and Review

| Requirement | Actor | Taxonomy Metrics | Tier |
|-------------|-------|-----------------|------|
| Post-market surveillance | Manufacturer | Performance Degradation Detection Latency, Cross-Practice Variance Coefficient | 🟡 2 |
| Monitor safety through incident analysis | Both | Adverse Event / Incident Rate (LFPSE), Near-Miss Reporting Rate | 🟢 1 |
| Review Hazard Log on modification | Both | Model Update Impact Score, Retraining Trigger Threshold Specification | 🟡 2 |
| Periodic safety reviews | Both | Safety Performance Indicators with Thresholds (DSCMS) | 🟢 1 |
| Manage safety through change | Manufacturer | Model Change Notification Compliance, FDA PCCP-Equivalent Pre-Defined Acceptance Criteria | 🟢 1 / 🟡 2 |
| Monitor for unexpected clinical impacts | Deployer | Downstream Diagnostic Accuracy, Medication Error Rate Differential | 🔵 3 |

#### Stage 7: Incident Management

| Requirement | Actor | Taxonomy Metrics | Tier |
|-------------|-------|-----------------|------|
| Incident management procedures | Both | Adverse Event / Incident Rate (LFPSE), SPI Escalation Response Time | 🟢 1 / 🟡 2 |
| Root cause investigation | Both | Error Attribution Analysis, Time-to-Correct | 🔵 3 / 🟡 2 |
| Corrective actions | Both | Time-to-Correct | 🟡 2 |
| Safety notices / field corrective actions | Manufacturer | Incident Disclosure Compliance, Model Change Notification Compliance | 🟢 1 |
| Report to MHRA if medical device | Manufacturer | *Process criterion - no metric equivalent* | - |
| Report through LFPSE | Deployer | Adverse Event / Incident Rate (LFPSE) | 🟢 1 |

---

### NHS England LLM Evaluation and Monitoring Framework (v0.2.2)

> **⚠️ Draft framework.** This mapping is against v0.2.2 (August 2025), which is experimental and subject to change. Dimensions marked with 🔄 appear provisional - their scope or measurement approach may evolve significantly before v1.0. This mapping should be reviewed when the framework reaches v1.0.

The framework has 30 evaluation dimensions across three groups. All dimensions in Suitability in Context and Wider Impact use manual monitoring; Quantifiable Changes dimensions use automatic continuous monitoring with manual review.

#### Group 1: Suitability in Context (11 dimensions)

| LLM Framework Dimension | Taxonomy Metrics | Tier | Notes |
|--------------------------|-----------------|------|-------|
| **Accountability** | Clinical Safety Case Completeness, ICB Engagement Documentation, Incident Disclosure Compliance | 🟢 1 | Taxonomy provides specific metrics for the accountability chain |
| **Concept drift** | Concept Drift in Clinical Notes, Performance Degradation Detection Latency, AI-Generated Data Contamination Rate | 🔵 3 / 🟡 2 | Taxonomy's Longitudinal Drift & Model Contamination sub-cluster maps directly |
| **Cost** 🔄 | Cost per Consultation, Governance & Maintenance Burden | 🟡 2 / 🔵 3 | **Partial gap** - taxonomy lacks total cost of ownership or cost-effectiveness metric |
| **Data governance** | DPIA Template Completion Rate, Audio Retention Compliance, Transcript Retention Compliance, Data Minimisation Score, Training Data Inclusion Status | 🟢 1 / 🟡 2 | Strong coverage through Privacy & Data Governance group |
| **Expected outcomes** | Clinical Decision Equivalence, Downstream Diagnostic Accuracy, Documentation Time per Consultation | 🔵 3 / 🟢 1 | Taxonomy addresses clinical outcomes; framework's "is an LLM the right solution?" question has no metric equivalent |
| **Explainability** 🔄 | Linked Evidence / Provenance Tracing, Intermediate Output Access, ASR Confidence Exposure | 🟡 2 | Taxonomy provides provenance tracing rather than model interpretability |
| **Fairness and edge cases** | Demographic-Disaggregated WER, Intersectional Performance, Rare Presentation Handling, Health Literacy Performance Variation, Coding Equity Index | 🟡 2 / 🔵 3 | Extensive coverage through Demographic Equity Disaggregation family + Fairness & Equity group |
| **Privacy** | PII Extraction Attack Success Rate, Re-identification Risk Assessment, Cross-Patient Information Leakage Rate, Membership Inference Attack AUC | 🟡 2 / 🔵 3 | Strong coverage for model-level privacy; audio/transcript privacy in separate group |
| **Safety assessment** | Safety Performance Indicators with Thresholds (DSCMS), Hazard Log Completeness, Clinical Safety Case Completeness | 🟢 1 | Maps directly to DCB0129/0160 requirements |
| **Subject matter expert involvement** 🔄 | *Gap - no metric for SME participation in evaluation* | - | Taxonomy assigns Responsible Actors but does not measure SME involvement depth |
| **Uncertainty communication** | Uncertainty Marker Preservation, ASR Confidence Exposure, ASR Confidence Calibration | 🟢 1 / 🟡 2 | Strong coverage for output uncertainty; automation bias addresses user response |

#### Group 2: Wider Impact (11 dimensions)

| LLM Framework Dimension | Taxonomy Metrics | Tier | Notes |
|--------------------------|-----------------|------|-------|
| **Accessibility of healthcare** | Deployment Equity Index, Adoption Rate & Selective Use Patterns | 🟡 2 / 🟢 1 | Taxonomy addresses deployment equity; does not address health literacy access |
| **Documentation** | Telemetry Provision Completeness, Benchmark & Evaluation Data Accessibility, Model Change Notification Compliance | 🟡 2 / 🟢 1 | Good coverage through Vendor Transparency group |
| **Ethics** 🔄 | Stigmatising Language Replication Rate, Emotional Content Preservation, Chilling Effect Assessment | 🟡 2 / 🔵 3 | Taxonomy addresses specific ethical dimensions; no general ethics framework metric |
| **Feedback mechanism** | Near-Miss Reporting Rate, Re-record / Abandonment Rate | 🟢 1 / 🟡 2 | Taxonomy covers incident/feedback reporting but not structured staff feedback mechanisms |
| **Human oversight** | Review-Before-Signing Rate, Edit Rate, Automation Bias Detection, Verification Burden | 🟢 1 / 🟡 2 | Strong coverage through Post-Generation Correction family + human factors metrics |
| **Intentional misuse** | Prompt Injection Resistance Rate, Jailbreak Resistance Score, Adversarial Audio Detection Rate, Template Injection Vulnerability Assessment | 🟡 2 / 🔵 3 | Strong coverage through Security & Adversarial Robustness group |
| **Natural environment** | Energy Consumption per Clinical Note, Carbon Emissions per Inference, Water Consumption per Query | 🔵 3 | Direct mapping to Environmental & Sustainability group |
| **Regulations** | Clinical Safety Case Completeness, DPIA Template Completion Rate, EU AI Act Event Logging Compliance, FDA PCCP-Equivalent Pre-Defined Acceptance Criteria | 🟢 1 / 🟡 2 | Strong coverage through NHS Compliance & Regulatory group |
| **Society** 🔄 | Clinical Documentation Skill Attenuation, Cognitive Offloading Rate, Therapeutic Relationship Impact | 🔵 3 | Taxonomy addresses skill/wellbeing impacts; no job security metric |
| **Third-party audit** | Audit Trail Completeness, Benchmark & Evaluation Data Accessibility | 🟡 2 / 🔵 3 | Taxonomy provides audit infrastructure metrics |
| **Unintentional misuse** | Clinician Training Completion Rate, Failure Mode Awareness Score, Off-Label Use Detection Rate | 🟢 1 / 🟡 2 | Good coverage through Training & Competency group |

#### Group 3: Quantifiable Changes (8 dimensions)

| LLM Framework Dimension | Taxonomy Metrics | Tier | Notes |
|--------------------------|-----------------|------|-------|
| **Benchmark relevance** 🔄 | Goodhart's Law Monitoring, Coverage Gap Analysis, Inter-Rater Reliability Baseline | 🟡 2 / 🔵 3 | **Partial gap** - taxonomy lacks explicit benchmark relevance decay metric |
| **Bias - in-context learning** 🔄 | *Gap - no metric for few-shot prompt bias* | - | Not directly applicable to most AVT systems (pipeline-based, not prompt-based) |
| **Bias analysis - error rates** | Demographic-Disaggregated WER, Intersectional Performance, Intersectional Compound Fairness Score, Compound Demographic Performance | 🟡 2 / 🔵 3 | Strong coverage through Demographic Equity Disaggregation family |
| **Changes to the system** | Model Version Tracking, Model Update Impact Score, Model Change Notification Compliance | 🟢 1 / 🟡 2 | Direct mapping - taxonomy has strong change management metrics |
| **Data drift** | Performance Degradation Detection Latency, Concept Drift in Clinical Notes, Retraining Trigger Threshold Specification | 🟡 2 / 🔵 3 | Good coverage; taxonomy distinguishes concept drift from data drift |
| **Evaluation techniques for ongoing monitoring** | PDSQI-9, CREOLA Error Taxonomy, LLM-as-a-Judge, Automated-Human Metric Concordance | 🟡 2 / 🔵 3 | Strong coverage; taxonomy extensively addresses clinical evaluation methodology |
| **Scalability** 🔄 | Full-Pipeline Latency Budget, System Availability / Uptime | 🟡 2 / 🟢 1 | **Partial gap** - taxonomy lacks explicit scalability / concurrency metric |
| **System for monitoring** | Safety Performance Indicators with Thresholds (DSCMS), Goodhart's Law Monitoring | 🟢 1 / 🟡 2 | Taxonomy provides the metrics; framework asks whether monitoring infrastructure exists |

---

### NHS T.E.S.T. Framework (Technology Evaluation Safety Test)

**Publisher:** Developed by clinicians at Great Ormond Street Hospital, NHS London, Chelsea & Westminster, and UCL; published via the Health Innovation Network (June 2025, v11.17625SS).
**Mandatory status:** Not statutorily mandatory, but positioned as an ICS-level assurance gate: "If your ICS has already approved an AVT vendor using T.E.S.T., individual Trusts, PCNs, or Surgeries may not need to conduct separate assurance processes." Liability for non-compliant choices rests locally.
**AVT relevance:** Purpose-built for AVT / ambient-scribing procurement. Directly addresses this taxonomy's scope.

The framework has two parts. **Section A** is a binary pass/fail platform-assurance checklist (7 domains, 22 requirements; all must pass to progress). **Section B** is a 420-point benefits score across 12 domains, with certification thresholds: Gold 🥇 360–410 (NHS-wide scale), Silver 🥈 290–359 (single-site use), 200–279 needs improvement, <200 not recommended. Gold is practically unreachable without the 50-point RCT / clinical-validation item.

#### Section A - Platform Assurance (binary, all 22 requirements mandatory)

| # | T.E.S.T. Requirement | Domain | Taxonomy Metrics | Tier | Notes |
|---|----------------------|--------|------------------|------|-------|
| 1 | NHS accreditations (DTAC, DSPT, CE Plus, CREST pentest, UK GDPR) | Cybersecurity | *Process criterion - covered by DTAC/DSPT mappings above* | - | Compound accreditation check; see DTAC and DSPT sections |
| 2 | Safeguarding patient information (DSPT, E2E encryption, DPIA, TRE rules, controllership) | Data Protection | GV.CR-7 DPIA Template Completion Rate, GV.PD-9 Cross-Border Data Transfer Compliance | 🟢 1 | Strong coverage; E2E encryption itself is a control, not a metric |
| 3 | Deletion of patient data (audio + transcript auto-delete, minimisation, retention proportionality) | Data Protection | GV.PD-1 Audio Retention Compliance, GV.PD-2 Audio Time-to-Deletion, GV.PD-3 Transcript Retention Compliance, GV.PD-4 Data Minimisation Score | 🟢 1 / 🟡 2 | Direct mapping - taxonomy's Privacy group was built around this exact requirement |
| 4 | AI training data quality, minimisation, anonymisation (ICO-aligned) | Data Protection | GV.PD-7 Training Data Inclusion Status | 🟡 2 | **Partial gap** - no metric on training-data anonymisation provenance |
| 5 | Servers in UK/EU, adequacy decisions, SCCs/BCRs for transfers | Data Protection | GV.PD-9 Cross-Border Data Transfer Compliance | 🟢 1 | Direct mapping |
| 6 | MHRA Class I minimum for summarisation; Class IIa+ for diagnoses/calculations | Clinical Safety | GV.CR-6 Clinical Safety Case Completeness | 🟢 1 | Covered indirectly via MHRA mapping; T.E.S.T. makes the Class boundary explicit |
| 7 | Local ICS/Trust governance approval (DPIA, DCB 0129 Safety Case + Hazard Log, DCB 0160) | Clinical Safety | GV.CR-6 Clinical Safety Case Completeness, GV.SG-17 Hazard Log Completeness, GV.CR-7 DPIA Template Completion Rate | 🟢 1 | Strong coverage; see also DCB0129/0160 mapping |
| 8 | Embedded Clinical Safety Officer (CSO), external validation recommended | Clinical Safety | *Structural requirement - no metric equivalent* | - | Process/organisational requirement |
| 9 | Defined product scope; re-review on scope change | Clinical Safety | GV.SG-2 Model Update Impact Score, GV.VT-1 Model Change Notification Compliance | 🟡 2 / 🟢 1 | Change-management metrics map well |
| 10 | Prompt-injection guardrails (end-users blocked from direct LLM interface) | Clinical Safety | GV.SC-1 Prompt Injection Resistance Rate, GV.SC-6 Template Injection Vulnerability Assessment | 🟡 2 | Direct mapping |
| 11 | Clinician-in-the-loop validation, annotated output data, continuous validation | Clinical Safety | HL.HF-3 Review-Before-Signing Rate, HL.HF-1 Edit Rate, ES.ME-7 Automated-Human Metric Concordance | 🟢 1 / 🔵 3 | Strong coverage through Human Factors + Meta-evaluation |
| 12 | Adverse-event reporting/mitigation processes; inbuilt error reporting advised | Clinical Safety | GV.SG-11 Adverse Event / Incident Rate (LFPSE), GV.SG-14 Near-Miss Reporting Rate, GV.VT-5 Incident Disclosure Compliance | 🟢 1 | Direct mapping |
| 13 | AI language translation liability remains with vendor (not clinician) | Clinical Safety | *Gap - no metric for translation accuracy or liability locus* | - | **Gap** - taxonomy does not currently address AI translation; candidate for roadmap |
| 14 | Disclosure of underlying AI models (even if proprietary) | Bias & Inclusivity | GV.VT-7 Sub-Processor Transparency, GV.VT-3 Benchmark & Evaluation Data Accessibility | 🟢 1 / 🔵 3 | Partial coverage - sub-processor transparency captures model stack disclosure |
| 15 | Evidence of testing on diverse populations; bias-free operation | Bias & Inclusivity | TP.ASR-4 Demographic-Disaggregated WER, IO.FE-4 Intersectional Performance, IO.FE-2 Accent Taxonomy Standardisation | 🟡 2 / 🔵 3 | Strong coverage through Demographic Equity Disaggregation family |
| 16 | Mandatory EHR integration (front-end or back-end) for write-back, provenance | Technical | TP.WB-1 Write-back Fidelity, TP.WB-3 Field Mapping Accuracy, TP.WB-4 Update vs Append Behaviour | 🟢 1 | Direct mapping to EPR Write-back group |
| 17 | Offer simple VR/dictation alongside ambient AI as standard | Technical | *Product-feature requirement - no metric equivalent* | - | Procurement feature check |
| 18 | Routine reporting of hallucination rate, omission rate, word-error-rate | Technical | TP.SN-5 Hallucination Rate, TP.SN-6 Omission Rate, TP.ASR-1 Word Error Rate (WER), TP.ASR-12 Hallucination-Under-Noise Rate | 🟢 1 / 🟡 2 | **Direct mapping** - T.E.S.T. names these three exact metrics |
| 19 | Handle multiple consultations; allow edit/correct pre-session-close | Technical | HL.HF-1 Edit Rate, HL.HF-7 Edit Location Distribution | 🟢 1 / 🟡 2 | Edit-pattern metrics cover in-session correction |
| 20 | Adaptability to clinician styles, formats, workflows | Technical | HL.HF-11 Inter-Clinician Edit Variance, TP.SN-22 Style & Format Consistency | 🔵 3 | Good coverage |
| 21 | Offline capture + async processing; local encryption; 24h auto-delete; logout clears data | Business Continuity | GV.OP-5 System Availability / Uptime, GV.PD-2 Audio Time-to-Deletion, PI.E2E-11 Pipeline Failure Recovery | 🟢 1 / 🟡 2 | Strong coverage |
| 22 | Continuous drift monitoring; formal periodic testing | Evolving Technology Test | GV.SG-3 Performance Degradation Detection Latency, GV.SG-6 Concept Drift in Clinical Notes, GV.SG-4 Retraining Trigger Threshold Specification, GV.SG-9 Safety Performance Indicators with Thresholds (DSCMS) | 🟡 2 / 🔵 3 / 🟢 1 | **Direct mapping** - taxonomy's Longitudinal Drift sub-cluster is built for this |

#### Section B - Benefits Assessment (420 points across 12 domains)

| # | T.E.S.T. Benefit Domain | Points | Taxonomy Metrics | Tier | Notes |
|---|-------------------------|-------:|------------------|------|-------|
| 1 | **Clinical Effectiveness** (RCT validation 50; care standardisation, admin burden, comms, coding accuracy 10 each) | 90 | ES.ME-8 Outcome Evidence Commitment Status (RCT-validation checkbox proxy), ES.ME-9 Causal Model Operationalisation, PI.E2E-9 Clinical Decision Equivalence, IO.PX-9 Downstream Diagnostic Accuracy, GV.OP-1 Documentation Time per Consultation, TP.CC-2 SNOMED CT Concept Mapping Accuracy, TP.CC-11 Code Specificity Index | 🟡 2 / 🔵 3 / 🟢 1 | ES.ME-8 measures **commitment to** RCT evidence (the closest the taxonomy gets to the 50-point RCT item without overstepping the [Outcomes Boundary](#outcomes-boundary)); ES.ME-9 measures whether vendor causal claims are documented. **Gap** - no metric for "timeliness of correspondence across care teams"; the taxonomy does not itself constitute RCT evidence |
| 2 | **Operational Cost-Effectiveness** (economic evaluation 25; ROI 10; cost savings 15; operational savings 10) | 60 | GV.OP-7 Cost per Consultation, GV.OP-8 Governance & Maintenance Burden | 🟡 2 / 🔵 3 | **Partial gap** - taxonomy lacks explicit ROI, total cost of ownership, formal economic-evaluation metric |
| 3 | **Workforce Impact Assessment** (settings, specialties, foci, burnout, job satisfaction) | 60 | GV.OP-6 Adoption Rate & Selective Use Patterns, IO.FE-1 Deployment Equity Index, GV.OP-2 Pyjama Time / After-Hours EHR Use, HL.HF-8 Trust Calibration Survey | 🟢 1 / 🟡 2 | Burnout and pyjama time well-covered. **Gap** - no direct "job satisfaction" metric; no "multi-specialty validation" metric |
| 4 | **Integration and Interoperability** (EHR integration, interoperability synergy, narrative quality) | 35 | TP.WB-6 FHIR R4 Resource Conformance Rate, TP.WB-7 openEHR Archetype Conformance, PI.PP-9 Structured/Free-Text Consistency | 🟡 2 / 🔵 3 | Strong coverage through EPR Write-back group |
| 5 | **Clinician Experience and Usability** (friction, speed, workflow, cognitive load, human factors) | 30 | HL.HF-10 Cognitive Load Assessment, HL.HF-17 Verification Burden, GV.OP-3 Note Turnaround Time, HL.HF-16 Work-as-Imagined vs Work-as-Done Gap | 🔵 3 / 🟡 2 | Strong coverage through Human Factors group |
| 6 | **Training, Adoption, and Human Factors** (ease of use, AI/human labelling, personalisation, learning, training) | 25 | GV.TC-1 Clinician Training Completion Rate, GV.TC-2 Failure Mode Awareness Score, GV.CR-3 AI-Generated Content Labelling Compliance, GV.TC-5 Training Material Currency | 🟢 1 / 🟡 2 | Direct mapping to Training & Competency group |
| 7 | **Patient Safety and Quality of Care** (time for care 15; documentation accuracy 5) | 20 | IO.PX-7 Full Attentiveness Rate, GV.SG-11 Adverse Event / Incident Rate (LFPSE), PI.E2E-1 Source-to-Record Concordance | 🟡 2 / 🟢 1 / 🔵 3 | Strong coverage; Full Attentiveness Rate is a direct proxy for "time for care" |
| 8 | **Patient Experience and Understanding** (communication, patient understanding) | 20 | IO.PX-2 Patient-Perceived Accuracy, IO.PX-6 Therapeutic Relationship Impact, IO.PX-8 Patient Comprehension of AI-Generated Summaries | 🔵 3 | Direct mapping to Patient Experience group |
| 9 | **Virtual Care Integration** (primary, secondary, ambulance/telephone) | 20 | IO.FE-1 Deployment Equity Index, IO.FE-8 Cross-Platform Fairness Consistency | 🟡 2 / 🔵 3 | **Partial gap** - no metric for virtual-care-specific performance; modality stratification absent |
| 10 | **Data & Analytics Integration** (real-time visualisation, data-driven decisions) | 20 | GV.VT-2 Telemetry Provision Completeness, GV.VT-4 Audit Trail Completeness | 🟡 2 | Telemetry metrics cover infrastructure; no metric on downstream analytics use |
| 11 | **Disbenefits / Potential Harm Analysis** (harms characterisation, distribution, mitigation) | 20 | HL.HF-12 Clinical Documentation Skill Attenuation, HL.HF-13 Cognitive Offloading Rate, IO.PX-5 Chilling Effect Assessment, PI.E2E-3 Error Propagation / Cascade Analysis | 🔵 3 | Strong coverage across human factors, patient experience, and pipeline harms |
| 12 | **Environmental and Societal Impact** (carbon, energy, societal, UK economy / sovereign AI) | 20 | GV.EN-1 Energy Consumption per Clinical Note, GV.EN-2 Carbon Emissions per Inference, GV.EN-3 Water Consumption per Query | 🔵 3 | Direct mapping to Environmental & Sustainability group. **Gap** - no metric for "sovereign AI" / UK economic contribution |

**Summary of taxonomy alignment with T.E.S.T.:**

- **Section A (platform assurance):** 18 of 22 requirements have direct or strong metric coverage. 3 are pure process/product-feature criteria (8 CSO, 17 VR/dictation offering). 1 is a clear gap: requirement 13 (AI language translation accuracy and liability) - candidate for the roadmap.
- **Section B (benefits):** All 12 domains have taxonomy metrics in scope. Partial gaps in cost-effectiveness (ROI / TCO / formal economic evaluation), workforce (job satisfaction, multi-specialty validation), virtual-care modality stratification, data analytics use, and sovereign-AI contribution. None are critical given the taxonomy's scope, but several would be practical additions.
- **Strongest alignment:** T.E.S.T. requirement 18 (hallucination / omission / WER) names three exact taxonomy metrics. Requirement 22 (drift) maps directly onto the Longitudinal Drift & Model Contamination sub-cluster. Requirement 3 (deletion) maps onto the full Privacy & Data Governance deletion chain.
- **Distinctive T.E.S.T. contributions:** The explicit MHRA Class I / Class IIa boundary (req 6), the DCB 0129 / DCB 0160 split with 'Evolving Technology Test' as a local post-market surveillance capability (req 7), and the translation-liability stance (req 13) are framing contributions that the taxonomy could reference directly in its Compliance & Regulatory group.

**Candidate metrics to add (T.E.S.T.-derived gaps)** — full entries in [`_gaps.md` §3](#nhs-test-framework-6-candidates):

| Proposed Ref | Title | T.E.S.T. Source | Suggested Placement | Tier |
|---|---|---|---|---|
| TP.SN-26 | AI Translation Accuracy & Liability Attribution | Req 13 | Part A (Summarisation/NLP) or new translation sub-group | 🟡 2 |
| GV.PD-15 | Training Data Anonymisation Provenance | Req 4 | Part E Privacy & Data Governance | 🟡 2 |
| GV.OP-13 | Total Cost of Ownership / Formal Economic Evaluation | Section B.2 | Part E Operational | 🟡 2 |
| GV.VT-11 | Multi-Specialty Validation Coverage | Section B.3 | Part E Vendor Transparency | 🔵 3 |
| IO.FE-9 | Virtual-Care Modality Stratified Performance | Section B.9 | Part D Fairness & Equity | 🔵 3 |
| GV.VT-12 | Sovereign AI / UK Supply Chain Disclosure | Section B.12 | Part E Vendor Transparency | 🔵 3 |

---

### MHRA Software and AI as a Medical Device (SaMD / AIaMD)

The MHRA's regulatory position on software and AI as medical devices is delivered through the **Change Programme** (workstreams WP1–WP11), the **joint FDA/Health Canada Guiding Principles**, and the **Post-Market Surveillance Regulations 2024** (SI 2024 No. 1368, in force 16 June 2025). This mapping covers the assessable criteria most relevant to AVT systems.

**Publisher:** Medicines and Healthcare products Regulatory Agency (MHRA)
**Mandatory status:** Mandatory for systems classified as medical devices under UK MDR 2002; cascades to AVT deployments via vendor compliance obligations
**AVT relevance:** AVT systems with clinical decision-support components may qualify as SaMD/AIaMD. Documentation-only systems may not, but the AI RIG and Transparency principles are widely applied as best practice regardless of classification.

#### Change Programme - Classification (WP1, WP2)

| MHRA Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| WP1-01 | What qualifies as SaMD | *Process criterion - no metric equivalent; informs scope* | - |
| WP1-02 | Crafting intended purpose | *Process criterion - documentation requirement* | - |
| WP1-03 | Manufacturer definition | *Process criterion - legal determination* | - |
| WP2-01 | Classification rules (UK MDR 2002, IMDRF-aligned) | GV.CR-6 Clinical Safety Case Completeness (evidences classification) | 🟢 1 |
| WP2-02 | Regulatory "airlock" sandbox | *Process route - no metric equivalent* | - |
| WP2-03 | Classification rule interpretation | *Process criterion* | - |

#### Change Programme - Premarket (WP3)

| MHRA Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| WP3-02 | Best-practice SaMD development | GV.VT-2 Telemetry Provision Completeness, GV.VT-3 Benchmark & Evaluation Data Accessibility | 🟡 2 / 🔵 3 |
| WP3-04 | Data-driven SaMD (joint with HRA) | GV.PD-7 Training Data Inclusion Status, TP.ASR-4 Demographic-Disaggregated WER | 🟡 2 |
| WP3-05 | Human-centred SaMD | HL.HF-1 Edit Rate, HL.HF-3 Review-Before-Signing Rate, HL.HF-6 Automation Bias Detection | 🟢 1 / 🟡 2 |

#### Change Programme - Post-Market Surveillance (WP4 + SI 2024 No. 1368)

| MHRA Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| PMS Plan | Signal detection, complaints handling, literature review, field experience | GV.SG-3 Performance Degradation Detection Latency, GV.SG-12 Cross-Practice Variance Coefficient | 🟡 2 |
| PMSR (Class I/IIa, on demand) | Periodic non-implantable reporting | *No metric equivalent - reporting artefact* | - |
| PSUR (Class IIb/III, annually) | Periodic Safety Update Report | *No metric equivalent - reporting artefact* | - |
| WP4-02 Reportable incidents (including indirect harm) | Documentation errors causing downstream clinical harm | GV.SG-11 Adverse Event / Incident Rate (LFPSE), GV.SG-14 Near-Miss Reporting Rate | 🟢 1 |
| Trend reporting | Statistically significant increases in non-serious incidents | GV.SG-12 Cross-Practice Variance Coefficient | 🟡 2 |
| WP4-03 Change management | Post-deployment changes and their re-evaluation | GV.SG-2 Model Update Impact Score, GV.VT-1 Model Change Notification Compliance | 🟡 2 / 🟢 1 |
| WP4-04 Predetermined Change Control Plans | PCCPs for AIaMD | GV.CR-9 FDA PCCP-Equivalent Pre-Defined Acceptance Criteria | 🟡 2 |
| Field Safety Corrective Action (FSCA) | Corrective action execution | GV.SG-15 Time-to-Correct, GV.VT-5 Incident Disclosure Compliance | 🟡 2 / 🟢 1 |
| Field Safety Notices (FSN) | Targeted notifications | GV.VT-5 Incident Disclosure Compliance | 🟢 1 |
| Reporting timelines (2/10/15 working days) | Serious threat / death / other serious incidents | GV.SG-16 SPI Escalation Response Time | 🟡 2 |

#### Change Programme - Cybersecurity (WP5)

| MHRA Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| WP5-01 / 02 | Cybersecurity legislation and guidance | GV.SC-1 Prompt Injection Resistance Rate, GV.SC-2 Jailbreak Resistance Score | 🟡 2 |
| WP5-03 | Unsupported software | GV.SG-1 Model Version Tracking | 🟢 1 |
| WP5-04 | Vulnerability reporting | GV.VT-5 Incident Disclosure Compliance | 🟢 1 |

#### Change Programme - AI Rigour (WP9)

| MHRA Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| WP9-01 | GMLP guiding principles (Oct 2021) | *Cross-references 10 GMLP principles below* | - |
| WP9-05 | "AIaMD for all" - bias across populations | TP.ASR-4 Demographic-Disaggregated WER, IO.FE-4 Intersectional Performance, TP.CC-9 Coding Equity Index | 🟡 2 / 🔵 3 |
| WP9-06 | Bias identification standards | IO.FE-3 Clinical Domain Performance Variance, IO.FE-5 Intersectional Compound Fairness Score | 🟡 2 / 🔵 3 |
| WP9-07 | Experimental bias detection / mitigation | IO.FE-2 Accent Taxonomy Standardisation, TP.ASR-5 Speaker-Stratified WER | 🟡 2 / 🔵 3 |

#### Change Programme - Glass Box / Interpretability (WP10)

| MHRA Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| WP10-01 | Human-centred AIaMD | TP.ASR-11 ASR Confidence Exposure, TP.SN-20 Uncertainty Marker Preservation, TP.SN-12 Linked Evidence / Provenance Tracing | 🟡 2 / 🟢 1 |
| WP10-02 | Trustworthy AIaMD standards | HL.HF-8 Trust Calibration Survey, HL.HF-6 Automation Bias Detection | 🟡 2 |

#### Change Programme - Ship of Theseus / Adaptivity (WP11)

| MHRA Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| WP11-01 | Adaptivity guiding principles (static/batch/individualised/continuous) | GV.SG-1 Model Version Tracking, GV.SG-2 Model Update Impact Score | 🟢 1 / 🟡 2 |
| WP11-02 | Concept drift and significant-change detection | GV.SG-6 Concept Drift in Clinical Notes, GV.SG-3 Performance Degradation Detection Latency | 🔵 3 / 🟡 2 |
| WP11-03 | PCCPs for AIaMD | GV.CR-9 FDA PCCP-Equivalent Pre-Defined Acceptance Criteria | 🟡 2 |

#### Transparency Guiding Principles (June 2024, joint MHRA/FDA/Health Canada)

Six-dimension framework (WHO/WHY/WHAT/WHERE/WHEN/HOW). The WHAT dimension contains the most assessable content items:

| Transparency Dimension | Content Items | Taxonomy Metrics | Tier |
|------------------------|---------------|-----------------|------|
| **WHAT - Device characterisation** | Medical purpose, disease/condition, intended users, use environments, target populations | *Partial gap - no specific "device characterisation completeness" metric* | - |
| **WHAT - Workflow integration** | How device fits workflow, intended inputs/outputs | HL.HF-1 Edit Rate, HL.HF-3 Review-Before-Signing Rate | 🟢 1 |
| **WHAT - Performance & safety** | Performance details, benefits/risks, bias-management, clinical study summaries | TP.ASR-1 WER, TP.SN-5 Hallucination Rate, GV.SG-9 Safety Performance Indicators | 🟡 2 / 🟢 1 |
| **WHAT - Model logic & development** | Output logic, ML approach, training/testing data characterisation | GV.PD-7 Training Data Inclusion Status, GV.VT-3 Benchmark & Evaluation Data Accessibility | 🟡 2 / 🔵 3 |
| **WHAT - Limitations** | Known biases, failure modes, confidence intervals, data gaps, validation envelope | TP.SN-5 Hallucination Rate, TP.SN-6 Omission Rate, TP.ASR-10 ASR Confidence Calibration, TP.AC-3 Acoustic Environment Profiling | 🟢 1 / 🟡 2 |
| **WHAT - Lifecycle** | Local acceptance testing, ongoing monitoring, change-management, vulnerability mitigation | GV.SG-3 Performance Degradation Detection Latency, GV.SG-1 Model Version Tracking | 🟡 2 / 🟢 1 |

#### Good Machine Learning Practice (GMLP) - 10 Principles (Oct 2021)

| GMLP Principle | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| GMLP-1 | Multi-Disciplinary Expertise | *Organisational requirement - no direct metric* | - |
| GMLP-2 | Good Software and Engineering Practices | GV.SC-1/2 security metrics, GV.VT-4 Audit Trail Completeness | 🟡 2 |
| GMLP-3 | Representative Datasets | TP.ASR-4 Demographic-Disaggregated WER, GV.PD-7 Training Data Inclusion Status | 🟡 2 |
| GMLP-4 | Training Data Independent from Test Data | *No metric equivalent - methodology check* | - |
| GMLP-5 | Best Available Reference Datasets | GV.VT-3 Benchmark & Evaluation Data Accessibility | 🔵 3 |
| GMLP-6 | Model Design Tailored to Data and Intended Use | ES.ME-1 Proximal vs Distal Outcome Distinction | 🔵 3 |
| GMLP-7 | Focus on Human-AI Team Performance | HL.HF-1 Edit Rate, HL.HF-6 Automation Bias Detection, HL.HF-8 Trust Calibration Survey | 🟢 1 / 🟡 2 |
| GMLP-8 | Testing in Clinically Relevant Conditions | TP.AC-3 Acoustic Environment Profiling, PI.E2E-9 Clinical Decision Equivalence | 🟡 2 / 🔵 3 |
| GMLP-9 | Users Provided Clear Essential Information | TP.ASR-11 ASR Confidence Exposure, TP.SN-20 Uncertainty Marker Preservation | 🟡 2 / 🟢 1 |
| GMLP-10 | Deployed Models Monitored, Retraining Risks Managed | GV.SG-3 Performance Degradation Detection Latency, GV.SG-4 Retraining Trigger Threshold Specification, GV.SG-5 AI-Generated Data Contamination Rate | 🟡 2 / 🔵 3 |

**Gaps:**
- Medical device classification documentation (no metric)
- PCCP documentation for adaptive algorithms (partial - GV.CR-9 is about acceptance criteria, not the PCCP itself)
- PMSR / PSUR report completeness (reporting artefacts, no metric)
- Transparency documentation for all WHAT content items as a composite
- Device characterisation completeness

**Taxonomy extends:** Strong coverage through Safety & Governance (incident detection and response), Security & Adversarial Robustness, Privacy & Data Governance, and Vendor Transparency groups. MHRA guidance is process-heavy; the taxonomy provides the measurement substrate that MHRA assumes exists.

---

### NICE Evidence Standards Framework for Digital Health Technologies (ECD7)

**Publisher:** National Institute for Health and Care Excellence (NICE)
**Version:** ECD7 published 10 December 2018; last substantive update 9 August 2022 (AI provisions)
**Mandatory status:** Not formally mandatory but de facto required for any DHT claiming NHS clinical benefit; referenced in NICE appraisal, procurement, and ICS commissioning.
**AVT relevance:** AVT systems typically sit in Tier B1 (Communicating) or Tier C1/C2 (Clinical Management) depending on write-back configuration. A pure transcription tool that does not influence clinical decisions is Tier B1; a tool whose output drives structured coding or decision-support is Tier C1/C2.

ECD7 contains **21 numbered standards across 5 lifecycle areas**. Each has **minimum** and **best practice** levels across **Tier A/B/C** functional classification. AI-specific provisions are concentrated in Standards 4, 5, 6, 15, and 16.

#### Standards 1–9: Design Factors

| NICE Standard | Description | Taxonomy Metrics | Tier |
|--------------|-------------|-----------------|------|
| 1 - Safety & Quality Compliance | UKCA/CE, GDPR, CQC (min); ISO 13485, IEC 82304-1, BS EN 62304 (best) | GV.CR-6 Clinical Safety Case Completeness, GV.CR-7 DPIA Template Completion Rate | 🟢 1 |
| 2 - User Acceptability | Users in design/testing (min); IEC 62366-1 usability engineering (best) | HL.HF-8 Trust Calibration Survey, IO.PX-7 Full Attentiveness Rate | 🟡 2 |
| 3 - Environmental Sustainability | Narrative (min); NHS net-zero alignment, quantified GHG (best) | GV.EN-1 Energy Consumption per Clinical Note, GV.EN-2 Carbon Emissions per Inference | 🔵 3 |
| **4 - Inequalities & Bias Mitigation** ⭐ AI-specific | Describe considerations (min); **document algorithmic bias mitigation** (best) | IO.FE-1 Deployment Equity Index, TP.ASR-4 Demographic-Disaggregated WER, TP.CC-9 Coding Equity Index, IO.FE-5 Intersectional Compound Fairness Score | 🟡 2 / 🔵 3 |
| **5 - Data Practices** ⭐ AI-specific | Identify datasets (min); **follow MHRA GMLP, dataset diversity** (best) | GV.PD-7 Training Data Inclusion Status, GV.PD-4 Data Minimisation Score | 🟡 2 |
| **6 - Professional Oversight** ⭐ AI-specific | Articulate oversight level (min); proportionate oversight, override tracking (best) | HL.HF-3 Review-Before-Signing Rate, HL.HF-1 Edit Rate, HL.HF-6 Automation Bias Detection | 🟢 1 / 🟡 2 |
| 7 - Health Information Reliability | Validity processes (min); expert review at intervals (best) | TP.SN-3 PDSQI-9, TP.SN-4 CREOLA Error Taxonomy Scores | 🟡 2 |
| 8 - UK Professional Credibility | Professional involvement (min); expert-group utility evidence (best) | *Process criterion - no metric equivalent* | - |
| 9 - Safeguarding | Access controls, moderation (min); documented agreements, qualified oversight (best) | GV.PD-8 Consent Verification Accuracy, TP.AC-4 Bystander Voice Detection Rate | 🟢 1 / 🔵 3 |

#### Standards 10–13: Describing Value

| NICE Standard | Description | Taxonomy Metrics | Tier |
|--------------|-------------|-----------------|------|
| 10 - Intended Purpose & Target Population | Inclusion/exclusion (min); subgroup variation (best) | IO.FE-3 Clinical Domain Performance Variance, IO.FE-6 Rare Presentation Handling | 🟡 2 / 🔵 3 |
| 11 - Current Pathway | Clinical guidelines + consultation (min) | *Process criterion - no metric equivalent* | - |
| 12 - Proposed Pathway | Differences from current care (min); workforce changes, boundaries crossed (best) | GV.OP-1 Documentation Time per Consultation, GV.OP-6 Adoption Rate & Selective Use Patterns | 🟢 1 |
| 13 - Expected Impacts | Compare benefits/costs (min); confidence intervals, sensitivity analysis (best) | IO.PX-9 Downstream Diagnostic Accuracy, PI.E2E-9 Clinical Decision Equivalence | 🔵 3 |

#### Standards 14–16: Demonstrating Performance

| NICE Standard | Description | Taxonomy Metrics | Tier |
|--------------|-------------|-----------------|------|
| 14 - Effectiveness Evidence *(Tier C only)* | Clinical-mgmt: real-world evaluations; Diagnostic: accuracy vs reference; Treatment: RCTs preferred | PI.E2E-9 Clinical Decision Equivalence, IO.PX-9 Downstream Diagnostic Accuracy, IO.PX-10 Medication Error Rate Differential | 🔵 3 |
| **15 - Real-World Evidence** ⭐ AI-specific | Pilot site statement (min); **"silent mode" evaluation for AI on local data** (best) | GV.SG-12 Cross-Practice Variance Coefficient, GV.OP-6 Adoption Rate & Selective Use Patterns | 🟡 2 / 🟢 1 |
| **16 - Performance Monitoring Plan** ⭐ AI-specific | Usage vs expected (min); **AI/ML: post-deployment reporting, retraining schedules, subgroup drift** (best) | GV.SG-3 Performance Degradation Detection Latency, GV.SG-4 Retraining Trigger Threshold Specification, GV.SG-6 Concept Drift in Clinical Notes | 🟡 2 / 🔵 3 |

#### Standards 17–18: Delivering Value

| NICE Standard | Description | Taxonomy Metrics | Tier |
|--------------|-------------|-----------------|------|
| 17 - Budget Impact Analysis | Direct costs vs comparator (min); indirect costs, NHS reference costs (best) | GV.OP-7 Cost per Consultation | 🟡 2 |
| 18 - Cost-Effectiveness Analysis | Cost-utility or cost-consequences (min); EQ-5D for QALYs, sensitivity/scenario analyses (best) | *Gap - taxonomy lacks cost-effectiveness or QALY metric* | - |

#### Standards 19–21: Deployment

| NICE Standard | Description | Taxonomy Metrics | Tier |
|--------------|-------------|-----------------|------|
| 19 - Deployment Transparency | Data dictionary, input description, infrastructure (min); tolerance for incomplete data, DICOM etc. (best) | GV.VT-2 Telemetry Provision Completeness, TP.WB-6 FHIR R4 Resource Conformance Rate | 🟡 2 |
| 20 - Communication, Consent & Training | Describe outputs (min); model cards, training approaches (best) | GV.TC-1 Clinician Training Completion Rate, GV.TC-2 Failure Mode Awareness Score, GV.CR-3 AI-Generated Content Labelling Compliance | 🟢 1 / 🟡 2 |
| 21 - Scalability | Load testing (min); documented methodology vs projected users (best) | GV.OP-5 System Availability / Uptime, PI.E2E-10 Full-Pipeline Latency Budget | 🟢 1 / 🟡 2 |

**Gaps:**
- Tier A/B/C functional classification documentation for specific AVT deployments
- "Silent mode" evaluation evidence (Standard 15 best practice) - partial coverage via GV.OP-6 but no dedicated metric
- Subgroup drift monitoring as a composite (Standard 16 best practice) - metrics exist but not assembled
- Cost-effectiveness analysis / QALY (Standard 18) - no metric
- Budget impact analysis composite (Standard 17) - GV.OP-7 is partial
- Real-world performance data plan documentation (Standard 15)

**Taxonomy extends:** Standards 14–16 (Performance) are well covered. Part A (Technical Pipeline) and Part B (Pipeline Interactions) provide measurement depth that NICE ESF does not prescribe at the operational level.

---

### FHIR UK Core / INTEROPen

**Publisher:** NHS England Digital, with HL7 UK; INTEROPen community contribution
**Scope:** UK-specific FHIR R4 profiles for health and care data exchange. Successor to CareConnect (STU3).
**Mandatory status:** De facto mandatory for NHS system interoperability; referenced in NHS Standard Contract and procurement.
**AVT relevance:** AVT systems writing back to EPRs must conform to UK Core profiles, not generic FHIR R4. Different STU versions expose different resources: STU1 is foundational only (no Composition/Condition/Observation); STU2 adds the clinical content profiles AVT actually needs; STU3 adds specialised observations.

#### Release Status

| Release | Base | Status | Relevance for AVT |
|---------|------|--------|-------------------|
| **STU1 (1.0.0)** | FHIR R4 | Published | 12 foundational profiles (Patient, Practitioner, Medication*, AllergyIntolerance) - insufficient alone for clinical note write-back |
| **STU2 (2.0.2)** | FHIR R4 | Released 28 May 2024 (current) | 33 profiles including Composition, Condition, Encounter, Observation, Procedure - the baseline for AVT write-back |
| **STU3** | FHIR R4 | In development ("Sequence") | ~52 profiles adding specialised vital-sign Observations (NEWS2, blood glucose, alcohol consumption, vital signs) |

#### Assertion-level profile conformance (STU2+ baseline for AVT)

| UK Core Profile | STU | AVT Write-back Relevance | Taxonomy Metrics | Tier |
|-----------------|-----|--------------------------|-----------------|------|
| UKCore-Composition | 2+ | Clinical note container; assembles sections | TP.WB-6 FHIR R4 Resource Conformance Rate *(refined: means UK Core, not generic FHIR R4)* | 🟡 2 |
| UKCore-Encounter | 2+ | Binds note to consultation event | TP.WB-6 FHIR R4 Resource Conformance Rate | 🟡 2 |
| UKCore-Condition | 2+ | Extracted diagnoses / problems | TP.WB-3 Field Mapping Accuracy, TP.CC-2 SNOMED CT Concept Mapping Accuracy | 🟢 1 / 🟡 2 |
| UKCore-AllergyIntolerance | 1+ | Extracted allergies (safety-critical) | TP.WB-1 Write-back Fidelity, TP.WB-4 Update vs Append Behaviour | 🟢 1 |
| UKCore-MedicationStatement | 1+ | Current medications | TP.CC-5 dm+d Medication Coding Accuracy, TP.WB-1 Write-back Fidelity | 🟡 2 / 🟢 1 |
| UKCore-MedicationRequest | 1+ | New prescriptions | TP.SN-19 Medication Attribute Extraction F1, TP.SN-21 Medication Event Classification | 🟡 2 |
| UKCore-Observation | 2+ | Structured vitals from consultation | TP.WB-3 Field Mapping Accuracy | 🟢 1 |
| UKCore-Procedure | 2+ | Procedures performed/planned | TP.CC-4 OPCS-4 Procedure Coding Accuracy | 🟡 2 |
| UKCore-ServiceRequest | 2+ | Referrals, tests ordered | TP.WB-3 Field Mapping Accuracy | 🟢 1 |
| UKCore-Patient | 1+ | Patient demographics | TP.WB-3 Field Mapping Accuracy | 🟢 1 |

#### UK-specific Extensions and Terminology Bindings

| UK Core Extension / Binding | Description | Taxonomy Metrics | Tier |
|------------------------------|-------------|-----------------|------|
| NHS Number + NHSNumberVerificationStatus | Primary patient identifier with verification state | TP.WB-3 Field Mapping Accuracy | 🟢 1 |
| EthnicCategory | UK census code system on Patient | *Gap - no specific ethnic category binding metric* | - |
| BirthSex extension | UK-specific sex at birth | *Process criterion - no metric equivalent* | - |
| DeathNotificationStatus | PDS integration | *Gap - no PDS integration metric* | - |
| ResidentialStatus | UK-specific residential state | *Process criterion* | - |
| SNOMED CT primary terminology binding | With CodingSCTDescDisplay extension | TP.CC-1 SNOMED Code Accuracy, TP.CC-2 SNOMED CT Concept Mapping Accuracy | 🟡 2 |
| dm+d for medicinal products | Medication terminology | TP.CC-5 dm+d Medication Coding Accuracy | 🟡 2 |
| NHS Data Dictionary codes | Administrative data | *Process criterion* | - |

**Refinement of existing metrics (interpretation clarification, not content change):**

| Existing Metric | Refinement |
|-----------------|-----------|
| TP.WB-6 FHIR R4 Resource Conformance Rate | "FHIR conformance" for NHS deployment means **UK Core profiles**, not generic FHIR R4. Vendors claiming STU1 compliance cannot write back Composition / Condition / Observation - that is STU2+ capability. Stratify conformance reporting by STU version. |
| TP.WB-7 openEHR Archetype Conformance | openEHR is the alternative to FHIR in some NHS trusts (particularly mental health). Relevance depends on target EPR. |

**Gaps:**
- Per-profile UK Core conformance stratification (aggregate TP.WB-6 doesn't distinguish Composition vs Condition vs Observation conformance)
- UK-specific extension conformance (NHS Number verification status, Ethnic Category, Death Notification, Residential Status)
- STU version targeting documentation (vendors must declare which STU version they support)
- INTEROPen-defined extension conformance (beyond UK Core base)
- PDS integration depth

**Taxonomy extends:** Write-back Safety sub-cluster (TP.WB-1 through TP.WB-4) addresses safety semantics that UK Core profile conformance alone doesn't guarantee. A valid-but-wrong FHIR resource passes conformance but fails fidelity.

---

### CQC Assessment for AI

**Publisher:** Care Quality Commission (CQC)
**Scope:** Deployer-side regulatory inspection covering the Five Key Questions (Safe, Effective, Caring, Responsive, Well-led) under the Single Assessment Framework, with AI-specific guidance in GP Mythbuster 109 and emerging quality statements.
**Mandatory status:** CQC inspection is mandatory for all registered providers; CQC ratings are public and directly affect commissioning.
**AVT relevance:** CQC regulates the *provider using the tool*, not the tool itself. Clinical responsibility is non-delegable to the AI. This mapping covers what CQC inspectors are likely to ask about an AVT deployment.

**⚠️ Emerging area (2025–26):** GP Mythbuster 109 is the published baseline. Formal CQC quality statements specific to AI in primary and secondary care are evolving. This mapping will need review when the CQC AI-specific assessment framework is finalised.

**Key dimensions and taxonomy coverage:**

- **GP Mythbuster 109 baseline assertions:**
  - CQC regulates providers not tools - provider remains accountable for AI output
  - Clinical responsibility non-delegable - clinician must review/sign off before the record is final → covered by HL.HF-3 Review-Before-Signing Rate, HL.HF-1 Edit Rate
  - Record-keeping duty (Regulation 17, good governance) applies unchanged → partial (no specific "record quality" composite metric)
  - AVT consent - implied consent acceptable if patients informed and can dissent → covered by GV.CR-1 Patient Dissent Recording Rate, GV.CR-2 Verbal Notification Compliance, IO.PX-1 Patient Opt-Out Rate
  - Medical device classification considerations → cross-reference to MHRA SaMD section
  - DCB0129/DCB0160 clinical safety case → covered by GV.CR-6 Clinical Safety Case Completeness, GV.SG-17 Hazard Log Completeness
  - DTAC compliance pre-procurement → cross-reference to DTAC section
  - Staff training on AI limitations → covered by GV.TC-1 Clinician Training Completion Rate, GV.TC-2 Failure Mode Awareness Score

- **Safe (Five Key Questions)**: Covered extensively by Safety & Governance group - GV.SG-17 Hazard Log Completeness, GV.SG-11 Adverse Event / Incident Rate (LFPSE), GV.SG-14 Near-Miss Reporting Rate, GV.SG-9 Safety Performance Indicators with Thresholds. Bias audits covered by IO.FE-3 Clinical Domain Performance Variance, TP.ASR-4 Demographic-Disaggregated WER. Rollback capability covered by TP.WB-5 Write-back Rollback Capability.

- **Effective**: Partial - clinical accuracy benchmarking covered by TP.ASR-1 WER, TP.SN-5 Hallucination Rate, TP.CC-1 SNOMED Code Accuracy. Outcome monitoring vs pre-AI baseline partially covered by GV.SG-3 Performance Degradation Detection Latency, IO.PX-9 Downstream Diagnostic Accuracy. Clinician review/sign-off covered by HL.HF-3 Review-Before-Signing Rate. NICE alignment cross-references NICE ESF section.

- **Caring**: Covered by IO.PX-1 Patient Opt-Out Rate, IO.PX-2 Patient-Perceived Accuracy, IO.PX-6 Therapeutic Relationship Impact, IO.PX-7 Full Attentiveness Rate, GV.CR-2 Verbal Notification Compliance. Dignity during recording - gap (no specific metric).

- **Responsive**: Partial - accessibility covered by IO.FE-2 Accent Taxonomy Standardisation, IO.FE-7 Health Literacy Performance Variation. Language coverage covered by TP.DI-6 Code-Switching Detection Rate. Equity audit covered by IO.FE-1 Deployment Equity Index, TP.CC-9 Coding Equity Index. Complaint routes specific to AI - gap.

- **Well-led**: Partial - board-level AI governance - gap. Named accountable director - gap. CSO role covered by GV.CR-6 Clinical Safety Case Completeness. Audit trail covered by GV.VT-4 Audit Trail Completeness. Vendor management covered by GV.VT group (transparency, incident disclosure, sub-processor). Risk register - partial via GV.SG-13 Assurance Debt Accumulation Rate.

- **CSO expectations**: Registered clinician, DCB0129/0160 trained, maintains Clinical Safety Case and Hazard Log, signs off DCB0160 before go-live. Covered procedurally by GV.CR-6 Clinical Safety Case Completeness, GV.SG-17 Hazard Log Completeness. CSO capacity for AI oversight is a gap (no metric).

**Overall position:** CQC assessment is structurally broader than any single standard because it covers the whole provider operation. The taxonomy provides strong measurement coverage for the Safe and Caring dimensions, partial coverage for Effective and Responsive, and weakest coverage for Well-led (board-level governance, named accountability, AI-specific complaint handling). The gaps are concentrated in provider-organisation-level governance mechanisms rather than clinical-AI performance.

**Gaps:**
- Board-level AI governance mechanism
- Named accountable director for AI
- CSO capacity for AI oversight (separate from CSO sign-off)
- Patient complaint handling specific to AI outputs
- Dignity during recording
- AI-specific equity of access auditing (language/accessibility composite)
- Record quality composite (Regulation 17 alignment)

---

### Patient Safety Incident Response Framework (PSIRF)

**Publisher:** NHS England
**Scope:** Systems-based, proportionate response to patient safety incidents, replacing the 2015 Serious Incident Framework.
**Mandatory status:** Mandatory for acute, ambulance, mental health, and community NHS providers since autumn 2023; primary care and independent-sector rollout 2024–26.
**AVT relevance:** PSIRF applies when AI-generated documentation contributes to patient harm. The response should be proportionate and system-based, looking at the whole sociotechnical pipeline (audio → ASR → summariser → clinician review → EPR) rather than blaming the clinician who signed off.

**Key dimensions and taxonomy coverage:**

- **Four PSIRF principles:**
  - **Compassionate engagement** - Gap (no metric for engagement with those affected by AI-related harm)
  - **Systems-based learning** - Partial - PI.E2E-3 Error Propagation / Cascade Analysis, PI.E2E-8 Error Attribution Analysis provide pipeline-level analysis but not the organisation-level learning response
  - **Proportionate response** - Partial - GV.SG-16 SPI Escalation Response Time addresses timeliness but not proportionality
  - **Supportive oversight** - Gap (no metric for board/ICB oversight of AI-related safety learning)

- **Key components:**
  - Patient Safety Incident Response Policy - Process artefact, no metric
  - Patient Safety Incident Response Plan (PSIRP, 12–18 month forward plan) - Process artefact, no metric
  - Patient Safety Incident Response Standards - Process artefact, no metric
  - Patient Safety Incident Investigation (PSII) - Partial via GV.SG-11 Adverse Event / Incident Rate (LFPSE), GV.SG-15 Time-to-Correct

- **Learning response types:**
  - After Action Review (AAR) - Gap
  - MDT Review - Gap
  - PSII (deepest response) - Partial via GV.SG-11 Adverse Event / Incident Rate (LFPSE), PI.E2E-8 Error Attribution Analysis
  - SEIPS-informed analysis - Gap (no metric for whole-system analysis of AI incidents)
  - Swarm huddle / thematic review / horizon scanning - Gap

- **Engagement requirements:**
  - Patients/families (early contact, named liaison, updates, draft review, access to final report) - Gap
  - Staff (psychological support, Just Culture, protection from blame) - Gap
  - Community (thematic issues) - Gap

- **Board oversight:**
  - Named executive lead for patient safety - Gap
  - Quarterly reports on safety themes and learning - Gap
  - PSIRP board sign-off - Gap
  - LFPSE integration - Partial via GV.SG-11 Adverse Event / Incident Rate (LFPSE)

- **Differences from old SI Framework:** PSIRF moves from blame-based RCA to systems thinking; from prescribed investigations to proportionate response; from transactional commissioner sign-off to supportive ICB/NHSE oversight. The taxonomy's existing incident metrics (GV.SG-11, GV.SG-14) capture that an incident occurred but not the organisation's systems-learning response.

**Overall position:** PSIRF complements DCB0129 Stage 7 Incident Management (already mapped). DCB0129 is about documenting the technical safety lifecycle; PSIRF is about organisation-level systems learning from live incidents. The taxonomy captures incident occurrence (GV.SG-11 LFPSE, GV.SG-14 Near-Miss Reporting Rate) and technical attribution (PI.E2E-8 Error Attribution Analysis) but not the PSIRF-required engagement, learning, and oversight responses. This is the clearest governance gap in the existing taxonomy.

**Gaps:**
- Systems-based root cause analysis readiness (SEIPS-informed)
- Compassionate engagement with affected patients/families
- Staff support and Just Culture protection
- Learning implementation tracking (did the learning actually change practice?)
- Board-level patient safety reporting on AI incidents
- Proportionate response type selection (when is AAR appropriate vs PSII?)

---

### PRSB Clinical Documentation Standards

**Publisher:** Professional Record Standards Body (community interest company, endorsed by Royal Colleges)
**Scope:** Semantic structure of clinical records - what information must be recorded and how it relates. Distinct from FHIR/openEHR which define technical transport.
**Mandatory status:** Increasingly expected for NHS-commissioned systems; referenced in NHS Standard Contract. Not yet formally mandatory but becoming de facto standard.
**AVT relevance:** AVT systems generating clinical notes must map their outputs to PRSB structures to ensure interoperability and clinical completeness. PRSB defines the "what" (mandatory information elements); FHIR UK Core defines the "how" (wire format).

**Key dimensions and taxonomy coverage:**

- **Main PRSB standards:**
  - Core Information Standard (CIS) - foundational; gap (no semantic-completeness metric)
  - GP Connect Access Record - gap
  - Outpatient Letter Standard - gap
  - Discharge Summary Standard - gap
  - Mental Health Inpatient Discharge Summary - gap
  - Emergency Care Discharge Summary - gap
  - Transfer of Care Around Medicines (ToCAM) - partial via TP.SN-19 Medication Attribute Extraction F1, TP.SN-21 Medication Event Classification
  - About Me - gap
  - End of Life Care - gap
  - Maternity Record Standard - gap
  - Palliative and End of Life Care - gap

- **Common header set (across standards):**
  - Patient demographics + NHS Number - covered by TP.WB-3 Field Mapping Accuracy
  - Allergies and adverse reactions - covered by TP.WB-1 Write-back Fidelity (specifically flagged), TP.WB-4 Update vs Append Behaviour
  - Medications (current, changes, reason) - covered by TP.SN-19 Medication Attribute Extraction F1, TP.SN-21 Medication Event Classification, TP.CC-5 dm+d Medication Coding Accuracy
  - Problems / diagnoses (SNOMED) - covered by TP.CC-1 SNOMED Code Accuracy, TP.CC-2 SNOMED CT Concept Mapping Accuracy
  - Procedures (OPCS) - covered by TP.CC-4 OPCS-4 Procedure Coding Accuracy
  - Observations / vital signs - partial via TP.WB-3 Field Mapping Accuracy
  - Communication needs (AIS flags, interpreter needs) - gap
  - Consent and preferences - partial via GV.PD-8 Consent Verification Accuracy
  - Legal status (MHA, DoLS, LPA, advance decisions) - gap
  - Clinical narrative (history, examination, assessment, plan) - partial via TP.SN-5 Hallucination Rate, TP.SN-6 Omission Rate, TP.SN-20 Uncertainty Marker Preservation
  - Safety netting - gap

- **Narrative vs structured trade-off:** PRSB explicitly preserves narrative text as valuable and does not mandate full structurisation. The taxonomy captures aspects of this - TP.SN-22 Style & Format Consistency, TP.SN-23 Length Appropriateness - but not the narrative-preservation-vs-structurisation trade-off directly. An AVT that over-structures at the expense of narrative fails the PRSB spirit; an AVT that preserves narrative but fails to populate required coded fields also fails.

- **Cardinality (Mandatory / Required-if-known / Optional):** Every data item in a PRSB standard has cardinality. The taxonomy has no metric for "is mandatory information present in the AVT output?"

- **Royal College endorsement:** AoMRC, RCGP, RCP, RCS, RCEM, RCPsych, RCPCH, RCOG, RCR, RCPath, RCA, RCN, RPS, AHP federation, patient groups. Process criterion, no metric.

- **Relationship to FHIR UK Core:** PRSB data items are explicitly mapped to FHIR UK Core resources/elements in published mapping tables. TP.WB-6 FHIR R4 Resource Conformance Rate partially covers this, but conformance to the wire format doesn't guarantee PRSB semantic completeness.

**Overall position:** PRSB is the clearest gap across all seven new standards. The taxonomy has strong technical integration metrics (TP.WB-1 Write-back Fidelity, TP.WB-3 Field Mapping Accuracy, TP.WB-6 FHIR R4 Resource Conformance) and strong content fidelity metrics (TP.SN-5 Hallucination, TP.SN-6 Omission) but no metric for "does the AVT output include all PRSB-mandatory information elements for the applicable standard?" A PRSB-aware AVT should be able to report per-standard compliance (CIS, Outpatient Letter, Discharge Summary, etc.) as a procurement signal.

**Gaps:**
- PRSB semantic completeness per standard (CIS, Outpatient Letter, Discharge, ToCAM)
- Mandatory information element coverage
- Professional narrative preservation (narrative vs over-structurisation trade-off)
- Communication needs (AIS) information capture
- Legal status information capture (MHA, DoLS, advance decisions)
- Safety netting information capture

---

### Caldicott Principles (2020 revision)

**Publisher:** National Data Guardian (originally Caldicott Report 1997; 2020 revision added Principle 8)
**Scope:** Eight principles governing the use of confidential patient information. Foundational to NHS information governance and the legal basis for DSPT operationalisation.
**Mandatory status:** Not statutory but operationalised through Common Law Duty of Confidentiality, UK GDPR, CQC Regulation 17, and DSPT. Every NHS organisation must have a Caldicott Guardian (mandatory since 1999).
**AVT relevance:** Each Caldicott principle has a direct AVT application - purpose justification in DPIA, minimum necessary data processing, Principle 8 inform-patient obligation mapping to verbal notification and dissent recording.

**Key dimensions and taxonomy coverage:**

- **Principle 1 - Justify the purpose(s)**: Partial - GV.CR-7 DPIA Template Completion Rate evidences purpose documentation, but "justify" is judgement-based. Gap: DPIA justification quality metric.

- **Principle 2 - Use confidential information only when it is necessary**: Partial - GV.PD-4 Data Minimisation Score partially addresses this. Gap: "necessity" judgement metric for AVT processing of specific consultation types (e.g. should AVT be used for safeguarding or mental health consultations?).

- **Principle 3 - Use the minimum necessary confidential information**: Partial - GV.PD-4 Data Minimisation Score addresses aggregate minimisation. Gap: per-data-item necessity documentation.

- **Principle 4 - Access on a strict need-to-know basis**: Covered by GV.VT-7 Sub-Processor Transparency, GV.SC-9 Cross-Patient Information Leakage Rate, GV.VT-4 Audit Trail Completeness.

- **Principle 5 - Everyone aware of their responsibilities**: Covered by GV.TC-1 Clinician Training Completion Rate, GV.TC-2 Failure Mode Awareness Score, GV.TC-3 Refresher Training & CPD Compliance.

- **Principle 6 - Comply with the law**: Covered by GV.CR-6 Clinical Safety Case Completeness, GV.CR-7 DPIA Template Completion Rate, GV.PD-9 Cross-Border Data Transfer Compliance, GV.PD-10 Subject Access Request Fulfilment, GV.PD-11 Right to Erasure Compliance.

- **Principle 7 - Duty to share for individual care**: Covered by TP.WB-1 Write-back Fidelity (ensures generated records flow into EPR for continuity of care), TP.WB-2 Integration Error Rate. The principle is that "AI-generated" is not an excuse to withhold information - the taxonomy ensures the information flows correctly.

- **Principle 8 - Inform patients and service users** *(added 2020)*: Directly covered by GV.CR-1 Patient Dissent Recording Rate, GV.CR-2 Verbal Notification Compliance, GV.CR-3 AI-Generated Content Labelling Compliance, IO.PX-1 Patient Opt-Out Rate. This is the clearest direct mapping between a Caldicott principle and existing taxonomy metrics.

- **Caldicott Guardian role:** Senior person in every NHS organisation, UKCGC-trained, advises on complex IG decisions, represents confidentiality at board level. Distinct from DPO (statutory UK GDPR role) and SIRO (risk ownership). Process role, no metric for Guardian's AI-specific engagement.

- **Relationship to UK GDPR and Common Law Duty of Confidentiality**: Three overlapping regimes. UK GDPR lawful basis does not automatically satisfy the Common Law Duty of Confidentiality; both must be met. Caldicott operationalises the CLDC inside health and care. Existing DSPT mapping covers the statutory floor; Caldicott is the ethical/professional framework on top.

- **National Data Guardian role:** Statutory (Health and Social Care (National Data Guardian) Act 2018). Publishes guidance with "have regard to" obligation. Publications directly relevant: 2020 Caldicott Principles, NDG Data Security Standards (underpin DSPT), public benefit test.

**Overall position:** Caldicott is largely operationalised by DSPT (already mapped). This section makes the strategic governance layer explicit for readers who come from an IG/ethics perspective rather than an operational security one. Principle 8 is the strongest direct mapping to existing metrics; Principles 4–7 are well covered; Principles 1–3 have partial coverage because judgement-based "justification" and "necessity" don't reduce to single metrics.

**Gaps:**
- DPIA justification quality under Principle 1
- Consultation-type appropriateness under Principle 2 (e.g. AVT in safeguarding/MH consultations)
- Per-data-item necessity documentation under Principle 3
- Caldicott Guardian AI-specific engagement (review of AVT deployment by the Guardian)

---

### Gap Summary

Gaps where the taxonomy has no coverage against a standard's requirements:

| Gap | Relevant Standard(s) | Severity |
|-----|----------------------|----------|
| **Web accessibility (WCAG 2.2 AA)** | DTAC D1.4.1 | Low - UI concern, not clinical AI pipeline |
| **Accessible Information Standard** | DTAC D1.3 | Low - UI concern, not clinical AI pipeline |
| **Total cost of ownership / cost-effectiveness** | LLM Framework (Cost), NICE ESF Standard 18 | Medium - relevant to deployment and commissioning decisions |
| **Benchmark relevance decay** | LLM Framework (Benchmark relevance) | Medium - implicit in Meta-evaluation but not explicit |
| **Scalability / concurrency testing** | LLM Framework (Scalability), NICE ESF Standard 21 | Medium - partially covered by latency and uptime |
| **SME involvement depth** | LLM Framework (SME involvement) | Low - taxonomy assigns Responsible Actors but doesn't quantify SME engagement |
| **Few-shot prompt bias** | LLM Framework (Bias - in-context learning) | Low - not applicable to pipeline-based AVT systems |
| **Structured staff feedback mechanism** | LLM Framework (Feedback mechanism) | Low - partially covered by incident reporting |
| **Job security / workforce impact** | LLM Framework (Society) | Low - partially covered by skill attenuation metrics |
| **Medical device classification documentation** | MHRA WP1/WP2 | Medium - process documentation, not performance |
| **PCCP documentation for adaptive algorithms** | MHRA WP11, WP4-04 | Medium - critical for adaptive AVT |
| **PMSR/PSUR report completeness** | MHRA SI 2024 No. 1368 | Medium - regulatory reporting artefact |
| **MHRA Transparency WHAT content items** | MHRA Transparency Principles (June 2024) | Medium - partial coverage; no composite |
| **Silent mode evaluation evidence** | NICE ESF Standard 15 (AI best practice) | Medium - key AI-specific provision |
| **Subgroup drift monitoring composite** | NICE ESF Standard 16 (AI best practice) | Medium - metrics exist but not assembled |
| **Cost-effectiveness / QALY** | NICE ESF Standard 18 | High for Tier C AVT - required for NICE appraisal |
| **Budget impact analysis composite** | NICE ESF Standard 17 | Medium - GV.OP-7 is partial |
| **Per-profile UK Core conformance stratification** | FHIR UK Core | High - aggregate TP.WB-6 is too coarse |
| **UK-specific FHIR extension conformance** | FHIR UK Core | Medium - NHS Number, Ethnic Category, etc. |
| **STU version targeting documentation** | FHIR UK Core | Medium - STU1 cannot write Composition/Condition/Observation |
| **Board-level AI governance mechanism** | CQC Well-led, PSIRF board oversight | High - named accountability |
| **Named accountable director for AI** | CQC Well-led | High - regulatory inspection point |
| **CSO capacity for AI oversight** | CQC Well-led, DCB0129 | Medium - distinct from CSO sign-off |
| **AI-specific patient complaint handling** | CQC Responsive | Medium - emerging inspection requirement |
| **Record quality composite (Reg 17)** | CQC Safe / Well-led (Mythbuster 109) | Medium - Regulation 17 alignment |
| **Systems-based root cause analysis (SEIPS)** | PSIRF | High - PSIRF mandatory approach |
| **Compassionate engagement with affected patients/families** | PSIRF | High - PSIRF principle |
| **Staff Just Culture protection** | PSIRF | Medium - organisation-level |
| **Learning implementation tracking** | PSIRF | Medium - did learning change practice? |
| **PRSB semantic completeness per standard** | PRSB (all standards) | High - clearest gap; no existing metric |
| **Mandatory information element coverage** | PRSB | High - cardinality not measured |
| **Professional narrative preservation** | PRSB | Medium - narrative vs over-structurisation trade-off |
| **Communication needs (AIS) capture** | PRSB | Medium - accessibility information |
| **Legal status information capture** | PRSB | Medium - MHA, DoLS, advance decisions |
| **Safety netting information capture** | PRSB | Medium - safety-critical handoff |
| **DPIA justification quality** | Caldicott Principle 1 | Medium - judgement-based |
| **Consultation-type appropriateness for AVT** | Caldicott Principle 2 | Medium - safeguarding/MH considerations |
| **Per-data-item necessity documentation** | Caldicott Principle 3 | Medium - minimum necessary |
| **Caldicott Guardian AI engagement** | Caldicott (Guardian role) | Low - process, not metric |

Gaps where the taxonomy provides coverage that no standard addresses:

| Taxonomy Coverage | Notes |
|-------------------|-------|
| Audio capture pipeline (9 metrics) | No standard addresses audio quality assurance |
| ASR accuracy and equity (14 metrics) | No standard addresses speech recognition quality |
| Diarisation (9 metrics) | No standard addresses speaker attribution |
| Clinical content fidelity family (5 metrics) | No standard addresses hallucination/omission in clinical AI |
| Post-generation correction family (4 metrics) | No standard addresses human-AI interaction in clinical documentation |
| EPR write-back safety sub-cluster (4 metrics) | DTAC addresses interoperability but not write-back safety semantics |
| Medication Safety Thread family (4 metrics) | No standard addresses medication accuracy across the AI pipeline |
| Demographic Equity Disaggregation family (7 metrics) | Standards require fairness but don't prescribe disaggregation method |
| Meta-evaluation (7 metrics) | No standard addresses measurement science quality |

---

### Proposed New Metrics (Not Yet Implemented)

The mapping exercise identified 28 gap candidates where the taxonomy could be extended with new metrics to close assurance gaps. These are consolidated into the roadmap at [Gaps & Proposed Metrics](#gaps-proposed-metrics-roadmap) alongside gaps from external coverage audits (RSET, NHSE IG) and the Responsible AI lens. The roadmap is the single source of truth; detailed per-standard tables are not duplicated here.

**Quick summary** (28 standards-derived candidates):

| Source Standard | Proposed Metrics | Tier Distribution |
|-----------------|------------------|-------------------|
| MHRA SaMD/AIaMD | 5 | 1 × Tier 1, 4 × Tier 2 |
| NICE ESF | 5 | 1 × Tier 1, 3 × Tier 2, 1 × Tier 3 |
| FHIR UK Core | 3 | 1 × Tier 1, 2 × Tier 2 |
| CQC Assessment | 4 | 1 × Tier 1, 3 × Tier 2 |
| PSIRF | 4 | 3 × Tier 2, 1 × Tier 3 |
| PRSB | 4 | 1 × Tier 1, 3 × Tier 2 |
| Caldicott | 3 | 1 × Tier 1, 1 × Tier 2, 1 × Tier 3 |
| **Total** | **28** | **6 × Tier 1, 19 × Tier 2, 3 × Tier 3** |

Highest-leverage single addition: **TP.WB-11 PRSB Semantic Completeness** - surfaces as a gap across PRSB directly, FHIR UK Core, and CQC record quality with no partial coverage in the existing taxonomy. See the roadmap § 2 for full per-standard entries.

## Responsible AI Lens

This section provides a **policy-intent view** of the taxonomy. Where the [Standards Mapping](#standards-mapping) section maps metrics against specific regulatory criteria (DTAC, DSPT, MHRA, etc.), this lens tags metrics against two complementary policy frameworks:

- **DSIT AI Playbook for the UK Government (Feb 2025)** - 10 principles for responsible AI use across UK public sector
- **Six Responsible AI Ethical Themes** - the AI Regulation White Paper's five principles (Safety/Security/Robustness; Transparency/Explainability; Fairness; Accountability/Governance; Contestability/Redress) plus the Playbook-added sixth theme (Societal Wellbeing)

### Why a separate lens document?

Standards prescribe *what artefacts and processes must exist*. Principles and themes are *policy lenses* - every metric hits multiple principles and themes, the Playbook itself acknowledges trade-offs between them (e.g. collecting demographic data to assess fairness reduces privacy), and the value is cross-tagging rather than 1:1 mapping.

This lens sits alongside:
- The standards mapping (regulatory-requirement view)
- The [applicability classification](#applicability-classification) (AVT-specific vs general AI view)
- The NHS LLM Evaluation Framework's three groups (operationalisation view - already mapped in standards section)

Think of these as four complementary readings of the same 214-metric substrate: **what's required** (standards), **who it applies to** (applicability), **how to measure** (NHS LLM framework), and **why it matters in policy terms** (this lens).

### On trade-offs

The Playbook is explicit that its principles and themes can be in tension:
- Collecting demographic data for fairness assessment may reduce privacy
- A more explainable or fairer algorithm may consume more energy
- Tighter security may reduce usability
- Stronger human oversight may reduce workflow benefit

Metrics in this lens often serve multiple principles/themes - the [Coverage Matrix](#part-c-coverage-matrix) in Part C highlights cross-cutting "policy-lever" metrics where a single measurement supports several assurance goals simultaneously. Metrics are listed against a principle/theme when they genuinely operationalise that principle, not when they merely touch on it.

---

## Part A - DSIT AI Playbook: 10 Principles

The DSIT AI Playbook (February 2025) sets out ten principles for responsible AI use across UK government. While the Playbook targets central government and arm's length bodies, its principles are referenced in NHS AI governance and many of its requirements (notably ATRS transparency publication) cascade to NHS ALBs. The principles are numbered P1–P10 for reference throughout this document.

### Principle 1: You know what AI is and what its limitations are

> *"AI is a broad field subject to rapid research and innovation, and many claims have been made about both its promise and risks."*

**AVT application:** Understanding AVT's inherent limitations - ASR has error rates proportional to audio quality, accent, and clinical vocabulary; LLM-based summarisation can hallucinate; demographic performance varies; outputs require clinical review. Users must know what the system *can't* do, not just what it can.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | Aspect of P1 |
|-----|--------|-------|------|--------------|
| TP.SN-5 | Hallucination Rate | Summarisation / NLP | 🟢 1 | Knowing fabrication rate |
| TP.SN-6 | Omission Rate | Summarisation / NLP | 🟢 1 | Knowing what gets dropped |
| TP.ASR-1 | Word Error Rate (WER) | ASR / Transcription | 🟡 2 | Baseline accuracy limit |
| TP.ASR-2 | Medical Word Error Rate (M-WER) | ASR / Transcription | 🔵 3 | Clinical vocabulary limits |
| TP.ASR-10 | ASR Confidence Calibration | ASR / Transcription | 🟡 2 | How well confidence reflects accuracy |
| TP.ASR-11 | ASR Confidence Exposure | ASR / Transcription | 🟡 2 | Surfacing uncertainty to users |
| TP.SN-20 | Uncertainty Marker Preservation | Summarisation / NLP | 🟢 1 | Preserving clinician hedging |
| TP.AC-3 | Acoustic Environment Profiling | Audio Capture | 🟡 2 | Environment-limit awareness |
| GV.TC-2 | Failure Mode Awareness Score | Training & Competency | 🟡 2 | Clinician understanding of limits |
| ES.ME-1 | Proximal vs Distal Outcome Distinction | Meta-evaluation | 🔵 3 | Understanding what the metric means |

**Gaps:** Limitations disclosure to patients (not just clinicians) - no direct metric. Running-tally of encountered failure modes over time.

### Principle 2: You use AI lawfully, ethically and responsibly

> *"AI solutions bring specific legal and ethical considerations. Your use of AI tools must be lawful and responsible."*

**AVT application:** UK GDPR lawful basis, DPIA completion, equality assessments, IP considerations for training data, environmental impact, proportionality - is AVT the right intervention for this context? Engages legal, compliance, and DP experts early.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | Aspect of P2 |
|-----|--------|-------|------|--------------|
| GV.CR-7 | DPIA Template Completion Rate | NHS Compliance | 🟢 1 | UK GDPR Art 35 compliance |
| GV.CR-6 | Clinical Safety Case Completeness | NHS Compliance | 🟢 1 | Clinical ethics grounding |
| GV.PD-8 | Consent Verification Accuracy | Privacy & Data Gov | 🟢 1 | Lawful basis foundation |
| GV.CR-1 | Patient Dissent Recording Rate | NHS Compliance | 🟢 1 | Respect for patient rights |
| GV.CR-2 | Verbal Notification Compliance | NHS Compliance | 🟢 1 | Transparency of use |
| GV.PD-9 | Cross-Border Data Transfer Compliance | Privacy & Data Gov | 🟢 1 | International lawfulness |
| GV.PD-10 | Subject Access Request Fulfilment | Privacy & Data Gov | 🟢 1 | UK GDPR Art 15 rights |
| GV.PD-11 | Right to Erasure Compliance | Privacy & Data Gov | 🟢 1 | UK GDPR Art 17 rights |
| GV.PD-4 | Data Minimisation Score | Privacy & Data Gov | 🟡 2 | Proportionality of data use |
| IO.PX-1 | Patient Opt-Out Rate | Patient Experience | 🟢 1 | Respect for dissent |
| GV.EN-1 | Energy Consumption per Clinical Note | Environmental | 🔵 3 | Environmental responsibility |
| GV.EN-2 | Carbon Emissions per Inference | Environmental | 🔵 3 | Environmental responsibility |
| TP.SN-24 | Stigmatising Language Replication Rate | Summarisation / NLP | 🟡 2 | Ethical content generation |

**Gaps:** IP status of training data (not directly measured). Proportionality review (is AVT the right tool for this use case - covered partially by ES.ME-1 but not as a procurement gate).

### Principle 3: You know how to use AI securely

> *"When building and deploying AI services, you must make sure that they are secure to use and resilient to cyber attacks."*

**AVT application:** AI-specific threats - prompt injection via dictated content, data poisoning of fine-tuning sets, audio-channel adversarial attacks, PHI leakage through model outputs, cross-patient information contamination. Secure by Design alignment.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | Aspect of P3 |
|-----|--------|-------|------|--------------|
| GV.SC-1 | Prompt Injection Resistance Rate | Security | 🟡 2 | AI-specific threat |
| GV.SC-2 | Jailbreak Resistance Score | Security | 🟡 2 | Bypass resistance |
| GV.SC-3 | Adversarial Audio Detection Rate | Security | 🔵 3 | AVT-specific threat |
| GV.SC-4 | Data Poisoning Resilience | Security | 🔵 3 | Training-time threat |
| GV.SC-5 | Output Safety Classifier Coverage | Security | 🟡 2 | Output safeguards |
| GV.SC-6 | Template Injection Vulnerability Assessment | Security | 🟡 2 | Template-layer threats |
| GV.SC-7 | Voice Cloning / Deepfake Detection | Security | 🔵 3 | Audio authenticity |
| GV.SC-8 | Side-Channel Data Leakage | Security | 🟡 2 | Information leakage |
| GV.SC-9 | Cross-Patient Information Leakage Rate | Security | 🟡 2 | Cross-contamination |
| GV.SC-10 | Clinician Identity Authentication | Security | 🟡 2 | Access control |
| GV.SC-11 | Membership Inference Attack AUC | Security | 🔵 3 | Privacy attack resistance |
| GV.PD-5 | PII Extraction Attack Success Rate | Privacy & Data Gov | 🟡 2 | PII threat resistance |

**Gaps:** Supply-chain security for model weights and dependencies. AI-specific red-teaming cadence (how often is security re-tested?).

### Principle 4: You have meaningful human control at the right stages

> *"You need to monitor the AI's behaviour and have plans in place to prevent any harmful effects on users."*

**AVT application:** Clinician-in-the-loop review before signing off AI-generated notes into the EPR; ability to edit freely; ability to reject; live monitoring of edit patterns as a signal of AI drift; fallback to manual documentation if AVT fails.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | Aspect of P4 |
|-----|--------|-------|------|--------------|
| HL.HF-3 | Review-Before-Signing Rate | Human Factors | 🟢 1 | Core human control |
| HL.HF-1 | Edit Rate (% Notes Edited) | Human Factors | 🟢 1 | Evidence of meaningful review |
| HL.HF-4 | Time-to-Sign Distribution | Human Factors | 🟢 1 | Review time sufficiency |
| HL.HF-2 | Edit Type Classification | Human Factors | 🟡 2 | Depth of review |
| HL.HF-6 | Automation Bias Detection (Error Injection) | Human Factors | 🟡 2 | Detecting over-reliance |
| HL.HF-7 | Edit Location Distribution | Human Factors | 🟡 2 | Where humans intervene most |
| HL.HF-8 | Trust Calibration Survey | Human Factors | 🟡 2 | Appropriate trust level |
| HL.HF-17 | Verification Burden | Human Factors | 🟡 2 | Cognitive cost of oversight |
| HL.HF-19 | AI-Off Performance Test | Human Factors | 🟡 2 | Graceful degradation |
| HL.HF-9 | Re-record / Abandonment Rate | Human Factors | 🟡 2 | User-initiated override |
| TP.WB-5 | Write-back Rollback Capability | EPR Write-back | 🟡 2 | Reversibility after error |

**Gaps:** Formal escalation paths when AI output is rejected. Board-level visibility of aggregate override patterns.

### Principle 5: You understand how to manage the full AI life cycle

> *"AI solutions, like other technology deployments, have a full product life cycle that you need to understand."*

**AVT application:** Pre-deployment validation, go-live gates, continuous monitoring for drift and bias, model version tracking, update impact assessment, retraining protocols, decommissioning. Aligned with Technology Code of Practice.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | Aspect of P5 |
|-----|--------|-------|------|--------------|
| GV.SG-1 | Model Version Tracking | Safety & Governance | 🟢 1 | Lifecycle foundation |
| GV.SG-2 | Model Update Impact Score | Safety & Governance | 🟡 2 | Change impact |
| GV.SG-3 | Performance Degradation Detection Latency | Safety & Governance | 🟡 2 | Drift detection speed |
| GV.SG-4 | Retraining Trigger Threshold Specification | Safety & Governance | 🟡 2 | When to retrain |
| GV.SG-5 | AI-Generated Data Contamination Rate | Safety & Governance | 🔵 3 | Training data integrity |
| GV.SG-6 | Concept Drift in Clinical Notes | Safety & Governance | 🔵 3 | Semantic drift |
| GV.SG-7 | Probabilistic Risk Quantification (P₁/P₂) | Safety & Governance | 🔵 3 | Risk quantification |
| GV.SG-9 | Safety Performance Indicators with Thresholds (DSCMS) | Safety & Governance | 🟢 1 | Ongoing safety |
| GV.VT-1 | Model Change Notification Compliance | Vendor Transparency | 🟢 1 | Vendor lifecycle cooperation |
| GV.CR-9 | FDA PCCP-Equivalent Pre-Defined Acceptance Criteria | NHS Compliance | 🟡 2 | Pre-defined change control |
| GV.CR-10 | EU AI Act Event Logging Compliance | NHS Compliance | 🟡 2 | Lifecycle event tracking |

**Gaps:** Decommissioning plan (no metric). Model retirement criteria.

### Principle 6: You use the right tool for the job

> *"You should select the most appropriate technology to meet your needs. AI is good at many tasks, but there are a wide range of models and products."*

**AVT application:** Is AVT the right tool? For which consultation types - not all? Should it be template-driven structured notes or full LLM summarisation? Small model or frontier? Procurement should compare AVT against non-AI alternatives (dictation, typing, templated notes).

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | Aspect of P6 |
|-----|--------|-------|------|--------------|
| ES.ME-1 | Proximal vs Distal Outcome Distinction | Meta-evaluation | 🔵 3 | Is AVT solving the right problem? |
| ES.ME-3 | Metric Interaction Analysis | Meta-evaluation | 🔵 3 | Are metrics telling a coherent story? |
| GV.OP-6 | Adoption Rate & Selective Use Patterns | Operational | 🟢 1 | Where clinicians choose to use AVT |
| GV.OP-1 | Documentation Time per Consultation | Operational | 🟢 1 | Comparison vs manual |
| GV.OP-7 | Cost per Consultation | Operational | 🟡 2 | Cost-benefit signal |
| GV.TC-2 | Failure Mode Awareness Score | Training & Competency | 🟡 2 | When not to use |
| HL.HF-9 | Re-record / Abandonment Rate | Human Factors | 🟡 2 | Signal of inappropriate fit |

**Gaps:** Formal comparison against non-AI alternatives (no metric). Procurement-stage tool-fit assessment.

### Principle 7: You are open and collaborative

> *"There are many teams across government and the wider public sector using or exploring AI tools in their work."*

**AVT application:** Publishing AVT use in the Algorithmic Transparency Recording Standard (ATRS) where applicable; patient-facing disclosure of AVT use; benchmark data shared; engaging with civil society, patient groups, and academic community.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | Aspect of P7 |
|-----|--------|-------|------|--------------|
| GV.CR-3 | AI-Generated Content Labelling Compliance | NHS Compliance | 🟢 1 | Output disclosure (parallel to ATRS for records) |
| GV.CR-2 | Verbal Notification Compliance | NHS Compliance | 🟢 1 | Patient-facing transparency |
| GV.CR-4 | AVT Supplier Registry Listing Verification | NHS Compliance | 🟢 1 | Registry transparency |
| GV.CR-5 | ICB Engagement Documentation | NHS Compliance | 🟢 1 | Cross-organisational transparency |
| GV.VT-1 | Model Change Notification Compliance | Vendor Transparency | 🟢 1 | Vendor-to-deployer openness |
| GV.VT-2 | Telemetry Provision Completeness | Vendor Transparency | 🟡 2 | Observability |
| GV.VT-3 | Benchmark & Evaluation Data Accessibility | Vendor Transparency | 🔵 3 | Reproducibility |
| GV.VT-7 | Sub-Processor Transparency | Vendor Transparency | 🟢 1 | Supply chain openness |
| GV.VT-8 | Intermediate Output Access | Vendor Transparency | 🟡 2 | Observability of internal state |

**Gaps:** ATRS publication completeness (no direct metric - ATRS may not apply to all NHS deployments). Patient-facing plain-language documentation.

### Principle 8: You work with commercial colleagues from the start

> *"AI is a rapidly developing market, and you should get specific advice from commercial colleagues on the implications for your project."*

**AVT application:** Vendor contracts should require the same ethical standards as in-house systems; contract clauses for transparency, auditability, incident disclosure; procurement via DTAC-compliant routes; supplier-registry verification.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | Aspect of P8 |
|-----|--------|-------|------|--------------|
| GV.VT-1 | Model Change Notification Compliance | Vendor Transparency | 🟢 1 | Contractual cooperation |
| GV.VT-4 | Audit Trail Completeness | Vendor Transparency | 🟡 2 | Contractual auditability |
| GV.VT-5 | Incident Disclosure Compliance | Vendor Transparency | 🟢 1 | Contractual disclosure |
| GV.VT-6 | Exit & Data Portability Provisions | Vendor Transparency | 🟡 2 | Exit strategy |
| GV.VT-7 | Sub-Processor Transparency | Vendor Transparency | 🟢 1 | Supply chain management |
| GV.VT-8 | Intermediate Output Access | Vendor Transparency | 🟡 2 | Contractual observability |
| GV.CR-4 | AVT Supplier Registry Listing Verification | NHS Compliance | 🟢 1 | Procurement eligibility |
| GV.CR-9 | FDA PCCP-Equivalent Pre-Defined Acceptance Criteria | NHS Compliance | 🟡 2 | Change control clauses |
| GV.OP-7 | Cost per Consultation | Operational | 🟡 2 | Commercial performance |

**Gaps:** Contractual SLA enforcement (no metric for whether SLAs are actually enforced). Exit-clause testing.

### Principle 9: You have the skills and expertise needed to implement and use AI

> *"You should understand the technical and ethical requirements for using AI tools and have them in place within your team."*

**AVT application:** Clinician training on AVT capabilities and limitations; failure-mode awareness; refresher training as models update; SRO/board understanding of AI-specific risks; prompt-craft literacy where applicable.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | Aspect of P9 |
|-----|--------|-------|------|--------------|
| GV.TC-1 | Clinician Training Completion Rate | Training & Competency | 🟢 1 | Foundational skill coverage |
| GV.TC-2 | Failure Mode Awareness Score | Training & Competency | 🟡 2 | Deep understanding |
| GV.TC-3 | Refresher Training & CPD Compliance | Training & Competency | 🟡 2 | Maintained currency |
| GV.TC-4 | Trainee Impact Assessment | Training & Competency | 🔵 3 | Training downstream users |
| GV.TC-5 | Training Material Currency | Training & Competency | 🟡 2 | Material kept current |
| GV.OP-9 | Training Time per Clinician | Operational | 🟡 2 | Training investment |
| HL.HF-8 | Trust Calibration Survey | Human Factors | 🟡 2 | Appropriately calibrated trust |

**Gaps:** SRO / board-level AI literacy assessment. Data scientist / engineering skills on the deployer side.

### Principle 10: You use these principles alongside your organisation's policies and have the right assurance in place

> *"These principles and this playbook set out a consistent approach... While you should use these principles when working with AI, many government organisations have their own governance structures and policies in place."*

**AVT application:** Alignment with trust-level AI safety committee, clinical safety case sign-off, DCB0129/0160 compliance, early engagement with assurance teams, documented review and escalation.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | Aspect of P10 |
|-----|--------|-------|------|---------------|
| GV.CR-6 | Clinical Safety Case Completeness | NHS Compliance | 🟢 1 | Org-specific safety assurance |
| GV.SG-17 | Hazard Log Completeness | Safety & Governance | 🟢 1 | DCB0129/0160 alignment |
| GV.CR-5 | ICB Engagement Documentation | NHS Compliance | 🟢 1 | Regional governance alignment |
| GV.SG-13 | Assurance Debt Accumulation Rate | Safety & Governance | 🟢 1 | Assurance-gap tracking |
| GV.SG-14 | Near-Miss Reporting Rate | Safety & Governance | 🟢 1 | Learning system |
| GV.SG-15 | Time-to-Correct | Safety & Governance | 🟡 2 | Responsive assurance |
| GV.SG-16 | SPI Escalation Response Time | Safety & Governance | 🟡 2 | Escalation mechanism |
| GV.VT-4 | Audit Trail Completeness | Vendor Transparency | 🟡 2 | Assurance evidence base |

**Gaps:** AI review board effectiveness metric. Integration with existing risk management (enterprise risk register alignment).

---

## Part B - Six Responsible AI Ethical Themes

The AI Regulation White Paper (March 2023) articulated five cross-sectoral principles for responsible AI; the DSIT AI Playbook (Feb 2025) ethics chapter extends this with a sixth theme (Societal Wellbeing and Public Good). These six themes are the **policy-intent axes** that the more operational NHS LLM Evaluation Framework's three groups (Suitability in Context, Wider Impact, Quantifiable Changes) help measure. The themes are labelled T1–T6 for reference.

### Theme 1: Safety, Security and Robustness

> *"AI systems should function in a robust, secure and safe way throughout the AI life cycle, and risks should be continually identified, assessed and managed."*

**Source:** AI Regulation White Paper Principle 1
**AVT application:** Clinical safety cases (DCB0129/0160), adversarial robustness to prompt injection, audio-capture reliability, end-to-end hallucination rate, model drift, degraded-mode behaviour.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | How the metric serves T1 |
|-----|--------|-------|------|--------------------------|
| TP.SN-5 | Hallucination Rate | Summarisation / NLP | 🟢 1 | Content safety |
| TP.SN-6 | Omission Rate | Summarisation / NLP | 🟢 1 | Content safety |
| TP.ASR-12 | Hallucination-Under-Noise Rate | ASR / Transcription | 🟢 1 | Robustness under degraded input |
| TP.WB-1 | Write-back Fidelity | EPR Write-back | 🟢 1 | Safety at integration boundary |
| TP.WB-3 | Field Mapping Accuracy | EPR Write-back | 🟢 1 | Safety-critical field routing |
| TP.WB-4 | Update vs Append Behaviour | EPR Write-back | 🟢 1 | Data integrity safety |
| GV.SG-9 | Safety Performance Indicators with Thresholds (DSCMS) | Safety & Governance | 🟢 1 | Ongoing safety threshold monitoring |
| GV.SG-11 | Adverse Event / Incident Rate (LFPSE) | Safety & Governance | 🟢 1 | Incident tracking |
| GV.SG-14 | Near-Miss Reporting Rate | Safety & Governance | 🟢 1 | Precursor signal |
| GV.SG-17 | Hazard Log Completeness | Safety & Governance | 🟢 1 | Risk identification completeness |
| GV.SG-3 | Performance Degradation Detection Latency | Safety & Governance | 🟡 2 | Drift robustness |
| GV.SC-1 | Prompt Injection Resistance Rate | Security | 🟡 2 | Security |
| GV.SC-2 | Jailbreak Resistance Score | Security | 🟡 2 | Security |
| GV.SC-3 | Adversarial Audio Detection Rate | Security | 🔵 3 | Audio-channel security |
| GV.CR-6 | Clinical Safety Case Completeness | NHS Compliance | 🟢 1 | Foundational safety assurance |
| PI.E2E-3 | Error Propagation / Cascade Analysis | End-to-End Pipeline | 🔵 3 | Systemic robustness |
| HL.HF-19 | AI-Off Performance Test | Human Factors | 🟡 2 | Graceful degradation |

**Relationship to other themes:** Overlaps with T4 (Accountability - who is responsible for safety?) and T5 (Contestability - what recourse when safety fails?). Trade-off with T3 (Fairness): safety monitoring may require demographic data collection.

### Theme 2: Appropriate Transparency and Explainability

> *"AI systems should be appropriately transparent and explainable."*

**Source:** AI Regulation White Paper Principle 2
**AVT application:** ATRS publication where applicable, patient-facing disclosure of AVT use, clinician-facing confidence exposure, uncertainty marker preservation, model cards, system cards, audit trails. Proportionate to risk - different audiences need different explanation types.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | How the metric serves T2 |
|-----|--------|-------|------|--------------------------|
| TP.ASR-11 | ASR Confidence Exposure | ASR / Transcription | 🟡 2 | Transparency to clinician |
| TP.SN-20 | Uncertainty Marker Preservation | Summarisation / NLP | 🟢 1 | Clinical uncertainty transparency |
| TP.SN-12 | Linked Evidence / Provenance Tracing | Summarisation / NLP | 🟡 2 | Explainability of output |
| GV.CR-2 | Verbal Notification Compliance | NHS Compliance | 🟢 1 | Patient-facing transparency |
| GV.CR-3 | AI-Generated Content Labelling Compliance | NHS Compliance | 🟢 1 | Record-level transparency |
| GV.VT-1 | Model Change Notification Compliance | Vendor Transparency | 🟢 1 | Model lifecycle transparency |
| GV.VT-2 | Telemetry Provision Completeness | Vendor Transparency | 🟡 2 | Observability |
| GV.VT-3 | Benchmark & Evaluation Data Accessibility | Vendor Transparency | 🔵 3 | Evidence transparency |
| GV.VT-4 | Audit Trail Completeness | Vendor Transparency | 🟡 2 | Auditability |
| GV.VT-7 | Sub-Processor Transparency | Vendor Transparency | 🟢 1 | Supply chain transparency |
| GV.VT-8 | Intermediate Output Access | Vendor Transparency | 🟡 2 | Internal-state transparency |
| PI.PP-5 | Epistemic Status Preservation | Partial-Pipeline | 🔵 3 | Preserving epistemic transparency |

**Relationship to other themes:** Overlaps with T4 (Accountability - transparency enables accountability). Trade-off with T1 (Security): too much transparency may expose attack surfaces. Trade-off with data minimisation (Caldicott Principle 3): audit trails vs minimisation.

### Theme 3: Fairness

> *"AI systems should not undermine the legal rights of individuals or organisations, discriminate unfairly against individuals or create unfair market outcomes."*

**Source:** AI Regulation White Paper Principle 3
**AVT application:** WER parity across accent/dialect/age/gender; summarisation fidelity parity; equity of access; demographic subgroup monitoring; non-discrimination in high-impact decisions. Equality Act 2010 and UK GDPR compliance.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | How the metric serves T3 |
|-----|--------|-------|------|--------------------------|
| TP.ASR-4 | Demographic-Disaggregated WER | ASR / Transcription | 🟡 2 | Fairness at transcription layer |
| TP.ASR-5 | Speaker-Stratified WER | ASR / Transcription | 🔵 3 | Role-based fairness |
| TP.CC-9 | Coding Equity Index | Clinical Coding | 🟡 2 | Fairness at coding layer |
| PI.E2E-5 | Compound Demographic Performance | End-to-End Pipeline | 🔵 3 | Pipeline-level fairness |
| IO.FE-1 | Deployment Equity Index | Fairness & Equity | 🟡 2 | Access-equity |
| IO.FE-2 | Accent Taxonomy Standardisation | Fairness & Equity | 🟡 2 | Equity measurement foundation |
| IO.FE-3 | Clinical Domain Performance Variance | Fairness & Equity | 🟡 2 | Domain-level fairness |
| IO.FE-4 | Intersectional Performance | Fairness & Equity | 🔵 3 | Intersectional fairness |
| IO.FE-5 | Intersectional Compound Fairness Score | Fairness & Equity | 🔵 3 | Composite intersectional |
| IO.FE-6 | Rare Presentation Handling | Fairness & Equity | 🔵 3 | Edge-case equity |
| IO.FE-7 | Health Literacy Performance Variation | Fairness & Equity | 🔵 3 | Literacy equity |
| IO.FE-8 | Cross-Platform Fairness Consistency | Fairness & Equity | 🔵 3 | Platform equity |
| IO.PX-4 | Cultural & Linguistic Appropriateness | Patient Experience | 🔵 3 | Cultural fit |
| TP.SN-24 | Stigmatising Language Replication Rate | Summarisation / NLP | 🟡 2 | Non-discrimination in output |

**Relationship to other themes:** Trade-off with T2 (Transparency around demographic-data collection): fairness assessment requires demographic data, which reduces privacy. Trade-off with T1 (Safety): safety floors may be set based on fairness gaps. Overlaps with T6 (Societal Wellbeing): fairness is part of societal benefit.

### Theme 4: Accountability and Governance

> *"Governance measures should be in place to ensure effective oversight of the supply and use of AI systems, with clear lines of accountability established across the AI life cycle."*

**Source:** AI Regulation White Paper Principle 4
**AVT application:** Clinical Safety Officer sign-off, SRO designation, vendor contract accountability, DTAC assurance, audit trails, AI review board, PSIRF organisation-level oversight.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | How the metric serves T4 |
|-----|--------|-------|------|--------------------------|
| GV.CR-5 | ICB Engagement Documentation | NHS Compliance | 🟢 1 | Regional governance |
| GV.CR-6 | Clinical Safety Case Completeness | NHS Compliance | 🟢 1 | Safety accountability |
| GV.CR-7 | DPIA Template Completion Rate | NHS Compliance | 🟢 1 | Data protection accountability |
| GV.SG-1 | Model Version Tracking | Safety & Governance | 🟢 1 | Traceability |
| GV.SG-13 | Assurance Debt Accumulation Rate | Safety & Governance | 🟢 1 | Governance-gap tracking |
| GV.SG-17 | Hazard Log Completeness | Safety & Governance | 🟢 1 | Safety accountability |
| GV.VT-1 | Model Change Notification Compliance | Vendor Transparency | 🟢 1 | Vendor accountability |
| GV.VT-4 | Audit Trail Completeness | Vendor Transparency | 🟡 2 | Auditability for accountability |
| GV.VT-5 | Incident Disclosure Compliance | Vendor Transparency | 🟢 1 | Vendor disclosure |
| GV.VT-7 | Sub-Processor Transparency | Vendor Transparency | 🟢 1 | Supply-chain accountability |
| GV.CR-10 | EU AI Act Event Logging Compliance | NHS Compliance | 🟡 2 | Regulatory accountability |
| GV.CR-4 | AVT Supplier Registry Listing Verification | NHS Compliance | 🟢 1 | Procurement accountability |

**Relationship to other themes:** Overlaps with T5 (Contestability: accountability enables contestation). Overlaps with T2 (Transparency enables accountability). Distinct from T1 (Safety is what is governed; accountability is how governance is structured).

### Theme 5: Contestability and Redress

> *"Where appropriate, users, impacted third parties and actors in the AI life cycle should be able to contest an AI decision or outcome that is harmful or creates material risk of harm."*

**Source:** AI Regulation White Paper Principle 5
**AVT application:** Patient route to challenge note content; clinician override capability; incident reporting workflow; complaint pipeline; redress for documentation errors; rollback capability.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | How the metric serves T5 |
|-----|--------|-------|------|--------------------------|
| IO.PX-1 | Patient Opt-Out Rate | Patient Experience | 🟢 1 | Patient-level contestability |
| GV.CR-1 | Patient Dissent Recording Rate | NHS Compliance | 🟢 1 | Documented dissent |
| GV.PD-10 | Subject Access Request Fulfilment | Privacy & Data Gov | 🟢 1 | Right to see the record |
| GV.PD-11 | Right to Erasure Compliance | Privacy & Data Gov | 🟢 1 | Right to delete |
| HL.HF-9 | Re-record / Abandonment Rate | Human Factors | 🟡 2 | Clinician override evidence |
| HL.HF-1 | Edit Rate (% Notes Edited) | Human Factors | 🟢 1 | Clinician contestability |
| GV.SG-15 | Time-to-Correct | Safety & Governance | 🟡 2 | Redress speed |
| GV.VT-5 | Incident Disclosure Compliance | Vendor Transparency | 🟢 1 | Incident-level redress signal |
| GV.VT-6 | Exit & Data Portability Provisions | Vendor Transparency | 🟡 2 | Organisation-level redress |
| TP.WB-5 | Write-back Rollback Capability | EPR Write-back | 🟡 2 | Technical redress |
| HL.HF-17 | Verification Burden | Human Factors | 🟡 2 | Cost of contestability |

**Relationship to other themes:** Overlaps with T4 (Accountability - contestability requires clear accountability). Overlaps with T2 (Transparency - you must see to contest). Trade-off with T1 (Safety - too-easy reversal may allow errors to propagate before correction).

### Theme 6: Societal Wellbeing and Public Good

> *"AI should deliver positive broader societal impact, use resources proportionately, and avoid deployment where harm outweighs benefit."*

**Source:** DSIT AI Playbook ethics chapter (Playbook-added sixth theme; not in original White Paper five)
**AVT application:** Environmental/compute footprint, equity of benefit distribution across practices, workforce impact (burnout relief vs deskilling), patient trust at population level, sustainability of adoption at scale, therapeutic relationship impact. This is the theme most distinct from operational performance - it asks whether AVT's deployment makes NHS healthcare better overall, including second-order effects.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | How the metric serves T6 |
|-----|--------|-------|------|--------------------------|
| GV.EN-1 | Energy Consumption per Clinical Note | Environmental | 🔵 3 | Environmental sustainability |
| GV.EN-2 | Carbon Emissions per Inference | Environmental | 🔵 3 | Environmental sustainability |
| GV.EN-3 | Water Consumption per Query | Environmental | 🔵 3 | Environmental sustainability |
| IO.FE-1 | Deployment Equity Index | Fairness & Equity | 🟡 2 | Access equity (societal) |
| IO.PX-6 | Therapeutic Relationship Impact | Patient Experience | 🔵 3 | Doctor-patient relationship |
| IO.PX-5 | Chilling Effect Assessment | Patient Experience | 🔵 3 | Patient willingness to disclose |
| HL.HF-12 | Clinical Documentation Skill Attenuation | Human Factors | 🔵 3 | Workforce deskilling |
| HL.HF-13 | Cognitive Offloading Rate | Human Factors | 🔵 3 | Workforce dependence |
| HL.HF-10 | Cognitive Load Assessment | Human Factors | 🔵 3 | Workforce wellbeing (reducing burnout) |
| GV.OP-1 | Documentation Time per Consultation | Operational | 🟢 1 | Workforce time impact |
| GV.OP-2 | Pyjama Time / After-Hours EHR Use | Operational | 🟡 2 | Workforce wellbeing |
| GV.TC-4 | Trainee Impact Assessment | Training & Competency | 🔵 3 | Future workforce development |

**Relationship to other themes:** Overlaps with T3 (Fairness - equity is part of societal wellbeing). Partial overlap with T1 (Safety - population-level safety is societal). Distinct from T2/T4/T5 (process-focused themes). **This is the theme with the highest concentration of Tier 3 metrics**, reflecting that societal effects are intrinsically harder to measure than operational performance.

---

## Part C - Coverage Matrix

Some metrics serve multiple Playbook principles *and* multiple ethical themes simultaneously. These are **policy-lever metrics** - a single measurement supports several assurance goals at once, making them high-leverage procurement and governance signals. Implementing or monitoring these metrics gives the broadest coverage for the least measurement burden.

The matrix below lists metrics that genuinely operationalise **3 or more principles** *or* **3 or more themes**. Metrics serving only 1–2 principles/themes are listed in the per-principle and per-theme tables in Parts A and B but not repeated here.

### High cross-cutting metrics (policy-lever)

| Ref | Metric | Tier | Playbook Principles | Ethical Themes | Why cross-cutting |
|-----|--------|------|--------------------|-----------------|--------------------|
| TP.SN-5 | Hallucination Rate | 🟢 1 | P1, P4, P5 | T1, T2 | Core content integrity - limits-awareness, human-control trigger, lifecycle drift signal, safety, transparency of fabrication |
| TP.SN-6 | Omission Rate | 🟢 1 | P1, P4, P5 | T1, T2 | Parallel to hallucination - what the system loses is as important as what it fabricates |
| TP.SN-20 | Uncertainty Marker Preservation | 🟢 1 | P1, P4 | T1, T2 | Preserves clinical uncertainty for human decision-making; transparency about confidence |
| HL.HF-1 | Edit Rate (% Notes Edited) | 🟢 1 | P1, P4, P5 | T2, T5 | Evidence of meaningful human review, running signal of model fit, contestability evidence |
| HL.HF-3 | Review-Before-Signing Rate | 🟢 1 | P4, P10 | T4, T5 | Core human control + accountability trail + contestability foundation |
| HL.HF-6 | Automation Bias Detection (Error Injection) | 🟡 2 | P1, P4, P9 | T1, T2 | Reveals user over-reliance, triggers training updates, safety and transparency interplay |
| HL.HF-8 | Trust Calibration Survey | 🟡 2 | P1, P4, P9 | T2, T5 | Calibrated trust is necessary for meaningful control, skills-check, and contestability |
| GV.CR-1 | Patient Dissent Recording Rate | 🟢 1 | P2, P7 | T4, T5 | Lawfulness, transparency, accountability, contestability all converge here |
| GV.CR-2 | Verbal Notification Compliance | 🟢 1 | P2, P7 | T2, T4 | Patient-facing transparency, lawfulness, accountability |
| GV.CR-3 | AI-Generated Content Labelling Compliance | 🟢 1 | P2, P7 | T2, T4, T5 | Record-level transparency enabling audit, contestation, and regulatory compliance |
| GV.CR-6 | Clinical Safety Case Completeness | 🟢 1 | P2, P5, P10 | T1, T4 | Lawfulness, lifecycle, organisational assurance, safety, accountability |
| GV.CR-7 | DPIA Template Completion Rate | 🟢 1 | P2, P10 | T4 | Lawfulness + organisational assurance + accountability |
| GV.SG-1 | Model Version Tracking | 🟢 1 | P5, P10 | T4 | Lifecycle foundation enabling accountability |
| GV.SG-9 | Safety Performance Indicators with Thresholds (DSCMS) | 🟢 1 | P5, P10 | T1, T4 | Lifecycle monitoring + organisational assurance + safety + accountability |
| GV.SG-11 | Adverse Event / Incident Rate (LFPSE) | 🟢 1 | P4, P5, P10 | T1, T4, T5 | Very high cross-cutting - incidents feed every theme |
| GV.SG-14 | Near-Miss Reporting Rate | 🟢 1 | P4, P5, P10 | T1, T4 | Precursor signal across multiple concerns |
| GV.SG-17 | Hazard Log Completeness | 🟢 1 | P2, P5, P10 | T1, T4 | DCB0129/0160 foundation, ethical grounding, organisational assurance |
| GV.VT-1 | Model Change Notification Compliance | 🟢 1 | P5, P7, P8 | T2, T4 | Lifecycle + openness + commercial + transparency + accountability |
| GV.VT-4 | Audit Trail Completeness | 🟡 2 | P3, P8, P10 | T2, T4, T5 | Foundational auditability serving multiple downstream goals |
| GV.VT-5 | Incident Disclosure Compliance | 🟢 1 | P7, P8 | T4, T5 | Openness + commercial + accountability + contestability |
| GV.VT-7 | Sub-Processor Transparency | 🟢 1 | P7, P8 | T2, T4 | Supply-chain openness + commercial accountability |
| GV.PD-8 | Consent Verification Accuracy | 🟢 1 | P2, P7 | T2, T4 | Lawful basis + transparency + accountability |
| IO.PX-1 | Patient Opt-Out Rate | 🟢 1 | P2, P4, P7 | T3, T5 | Lawful basis, human control at patient level, openness, fairness of access, contestability |
| GV.TC-2 | Failure Mode Awareness Score | 🟡 2 | P1, P6, P9 | T1, T2 | Understanding limits + right-tool assessment + skills + safety + transparency |
| TP.WB-1 | Write-back Fidelity | 🟢 1 | P3, P4, P5 | T1, T4 | Safety-critical integration point across multiple axes |

### Patterns in the matrix

**Highest cross-cutting metrics (5 principles/themes or more):**
- GV.SG-11 Adverse Event / Incident Rate (LFPSE) - 6 axes
- GV.VT-4 Audit Trail Completeness - 6 axes
- GV.CR-3 AI-Generated Content Labelling Compliance - 5 axes
- HL.HF-1 Edit Rate - 5 axes
- IO.PX-1 Patient Opt-Out Rate - 5 axes

These five metrics are the "policy-lever megas" - implementing and monitoring them captures a disproportionate share of the responsible-AI requirement space. They should be the backbone of any AVT assurance programme.

**Concentration by group:**
- Safety & Governance, NHS Compliance & Regulatory, and Vendor Transparency groups dominate the cross-cutting list
- Content fidelity metrics (TP.SN-5, TP.SN-6, TP.SN-20) are the only Part A metrics that reach 4+ axes - reflecting how clinical content integrity sits at the intersection of safety, transparency, limits-awareness, and human control
- Human Factors metrics (HL.HF-1, HL.HF-3, HL.HF-6, HL.HF-8) are heavily cross-cutting because human-AI interaction intersects every principle

**Tier distribution:** Nearly all cross-cutting metrics are Tier 1 or Tier 2. This is expected - the most load-bearing assurance metrics are the ones that multiple principles converge on.

---

## Part D - Gaps

Gap analysis has been consolidated into the single roadmap at [Gaps & Proposed Metrics](#gaps-proposed-metrics-roadmap) § 3 (Responsible AI Lens). 38 candidates are tracked there: 20 organised by Playbook principle, 18 organised by ethical theme. Cross-references to standards-mapping gaps (e.g. PSIRF → GV.SG-19, CQC → GV.CR-12) are preserved in the roadmap. Highest-severity cross-cutting findings are summarised below.

### Summary

**Highest-severity cross-cutting gaps (appear in multiple lens axes):**

1. **Patient-facing explanation / contestability of AVT output** - appears as gap under P7 (Openness), T2 (Transparency), T5 (Contestability). The taxonomy assumes clinicians mediate AI output to patients; increasingly, patient-facing AI requires direct patient channels.
2. **Board-level AI governance** - appears under P10 (Org assurance), T4 (Accountability), and CQC Well-led. Captured in proposed GV.CR-12; arguably the single highest-leverage missing metric for NHS deployment.
3. **Tool-fit / proportionality assessment** - appears under P2 (ethical), P6 (Right tool), and NICE ESF Tier classification. Procurement-stage gap.
4. **Systems-based incident learning (SEIPS)** - appears under T1 (Safety), PSIRF mandatory requirements. Captured in proposed GV.SG-19.
5. **Societal Wellbeing measurement generally** - Theme 6 has the highest concentration of gaps because second-order effects on workforce, patient relationships, and healthcare sustainability are intrinsically hard to measure.

**Gap concentration by theme:** Theme 6 (Societal Wellbeing) has the most gaps, followed by Theme 5 (Contestability). Theme 1 (Safety) and Theme 4 (Accountability) have the fewest gaps - reflecting that the taxonomy was built from a safety-first, governance-aware starting point.

**Gap concentration by principle:** P6 (Right tool) and P7 (Openness) have the largest number of gaps - reflecting that the taxonomy is weaker on *decision-to-deploy* and *outward transparency* than on *in-deployment performance*. This is a structural gap that several of the proposed new metrics in the standards mapping would begin to close.

## Outcomes Boundary

This section is an explicit scope statement: what this taxonomy assures, what it does not, and where the responsibility for the rest lies. The intent is to prevent a common failure mode in clinical AI governance — passing every metric in a deployment-assurance framework and reading that as evidence of clinical benefit, when the framework was never designed to measure benefit at all.

### What this taxonomy assures

The 216 metrics measure the conditions under which an AVT system can be deployed safely and operated responsibly:

- **Technical fidelity** — does the system transcribe, diarise, summarise, and write back accurately enough for the intended clinical use? (Parts A and B)
- **Documentation quality** — do generated notes preserve clinical content, negation, uncertainty, and structure? (Part A — Summarisation / NLP)
- **Clinician oversight** — do clinicians review, edit, and sign in ways that catch system errors? (Part C — Human Factors)
- **Equitable performance** — does the system work across demographic groups, accents, disabilities, and clinical settings? (Part D — Fairness & Equity)
- **Hazard identification and incident response** — are safety events detected, investigated, and learned from? (Part E — Safety & Governance)
- **Compliance and governance** — privacy, consent, data protection, regulatory classification, vendor transparency, training, business continuity. (Part E)
- **Measurement quality** — is the evaluation methodology itself sound? (Part F — Meta-evaluation)

These are **process, structure, and proximal-outcome measures**. They tell a deployer whether the system is *operating as specified* and whether the conditions for safe use are in place.

### What this taxonomy does not assure

**Clinical outcome validation is out of scope.** This taxonomy does not contain, and is not designed to contain, metrics that establish:

- Whether AVT use changes diagnostic accuracy in real practice
- Whether AVT use changes the rate or severity of patient safety incidents
- Whether AVT use changes downstream care quality, patient outcomes, or population health
- Whether AVT use changes clinician decision-making in ways that benefit (or harm) patients
- Whether AVT delivers the cost-effectiveness claimed at procurement

These are **distal-outcome questions**. They require infrastructure that no individual deployer can provide alone: multi-site randomised trial designs, longitudinal follow-up, case-mix controls, baseline incident data of sufficient power to detect change, and independence from the vendor whose product is being evaluated.

### Why the boundary

Three reasons this is drawn explicitly rather than left implicit:

1. **The field has not solved outcome measurement for clinical AI generally, and AVT specifically.** Coiera & Fraile-Navarro (2026) name this as a structural gap. Adding outcome metrics to a deployment taxonomy does not produce outcome evidence; it produces the appearance of coverage. That risks substituting framework completeness for empirical evidence.

2. **Outcome validation belongs to bodies with the right authority and reach.** National research bodies (e.g. NIHR RSET), regulators with post-market surveillance powers (MHRA), evidence-standards frameworks (NICE ESF Tier C clinical-management evidence), and vendors pursuing formal regulatory claims are the appropriate actors. This taxonomy can require deployers to ensure those processes are in train; it cannot substitute for them.

3. **Process compliance is not clinical benefit.** A deployment passing all 43 Tier 1 metrics in this taxonomy is *assured of deployment safety* — that the system is configured, monitored, governed, and overseen correctly. It is not assured of *clinical benefit*. The taxonomy makes that distinction visible so deployers, vendors, and procurement leads do not conflate the two.

### What deployers should do instead

For the questions this taxonomy does not answer, deployers should:

- **Require post-market outcome studies** in vendor contracts. The two new meta-metrics in this v3.3 release operationalise this requirement: [ES.ME-8 Outcome Evidence Commitment Status](#es-me-8) measures whether a vendor has committed (protocol, registration, post-market surveillance plan) to outcome evaluation; [ES.ME-9 Causal Model Operationalisation](#es-me-9) measures whether the vendor has specified how the proximal metrics in this taxonomy connect to claimed distal outcomes.
- **Require T.E.S.T. Section B RCT evidence** where Gold certification (national-scale deployment) is sought. T.E.S.T. awards 50 of 420 points for clinical validation through RCTs or sufficiently powered NHS pilot studies; this taxonomy treats that evidence as input to procurement, not output of measurement.
- **Treat proximal metrics as deployment-safety signals, not as evidence of clinical benefit.** Hallucination rate is a safety-floor signal; edit rate is a workflow-and-attention signal; cumulative information yield is a fidelity signal. None of these establish that the deployed system improves care.
- **Consult [ES.ME-1 Proximal vs Distal Outcome Distinction](#es-me-1)** for the causal-logic framework that names what proximal-to-distal evidence vendors must supply, and what this taxonomy's metrics do and do not establish.

### Cross-references

- **ES.ME-1 Proximal vs Distal Outcome Distinction** — names the causal-logic burden on vendors
- **ES.ME-8 Outcome Evidence Commitment Status** — operationalises outcome-study commitment as a metric
- **ES.ME-9 Causal Model Operationalisation** — operationalises the proximal-to-distal causal chain as a metric
- **NHS T.E.S.T. Framework Section B** — Clinical Effectiveness benefit domain (90 pts of 420), with 50 pts gated on RCT evidence; see [Standards Mapping § NHS T.E.S.T.](#nhs-test-framework-technology-evaluation-safety-test)
- **MHRA Software and AI as a Medical Device** — Post-Market Surveillance (WP4 + SI 2024 No. 1368) effectiveness-evidence requirements

### Future direction

This boundary may need revisiting if (a) NHS England, NIHR, or an equivalent body publishes a national outcome-evaluation framework for AVT that this taxonomy can map to; (b) the field converges on a defensible set of distal outcome metrics with validated measurement protocols; or (c) the proximal metrics in this taxonomy are themselves shown by clinical evidence to be inadequate proxies for the outcomes that matter. Until then, the boundary stays explicit.

---

## Gaps & Proposed Metrics (Roadmap)

Consolidated register of metrics not yet in the taxonomy but flagged during mapping, coverage audit, or policy-lens analysis. Nothing here has been added to the 214-metric catalogue - each entry is a *candidate*, tracked so future rounds can draw from one place instead of re-discovering gaps.

**Entry states:**
- `proposed` - identified, not yet reviewed for inclusion
- `accepted` - approved for a future metric round (awaiting full entry drafting)
- `deferred` - considered and set aside with reasoning; may revisit
- `rejected` - considered and dismissed; reasoning preserved so it's not re-raised

**Totals across origins:** 89 candidates (9 external-review accepted, 4 external-review deferred, 4 NHSE IG, 28 standards-mapping, 6 NHS T.E.S.T., 38 Responsible AI lens).

---

## 1. External Review (RSET + NHSE IG)

Derived from two external-source coverage audits (see `archive/rset-coverage-audit.md` and `archive/nhse-ig-alignment-audit.md`).

### 1a. Accepted - RSET taxonomy (9 candidates)

Gaps identified against the Nuffield Trust RSET AVT taxonomy (Feb 2026) - a product-capability checklist that complements our measurement taxonomy.

| Gap ID | Title | Suggested Tier | Rationale | Source |
|--------|-------|----------------|-----------|--------|
| Gap-RSET-E | AI-mediated editing modality integrity | 🟡 2 | Voice/chat-based editing introduces a second hallucination surface on top of the original summarisation. Distinct failure mode not covered by summary-edit metrics (HL.HF-1/2/7). | RSET #16 |
| Gap-RSET-F | Letter / referral generation quality | 🟡 2 | Patient-facing and clinician-facing letters are a discrete output class from summaries written to the EPR. Own failure modes (audience calibration, tone, clinical accuracy). Matches scoping-review "document turnaround" evidence gap. | RSET #21–22, Phase 1 slide deck |
| Gap-RSET-G | Contextual data fusion accuracy | 🟡 2 | When AVT pulls prior EHR content into the note, fidelity of that pull is distinct from within-consultation summarisation fidelity. Untested territory. | RSET #23, #37 |
| Gap-RSET-H | Task / action-item extraction accuracy | 🟡 2 | Separate construct from consultation summary: can misattribute, fabricate, or miss tasks. Downstream workflow impact. | RSET #25 |
| Gap-RSET-I | Disability-specific speech performance | 🟡 2 | Dysarthria, aphasia, hearing-impaired speech as explicit sub-populations. Current IO.FE-* covers general demographics but not disability-specific speech. Health-equity salience. | RSET #31 |
| Gap-RSET-J | Interpreter-mediated consultation performance | 🟢 1 | Explicitly flagged by NHSE IG guidance ("enhanced verification for translated consultations") - cross-validated by both external audits. Translation introduces distortion of speaker turns, content, and consent flow. Tier 1 because the IG guidance makes it a compliance expectation. | RSET #32, NHSE IG Mar-2026 |
| Gap-RSET-K | Offline-mode integrity | 🟡 2 | Everyday safety concern when connectivity drops mid-consultation: does the product fail safely, buffer with integrity, or silently degrade? Current GV.OP-5 covers uptime but not offline-mode semantics. | RSET #38 |
| Gap-RSET-L | Validated wellbeing-instrument metric | 🔵 3 | Named validated instruments (Maslach Burnout Inventory, Copenhagen Burnout) rather than ad-hoc surveys. Scoping review confirms the field is still using non-standardised self-reports. | Phase 1 slide deck p. 14 |
| Gap-RSET-M | Consultation duration / overrun impact | 🟡 2 | Time per encounter, overrun rate - genuinely missing operational metric. Scoping review called this out as an inconsistent measure across studies. | Phase 1 slide deck p. 14 |

### 1b. Deferred - RSET taxonomy (4 candidates)

Considered and set aside. Preserved so the reasoning is durable if the same gaps are re-raised in future rounds.

| Gap ID | Title | Proposed Tier | Why deferred |
|--------|-------|---------------|--------------|
| Gap-RSET-A | Transcript / code review-ergonomics | (would have been 🟡 2) | HL.HF-3 Review-Before-Signing Rate and HL.HF-4 Time-to-Sign Distribution already capture whether review happens and how long it takes. "Ergonomics" as a distinct construct is hard to operationalise without subjective instruments; not a pure measurement gap. Revisit only if HL.HF-3/4 prove insufficient in practice. |
| Gap-RSET-B | Transcript relevance / signal-preservation | (would have been 🔵 3) | Most AVT products don't expose the raw transcript to the clinician; measurement would apply to a minority of deployments. Signal-preservation is also already bracketed by TP.SN-6 Omission Rate (summary level) and TP.SN-11 MEDIC Cross-Examination. Narrow additional value. |
| Gap-RSET-C | Transcript edit metrics (parallel to summary) | (would have been 🔵 3) | Only meaningful where the transcript is user-editable - a minority feature. HL.HF-* metrics can be applied to transcript edits by analogy if the product supports it; no new metric needed. |
| Gap-RSET-D | Configurability surface integrity | (would have been 🔵 3) | Meta-property of product configuration surfaces (whether safety-critical features can be toggled off). Unusual measurement shape - closer to a design review than a continuous metric. Out of scope for an assurance metrics taxonomy; belongs to vendor-transparency reporting. Revisit only if configuration-related incidents surface. |

### 1c. Accepted - NHSE IG alignment (4 candidates)

Derived from the NHSE IG guidance alignment audit. All are IG-driven compliance surfaces not covered by existing metrics.

| Gap ID | Title | Suggested Tier | Rationale | Source |
|--------|-------|----------------|-----------|--------|
| Gap-IG-A | Refusal impact-explanation quality | 🟡 2 | NHSE IG explicitly requires clinicians to explain *how* refusal affects care. We measure recording/respecting dissent (GV.CR-1) but not the quality of the explanation. Periodic audit. | NHSE IG Mar-2026 |
| Gap-IG-B | Privacy notice currency & completeness | 🟢 1 | Organisational privacy notices must be updated to include ambient-scribe processing specifics. Binary compliance, trivial measurement cost, named requirement in the guidance. | NHSE IG Mar-2026 |
| Gap-IG-C | SAR deletion-pause interaction | 🟡 2 | Guidance explicitly requires deletion paused during active SAR handling. GV.PD-2 Audio Time-to-Deletion doesn't test the SAR interaction - the two processes are measured separately today. | NHSE IG Mar-2026 |
| Gap-IG-D | Right-to-restrict tooling support | 🟡 2 | Restriction is distinct from erasure - data held, marked, not processed. Current GV.PD-11 covers erasure only. IG guidance explicitly requires tool functionality for restriction. | NHSE IG Mar-2026 |

---

## 2. Standards Mapping (28 candidates)

Identified during assertion-level mapping to extended standards (`_standards-mapping.md`). Proposed reference IDs reserve the next available slot in each group; if adopted, full dimensions-table entries would be drafted matching the existing metric format.

### 2a. MHRA SaMD / AIaMD (5)

| Proposed Ref | Title | Tier | What it measures |
|---|---|---|---|
| GV.CR-11 | Medical Device Classification Documentation | 🟢 1 | Whether the AVT system's SaMD classification (Class I/IIa/IIb/III) is documented with justification. Deployer must know regulatory status before go-live. |
| GV.SG-18 | PCCP Documentation Completeness | 🟡 2 | Whether Predetermined Change Control Plans cover model updates, thresholds, and rollback. Required for adaptive/retrained models. |
| GV.VT-9 | Post-Market Surveillance Report Currency | 🟡 2 | PMSR (Class I/IIa) availability on demand; PSUR (Class IIb/III) annual currency. Regulatory reporting cadence. |
| GV.VT-10 | MHRA Transparency Content Completeness | 🟡 2 | Composite check of WHAT content items (device characterisation, performance, limitations, lifecycle). |
| GV.PD-12 | Training Data Representativeness Documentation | 🟡 2 | Evidence that training data covers intended patient population (age, ethnicity, accent, comorbidity). Foundational for bias mitigation. |

### 2b. NICE Evidence Standards Framework (5)

| Proposed Ref | Title | Tier | What it measures |
|---|---|---|---|
| ES.ME-8 | NICE ESF Tier Classification Documentation | 🟢 1 | Whether the AVT deployment is classified as Tier A / B / C with justification. Required before evidence assembly. |
| ES.ME-9 | Silent Mode Evaluation Coverage | 🟡 2 | Evidence that AVT was run in silent mode on local data before go-live. |
| ES.ME-10 | Subgroup Drift Monitoring Plan | 🟡 2 | Documented plan for monitoring performance drift across demographic subgroups post-deployment. |
| GV.OP-10 | Cost-Effectiveness Analysis Availability | 🔵 3 | For Tier C AVT: CEA with QALY or cost-consequences. Research-grade for most deployments. |
| GV.OP-11 | Budget Impact Analysis Completeness | 🟡 2 | Direct and indirect costs; NHS reference costs; sensitivity analysis. Extends GV.OP-7. |

### 2c. FHIR UK Core (3)

| Proposed Ref | Title | Tier | What it measures |
|---|---|---|---|
| TP.WB-8 | Per-Resource UK Core Conformance | 🟡 2 | Stratified conformance by resource type (Composition, Condition, AllergyIntolerance, etc.). |
| TP.WB-9 | UK Core Extension Conformance | 🟡 2 | NHS Number verification status, Ethnic Category, Birth Sex, Death Notification extensions. |
| TP.WB-10 | STU Version Targeting Declaration | 🟢 1 | Vendor declaration of which UK Core STU version(s) supported. Procurement requirement. |

### 2d. CQC Assessment (4)

| Proposed Ref | Title | Tier | What it measures |
|---|---|---|---|
| GV.CR-12 | Board-Level AI Governance Mechanism | 🟢 1 | Named board committee or director with AI oversight responsibility. CQC inspection point. Also flagged under RAI Theme 4 (Accountability) and Principle 10 (Org assurance). |
| GV.CR-13 | CSO AI Oversight Capacity | 🟡 2 | Protected time / budget for CSO to oversee AI safety (not just sign-off). Operational capacity. |
| IO.PX-11 | AI-Specific Complaint Handling Rate | 🟡 2 | Rate of complaints about AI-generated records and their resolution time. Also flagged under RAI Theme 5 (Contestability). |
| GV.OP-12 | Record Quality Composite (Reg 17) | 🟡 2 | Composite of content accuracy, completeness, and timeliness against Reg 17 good-governance standard. |

### 2e. PSIRF (4)

| Proposed Ref | Title | Tier | What it measures |
|---|---|---|---|
| GV.SG-19 | Systems-Based Incident Analysis Rate | 🟡 2 | Proportion of AI-related safety incidents receiving SEIPS-informed systems analysis. Also flagged under RAI Theme 1 (Safety). |
| IO.PX-12 | Compassionate Engagement with Affected Patients | 🟡 2 | Rate at which patients/families affected by AI-related harm received early contact, named liaison, and draft report review. |
| GV.TC-6 | Staff Just Culture Protection | 🔵 3 | Staff survey on whether they feel supported vs blamed after AI-related incidents. Organisational culture. |
| GV.SG-20 | Learning Implementation Tracking | 🟡 2 | Did identified learning actually change practice? Closure rate on systemic actions. |

### 2f. PRSB (4)

| Proposed Ref | Title | Tier | What it measures |
|---|---|---|---|
| TP.WB-11 | PRSB Semantic Completeness | 🟢 1 | Proportion of PRSB-mandatory information elements present in AVT-generated output, per applicable PRSB standard (CIS, Outpatient Letter, Discharge, etc.). **Highest-leverage single addition** - appears as a gap across PRSB, FHIR UK Core, and CQC record quality. |
| TP.SN-25 | Professional Narrative Preservation | 🟡 2 | Ratio of free-text narrative vs structured extraction; flags over-structurisation and loss of clinical nuance. |
| TP.WB-12 | Communication Needs (AIS) Capture | 🟡 2 | Whether Accessible Information Standard flags (interpreter, BSL, etc.) are captured and preserved. Accessibility-critical. |
| TP.WB-13 | Legal Status Information Capture | 🟡 2 | Whether MHA status, DoLS, LPA, advance decisions are preserved when present. Clinical-legal critical. |

### 2g. Caldicott Principles (3)

| Proposed Ref | Title | Tier | What it measures |
|---|---|---|---|
| GV.PD-13 | DPIA Justification Quality | 🟡 2 | Independent review (e.g. by Caldicott Guardian) of DPIA purpose justification, not just completion. Extends GV.CR-7 completion metric. |
| GV.CR-14 | Consultation-Type Appropriateness Assessment | 🟢 1 | Documented assessment of whether AVT is appropriate for sensitive consultation types (safeguarding, MH, children, intimate exams). High-risk carve-outs. |
| GV.PD-14 | Per-Data-Item Necessity Documentation | 🔵 3 | DPIA-level documentation of why each data element processed is necessary. Granular and burdensome but thorough. |

### 2h. Standards summary

| Source Standard | Gaps | Tier Distribution |
|-----------------|------|-------------------|
| MHRA SaMD / AIaMD | 5 | 1 × Tier 1, 4 × Tier 2 |
| NICE ESF | 5 | 1 × Tier 1, 3 × Tier 2, 1 × Tier 3 |
| FHIR UK Core | 3 | 1 × Tier 1, 2 × Tier 2 |
| CQC Assessment | 4 | 1 × Tier 1, 3 × Tier 2 |
| PSIRF | 4 | 3 × Tier 2, 1 × Tier 3 |
| PRSB | 4 | 1 × Tier 1, 3 × Tier 2 |
| Caldicott | 3 | 1 × Tier 1, 1 × Tier 2, 1 × Tier 3 |
| **Total** | **28** | **6 × Tier 1, 19 × Tier 2, 3 × Tier 3** |

---

## 3. NHS T.E.S.T. Framework (6 candidates)

Derived from the NHS T.E.S.T. Framework mapping (see `_standards-mapping.md` § NHS T.E.S.T.). T.E.S.T. is AVT-specific, so alignment is already strong - these 6 gaps are genuinely novel surfaces rather than re-statements of existing standards.

| Proposed Ref | Title | Tier | T.E.S.T. Source | What it measures |
|---|---|---|---|---|
| TP.SN-26 | AI Translation Accuracy & Liability Attribution | 🟡 2 | Section A req 13 | Accuracy of AI-generated language translation in AVT output, with explicit documentation that liability for translation errors rests with the vendor, not the clinician. T.E.S.T. names translation as a distinctive clinical safety surface; no existing metric. |
| GV.PD-15 | Training Data Anonymisation Provenance | 🟡 2 | Section A req 4 | Documented provenance of anonymisation technique applied to AI training data (ICO-aligned). Extends GV.PD-7 Training Data Inclusion Status, which covers inclusion declaration but not anonymisation quality. |
| GV.OP-13 | Total Cost of Ownership / Formal Economic Evaluation | 🟡 2 | Section B domain 2 (25 pts) | Formal multi-dimensional economic evaluation including ROI, operational savings, and full TCO. Extends GV.OP-7 (per-consultation cost) and GV.OP-8 (governance burden) with a top-down economic view that T.E.S.T. weights at 25 of 420 points. Distinct from NICE-derived GV.OP-10 (CEA / QALY) and GV.OP-11 (budget impact) - this is an NHS-procurement-framed TCO view. |
| GV.VT-11 | Multi-Specialty Validation Coverage | 🔵 3 | Section B domain 3 | Count and breadth of clinical specialties in which the AVT has been formally validated (medical, surgical, allied health). T.E.S.T. awards 10 pts for multi-specialty validation; no existing metric captures breadth of validation scope. |
| IO.FE-9 | Virtual-Care Modality Stratified Performance | 🔵 3 | Section B domain 9 | Performance stratified by consultation modality (in-person, video, telephone, ambulance triage). Existing IO.FE-1 covers deployment equity by site/setting but not by modality. T.E.S.T. singles out ambulance telephone triage as a distinct high-weight case (10 pts). |
| GV.VT-12 | Sovereign AI / UK Supply Chain Disclosure | 🔵 3 | Section B domain 12 | Disclosure of whether the vendor and underlying model stack are UK-based (contributing to UK PLC per T.E.S.T. domain 12). Procurement transparency surface. Complements GV.VT-7 Sub-Processor Transparency with sovereignty-specific attribute. |

### 3a. T.E.S.T. summary

| Source | Gaps | Tier Distribution |
|--------|------|-------------------|
| NHS T.E.S.T. Section A | 2 | 2 × Tier 2 |
| NHS T.E.S.T. Section B | 4 | 1 × Tier 2, 3 × Tier 3 |
| **Total** | **6** | **3 × Tier 2, 3 × Tier 3** |

Note: 18 of 22 Section A requirements already have direct or strong metric coverage. 3 Section A items are pure process/product-feature criteria (CSO embedding, VR/dictation product offering, DCB 0160 local risk control) and are not metric-shaped. The 4th un-mapped item (req 13, translation) becomes Gap TP.SN-26 above. Section B's 12 domains all have at least partial coverage; the 4 gaps captured above are where weighting is heavy or coverage is thin.

---

## 4. Responsible AI Lens (38 candidates)

Derived from the DSIT AI Playbook principle mapping and the six ethical theme mapping in `_responsible-ai-lens.md`. Some overlap the standards-mapping gaps - cross-references noted inline.

### 4a. By Playbook principle (20)

| Principle | Gap | Severity | Cross-reference |
|-----------|-----|----------|-----------------|
| P1 - Limitations | Patient-facing disclosure of AVT limitations (not just clinician-facing) | Medium | - |
| P1 - Limitations | Running tally of encountered failure modes over deployment time | Medium | Partial via GV.SG-11 / GV.SG-14 |
| P2 - Lawful/ethical | IP status of training data (copyright, consent) | Medium | - |
| P2 - Lawful/ethical | Proportionality review (is AVT the right intervention?) | Medium | See P6; partial via ES.ME-1 |
| P3 - Security | Supply-chain security for model weights and dependencies | Medium | - |
| P3 - Security | AI-specific red-teaming cadence | Medium | - |
| P4 - Human control | Formal escalation paths when AI output is rejected | Medium | - |
| P4 - Human control | Board-level visibility of aggregate override patterns | Medium | Partial via GV.SG-13 |
| P5 - Lifecycle | Decommissioning plan | Medium | - |
| P5 - Lifecycle | Model retirement criteria | Low | - |
| P6 - Right tool | Formal comparison against non-AI alternatives at procurement | High | No existing metric |
| P6 - Right tool | Procurement-stage tool-fit assessment | High | No existing metric |
| P7 - Openness | ATRS publication completeness (where applicable) | Low | ATRS referenced but not mapped |
| P7 - Openness | Patient-facing plain-language AVT documentation | Medium | - |
| P8 - Commercial | Contractual SLA enforcement (actual enforcement, not just clauses) | Medium | - |
| P8 - Commercial | Exit-clause testing | Medium | GV.VT-6 is about provisions; gap is on testing |
| P9 - Skills | SRO / board-level AI literacy assessment | Medium | - |
| P9 - Skills | Deployer-side data science / engineering skills | Low | - |
| P10 - Org assurance | AI review board effectiveness metric | Medium | - |
| P10 - Org assurance | Enterprise risk register alignment for AI risks | Medium | Partial via GV.SG-13 |

### 4b. By ethical theme (18)

| Theme | Gap | Severity | Cross-reference |
|-------|-----|----------|-----------------|
| T1 - Safety/Security/Robustness | Systems-based root cause analysis (SEIPS) for AI incidents | High | GV.SG-19 proposed (Standards §2e) |
| T1 - Safety | Catastrophic failure mode planning | Medium | - |
| T2 - Transparency | Patient-facing explanation of AI decision-making in the record | High | TP.WB-11 proposed (Standards §2f) |
| T2 - Transparency | Model card / system card publication | Medium | Partial via GV.VT-2 |
| T2 - Transparency | Audience-proportionate explanation | Medium | - |
| T3 - Fairness | Fairness during deployment ramp | Medium | Partial via IO.FE-1 |
| T3 - Fairness | Intersectional fairness at small-group level | High | IO.FE-4/5 partial; small-group power unresolved |
| T4 - Accountability | Board-level AI governance mechanism | High | GV.CR-12 proposed (Standards §2d) |
| T4 - Accountability | Named accountable director for AI | High | Covered under GV.CR-12 |
| T4 - Accountability | Clear role distinction: CSO, DPO, SIRO, Caldicott Guardian in AI context | Medium | - |
| T5 - Contestability | Patient route to challenge AI-generated note content (beyond SAR) | High | Related to IO.PX-11 (Standards §2d) |
| T5 - Contestability | Affected-third-party contestability | Medium | - |
| T5 - Contestability | Redress mechanism for population-level AVT harm | Medium | - |
| T6 - Societal Wellbeing | Workforce displacement / role change assessment | High | HL.HF-12 partial |
| T6 - Societal Wellbeing | Equity of benefit distribution across practices | High | IO.FE-1 partial |
| T6 - Societal Wellbeing | Patient trust at population level | High | IO.PX-5, IO.PX-6 partial |
| T6 - Societal Wellbeing | Long-term sustainability of AVT adoption | Medium | - |
| T6 - Societal Wellbeing | Job security / workforce anxiety assessment | Medium | Flagged low severity in Standards Mapping |

### 4c. Highest-severity cross-cutting gaps

Gaps that surface under multiple lens axes - highest-leverage targets for future metric rounds.

1. **Patient-facing explanation / contestability of AVT output** - P7, T2, T5. The taxonomy assumes clinicians mediate AI output to patients; patient-facing AI requires direct channels.
2. **Board-level AI governance** - P10, T4, CQC Well-led. Captured in proposed GV.CR-12. Arguably the single highest-leverage missing metric for NHS deployment.
3. **Tool-fit / proportionality assessment** - P2, P6, NICE ESF Tier classification. Procurement-stage gap.
4. **Systems-based incident learning (SEIPS)** - T1, PSIRF mandatory requirements. Captured in proposed GV.SG-19.
5. **Societal Wellbeing measurement generally** - Theme 6 has the highest concentration of gaps because second-order effects on workforce, patient relationships, and healthcare sustainability are intrinsically hard to measure.

---

## 5. Roll-up

**Totals across origins:**

| Origin | Accepted / Proposed | Deferred | Rejected | Total |
|--------|---------------------|----------|----------|-------|
| RSET external review | 9 | 4 | 0 | 13 |
| NHSE IG external review | 4 | 0 | 0 | 4 |
| Standards mapping | 28 | 0 | 0 | 28 |
| NHS T.E.S.T. | 6 | 0 | 0 | 6 |
| Responsible AI lens | 38 | 0 | 0 | 38 |
| **Total** | **85** | **4** | **0** | **89** |

**Tier distribution of the 85 accepted/proposed candidates:**

| Tier | Count |
|------|-------|
| 🟢 1 | 10 (Gap-RSET-J, Gap-IG-B, 6 from Standards, 2 from RAI high-severity) |
| 🟡 2 | 50 (+3 from T.E.S.T.) |
| 🔵 3 | 9 (+3 from T.E.S.T.) |
| Unassigned (RAI severity only) | 16 |

**If all 85 accepted candidates were adopted as metrics,** the taxonomy would grow from 214 to ~299 metrics. In practice, cross-cutting gaps (e.g. Board-Level AI Governance surfaces under CQC, P10, and T4) will collapse to single metrics, so the true additive count is likely ~65–70.

**Highest-leverage single additions** (gap appears in multiple origins simultaneously):
- **TP.WB-11 PRSB Semantic Completeness** - Standards §2f (PRSB), implicit in CQC record quality, implicit in FHIR UK Core conformance, T2 Transparency
- **GV.CR-12 Board-Level AI Governance Mechanism** - Standards §2d (CQC), P10, T4
- **GV.SG-19 Systems-Based Incident Analysis Rate** - Standards §2e (PSIRF), T1
- **GV.CR-14 Consultation-Type Appropriateness Assessment** - Standards §2g (Caldicott), direct NHSE IG concern for sensitive consultation carve-outs

## 6. How this file is maintained

- New gaps identified in any source document are added here with `status: proposed`.
- Gaps promoted to metrics: status changes to `accepted`, then the entry is *removed* when the metric is drafted and numbered. The CHANGELOG records the promotion.
- Deferred gaps stay in §1b-style "Deferred" subsections with explicit reasoning so the rejection is durable.
- Cross-cutting gaps (single concept across multiple origins) are listed once in their primary origin with cross-references, not duplicated.
- This file is the **single source of truth for roadmap content**. The prose gap sections in `_standards-mapping.md` and `_responsible-ai-lens.md` are summaries that point here.

# Glossary

Quick reference for terms, abbreviations, and standards referenced throughout the taxonomy. Each entry gives a one-line gloss and - where applicable - a link to the authoritative source and the metric(s) or standards that reference it.

## Pipeline and technical terms

- **AVT** - Ambient Voice Technology. Generic term for AI systems that listen to a consultation and produce clinical documentation, typically comprising audio capture → ASR → diarisation → summarisation → EPR write-back.
- **ASR** - Automatic Speech Recognition. The pipeline stage that converts speech audio to text (transcript).
- **Diarisation** - Speaker attribution. Determining who spoke which segment of the transcript (clinician, patient, bystander).
- **EPR** - Electronic Patient Record. Used synonymously with EHR (Electronic Health Record) in this taxonomy.
- **LLM** - Large Language Model. Statistical model used for summarisation and coding in most current AVT products.
- **SaMD** - Software as a Medical Device. MHRA regulatory classification.
- **AIaMD** - AI as a Medical Device. Subclass of SaMD covering adaptive and learning systems.
- **SNR** - Signal-to-Noise Ratio. See `TP.AC-1`.
- **VAD** - Voice Activity Detection. See `TP.AC-2`.
- **WER** - Word Error Rate. ASR accuracy metric. See `TP.ASR-1`.
- **M-WER** - Medical WER. Clinical-vocabulary-weighted WER. See `TP.ASR-2`.
- **CK-ER** - Clinical Keyword Error Rate. See `TP.ASR-3`.
- **CER** - Character Error Rate. See `TP.ASR-8`.
- **OOV** - Out-of-Vocabulary. See `TP.ASR-9`.
- **RTF** - Real-Time Factor. Processing speed metric. See `TP.ASR-7`.
- **DER** - Diarisation Error Rate. See `TP.DI-1`.
- **HEWER** - Holistic Error-Weighted Error Rate. Diarisation-aware variant. See `TP.DI-8`.
- **cpHEWER** - Clinical-Perspective HEWER.
- **ROUGE** - Recall-Oriented Understudy for Gisting Evaluation. Summarisation text-similarity metric. See `TP.SN-1`.
- **BERTScore** - Neural-embedding-based text similarity metric. See `TP.SN-2`.
- **PDSQI-9** - Physician Documentation Quality Instrument, 9 items. See `TP.SN-3`.
- **CREOLA** - Clinical Record Error Ontology and Labelling Architecture. See `TP.SN-4`.

## Standards and regulatory

- **DTAC** - Digital Technology Assessment Criteria (NHS England). The pre-procurement digital assurance framework.
- **DSPT** - Data Security and Protection Toolkit (NHS Digital). Annual data-security self-assessment.
- **DCB0129** - Clinical Risk Management: Manufacturer. Mandatory for health IT system manufacturers.
- **DCB0160** - Clinical Risk Management: Healthcare Organisation. Deployer-side counterpart to DCB0129.
- **NHS LLM Eval Framework** - NHS England's Large Language Model Evaluation and Monitoring Framework.
- **MHRA** - Medicines and Healthcare products Regulatory Agency.
- **NICE ESF** - National Institute for Health and Care Excellence, Evidence Standards Framework for Digital Health Technologies (ECD7).
- **FHIR UK Core** - HL7 Fast Healthcare Interoperability Resources, UK Core profile (INTEROPen / NHS Digital).
- **CQC** - Care Quality Commission. The primary healthcare regulator in England.
- **PSIRF** - Patient Safety Incident Response Framework (NHS England, 2022→).
- **PRSB** - Professional Record Standards Body.
- **Caldicott Principles** - Eight principles governing the use of confidential patient information (NDG, 2020 revision).
- **UK GDPR** - UK General Data Protection Regulation.
- **DPIA** - Data Protection Impact Assessment.
- **DSPA** - Data Sharing and Processing Agreement.
- **DCB** - Data Coordination Board (NHS Digital).
- **NDG** - National Data Guardian.
- **ICO** - Information Commissioner's Office.
- **SAR** - Subject Access Request (UK GDPR Article 15).

## Policy and governance

- **DSIT AI Playbook** - Department for Science, Innovation and Technology, *AI Playbook for the UK Government* (Feb 2025). Source of the 10 Playbook principles mapped in the Responsible AI lens.
- **ICB** - Integrated Care Board.
- **LFPSE** - Learn from Patient Safety Events (NHS England national reporting system).
- **NAS** - National Assurance Service (NHS England Chief Safety Officer; publishes AVT Day Zero SPIs).
- **SPI** - Safety Performance Indicator.
- **DSCMS** - Digital Safety Clinical Monitoring Scheme (NHS England).
- **CSO** - Clinical Safety Officer (DCB0129/0160 role).
- **SIRO** - Senior Information Risk Officer.
- **CIO / CCIO** - Chief Information Officer / Chief Clinical Information Officer.
- **DPO** - Data Protection Officer.
- **AIS** - Accessible Information Standard (NHS).
- **ATRS** - Algorithmic Transparency Recording Standard (UK government).

## Taxonomy-specific

- **Metric family** - A named parent-construct grouping of related metrics (e.g. *Clinical Content Fidelity*) that may span multiple groups. The full list: Reference-Based Text Similarity, Clinical Content Fidelity, Clinical Transcription Accuracy, Post-Generation Correction, Medication Safety Thread, Demographic Equity Disaggregation.
- **Sub-cluster** - A thematic grouping of metrics within a single group. Sub-clusters have italic introductory text before the first member.
- **Reference ID** - Format `{Part}.{Group}-{Number}` (e.g. `TP.AC-1`). Stable across versions; cite as `TP.AC-1` → `/groups/audio-capture/#tp-ac-1`.
- **Tier 1 / 2 / 3** - Priority classification: Tier 1 is minimum viable assurance (measurable today, every deployer must do it); Tier 2 is recommended; Tier 3 is advanced/research-grade.
- **Cadence** - One of *Gate* (pre-deployment), *Continuous*, or *Audit* (periodic).
- **Responsible Actor** - Who is accountable for measuring: *Vendor*, *Deployer*, *Regional body* (ICB), *National body* (NHS England), or *Academic*.
- **Applicability** - Three-way classification per metric: *AVT-Specific*, *AVT-Contextualised*, or *General Healthcare AI*.
- **Underspecification warning** - Explicit flag on a metric where the measurement science does not yet have consensus. Readers should treat these as calls for caution.

*This glossary is a convenience only; the authoritative source for any term is the standards document or the metric entry itself.*

### TP.AC-1 🟡 Signal-to-Noise Ratio (SNR) Monitoring

Continuous measurement of audio input quality. SNR below threshold degrades ASR accuracy unpredictably - the system may continue producing confident-looking but degraded output without alerting the clinician.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.AC-1 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
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

> Simple energy-based SNR is a crude proxy - overlapping speech, reverberation, and non-stationary noise complicate measurement. Clinical environments have complex acoustic profiles.

**Novel Thinking / Implications**

> 💡 The system should degrade gracefully: if SNR drops below threshold mid-consultation, the AVT should flag the note as potentially degraded rather than producing output with false confidence. This is an architectural requirement - the AVT should know when its own input quality is insufficient.

---

### TP.AC-2 🔵 Voice Activity Detection (VAD) Accuracy

Accuracy of detecting when speech is occurring vs silence/noise. VAD errors cause missed speech (content lost) or false activations (noise processed as speech, potentially generating hallucinated content from non-speech audio).

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.AC-2 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
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

> 💡 False activations are the underappreciated risk: if the VAD activates on background TV, corridor conversation, or equipment alarms, the ASR processes non-clinical audio. The summariser then has to decide what to do with transcribed noise - which may look like clinical content and get included in the note.

---

### TP.AC-3 🟡 Acoustic Environment Profiling

Characterisation of the deployment acoustic environment against the vendor's validated acoustic conditions. Gap between validated and actual environment = unquantified risk.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.AC-3 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Proposed - extends validated use envelope concept to acoustic conditions |

**Why this tier?**

> Deployer should characterise their acoustic environment at setup to confirm it falls within the vendor's validated conditions.

**Formal Definition**

```
Profile vector: [SNR_typical, reverberation_time_RT60, background_noise_type, speaker_distance_range, microphone_type]. Validated envelope V = vendor's tested conditions. Environment gap G = distance(actual_profile, V). G > threshold → environment outside validated envelope.
```

**Limitations**

> Acoustic conditions vary within a single practice (different rooms, open/closed doors, time of day). Point-in-time profiling may not capture the full range.

**Novel Thinking / Implications**

> 💡 This is the acoustic equivalent of the compound boundary risk model. A system validated with a lapel mic at 30cm in a quiet room may be deployed with a desk mic at 1.5m in a busy practice with a door open to the waiting room. Each acoustic parameter crossing the validated boundary compounds risk - and unlike clinical domain boundaries, acoustic boundaries are invisible to governance processes.

---

### TP.AC-4 🔵 Bystander Voice Detection Rate

Ability to detect and flag speech from individuals who have not consented to AVT processing: patients in adjacent rooms, reception staff audible through walls, family members who arrive mid-consultation without being informed.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.AC-4 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Patient Experience |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Identified in NHSE IG guidance on ambient scribing privacy implications; CQC Mythbuster 109 context |

**Why this tier?**

> Technology for reliable bystander detection does not yet exist. Important research direction but not actionable today.

**Formal Definition**

```
Detection rate = |bystander_speech_detected| / |total_bystander_speech|. False positive rate = |participant_speech_flagged_as_bystander| / |total_participant_speech|. Requires speaker enrolment or real-time speaker count monitoring.
```

**Limitations**

> Technically challenging - requires distinguishing expected speakers from unexpected ones without prior voice enrolment. Current diarisation can count speakers but cannot determine consent status.

**Novel Thinking / Implications**

> 💡 This sits at the intersection of audio capture, privacy, and consent. UK GDPR requires lawful basis for processing personal data - bystander speech captured and processed by AVT has no consent basis. The NHSE IG guidance (March 2026) flags this but provides no technical solution. A detection-and-redaction pipeline for non-consented speech would be architecturally significant.

---

### TP.AC-5 🟢 Microphone & Hardware Validation

Verification that the capture hardware meets minimum specifications for the AVT system. Includes microphone frequency response, placement distance, device compatibility, and Bluetooth/connectivity reliability.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.AC-5 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
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

### TP.AC-6 🔵 Speaker Overlap Rate

Proportion of audio time with simultaneous speech from multiple speakers. Common in real consultations (interruptions, agreement utterances, talking over) and most ASR/diarisation systems handle overlap poorly - often dropping content from one speaker entirely.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.AC-6 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
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

> 💡 Real consultations have 5-15% overlap rates depending on style. A vendor benchmarking on scripted dyadic dialogue may report excellent performance that doesn't translate to spontaneous clinical interaction. Overlap rate should be a procurement question - what conditions was the system validated under?

---

### TP.AC-7 🟡 Audio Clipping / Saturation Rate

Frequency of audio level exceeding the dynamic range of the capture system, causing waveform distortion. Different from SNR - clipping is a hardware/gain issue that destroys content even in quiet environments. Commonly caused by mic too close, gain set too high, or sudden loud sounds.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.AC-7 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
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

### TP.AC-8 🟡 Codec & Sampling Rate Compliance

Whether audio meets minimum bit depth and sample rate specifications for the AVT system. Telephone audio at 8kHz degrades ASR significantly compared to 16kHz studio quality. Compressed codecs (e.g. heavily lossy Bluetooth audio) introduce artifacts.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.AC-8 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Standard audio engineering; vendor minimum specifications |

**Why this tier?**

> Automated check per encounter. Should be enforced architecturally - non-compliant audio should be flagged before processing.

**Formal Definition**

```
Compliance check per encounter: (1) sample_rate >= vendor_minimum (typically 16kHz); (2) bit_depth >= vendor_minimum (typically 16-bit); (3) codec in approved_codecs. Binary pass/fail per criterion. Non-compliant audio should trigger pre-processing warning or rejection.
```

**Limitations**

> Telephone consultations are increasingly common in NHS practice but most AVT systems are validated on 16kHz+ audio. The mismatch is often invisible until accuracy degrades.

**Novel Thinking / Implications**

> 💡 Telephone consultations are a hidden boundary risk. A practice using AVT for in-person consultations and then extending to telephone is operating outside the validated codec envelope. The system may produce confident-looking output of much lower accuracy.

---

### TP.AC-9 🔵 Microphone Drift Detection

Detection of gradual hardware degradation over time: declining battery performance, mechanical wear, positioning shift, accumulated debris, Bluetooth interference patterns. Different from initial validation - this catches problems that develop after deployment.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.AC-9 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Proposed - extends hardware validation to ongoing monitoring |

**Why this tier?**

> Conceptually valuable but requires telemetry infrastructure most vendors don't provide. Better suited for vendor-side implementation.

**Formal Definition**

```
Track baseline audio quality metrics (SNR, frequency response, noise floor) over time. Drift = significant deviation from baseline established at hardware validation. Alert if SNR drops >5dB from baseline or frequency response shifts >10%.
```

**Limitations**

> Requires establishing per-device baselines and tracking longitudinally. Most AVT systems treat hardware as a black box.

**Novel Thinking / Implications**

> 💡 Hardware degrades silently. A wireless lapel mic that worked perfectly at deployment may have degraded battery contacts six months later, producing intermittent dropout that the clinician doesn't notice but that affects ASR accuracy. Drift detection is proactive maintenance - catching the problem before it causes a clinical incident.

---

### TP.ASR-1 🟡 Word Error Rate (WER)

Standard ASR accuracy metric. Treats all word errors equally - a misheard 'the' counts the same as a misheard drug name.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-1 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
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

- **NIST scoring toolkit**: [SCTK - NIST Speech Recognition Scoring Toolkit](https://github.com/usnistgov/SCTK)
- **Original**: Woodard & Nelson (1982), NBS Report

**Limitations**

> Clinically uninformative - does not weight by clinical significance. A 5% WER could be safe or dangerous depending on which words are wrong.

*See also: Medical WER (M-WER), Clinical Keyword Error Rate (CK-ER) - all members of the Clinical Transcription Accuracy family. Raw WER is level 1 of the family; the other two add clinical weighting but require a standardised significance ontology that does not yet exist.*

---

### TP.ASR-2 🔵 Medical Word Error Rate (M-WER)

Weighted WER where errors on clinically significant tokens carry higher penalty. Requires a clinical significance ontology to define token weights.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-2 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, National Body |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
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

**⚠️ Underspecification Warning (Tier B - no standardised weighting ontology)**

> M-WER requires a weighting ontology defining the clinical significance of token classes. **No such ontology is standardised for NHS or international use.** Abridge's Medical Term Recall (MTR) and DeepScribe's Medical Word Hit Rate are functionally equivalent implementations that use different proprietary term lists and different weighting schemes - so a vendor claiming "95% MTR" cannot be directly compared with another claiming "95% M-WER". A national body standard mapping SNOMED safety-critical concept classes to weight values would make vendor benchmarks comparable and is a candidate for NHS England or equivalent commissioning. Until then, require vendors to disclose (a) their term list and provenance, (b) the weighting scheme, and (c) the reference dataset used for M-WER computation. Refuse to compare M-WER values across vendors without this disclosure.

**Novel Thinking / Implications**

> 💡 A national body could define a standardised M-WER weighting ontology mapped to SNOMED safety-critical concept classes, making vendor benchmarks comparable.

*See also: Word Error Rate (WER), Clinical Keyword Error Rate (CK-ER) - all members of the Clinical Transcription Accuracy family. Abridge's Medical Term Recall (MTR) and DeepScribe's Medical Word Hit Rate are functionally equivalent implementations of this metric reported under different names; a vendor reporting any of these is reporting the same construct with different term lists.*

---

### TP.ASR-3 🔵 Clinical Keyword Error Rate (CK-ER)

Focused accuracy for high-stakes clinical terminology. Binary: was the keyword captured correctly or not?

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-3 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
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

**⚠️ Underspecification Warning (Tier B - same standardisation gap as M-WER)**

> CK-ER depends on a clinical significance ontology defining which terms are keywords - no standardised ontology exists. The vendor or deployer implementing CK-ER chooses which terms count, and the resulting metric is only as good as that choice. Different keyword lists produce materially different CK-ER values for the same system, which prevents cross-vendor comparison and makes local benchmarks difficult to interpret. This metric sits in the same standardisation gap as M-WER: it is conceptually sound but requires national body specification of a canonical keyword ontology mapped to SNOMED safety-critical concept classes before it can be reported in a comparable way. In the interim, document the keyword dictionary used and its provenance when reporting CK-ER.

**Novel Thinking / Implications**

> 💡 Could run as automated post-transcription guardrail on every encounter without human review.

*See also: Word Error Rate (WER), Medical WER (M-WER) - all members of the Clinical Transcription Accuracy family. CK-ER is the most actionable variant - binary per keyword, suited to running as an automated guardrail - but is most sensitive to the choice of keyword dictionary.*

---

### Family: Demographic Equity Disaggregation

> **Parent construct** - the family of metrics that apply demographic disaggregation to pipeline performance, measuring whether system quality varies across population subgroups. The underlying principle is the same at every layer: compute the base metric separately for each demographic group, then quantify the gap.
>
> This family spans the full pipeline because equity failures can originate at any stage. ASR accuracy may vary by accent; summarisation quality may vary by consultation style correlated with ethnicity; coding completeness may systematically differ across patient populations. Measuring equity at only one layer provides false assurance - a system that transcribes equitably may still summarise or code inequitably.
>
> **The disaggregation axes.** Most metrics in this family operate on the same set of demographic variables: accent/dialect, first language, age band, sex, ethnicity, deprivation quintile, and speech characteristics (rate, volume, disorder). The specific axes depend on the base metric and available data. The NAS framework proposes a maximum 5 percentage-point gap across groups as a starting threshold.
>
> **Metrics in this family:**
> - 🟡 **Demographic-Disaggregated WER** (ASR / Transcription) - WER by accent, language, age, speech characteristics
> - 🔵 **Speaker-Stratified WER** (ASR / Transcription) - WER by speaker role (clinician vs patient)
> - 🟡 **Coding Equity Index** (Clinical Coding) - whether AVT-driven coding changes are equitable across demographics
> - 🔵 **Compound Demographic Performance** (End-to-End Pipeline) - intersectional performance at full-pipeline level
> - 🟡 **Accent Taxonomy Standardisation** (Fairness & Equity) - standardised accent/dialect categorisation for disaggregation
> - 🔵 **Intersectional Performance** (Fairness & Equity) - performance at demographic intersections
> - 🔵 **Intersectional Compound Fairness Score** (Fairness & Equity) - formal intersectional fairness quantification

### TP.ASR-4 🟡 Demographic-Disaggregated WER

WER by accent group, first language, age band, and speech characteristics. NAS proposes max 5pp gap across groups.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-4 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, National Body |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
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

- **ASR bias**: [Koenecke et al. (2020) - Racial disparities in automated speech recognition, PNAS](https://doi.org/10.1073/pnas.1915768117)
- **NAS framework**: NAS Day Zero SPIs; NHSE IG guidance (March 2026)

**Limitations**

> Vendors control test datasets. No independent UK-representative speech corpus exists at scale.

**⚠️ Underspecification Warning (Tier C - well-defined structure, ad hoc categorisation)**

> Published demographic WER reporting uses ad-hoc accent categorisation that has been systematically critiqued. A FAccT 2024 paper identified race-based, geography-based, and native/non-native categories as poor proxies for the actual acoustic variation that affects ASR performance - they are demographically convenient but phonologically arbitrary. No standardised maximum acceptable disparity threshold exists across the field; the NAS 5 percentage point target is a proposed rather than evidence-based threshold. For NHS context, a defensible taxonomy must include at minimum: British regional accents (with meaningful sub-categorisation), South Asian English varieties (distinct from "Indian English" as a single category), West African English, Caribbean English, and Eastern European English - none of which are consistently present in vendor-reported demographic WER data. The accompanying **Accent Taxonomy Standardisation** metric (Fairness & Equity) assesses whether the categorisation itself is defensible before the disaggregation numbers become meaningful.

**Novel Thinking / Implications**

> 💡 A national independent speech corpus reflecting NHS patient demographics would make vendor-reported demographic WER meaningful rather than self-assessed.

---

### TP.ASR-5 🔵 Speaker-Stratified WER

Separate WER for clinician vs patient speech. Patient speech is more diagnostically important and typically harder to transcribe.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-5 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
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

### TP.ASR-6 🟡 Error Transmission Rate

Proportion of ASR transcription errors that survive into the final clinical note. Distinct from end-to-end accuracy because it isolates the ASR→NLP propagation step - a system with high raw WER but strong contextual inference in the summariser can have a low transmission rate, while a system with low WER and literal summarisation can still transmit every error it makes.

|Dimension              |Value                                                                  |
|-----------------------|-----------------------------------------------------------------------|
| **Reference** | TP.ASR-6 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                                 |
|**Measurement Cadence**|Periodic audit                                                         |
|**Pipeline Layer**     |ASR + Summarisation                                                    |
|**Assurance Question** |Fidelity & Accuracy                                                    |
|**Measurement Method** |Computational                                                          |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                         |
|**Responsible Actors** |Vendor                                                                 |
|**Maturity**           |Emerging                                                               |
|**Outcome Type**       |Proximal                                                               |
|**Applicability**      |AVT-Specific                                                           |
|**Source**             |Anderson et al., Mayo Clinic Proceedings Digital Health, 2025 (OHSU 5-platform study found 19.5% transmission rate)|

**Why this tier?**

> Vendor metric requiring intermediate output access. Measurable when raw transcript and final note are both available for comparison. Valuable diagnostic because it distinguishes ASR-bottleneck systems from summarisation-bottleneck systems - the intervention is completely different in each case.

**Formal Definition**

```
ETR = |ASR_errors_present_in_final_note| / |ASR_errors_in_raw_transcript|. ETR = 0 means the summariser corrects every ASR error (unlikely). ETR = 1 means the summariser transmits every error unchanged. ETR > 1 is possible if summariser amplification adds errors beyond the ASR baseline. Compute per error category (numeric, drug name, negation, demographic) - the overall rate obscures category-specific failure modes.
```

**Limitations**

> Requires access to raw transcript and final note with alignment between the two. Not all vendors expose the intermediate transcript. Error categorisation requires NER infrastructure.

**Novel Thinking / Implications**

> 💡 The OHSU finding that 19.5% of ASR errors reach the final note suggests the summariser provides meaningful but imperfect error correction. The more interesting question is *which* errors transmit: if safety-critical errors transmit at higher rates than stylistic errors, the summariser is learning the wrong patterns. Transmission rate disaggregated by error category is more useful than the aggregate.

### TP.ASR-7 🟡 Real-Time Factor (RTF)

Processing speed relative to audio duration. RTF < 1.0 = faster than real-time.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-7 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
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

### TP.ASR-8 🟡 Character Error Rate (CER)

Character-level edit distance between reference and hypothesis. More sensitive than WER for medical terminology where subword errors are common: 'amoxicillin' vs 'amoxycillin' has WER=1 but CER=1/12. Particularly important for drug names, anatomical terms, and proper nouns.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-8 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
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

> CER and WER measure different things - neither is universally better. CER can underweight serious errors (a wrong drug name with similar spelling has low CER but high clinical risk).

**Novel Thinking / Implications**

> 💡 CER and WER should be reported together. A system with low WER but high CER is making many minor errors; a system with high WER but low CER is making fewer but more substantial errors. The clinical implications differ.

---

### TP.ASR-9 🟡 Out-of-Vocabulary (OOV) Rate

Proportion of tokens the ASR model doesn't recognise as valid vocabulary. New drug names, novel diagnoses, proper nouns, and recently approved medications are systematically OOV in older models. High OOV rate predicts systematic clinical accuracy gaps.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-9 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Standard speech recognition literature |

**Why this tier?**

> Should be re-tested when dm+d updates and when model versions change. Vendors should commit to maintenance schedule for vocabulary currency.

**Formal Definition**

```
OOV Rate = |tokens_not_in_vocab| / |total_tokens|. Compute against the ASR's lexicon. For end-to-end neural ASR, OOV manifests as decomposition into subword units which may produce nonsense. Track per encounter and per clinical category (drugs, diagnoses, procedures).
```

**Limitations**

> End-to-end neural ASR systems don't have explicit vocabularies - OOV is harder to define. Subword tokenisation means any word can be 'represented' but may not be transcribed correctly.

**Novel Thinking / Implications**

> 💡 Newly approved drugs (every quarter, MHRA approves new medicines) are by definition OOV until the model is updated. A model trained two years ago will systematically fail on the latest oncology agents, biologics, and recently licensed treatments. OOV rate against the current dm+d should be a procurement question.

---

### TP.ASR-10 🟡 ASR Confidence Calibration

Whether the ASR's stated confidence scores correlate with actual accuracy. A poorly-calibrated ASR that reports 95% confidence on 70%-accurate output is dangerous because downstream consumers (summariser, clinician) trust the output inappropriately.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-10 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Machine learning calibration literature |

**Why this tier?**

> Vendor should test and report. Confidence calibration is a prerequisite for confidence-based filtering and human review routing.

**Formal Definition**

```
For each confidence bin b in [0.5, 0.6, ..., 1.0], compute actual_accuracy(b) = correct_predictions(b) / total_predictions(b). Calibration Error = sum |b - actual_accuracy(b)| weighted by bin frequency. Perfect calibration: ECE = 0. Reliable systems: ECE < 0.05.
```

**References**

- **Calibration**: [Guo et al. (2017) - On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599)

**Limitations**

> Modern neural ASR systems are typically miscalibrated (overconfident). Calibration can be improved post-hoc but most vendors don't expose confidence scores at all.

**Novel Thinking / Implications**

> 💡 If confidence scores are exposed and well-calibrated, downstream systems can route low-confidence segments for human review. If they're miscalibrated or absent, the AVT cannot signal its own uncertainty - which means the clinician must assume everything is equally reliable.

---

### TP.ASR-11 🟡 ASR Confidence Exposure

Whether the ASR system exposes per-token or per-segment confidence scores to downstream consumers - both the summariser and the clinician reviewing. Different from the existing ASR Confidence Calibration metric, which asks whether confidence scores are *accurate*. Exposure asks whether they are *available at all*. Well-calibrated confidence locked inside the vendor's infrastructure provides no downstream benefit.

|Dimension              |Value                                                           |
|-----------------------|----------------------------------------------------------------|
| **Reference** | TP.ASR-11 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                          |
|**Measurement Cadence**|One-off gate                                                    |
|**Pipeline Layer**     |ASR / Transcription                                             |
|**Assurance Question** |Safety                                                          |
|**Measurement Method** |Human Review                                                    |
|**Lifecycle Phases**   |Pre-deployment                                                  |
|**Responsible Actors** |Vendor                                                          |
|**Maturity**           |Proposed / Novel                                                |
|**Outcome Type**       |Proximal                                                        |
|**Applicability**      |AVT-Specific                                                    |
|**Source**             |Derived from Abridge Linked Evidence architecture; confidence-based routing literature|

**Why this tier?**

> Pre-deployment architectural question. Should be a procurement requirement for any AVT system where confidence-based review routing or uncertainty display is intended. Without exposure, the rest of the confidence-based safety architecture cannot be built.

**Formal Definition**

```
Exposure assessed on three levels: (1) Internal - confidence scores exist but are not exposed; (2) Downstream - confidence scores passed to summariser for internal use; (3) Clinician-visible - low-confidence segments highlighted in the review interface. Target: Level 3 for any safety-critical deployment. Binary per level; report highest level achieved.
```

**Limitations**

> End-to-end neural ASR systems may produce confidence scores that are poorly calibrated (see existing ASR Confidence Calibration metric). Exposure without calibration can be actively misleading - a clinician seeing "95% confidence" on a 70%-accurate segment has worse situational awareness than a clinician seeing no score at all.

**Novel Thinking / Implications**

> 💡 Confidence display is the architectural prerequisite for intelligent review. A reviewer who can see which words or segments the system is uncertain about can focus their attention there. A reviewer looking at a flat wall of text must review everything equally - which in practice means reviewing nothing carefully. Clinician-visible confidence should be a standard AVT interface element, not an advanced feature.

### TP.ASR-12 🟢 Hallucination-Under-Noise Rate

Rate at which the ASR generates plausible-sounding but fabricated text when fed noise, silence, or non-speech audio. Whisper is famously prone to this - it can produce coherent-looking transcriptions of pure silence. A distinct failure mode from substitution errors that creates content from nothing.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-12 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Koenecke et al. 2024 'Careless Whisper'; specific to neural end-to-end ASR architectures |

**Why this tier?**

> Critical pre-deployment test. Whisper-based systems are documented to hallucinate from silence - this must be tested before clinical use. Tier 1 because the failure mode is well-documented and the test is straightforward.

**Formal Definition**

```
Test corpus: known non-speech audio (silence, music, environmental noise, foreign language). Hallucination Rate = |outputs_containing_text| / |test_samples|. Severity weighted: spurious clinical content (drug names, symptoms) is more dangerous than spurious filler.
```

**References**

- **Whisper hallucinations**: [Koenecke et al. (2024) - Careless Whisper: Speech-to-Text Hallucination Harms](https://arxiv.org/abs/2402.08021)

**Limitations**

> Different from general hallucination rate at the summarisation layer. Specifically tests ASR architectural failure on silence/noise inputs.

**Novel Thinking / Implications**

> 💡 This is a specific architectural failure mode of neural ASR systems trained on aligned speech-text pairs. When fed audio that doesn't contain speech, they don't output silence - they output their best guess at what speech might have been there. The clinical implication: pauses in consultations, brief silences, or background noise can produce fabricated clinical content. Should be a hard pre-deployment test.

---

### TP.ASR-13 🟢 Numeric Accuracy

Accuracy specifically on numbers: dosages, dates, vital signs, lab values, durations. Numbers fail differently from words and have outsized clinical importance. '15mg' vs '50mg' is a tenfold dosing error invisible to standard WER weighting.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-13 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
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

> 💡 The dosage error case is the canonical clinical AI safety nightmare. A standard WER calculation treats '15mg' and '50mg' as equally wrong as 'the' becoming 'a' - they're not. Numeric accuracy should be reported separately and a single dosage error should trigger immediate review of the entire encounter.

---

### TP.ASR-14 🔵 Punctuation & Capitalisation Accuracy

Accuracy of sentence boundary detection, punctuation, and capitalisation. Affects readability and downstream NLP. Misplaced sentence boundaries can completely change clinical meaning: 'no chest pain. Shortness of breath' vs 'no chest pain, shortness of breath' have different clinical implications.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-14 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Standard ASR post-processing literature |

**Why this tier?**

> Vendor responsibility. Important for downstream NLP quality but harder to attribute clinical impact directly.

**Formal Definition**

```
Sentence boundary F1 = harmonic mean of precision and recall on sentence boundaries. Punctuation accuracy = |correct_punctuation_marks| / |total_punctuation_in_reference|. Capitalisation accuracy = |correct_case_decisions| / |total_words|.
```

**Limitations**

> Punctuation in clinical speech is often ambiguous - clinicians don't speak in clearly punctuated sentences. Reference annotations are themselves variable.

**Novel Thinking / Implications**

> 💡 Sentence boundary errors propagate into summarisation as compounded meaning changes. A misplaced full stop can split a single clinical concept across two summarised statements, or merge two distinct concepts into one.

---

### TP.DI-1 🟡 Diarisation Error Rate (DER)

Proportion of audio time with incorrect speaker labels. Combines missed speech, false alarm, and speaker confusion.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.DI-1 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Diarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
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

- **Scoring tool**: [dscore - Python NIST md-eval](https://github.com/nryant/dscore)
- **SCRIBE**: [Wang et al. (2025) - npj Digital Medicine](https://doi.org/10.1038/s41746-025-01449-w)

**Limitations**

> Challenging in multi-party consultations. Most benchmarks assume two speakers.

**⚠️ Underspecification Warning (Tier C - standard methodology, absent clinical context)**

> DER has a rigorous technical definition (NIST RT evaluation protocol) and established general benchmarks (AMI ~7.2%, CALLHOME ~12.4%), but **no clinical-specific benchmarks exist** for the multi-party consultations routinely encountered in NHS practice. No validated link has been established between DER and downstream clinical documentation quality - a low DER does not guarantee accurate speaker attribution on clinically significant utterances, and a moderate DER may be acceptable if the errors concentrate on non-clinical content. Word-level DER (WDER) is more clinically relevant than time-based DER but is rarely reported by vendors. Require WDER from vendors and request reporting stratified by utterance type: clinician instruction, patient symptom report, family contextual information, medication discussion. The aggregate DER number in isolation is technically correct but clinically uninterpretable.

---

### TP.DI-2 🟡 Speaker Attribution Accuracy

Percentage of utterances assigned to correct speaker. Misattributed medication instructions directly cause prescribing errors.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.DI-2 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Diarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
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

### TP.DI-3 🟡 Speaker Count Accuracy

Does the system correctly identify how many speakers are present? Particularly important for distinguishing 2-speaker (validated) from 3+-speaker (out-of-envelope) consultations. Over-counting fragments single speakers; under-counting merges distinct speakers.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.DI-3 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Diarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
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

> 💡 Speaker count is the gateway to multi-party robustness. If the system thinks there are 2 speakers when there are actually 3 (interpreter, family member), the third speaker's content is misattributed to one of the others - silently changing the clinical meaning of utterances.

---

### TP.DI-4 🔵 Speaker Boundary Precision

Temporal accuracy of where one speaker stops and another starts. Affects attribution at turn boundaries - words at the edge of a turn may be attributed to the wrong speaker.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.DI-4 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Diarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
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

> 💡 Boundary errors are the most common cause of speaker attribution errors at turn boundaries. The first or last word of a turn is the most likely to be misattributed - and often these are the words that carry clinical meaning ('yes' to a question about symptoms, 'no' to a question about allergies).

---

---

### Conversation Analysis sub-cluster

*Multi-role identification, code-switching, turn-taking in overlap, addressee recognition, and clinically weighted attribution. Extends the existing diarisation metrics (which focus on speaker counts and boundaries) into the semantics of multi-party clinical dialogue.*

---

### TP.DI-5 🟡 Speaker Role Identification F1

Accuracy of classifying speakers into clinical roles - clinician, patient, family member, nurse, interpreter, student - rather than just distinguishing anonymous speakers. Distinct from the existing Speaker Attribution Accuracy metric, which measures whether an utterance is assigned to the correct speaker *given that roles are known*. Role identification is the prerequisite step.

|Dimension              |Value                                                                |
|-----------------------|---------------------------------------------------------------------|
| **Reference** | TP.DI-5 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                               |
|**Measurement Cadence**|One-off gate                                                         |
|**Pipeline Layer**     |Diarisation                                                          |
|**Assurance Question** |Safety                                                               |
|**Measurement Method** |Computational                                                        |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                       |
|**Responsible Actors** |Vendor                                                               |
|**Maturity**           |Emerging                                                             |
|**Outcome Type**       |Proximal                                                             |
|**Applicability**      |AVT-Specific                                                         |
|**Source**             |mpathic.ai clinical ASR benchmark 2025; extends standard diarisation |

**Why this tier?**

> Safety-relevant whenever AVT is used outside simple dyadic consultations. Interpreter-mediated, family-present, and multidisciplinary scenarios are common in NHS practice. Role identification errors cause medication attribution errors and epistemic status inversions (patient reports vs clinician observes).

**Formal Definition**

```
Per-role precision, recall, and F1. Role set R ⊇ {clinician, patient, family_member, nurse, interpreter, student, other}. F1_macro = mean F1 across roles. Report per-role breakdown because aggregate hides minority-role failures (interpreter role is often the lowest-performing and the most safety-critical for attribution). Require minimum 0.90 F1 for clinician and patient roles; 0.80 for other identified roles.
```

**Limitations**

> Role identification often relies on content cues (who asks questions, who describes symptoms) rather than voice characteristics, which means errors correlate with atypical consultations - exactly where they matter most. Role-labelled ground truth is rarely available in clinical speech corpora.

**Novel Thinking / Implications**

> 💡 Role identification is more forgiving than individual speaker identification in one sense (you don't need to track specific individuals across sessions) but less forgiving in another (the consequences of confusing roles are semantic, not just attributional). A system that confuses "clinician" with "family member" in an interpreter-mediated consultation can end up attributing medication instructions to the wrong party.

---

### TP.DI-6 🟡 Code-Switching Detection Rate

Accuracy of detecting within-utterance language switching - a speaker moving between English and another language mid-sentence or across turns. Common in NHS consultations with EAL patients and interpreter-mediated encounters. Code-switching confounds ASR because most systems are trained on single-language audio and may transcribe the non-English segments as phonetically similar English, or drop them entirely.

|Dimension              |Value                                                 |
|-----------------------|------------------------------------------------------|
| **Reference** | TP.DI-6 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                |
|**Measurement Cadence**|One-off gate                                          |
|**Pipeline Layer**     |ASR / Transcription                                   |
|**Assurance Question** |Fairness & Equity                                     |
|**Measurement Method** |Computational                                         |
|**Lifecycle Phases**   |Pre-deployment                                        |
|**Responsible Actors** |Vendor                                                |
|**Maturity**           |Established                                           |
|**Outcome Type**       |Proximal                                              |
|**Applicability**      |AVT-Specific                                          |
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

> 💡 Code-switching is a genuine equity dimension distinct from accent. A patient with fluent English who occasionally uses terms from their first language for culturally specific concepts (family roles, traditional remedies, culturally defined symptoms) should have those terms captured, not erased. A system that silently drops non-English tokens is performing lossy documentation with equity implications - and the clinician reviewing the note has no signal that anything was lost.

---

### TP.DI-7 🟡 Turn-Taking Accuracy in Overlap

Accuracy of attributing words spoken during overlapping speech - when two or more speakers are simultaneously active. The existing Speaker Overlap Rate metric measures how much overlap occurs; this metric measures how well the system handles it when it does. Most ASR+diarisation pipelines degrade substantially in overlap, with one speaker's content being dropped or merged into the other.

|Dimension              |Value                                          |
|-----------------------|-----------------------------------------------|
| **Reference** | TP.DI-7 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                         |
|**Measurement Cadence**|One-off gate                                   |
|**Pipeline Layer**     |ASR + Diarisation                              |
|**Assurance Question** |Fidelity & Accuracy                            |
|**Measurement Method** |Computational                                  |
|**Lifecycle Phases**   |Pre-deployment                                 |
|**Responsible Actors** |Vendor                                         |
|**Maturity**           |Established                                    |
|**Outcome Type**       |Proximal                                       |
|**Applicability**      |AVT-Specific                                   |
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

### TP.DI-8 🔵 Clinical-Perspective HEWER (cpHEWER)

Hypothesis-Error Word Error Rate weighted by clinical importance of the utterance speaker-and-content combination. An error on a clinician's medication instruction is weighted much higher than an equivalent error on a family member's small-talk contribution. Introduced in the mpathic.ai benchmark as a clinically-aware alternative to standard diarisation error rate.

|Dimension              |Value                                       |
|-----------------------|--------------------------------------------|
| **Reference** | TP.DI-8 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research              |
|**Measurement Cadence**|One-off gate                                |
|**Pipeline Layer**     |ASR + Diarisation                           |
|**Assurance Question** |Safety                                      |
|**Measurement Method** |Computational                               |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit              |
|**Responsible Actors** |Vendor, Academic                            |
|**Maturity**           |Emerging                                    |
|**Outcome Type**       |Proximal                                    |
|**Applicability**      |AVT-Specific                                |
|**Source**             |mpathic.ai clinical ASR benchmark 2025      |

**Why this tier?**

> Research metric. Requires both role-labelled ground truth and a clinical importance ontology - neither of which is standardised. Conceptually valuable but not operationally ready for routine deployment assessment.

**Formal Definition**

```
cpHEWER = Σ(w(role, content) × error(i)) / Σ w(role, content), where w is the clinical importance weight for the (speaker role, content type) combination. Weight matrix: clinician medication instruction = 10.0; clinician safety-netting = 10.0; patient red-flag symptom = 9.0; patient history = 5.0; family contextual information = 3.0; small talk = 0.1. Matrix requires clinical consensus.
```

**Limitations**

> Weight matrix is inherently subjective. No standardised matrix exists. Requires accurate role identification as prerequisite - compounds with Speaker Role Identification F1 errors. Benchmark datasets with the required role-and-content annotation do not exist at scale.

**Novel Thinking / Implications**

> 💡 cpHEWER is the diarisation-layer equivalent of Medical WER at the transcription layer: both attempt to weight errors by clinical consequence rather than treating all errors equally. The same standardisation gap applies - without a nationally agreed weight matrix, every vendor's cpHEWER number means something different. This is a candidate for national body specification work.

---

### TP.DI-9 🔵 Addressee Recognition Accuracy

In multi-party consultations, correctly identifying who the speaker is addressing - the patient, a specific family member, another clinician, or the room at large. Affects the pragmatic interpretation of utterances: "you should stop smoking" addressed to the patient is a clinical instruction; addressed to a family member present it is different content entirely.

|Dimension              |Value                                            |
|-----------------------|-------------------------------------------------|
| **Reference** | TP.DI-9 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research                   |
|**Measurement Cadence**|One-off gate                                     |
|**Pipeline Layer**     |Diarisation                                      |
|**Assurance Question** |Fidelity & Accuracy                              |
|**Measurement Method** |Computational                                    |
|**Lifecycle Phases**   |Pre-deployment                                   |
|**Responsible Actors** |Vendor, Academic                                 |
|**Maturity**           |Proposed / Novel                                 |
|**Outcome Type**       |Proximal                                         |
|**Applicability**      |AVT-Specific                                     |
|**Source**             |Multi-party dialogue research; pragmatics literature|

**Why this tier?**

> Research frontier. No current AVT system explicitly models addressee. Academic research area - cannot be deployed in routine assessment today.

**Formal Definition**

```
For each utterance u in multi-party encounter: addressee(u) ∈ {patient, family_member_1, family_member_2, clinician, room}. Accuracy = |correctly_identified_addressee| / |total_utterances_in_multi_party_segments|. Requires turn-level annotation of addressee identity.
```

**Limitations**

> Addressee is often ambiguous even to humans - clinicians frequently address statements to "the room" without a specific target. Annotation inter-rater reliability is low. Technical solutions require multimodal input (gaze, body orientation) not available from audio alone.

**Novel Thinking / Implications**

> 💡 Addressee recognition is the pragmatic layer above speaker attribution. When a clinician turns to a family member and says "make sure she takes these at the same time each day", the instruction is for the family member, not the patient. If the AVT attributes this to the patient, the resulting note reads as a patient-directed instruction that the patient may not have even heard clearly. This kind of pragmatic misattribution is invisible to diarisation error rate but directly affects clinical documentation accuracy.

### TP.SN-1 🟡 ROUGE Scores

N-gram overlap between generated and reference text. Demonstrably inadequate for clinical safety evaluation.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-1 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
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
# NOTE: hypothesis omits specific drug name and dose -
# a safety-critical omission - but still scores ~0.58 ROUGE-1.
# This is exactly why ROUGE is insufficient for clinical eval.
```

**References**

- **Original**: [Lin (2004) - ROUGE: A Package for Automatic Evaluation of Summaries](https://aclanthology.org/W04-1013/)
- **Inadequacy**: Croxford et al. (2025) - LLM-as-Judge outperforms ROUGE/BERTScore

**Limitations**

> Measures lexical overlap, not clinical accuracy. Continued use as primary vendor marketing metric is a red flag.

**⚠️ Underspecification Warning (Tier C - technically rigorous, clinically invalid)**

> Published evidence demonstrates near-zero correlation between ROUGE and human clinical judgment in clinical summarisation evaluation. Croxford et al. (2025, npj Digital Medicine) reported ROUGE-L Kendall-Tau of just 0.080 with expert clinician scoring on clinical diagnosis generation - indistinguishable from random for practical purposes. A separate investigation of automated metrics for medical note generation (ar5iv 2305.17364) documented catastrophic failure modes with Spearman ρ between −0.66 and −0.77 in some medical contexts, meaning higher ROUGE scores actively correlated with worse human judgments. The root cause is that string matching penalises clinically valid paraphrase and rewards surface overlap regardless of clinical meaning. **ROUGE must not be used as a standalone clinical quality indicator.** Retain only for technical benchmarking, and always report alongside a validated clinical instrument (PDSQI-9, CREOLA, or LLM-as-a-Judge with bias quantification).

**Novel Thinking / Implications**

> 💡 Necessary but not sufficient pre-deployment screen. Tells you almost nothing about clinical safety.

*See also: BERTScore - both members of the Reference-Based Text Similarity family. Both metrics measure surface or semantic similarity to a reference text, not clinical quality. Always report alongside a validated clinical instrument (PDSQI-9, CREOLA, or LLM-as-a-Judge with bias quantification).*

---

### TP.SN-2 🔵 BERTScore

Semantic similarity via contextual embeddings. More meaning-aware than ROUGE but still linguistic, not clinical.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-2 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
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
# F1 tensor - higher = more semantically similar
# BUT: semantic similarity ≠ clinical correctness
```

**References**

- **Paper**: [Zhang et al. (2020) - BERTScore](https://arxiv.org/abs/1904.09675)

**Limitations**

> Linguistic similarity ≠ clinical correctness. Correlates poorly with clinician judgements.

**⚠️ Underspecification Warning (Tier C - better than ROUGE but insufficient alone)**

> BERTScore-R achieves approximately Pearson 0.62 correlation with omission rate in clinical summarisation (Croxford et al. 2025) - materially better than ROUGE but still inadequate as a standalone clinical quality indicator. The underlying limitation is the same as ROUGE: semantic similarity is not clinical correctness. A note can be semantically close to the reference while missing a clinically critical element, or semantically distant while conveying the same clinical meaning through appropriate medical abstraction. BERTScore is useful as one input to a multi-metric assessment but should never be reported as the primary quality finding. Pair with PDSQI-9 or an LLM-as-a-Judge protocol that has been subjected to bias quantification.

*See also: ROUGE Scores - both members of the Reference-Based Text Similarity family. BERTScore is materially better than ROUGE as a text similarity metric but shares the fundamental limitation: semantic closeness to a reference is not clinical correctness. Always report alongside a validated clinical instrument.*

---

### TP.SN-3 🟡 PDSQI-9 (Physician Documentation Quality Instrument)

Nine-item validated rubric. Gold standard for human evaluation - now automatable via LLM-as-a-Judge.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-3 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Stetson et al.; Croxford et al. 2025 |

**Why this tier?**

> Validated gold-standard rubric. Resource-intensive without LLM automation. Recommended for periodic audit (quarterly sample).

**Formal Definition**

```
Nine dimensions scored 1–5 Likert: Up-to-date, Accurate, Thorough, Useful, Organised, Comprehensible, Succinct, Synthesised, Internally consistent. Composite = mean across dimensions. Published IRR: ICC 0.43–0.68.
```

**References**

- **Instrument**: [Stetson et al. (2012) - PDSQI-9, JAMIA](https://doi.org/10.1197/jamia.M2248)
- **LLM automation**: Croxford et al. (2025) - GPT-o3-mini ICC 0.818

**Limitations**

> Resource-intensive without LLM automation. NHS-context validation of automated scoring needed.

**Novel Thinking / Implications**

> 💡 GPT-o3-mini ICC 0.818 opens automated PDSQI-9 at scale - needs independent NHS validation.

---

### TP.SN-4 🟡 CREOLA Error Taxonomy Scores

Structured error categories: omission, addition, incorrect - with sub-types. 12,999 annotated sentences. Now underpins Tortus automated guardrails.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-4 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Deployer, Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Asgari et al. 2025 (Tortus/GOSH). Now underpins automated guardrails. |

**Why this tier?**

> Most granular UK-origin error taxonomy. Recommended for deployers with access to CREOLA platform or equivalent structured review.

**Formal Definition**

```
Hierarchical taxonomy: L1 - Omission, Addition, Incorrect. L2 sub-types: Omission → {key finding, medication, allergy, plan}; Addition → {unsupported claim, confabulated detail, inferred}; Incorrect → {wrong value, wrong attribution, wrong timing}. Each sentence gets error vector. Aggregate: rate per category, severity-weighted composite.
```

**References**

- **CREOLA**: Asgari et al. (2025) - Tortus / Great Ormond Street Hospital

**Limitations**

> Developed in secondary care paediatrics. Primary care transferability needs validation.

**Novel Thinking / Implications**

> 💡 CREOLA's transition from evaluation instrument to automated guardrail shows the evaluation-to-guardrail pipeline other vendors should replicate.

---

### Family: Clinical Content Fidelity

> **Parent construct** - whether the generated note faithfully represents the clinical content of the source consultation.
>
> The next five metrics measure different facets of a single underlying construct. Treating them as unrelated obscures three important things: the existence of distinct error subtypes with different clinical implications, the difference between factuality and faithfulness, and the reason that aggregate rates can mask serious category-specific failures.
>
> **Subtypes are not substitutes.** The CREOLA framework (Asgari et al., npj Digital Medicine 2025) and the AutoscriberValidate analysis (medRxiv 2026) identify at least five distinct error subtypes within this family, each with different clinical implications and different mitigations:
>
> - **Fabrication** - completely invented clinical content with no basis in the source. CREOLA data attribute 43% of observed hallucinations to this subtype. Fictional examination findings are the canonical example. Most dangerous.
> - **Context conflation** - content misattributed between different parts of the conversation or between speakers, e.g. one patient's symptom attributed to another's discussion in a multi-encounter session. Compounds diarisation errors.
> - **Incorrect negation** - polarity reversal of a clinical assertion, e.g. "no chest pain" rendered as "chest pain". Measured by the dedicated Negation Handling Accuracy metric in this family. Directly causes clinical harm via phantom allergies, eliminated presenting symptoms, and inverted medication instructions.
> - **Speculation or inference beyond source** - plausible but unverifiable content that extends beyond what was discussed, e.g. adding a likely diagnosis the clinician never stated. The summariser is exercising clinical judgment it shouldn't.
> - **Certainty inflation** - clinician uncertainty markers ("possibly", "consistent with", "rule out") stripped from the note, converting hedged observations into definitive statements. Measured by the Uncertainty Marker Preservation metric in this family.
>
> Subtypes have different root causes (ASR vs LLM vs diarisation) and different mitigations. An aggregate "hallucination rate" of 2% means very different things if 90% of the errors are speculation vs if 90% are fabrications.
>
> **Factuality and faithfulness are distinct dimensions within the family.** Factuality is world-correctness: does the statement match clinical reality? Faithfulness is source-correctness: does the statement match what was discussed? A note can be factually correct but unfaithful (the summariser inferred a correct diagnosis the clinician never stated) or faithful but factually incorrect (the summariser accurately captured the clinician's mistake). For ambient scribes, **faithfulness is the primary assurance concern** because the scribe's job is to represent the consultation, not to exercise clinical judgment. A system that silently corrects clinician errors or adds information the clinician did not state has exceeded its safe operating scope regardless of whether the resulting statement is factually true.
>
> **Recommendation for measurement.** When measuring content fidelity in periodic audit, require subtype reporting rather than aggregate rate only. A single headline number hides the distribution that matters for intervention. Vendors reporting only aggregate rates should be asked to provide the CREOLA subtype breakdown or equivalent.
>
> **Metrics in this family:**
> - 🟢 **Hallucination Rate** - the aggregate rate of generated content unsupported by source. Entry point to the family. *See underspecification warning re: definitional instability.*
> - 🟢 **Omission Rate** - the silent killer. Arguably more dangerous than hallucination because omissions are invisible to the reviewer looking at a clean-looking note.
> - 🔵 **Confabulation Detection (Support × Severity)** - vendor-proprietary two-axis approach (Abridge) that stratifies by evidence support and clinical severity. Methodologically superior where available.
> - 🟢 **Negation Handling Accuracy** - measures the Incorrect Negation subtype as a dedicated metric because of its direct clinical harm potential.
> - 🟢 **Uncertainty Marker Preservation** - measures the Certainty Inflation subtype as a dedicated metric because certainty inflation is the more dangerous direction of epistemic drift.

---

### TP.SN-5 🟢 Hallucination Rate

Proportion of generated content unsupported by source. Currently defined inconsistently across vendors.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-5 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Continuous, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Various; Tortus 1.47% per sentence |

**Why this tier?**

> Core safety metric. NAS Day Zero SPI with <2% review and ≥5% pause thresholds. Every deployer must measure this through periodic clinical audit even if methodology is manual.

**Formal Definition**

```
HR = |S_unsupported| / |S_total|, where S_total = atomic propositions in generated note, S_unsupported = subset not evidentially supported by source transcript. Severity: benign (formatting), moderate (non-safety addition), critical (fabricated clinical content).
```

**Reference Standard**

> Source transcript is primary ground truth. Atomic propositions in the generated note are classified {Fully Supported, Partially Supported, Unsupported} via structured clinician review using the CREOLA subtype taxonomy (Asgari et al. 2025). Unsupported = hallucination. Inter-rater reliability target: ICC ≥ 0.75 on the subtype classification. NLI-based automated detection (e.g. the CHECK framework, arXiv 2506.11129) is acceptable as a primary screen if reported AUC ≥ 0.90 against a human-reviewed reference set; remains subject to the underspecification warning below until concordance with clinician review is established locally.

**Operational Specification**

> - **Window:** per-note (not per-sentence aggregate), covering all atomic propositions in the generated note.
> - **Population:** all clinical consultations during the measurement period; exclude only transcription failures (ASR confidence < 0.7).
> - **Subtype reporting MANDATORY:** aggregate rate plus CREOLA subtype breakdown - Fabrication / Context Conflation / Incorrect Negation / Speculation / Certainty Inflation. Aggregate-only reporting is not sufficient for Tier 1 compliance.
> - **Severity classification MANDATORY:** every flagged proposition labelled benign / moderate / critical, with critical rate reported separately.
> - **Aggregation:** weighted aggregate HR_w = (0.1·benign + 0.5·moderate + 1.0·critical) / N_total. Unweighted rate may be reported alongside but not in place of HR_w.

**Threshold Guidance**

> ⚠️ **Provenance:** the < 2 % gate and ≥ 5 % pause trigger derive from the NAS Day Zero SPI cited in the Why-this-tier rationale; the > 3 % monitoring alert and the 500-note test-set floor are **proposed in v3.3 as starting points**, not externally validated. All numbers below are indicative and require local calibration against deployment context (specialty mix, consultation length, vendor reference dataset) before contractual use.
>
> - **Pre-deployment gate:** HR_w ≤ 2 % on a representative ≥500-note test set; critical-subtype rate < 0.5 %.
> - **Continuous monitoring:** weekly HR_w; alert if > 3 % sustained two weeks or any new critical subtype emerges.
> - **Pause trigger:** critical-subtype rate ≥ 5 % or HR_w > 5 % for three consecutive days. Mirrors the NAS Day Zero SPI threshold cited in the Why-this-tier rationale.

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
# NOTE: NLI is coarse - doesn't distinguish benign
# formatting from dangerous clinical fabrication.
```

**References**

- **Tortus data**: 1.47% per sentence (Asgari et al. 2025)
- **Abridge**: Support × severity matrix (Oberst et al. 2024/2025)

**Limitations**

> Definition varies. No standard severity weighting.

**⚠️ Underspecification Warning (Tier B - conceptually central, definitionally unstable)**

> The term "hallucination" has no universally accepted operational definition in clinical NLG. The CREOLA framework (Asgari et al., npj Digital Medicine 2025) explicitly identifies this ambiguity as a fundamental measurement challenge. Reported rates across the published literature range from 1–3% in deployed ambient scribe studies to 43–67% in adversarial LLM clinical benchmarks - a span that largely reflects methodological differences rather than true performance variation. Only two public reference datasets exist for AVT hallucination evaluation (ACI Bench, PriMock), which limits cross-study comparability. Promising recent work: the CHECK framework (arXiv 2506.11129) reduced hallucination from 31% to 0.3% using information-theoretic classification with AUC 0.95–0.96 and is a candidate standard for operational definition. Until a consensus definition emerges, require reporting of: (a) the specific subtype taxonomy used (CREOLA or equivalent); (b) inter-rater reliability on the taxonomy; (c) the reference dataset; (d) the severity classification scheme.

**Novel Thinking / Implications**

> 💡 NAS proposes <2% major hallucination Day Zero SPI, ≥5% pause trigger. 'Major' needs operational definition.

*See also: Omission Rate, Confabulation Detection, Negation Handling Accuracy, Uncertainty Marker Preservation - all members of the Clinical Content Fidelity family. The CREOLA subtype taxonomy (Fabrication / Context Conflation / Incorrect Negation / Speculation / Certainty Inflation) provides the structural decomposition.*

---

### TP.SN-6 🟢 Omission Rate

Clinically relevant source content absent from note. More dangerous than hallucination - omissions are invisible to the reviewer.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-6 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Tortus 3.45%; CREOLA taxonomy |

**Why this tier?**

> Arguably more dangerous than hallucination because omissions are invisible to the reviewer. Must be included in periodic clinical note audit alongside hallucination rate.

**Formal Definition**

```
OR = |P_missing| / |P_reference|. P_reference = clinically relevant propositions in source. Clinical relevance per CREOLA: key findings, medications, allergies, plan elements, safety-netting, red-flags are mandatory.
```

**Reference Standard**

> Source transcript + clinician review. The reference set P_reference is the clinically relevant propositions identified by structured clinician review of the source transcript, using the CREOLA mandatory categories (key findings, medications, allergies, plan elements, safety-netting, red-flags) as the floor. A proposition counts as omitted when it appears in P_reference and does not appear in the generated note in any form (verbatim, paraphrase, or structurally implied). Inter-rater reliability target: ICC ≥ 0.75 on the reference-set construction, since omission rate is bounded above by what reviewers agree was relevant in the first place.

**Operational Specification**

> - **Window:** per-note, covering all clinically relevant propositions identified in the source transcript.
> - **Population:** all clinical consultations during the measurement period; same exclusions as TP.SN-5.
> - **Category breakdown MANDATORY:** report omission rate by CREOLA mandatory category (findings / medications / allergies / plan / safety-netting / red-flags). A 5 % aggregate that hides 30 % missed allergies is unacceptable; category-stratified reporting catches this.
> - **Severity classification MANDATORY:** flagged omissions labelled benign / moderate / critical. Allergies, red-flag symptoms, medication doses, and safety-netting omissions are critical by default; downgrading requires documented justification.
> - **Aggregation:** weighted aggregate OR_w = (0.1·benign + 0.5·moderate + 1.0·critical) / |P_reference|.

**Threshold Guidance**

> ⚠️ **Provenance:** the Tortus 3.45 % omission baseline cited above informs the pre-deployment gate framing, but the specific numbers (≤ 3 % gate, 5 % critical-category alert, 10 % critical-category pause, 1.5× drift trigger) are **proposed in v3.3 as starting points**, not externally validated. Indicative; require local calibration before contractual use.
>
> - **Pre-deployment gate:** OR_w ≤ 3 % on a representative ≥500-note test set; critical-category omission rate < 1 % for any single mandatory category.
> - **Continuous monitoring:** monthly OR_w by category; alert if any mandatory category exceeds 5 % critical omission rate or if aggregate OR_w drifts > 1.5× the deployment-baseline established in the first 30 days.
> - **Pause trigger:** any mandatory-category critical-omission rate ≥ 10 % or OR_w > 8 % aggregate.

**References**

- **Tortus**: 3.45% omission rate (Asgari et al. 2025)

**Limitations**

> Harder to detect than hallucination because the reference set must be constructed from the source rather than checked against the output. Automated detection at scale unsolved; the reference-set construction step is the bottleneck and the dominant source of inter-rater variance.

**Novel Thinking / Implications**

> 💡 The silent killer. A clean-looking note gives no cue something is missing. Argues for source-linked evidence as structural safeguard.

*See also: Hallucination Rate, Confabulation Detection, Negation Handling Accuracy, Uncertainty Marker Preservation - all members of the Clinical Content Fidelity family. Omission is the faithfulness failure that cannot be detected without source-linked evidence (see Linked Evidence / Provenance Tracing).*

---

### TP.SN-7 🔵 Confabulation Detection (Support × Severity)

Two-axis classification: evidential support × clinical severity. Abridge model achieves 97% detection. Produces risk matrix, not single rate.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-7 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Vendor-Proprietary |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Abridge whitepaper (50,000+ training examples) |

**Why this tier?**

> Vendor-proprietary (Abridge). Methodologically superior two-axis approach but not independently implementable. Informs what a national standard should require.

**Formal Definition**

```
Each proposition p classified on: Support(p) ∈ {Fully Supported, Partially Supported, Unsupported, Contradicted} × Severity(p) ∈ {Benign, Moderate, Critical}. Risk R(p) = Support_weight × Severity_weight. Safety-critical quadrant: {Unsupported ∨ Contradicted} × {Critical}.
```

**References**

- **Abridge**: Oberst, Liang, Lipton (2024/2025) - 97% vs GPT-4o 82%

**Limitations**

> Proprietary. Not independently validated.

**Novel Thinking / Implications**

> 💡 Two-axis approach is methodologically superior. National standard should mandate dimensional approach even if implementation varies.

*See also: Hallucination Rate, Omission Rate, Negation Handling Accuracy, Uncertainty Marker Preservation - all members of the Clinical Content Fidelity family. The Support × Severity axes formalise what the aggregate Hallucination Rate metric leaves implicit.*

---

### TP.SN-8 🔵 VeriFact Factual Verification

Automated EHR fact-checking via RAG + LLM-as-a-Judge. 92.7% agreement with clinicians (exceeds inter-clinician 88.5%). Open-source, locally deployable.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-8 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | LLM-as-Judge |
| **Lifecycle Phases** | Continuous, Periodic Audit |
| **Responsible Actors** | Deployer, National Body |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
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

- **NEJM AI**: [Chung et al. (2025) - VeriFact](https://ai.nejm.org/doi/full/10.1056/AIdbp2500418)
- **Code**: [GitHub - philipchung/verifact](https://github.com/philipchung/verifact)

**Limitations**

> Validated on MIMIC-III (US ICU). NHS primary care transferability untested. Requires FHIR R4 read access.

**Novel Thinking / Implications**

> 💡 Most credible path to automated continuous faithfulness monitoring. Open-source = no vendor dependency. National pilot would generate first independent continuous accuracy data.

---

### TP.SN-9 🟡 LLM-as-a-Judge (PDSQI-9 Proxy)

Reasoning LLMs scoring documentation at 27× speed (22s vs 600s). Enables 100% note evaluation.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-9 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | LLM-as-Judge |
| **Lifecycle Phases** | Continuous, Periodic Audit |
| **Responsible Actors** | Deployer, National Body |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Croxford et al. 2025 |

**Why this tier?**

> 27× speed improvement enables practical scale. Recommended for deployers with API access. Needs NHS-context validation of scoring calibration.

**Formal Definition**

```
Reasoning LLM prompted with PDSQI-9 rubric scores each note on 9 dimensions. ICC = 0.818 (o3-mini) vs 0.43 (human-human). Non-reasoning models achieve substantially lower agreement.
```

**References**

- **Study**: Croxford et al. (2025) - npj Digital Medicine

**Limitations**

> One LLM evaluating another = correlated failure modes. Evaluation LLM should be different model family.

**⚠️ Underspecification Warning (Tier C - high measured reliability, unknown validity)**

> LLM-as-a-Judge has documented biases that are rarely quantified in published deployment: position bias (prefers the first response in pairwise comparison), verbosity bias (prefers longer responses), self-enhancement bias (prefers outputs from the same model family as the judge), and fine-grained scoring unreliability (inconsistent discrimination at the high end of Likert scales). The headline Croxford et al. (2025) finding of GPT-o3-mini achieving ICC 0.818 with human evaluators on PDSQI-9 should be read alongside a separate Rwanda clinical LLM evaluation study that found LLM judges correlated more strongly with non-expert than expert annotators - apparent reliability that may reflect alignment with a particular class of evaluator rather than with clinical ground truth. This is the most uncomfortable possibility in automated evaluation: high ICC with humans that does not generalise to correctness. Any deployment relying on LLM-as-a-Judge for safety-relevant decisions should run the proposed **LLM-Judge Bias Quantification** metric (see Meta-evaluation section) and document residual uncertainty before treating judge outputs as substitutes for expert review.

**Novel Thinking / Implications**

> 💡 27× speed enables 100% evaluation. But meta-problem: correlated blindspots between evaluator and evaluated.

---

### TP.SN-10 🔵 MedHELM LLM-Jury

121 tasks, 22 subcategories. LLM-jury ICC 0.47 exceeds clinician-clinician 0.43. Capability gate, not deployment evidence.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-10 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | LLM-as-Judge |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor, National Body |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Bedi et al., Stanford CRFM, May 2025 |

**Why this tier?**

> Research benchmark for pre-deployment capability gating. Vendor responsibility. Value is as minimum capability floor, not deployment safety evidence.

**Formal Definition**

```
Holistic Evaluation of Language Models for Medicine. LLM-jury: panel of LLMs independently scores, aggregated via majority/mean. Available via Microsoft MedEvals on Azure AI Foundry.
```

**References**

- **Paper**: [Bedi et al. (2025) - MedHELM, Stanford CRFM](https://arxiv.org/abs/2505.23802)

**Limitations**

> Benchmarks ≠ deployment. MEDIC knowledge-execution gap is the critical caveat.

**Novel Thinking / Implications**

> 💡 Value is as minimum capability gate, not deployment safety evidence.

---

### TP.SN-11 🔵 MEDIC Cross-Examination

One LLM interrogates another to detect hallucinations without references. Identifies the 'knowledge-execution gap'.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-11 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | LLM-as-Judge |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Kanithi et al. 2025 |

**Why this tier?**

> Research framework. Knowledge-execution gap finding is important but MEDIC methodology is not yet deployable outside research settings.

**Formal Definition**

```
Examiner LLM probes claims in target output, evaluates consistency. Knowledge-execution gap KE = benchmark_accuracy - operational_accuracy.
```

**References**

- **Paper**: Kanithi et al. (2025) - MEDIC

**Limitations**

> Correlated blindspots possible.

**Novel Thinking / Implications**

> 💡 Knowledge-execution gap: exam performance ≠ operational performance. Pre-deployment benchmarks are structurally insufficient.

---

### TP.SN-12 🟡 Linked Evidence / Provenance Tracing

Every text span linked to source audio. Architectural safety property - transforms review from 'looks right?' to 'is this supported?'

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-12 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Vendor-Proprietary |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Abridge Linked Evidence |

**Why this tier?**

> Architectural safety property. Should be a procurement requirement - provenance tracing transforms review quality. Vendor must provide.

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

### TP.SN-13 🔵 SCRIBE Framework Composite

First comprehensive multi-modal AVT evaluation: simulation + computational + human + LLM. Minimum standard for pre-deployment.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-13 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Academic, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Wang et al. 2025 (Duke/MedStar) |

**Why this tier?**

> Comprehensive research framework. Should be the aspiration for pre-deployment evaluation but requires simulation infrastructure no NHS deployer currently has.

**Formal Definition**

```
Four modalities: (1) Simulated encounters with ground truth; (2) Computational metrics on outputs; (3) Structured clinician review; (4) LLM evaluation. Composite requires passing all four - no single modality compensates for another.
```

**References**

- **Paper**: [Wang et al. (2025) - SCRIBE, npj Digital Medicine](https://doi.org/10.1038/s41746-025-01449-w)

**Limitations**

> Complex to implement. Research framework, not deployable toolkit.

**Novel Thinking / Implications**

> 💡 Demonstrates no single modality is sufficient. Should be minimum pre-deployment standard.

---

### TP.SN-14 🟡 Template Modification Underspecification Score

INSYTE underspecification delta when clinicians modify AVT templates. Every modification potentially invalidates the safety case.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-14 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer, Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | INSYTE analysis; DCB0129 gap |

**Why this tier?**

> Relevant whenever deployers allow template customisation. Must monitor if templates are configurable - every modification potentially invalidates the safety case.

**Formal Definition**

```
For default template T₀ with INSYTE underspecification U₀, modified template T' with U': ΔU = U' - U₀. If ΔU > threshold, modified template exits validated safety envelope → re-evaluation required under DCB0129.
```

**References**

- **INSYTE**: INSYTE autonomy classification - DCB0129 structural gap

**Limitations**

> Not yet operationalised for routine use.

**Novel Thinking / Implications**

> 💡 Hidden risk vector: template customisation as feature, but every modification potentially invalidates safety case.

---

### TP.SN-15 🟢 Negation Handling Accuracy

Does the summary correctly preserve negations? 'No chest pain' vs 'chest pain' is a clinically critical distinction that LLMs commonly mishandle, particularly when negation is far from the negated concept.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-15 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Clinical NLP literature; identified as systematic LLM failure mode |

**Why this tier?**

> Safety-critical and well-documented LLM failure mode. Should be tested pre-deployment and periodically re-audited. Negation errors directly cause clinical harm.

**Formal Definition**

```
For each negated concept in reference: Negation Preserved = (concept appears in summary) AND (negation marker correctly attached). Negation Accuracy = |correctly_negated| / |total_negations|. Failure modes: dropped negation (becomes positive), added negation (becomes negative), wrong scope.
```

**Reference Standard**

> Source transcript + ConText-style negation detection (Harkema et al.) as the primary algorithmic floor, with clinician adjudication where automated detection is ambiguous. Each negated concept in the source is classified by **negation type** (explicit / implicit / hedged / conditional / historical) and **clinical category** (allergy / symptom / sign / diagnosis / medication / red-flag). Inter-rater reliability target: ICC ≥ 0.80 on negation type classification (higher than the TP.SN-5/-6 floor because negation typing is a more constrained task).

**Operational Specification**

> - **Negation types in scope (MANDATORY):** explicit ("no chest pain"), implicit ("denies dyspnoea"), and hedged ("unlikely to be cardiac"). Conditional negation ("if no improvement") and historical negation ("previously denied") MUST be reported separately and counted only when their truth-value at the time of the consultation can be determined from the transcript.
> - **Scope correctness:** preservation requires both the concept and the negation's syntactic scope. "No history of MI" preserved as "no MI" is a scope error and counts as a failure even though the concept and negation both appear.
> - **Population:** all clinical consultations during the measurement period. For pre-deployment gating, supplement with an **adversarial test set** of ≥200 sentences specifically constructed to challenge negation handling (long-distance negation, multiple negations per sentence, double negatives, implicit forms). Adversarial-set performance reported separately from real-consultation performance.
> - **Severity classification MANDATORY:** failures by clinical category, with allergy / red-flag / medication-dose negation errors classified critical by default.
> - **Aggregation:** report per-type accuracy and per-category accuracy. A weighted aggregate NA_w using the same 0.1 / 0.5 / 1.0 severity weights as TP.SN-5/-6 is the headline figure.

**Threshold Guidance**

> ⚠️ **Provenance:** all numbers below (≥ 98 % real-consultation NA_w, ≥ 90 % adversarial NA_w, ≥ 200-sentence adversarial floor, < 95 % pause trigger) are **proposed in v3.3 as starting points**, not externally validated. The zero-allergy-failure gate reflects the clinical-safety logic in the Novel Thinking section but is not externally cited. Indicative; require local calibration before contractual use.
>
> - **Pre-deployment gate:** real-consultation NA_w ≥ 98 %; adversarial-test NA_w ≥ 90 %; zero allergy-category negation failures on the adversarial test set.
> - **Continuous monitoring:** monthly real-consultation NA_w by category; alert on any allergy / red-flag / medication-dose category failure within the audit window.
> - **Pause trigger:** any allergy-category critical failure in production traffic, or NA_w < 95 % for two consecutive audit cycles.

**References**

- **Negation in clinical NLP**: ConText algorithm (Harkema et al.); standard clinical NLP problem

**Limitations**

> Negation detection itself is imperfect. Clinical negation has subtleties: hedged negation ('unlikely to be'), conditional negation ('if no improvement'), historical negation ('previously denied'). The Operational Specification above brings these into scope by requiring explicit reporting; it does not solve the underlying detection problem, only makes the gap visible.

**Novel Thinking / Implications**

> 💡 Negation handling is the single most clinically dangerous LLM failure mode. A summary that drops 'no' from 'no allergies' creates a phantom allergy. A summary that adds 'no' to 'has chest pain' eliminates a presenting symptom. Both can cause direct harm. This deserves dedicated testing with adversarially constructed test cases - sentences specifically designed to challenge negation handling.

*See also: Hallucination Rate, Omission Rate, Confabulation Detection, Uncertainty Marker Preservation - all members of the Clinical Content Fidelity family. Negation failure is one subtype (Incorrect Negation) made explicit as a dedicated metric because of its direct clinical harm potential.*

---

### TP.SN-16 🟡 Temporal Accuracy

Preservation of when things happened. 'Patient had chest pain three weeks ago' vs 'patient has chest pain' is the difference between historical and presenting complaint. LLMs frequently collapse temporal markers when summarising.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-16 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
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

> 💡 Temporal collapse is a subtle but dangerous failure mode. 'Patient had a heart attack five years ago' becoming 'patient has had a heart attack' loses the time information that distinguishes acute from historical. The clinical implications differ entirely. This is particularly relevant for problem list management - historical conditions should not be coded as active.

---

### TP.SN-17 🟡 Temporal Event Ordering Accuracy

Accuracy of reconstructing the chronological sequence of clinical events from non-linear conversation. Patients rarely describe symptoms in temporal order - they jump between current symptoms, historical episodes, family history, and future concerns. The summary must impose a coherent timeline. Distinct from the existing Temporal Accuracy metric, which covers tense and time-marker preservation at the sentence level; this metric covers event sequencing across the whole note.

|Dimension              |Value                                                   |
|-----------------------|--------------------------------------------------------|
| **Reference** | TP.SN-17 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                  |
|**Measurement Cadence**|Periodic audit                                          |
|**Pipeline Layer**     |Summarisation                                           |
|**Assurance Question** |Safety                                                  |
|**Measurement Method** |Hybrid                                                  |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                          |
|**Responsible Actors** |Vendor, Deployer                                        |
|**Maturity**           |Emerging                                                |
|**Outcome Type**       |Proximal                                                |
|**Applicability**      |AVT-Contextualised                                      |
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

### TP.SN-18 🟡 Quantifier Preservation

Preservation of clinical qualifiers: 'occasional', 'frequent', 'constant', 'mild', 'moderate', 'severe', 'intermittent'. LLMs often drop or paraphrase these, losing diagnostic information that affects clinical reasoning.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-18 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Identified as systematic LLM summarisation failure mode |

**Why this tier?**

> Important quality dimension that current metrics don't capture. Periodic audit recommended. Annotated test cases would be straightforward to construct.

**Formal Definition**

```
For each quantifier in reference: Quantifier Preservation = (quantifier present in summary) OR (semantically equivalent quantifier present). Track: dropped quantifiers, paraphrased quantifiers (acceptable), replaced quantifiers (unacceptable - changes severity).
```

**Limitations**

> Quantifier semantics are imprecise. Clinical training varies in how quantifiers are interpreted.

**Novel Thinking / Implications**

> 💡 'Occasional headaches' becoming 'headaches' loses the frequency information that distinguishes a normal variant from a clinical concern. 'Severe' becoming 'present' eliminates the severity assessment. These dropped qualifiers compound across the note - by the end, the clinical picture has been subtly distorted in ways that affect downstream decisions.

---

### Family: Medication Safety Thread

> **Parent construct** - the family of metrics that track medication information accuracy across the full pipeline, from spoken consultation to structured EPR record. Medication errors are the canonical safety-critical failure mode in clinical documentation AI.
>
> Unlike the other families in this taxonomy, the Medication Safety Thread spans multiple pipeline layers and multiple groups: extraction and event classification at the summarisation layer, terminology coding at the clinical coding layer, and downstream outcome monitoring at the patient experience layer. The family exists because a medication error can originate at any of these stages, and measuring only one stage gives false assurance about the others.
>
> **The safety argument.** A medication mentioned in consultation passes through at least four processing stages before it affects patient care: (1) ASR must transcribe the drug name, dose, and frequency correctly; (2) the summariser must extract these attributes and classify the medication event (start, stop, change); (3) the clinical coder must map to the correct dm+d concept; (4) the EPR write-back must place the medication data in the correct structured field. An error at any stage propagates - and the stages are tested by different metrics in different groups. The family framing makes the end-to-end thread visible.
>
> **Metrics in this family:**
> - 🟡 **Medication Attribute Extraction F1** (Summarisation / NLP) - per-attribute accuracy for drug name, dose, route, frequency, duration, indication
> - 🟡 **Medication Event Classification** (Summarisation / NLP) - classification of medication actions: start, stop, increase, decrease, continue
> - 🟡 **dm+d Medication Coding Accuracy** (Clinical Coding) - mapping to NHS dm+d terminology; currency against quarterly updates
> - 🔵 **Medication Error Rate Differential** (Patient Experience) - downstream outcome: pre/post AVT medication error rates

### TP.SN-19 🟡 Medication Attribute Extraction F1

Per-attribute accuracy for each component of a medication reference: drug name, dose, route, frequency, duration, indication, and start/stop dates. Each attribute is scored independently with its own F1. The medication as a whole is only fully correct if all attributes are correct - and aggregate medication accuracy masks systematic attribute-level failures (e.g. systems that get drug names right but frequencies wrong).

|Dimension              |Value                                                        |
|-----------------------|-------------------------------------------------------------|
| **Reference** | TP.SN-19 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                       |
|**Measurement Cadence**|Periodic audit                                               |
|**Pipeline Layer**     |Summarisation                                                |
|**Assurance Question** |Safety                                                       |
|**Measurement Method** |Computational                                                |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                               |
|**Responsible Actors** |Vendor                                                       |
|**Maturity**           |Established                                                  |
|**Outcome Type**       |Proximal                                                     |
|**Applicability**      |AVT-Contextualised                                           |
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

> 💡 Aggregate medication accuracy is a misleading single number. A system with 95% medication accuracy could be getting drug names right 99% of the time and doses right 92% of the time - and the 8% dose error rate is the safety-critical finding. Attribute-level breakdown is necessary for safety assurance.

### TP.SN-20 🟢 Uncertainty Marker Preservation

Does the summary maintain clinician diagnostic uncertainty ('possibly', 'suggestive of', 'consistent with', 'rule out', 'unlikely to be') rather than collapsing to definitive statements? Loss of uncertainty markers creates false certainty in the record.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-20 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
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

*See also: Hallucination Rate, Omission Rate, Confabulation Detection, Negation Handling Accuracy - all members of the Clinical Content Fidelity family. Certainty Inflation is the subtype most likely to cause diagnostic anchoring in downstream clinicians reading the note.*

---

### TP.SN-21 🟡 Medication Event Classification

Classification of medication *actions* discussed in a consultation: start, stop, increase, decrease, continue, hold, restart, allergy/contraindication. Distinct from medication attribute extraction, which captures what the medication is; event classification captures what is being *done* with it. A medication mentioned as "we'll stop this one" is not the same as "we'll keep this one" - the attributes may be identical but the clinical action is opposite.

|Dimension              |Value                                              |
|-----------------------|---------------------------------------------------|
| **Reference** | TP.SN-21 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                             |
|**Measurement Cadence**|Periodic audit                                     |
|**Pipeline Layer**     |Summarisation                                      |
|**Assurance Question** |Safety                                             |
|**Measurement Method** |Computational                                      |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                     |
|**Responsible Actors** |Vendor                                             |
|**Maturity**           |Established                                        |
|**Outcome Type**       |Proximal                                           |
|**Applicability**      |AVT-Contextualised                                 |
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

> 💡 The start↔stop confusion is the canonical AVT safety nightmare. A consultation discussion of "we're going to stop your warfarin and start apixaban instead" that is silently inverted by the summariser produces a note that documents starting warfarin and stopping apixaban - both incorrect, both dangerous, and neither flagged by attribute-level accuracy metrics. Event classification should be a mandatory safety gate.

### TP.SN-22 🔵 Style & Format Consistency

Does the system produce notes in the same structure each time? Inconsistency increases cognitive load for review and makes it harder for clinicians to develop efficient review patterns.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-22 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Human factors literature on documentation consistency |

**Why this tier?**

> Quality of life metric. Important for review efficiency but not safety-critical.

**Formal Definition**

```
Structural similarity across notes from the same template/configuration. Section presence consistency, ordering consistency, formatting consistency (bullet vs prose, headers, etc.). Report as variance metric across encounters.
```

**Limitations**

> Some legitimate variation is desirable - different consultations need different structures. Distinguishing legitimate variation from inappropriate inconsistency is judgement-based.

**Novel Thinking / Implications**

> 💡 Cognitive load research shows that consistent visual structure dramatically improves review efficiency. A note that always has 'History' followed by 'Examination' followed by 'Plan' allows clinicians to develop scanning patterns. A note that varies its structure forces re-orientation each time, increasing review time and reducing review quality.

---

### TP.SN-23 🔵 Length Appropriateness

Over-summarisation (losing detail) vs under-summarisation (verbatim transcript). Should be calibrated to consultation complexity - a 5-minute follow-up needs less than a 30-minute new patient assessment.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-23 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
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

> 💡 Over-summarisation is a quiet failure mode - the note looks clean but has lost necessary detail. Under-summarisation produces verbatim transcripts that defeat the purpose of AVT. Both can be detected statistically: a system that produces 200-word notes for both 5-minute and 30-minute consultations is not adapting appropriately.

---

---

### TP.SN-24 🟡 Stigmatising Language Replication Rate

Proportion of AI-generated notes that reproduce biased or stigmatising language patterns learned from training data. Distinct from the existing Cultural & Linguistic Appropriateness metric, which covers broader sensitivity issues. This metric specifically tracks whether the system has learned to generate language like "drug-seeking", "non-compliant", "frequent flyer", "difficult patient" - terms which research shows appear disproportionately in notes about specific patient populations.

|Dimension              |Value                                                                       |
|-----------------------|----------------------------------------------------------------------------|
| **Reference** | TP.SN-24 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                                      |
|**Measurement Cadence**|Periodic audit                                                              |
|**Pipeline Layer**     |Summarisation                                                               |
|**Assurance Question** |Fairness & Equity                                                           |
|**Measurement Method** |Computational                                                               |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                              |
|**Responsible Actors** |Vendor, Deployer                                                            |
|**Maturity**           |Proposed / Novel                                                            |
|**Outcome Type**       |Distal                                                                      |
|**Applicability**      |AVT-Contextualised                                                          |
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

### TP.CC-1 🟡 SNOMED Code Accuracy

AI-suggested code correctness. Precision, recall, and F1 reported separately for diagnosis, medication, procedure codes.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.CC-1 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Clinical Coding |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Day Zero Baseline, Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
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

### TP.CC-2 🟡 SNOMED CT Concept Mapping Accuracy

Accuracy of the mapping from extracted clinical entities in free-text to the correct SNOMED CT concept ID. Distinct from the existing SNOMED Code Accuracy metric, which measures whether the assigned code is clinically correct. Concept mapping measures whether the system correctly resolves "chest pain" to the correct SNOMED concept (29857009 - chest pain) rather than a near-miss concept (102588006 - chest discomfort). The boundary between correct and near-miss is where most mapping errors occur.

|Dimension              |Value                                                                    |
|-----------------------|-------------------------------------------------------------------------|
| **Reference** | TP.CC-2 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                                   |
|**Measurement Cadence**|Periodic audit                                                           |
|**Pipeline Layer**     |Clinical Coding                                                          |
|**Assurance Question** |Fidelity & Accuracy                                                      |
|**Measurement Method** |Computational                                                            |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                           |
|**Responsible Actors** |Vendor                                                                   |
|**Maturity**           |Established                                                              |
|**Outcome Type**       |Proximal                                                                 |
|**Applicability**      |AVT-Contextualised                                                       |
|**Source**             |NLP2FHIR pipeline literature; John Snow Labs FHIR-Ready AI; MedCAT benchmarks|

**Why this tier?**

> Vendor pre-deployment metric. Should be reported alongside SNOMED Code Accuracy. Essential for NHS interoperability as ambient scribes increasingly drive structured data entry.

**Formal Definition**

```
For each extracted clinical mention m: mapping function M(m) → SNOMED concept ID. Accuracy = |correctly_mapped| / |total_mentions|. Additional measures: (a) Exact Match Rate - mapped to exactly the reference concept; (b) Hierarchical Match Rate - mapped to an ancestor or descendant within 2 levels of reference; (c) Semantic Type Match Rate - mapped to correct semantic category. Report all three because acceptable mapping depth depends on context.
```

**Limitations**

> "Correct" mapping is context-dependent - sometimes a more general concept is preferable to an over-specific one. Ground truth annotation requires SNOMED expertise. NHS-specific subset mappings add complexity (not all SNOMED concepts are in the UK Edition).

**Novel Thinking / Implications**

> 💡 Concept mapping is where most structured data failures occur in ambient scribes. The surface text can look correct while the underlying code points to a subtly different concept. A clinician reviewing the free-text note won't notice that the coded entry resolves to "chest discomfort" rather than "chest pain" - but the downstream analytics, safety alerts, and QOF calculations will.

### TP.CC-3 🟡 ICD-10 / ICD-11 Full-Specificity Precision

Precision of ICD coding at maximum digit specificity, reported separately from category-level accuracy. Performance typically degrades sharply at full specificity compared to 3-character category level. The Hybrid-Code v2 framework reported 93% accuracy at 3-character level but only 82% at full specificity - the difference representing systematic specificity errors that aggregate metrics hide.

|Dimension              |Value                                       |
|-----------------------|--------------------------------------------|
| **Reference** | TP.CC-3 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                      |
|**Measurement Cadence**|Periodic audit                              |
|**Pipeline Layer**     |Clinical Coding                             |
|**Assurance Question** |Fidelity & Accuracy                         |
|**Measurement Method** |Computational                               |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit              |
|**Responsible Actors** |Vendor                                      |
|**Maturity**           |Emerging                                    |
|**Outcome Type**       |Proximal                                    |
|**Applicability**      |AVT-Contextualised                          |
|**Source**             |Hybrid-Code v2 (arXiv 2512.23743); WHO ICD-11 implementation guidance|

**Why this tier?**

> Vendor pre-deployment. Should be reported at multiple specificity levels (3-char, 4-char, full). Important for secondary care deployment and research data quality.

**Formal Definition**

```
Report precision at each specificity level independently: P_3char, P_4char, P_full. Specificity Degradation = P_3char - P_full. Values > 10 percentage points indicate the system systematically fails at high specificity. For ICD-11, which has more granular specificity than ICD-10, report per specificity depth.
```

**Limitations**

> Full-specificity coding requires clinical judgement that may exceed what is documented in the consultation. Some codes are legitimately unreachable from the source material - the consultation didn't contain enough information. Distinguishing unreachable codes from model errors requires careful reference construction.

**Novel Thinking / Implications**

> 💡 Over-specific coding is a form of clinical hallucination: the system generates specificity that wasn't present in the source. Under-specific coding is information loss. Both are quality issues, and they require different interventions. Reporting only aggregate accuracy conflates them.

### TP.CC-4 🟡 OPCS-4 Procedure Coding Accuracy

Accuracy of OPCS-4 procedure code assignment from consultation documentation. NHS-specific - the OPCS-4 classification (Office of Population Censuses and Surveys, 4th revision) is the mandatory procedure coding standard for NHS secondary care. **No published AI benchmarks currently exist for OPCS-4 coding** despite it being essential for NHS deployment.

|Dimension              |Value                                         |
|-----------------------|----------------------------------------------|
| **Reference** | TP.CC-4 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                        |
|**Measurement Cadence**|Periodic audit                                |
|**Pipeline Layer**     |Clinical Coding                               |
|**Assurance Question** |Fidelity & Accuracy                           |
|**Measurement Method** |Computational                                 |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                |
|**Responsible Actors** |Vendor                                        |
|**Maturity**           |Proposed / Novel                              |
|**Outcome Type**       |Proximal                                      |
|**Applicability**      |AVT-Contextualised                            |
|**Source**             |NHS Digital OPCS-4 coding standards; gap identified in published AVT literature|

**Why this tier?**

> Critical for NHS secondary care deployment. Should be a procurement requirement but cannot currently be assessed against published benchmarks - deployers must require vendor evidence on their specific cases.

**Formal Definition**

```
Precision, Recall, F1 at OPCS-4 code level. Specificity breakdown: chapter level (first character), category (first 2 characters), sub-category (3 characters), full code. Report per clinical chapter because procedure complexity varies dramatically (codes in Chapter V - Nervous System - are harder than Chapter W - Bones & Joints).
```

**Limitations**

> No public NHS-representative benchmark dataset for OPCS-4 coding exists. Vendors must construct their own evaluation, which creates comparability problems. Ground truth annotation requires specialist NHS coding expertise.

**Novel Thinking / Implications**

> 💡 The absence of any published OPCS-4 AI benchmark is itself a diagnostic finding about the state of the field. Ambient scribe vendors focused on the US market optimise for ICD-10 and CPT; NHS-specific standards are an afterthought. This is a strong argument for NHS England to commission a national OPCS-4 benchmark dataset as infrastructure investment - without it, NHS secondary care AVT deployment is operating without evidence.

### TP.CC-5 🟡 dm+d Medication Coding Accuracy

Accuracy of Dictionary of Medicines and Devices (dm+d) coding for medications discussed in consultations. NHS-specific - dm+d is the mandatory NHS medication terminology, maintained by NHS BSA, and essential for medication safety, interoperability, and prescribing workflows. **Like OPCS-4, no published AI benchmarks exist for dm+d coding**.

|Dimension              |Value                                                     |
|-----------------------|----------------------------------------------------------|
| **Reference** | TP.CC-5 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                    |
|**Measurement Cadence**|Periodic audit                                            |
|**Pipeline Layer**     |Clinical Coding                                           |
|**Assurance Question** |Safety                                                    |
|**Measurement Method** |Computational                                             |
|**Lifecycle Phases**   |Pre-deployment, Continuous                                |
|**Responsible Actors** |Vendor                                                    |
|**Maturity**           |Proposed / Novel                                          |
|**Outcome Type**       |Proximal                                                  |
|**Applicability**      |AVT-Contextualised                                        |
|**Source**             |NHS BSA dm+d standard; gap identified in published AVT literature|

**Why this tier?**

> Safety-critical for any AVT writing medication data back to the EPR. Should be a procurement requirement with vendor attestation. Monitoring required as dm+d is updated quarterly - a model trained against an old version will systematically fail on newer medications.

**Formal Definition**

```
Per medication mention: correct mapping to dm+d VMP (Virtual Medicinal Product), AMP (Actual Medicinal Product), VMPP (Virtual Medicinal Product Pack), or AMPP (Actual Medicinal Product Pack) depending on the level required by the EPR write-back. Currency Check: proportion of reference medications that exist in the current dm+d release. Drift = proportion of codes generated that no longer exist in the current dm+d release.
```

**Limitations**

> Mapping from spoken medication name to dm+d concept involves disambiguation (brand vs generic, different strengths, different formulations). Spoken names rarely contain enough specificity to uniquely identify a dm+d code without additional context.

**Novel Thinking / Implications**

> 💡 dm+d is updated quarterly. Any AVT system with a static model is by definition accumulating vocabulary drift against the current standard. A system trained two years ago has approximately eight releases of drift. Currency should be a contractual requirement - vendors should commit to a maximum acceptable drift against the live dm+d.

---

### TP.CC-6 🟢 Code Hallucination Rate

Rate at which the system generates codes that do not exist in the target code set. Distinct from all other coding error metrics because a non-existent code is not a "wrong" code - it is a structural error. The code looks valid syntactically but resolves to nothing. The Hybrid-Code v2 framework explicitly targeted "zero-hallucination coding" because this failure mode is both detectable and unambiguously wrong.

|Dimension              |Value                                                |
|-----------------------|-----------------------------------------------------|
| **Reference** | TP.CC-6 |
|**Priority Tier**      |🟢 Tier 1 - Minimum Viable                            |
|**Measurement Cadence**|Continuous                                           |
|**Pipeline Layer**     |Clinical Coding                                      |
|**Assurance Question** |Safety                                               |
|**Measurement Method** |Computational                                        |
|**Lifecycle Phases**   |Pre-deployment, Continuous                           |
|**Responsible Actors** |Vendor, Deployer                                     |
|**Maturity**           |Emerging                                             |
|**Outcome Type**       |Proximal                                             |
|**Applicability**      |AVT-Contextualised                                   |
|**Source**             |Hybrid-Code v2 (arXiv 2512.23743) - neuro-symbolic verification approach|

**Why this tier?**

> Architecturally preventable failure mode - there is no reason a production system should generate non-existent codes. Should be a hard zero-tolerance metric validated pre-deployment and monitored continuously. Automated detection is trivial (lookup against the code set).

**Formal Definition**

```
Code Hallucination Rate = |generated_codes_not_in_target_code_set| / |total_generated_codes|. Target: 0.0. Any non-zero value indicates architectural failure - the system should be constrained to generate only valid codes via lookup or constrained decoding. Report per code set (SNOMED, ICD, OPCS-4, dm+d) because constraint enforcement may vary.
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

> Requires current version of the target code set for lookup. Code set updates may temporarily create false positives (newly valid codes that haven't propagated). Does not detect codes that exist but are clinically wrong - that's captured by SNOMED Code Accuracy.

**Novel Thinking / Implications**

> 💡 This is a zero-tolerance metric. A non-existent code in a clinical record is a data quality failure that breaks downstream systems. The correct architectural response is constrained generation - the system should be structurally unable to produce a code outside the target code set. Any vendor reporting a non-zero hallucination rate is implicitly admitting that their generation is unconstrained, which is a procurement red flag.

### TP.CC-7 🟡 Coding Inflation Detection

Systematic upcoding monitoring via SPC. In NHS, primary risk is data quality corruption of epidemiological data, QOF, and population health.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.CC-7 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Clinical Coding |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Regional (ICB), National Body |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
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

### TP.CC-8 🟡 E/M Level Shift Monitoring

Monitoring of shifts in Evaluation & Management (E/M) coding levels pre- and post-AVT deployment. In US settings, E/M level shift has been a primary revenue impact channel; in NHS settings, the equivalent concern is SNOMED specificity shift and its effect on QOF, Hospital Episode Statistics, and population health analytics. Extension of the existing Coding Inflation Detection metric with a specific focus on tariff-relevant code distributions.

|Dimension              |Value                                                                                |
|-----------------------|-------------------------------------------------------------------------------------|
| **Reference** | TP.CC-8 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                                               |
|**Measurement Cadence**|Continuous                                                                           |
|**Pipeline Layer**     |Clinical Coding                                                                      |
|**Assurance Question** |Safety                                                                               |
|**Measurement Method** |Computational                                                                        |
|**Lifecycle Phases**   |Day Zero Baseline, Continuous                                                        |
|**Responsible Actors** |Regional (ICB), National Body                                                        |
|**Maturity**           |Emerging                                                                             |
|**Outcome Type**       |Distal                                                                               |
|**Applicability**      |AVT-Contextualised                                                                   |
|**Source**             |npj Digital Medicine policy brief (Nature s41746-025-02272-z) - documented 3.0→4.1 diagnoses/encounter post-AVT|

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

### TP.CC-9 🟡 Coding Equity Index

Whether AVT-driven changes in coding distribution are equitably spread across patient demographics or systematically benefit some populations more than others. If AVT improves coding completeness more for majority populations than for minority populations, it widens existing inequalities in data quality and downstream resource allocation.

|Dimension              |Value                                                 |
|-----------------------|------------------------------------------------------|
| **Reference** | TP.CC-9 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                |
|**Measurement Cadence**|Periodic audit                                        |
|**Pipeline Layer**     |Clinical Coding                                       |
|**Assurance Question** |Fairness & Equity                                     |
|**Measurement Method** |Computational                                         |
|**Lifecycle Phases**   |Periodic Audit                                        |
|**Responsible Actors** |Regional (ICB), National Body                         |
|**Maturity**           |Proposed / Novel                                      |
|**Outcome Type**       |Distal                                                |
|**Applicability**      |AVT-Contextualised                                    |
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

> 💡 If AVT makes the documented patient population look healthier for some demographics and more accurately unwell for others, the resource allocation implications compound existing health inequalities. This is an equity dimension that the existing taxonomy's fairness metrics don't capture - they focus on AVT accuracy across demographics, not on AVT's effect on the resulting data about those demographics.

### TP.CC-10 🔵 wRVU / Tariff Impact Attribution

Attribution of workload or tariff-relevant coding changes to AVT specifically, separated from concurrent changes (training, policy updates, case mix shifts). Quasi-experimental methodology required. In NHS context, applies to PbR tariffs, QOF achievement, and secondary care activity-based funding.

|Dimension              |Value                                        |
|-----------------------|---------------------------------------------|
| **Reference** | TP.CC-10 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research               |
|**Measurement Cadence**|Periodic audit                               |
|**Pipeline Layer**     |Clinical Coding                              |
|**Assurance Question** |Meta-evaluation                              |
|**Measurement Method** |Hybrid                                       |
|**Lifecycle Phases**   |Periodic Audit                               |
|**Responsible Actors** |Regional (ICB), National Body, Academic     |
|**Maturity**           |Proposed / Novel                             |
|**Outcome Type**       |Distal                                       |
|**Applicability**      |AVT-Contextualised                           |
|**Source**             |Extends E/M Level Shift Monitoring with causal attribution methodology|

**Why this tier?**

> Research-grade metric requiring quasi-experimental design. National or academic responsibility. Not routinely measurable at deployer level.

**Formal Definition**

```
Using difference-in-differences or synthetic control methodology: compare coding/tariff trajectories of AVT-adopting practices against matched non-adopting practices over the same period. Attribution Coefficient = (ΔAVT - ΔControl) / ΔControl. Positive values indicate AVT-driven shift; magnitude indicates size of effect. Confidence intervals essential given small sample sizes in practice-level comparisons.
```

**Limitations**

> Practice selection into AVT is not random - early adopters may differ systematically from non-adopters. Matching methodology is contested. Small sample sizes at practice level undermine statistical power.

**Novel Thinking / Implications**

> 💡 This is the metric that answers the governance question: is AVT making the coded data more accurate or more inflated? Without this attribution, every observed coding shift is ambiguous. National evaluation programmes are the only plausible venue for doing this properly - individual deployers cannot.

### TP.CC-11 🔵 Code Specificity Index

Whether suggested codes are at appropriate hierarchy level. SNOMED has multiple specificity levels for the same concept; AI may default to over-general (loses detail) or over-specific (introduces false precision) codes inappropriately.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.CC-11 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Clinical Coding |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
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

> 💡 Over-specific coding is the more insidious problem: AI may code 'chest pain' as 'precordial chest pain' when the patient simply said 'pain in my chest'. The over-specific code carries information that wasn't in the source - a form of coded hallucination. Under-specific coding loses information but is more obviously a quality issue.

---

### TP.CC-12 🔵 Code Suggestion Latency

Time from note generation to code suggestion availability. Affects coding workflow integration - if coding suggestions arrive too late, clinicians have moved on to the next patient and won't engage with them.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.CC-12 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Clinical Coding |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
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

### TP.WB-1 🟢 Write-back Fidelity

Data transfer accuracy to EPR structured fields. Where errors become patient safety events - hallucinated allergy in allergy field propagates to all future decisions.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.WB-1 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | EPR Write-back |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Critical gap - no standardised FHIR R4 write-back in NHS primary care |

**Why this tier?**

> Highest-priority pre-deployment gate. A hallucinated allergy written to the EPR allergy field is a system-level safety failure that propagates to every future clinical decision. Must test per EPR system before go-live.

**Formal Definition**

```
Fidelity(d,f) = 1 if content correct AND target field correct. Report per category: (a) free-text, (b) coded diagnoses, (c) medications, (d) allergies, (e) problem list. Categories c-e are safety-critical.
```

**Reference Standard**

> Pre-defined gold-standard test corpus per target EPR (EMIS, SystmOne, Epic, others as applicable). Each test case specifies: source AVT output (transcript + summary), expected target EPR field, expected content semantically equivalent to a clinician-authored entry. "Content correct" decomposes into:
>
> - **Structural equivalence** - the value lands in the field of the correct datatype (string, coded value, numeric, date) with correct units where applicable
> - **Semantic equivalence** - the value preserves clinical meaning. For coded categories (c-e) semantic equivalence requires preservation of the coded concept (e.g. SNOMED CT identifier match, not just string match); for free text (a) it requires preservation of every clinically relevant proposition per the [TP.SN-6 Omission Rate](#tp-sn-6) reference standard
> - **No content addition** - the value introduces no information absent from the AVT output. Hallucinated content reaching a structured field counts as a write-back failure even where the same content in free text would be a TP.SN-5 hallucination
>
> Inter-rater target on test-case construction: ICC ≥ 0.85 (write-back fidelity is a more constrained task than free-text fidelity; higher reliability expected).

**Operational Specification**

> - **Test corpus MANDATORY:** ≥ 200 test cases per target EPR system, balanced across the five categories with safety-critical categories (medications / allergies / problem-list) over-represented (≥ 40 cases each).
> - **Pre-deployment gate per EPR:** fidelity tested against every EPR system in scope at the deployment site. A vendor-asserted "EMIS-compatible" claim does not transfer to SystmOne without re-test.
> - **Population for continuous monitoring:** sampled production write-backs reviewed against a clinician-authored gold standard at a frequency proportional to write-back volume (minimum monthly audit; weekly for high-volume deployments).
> - **Per-category reporting MANDATORY:** report fidelity by category (a)-(e) with safety-critical categories reported separately. Aggregate-only reporting hides the failure modes that matter most.
> - **Failure-mode classification MANDATORY:** every failure classified as (i) wrong field, (ii) correct field, wrong content (omission), (iii) correct field, wrong content (addition / hallucination), (iv) structural mismatch (e.g. coded concept missing, unit error). Type (iii) on safety-critical fields is a critical incident regardless of frequency.

**Threshold Guidance**

> ⚠️ **Provenance:** the zero-tolerance posture on type-(iii) failures into safety-critical fields follows from the clinical-safety logic in the Why-this-tier and Novel Thinking sections (a hallucinated allergy in an allergy field is a system-level safety failure). Specific numbers (100 % safety-critical gate, ≥ 95 % free-text gate, ≥ 99 % monthly audit floor, ≥ 200 cases per EPR) are **proposed in v3.3 as starting points**, not externally validated. Indicative; require local calibration before contractual use.
>
> - **Pre-deployment gate (per EPR):** safety-critical category fidelity = 100 % on the test corpus; free-text fidelity ≥ 95 %; zero type-(iii) failures on any safety-critical field.
> - **Continuous monitoring:** monthly audited fidelity ≥ 99 % on safety-critical categories; alert on any type-(iii) failure detected in production traffic (no rate threshold - single instance is alert-worthy).
> - **Pause trigger:** any type-(iii) failure on allergy or medication-dose fields confirmed in production; or aggregate safety-critical fidelity < 95 % in any monthly audit cycle.

**References**

- **IM1**: NHS IM1 interface assurance

**Limitations**

> Integration-specific: must test per EPR (EMIS, SystmOne, Epic). The Operational Specification scope ("≥200 cases per EPR with safety-critical over-representation") makes the testing burden visible; it does not reduce it. A multi-EPR vendor claim translates to a multi-EPR test programme.

**Novel Thinking / Implications**

> 💡 Highest-priority pre-deployment gate. Hallucination in free text is bad; hallucinated allergy in allergy field is system-level safety failure. The structured Reference Standard / Operational Specification / Threshold Guidance pattern above promotes the existing severity intuition into an operational gate: type-(iii) failures on safety-critical fields are not measured as a rate to be optimised; they are measured as binary defects that must not occur.

---

### TP.WB-2 🟢 Integration Error Rate

AVT-to-EPR pipeline failures: failed writes, partial writes, timeouts, truncation.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.WB-2 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | EPR Write-back |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
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

### TP.WB-3 🟢 Field Mapping Accuracy

Does content land in the correct EPR field even when content is correct? A correctly transcribed allergy written to the free-text consultation field rather than the allergies field is a system failure with safety implications - the allergy won't trigger drug interaction checks.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.WB-3 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | EPR Write-back |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
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

> 💡 This is distinct from write-back fidelity. Fidelity asks 'is the content correct?' Field mapping asks 'is it in the right place?' Both can fail independently. An allergy correctly transcribed but written to the consultation note rather than the allergy list is a silent failure - the content is technically present but won't trigger downstream safety checks like drug interaction warnings.

---

### TP.WB-4 🟢 Update vs Append Behaviour

Does the system correctly handle existing structured data? Overwriting an existing allergy list vs appending to it has different safety implications. Overwriting can erase critical historical information; inappropriate appending can create duplicates and inconsistencies.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.WB-4 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | EPR Write-back |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
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

> 💡 The classic failure: AVT writes 'allergies: penicillin' to a patient who already has 'penicillin, sulpha, aspirin' in their allergy list. If the system overwrites, the patient loses two allergies from their record - a direct patient safety event. Pre-deployment testing must include scenarios with existing structured data, not just clean-slate consultations.

---

### TP.WB-5 🟡 Write-back Rollback Capability

When errors are detected, can the write-back be reversed cleanly? Particularly important for coded data that triggers downstream processes (alerts, prescribing rules, audit trails).

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.WB-5 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | EPR Write-back |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
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

### TP.WB-6 🟡 FHIR R4 Resource Conformance Rate

Validated conformance of generated structured data against FHIR R4 profiles. FHIR is increasingly the interoperability standard for NHS EPRs; systems that produce technically parseable but profile-non-conformant resources create silent integration failures downstream. The ADS/Harvard SPIE 2025 study reported 95% data field retention via FHIR vs ~70% for legacy formats - but retention is not the same as profile conformance.

|Dimension              |Value                                    |
|-----------------------|-----------------------------------------|
| **Reference** | TP.WB-6 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                   |
|**Measurement Cadence**|Continuous                               |
|**Pipeline Layer**     |EPR Write-back                           |
|**Assurance Question** |Fidelity & Accuracy                      |
|**Measurement Method** |Computational                            |
|**Lifecycle Phases**   |Pre-deployment, Continuous               |
|**Responsible Actors** |Vendor                                   |
|**Maturity**           |Established                              |
|**Outcome Type**       |Proximal                                 |
|**Applicability**      |AVT-Contextualised                       |
|**Source**             |FHIR R4 validation tooling; SPIE 14009E 2025 interoperability study|

**Why this tier?**

> Established methodology with open-source validators. Vendor pre-deployment requirement. Should be reported per FHIR profile used (UK Core, INTEROPen, local).

**Formal Definition**

```
For each generated FHIR resource: validate against the applicable profile using the official HL7 FHIR validator. Conformance Rate = |resources_passing_validation| / |total_resources|. Stratify by resource type (Condition, MedicationStatement, AllergyIntolerance, Observation) - failures often cluster in specific resource types. Target: 100% on safety-critical resource types.
```

**Limitations**

> Conformance to a profile does not guarantee clinical correctness - a valid but wrong medication code passes validation. Profile requirements may be under-specified for some NHS use cases.

**Novel Thinking / Implications**

> 💡 Profile conformance is a necessary but not sufficient condition for interoperability. The existing Write-back Fidelity metric measures whether content is correct; this metric measures whether the structural container is valid. Both can fail independently. A system that produces valid-but-wrong FHIR is dangerous; a system that produces right-but-invalid FHIR will fail to write-back silently.

---

### TP.WB-7 🔵 openEHR Archetype Conformance

Conformance of generated clinical data against openEHR archetypes for NHS trusts using openEHR-based EPR platforms. Less widespread than FHIR in UK primary care but relevant for specific secondary care deployments (particularly in mental health trusts and specialised services).

|Dimension              |Value                                     |
|-----------------------|------------------------------------------|
| **Reference** | TP.WB-7 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research            |
|**Measurement Cadence**|Continuous                                |
|**Pipeline Layer**     |EPR Write-back                            |
|**Assurance Question** |Fidelity & Accuracy                       |
|**Measurement Method** |Computational                             |
|**Lifecycle Phases**   |Pre-deployment, Continuous                |
|**Responsible Actors** |Vendor                                    |
|**Maturity**           |Established                               |
|**Outcome Type**       |Proximal                                  |
|**Applicability**      |AVT-Contextualised                        |
|**Source**             |openEHR Foundation standards; Clinical Knowledge Manager archetype library|

**Why this tier?**

> Deployment context-specific. Tier 3 for most deployers but Tier 2 or even Tier 1 for trusts using openEHR-based platforms - context adjustment per the "Adapting to Local Context" section.

**Formal Definition**

```
For each generated composition: validate against the applicable openEHR archetype(s) and template(s). Report: archetype conformance rate (structural), terminology binding conformance (codes map to required terminology subset), cardinality compliance. Must validate both the composition structure and the path-based data bindings.
```

**Limitations**

> openEHR archetype validation tooling is less mature than FHIR validation. Archetype maintenance varies by trust. Cross-trust conformance may require different archetype versions.

**Novel Thinking / Implications**

> 💡 The UK has bifurcated EPR infrastructure: primary care is standardising on FHIR-based interoperability, while parts of secondary care (particularly the Code4Health-aligned trusts) have significant openEHR investment. AVT vendors focused on primary care may simply not support openEHR, making them structurally unsuitable for some secondary care deployments. This should be a procurement question rather than a post-contract discovery.

### PI.PP-1 🔵 Speaker-Attributed Transcript Accuracy

Combined ASR + diarisation: was the right text assigned to the right person? Neither WER nor DER alone captures this - a transcript can have low WER and low DER but still misattribute a critical utterance.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.PP-1 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR + Diarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Identified as compound metric gap - neither WER nor DER alone captures this |

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

### PI.PP-2 🟡 Multi-Party Conversation Robustness

Combined ASR + diarisation degradation when >2 speakers present: interpreter, family member, student, MDT. Most benchmarks assume dyadic (2-speaker) encounters.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.PP-2 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR + Diarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Identified in NHS consultation pattern analysis - interpreter-mediated, family-present, and MDT consultations are common |

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

### PI.PP-3 🔵 Information Extraction Yield

Spans ASR + summarisation: what proportion of clinically relevant content in source audio survives through transcription AND into the generated note? Captures the combined loss from ASR errors and summarisation omissions.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.PP-3 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | ASR + Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Identified as structural gap - component metrics don't capture cross-stage information loss |

**Why this tier?**

> Requires expert annotation of source audio - expensive. Best suited for national evaluation programme or academic pilot.

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

> 💡 The key insight: summarisation can sometimes compensate for ASR errors (inferring the right drug from context), or it can amplify them (hallucinating a plausible but wrong drug to fill the gap). IEY captures both - the net yield is what matters clinically.

---

### PI.PP-4 🔵 Noise-to-Note Resilience

Spans ASR + summarisation: how gracefully does the final note quality degrade as audio quality worsens? Tests whether the summarisation layer can compensate for degraded transcription.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.PP-4 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR + Summarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Proposed for pre-deployment testing - NHS clinical environments have variable acoustics |

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

### PI.PP-5 🔵 Epistemic Status Preservation

Spans diarisation + summarisation: does the note correctly distinguish what was reported by the patient vs observed by the clinician vs inferred by the AI? 'Patient reports headache' vs 'headache noted' vs 'headache' have different clinical meanings.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.PP-5 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Diarisation + Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
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

> Epistemic status annotation requires clinical expertise. Automated classification via markers is crude - many assertions lack explicit markers.

**Novel Thinking / Implications**

> 💡 This is clinically significant: 'patient reports chest pain' documents subjective experience; 'chest pain' in the note without qualification implies objective finding. If diarisation misattributes patient speech to clinician, the summariser may strip the 'reports' qualifier, silently changing the epistemic status. This compounds two different error types into a clinical safety risk invisible to either WER or hallucination rate.

---

### PI.PP-6 🔵 Diarisation-Stratified WER

WER computed separately for each speaker after diarisation. Captures the compound effect of diarisation errors on per-speaker accuracy measurement. A speaker whose utterances are frequently misattributed will have artificially inflated WER even if the underlying ASR is accurate.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.PP-6 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR + Diarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
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

### PI.PP-7 🟡 Concept Extraction Concordance

Spans summarisation + coding: do the SNOMED codes match the clinical concepts in the free-text note? An internal consistency check that doesn't need source audio - the note and its codes should agree.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.PP-7 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation + Coding |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Proposed as automated internal consistency check - no ground truth needed |

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

> 💡 This is uniquely valuable because it requires no ground truth - it's a self-consistency check that can run on every encounter. An orphan code (coded but not mentioned in text) is a strong signal for hallucinated coding. A missing code (mentioned but not coded) is a completeness gap. Both can be detected without human review.

---

### PI.PP-8 🔵 End-of-Utterance Timing Accuracy

Whether the system correctly identifies where an utterance ends. Affects both diarisation (turn boundaries) and summarisation (sentence boundaries). Misalignment causes content fragmentation across utterances or merging of distinct utterances.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.PP-8 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR + Diarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Standard speech processing metric |

**Why this tier?**

> Vendor research metric. Affects multiple downstream stages.

**Formal Definition**

```
EOU Timing Error = mean temporal error (ms) between predicted and actual utterance boundaries. Different from speaker boundary precision - EOU timing is within-speaker pauses that should/shouldn't be treated as utterance breaks.
```

**Limitations**

> Defining 'correct' utterance boundaries is itself contested. Conversational speech doesn't always have clean utterance breaks.

**Novel Thinking / Implications**

> 💡 EOU errors propagate: a missed boundary causes two utterances to merge, which then have to be diarised as one (potentially with conflicting speakers) and summarised as one (potentially conflating two clinical concepts).

---

### PI.PP-9 🟡 Structured/Free-Text Consistency

Spans summarisation + write-back: does the coded allergy entry agree with allergies mentioned in the free-text note? Does the medication list match medications discussed in the narrative?

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.PP-9 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation + Write-back |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Identified as post-write-back automated safety check |

**Why this tier?**

> Automated post-write-back guardrail requiring no ground truth. If structured allergy field disagrees with narrative text, something has gone wrong. Deployer-implementable.

**Formal Definition**

```
For each structured field category f ∈ {allergies, medications, diagnoses}: Consistency(f) = |items_in_structured(f) ∩ items_in_freetext| / |items_in_structured(f) ∪ items_in_freetext|. Inconsistencies: (a) in structured but not free text - unexplained entries; (b) in free text but not structured - missed structuring.
```

**Limitations**

> Requires NER capable of matching free-text mentions to structured field entries. Partial mentions (e.g. 'penicillin allergy' in text vs SNOMED allergy code) need fuzzy matching.

**Novel Thinking / Implications**

> 💡 This is a post-write-back guardrail that can run automatically. If the allergy field says 'penicillin' but the note never mentions penicillin, something has gone wrong - either the note omitted it (summarisation failure) or the structured entry is hallucinated (coding/write-back failure). Either way, it needs review.

---

### PI.E2E-1 🔵 Source-to-Record Concordance

End-to-end: comparing original consultation audio directly against the final EPR entry, bypassing all intermediate representations. This is what actually matters for patient safety.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.E2E-1 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | Proposed as the ultimate AVT safety metric - captures cumulative pipeline effect |

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

> 💡 This is the metric the entire field should be targeting but almost nobody measures. Every other metric is a proxy for this one. VeriFact gets close by checking against existing EHR, but source-to-record concordance checks against what was actually said - a fundamentally stronger test. A national benchmark programme could fund periodic SRC audits as the definitive AVT safety assessment.

---

### PI.E2E-2 🔵 Cumulative Information Yield

The positive framing of source-to-record concordance: what proportion of the clinical information present in the source audio successfully survives the entire pipeline and appears in the final EPR record. Where Source-to-Record Concordance measures preservation rate (how much was preserved), Cumulative Information Yield measures the distributional yield across clinical categories - so it exposes systematic category bias (e.g. a system that yields 95% on medications but 60% on psychosocial content).

|Dimension              |Value                                                                            |
|-----------------------|---------------------------------------------------------------------------------|
| **Reference** | PI.E2E-2 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research                                                   |
|**Measurement Cadence**|Periodic audit                                                                   |
|**Pipeline Layer**     |End-to-End                                                                       |
|**Assurance Question** |Safety                                                                           |
|**Measurement Method** |Hybrid                                                                           |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                                   |
|**Responsible Actors** |Academic, National Body                                                          |
|**Maturity**           |Proposed / Novel                                                                 |
|**Outcome Type**       |Distal                                                                           |
|**Applicability**      |AVT-Contextualised                                                               |
|**Source**             |Extension of existing Source-to-Record Concordance with categorical yield decomposition|

**Why this tier?**

> Resource-intensive evaluation requiring expert annotation of source audio, organised into categorical yield rather than binary preservation. Best suited for national evaluation programme. Per-category reporting reveals systematic content bias invisible to aggregate preservation metrics.

**Formal Definition**

```
For each clinical category c ∈ C = {medications, allergies, diagnoses, symptoms, plan, safety_netting, social_context, psychosocial, red_flags}: Yield(c) = |items_in_c_present_in_record| / |items_in_c_in_source|. Composite: Yield_weighted = Σ w_c × Yield(c), where w_c are clinical importance weights. Report per-category breakdown alongside composite - the aggregate obscures category bias.
```

**Limitations**

> Categorical annotation of source audio is even more labour-intensive than binary annotation. Category boundaries are contested (is "stopped smoking 5 years ago" social context or relevant history?). Weight assignment for the composite is subjective.

**Novel Thinking / Implications**

> 💡 The most common finding in ambient scribe evaluation is systematic yield bias toward clinical content the model recognises as "medical" (medications, symptoms, diagnoses) and away from content it treats as peripheral (social context, psychosocial factors, patient concerns that don't map to a code). This bias is invisible to concordance metrics that treat all clinical items equally - but it has direct consequences for patient-centred care and safeguarding. Per-category yield reporting makes the bias visible and actionable.

### PI.E2E-3 🔵 Error Propagation / Cascade Analysis

End-to-end: tracking how a single upstream error amplifies or gets corrected through subsequent stages. An ASR misrecognition could be caught by the summariser (correction) or cascade into wrong coding and wrong EPR entry (amplification).

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.E2E-3 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Proposed - analogous to fault propagation analysis in safety engineering |

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

### PI.E2E-4 🟡 Safety-Critical Information Chain of Custody

End-to-end per-item trace for highest-risk content: did this specific allergy survive ASR → diarisation → summarisation → coding → EPR field? A per-item trace, not a statistical rate.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.E2E-4 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | Proposed - analogous to chain-of-custody in evidence management and traceability in safety-critical systems |

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

> Requires access to intermediate outputs (transcript, diarised transcript, summary, codes) - most vendors expose only the final note. Per-item tracing is manual without automation.

**Novel Thinking / Implications**

> 💡 This is the audit methodology that a CSO should be able to perform. Pick 10 safety-critical items from a sample of consultations and trace each through the pipeline. If any chain breaks, you know exactly where the system fails. This should be a Day Zero acceptance test and a quarterly audit procedure.

---

### PI.E2E-5 🔵 Compound Demographic Performance

End-to-end: demographic performance gap measured at the final output, not just at ASR. ASR bias against an accent might be corrected by summarisation (context inference) or amplified (hallucination to fill gaps).

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.E2E-5 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, National Body |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | Proposed - extends demographic-disaggregated WER to end-to-end measurement |

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

### PI.E2E-6 🔵 Semantic Drift Accumulation

End-to-end: measuring cumulative meaning transformation across stages. Each stage subtly transforms meaning - 'occasional chest tightness on stairs' → 'chest pain on exertion'. Each individual transformation may be defensible; the cumulative drift may not be.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.E2E-6 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Proposed - inspired by signal processing concept of cumulative distortion |

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

> 💡 Not all drift is bad - 'occasional tightness going upstairs' → 'exertional chest pain' is appropriate medical abstraction. The question is whether the drift preserves clinical decision-relevance. A clinically-aware drift metric would weight drift on safety-critical elements higher than drift on contextual description.

---

### PI.E2E-7 🟡 Pipeline Non-Determinism / Reproducibility

End-to-end: if you re-process the same audio, do you get the same output? Each stochastic component introduces variance. Compound variance could mean the same consultation produces materially different notes on different runs.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.E2E-7 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Proposed - standard practice in safety-critical software testing but not yet applied to AVT pipelines |

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

### PI.E2E-8 🔵 Error Attribution Analysis

End-to-end: when an error appears in the final output, which stage introduced it? Essential for improvement but requires intermediate output logging most vendors don't expose.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.E2E-8 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Proposed - analogous to root cause analysis in incident investigation |

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

### PI.E2E-9 🔵 Clinical Decision Equivalence

End-to-end: does the final note support the same clinical decisions a clinician present at the consultation would make? The ultimate distal outcome metric connecting documentation to patient safety.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.E2E-9 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Academic, National Body |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | Proposed - the ultimate validity test for clinical documentation |

**Why this tier?**

> Gold-standard distal outcome metric. Extremely resource-intensive (blinded clinician decision comparison). National research programme candidate.

**Formal Definition**

```
Present note to blinded clinician(s). Clinician makes clinical decisions (diagnosis, plan, prescribing) based solely on note. Compare with decisions of clinician who observed original consultation. Equivalence = |decisions_matching| / |total_decisions|. Per category: diagnostic, therapeutic, safety-netting, follow-up.
```

**Limitations**

> Extremely resource-intensive: requires blinded clinical decision-making from multiple clinicians. Inter-clinician variation in decision-making adds noise. Simulated decisions may not reflect real-world behaviour.

**⚠️ Underspecification Warning (Tier B - conceptually essential, operationally impractical)**

> Clinical Decision Equivalence is conceptually the most important metric in the taxonomy for distal outcome validation - it directly tests whether AVT-generated notes support the same clinical decisions as direct observation, which is what AVT ultimately needs to do to be safe. But measurement methodology is extremely resource-intensive: blinded clinical decision-making from multiple clinicians per case, inter-clinician variation adding noise, simulated decision contexts differing from real-world behaviour under time pressure. No validated protocol exists. No threshold for "adequate equivalence" has been established. Best interpreted as a target for national or academic evaluation programmes rather than deployer-level assessment. When operationalised, the study design must specify: (a) number of clinicians per case and selection criteria; (b) blinding methodology and how information leakage is prevented; (c) decision categories assessed (diagnostic, therapeutic, safety-netting, follow-up); (d) agreement metric (kappa, per-category accuracy, weighted agreement); (e) clinical complexity stratification; (f) handling of inter-clinician disagreement in the ground-truth condition.

**Novel Thinking / Implications**

> 💡 This is the metric that closes the proximal-distal gap. If a note produced by AVT leads to the same clinical decisions as direct observation, the documentation is functionally safe regardless of WER, ROUGE, or any other proxy metric. This should be the gold-standard validation for any AVT claiming clinical deployment readiness.

---

### PI.E2E-10 🟡 Full-Pipeline Latency Budget

End-to-end: total time from consultation end to note availability in EPR, broken down by stage. Not just ASR RTF - the full wait before a clinician can review.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.E2E-10 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Proposed as operational metric - RTF alone doesn't capture full workflow impact |

**Why this tier?**

> Operational metric deployers can measure: time from consultation end to note availability. Directly affects review quality - if note arrives after next patient, review suffers.

**Formal Definition**

```
L_total = Σ L_stage for stages ∈ {ASR, diarisation, summarisation, coding, write-back, EPR rendering}. Report: L_total distribution (P50, P95, P99). Per-stage breakdown identifies bottlenecks. Clinical constraint: L_total should be < time between consultations.
```

**Limitations**

> End-to-end latency depends on infrastructure (network, cloud processing, EPR API speed) not just AI model performance.

**Novel Thinking / Implications**

> 💡 If the note isn't available before the next patient arrives, the clinician either reviews it later (losing context) or doesn't review it at all (rubber-stamping). Latency directly affects the quality of human oversight. The pipeline latency budget should be a deployment acceptance criterion.

---

### PI.E2E-11 🟡 Pipeline Failure Recovery

When one stage fails (e.g. diarisation crashes), what does the system produce? Graceful degradation vs catastrophic failure. Most metrics assume the pipeline runs to completion - but partial failures are common in production.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.E2E-11 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
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

> 💡 The dangerous failure mode is silent degradation: the pipeline produces output that looks normal but is built on a failed component. A diarisation failure could cause all speech to be attributed to the clinician - producing a confident-looking note with completely wrong attribution. The clinician reviewing the note has no signal that anything went wrong. Pre-deployment testing must include controlled failure injection.

---

### PI.E2E-12 🔵 Round-Trip Information Loss

If the AVT-generated note were used to reconstruct the original consultation, how much would be lost? An information-theoretic complement to source-to-record concordance - measures total information preserved through the pipeline.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.E2E-12 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Specific |
| **Source** | Information theory applied to clinical documentation |

**Why this tier?**

> Research metric. Theoretically interesting but not operationally measurable at scale.

**Formal Definition**

```
Round-Trip Loss = 1 - I(audio; note) / H(audio), where I is mutual information and H is entropy. In practice: have a clinician attempt to answer specific questions about the consultation using only the note vs the full audio; compare answer accuracy.
```

**Limitations**

> Theoretical metric; practical measurement is approximate. Information loss is not always bad - appropriate medical abstraction is loss in the technical sense.

**Novel Thinking / Implications**

> 💡 Different from source-to-record concordance because it asks about all information, not just clinical items. Includes contextual information that may matter for safeguarding, family dynamics, patient understanding - content that AVT systems systematically strip but that clinicians sometimes rely on.

---

### HL.HF-1 🟢 Edit Rate (% Notes Edited)

Percentage of AI notes edited before approval. At Day Zero: quality signal. Declining trajectory: primary complacency indicator.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-1 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Day Zero Baseline, Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Abridge; NAS; Stanford framework |

**Why this tier?**

> Primary continuous complacency indicator. Deployer-measurable from EPR workflow data. NAS Day Zero SPI. The single most important human factors metric - trajectory reveals automation bias before incidents occur.

**Formal Definition**

```
ER(t) = |N_edited(t)| / |N_total(t)|. Complacency signal: dER/dt < 0 sustained ≥4 weeks without AI accuracy improvement. Alert: ER drops >15pp from baseline within 3 months.
```

**Reference Standard**

> EPR or AVT-product telemetry capturing the post-generation, pre-signature note-state diff. An "edit" is any change to the AI-generated text between AI output and clinician signature. Out of scope: changes after signature (correction workflows are tracked under [GV.SG-15 Time-to-Correct](#gv-sg-15), not Edit Rate). Edit detection MUST distinguish:
>
> - **Substantive edits** - additions, deletions, or modifications that alter clinical meaning (default count for ER)
> - **Stylistic edits** - formatting, punctuation, casing, whitespace (reported separately, not counted in headline ER)
>
> Where the diff cannot reliably classify substantive vs stylistic, count as substantive. The classification rule MUST be documented and held constant across the deployment; vendors changing the rule must declare a baseline reset (see Operational Specification).

**Operational Specification**

> - **Window:** weekly aggregate per clinician and per deployment site. Continuous monitoring (the Cadence above); weekly granularity is the floor for trajectory analysis.
> - **Population:** all AI-generated notes signed by the clinician during the window. Exclude notes where the clinician aborted the AI workflow before signature (these belong under [HL.HF-9 Re-record / Abandonment Rate](#hl-hf-9)).
> - **Baseline establishment MANDATORY:** the deployment baseline is the mean weekly ER across the first 4 weeks of clinician live use, computed per clinician (not pooled). All complacency-alert calculations are referenced to this per-clinician baseline.
> - **Severity stratification MANDATORY:** edits classified as **safety-critical** (allergy, medication, dose, red-flag, diagnosis, plan), **clinically meaningful** (history, exam findings, risk-factor wording), or **stylistic**. Headline ER is over substantive (safety-critical + clinically-meaningful) edits; safety-critical edit rate reported separately as a leading indicator.
> - **Per-clinician disaggregation MANDATORY:** site-level ER hides individual complacency. Reporting must include per-clinician trajectories alongside aggregate.

**Threshold Guidance**

> ⚠️ **Provenance:** the > 15-percentage-point drop sustained ≥ 4 weeks comes from the existing Formal Definition complacency signal (carried from prior versions of the metric); the 30–80 % baseline range, the < 50 %-of-baseline pause trigger, and the zero-safety-critical-edits-with-continued-stylistic-editing trigger are **proposed in v3.3 as starting points**, not externally validated. Edit Rate is **interpretable only as a trajectory** (per Limitations and Novel Thinking); absolute thresholds below are deployment-context-dependent and require local calibration before contractual use.
>
> - **Pre-deployment / Day Zero baseline expectation:** substantive ER between 30 % and 80 % during the first 4 weeks. ER below 30 % in week 1 is a flag for inadequate review, not for excellent AI.
> - **Continuous monitoring alert:** substantive ER drops > 15 percentage points from the per-clinician baseline within any 12-week rolling window, sustained ≥ 4 weeks (the existing complacency signal in the Code block).
> - **Pause / review trigger:** substantive ER < 50 % of per-clinician baseline for 4 consecutive weeks, OR safety-critical edit rate drops to zero for ≥ 4 weeks while substantive edit rate remains > 10 % (suggests clinicians are stopping their safety review while continuing minor editing). Triggers trust-calibration review and pairing with HL.HF-6 Automation Bias Detection.

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

*See also: Edit Type Classification, Edit Location Distribution, Edit-Pattern Monitoring at Scale - all members of the Post-Generation Correction family. Edit Rate is the binary entry point; the other metrics add diagnostic depth. Interpret alongside Review-Before-Signing Rate and Time-to-Sign Distribution to distinguish improving AI from increasing complacency.*

---

### HL.HF-2 🟡 Edit Type Classification

Categorising edits: additions (omission fix), deletions (hallucination fix), modifications, structural. Distribution diagnoses failure mode.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-2 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Abridge; DeepScore |

**Why this tier?**

> More granular than edit rate - diagnoses failure mode (additions = omission problem, deletions = hallucination problem). Requires NLP classification but adds substantial diagnostic value.

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

*See also: Edit Rate, Edit Location Distribution, Edit-Pattern Monitoring at Scale - all members of the Post-Generation Correction family. Type classification is where the family becomes diagnostic rather than just descriptive: predominantly additions indicate an omission-dominant failure mode; predominantly deletions indicate a hallucination-dominant mode.*

---

### HL.HF-3 🟢 Review-Before-Signing Rate

Notes demonstrably reviewed before sign-off. NAS: ≥95% threshold, <85% pause trigger.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-3 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
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

### HL.HF-4 🟢 Time-to-Sign Distribution

Duration between generation and approval. Model as distribution - tail of very-fast approvals is safety-critical.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-4 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | EPR workflow data; Stanford principles |

**Why this tier?**

> Deployer-measurable from EPR data. The tail of very-fast approvals (<5 seconds for complex notes) is the safety-critical population. Distribution analysis detects rubber-stamping patterns.

**Formal Definition**

```
TTS = t_approve - t_generated. Report: median, P5, P10, P90. Normalise: TTS_norm = TTS / word_count. Flag: TTS_norm < 0.5s/word suggests rubber-stamping.
```

**Reference Standard**

> EPR + AVT product telemetry. `t_generated` = the timestamp at which the AVT-generated note becomes visible to the clinician for review. `t_approve` = the clinician signature event on the note. The window between these two timestamps captures total review-and-edit duration; TTS does NOT include time before AVT note availability or time after signature. Where the clinician opens, leaves, and returns to the note, TTS counts only the foreground review time within the EPR session if the EPR can distinguish; otherwise the full elapsed time is used and the limitation declared.

**Operational Specification**

> - **Window:** continuous; weekly distribution analysis per clinician.
> - **Population:** all AVT-generated notes signed during the window. Notes signed by a clinician other than the one to whom AVT was active (delegated workflows) excluded; flagged as a separate audit item.
> - **Distribution reporting MANDATORY:** P5, P10, median, P90 of TTS per clinician AND of TTS_norm (TTS / word_count). Single-number reporting (mean or median alone) is not Tier 1 sufficient - the safety signal lives in the lower tail.
> - **Per-clinician baseline MANDATORY:** baseline TTS_norm distribution computed across the first 4 weeks of clinician live use; subsequent reporting referenced to per-clinician baseline (parallel to [HL.HF-1 Edit Rate](#hl-hf-1)).
> - **Pairing with Edit Rate MANDATORY:** TTS distribution reported alongside HL.HF-1 substantive edit rate for the same clinician-window. Low TTS + low substantive edit rate is the rubber-stamping signal; either alone is ambiguous.
> - **Note-complexity stratification:** report TTS_norm distribution stratified by note word count quartile (short / medium / long / very-long); rubber-stamping risk is most visible on long/complex notes signed at short-note speed.

**Threshold Guidance**

> ⚠️ **Provenance:** the TTS_norm < 0.5 s/word rubber-stamping flag and the lower-tail focus carry over from the existing Formal Definition and Stanford principles cited in Source. Specific numbers (P5 < 0.3 s/word pause trigger, 4-week baseline window, 10 % below-baseline rate alert) are **proposed in v3.4 as starting points**, not externally validated. TTS is interpretable only as a distribution paired with edit rate; absolute thresholds below are deployment-context-dependent.
>
> - **Pre-deployment / Day Zero baseline:** establish per-clinician TTS_norm distribution across the first 4 weeks of live use; record P5, P10, median, P90.
> - **Continuous monitoring alert:** weekly P5 of TTS_norm < 0.3 s/word for any clinician (the rubber-stamping floor); OR the proportion of notes with TTS_norm < 0.5 s/word rises > 10 percentage points from per-clinician baseline.
> - **Pause / review trigger:** weekly P10 of TTS_norm < 0.3 s/word AND HL.HF-1 substantive edit rate < 25 % for the same clinician-window (rubber-stamping confirmed in distribution and in editing behaviour). Triggers trust-calibration review and pairing with HL.HF-6 Automation Bias Detection.

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

### HL.HF-5 🔵 Edit-Pattern Monitoring at Scale

Cross-system edit analysis (1M+/week, 150+ systems). Most scalable quality signal - locked inside one vendor.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-5 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Vendor-Proprietary |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
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

*See also: Edit Rate, Edit Type Classification, Edit Location Distribution - all members of the Post-Generation Correction family. Pattern monitoring operates at the fleet level to detect shifts invisible to any single deployer; informs what a national standard should require all vendors to provide.*

---

### HL.HF-6 🟡 Automation Bias Detection (Error Injection)

Deliberately seeded errors to test clinician catch rate. The only metric directly measuring human oversight. All others are proxies.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-6 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Regional (ICB) |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
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

**⚠️ Underspecification Warning (Tier B - strong concept, ad hoc protocols)**

> Automation bias is well-defined conceptually (Parasuraman & Manzey, *Human Factors* 2010) but measurement protocols in clinical AI remain ad hoc. Most published studies use vignette-based designs comparing diagnostic accuracy with and without AI assistance; there is no standardised measurement protocol for production AVT systems operating under real clinical time pressure. No consensus exists on acceptable automation bias rate thresholds - one computational pathology study reported a 7% rate without specifying whether that was concerning or within expected bounds for the task. An active RCT (NCT07328815) is testing nudge interventions but results are not yet available. Until standardised production protocols emerge, document explicitly: (a) the injection methodology (how errors are generated), (b) the injection rate, (c) the severity distribution of injected errors, (d) the detection criteria (what counts as "caught"), (e) the timing of assessment. Changes to any of these make values incomparable across audits.

**Novel Thinking / Implications**

> 💡 Only metric directly measuring oversight function. Quarterly error injection with known difficulty thresholds.

---

### HL.HF-7 🟡 Edit Location Distribution

Where in the note do clinicians make edits? Concentration in specific sections (history, examination, plan) reveals which sections the AI handles poorly. A diagnostic that complements edit type classification.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-7 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
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

*See also: Edit Rate, Edit Type Classification, Edit-Pattern Monitoring at Scale - all members of the Post-Generation Correction family. Locus analysis complements type classification: what kind of edit combined with where in the note identifies specific failure modes that either dimension alone would miss.*

---

### HL.HF-8 🟡 Trust Calibration Survey

Clinician confidence vs actual accuracy. Overconfidence = automation bias risk. Gap between stated and behavioural trust is itself a metric.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-8 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Day Zero Baseline, Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
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

**⚠️ Underspecification Warning (Tier B - concept defined, no AVT-validated instrument)**

> Multiple candidate instruments exist for trust calibration in clinical AI (TIAS, HATAS, AITI-H), but **none are validated specifically for ambient scribe contexts**. A 2024 Dokkyo Medical University review concluded that there are currently no accurate and objective measures available for evaluating trust calibration in clinical AI deployments. No thresholds exist for defining "appropriately calibrated" trust, and no empirical integration has been established between subjective trust measures and behavioural proxies (edit rate, review time, error detection) that would allow triangulation. Adapt TIAS or HATAS for AVT context as an interim measure, document the adaptation explicitly, and flag the absence of formal validation when reporting results. Pair with the existing behavioural complacency indicators (Edit Rate, Time-to-Sign, Review-Before-Signing) rather than relying on the survey instrument alone.

**Novel Thinking / Implications**

> 💡 'I always check carefully' + 5-second approval = trust calibration gap requiring architectural intervention.

---

### HL.HF-9 🟡 Re-record / Abandonment Rate

Frequency of clinicians abandoning AVT mid-consultation and starting again, or abandoning the AVT-generated note entirely and writing manually. Strong dissatisfaction signal indicating either technical failure or fundamental quality issues.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-9 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
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

> 💡 Re-record rate is the canary in the coal mine. When clinicians start restarting consultations or abandoning notes, something has gone fundamentally wrong - either the system has degraded or the workflow is broken. This is a leading indicator that should trigger immediate investigation, not routine review.

---

### HL.HF-10 🔵 Cognitive Load Assessment

Mental effort for review. Target: 'effortful but efficient' - enough to catch errors, not so much that time savings disappear.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-10 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
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

**⚠️ Underspecification Warning (Tier B - generic validation, no AVT-specific calibration)**

> NASA-TLX is validated generically with acceptable individual-setting ICC of 0.71–0.81 (lower for group settings). However, for AVT specifically: no subscale selection protocol exists, no consensus on measurement timing (during encounter / immediately after charting / end of day / end of week), no documentation-specific adaptation of the instrument, and no established thresholds for "acceptable" cognitive load in AVT review tasks. The 60.7% reduction in composite cognitive load reported in a 2024 Abridge study is a point estimate with no reference scale for clinical interpretation - "60% less" of an undefined baseline is not directly actionable. Use NASA-TLX as an interim measure, specify the timing and subscale selection used, and avoid comparing raw scores across studies that use different protocols. The proposed **Verification Burden** metric (Human Factors & Workflow) is intended to capture a more specific construct that may ultimately prove more actionable than global cognitive load.

**Novel Thinking / Implications**

> 💡 Optimal load is non-obvious: too low = disengagement, too high = no benefit.

---

### HL.HF-11 🔵 Inter-Clinician Edit Variance

Do different clinicians edit the same AI output similarly? High variance suggests either ambiguous AI output (different clinicians read it differently) or inconsistent quality standards across clinicians. Both are governance issues.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-11 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
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

> 💡 If Clinician A always edits the AI output extensively and Clinician B never edits it, the issue might be either clinician (one is too critical, the other is too lax) or the AI (the output is ambiguous). Inter-clinician variance reveals whether the review function is consistent - a prerequisite for meaningful aggregate metrics.

---

### HL.HF-12 🔵 Clinical Documentation Skill Attenuation

Longitudinal ability to document without AI. Sleeper risk - if a generation trains with AVT, baseline capability degrades.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-12 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | Aviation skill degradation literature |

**Why this tier?**

> Long-term longitudinal study. Effects take years to manifest. Important for workforce planning but not actionable at individual deployer level.

**Formal Definition**

```
Annual: clinicians document N simulated encounters without AI, scored via PDSQI-9. SA(t) = PDSQI9_noAI(t) - PDSQI9_noAI(t-1). Negative SA = attenuation. Compare trainees against pre-AVT cohort norms.
```

**References**

- **Aviation analogy**: Casner & Schooler (2014) - pilot skill degradation

**Limitations**

> Long-term study. Hard to isolate AVT as cause.

**Novel Thinking / Implications**

> 💡 Medical education bodies should be tracking this now.

---

### HL.HF-13 🔵 Cognitive Offloading Rate

Proportion of clinicians who report relying on AI for content recall ('I don't need to remember, the AI will catch it'). Different from automation bias - this is active delegation rather than passive trust. Predicts skill attenuation.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-13 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
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

### HL.HF-14 🔵 Trust Halo Decay Rate

Whether initial high trust persists after errors. Absent decay = dangerous over-trust. Trust halo drives off-label scope creep.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-14 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | Trust halo effect analysis |

**Why this tier?**

> Research metric requiring longitudinal measurement. Conceptually important for understanding off-label use drivers but not operationally measurable at scale.

**Formal Definition**

```
Longitudinal T(t). After error at t_e, decay rate λ = -dT/dt for t > t_e. Healthy: λ > 0 (appropriate recalibration). Dangerous: λ ≈ 0 (trust unchanged despite evidence).
```

**Limitations**

> Longitudinal measurement required.

**⚠️ Underspecification Warning (Tier A - no validated measurement in clinical AI)**

> The trust halo effect is well-established in cognitive psychology but has **not been operationalised for clinical AI or AVT specifically**. The concept substantially overlaps with automation bias, and the empirical boundary between the two constructs is not established - it is unclear whether they should be measured as distinct phenomena or as facets of a common over-reliance construct. No validation studies exist. No measurement instruments have been adapted from cognitive psychology to the clinical AI context. Two viable paths forward: (a) define a specific experimental paradigm (e.g. testing whether positive experience with transcription accuracy transfers uncritically to trust in clinical summarisation accuracy, which is a different capability) and build validation evidence from there, or (b) fold the construct into the broader automation bias / over-reliance family until the measurement science matures enough to distinguish it meaningfully. Until one of these is done, any reported values should carry explicit acknowledgement of the definitional uncertainty.

**Novel Thinking / Implications**

> 💡 Trust halo → off-label use: over-trust drives scope creep. The halo is the mechanism; off-label use is the consequence.

---

### HL.HF-15 🔵 Note Review Fatigue Trajectory

Review quality degradation over a clinical session. The 9am note review may be different from the 5pm note review, and AVT may amplify end-of-session fatigue effects by adding documentation review burden to existing clinical fatigue.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-15 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | Clinical fatigue research applied to AVT review |

**Why this tier?**

> Research metric. Important workforce safety question but not routinely measurable.

**Formal Definition**

```
Track review quality metrics (time-to-sign, edit rate, error detection in injection audits) by time-of-day and session position. Fatigue Slope = degradation rate per hour into session. Significant negative slope indicates fatigue effects.
```

**Limitations**

> Confounded with case mix variation (afternoon clinics may have different complexity). Requires careful statistical controls.

**⚠️ Underspecification Warning (Tier A - underlying concept unoperationalised)**

> The broader concept of attention drift across a clinician's reviewing session has **no operationalised definition in AVT literature**. The Cognitive Drift Index (Frontiers in Neuroscience 2025) measures information consumers' judgment shifts in unrelated domains, not clinician review vigilance. A 2026 KevinMD essay described "the slow erosion of clinical humility" qualitatively but offered no measurement approach. No published study has established a detection methodology, thresholds, or relationship to patient safety outcomes. Proposed interim operationalisation for this taxonomy - to be treated as a working definition pending empirical validation - is a composite of (a) declining review time per note over a session, (b) reduced edit rate trajectory within sessions, and (c) reduced error detection rate in periodic injection testing stratified by time-of-session. This proposal has not been validated; deployers using it should document the operational definition applied and treat results as exploratory rather than diagnostic.

**Novel Thinking / Implications**

> 💡 If review quality degrades through the session, the safety implications are significant: the last patients of the day get the least rigorous oversight. AVT systems designed assuming consistent reviewer attention are operating outside that assumption for a meaningful fraction of consultations. This argues for fatigue-aware workflow design - perhaps requiring more thorough review for end-of-session notes, or rotating review responsibility.

---

---

### Sociotechnical & Resilience sub-cluster

*Systems-level constructs drawn from FRAM, Safety-II, and resilience engineering. These metrics assess the clinician-AVT joint cognitive system rather than AVT alone, and capture dimensions that standard human factors metrics miss - the gap between intended and actual practice, the hidden cost of verification, and the capacity to handle unexpected situations.*

---

### HL.HF-16 🔵 Work-as-Imagined vs Work-as-Done Gap

The gap between how AVT is intended to be used (per procedures, training, and governance documentation) and how it is actually used in clinical practice. A construct from Hollnagel's FRAM methodology and the Safety-II tradition. Subsumes and generalises the existing Off-Label Use Detection metric - not every WAI/WAD gap is off-label, and not every adaptation is a safety problem, but the gap itself is diagnostically valuable.

|Dimension              |Value                                                                  |
|-----------------------|-----------------------------------------------------------------------|
| **Reference** | HL.HF-16 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research                                         |
|**Measurement Cadence**|Periodic audit                                                         |
|**Pipeline Layer**     |Cross-cutting                                                          |
|**Assurance Question** |Safety                                                                 |
|**Measurement Method** |Hybrid                                                                 |
|**Lifecycle Phases**   |Periodic Audit                                                         |
|**Responsible Actors** |Deployer, Academic                                                     |
|**Maturity**           |Proposed / Novel                                                       |
|**Outcome Type**       |Distal                                                                 |
|**Applicability**      |General Healthcare AI                                                  |
|**Source**             |Hollnagel FRAM methodology; JMIR 2026 SEIPS-based AVT evaluations      |

**Why this tier?**

> Research-grade metric requiring ethnographic observation and structured interview methodology. Not routinely measurable at deployer level. Academic or national evaluation programme responsibility.

**Formal Definition**

```
Three-step methodology: (1) Document WAI from training materials, SOPs, vendor guidance, and governance policies; (2) Observe WAD through shadowing, workflow analysis, and semi-structured clinician interviews; (3) Gap analysis - categorise deviations as {beneficial adaptation, neutral workaround, latent risk, active hazard}. Report gap count per category and exemplar descriptions rather than a single scalar - the qualitative detail is what supports intervention.
```

**Limitations**

> Ethnographic methods are resource-intensive and subjective. WAI is itself often poorly documented. Observer effects shape observed behaviour. Generalisation across practices is limited.

**Novel Thinking / Implications**

> 💡 Every complex sociotechnical system has a WAI/WAD gap - procedures can never fully specify practice. The Safety-II insight is that adaptations are not automatically failures; they are often what makes the system work at all. The diagnostic question is not "is there a gap?" (there always is) but "which gaps indicate genuine risk vs which indicate necessary adaptation that should be formalised back into WAI?" This metric surfaces the question; human judgment answers it.

---

### HL.HF-17 🟡 Verification Burden

The additional workload created by the need to verify AI-generated content against clinical reality - reading the note, cross-checking against the conversation, identifying errors, making corrections. Distinct from the existing Cognitive Load Assessment metric, which measures total effort. Verification burden is specifically the checking overhead that exists only because the output needs checking. A well-calibrated AVT system minimises this burden; a poorly-calibrated one shifts documentation time into verification time and may eliminate the apparent efficiency gain.

|Dimension              |Value                                                               |
|-----------------------|--------------------------------------------------------------------|
| **Reference** | HL.HF-17 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                              |
|**Measurement Cadence**|Periodic audit                                                      |
|**Pipeline Layer**     |Cross-cutting                                                       |
|**Assurance Question** |Human Factors                                                       |
|**Measurement Method** |Hybrid                                                              |
|**Lifecycle Phases**   |Day Zero Baseline, Periodic Audit                                   |
|**Responsible Actors** |Deployer, Academic                                                  |
|**Maturity**           |Emerging                                                            |
|**Outcome Type**       |Proximal                                                            |
|**Applicability**      |AVT-Contextualised                                                  |
|**Source**             |JMIR 2026 e86166 SEIPS-based evaluation; GOSH Phase 4 TimeCat data  |

**Why this tier?**

> Conceptually important - distinguishes apparent efficiency gain from actual efficiency gain - but requires time-motion observation methodology (TimeCat or equivalent). Day Zero baseline plus periodic re-measurement supports trajectory analysis.

**Formal Definition**

```
VB = t_review + t_correction + t_cross_reference, measured per consultation. Baseline pre-AVT: equivalent activities (proofreading own notes, referencing structured fields). Net Verification Cost = VB_AVT - VB_pre-AVT. Efficiency gain = (t_documentation_pre - t_documentation_AVT) - Net Verification Cost. A genuinely efficient system has positive net gain after accounting for verification burden.
```

**Limitations**

> TimeCat or equivalent time-motion methodology is labour-intensive. Verification activities are often interleaved with other work and hard to isolate. Self-report on verification time is unreliable because the activity is partly automatic.

**Novel Thinking / Implications**

> 💡 The marketing claim "AVT saves 3 minutes of documentation time per consultation" is meaningless without verification burden accounting. A system that saves 3 minutes of typing but adds 4 minutes of verification has negative net efficiency - and research suggests this scenario is common early in deployment before clinicians develop efficient review patterns. Verification burden should be reported alongside every documentation time saving claim, or the claim should not be reported at all.

---

### HL.HF-18 🔵 Resilience Capacities Assessment

Structured assessment of the clinician-AVT joint cognitive system against the four Safety-II resilience capacities: **responding** to unexpected events, **monitoring** for signs of degradation, **learning** from experience, and **anticipating** future challenges. From Hollnagel's resilience engineering framework. Applied not to AVT alone but to the combined human-machine system as it operates in context.

|Dimension              |Value                                                             |
|-----------------------|------------------------------------------------------------------|
| **Reference** | HL.HF-18 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research                                    |
|**Measurement Cadence**|Periodic audit                                                    |
|**Pipeline Layer**     |Cross-cutting                                                     |
|**Assurance Question** |Safety                                                            |
|**Measurement Method** |Hybrid                                                            |
|**Lifecycle Phases**   |Periodic Audit                                                    |
|**Responsible Actors** |Deployer, National Body, Academic                                 |
|**Maturity**           |Proposed / Novel                                                  |
|**Outcome Type**       |Distal                                                            |
|**Applicability**      |General Healthcare AI                                             |
|**Source**             |Hollnagel Safety-II; FRAM methodology; resilience engineering literature|

**Why this tier?**

> Research framework applied at system level. Not a routine metric. National or academic responsibility for maturing the methodology into deployable assessment.

**Formal Definition**

```
Four capacity dimensions scored via structured scenario-based assessment and qualitative evaluation:
(1) Responding - when an AVT failure occurs mid-consultation (crash, silent degradation, wrong-patient data), how does the clinician-system respond? Recovery time, recovery completeness, downstream impact.
(2) Monitoring - what signals does the system provide that allow the clinician to detect degradation? Are those signals attended to in practice?
(3) Learning - when errors are discovered, how is that learning captured and integrated into future work? (Links to Hazard Log Completeness and Training Material Currency)
(4) Anticipating - does the deployer identify and prepare for foreseeable challenges (model updates, regulatory changes, novel failure modes)?
Score each capacity 1–5 with narrative justification. Composite is a profile, not a single number.
```

**Limitations**

> Assessment is qualitative and requires trained evaluators. Framework originally developed for complex sociotechnical systems (healthcare, aviation); application to AVT specifically is novel. Scoring inter-rater reliability has not been established for this application.

**Novel Thinking / Implications**

> 💡 Traditional safety metrics are Safety-I: counting failures and aiming for zero. Resilience metrics are Safety-II: assessing the capacity to handle failures that will inevitably occur. An AVT deployment with zero recorded incidents but weak resilience capacities is brittle - the first real test will reveal the gap. This metric family complements rather than replaces the incident-based metrics in Safety & Governance.

---

### HL.HF-19 🟡 AI-Off Performance Test

Scheduled exercises where clinicians document a clinical encounter without AVT assistance, and the resulting documentation is assessed for quality against baseline standards. Provides an operational implementation of the existing Clinical Documentation Skill Attenuation concept - instead of inferring skill degradation longitudinally, directly measure current unassisted capability. Also doubles as business continuity assurance: can the clinical team function if AVT is unavailable?

|Dimension              |Value                                                                                                 |
|-----------------------|------------------------------------------------------------------------------------------------------|
| **Reference** | HL.HF-19 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                                                                |
|**Measurement Cadence**|Periodic audit                                                                                        |
|**Pipeline Layer**     |Cross-cutting                                                                                         |
|**Assurance Question** |Human Factors                                                                                         |
|**Measurement Method** |Hybrid                                                                                                |
|**Lifecycle Phases**   |Day Zero Baseline, Periodic Audit                                                                     |
|**Responsible Actors** |Deployer                                                                                              |
|**Maturity**           |Proposed / Novel                                                                                      |
|**Outcome Type**       |Distal                                                                                                |
|**Applicability**      |General Healthcare AI                                                                                 |
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

> 💡 The endoscopy AI-off finding (adenoma detection rate falling from 28.4% to 22.4% when AI was removed after a period of AI use) is the first robust real-world evidence of clinical deskilling from AI dependency. For ambient scribes, the equivalent question is whether clinicians lose the ability to write a clinically complete note unassisted after a period of AVT use. This is testable today. The business continuity case - can the practice function during a vendor outage? - is almost sufficient reason to run the test regardless of the deskilling question.

### IO.PX-1 🟢 Patient Opt-Out Rate

Percentage declining AVT. Disaggregate by demographics to reveal equity issues in consent model.

| Dimension | Value |
|-----------|-------|
| **Reference** | IO.PX-1 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Patient Experience |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | NAS SPI; CQC Mythbuster 109 |

**Why this tier?**

> Deployer-measurable from practice records. Low-burden continuous monitoring. Rising rates signal trust issues. Demographic disaggregation reveals consent model equity.

**Formal Definition**

```
OOR = |P_optout| / |P_offered|. χ² test for independence between opt-out and demographic group. Significant association = inequitable consent model.
```

**Reference Standard**

> EPR + AVT product workflow telemetry. Two distinct opt-out events MUST be tracked separately:
>
> - **Registration-level opt-out** - patient declines AVT use across all encounters with the practice (status set in patient record)
> - **Per-encounter opt-out** - patient declines AVT for a specific consultation while remaining eligible elsewhere (cross-link to [GV.CR-1 Patient Dissent Recording Rate](#gv-cr-1))
>
> Aggregating the two hides the underlying signal. The denominator `P_offered` is the count of patients to whom AVT use was offered (not consultations); a patient declining once and accepting later contributes once to numerator and once to denominator. Pre-conditions for inclusion: the patient was demonstrably informed (cross-link to [GV.CR-2 Verbal Notification Compliance](#gv-cr-2)) - undocumented offers are excluded with reason.

**Operational Specification**

> - **Window:** continuous; monthly aggregate per practice and per clinician.
> - **Population:** all patients offered AVT during the window. Excludes patients for whom AVT was not offered (e.g. consultation type explicitly carved out under proposed metric *GV.CR-14 Consultation-Type Appropriateness Assessment* — see Roadmap — when implemented).
> - **Demographic disaggregation MANDATORY:** opt-out rate stratified by age band, sex, ethnicity, and primary language at minimum. Disability status and deprivation index where the data is available. Aggregate-only reporting hides the equity signal that is the metric's primary purpose.
> - **Statistical test MANDATORY:** χ² (or Fisher's exact for small cells) test for independence between opt-out and each demographic axis, with multiple-comparison correction (Holm-Bonferroni or FDR) across axes. Report both raw rates and significance.
> - **Trajectory MANDATORY:** monthly opt-out rate trajectory per practice; rising aggregate rate is a separate signal from disparate rate, and both matter.

**Threshold Guidance**

> ⚠️ **Provenance:** the demographic-disaggregation requirement and the equity-not-preference framing follow from the NAS SPI and CQC Mythbuster 109 cited above, plus the existing Novel Thinking section. Specific numerical thresholds (5 % aggregate alert, 2× demographic-disparity ratio trigger, χ² p < 0.05 with Holm correction) are **proposed in v3.4 as starting points**, not externally validated. The metric's value is in the disparities it reveals, not in any absolute opt-out target; require local calibration before contractual use.
>
> - **Pre-deployment / Day Zero baseline:** establish baseline opt-out rate disaggregated by the demographic axes above; document any historical signal in the practice population that should be expected to carry over.
> - **Continuous monitoring alert:** monthly aggregate opt-out rate rises > 2 percentage points from per-practice baseline; OR any demographic axis shows opt-out ratio ≥ 2× the practice mean with χ² (Holm-corrected) p < 0.05.
> - **Pause / review trigger:** demographic disparity ≥ 3× the practice mean sustained two consecutive months on any axis (signals systematic equity failure in the consent model, not noise); OR aggregate opt-out rate rises > 5 percentage points (signals trust deterioration). Pair with [GV.CR-2 Verbal Notification Compliance](#gv-cr-2) to test whether the consent model is the cause.

**References**

- **CQC**: Mythbuster 109: implied consent sufficient but patients must be informed

**Limitations**

> Low opt-out ≠ informed consent. The demographic-disaggregation requirement in the Operational Specification surfaces equity issues that aggregate rate hides; it does not address the upstream concern that opt-out rates depend on the quality of notification (covered by GV.CR-2) and on patient understanding of what they are declining (no current metric).

**Novel Thinking / Implications**

> 💡 Higher opt-out in specific demographics = equity issue in consent model, not just preference.

---

### IO.PX-2 🔵 Patient-Perceived Accuracy

When patients are shown their AVT-generated notes, do they recognise the consultation? Distinct from clinician-judged accuracy - patients may identify omissions or distortions that clinicians miss because they were the speakers.

| Dimension | Value |
|-----------|-------|
| **Reference** | IO.PX-2 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Patient Experience |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
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

### IO.PX-3 🔵 Emotional Content Preservation

Does the note capture the patient's emotional state when clinically relevant? AVT systems trained on standard clinical notes may strip affective content that matters for mental health, end-of-life care, safeguarding, and complex consultations.

| Dimension | Value |
|-----------|-------|
| **Reference** | IO.PX-3 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Patient Experience |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | Identified gap in clinical AI evaluation - affective content is systematically deprioritised |

**Why this tier?**

> Critical for specific clinical contexts (mental health, palliative care, safeguarding) but not universally applicable.

**Formal Definition**

```
For consultations involving emotional content (annotated): proportion of clinically relevant emotional markers preserved in summary. Categories: distress, grief, fear, ambivalence, hope. Required for: mental health, end-of-life, safeguarding, life-limiting illness consultations.
```

**Limitations**

> Emotional content annotation is subjective. Different clinical contexts have different requirements for affective documentation.

**Novel Thinking / Implications**

> 💡 AVT systems trained on standard primary care notes have learned that emotional content is rarely documented. When deployed in mental health, palliative care, or safeguarding contexts, this learned behaviour becomes a serious gap. The patient who said 'I just don't know how I'll cope' deserves to have that documented - but the AI may strip it as non-clinical content.

---

### IO.PX-4 🔵 Cultural & Linguistic Appropriateness

Does the note use language that respects the patient's cultural and linguistic context? Important for shared records that patients can access. Includes avoiding stigmatising language and respecting how patients describe their own conditions.

| Dimension | Value |
|-----------|-------|
| **Reference** | IO.PX-4 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Patient Experience |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
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

> 💡 AVT systems trained on legacy clinical notes may perpetuate language patterns that are inappropriate when patients can read their own records. The language that was acceptable when notes were clinician-only is sometimes unacceptable when notes are shared. This is a quiet failure mode - the AI is faithfully reproducing patterns from its training data that need to change.

---

### IO.PX-5 🔵 Chilling Effect Assessment

Whether AVT suppresses sensitive disclosures. Most under-researched risk - population-level safety issue if record becomes systematically biased.

| Dimension | Value |
|-----------|-------|
| **Reference** | IO.PX-5 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Patient Experience |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | NHSE LLM framework gap analysis |

**Why this tier?**

> The most under-researched AVT risk but extremely difficult to measure - detecting information that wasn't shared. Requires carefully designed qualitative research.

**Formal Definition**

```
Disclosure Rate Ratio DRR = DR_AVT / DR_noAVT for sensitive categories (mental health, substance use, sexual health, domestic abuse). DRR < 1.0 = chilling effect. Mixed-methods: quantitative + qualitative.
```

**Limitations**

> Detecting information not shared requires careful qualitative research.

**Novel Thinking / Implications**

> 💡 If AVT suppresses sensitive disclosures, the record becomes systematically biased - missing exactly the information that matters most.

---

### IO.PX-6 🔵 Therapeutic Relationship Impact

How AVT affects consultation quality. Net impact depends on whether review is in-consultation or post-consultation.

| Dimension | Value |
|-----------|-------|
| **Reference** | IO.PX-6 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Patient Experience |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
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

### IO.PX-7 🟡 Full Attentiveness Rate

Proportion of consultation time during which the clinician is fully attentive to the patient, measured objectively rather than through self-report. Distinct from the existing Therapeutic Relationship Impact metric, which captures subjective perception. Stults et al. (2025) reported an increase from 57.9% to 93.0% with ambient AI - a large effect size that, if reproducible, represents one of the strongest AVT benefit signals currently available.

|Dimension              |Value                                                           |
|-----------------------|----------------------------------------------------------------|
| **Reference** | IO.PX-7 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                          |
|**Measurement Cadence**|Periodic audit                                                  |
|**Pipeline Layer**     |Cross-cutting                                                   |
|**Assurance Question** |Patient Experience                                              |
|**Measurement Method** |Passive Observational                                           |
|**Lifecycle Phases**   |Day Zero Baseline, Periodic Audit                               |
|**Responsible Actors** |Deployer, Academic                                              |
|**Maturity**           |Emerging                                                        |
|**Outcome Type**       |Proximal                                                        |
|**Applicability**      |AVT-Contextualised                                              |
|**Source**             |Stults et al. 2025 (57.9%→93.0% improvement with ambient AI)     |

**Why this tier?**

> Observable with time-motion methodology (TimeCat or equivalent). Day Zero baseline enables pre/post comparison. Important for establishing genuine patient experience improvement rather than self-reported improvement.

**Formal Definition**

```
Full Attentiveness = t_eye_contact + t_active_listening + t_direct_engagement / t_total_consultation. Measured via TimeCat observation, video analysis, or (where accepted by patients) automated gaze tracking. Baseline pre-AVT vs post-AVT comparison. Report as distribution across consultations, not just mean - the clinically relevant improvement is often in the tail (consultations where the clinician was previously heavily divided between patient and screen).
```

**Limitations**

> Observation methodology is labour-intensive. Observer effects change clinician behaviour. Eye contact patterns are culturally variable and not always a valid proxy for attention. Patient consent required for video or automated tracking.

**Novel Thinking / Implications**

> 💡 This is probably the strongest candidate for a positive AVT benefit metric that isn't subject to the Coiera critique. Unlike documentation time saved (which says nothing about patient outcome), attentiveness is directly related to the therapeutic alliance, to patient disclosure, and to shared decision-making. If the Stults et al. finding is reproducible, it becomes the primary argument for AVT adoption on quality-of-care grounds rather than efficiency grounds.

---

### IO.PX-8 🔵 Patient Comprehension of AI-Generated Summaries

When AI-generated clinical summaries are shared with patients (via NHS App, patient portals, or printed after-visit summaries), do patients actually understand them? Distinct from the existing Patient-Perceived Accuracy metric, which measures recognition ("does this match our conversation?"). Comprehension measures whether the patient can correctly state what the summary says about their condition, medications, and next steps.

|Dimension              |Value                                                                    |
|-----------------------|-------------------------------------------------------------------------|
| **Reference** | IO.PX-8 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research                                           |
|**Measurement Cadence**|Periodic audit                                                           |
|**Pipeline Layer**     |Summarisation                                                            |
|**Assurance Question** |Patient Experience                                                       |
|**Measurement Method** |Survey                                                                   |
|**Lifecycle Phases**   |Periodic Audit                                                           |
|**Responsible Actors** |Deployer, Academic                                                       |
|**Maturity**           |Proposed / Novel                                                         |
|**Outcome Type**       |Distal                                                                   |
|**Applicability**      |General Healthcare AI                                                    |
|**Source**             |Health literacy research; growing relevance as patient access to records expands|

**Why this tier?**

> Important as patient-facing summaries become routine. Research-grade measurement methodology required. Best suited for periodic structured study.

**Formal Definition**

```
Patient Comprehension Test: after receiving an AI-generated summary, patient is asked structured questions about: (1) primary diagnosis or problem identified; (2) medications prescribed and their purpose; (3) follow-up actions required; (4) warning signs requiring re-contact. Comprehension Rate = |correctly_answered_questions| / |total_questions|. Disaggregate by health literacy level, age, language, and education to detect differential comprehension.
```

**Limitations**

> Requires patient time and willingness. Cultural and language barriers affect comprehension measurement itself. Summaries generated for clinical purposes may use language appropriate for clinicians but inaccessible to patients - this is a separable design question from AVT accuracy.

**Novel Thinking / Implications**

> 💡 With NHS App access making records patient-facing by default, AI-generated summaries written in clinical language become a health literacy barrier. A summary that is technically correct but uses "dyspnoea" instead of "breathlessness" is accurate from an AVT evaluation standpoint but opaque to the patient. Comprehension measurement should drive a design choice: should AVT generate two versions (clinical record + patient summary) or one version written for both audiences?

---

### IO.PX-9 🔵 Downstream Diagnostic Accuracy

Whether clinicians making subsequent decisions based on AVT-generated notes arrive at the same diagnostic and management conclusions they would have reached if they had access to the original consultation. Measured through controlled clinical reasoning studies where clinicians work from AVT notes vs verbatim transcripts vs direct observation. The distal outcome metric Coiera & Fraile-Navarro argue is missing from current AVT evaluation.

|Dimension              |Value                                                             |
|-----------------------|------------------------------------------------------------------|
| **Reference** | IO.PX-9 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research                                    |
|**Measurement Cadence**|Periodic audit                                                    |
|**Pipeline Layer**     |End-to-End                                                        |
|**Assurance Question** |Safety                                                            |
|**Measurement Method** |Human Review                                                      |
|**Lifecycle Phases**   |Periodic Audit                                                    |
|**Responsible Actors** |Academic, National Body                                           |
|**Maturity**           |Proposed / Novel                                                  |
|**Outcome Type**       |Distal                                                            |
|**Applicability**      |General Healthcare AI                                             |
|**Source**             |Coiera & Fraile-Navarro, JMIR Med Inform February 2026            |

**Why this tier?**

> Gold-standard distal outcome metric. Extremely resource-intensive. National research programme responsibility. Complements the existing Clinical Decision Equivalence metric by focusing specifically on diagnostic rather than management decisions.

**Formal Definition**

```
Blinded multi-clinician study design: same clinical case presented in three conditions - (a) clinician observes consultation directly, (b) clinician reads AVT-generated note, (c) clinician reads verbatim transcript. Each clinician makes diagnostic and differential diagnostic choices. Downstream Diagnostic Accuracy = agreement between conditions. Primary metric: κ between AVT condition and direct observation condition. Secondary metric: discrepancies stratified by clinical complexity.
```

**Limitations**

> Very expensive - requires multiple blinded clinicians per case, clinical reasoning time, and careful study design. Inter-clinician variation in diagnostic reasoning adds noise. Simulated decision-making may not reflect real-world behaviour under time pressure.

**Novel Thinking / Implications**

> 💡 This is the metric that answers the question "does AVT preserve the clinical signal?" If clinicians reading AVT-generated notes make different diagnostic decisions than clinicians who observed the original consultation, all the proximal metrics (WER, edit rate, documentation time) are at best partially informative and at worst misleading. The Coiera critique is that the field has been measuring proxies and assuming they correlate with this - without evidence. This metric is the evidence.

---

### IO.PX-10 🔵 Medication Error Rate Differential

Pre/post AVT comparison of medication errors at the practice or trust level, including wrong-drug, wrong-dose, wrong-frequency, allergy-related, and interaction-related errors. The ultimate distal outcome that medication documentation accuracy ultimately serves. If AVT improves medication documentation (per attribute-level metrics) but medication errors don't decrease, the documentation improvement is not reaching the patient.

|Dimension              |Value                                                                |
|-----------------------|---------------------------------------------------------------------|
| **Reference** | IO.PX-10 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research                                       |
|**Measurement Cadence**|Periodic audit                                                       |
|**Pipeline Layer**     |End-to-End                                                           |
|**Assurance Question** |Safety                                                               |
|**Measurement Method** |Hybrid                                                               |
|**Lifecycle Phases**   |Day Zero Baseline, Periodic Audit                                    |
|**Responsible Actors** |National Body, Academic                                              |
|**Maturity**           |Proposed / Novel                                                     |
|**Outcome Type**       |Distal                                                               |
|**Applicability**      |General Healthcare AI                                                |
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

### IO.FE-1 🟡 Deployment Equity Index

Whether AVT creates two-tier documentation quality across practices. Track against deprivation indices.

| Dimension | Value |
|-----------|-------|
| **Reference** | IO.FE-1 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Regional (ICB), National Body |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
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

### IO.FE-2 🟡 Accent Taxonomy Standardisation

Meta-metric assessing whether demographic-disaggregated WER uses a sociolinguistically informed accent taxonomy appropriate for NHS populations, rather than ad-hoc or inappropriate categorisations. The FAccT 2024 critique of ASR accent categorisation highlighted that race-based, geography-based, and native/non-native categories are systematically flawed proxies for the actual acoustic variation that affects ASR performance. For NHS deployment, a meaningful taxonomy must cover British regional accents, South Asian English varieties, West African English, Caribbean English, Eastern European English, and other varieties representative of NHS patient populations.

|Dimension              |Value                                                         |
|-----------------------|--------------------------------------------------------------|
| **Reference** | IO.FE-2 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                        |
|**Measurement Cadence**|One-off gate                                                  |
|**Pipeline Layer**     |ASR / Transcription                                           |
|**Assurance Question** |Fairness & Equity                                             |
|**Measurement Method** |Human Review                                                  |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                |
|**Responsible Actors** |Vendor, National Body                                         |
|**Maturity**           |Proposed / Novel                                              |
|**Outcome Type**       |Proximal                                                      |
|**Applicability**      |AVT-Specific                                                  |
|**Source**             |FAccT 2024 critique of ASR accent categorisation; sociolinguistics literature|

**Why this tier?**

> Prerequisite for meaningful fairness assessment. Without a defensible taxonomy, Demographic-Disaggregated WER numbers are not comparable across vendors and may hide rather than reveal bias.

**Formal Definition**

```
Assessment against criteria: (1) Sociolinguistic validity - categories correspond to identifiable phonological communities, not political or racial groupings; (2) NHS relevance - categories include varieties actually present in NHS patient populations; (3) Sample adequacy - each category has sufficient evaluation data for stable WER estimation; (4) Documentation - categorisation methodology is transparent and replicable. Binary pass/fail per criterion; composite = all four must pass.
```

**Limitations**

> Sociolinguistic categorisation is itself contested. Any taxonomy makes choices that can be critiqued. The alternative - no categorisation - is worse because it hides all disparities.

**Novel Thinking / Implications**

> 💡 The hardest form of bias to fix is bias that cannot be measured, and ad-hoc accent categorisation produces unmeasurable bias. An NHS-specific accent taxonomy is infrastructure that would benefit every deployed AVT system - a national body responsibility that would pay for itself quickly. Without it, every vendor's Demographic-Disaggregated WER is self-reported against self-chosen categories, and independent verification is impossible.

### IO.FE-3 🟡 Clinical Domain Performance Variance

Accuracy variation across specialties and complexity. Compound boundary risk: degradation multiplies across dimensions.

| Dimension | Value |
|-----------|-------|
| **Reference** | IO.FE-3 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

### IO.FE-4 🔵 Intersectional Performance

Accuracy at the intersection of demographic dimensions (e.g. elderly EAL women). Single-axis disaggregation misses compound disadvantage - a system may perform adequately on each dimension separately but fail badly at intersections.

| Dimension | Value |
|-----------|-------|
| **Reference** | IO.FE-4 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor, National Body |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

> 💡 An elderly, EAL, female patient with limited health literacy may be at the worst-case intersection for AVT accuracy - yet single-axis metrics for elderly, EAL, female, and low-literacy patients may all look acceptable individually. Intersectional analysis reveals this compound disadvantage. Required by population health equity but rarely measured.

---

### IO.FE-5 🔵 Intersectional Compound Fairness Score

Extension of the existing Intersectional Performance metric using the FAIR-MED Compound Fairness Score methodology. Where Intersectional Performance measures accuracy at each demographic intersection, Compound Fairness Score calculates whether disadvantage compounds multiplicatively or additively - that is, whether the intersection performs worse than would be predicted by adding the individual demographic disadvantages.

|Dimension              |Value                                                                                |
|-----------------------|-------------------------------------------------------------------------------------|
| **Reference** | IO.FE-5 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research                                                       |
|**Measurement Cadence**|Periodic audit                                                                       |
|**Pipeline Layer**     |Cross-cutting                                                                        |
|**Assurance Question** |Fairness & Equity                                                                    |
|**Measurement Method** |Computational                                                                        |
|**Lifecycle Phases**   |Periodic Audit                                                                       |
|**Responsible Actors** |Vendor, National Body, Academic                                                      |
|**Maturity**           |Emerging                                                                             |
|**Outcome Type**       |Distal                                                                               |
|**Applicability**      |General Healthcare AI                                                                |
|**Source**             |FAIR-MED: Bias Detection and Fairness Evaluation in Healthcare Focused XAI (Springer 2025)|

**Why this tier?**

> Research-grade methodology requiring substantial demographic-linked data. National evaluation or vendor pre-deployment. Complements rather than replaces single-axis fairness metrics.

**Formal Definition**

```
For demographic axes A₁, A₂, ..., Aₙ with performance gaps gap(Aᵢ): expected intersection gap under additive model = Σ gap(Aᵢ); actual intersection gap = observed gap at intersection ∩Aᵢ. Compound Fairness Score CFS = actual_gap / expected_additive_gap. CFS > 1 indicates multiplicative compounding (intersection is worse than sum of parts); CFS ≈ 1 indicates additive; CFS < 1 indicates sub-additive. Multiplicative compounding is the warning signal for worst-case population failures.
```

**Limitations**

> Requires large enough samples at every demographic intersection for stable estimation - often infeasible for rare intersections. Additive model assumption may not hold even in fair systems. Interpretation is statistical rather than mechanistic.

**Novel Thinking / Implications**

> 💡 Single-axis fairness can miss compound disadvantage entirely. A system that performs acceptably on "elderly", "EAL", "female", and "low literacy" as separate categories may perform catastrophically on the intersection. The compound fairness score tests whether this is happening and quantifies how bad it is. For NHS populations where intersectional disadvantage is the rule rather than the exception, single-axis metrics alone are insufficient.

### IO.FE-6 🔵 Rare Presentation Handling

Accuracy on uncommon clinical presentations vs common ones. Long-tail performance matters disproportionately for diagnostic safety - the rare presentation that's missed is the most dangerous one to miss.

| Dimension | Value |
|-----------|-------|
| **Reference** | IO.FE-6 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

> 💡 AVT systems trained on common presentations will perform best on common presentations and worst on rare ones. But rare presentations are exactly where clinical decision support matters most - the unusual case that benefits from accurate documentation. Long-tail performance should be a procurement question, not just average performance.

---

### IO.FE-7 🔵 Health Literacy Performance Variation

Does AVT performance vary with patient health literacy level? Medically sophisticated patients use clinical terminology that ASR handles well; patients describing symptoms in lay terms may be harder to transcribe and summarise accurately.

| Dimension | Value |
|-----------|-------|
| **Reference** | IO.FE-7 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
| **Source** | Health literacy and equity research |

**Why this tier?**

> Important equity dimension but conceptually and methodologically novel.

**Formal Definition**

```
Compare accuracy on: (1) patients using clinical terminology; (2) patients using lay terms for the same conditions. Performance Gap = accuracy_clinical_terms - accuracy_lay_terms. Significant gap indicates the system rewards health literacy - an equity concern.
```

**Limitations**

> Health literacy is hard to measure. Distinguishing 'lay terms' from 'clinical terms' is not always clean.

**Novel Thinking / Implications**

> 💡 If AVT performs better when patients use clinical language, the system rewards health literacy and disadvantages patients who describe symptoms in everyday terms. This compounds existing health inequalities - the patients who already face barriers to healthcare get less accurate documentation as well. This is an equity dimension that single-axis demographic metrics miss.

---

---

### IO.FE-8 🔵 Cross-Platform Fairness Consistency

Whether fairness properties are consistent across multiple AVT platforms deployed within the same ICB or trust. Differential bias between vendors is itself an equity concern - if Practice A uses Vendor X (which performs well on majority populations but poorly on minority populations) and Practice B uses Vendor Y (with the opposite bias profile), patients experience different quality of documentation depending on which practice happens to serve them.

|Dimension              |Value                                                              |
|-----------------------|-------------------------------------------------------------------|
| **Reference** | IO.FE-8 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research                                     |
|**Measurement Cadence**|Periodic audit                                                     |
|**Pipeline Layer**     |Cross-cutting                                                      |
|**Assurance Question** |Fairness & Equity                                                  |
|**Measurement Method** |Computational                                                      |
|**Lifecycle Phases**   |Periodic Audit                                                     |
|**Responsible Actors** |Regional (ICB), National Body                                      |
|**Maturity**           |Proposed / Novel                                                   |
|**Outcome Type**       |Distal                                                             |
|**Applicability**      |General Healthcare AI                                              |
|**Source**             |Extension of existing Cross-Practice Variance Coefficient into equity dimension|

**Why this tier?**

> Regional or national metric. Requires cross-vendor evaluation on equivalent test data. Only meaningful where multiple platforms are deployed across an integrated care system.

**Formal Definition**

```
For each vendor v in the ICB's deployed platforms: compute demographic-disaggregated performance profile P_v. Cross-Platform Fairness Consistency = variance of P_v across vendors for each demographic group. High variance = patients experience differential fairness depending on which practice (and which vendor) they attend. Report per demographic group; worst-case group determines the equity-consistency floor for the ICB.
```

**Limitations**

> Requires standardised test data available for use against multiple vendors - which currently doesn't exist for NHS. Vendors may resist independent cross-comparison. Aggregation across practices raises information governance questions.

**Novel Thinking / Implications**

> 💡 The current NHS AVT landscape allows ICBs to have multiple vendors deployed across their patch. If those vendors have different fairness profiles, the ICB is effectively running an uncontrolled experiment where patient outcomes depend on which GP they happened to register with. This is invisible to single-vendor fairness metrics and can only be detected by cross-platform comparison. Commissioning should consider fairness consistency as a portfolio-level property, not just a single-vendor property.

### GV.SG-1 🟢 Model Version Tracking

Logging which model version produces each output. Foundation for all continuous metrics - without it, performance changes are uninterpretable.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SG-1 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | Keyes et al., Stanford, Dec 2025 |

**Why this tier?**

> Foundation for all continuous assurance. Without knowing which model version produced which output, no performance change is interpretable. Must be contractually required.

**Formal Definition**

```
Per inference: log model_id, model_version, timestamp, config_hash. On change (v_old → v_new), monitoring window W with duration Δt calibrated for statistical power ≥0.8.
```

**Reference Standard**

> Vendor inference-logging telemetry covering every component of the deployed system that can change independently. Component list MUST include at minimum: (a) ASR model; (b) summarisation/LLM model weights; (c) system prompt / instruction template; (d) retrieval indices or RAG corpora; (e) safety classifier or guardrail models; (f) any fine-tuning adapter or LoRA. Each component carries its own version identifier and `config_hash`. A "model update" is any change to any of the six components - not just LLM weight updates. Notification of change to the deployer is mandatory; the time between change-event and deployer notification is itself a monitored quantity.

**Operational Specification**

> - **Window:** continuous logging; per-inference granularity.
> - **Per-component versioning MANDATORY:** the six components above each have a recorded version on every inference. A single rolled-up "system version" is not Tier 1 sufficient - downstream incident attribution requires component-level provenance.
> - **Change-event log MANDATORY:** every change to any component generates a structured change-event record with component name, old version, new version, change type (weights / prompt / retrieval / classifier), timestamp, and notification status (notified / not-yet-notified).
> - **Notification timeline MANDATORY:** the time between change-event and deployer notification is recorded per change-event; aggregate notification latency reported monthly. Deployer-side, the notification triggers the [GV.SG-2 Model Update Impact Score](#gv-sg-2) workflow and the monitoring window referenced in the Formal Definition.
> - **Regulatory cross-link MANDATORY:** any change classified as "substantial" under MHRA Post-Market Surveillance regulations must be flagged in the change-event record with the regulatory reference, and surfaced through [GV.VT-1 Model Change Notification Compliance](#gv-vt-1).

**Threshold Guidance**

> ⚠️ **Provenance:** the three-layer surveillance framing carries from the Novel Thinking section and Keyes et al. 2025; the MHRA PMS regulatory tie-in derives from SI 2024 No. 1368 in force from 16 June 2025. Specific numerical thresholds (24-hour notification target, 14-day notification escalation, 100 % per-component versioning gate) are **proposed in v3.4 as starting points**, not externally validated. Indicative; require local calibration against contractual SLA before procurement use.
>
> - **Pre-deployment gate:** vendor demonstrates per-component versioning on a representative sample of inferences; change-event log schema documented; notification process documented and contractually committed.
> - **Continuous monitoring:** per-inference component-version coverage = 100 % (any inference missing a versioned component is a defect, not a rate); median deployer-notification latency ≤ 24 hours from change-event; alert if any change-event remains unnotified > 7 days.
> - **Pause / escalation trigger:** any inference produced without complete per-component version log; OR any change-event unnotified > 14 days; OR any "substantial" MHRA-PMS-relevant change deployed without prior deployer notification (this is a regulatory event, not just an operational one).

**References**

- **Stanford**: [Keyes et al. (2025)](https://arxiv.org/abs/2512.09048)

**Limitations**

> Not contractually mandated in most NHS procurement. The Operational Specification's per-component versioning requirement makes this gap visible at procurement-time but does not close it - vendors can decline to log all six components, in which case the deployer is choosing to forgo Tier 1 assurance for that part of the stack.

**Novel Thinking / Implications**

> 💡 Three-layer surveillance: detected nationally (contractual), evaluated regionally (benchmark), monitored locally (edit-pattern shift).

---

### GV.SG-2 🟡 Model Update Impact Score

Standardised before/after on update. Governance: vendor notifies → regional benchmark → local monitoring.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SG-2 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Regional (ICB) |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

### GV.SG-3 🟡 Performance Degradation Detection Latency

Time delay between the onset of model performance degradation and its detection by the monitoring infrastructure. Distinct from the existing Model Update Impact Score, which measures the effect of notified updates at a known switchover point. This metric addresses silent degradation - performance decay that occurs without any vendor notification or identifiable event, from causes including data drift, infrastructure changes, or subtle model updates that are not disclosed.

|Dimension              |Value                                                              |
|-----------------------|-------------------------------------------------------------------|
| **Reference** | GV.SG-3 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                             |
|**Measurement Cadence**|Continuous                                                         |
|**Pipeline Layer**     |Cross-cutting                                                      |
|**Assurance Question** |Safety                                                             |
|**Measurement Method** |Computational                                                      |
|**Lifecycle Phases**   |Continuous                                                         |
|**Responsible Actors** |Regional (ICB), National Body                                      |
|**Maturity**           |Proposed / Novel                                                   |
|**Outcome Type**       |Proximal                                                           |
|**Applicability**      |General Healthcare AI                                              |
|**Source**             |NICE Evidence Standards Framework 2022 AI-specific updates; drift detection literature|

**Why this tier?**

> Regional or national monitoring because detection requires aggregation across sites - single-practice data lacks statistical power to distinguish drift from noise. The detection infrastructure is the binding constraint; the metric itself is straightforward once infrastructure exists.

**Formal Definition**

```
Detection Latency = t_detection - t_degradation_onset. Requires: (1) continuous measurement of sentinel metrics against a stable reference; (2) statistical drift detection (CUSUM, Page-Hinkley, or equivalent sequential testing); (3) pre-specified threshold for declaring drift. Report Latency distribution across detected drift events. Target: detection within 4 weeks of onset for clinically significant degradation.
```

**Limitations**

> Requires stable reference benchmarks that don't drift with the model. Small drift signals are hidden by consultation case-mix variation. Attribution of detected drift to model changes vs environmental changes is often ambiguous.

**Novel Thinking / Implications**

> 💡 Silent degradation is the failure mode that notified update monitoring cannot catch. A vendor pushing incremental improvements, a cloud infrastructure change that affects inference behaviour, or gradual model quality decay from training data drift - none of these trigger Model Version Tracking but all can cause clinically significant performance change. Detection latency is the metric that tells you whether your monitoring would actually catch a silent failure before it caused harm. A system with excellent monitoring coverage but 6-month detection latency is operationally fragile.

---

### GV.SG-4 🟡 Retraining Trigger Threshold Specification

Pre-defined, quantitative criteria specifying the conditions under which a model must be retrained or recalibrated. Required by FDA Predetermined Change Control Plans (PCCP, December 2024) for AI-enabled medical devices, and aligned with NICE ESF 2022's AI-specific requirements. Distinct from the existing Model Update Impact Score (which measures impact of executed updates) - this metric assesses whether the trigger logic for when updates should occur is even specified.

|Dimension              |Value                                                             |
|-----------------------|------------------------------------------------------------------|
| **Reference** | GV.SG-4 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                            |
|**Measurement Cadence**|One-off gate                                                      |
|**Pipeline Layer**     |Cross-cutting                                                     |
|**Assurance Question** |Safety                                                            |
|**Measurement Method** |Human Review                                                      |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                    |
|**Responsible Actors** |Vendor                                                            |
|**Maturity**           |Emerging                                                          |
|**Outcome Type**       |Proximal                                                          |
|**Applicability**      |General Healthcare AI                                             |
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

> 💡 The FDA PCCP framework represents a regulatory shift from "approve the specific model" to "approve the change control process that governs model evolution". For AVT, where continuous improvement is assumed, this shift is essential - but only works if the change control process is specified, auditable, and followed. A vendor without a PCCP-equivalent framework is effectively promising that their model will never need updating, or that updating decisions will be made ad hoc. Neither is credible for a production clinical system.

---

### GV.SG-5 🔵 AI-Generated Data Contamination Rate

The proportion of training or fine-tuning data that is itself AI-generated clinical content - either directly (notes written by earlier versions of the same AVT system used to train successors) or indirectly (clinical records that have been shaped by AI suggestions even where the final text was human-edited). Known in the machine learning literature as "model autophagy disorder" or "MAD". A medRxiv 2026 study of iterative training on AI-generated clinical content reported vocabulary collapse of 98.9% by generation 4 and effective disappearance of rare clinical findings.

|Dimension              |Value                                                                                            |
|-----------------------|-------------------------------------------------------------------------------------------------|
| **Reference** | GV.SG-5 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research                                                                   |
|**Measurement Cadence**|Periodic audit                                                                                   |
|**Pipeline Layer**     |Cross-cutting                                                                                    |
|**Assurance Question** |Safety                                                                                           |
|**Measurement Method** |Human Review                                                                                     |
|**Lifecycle Phases**   |Periodic Audit                                                                                   |
|**Responsible Actors** |Vendor, National Body                                                                            |
|**Maturity**           |Emerging                                                                                         |
|**Outcome Type**       |Distal                                                                                           |
|**Applicability**      |General Healthcare AI                                                                            |
|**Source**             |medRxiv 2026 model autophagy study; Shumailov et al. curse of recursion literature             |

**Why this tier?**

> Systemic risk affecting the entire AVT ecosystem. Cannot be measured by any individual deployer. National body responsibility - and specifically a question that the NHS should pose to any vendor who fine-tunes on deployed clinical data.

**Formal Definition**

```
Contamination Rate = |training_examples_derived_from_AI_generated_content| / |total_training_examples|. Direct contamination: training data includes AI-generated clinical notes. Indirect contamination: training data includes human-approved notes that were initially AI-drafted (where the AI fingerprint remains). Assessment methodology: (1) vendor attestation of training data provenance; (2) statistical detection of AI fingerprints in training corpora; (3) vocabulary drift analysis comparing successive model generations on stable held-out test sets.
```

**Limitations**

> Detecting AI-generated content in training data is an unsolved problem - watermarking proposals are not yet standardised. Vendor attestation is self-reported. Longitudinal monitoring requires visibility into vendor training pipelines that is rarely contractually granted.

**Novel Thinking / Implications**

> 💡 Every NHS trust deploying AVT is a data generation site. If vendors fine-tune on deployed clinical data (a common practice for improvement), NHS content flows back into the training pipeline. Over multiple training cycles, this creates a feedback loop where the model is increasingly trained on its own output - the vocabulary collapse and rare-event disappearance finding becomes a direct patient safety risk because rare clinical presentations are exactly where documentation accuracy matters most. This is the AVT-specific version of what the ML literature calls "the curse of recursion", and it's a systemic risk that requires national-level intervention rather than deployer-level monitoring.

---

### GV.SG-6 🔵 Concept Drift in Clinical Notes

Statistical detection of drift in the distribution of clinical concepts present in AI-generated notes over time. Concept drift can occur for legitimate reasons (true population shifts, new conditions, changed coding practice) or problematic reasons (model degradation, training data contamination, prompt drift). The metric doesn't distinguish legitimate from problematic - that requires human judgment - but it makes drift visible so it can be investigated.

|Dimension              |Value                                                    |
|-----------------------|----------------------------------------------------------|
| **Reference** | GV.SG-6 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research                            |
|**Measurement Cadence**|Continuous                                                |
|**Pipeline Layer**     |Cross-cutting                                             |
|**Assurance Question** |Meta-evaluation                                           |
|**Measurement Method** |Computational                                             |
|**Lifecycle Phases**   |Continuous                                                |
|**Responsible Actors** |Regional (ICB), National Body, Academic                   |
|**Maturity**           |Proposed / Novel                                          |
|**Outcome Type**       |Distal                                                    |
|**Applicability**      |General Healthcare AI                                     |
|**Source**             |Concept drift literature from ML monitoring applied to clinical NLG|

**Why this tier?**

> Requires statistical infrastructure and cross-site aggregation for meaningful signal. National or regional responsibility.

**Formal Definition**

```
For each reference time window W_ref and comparison window W_t: compute the distribution of SNOMED concepts (or other structured clinical categories) present in AI-generated notes. Drift = KL divergence or earth mover's distance between distributions. Threshold for investigation: drift > 2σ from historical seasonal variation. Report per concept category - aggregate drift obscures category-specific shifts. Specifically monitor: rare diagnoses, psychosocial content, safety-netting language, safeguarding flags.
```

**Limitations**

> Distinguishing concept drift from case-mix drift requires population-level context. Seasonal variation (respiratory conditions in winter, mental health referrals in January) creates baseline noise. Rare concepts have high variance even without true drift.

**Novel Thinking / Implications**

> 💡 The most worrying drift signal is concepts that progressively disappear - safeguarding language, mental health content, social context - because the disappearance may indicate the model has learned to deprioritise these categories over time through training data feedback loops. If an AVT system in year 3 documents less psychosocial content than the same system in year 1 despite similar patient populations, something has shifted in what the system considers "clinical content worth recording". This is exactly the kind of drift that aggregate performance metrics cannot detect.

### GV.SG-7 🔵 Probabilistic Risk Quantification (P₁/P₂)

Medical device safety paradigm for LLMs. First quantitative risk analysis: P₁ from 2.0×10⁻⁸ to 2.6×10⁻⁴.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SG-7 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
| **Source** | medRxiv, Nov 2025 |

**Why this tier?**

> Research methodology. First published PRA for LLM-SaMD. Important for DCB0129 maturity but requires clinical harm pathway modelling that doesn't yet exist for AVT.

**Formal Definition**

```
P₁ = P(hazardous output | normal use). P₂ = P(harm | hazardous output). Risk R = P₁ × P₂ × Severity. P₂ requires clinical harm pathway modelling with probability attenuation at each stage.
```

**References**

- **Preprint**: medRxiv, Nov 2025 - 14 open-source LLMs

**Limitations**

> Validated on open-source only. Commercial AVT = black box.

**Novel Thinking / Implications**

> 💡 For DCB0129: translating error rates into P₁/P₂ makes safety cases quantitative, not just qualitative.

---

### GV.SG-8 🔵 DeepScore (Defect-Free Rate)

Two-tier: Major Defect-Free Rate + Critical Defect-Free Rate. 135,900 notes. Sound approach but proprietary definitions.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SG-8 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Vendor-Proprietary |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | DeepScribe |

**Why this tier?**

> Vendor-proprietary (DeepScribe). Sound two-tier severity approach but proprietary definitions prevent cross-vendor comparison.

**Formal Definition**

```
MDFR = |N_no_major| / |N_total|. CDFR = |N_no_critical| / |N_total|. Vendor-specific severity definitions - not aligned to external standard.
```

**References**

- **DeepScore**: DeepScribe, arXiv Sept 2024

**Limitations**

> Proprietary severity definitions. Human QA in enterprise tier conflates AI + human performance.

**Novel Thinking / Implications**

> 💡 CREOLA taxonomy is best candidate for common severity framework.

---

### GV.SG-9 🟢 Safety Performance Indicators with Thresholds (DSCMS)

Metrics + thresholds + escalation = governance. A metric without a threshold is information; with a threshold and action it becomes governance.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SG-9 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer, Regional (ICB) |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

### GV.SG-10 🟡 Off-Label Use Detection Rate

AVT use outside validated contexts. Well-intentioned scope creep - each boundary crossing compounds risk.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SG-10 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

**⚠️ Underspecification Warning (Tier A - no established methodology)**

> Off-label use of AVT has **no established detection methodology** in the published literature. The concept borrows from pharmaceutical regulation, but AVT "indicated use" boundaries are rarely defined precisely enough to determine when specific use is off-label. A 2025 Morgan Lewis legal analysis highlighted the liability risk but provided no detection framework. No use-case taxonomy exists to define intended vs off-label boundaries. No monitoring approach has been proposed in peer-reviewed literature. This metric requires definitional work before operational implementation is possible: deployers should, in collaboration with vendors, specify the validated use envelope (specialties, patient populations, acuity levels, languages, consultation modes) and build usage-pattern monitoring against that envelope rather than attempting to measure "off-label use" as an isolated concept. Consider operationalising as the proposed **Work-as-Imagined vs Work-as-Done Gap** metric (Human Factors & Workflow) which provides a more structured framework for detecting adaptation, workaround, and scope creep.

**Novel Thinking / Implications**

> 💡 Automated detection feasible if validated envelope is machine-readable.

---

### GV.SG-11 🟢 Adverse Event / Incident Rate (LFPSE)

National patient safety reporting. Ultimate lagging indicator. No specific LFPSE category for AI/AVT incidents exists.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SG-11 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer, National Body |
| **Maturity** | Established |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
| **Source** | LFPSE national reporting |

**Why this tier?**

> Established national reporting. The ultimate lagging indicator - by the time this metric moves, harm has occurred. Needs dedicated LFPSE category for AI/AVT incidents.

**Formal Definition**

```
IR = N_incidents / N_encounters. Stratify by severity. Currently no LFPSE taxonomy code for AI/AVT - coded under general documentation errors.
```

**References**

- **LFPSE**: NHS Learn From Patient Safety Events

**Limitations**

> Massive under-reporting. No specific AI/AVT category. Unknown denominator.

**Novel Thinking / Implications**

> 💡 Dedicated LFPSE reporting category needed for this to function as national signal.

---

### GV.SG-12 🟡 Cross-Practice Variance Coefficient

Performance variation across practices within ICB. High variance = context-dependent performance. Justifies regional assurance tier.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SG-12 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Regional (ICB) |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

### GV.SG-13 🟢 Assurance Debt Accumulation Rate

Gap between required and completed assurance. The honest metric - better visible and managed than hidden until incident.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SG-13 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer, Regional (ICB) |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
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

### GV.SG-14 🟢 Near-Miss Reporting Rate

Incidents caught by clinician review before reaching the EPR. The leading indicator that LFPSE rate is the lagging indicator of. A high near-miss rate with low LFPSE rate suggests the human review layer is functioning; a low near-miss rate may indicate either an excellent system or inadequate review.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SG-14 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | Patient safety leading vs lagging indicator literature |

**Why this tier?**

> Essential leading indicator. Should be Tier 1 because it's the early warning system that LFPSE is the lagging indicator of. Requires lightweight reporting infrastructure.

**Formal Definition**

```
Near-Miss Rate = |errors_caught_in_review| / |total_AI_outputs|. Track separately from LFPSE incidents (errors that reached the record). Healthy ratio: high near-miss rate, low LFPSE rate. Concerning ratio: low near-miss rate, any LFPSE incidents.
```

**Reference Standard**

> Two distinct sources MUST be combined to construct the numerator:
>
> - **Active reports:** clinician-submitted near-miss reports through a deployer-provided reporting mechanism (in-product button, EPR form, or dedicated channel)
> - **Inferred near-misses:** safety-critical edits detected by [HL.HF-1 Edit Rate](#hl-hf-1)'s severity stratification — substantive edits flagged as safety-critical (allergy / medication / dose / red-flag / diagnosis / plan changes between AI output and clinician signature) constitute presumptive near-misses
>
> Both are required because active-only reporting under-counts (clinicians under busy conditions edit-and-move-on without reporting), and edit-only inference over-counts (some safety-critical edits are stylistic refinements not error corrections). Cross-validate the two sources monthly; ratio of active-to-inferred is itself a safety-culture signal. The denominator is total AI outputs reaching clinician review (excludes outputs aborted before review per [HL.HF-9 Re-record / Abandonment Rate](#hl-hf-9)).

**Operational Specification**

> - **Window:** continuous; weekly aggregate per practice and per clinician.
> - **Population:** all AVT-generated outputs reviewed by clinicians during the window.
> - **Two-source reporting MANDATORY:** active near-miss rate and inferred near-miss rate reported separately, with composite headline rate = max(active, inferred) where the two sources contradict (the higher source is the more conservative safety estimate). Cross-validation report monthly with the active-to-inferred ratio.
> - **Severity classification MANDATORY:** near-misses classified by clinical category (allergy / medication / red-flag / diagnosis / plan / other) parallel to [HL.HF-1](#hl-hf-1) severity stratification. Per-category breakdown reported.
> - **Pairing with LFPSE rate MANDATORY:** the metric's value is in the conjunction with [GV.SG-11 Adverse Event / Incident Rate (LFPSE)](#gv-sg-11). Headline reporting MUST include both rates and the ratio. A near-miss rate reported without the LFPSE rate is not Tier 1 sufficient — neither alone interprets safety culture.
> - **No-blame culture check:** if active reporting rate is < 25 % of inferred rate sustained two months, this is a safety-culture flag (clinicians editing-without-reporting), not a metric failure. Triggers a separate qualitative review.

**Threshold Guidance**

> ⚠️ **Provenance:** the leading-vs-lagging indicator framing carries from the patient safety literature cited in Source. The two-source construction (active + inferred via [HL.HF-1](#hl-hf-1)) is **proposed in v3.5** as a way to address the well-documented under-reporting problem in clinical near-miss capture. Specific numerical thresholds (25 % active-to-inferred floor, ratio thresholds vs LFPSE) are **proposed in v3.5 as starting points**, not externally validated. Indicative; require local calibration against safety-culture baseline before contractual use.
>
> - **Pre-deployment / Day Zero baseline:** establish baseline active near-miss rate and inferred near-miss rate during the first 4 weeks; record per-category breakdown; pair with concurrent LFPSE rate.
> - **Continuous monitoring:** weekly two-source reporting; monthly cross-validation; alert when active-to-inferred ratio < 25 % sustained two months (under-reporting culture flag); alert when near-miss-to-LFPSE ratio falls (rising LFPSE without rising near-miss = review layer is failing, not improving).
> - **Pause / escalation trigger:** LFPSE rate rises while near-miss rate stays flat or falls (the leading indicator should rise BEFORE the lagging indicator if review is functioning); OR safety-critical-category near-miss rate falls > 50 % from baseline without corresponding documented system improvement (suggests complacency, cross-link [HL.HF-1 Edit Rate](#hl-hf-1) trajectory).

**Limitations**

> Requires clinicians to actively report near-misses, which is often under-reported in busy clinical practice. The two-source Operational Specification (active + inferred via edit telemetry) addresses this directly — the inferred channel doesn't depend on active reporting — but introduces its own risk that some safety-critical edits are stylistic rather than error-corrections, leading to over-counting. The active-to-inferred ratio is a deliberate safety-culture diagnostic in this context, not just a measurement-error indicator.

**Novel Thinking / Implications**

> 💡 The leading indicator: by the time LFPSE moves, harm has occurred. Near-miss reporting catches errors before they cause harm - but only if there's a low-friction reporting mechanism and a no-blame culture. The ratio of near-miss to actual incidents is itself diagnostic of safety culture.

---

### GV.SG-15 🟡 Time-to-Correct

When an AVT error is detected, how quickly is it corrected and the lessons disseminated? Measures the responsiveness of the governance loop from detection to action.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SG-15 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

> 💡 A long time-to-correct means errors persist in the system and may affect multiple patients before resolution. This is operationally important - a single error is bad, but a single error that took 3 weeks to correct is a governance failure.

---

### GV.SG-16 🟡 SPI Escalation Response Time

When an SPI threshold is breached, how quickly does the governance response actually occur? Measures whether the SPI framework is operationally functional or just a paper exercise.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SG-16 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer, Regional (ICB) |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

### GV.SG-17 🟢 Hazard Log Completeness

DCB0129 requires a hazard log. Is it actually maintained and updated as new failure modes are discovered operationally? A static hazard log written at deployment and never updated is a compliance failure with safety implications.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SG-17 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

> Requires connecting operational monitoring to hazard log update process - often disconnected in current practice.

**Novel Thinking / Implications**

> 💡 DCB0129 hazard logs are often written once at deployment and forgotten. As operational monitoring discovers new failure modes (through edit pattern analysis, near-miss reporting, incident investigation), these should be added to the hazard log with mitigations. A hazard log that hasn't been updated in 6 months is either a perfect system or a compliance failure - and almost certainly the latter.

---

### GV.CR-1 🟢 Patient Dissent Recording Rate

Per-encounter rate at which patient objections or dissent to AVT use are recorded and respected. Distinct from the existing Patient Opt-Out Rate, which is aggregate and applies at the registration or consent level. Patient Dissent Recording is the per-encounter process compliance metric: when a patient objects at the point of care, is that objection documented, is AVT actually paused for that encounter, and is the objection respected in subsequent encounters without re-litigation.

|Dimension              |Value                                                  |
|-----------------------|--------------------------------------------------------|
| **Reference** | GV.CR-1 |
|**Priority Tier**      |🟢 Tier 1 - Minimum Viable                              |
|**Measurement Cadence**|Continuous                                              |
|**Pipeline Layer**     |Cross-cutting                                           |
|**Assurance Question** |Patient Experience                                      |
|**Measurement Method** |Passive Observational                                   |
|**Lifecycle Phases**   |Continuous                                              |
|**Responsible Actors** |Deployer                                                |
|**Maturity**           |Established                                             |
|**Outcome Type**       |Proximal                                                |
|**Applicability**      |General Healthcare AI                                   |
|**Source**             |NHSE IG guidance on ambient scribing (March 2026)       |

**Why this tier?**

> Direct compliance requirement under NHSE IG guidance. Deployer-measurable from workflow records. Binary compliance - a patient dissent not recorded and respected is a regulatory and ethical failure.

**Formal Definition**

```
Recording Rate = |dissent_events_with_recorded_and_respected_objection| / |total_dissent_events|. Target: 100%. Sub-metrics: (a) dissent documentation rate (was it recorded?); (b) dissent respect rate (was AVT paused?); (c) dissent persistence rate (was it respected in subsequent encounters?). Any sub-metric below 100% indicates compliance failure.
```

**Reference Standard**

> Authoritative source: the EPR consultation record + AVT activation telemetry. A "dissent event" is any patient communication declining AVT use at the point of care, captured by one of:
>
> - **Explicit verbal objection** logged by the clinician in the consultation record (free-text or structured field; structured preferred)
> - **Structured opt-out indicator** set in the patient record at or before the encounter (must propagate to AVT activation - see [IO.PX-1 Patient Opt-Out Rate](#io-px-1))
> - **Patient-initiated AVT termination mid-consultation** signalled to the clinician
>
> Implicit / inferred dissent (patient appears uncomfortable, clinician guesses) is out of scope for this metric and belongs under separate human-factors observation. "Respected" means AVT was not active at any point after the dissent event during that encounter or in subsequent encounters until the patient affirmatively reverses the dissent. Reversal MUST be documented separately; absence of new dissent ≠ reversal.

**Operational Specification**

> - **Window:** continuous, monthly compliance reporting per practice / per clinician.
> - **Population:** all AVT-eligible consultations during the window. Denominator includes encounters where the patient *could* have dissented (i.e. AVT was offered or activated), not just encounters where dissent occurred.
> - **Sub-metric breakdown MANDATORY:** the three sub-metrics (documentation, respect, persistence) reported separately; aggregate-only reporting is not Tier 1 sufficient.
> - **Per-clinician disaggregation MANDATORY:** dissent compliance hides at clinician level. A practice 95 % aggregate may hide one clinician at 50 %.
> - **Dissent-detection coverage check:** if recorded dissent rate is < 0.5 % of AVT-eligible consultations, the deployer must run a sampling check (clinician self-report or patient survey) to verify the low rate reflects actual patient acceptance rather than under-detection.

**Threshold Guidance**

> ⚠️ **Provenance:** the IG-incident reportability framing follows from NHSE IG guidance (March 2026) and the single-instance dissent-not-respected escalation reflects the binary-compliance logic in the Why-this-tier section. Specific numbers (≥ 99 % monthly sub-metric compliance, < 95 % escalation trigger, < 0.5 % coverage-check threshold) are **proposed in v3.3 as starting points**, not externally validated. Indicative; require local calibration before contractual use.
>
> - **Pre-deployment gate:** EPR / AVT integration capable of recording dissent in a structured form and propagating it to subsequent encounters; consultation workflow includes a documented step at which the clinician offers AVT and records the response.
> - **Continuous monitoring:** documentation, respect, and persistence sub-metrics each ≥ 99 % monthly; alert on any single dissent-not-respected event.
> - **Pause / escalation trigger:** any dissent-not-respected event confirmed (single instance), OR sub-metric < 95 % in any month. Both reportable as IG incidents.

**Limitations**

> Detection of dissent events requires clinician reporting or structured capture in the EPR workflow. Silent non-compliance (clinician uses AVT despite patient objection) is invisible to passive observation. The dissent-detection coverage check in the Operational Specification provides a partial counter to this by requiring sampling-based verification when recorded dissent is implausibly low.

**Novel Thinking / Implications**

> 💡 This is the per-encounter teeth behind the aggregate opt-out metric. Opt-out gives the patient a blanket choice; dissent recording ensures the choice is honoured at each specific consultation where it matters. The two metrics measure different things: opt-out measures consent model acceptance; dissent recording measures procedural integrity at the point of care. Both are necessary for a coherent consent architecture.

---

### GV.CR-2 🟢 Verbal Notification Compliance

Proportion of AVT-using consultations where verbal notification was delivered to the patient at session start, as required by NHSE IG guidance (March 2026). Consent model in NHS primary care relies on informing patients before AVT activation, but the "informing" step is often poorly observed in busy practice. This metric measures the actual delivery of notification, not just the existence of a notification policy.

|Dimension              |Value                                                    |
|-----------------------|----------------------------------------------------------|
| **Reference** | GV.CR-2 |
|**Priority Tier**      |🟢 Tier 1 - Minimum Viable                                |
|**Measurement Cadence**|Periodic audit                                            |
|**Pipeline Layer**     |Cross-cutting                                             |
|**Assurance Question** |Patient Experience                                        |
|**Measurement Method** |Hybrid                                                    |
|**Lifecycle Phases**   |Day Zero Baseline, Periodic Audit                         |
|**Responsible Actors** |Deployer                                                  |
|**Maturity**           |Established                                               |
|**Outcome Type**       |Proximal                                                  |
|**Applicability**      |General Healthcare AI                                     |
|**Source**             |NHSE IG guidance on ambient scribing (March 2026); CQC Mythbuster 109 context|

**Why this tier?**

> Direct compliance requirement. Measurable via patient survey sampling, consultation audit, or (with appropriate consent) recording sampling. Binary compliance - notification either happened or it didn't.

**Formal Definition**

```
Compliance Rate = |consultations_with_verbal_notification_delivered| / |total_AVT_consultations|. Measurement methods in order of increasing rigour: (a) clinician self-report at end of session; (b) patient survey sampling asking whether notification was delivered; (c) audit of audio recordings (where retention allows) for notification language. Target: 100%. Values below 95% indicate systematic compliance failure requiring intervention.
```

**Reference Standard**

> The deployer-approved patient notification script (drawn from NHSE IG guidance March 2026 + local DPIA). A consultation counts as "notified" only if the script's required content elements were delivered to the patient before AVT activation:
>
> - **What** the technology is (ambient scribe / AI-assisted documentation) and what it does
> - **What** is captured (audio + transcript) and where it goes
> - **Who** has access (clinician, vendor, sub-processors)
> - **How** to decline (without service consequence)
>
> A notification missing any of the four content elements counts as non-compliant even if some notification language was used. The most rigorous measurement method available at the deployment site is the gold standard; methods (a)-(c) are ranked by reliability and the headline rate must be reported with the method declared.

**Operational Specification**

> - **Window:** monthly, with quarterly periodic audit using the highest-rigour method available.
> - **Population:** all AVT consultations during the window (denominator excludes consultations where AVT was not used, including patient-opt-out cases).
> - **Method declaration MANDATORY:** the headline compliance rate carries the measurement method (self-report / patient survey / audio audit). Reporting "Compliance: 98 %" without method is not Tier 1 sufficient.
> - **Sample size for survey or audit MANDATORY:** ≥ 30 patients per clinician per quarter for survey method; ≥ 30 audio recordings per clinician per quarter where audio audit is used. Sub-30 samples are uninformative and do not satisfy the metric.
> - **Content-element breakdown MANDATORY:** report compliance per content element (what / what / who / how). A clinician who consistently omits "how to decline" is failing differently from one who omits "where it goes"; aggregate-only reporting hides the failure pattern.

**Threshold Guidance**

> ⚠️ **Provenance:** the four content-element framing (what / what / who / how) follows from NHSE IG guidance (March 2026). Specific numerical thresholds (≥ 95 % self-report, ≥ 90 % audited, ≥ 85 % per-element, < 75 % escalation, ≥ 30 sample-size floor) are **proposed in v3.3 as starting points**, not externally validated. Indicative; require local calibration before contractual use.
>
> - **Pre-deployment gate:** notification script drafted and reviewed against NHSE IG content elements; clinician training complete; one mock-consultation audit per clinician confirms script delivery.
> - **Continuous monitoring:** monthly self-report compliance ≥ 95 %; quarterly survey-based or audio-based compliance ≥ 90 % overall and ≥ 85 % on every content element.
> - **Pause / escalation trigger:** any content element < 75 % compliance in any audit cycle; or self-report > 95 % paired with audited rate < 75 % (this is a self-report integrity failure, separately serious).

**Limitations**

> Self-report over-estimates compliance. Patient recall is imperfect. Audio audit is resource-intensive and depends on retention policies that may conflict with data minimisation. The Operational Specification's method-declaration requirement makes the self-report bias visible by forcing the audited cross-check.

**Novel Thinking / Implications**

> 💡 The gap between policy and practice on patient notification is the compliance equivalent of the consent understanding gap. A practice can have a 100% notification policy and a 60% actual notification rate - and the 40% gap is where the consent model breaks down. Periodic audit is the only way to know which side of the gap a deployer is on. A practice that refuses to audit is implicitly choosing not to know.

---

### GV.CR-3 🟢 AI-Generated Content Labelling Compliance

Automated verification that AI-generated clinical record entries carry the mandatory SNOMED suffix identifying them as AVT output (e.g. "Audio Dictation 24771000000105" per NHSE guidance). Required for downstream systems to distinguish AI-generated content from clinician-authored content - essential for audit, safety investigation, and future training data curation.

|Dimension              |Value                                                     |
|-----------------------|-----------------------------------------------------------|
| **Reference** | GV.CR-3 |
|**Priority Tier**      |🟢 Tier 1 - Minimum Viable                                 |
|**Measurement Cadence**|Continuous                                                 |
|**Pipeline Layer**     |EPR Write-back                                             |
|**Assurance Question** |Meta-evaluation                                            |
|**Measurement Method** |Computational                                              |
|**Lifecycle Phases**   |Pre-deployment, Continuous                                 |
|**Responsible Actors** |Vendor, Deployer                                           |
|**Maturity**           |Established                                                |
|**Outcome Type**       |Proximal                                                   |
|**Applicability**      |General Healthcare AI                                      |
|**Source**             |NHSE IG guidance on ambient scribing (March 2026)          |

**Why this tier?**

> Automated compliance check with trivial implementation cost. Should be a pre-deployment gate and continuous monitoring metric. Non-compliance is both a governance failure and a downstream data quality problem.

**Formal Definition**

```
Labelling Rate = |AI_generated_entries_with_correct_suffix| / |total_AI_generated_entries|. Target: 100%. Zero-tolerance - every AI-generated entry must be labelled. Automated verification is feasible because the suffix is a fixed SNOMED concept that either appears or doesn't. Report non-compliance instances for immediate remediation.
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

> Assumes the vendor's write-back system supports the suffix - some EPR integrations strip metadata fields that don't map to native EPR structures. The suffix location (free-text vs metadata) affects automated detection methodology.

**Novel Thinking / Implications**

> 💡 Without reliable labelling, every downstream system that consumes clinical records is operating without knowing which content is AI-generated. This matters for: safety investigation (was the error in a human-written or AI-generated entry?); training data curation (if AI-generated records are fed back into training, the labelling is necessary to detect and exclude them); audit trails (which clinicians rely on AI assistance and how frequently). Non-labelling is an infrastructure failure with cascading consequences.

---

### GV.CR-4 🟢 AVT Supplier Registry Listing Verification

Procurement and ongoing verification that the deployed AVT system is listed on the NHS England AVT Supplier Registry and remains listed throughout the deployment lifecycle. The Registry (launched January 2026) is the NHS-level mechanism for self-certified minimum standards, and registry status is expected to become a procurement precondition.

|Dimension              |Value                                                 |
|-----------------------|------------------------------------------------------|
| **Reference** | GV.CR-4 |
|**Priority Tier**      |🟢 Tier 1 - Minimum Viable                             |
|**Measurement Cadence**|Continuous                                            |
|**Pipeline Layer**     |Cross-cutting                                         |
|**Assurance Question** |Safety                                                |
|**Measurement Method** |Human Review                                          |
|**Lifecycle Phases**   |Pre-deployment, Continuous                            |
|**Responsible Actors** |Deployer, Vendor                                      |
|**Maturity**           |Established                                           |
|**Outcome Type**       |Proximal                                              |
|**Applicability**      |AVT-Specific                                          |
|**Source**             |NHSE AVT Supplier Registry (January 2026)             |

**Why this tier?**

> Procurement gate with trivial verification cost. Should be confirmed at procurement and re-verified at contract renewal and on notification of vendor compliance events.

**Formal Definition**

```
Listing Verification: at procurement, confirm vendor is on the live Registry. Quarterly re-verification during deployment. Binary: listed or not listed. Where not listed, deployment should not proceed (pre-deployment) or should trigger formal risk review (during deployment). Also track: date of most recent vendor compliance attestation, scope of attested compliance (which AVT products are covered).
```

**Limitations**

> Registry is self-certified - listing indicates vendor attestation rather than independent verification. Listing scope may not cover all deployed AVT modules from a vendor with multiple products.

**Novel Thinking / Implications**

> 💡 The Registry's value depends on NHS bodies treating listing as a procurement precondition. If deployments proceed with non-listed vendors, the Registry becomes advisory rather than normative and loses its governance function. Making Registry verification a Tier 1 metric supports the norm that listing is expected - and creates visible data on deployment-to-listing alignment that can inform Registry policy over time.

---

### GV.CR-5 🟢 ICB Engagement Documentation

Documented evidence that the deployer engaged with their ICB digital team (or equivalent regional body) before AVT deployment, as required by the CIO/CCIO guidance (v2, January 2026). The ICB engagement requirement exists to prevent uncoordinated deployment across an integrated care system and to ensure regional intelligence about AVT risks and mitigations is applied consistently.

|Dimension              |Value                                                       |
|-----------------------|-------------------------------------------------------------|
| **Reference** | GV.CR-5 |
|**Priority Tier**      |🟢 Tier 1 - Minimum Viable                                   |
|**Measurement Cadence**|One-off gate                                                 |
|**Pipeline Layer**     |Cross-cutting                                                |
|**Assurance Question** |Meta-evaluation                                              |
|**Measurement Method** |Human Review                                                 |
|**Lifecycle Phases**   |Pre-deployment                                               |
|**Responsible Actors** |Deployer, Regional (ICB)                                     |
|**Maturity**           |Established                                                  |
|**Outcome Type**       |Proximal                                                     |
|**Applicability**      |General Healthcare AI                                        |
|**Source**             |CIO/CCIO guidance v2 (January 2026); NHS CIO priority notification|

**Why this tier?**

> Pre-deployment compliance requirement. Should be a documented gate before go-live. Failure indicates a governance process breakdown that deserves immediate correction.

**Formal Definition**

```
Engagement documentation includes: (1) formal notification to ICB digital team dated before go-live; (2) ICB response acknowledging notification; (3) any conditions or recommendations from ICB on file. Binary compliance: all three present = compliant. Missing ICB response is a flag for follow-up, not automatic non-compliance, because ICB capacity constraints may prevent timely response.
```

**Reference Standard**

> Authoritative source: the deployer's governance file plus ICB digital team's correspondence record. "Formal notification" = a written communication to the named ICB digital lead (not generic inbox) containing at minimum: vendor identity, product scope, deployment site list, intended go-live date, DPIA reference, and Clinical Safety Case reference. "ICB response" = any written acknowledgement, including auto-receipts where the ICB has explicitly designated them as acknowledgements; substantive review responses are tracked separately as "ICB conditions". A response received after go-live counts but is recorded with the latency.

**Operational Specification**

> - **Window:** one-off pre-deployment gate; quarterly re-verification when material scope changes (new sites, new vendor product, new use case).
> - **Population:** every AVT deployment by the practice / Trust / federation. The denominator is deployments, not consultations.
> - **Three sub-metrics MANDATORY:** notification-sent rate, ICB-acknowledged rate, ICB-conditions-on-file rate. Aggregate-only reporting is not Tier 1 sufficient — the three failure modes (deployer didn't notify / ICB didn't acknowledge / conditions exist but not actioned) require separate visibility.
> - **Latency reporting MANDATORY:** time-to-notification (deployment-decision to ICB notification) and time-to-acknowledgement (notification to ICB response). Latency reveals process health independently of binary compliance.
> - **Carve-out logging MANDATORY:** any deployment proceeding without ICB acknowledgement (under the capacity-constraint allowance) MUST be logged with reason and review date. Repeated unanswered notifications to the same ICB within 12 months trigger escalation to the regional CCIO, not silent acceptance.

**Threshold Guidance**

> ⚠️ **Provenance:** the three-sub-metric framing follows from the CIO/CCIO guidance v2 (January 2026) and the carve-out logic in the existing Formal Definition. Specific numerical thresholds (≥ 14-day notification lead time, escalation after two unanswered notifications in 12 months, quarterly re-verification cadence) are **proposed in v3.5 as starting points**, not externally validated. Indicative; require local calibration before contractual use.
>
> - **Pre-deployment gate:** notification sent to named ICB digital lead ≥ 14 days before planned go-live; DPIA + Clinical Safety Case referenced; deployment-site list complete.
> - **Continuous monitoring:** quarterly review of acknowledgement rate and conditions-on-file rate; alert when any ICB has > 1 unanswered notification on the deployer's books.
> - **Pause / escalation trigger:** any deployment going live without notification sent (process failure, not capacity issue); OR same ICB unanswered for ≥ 2 separate notifications within 12 months (escalate to regional CCIO).

**Limitations**

> ICB engagement quality varies - some ICBs have mature digital teams providing substantive review; others acknowledge notifications without meaningful engagement. Documentation presence does not guarantee engagement quality. The Operational Specification's separate sub-metric for ICB-conditions-on-file makes substantive engagement visible (it surfaces only when the ICB has actually reviewed), but the metric still cannot distinguish deep review from cursory acknowledgement.
>
> The escalation-to-regional-CCIO trigger in the Threshold Guidance assumes regional CCIO capacity exists to receive and act on escalations. The CIO/CCIO guidance v2 (January 2026) does not mandate or fund that capacity, so in regions where it is absent the metric's escalation pathway is non-operational — failed acknowledgements pile up at the next layer rather than being resolved. Where this is the case, deployers should document the gap in their governance file and surface it via routes other than this metric (e.g. ICS digital risk register).

**Novel Thinking / Implications**

> 💡 ICB engagement is the mechanism that prevents NHS AVT deployment from being a series of disconnected practice-level decisions with no regional coordination. It only works if it is actually happening - and practices deploying AVT without ICB engagement are a visible symptom of governance friction, ICB capacity constraints, or deployment urgency overriding process. Tracking the metric is a diagnostic tool for that friction as much as it is a compliance check.

---

### GV.CR-6 🟢 Clinical Safety Case Completeness

Existence, currency, and coverage of a formal DCB0129/0160 clinical safety case for the AVT deployment. Distinct from the existing Hazard Log Completeness metric, which covers log currency. Safety Case Completeness is the broader document: hazard identification, risk analysis, mitigations, residual risk acceptance, and governance arrangements. A 2025 FOI-based study (PubMed 41172285) found widespread non-compliance with DCB0129 requirements among NHS digital health deployments.

|Dimension              |Value                                                                                            |
|-----------------------|-------------------------------------------------------------------------------------------------|
| **Reference** | GV.CR-6 |
|**Priority Tier**      |🟢 Tier 1 - Minimum Viable                                                                        |
|**Measurement Cadence**|Periodic audit                                                                                   |
|**Pipeline Layer**     |Cross-cutting                                                                                    |
|**Assurance Question** |Safety                                                                                           |
|**Measurement Method** |Human Review                                                                                     |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                                                   |
|**Responsible Actors** |Deployer                                                                                         |
|**Maturity**           |Established                                                                                      |
|**Outcome Type**       |Proximal                                                                                         |
|**Applicability**      |General Healthcare AI                                                                            |
|**Source**             |DCB0129/0160 regulatory requirement; PubMed 41172285 FOI study of NHS digital safety standard compliance|

**Why this tier?**

> Direct regulatory requirement. Non-compliance is both a legal and a safety issue. The 2025 FOI study found widespread non-compliance, making this a known high-risk area requiring active monitoring.

**Formal Definition**

```
Completeness assessed against DCB0129 standard sections: (1) safety management system; (2) hazard identification; (3) hazard analysis and evaluation; (4) hazard control; (5) hazard log; (6) safety case report; (7) safety incident management; (8) issue resolution. Each section binary (present and current / missing or out-of-date). Full compliance requires all sections. Currency: major update triggered by significant system change, model version change, or new hazard identification.
```

**Reference Standard**

> DCB0129 (Clinical Risk Management for Health IT Systems) is the authoritative section schema for vendors / manufacturers. The deployer-side equivalent DCB0160 governs the safety case for the implementing institution and is the cross-reference for sites operating their own safety case (see also [Clinical Safety Officer reviewer requirement under DCB0129/0160]). "Present" requires a section heading plus content authored by a named Clinical Safety Officer (CSO); template-only sections (heading present, body empty or "TBC") count as missing. "Current" requires last-update date within the metric's currency window per the Operational Specification below.

**Operational Specification**

> - **Window:** annual periodic audit; mandatory re-review on any of the four trigger events (significant system change, model version change in any component per [GV.SG-1 Model Version Tracking](#gv-sg-1), new hazard identification, scope expansion).
> - **Population:** every deployment site holding a safety case (typically Trust-level for hospitals, federation-level for primary-care networks).
> - **Per-section reporting MANDATORY:** the eight sub-metrics (one per DCB0129 section) reported separately. Aggregate-only reporting is not sufficient — the failure pattern matters: a site missing section 5 (hazard log) has a different compliance failure from one missing section 7 (incident management).
> - **Currency window MANDATORY:** sections (2) hazard identification, (3) analysis, (4) control, and (5) log MUST be updated within 30 days of any trigger event (the 30-day figure is proposed in v3.5 as a starting point; DCB0129 itself does not specify a numeric window — see Threshold Guidance Provenance). Section (1) safety management system, (6) safety case report, and (8) issue resolution MUST be reviewed at least annually. Section (7) safety incident management MUST be live-current (updated on each new incident per the existing process).
> - **Trigger-event log MANDATORY:** every trigger event recorded with date, type, sections requiring update, and target completion date. Time-to-update reported per trigger.
> - **External review:** independent CSO review of the safety case at intervals not exceeding 24 months OR on any major version change of the AVT product. Internal-only review is not Tier 1 sufficient.

**Threshold Guidance**

> ⚠️ **Provenance:** the eight-section schema and currency triggers carry from DCB0129 itself. Specific numerical thresholds (30-day post-trigger window, 24-month external review cadence, 100 % per-section currency gate) are **proposed in v3.5 as starting points**, not externally validated. The 2025 PubMed FOI study (cited in Source) found widespread non-compliance; these thresholds reflect a procurement-grade interpretation of "current" rather than a regulator-published standard. Indicative; require local calibration against the deployer's clinical risk management framework before contractual use.
>
> - **Pre-deployment gate:** all eight DCB0129 sections present with named CSO author; safety case report explicitly references the AVT product version, EPR target, and deployment scope.
> - **Continuous monitoring:** annual per-section review; alert when any of sections 2-5 falls outside the 30-day post-trigger window; alert when external review is overdue.
> - **Pause / escalation trigger:** any section in "missing" state (heading present, content empty or stub); OR sections 2-5 unupdated > 90 days after a trigger event; OR any model-version change deployed without corresponding safety-case update (cross-link MHRA PMS substantial-change framework).

**Limitations**

> Compliance with structure does not guarantee quality of content. Safety cases are often written to satisfy the standard rather than to genuinely analyse system safety - the "compliance theatre" problem. External independent review is the only reliable check; the Operational Specification's 24-month external-review cadence makes this requirement explicit but does not eliminate the gap between structural compliance and genuine safety analysis.

**Novel Thinking / Implications**

> 💡 The 2025 FOI finding that many NHS digital health deployments lack DCB0129 compliance is a structural warning about regulatory enforcement gaps. AVT deployment is happening faster than safety case development in many places. Making Safety Case Completeness a Tier 1 metric both highlights the compliance obligation and creates visible data on how widespread the gap is - which is itself a governance intervention.

---

### GV.CR-7 🟢 DPIA Template Completion Rate

Proportion of AVT deployments using the NHS-provided March 2026 DPIA template with all mandatory sections completed. Data Protection Impact Assessment is required under UK GDPR Article 35 for high-risk processing, and AVT meets the high-risk threshold. The NHSE template provides standardised structure - but the template only helps if it's actually used and completed.

|Dimension              |Value                                                 |
|-----------------------|------------------------------------------------------|
| **Reference** | GV.CR-7 |
|**Priority Tier**      |🟢 Tier 1 - Minimum Viable                             |
|**Measurement Cadence**|Periodic audit                                        |
|**Pipeline Layer**     |Cross-cutting                                         |
|**Assurance Question** |Safety                                                |
|**Measurement Method** |Human Review                                          |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                        |
|**Responsible Actors** |Deployer                                              |
|**Maturity**           |Established                                           |
|**Outcome Type**       |Proximal                                              |
|**Applicability**      |General Healthcare AI                                 |
|**Source**             |UK GDPR Article 35; NHSE IG guidance template (March 2026)|

**Why this tier?**

> Legal requirement. Pre-deployment gate. Template completion is measurable and binary.

**Formal Definition**

```
Completion Rate = |deployments_with_complete_DPIA_using_template| / |total_AVT_deployments|. Template mandatory sections: processing description, lawful basis, data flows, risks identified, mitigations, residual risk acceptance, DPO sign-off, review schedule. Each section binary; complete DPIA requires all sections. Review cadence: minimum annually or on significant processing change.
```

**Reference Standard**

> The NHSE March 2026 DPIA template is the authoritative section schema for AVT deployments; UK GDPR Article 35 is the legal floor. "Complete" requires every mandatory section populated with substantive content, signed off by the named Data Protection Officer (DPO). Template-only sections (heading present, body empty, "TBC", or boilerplate copied from the template's example text) count as incomplete. Cross-link to [GV.CR-6 Clinical Safety Case Completeness](#gv-cr-6) — DPIA risks identified MUST be reconcilable with hazards in the safety case; gaps between the two are themselves a quality signal.

**Operational Specification**

> - **Window:** annual periodic audit; mandatory re-review on significant processing change (defined: new vendor, new data flow, new sub-processor, new use case, model component change per [GV.SG-1](#gv-sg-1), site expansion).
> - **Population:** every AVT deployment (denominator: deployments, not consultations).
> - **Per-section reporting MANDATORY:** the eight mandatory sections (processing description, lawful basis, data flows, risks identified, mitigations, residual-risk acceptance, DPO sign-off, review schedule) reported separately. Aggregate-only reporting hides sectional failure patterns.
> - **Significant-change definition MANDATORY:** the deployer's local definition of "significant processing change" must be documented; ambiguity here is a common failure mode for the metric. Default rule: any change requiring sub-processor disclosure update under [GV.VT-7](#gv-vt-7) is significant by definition.
> - **DPO sign-off MANDATORY (binary):** unsigned DPIAs do not count as complete regardless of section content. Sign-off date recorded; sign-offs preceding the most recent significant change are stale.
> - **Cross-reconciliation with safety case:** DPIA-identified risks MUST be cross-mapped to safety-case hazards; risks named in DPIA but absent from safety case (or vice versa) are flagged in the audit output.

**Threshold Guidance**

> ⚠️ **Provenance:** the eight-section schema and DPO sign-off requirement carry from UK GDPR Article 35 and the NHSE March 2026 template. Specific numerical thresholds (annual audit cadence, 30-day post-significant-change re-review window, 100 % per-section gate) are **proposed in v3.5 as starting points**, not externally validated. Indicative; require local calibration against the deployer's IG framework before contractual use.
>
> - **Pre-deployment gate:** all eight template sections complete with substantive content; DPO sign-off dated within the 30 days preceding go-live; DPIA-safety-case reconciliation documented.
> - **Continuous monitoring:** annual completion-rate review; alert on any DPIA where sign-off precedes the most recent significant change; alert when DPIA-safety-case reconciliation reveals unaligned risk/hazard list.
> - **Pause / escalation trigger:** any deployment going live without a DPO-signed DPIA (legal failure, not process); OR any DPIA stale > 12 months past a significant change without re-review (regulatory exposure).

**Limitations**

> Template compliance doesn't guarantee substantive risk analysis. "Completed" DPIAs that list "no residual risks identified" for a novel AVT deployment are likely inadequate regardless of template adherence. The Operational Specification's reconciliation-with-safety-case requirement creates a partial check on substantive quality (a DPIA that names no risks while the safety case names hazards is automatically flagged), but the gap between section-completion compliance and genuine analysis remains.

**Novel Thinking / Implications**

> 💡 The NHSE template provides common structure across deployments, which has three benefits: (1) makes comparison possible across sites, (2) ensures mandatory considerations aren't missed, (3) creates an evidence base for national-level risk analysis. Template non-use isn't necessarily non-compliance with UK GDPR (bespoke DPIAs can be legitimate) but it loses the aggregation benefit. Tracking template use rate is a proxy for how consistently the governance infrastructure is being built.

---

### GV.CR-8 🟡 DSPA Status

Existence and currency of Data Sharing/Processing Agreements with all data processors involved in AVT operation. UK GDPR Article 28 requires written agreements with processors, and cloud-hosted AVT typically involves multiple processors (primary vendor, cloud provider, model provider, annotation services). Related to the existing Sub-Processor Transparency metric but specifically focuses on the contractual agreements rather than the disclosure of sub-processors.

|Dimension              |Value                                         |
|-----------------------|----------------------------------------------|
| **Reference** | GV.CR-8 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                        |
|**Measurement Cadence**|Periodic audit                                |
|**Pipeline Layer**     |Cross-cutting                                 |
|**Assurance Question** |Safety                                        |
|**Measurement Method** |Human Review                                  |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                |
|**Responsible Actors** |Deployer, Vendor                              |
|**Maturity**           |Established                                   |
|**Outcome Type**       |Proximal                                      |
|**Applicability**      |General Healthcare AI                         |
|**Source**             |UK GDPR Article 28; NHS data protection guidance|

**Why this tier?**

> Legal compliance requirement. Annual audit recommended. Slightly lower tier than DPIA because absence of DSPA is more commonly an oversight than a structural governance failure - but still a legal requirement.

**Formal Definition**

```
DSPA Status per processor: (a) agreement in place (binary); (b) agreement currency (signed within last 2 years or since last significant change); (c) agreement covers all processing activities actually performed by that processor; (d) UK GDPR Article 28 mandatory clauses present. Full compliance requires all four per processor. Aggregate metric: |processors_fully_compliant| / |total_processors|.
```

**Limitations**

> Agreement existence doesn't guarantee processor compliance with the agreement. Cross-border processors may have limited enforceability. Complex sub-processor chains make coverage verification difficult.

**Novel Thinking / Implications**

> 💡 DSPAs are where the legal rubber meets the road. A deployer with a DPIA but no DSPAs has documented the risks without contractually binding the processors to manage them. This is a common gap because DPIAs are visible in NHS audit processes while DSPAs are often handled by legal departments outside the IG team's line of sight.

---

### GV.CR-9 🟡 FDA PCCP-Equivalent Pre-Defined Acceptance Criteria

Whether the vendor has pre-specified quantitative acceptance criteria that any model update must meet before being deployed to production. FDA Predetermined Change Control Plans (finalised December 2024) require this for US-market medical device AI. Even in UK-only deployments, it matters because: (1) EU-market vendors cascade similar requirements through the EU AI Act, and (2) the existence of pre-defined acceptance criteria is a proxy for mature change control regardless of regulatory jurisdiction.

|Dimension              |Value                                                   |
|-----------------------|---------------------------------------------------------|
| **Reference** | GV.CR-9 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                   |
|**Measurement Cadence**|One-off gate                                             |
|**Pipeline Layer**     |Cross-cutting                                            |
|**Assurance Question** |Safety                                                   |
|**Measurement Method** |Human Review                                             |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                           |
|**Responsible Actors** |Vendor                                                   |
|**Maturity**           |Emerging                                                 |
|**Outcome Type**       |Proximal                                                 |
|**Applicability**      |General Healthcare AI                                    |
|**Source**             |FDA PCCP guidance (December 2024); EU AI Act Article 15; NICE ESF 2022 AI updates|

**Why this tier?**

> Procurement assessment. Should be standard due diligence for any AVT acquisition. Vendors without PCCP-equivalent frameworks are a higher governance risk.

**Formal Definition**

```
Assessment against criteria: (1) Performance acceptance thresholds pre-specified and quantitative; (2) Regression test suite defined and maintained; (3) Fairness/equity criteria included in acceptance testing; (4) Rollback procedure specified if update fails acceptance post-deployment; (5) Documentation of acceptance decisions available for audit. Binary per criterion; full compliance = all five.
```

**Limitations**

> Vendors may claim PCCP equivalence without independent verification. The substantive quality of acceptance criteria matters more than their existence - a criterion like "WER not more than 20% worse" technically exists but provides no meaningful safety floor.

**Novel Thinking / Implications**

> 💡 PCCP is a structural shift in how AI medical devices are regulated - from approving specific models to approving the change control process. For AVT specifically, this is essential because continuous model improvement is expected, and ad-hoc change control makes every update a regulatory event. NHS procurement should treat PCCP-equivalent frameworks as the baseline expectation, not a differentiator, even though the formal PCCP framework applies to US-market devices.

---

### GV.CR-10 🟡 EU AI Act Event Logging Compliance

Compliance with EU AI Act Article 12 automatic event logging requirements for high-risk AI systems. High-risk provisions became effective August 2026. Applies to any AVT vendor with EU market exposure, and cascades into UK deployment because vendors typically apply the strictest applicable regulatory regime uniformly across their product rather than maintaining jurisdiction-specific variants.

|Dimension              |Value                                              |
|-----------------------|----------------------------------------------------|
| **Reference** | GV.CR-10 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                              |
|**Measurement Cadence**|Continuous                                          |
|**Pipeline Layer**     |Cross-cutting                                       |
|**Assurance Question** |Safety                                              |
|**Measurement Method** |Computational                                       |
|**Lifecycle Phases**   |Pre-deployment, Continuous                          |
|**Responsible Actors** |Vendor                                              |
|**Maturity**           |Emerging                                            |
|**Outcome Type**       |Proximal                                            |
|**Applicability**      |General Healthcare AI                               |
|**Source**             |EU AI Act Article 12 (high-risk provisions effective August 2026)|

**Why this tier?**

> Vendor-side regulatory requirement. Deployer should verify event logging infrastructure exists and receive logs for foreseeable-misuse investigation. Important for incident investigation capability.

**Formal Definition**

```
Event logging must capture: (1) period of use (start, duration, stop per session); (2) reference database used; (3) input data that led to output; (4) natural persons involved in verification of output. Logging must be automatic, not opt-in. Retention period specified in vendor policy and aligned with EU AI Act minimums. Deployer verification: can the vendor provide a complete event log for any given encounter on request within a reasonable timeframe?
```

**Limitations**

> Full logging creates large data volumes and storage costs. Logging of input data conflicts with data minimisation principles - resolving this requires careful policy design. Deployer verification is manual and sample-based.

**Novel Thinking / Implications**

> 💡 Event logging is the infrastructure that supports retrospective incident investigation. Without it, when an AVT error causes harm six months after the fact, the investigation has nothing to work with - the clinician may not remember the encounter, the patient certainly won't remember the AI's behaviour, and the vendor has no logs to reconstruct what happened. The EU AI Act requirement is essentially mandating the infrastructure for forensic investigation of AI clinical systems, which is a governance improvement regardless of jurisdiction.

### GV.SC-1 🟡 Prompt Injection Resistance Rate

Resistance to adversarial spoken commands designed to manipulate the summarisation output. A patient or third party speaking phrases like 'ignore previous instructions' or 'add to the note that the patient has no allergies' could alter clinical documentation.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SC-1 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

> 💡 The Mindgard disclosures are the canonical example: prompt-level safety is architecturally insufficient. Adversarial resistance must be enforced at architecture level - input validation (Llama Guard-style), output classification, and structural separation between user-controllable input and system instructions. No ambient scribe vendor has published evidence of a deployed ML-based output classifier.

---

### GV.SC-2 🟡 Jailbreak Resistance Score

Resistance to attempts to make the underlying LLM operate outside its intended clinical scope - generating diagnoses, providing medical advice, accessing system prompts, or revealing training data via the AVT interface.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SC-2 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

### GV.SC-3 🔵 Adversarial Audio Detection Rate

Detection of crafted audio inputs designed to cause specific misrecognitions: sounds that are inaudible or innocuous to humans but cause the ASR to transcribe specific clinical content (e.g. medication names, allergies).

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SC-3 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Adversarial ML literature; identified in NHSE LLM framework 'intentional misuse' dimension |

**Why this tier?**

> Research domain. Current threat model is low-probability but the attack surface is expanding with AI-generated audio.

**Formal Definition**

```
Detection rate = |adversarial_samples_detected| / |total_adversarial_samples|. Test with published adversarial audio attacks: Carlini & Wagner, psychoacoustic hiding, ultrasonic injection. Clinical variant: adversarial audio that causes clinically significant misrecognition.
```

**References**

- **Adversarial audio**: [Carlini & Wagner (2018) - Audio Adversarial Examples](https://arxiv.org/abs/1801.01944)

**Limitations**

> Academic adversarial audio attacks often require precise acoustic conditions that may not transfer to clinical settings. But the threat model is evolving - particularly with AI-generated audio becoming more accessible.

**Novel Thinking / Implications**

> 💡 The current threat model is low-probability but high-consequence. A more realistic near-term risk is audio deepfakes - a pre-recorded or AI-generated audio snippet played during a consultation to inject specific content into the transcript. As voice cloning becomes trivial, this attack surface expands.

---

### GV.SC-4 🔵 Data Poisoning Resilience

Resilience of the AVT system to training data poisoning. Research shows poisoning at 0.001% of training tokens can alter model behaviour. For vendor-hosted models receiving ongoing fine-tuning from clinical data, this is a supply chain risk.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SC-4 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

### GV.SC-5 🟡 Output Safety Classifier Coverage

Whether a safety classifier (analogous to Llama Guard or NeMo Guardrails) sits between the LLM and the clinician/EPR. Measures coverage: what proportion of outputs pass through the classifier, and what is its detection rate?

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SC-5 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | NVIDIA reference architecture; absence noted in vendor safety architecture review |

**Why this tier?**

> Architectural requirement. No AVT vendor has published evidence of a deployed output classifier. Should be a procurement question and eventually a regulatory expectation.

**Formal Definition**

```
Coverage = |outputs_classified| / |total_outputs|. Must be 100% for safety-critical deployment. Detection rate = |unsafe_outputs_caught| / |total_unsafe_outputs|. False positive rate = |safe_outputs_blocked| / |total_safe_outputs|. No ambient scribe vendor has published evidence of a deployed output classifier.
```

**References**

- **NVIDIA ref arch**: NVIDIA healthcare reference architecture (arXiv, Sept 2024) - Llama Guard 3 + NeMo Guardrails
- **Microsoft**: Microsoft Copilot Studio Healthcare Agent Service

**Limitations**

> Output classifiers add latency and may have their own failure modes. Clinical-specific safety classifiers don't yet exist - general-purpose classifiers (Llama Guard) don't understand clinical safety.

**Novel Thinking / Implications**

> 💡 The architectural gap: no AVT vendor has published evidence of a deployed ML-based output classifier. NVIDIA's reference architecture demonstrates the pattern; Microsoft's Copilot Studio comes closest to production. The absence of this layer means the clinician is the only safety gate - and we know from automation bias research that human oversight degrades over time.

---

### GV.SC-6 🟡 Template Injection Vulnerability Assessment

Testing whether user-configurable prompt templates can be crafted to bypass safety controls, alter system behaviour, or extract system prompts. Distinct from prompt injection (external attack) - this is an insider risk from authorised template modification.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SC-6 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

### GV.SC-7 🔵 Voice Cloning / Deepfake Detection

Given rapid maturation of voice cloning, can the system detect synthetic audio attempting to inject content? Increasingly relevant threat model as voice cloning becomes accessible.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SC-7 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
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

### GV.SC-8 🟡 Side-Channel Data Leakage

Does the system leak information through metadata, timing, error messages, or processing artifacts that could reveal patient information to unauthorised parties? A common security failure mode that's distinct from direct data exposure.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SC-8 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

### GV.SC-9 🟡 Cross-Patient Information Leakage Rate

Rate at which content from one patient's encounter contaminates another patient's generated note. Distinct from general PII leakage because cross-patient contamination can occur through context window contamination rather than training data memorisation - the leakage happens at inference time, not at training time, and is therefore invisible to standard privacy testing methodologies such as membership inference attacks.

|Dimension              |Value                                                         |
|-----------------------|--------------------------------------------------------------|
| **Reference** | GV.SC-9 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                        |
|**Measurement Cadence**|Periodic audit                                                |
|**Pipeline Layer**     |Cross-cutting                                                 |
|**Assurance Question** |Safety                                                        |
|**Measurement Method** |Computational                                                 |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                |
|**Responsible Actors** |Vendor                                                        |
|**Maturity**           |Emerging                                                      |
|**Outcome Type**       |Proximal                                                      |
|**Applicability**      |General Healthcare AI                                         |
|**Source**             |MIT Jameel Clinic 2026 cross-patient leakage disclosure       |

**Why this tier?**

> Vendor-side testing required because deployers cannot directly observe cross-encounter contamination. Should be a pre-deployment test and periodic audit requirement. Cross-patient leakage is a catastrophic failure mode - a single incident can affect hundreds of patients.

**Formal Definition**

```
Leakage Rate = |notes_containing_content_from_different_patient| / |total_notes|. Testing methodology: (1) process a batch of encounters sequentially through the same pipeline; (2) inject distinctive canary content into some encounters; (3) check whether canary content appears in notes from unrelated encounters processed in the same batch. Target: zero. Any non-zero rate indicates architectural failure in context isolation.
```

**Limitations**

> Requires controlled testing with injected canaries. Production leakage may occur under load conditions that aren't replicated in testing. Cross-patient contamination is rare enough that statistical power requires large test batches.

**Novel Thinking / Implications**

> 💡 Cross-patient leakage is the AVT-specific instantiation of context window contamination in multi-tenant LLM systems. When a single model instance serves multiple encounters in rapid succession, caching, state retention, and async processing all create potential vectors for one patient's content to leak into another's. This is architecturally preventable - strict per-encounter context isolation with explicit state resets - but only if the failure mode is explicitly tested for. Most vendor privacy testing focuses on training data leakage and doesn't cover this.

### GV.SC-10 🟡 Clinician Identity Authentication

Is the system confident that the clinician using AVT is who they claim to be? Voice biometrics could provide this but are rarely deployed. Without strong authentication, AVT outputs may be attributed to clinicians who weren't actually present.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SC-10 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

> 💡 The scenario: a registrar leaves their workstation logged in, a colleague uses AVT to dictate a note. The note is attributed to the registrar but reflects the colleague's clinical decisions. Without strong authentication and session management, AVT can produce notes attributed to clinicians who didn't make the relevant decisions - an audit trail integrity failure.

---

---

### GV.SC-11 🔵 Membership Inference Attack AUC

Standardised privacy testing metric measuring the success rate of adversarial attempts to determine whether a specific patient's data was used in training the AVT model. Higher AUC means the attack is more successful - an AUC of 0.5 indicates attacks are no better than random guessing, while an AUC near 1.0 indicates complete privacy failure. Undefended LLMs show MIA AUC of approximately 0.96; differential privacy training can collapse this to near 0.5.

|Dimension              |Value                                                         |
|-----------------------|--------------------------------------------------------------|
| **Reference** | GV.SC-11 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research                                |
|**Measurement Cadence**|Periodic audit                                                |
|**Pipeline Layer**     |Cross-cutting                                                 |
|**Assurance Question** |Safety                                                        |
|**Measurement Method** |Computational                                                 |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                |
|**Responsible Actors** |Vendor, Academic                                              |
|**Maturity**           |Established                                                   |
|**Outcome Type**       |Proximal                                                      |
|**Applicability**      |General Healthcare AI                                         |
|**Source**             |IEEE S&P 2023 LLM PII leakage study; arXiv 2601.03791 Cue-Resistant Memorisation framework|

**Why this tier?**

> Research-grade privacy testing. Requires specialist ML security expertise. Academic or vendor-side testing, not deployer-implementable. Important for understanding model-level privacy properties but not routinely measurable at deployment.

**Formal Definition**

```
Standard membership inference attack: attacker trains a classifier to distinguish model outputs on training data from outputs on held-out data. AUC of this classifier is the MIA metric. AUC = 0.5 means attacks fail; AUC > 0.7 indicates concerning leakage; AUC > 0.9 indicates severe privacy failure. Testing should use multiple attack methodologies (shadow model, loss-based, gradient-based) and report the highest AUC as the conservative estimate.
```

**Limitations**

> MIA methodology has been criticised for evaluation artefacts - the recent Cue-Resistant Memorisation framework (arXiv 2601.03791) showed that previous MIA estimates were inflated by control set selection. Modern MIA requires careful methodology. Mitigations (differential privacy) come with accuracy costs.

**Novel Thinking / Implications**

> 💡 MIA is the standardised way to compare privacy properties across models. A vendor claiming strong privacy should be willing to disclose MIA AUC under standard attack protocols - if they're not, that's itself informative. For NHS deployment, MIA matters because patient audio, transcripts, and notes entering training pipelines create membership signatures that, if exploitable, mean a sufficiently motivated attacker could determine whether a specific patient was present in training data. The 2023 finding of AUC 0.96 for undefended LLMs is a sobering baseline for what "no privacy defences" looks like in practice.

### GV.PD-1 🟢 Audio Retention Compliance

Whether audio recordings are retained, for how long, and whether retention complies with the stated DPIA and privacy notice. Includes monitoring for unauthorised retention beyond stated periods.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.PD-1 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | UK GDPR Article 5(1)(e) storage limitation; NHSE IG guidance on ambient scribing (March 2026) |

**Why this tier?**

> UK GDPR storage limitation requirement. Non-compliance is a regulatory breach. Deployer must verify vendor retention practices align with DPIA.

**Formal Definition**

```
Compliance rate = |encounters_within_retention_policy| / |total_encounters|. Track: actual deletion timestamps vs policy-required deletion timestamps. Delta > 0 = non-compliant retention. Must verify deletion is genuine (not just flagged), including backup systems.
```

**Reference Standard**

> The deployer-approved DPIA and privacy notice are the authoritative retention policy. "Compliant" means the audio is deleted from every named storage location within the policy-stated period. Storage locations in scope MUST include: primary vendor storage, vendor backups and disaster-recovery systems, vendor logs, any downstream analytic or quality-monitoring system, deployer-side caches, and any sub-processor systems named in the vendor's [GV.VT-7 Sub-Processor Transparency](#gv-vt-7) declaration. "Deletion" means cryptographic erasure or physical deletion; logical deletion (flagged-deleted-but-retained) does not count without an explicit DPIA carve-out.

**Operational Specification**

> - **Window:** continuous, with monthly attested compliance reporting.
> - **Population:** all consultation audio captured during the reporting window. No sampling; this is a compliance metric, not a quality metric.
> - **Per-storage-location reporting MANDATORY:** compliance reported per named storage location, not as a single rolled-up number. A 99 % aggregate that hides 100 % retention in backups is not compliant.
> - **Verification method MANDATORY:** vendor self-attestation alone is not Tier 1 sufficient. Independent verification is required at minimum annually via a third-party audit, deployer-witnessed deletion test, or cryptographic proof (e.g. key destruction for envelope-encrypted audio).
> - **Exception handling:** any audio retained beyond policy MUST be logged with reason, DPIA reference, and re-deletion target date. Exception rate reported as a separate KPI.

**Threshold Guidance**

> ⚠️ **Provenance:** the IG-incident reportability framing follows from UK GDPR storage-limitation requirements and the existing NHSE IG framework. Specific numerical thresholds (≥ 99.5 % monthly compliance, < 95 % escalation trigger, annual independent verification cadence) are **proposed in v3.3 as starting points**, not externally validated. Indicative; require local calibration against DPIA risk appetite before contractual use.
>
> - **Pre-deployment gate:** vendor produces a deletion-verification protocol covering every storage location in the architecture; deployer DPIA cross-references the protocol; one end-to-end deletion test passes prior to go-live.
> - **Continuous monitoring:** monthly compliance ≥ 99.5 % per storage location; alert on any single non-exception retention beyond policy; quarterly audit of exception log.
> - **Pause / escalation trigger:** any storage-location compliance < 95 % in any month, OR any unlogged retention beyond policy detected. Both are reportable as IG incidents per the existing NHSE IG framework.

**Limitations**

> Deployers typically cannot verify vendor-side deletion without independent audit. Backup and disaster recovery systems may retain data beyond primary deletion. The Operational Specification above makes this gap measurable rather than tacit; it does not eliminate it.

**Novel Thinking / Implications**

> 💡 Audio is the most sensitive data AVT processes - it captures everything said in the consultation, including content that doesn't make it into the note. Retention policy must distinguish between audio needed for review-before-signing (minutes) and audio retained for quality improvement or dispute resolution (potentially months). The DPIA must address both.

---

### GV.PD-2 🟢 Audio Time-to-Deletion

Measured time from consultation end to verified deletion of the captured audio. Operational implementation of the existing Audio Retention Compliance metric. NHS England's March 2026 IG guidance requires deletion of audio after the summary is signed off, unless explicitly retained for safety monitoring with documented justification. This metric measures whether the deletion is actually happening in the timeframe the policy claims.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.PD-2 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | NHSE IG guidance on ambient scribing (March 2026); UK GDPR Article 5(1)(e) storage limitation |

**Why this tier?**

> Direct compliance requirement. Measurable through vendor-provided deletion telemetry. Binary-ish: deletion within policy timeframe or not. Should be continuously monitored rather than periodically audited.

**Formal Definition**

```
Time-to-Deletion = t_deletion_verified - t_consultation_end. Report distribution: median, P95, P99, and count of encounters exceeding policy threshold. Verification requirement: deletion confirmed in primary storage, caches, backups, and any downstream analytic systems. Policy threshold per deployer: typically 24 hours to 7 days depending on DPIA. Compliance = proportion of encounters with verified deletion within threshold.
```

**Reference Standard**

> Inherits the storage-location enumeration and deletion-method definition from [GV.PD-1 Audio Retention Compliance](#gv-pd-1): primary vendor storage, backups and DR, vendor logs, downstream analytic systems, deployer-side caches, and named sub-processor systems per [GV.VT-7 Sub-Processor Transparency](#gv-vt-7). "Deletion" means cryptographic erasure or physical deletion (not logical/flagged-deleted). `t_consultation_end` is the clinician signature event on the AVT-generated note (sign-off triggers deletion under the NHSE IG March 2026 guidance); `t_deletion_verified` is the timestamp at which deletion is confirmed across every named storage location, not the timestamp at which deletion was initiated. Where the deployer's DPIA carves out retention for a named purpose, that purpose extends `t_deletion_verified` only for the carved-out subset and only for the carved-out duration.

**Operational Specification**

> - **Window:** continuous; monthly distribution reporting.
> - **Population:** every consultation audio captured during the window. No sampling — this is a compliance metric.
> - **Distribution reporting MANDATORY:** median, P95, P99, AND count of encounters exceeding policy threshold (the tail is the safety signal, not the median). Per-storage-location distribution where the architecture allows; otherwise the slowest-location time is the headline.
> - **Per-storage-location verification MANDATORY:** time-to-deletion measured against every storage location named in the GV.PD-1 enumeration. A median of 6 hours that hides 100 % retention in backups (where deletion never occurs) is non-compliant.
> - **Carve-out logging MANDATORY:** any audio retained beyond standard threshold under a DPIA carve-out logged with reason, duration, and re-deletion target date. Carved-out audio tracked in a separate distribution from standard audio; aggregating the two hides policy adherence.
> - **Deletion-verification method MANDATORY:** parallel to GV.PD-1 — vendor self-attestation alone insufficient; periodic independent verification (third-party audit, deployer-witnessed deletion test, or cryptographic proof via key destruction).

**Threshold Guidance**

> ⚠️ **Provenance:** the post-sign-off deletion expectation derives from NHSE IG guidance March 2026; UK GDPR Article 5(1)(e) storage-limitation provides the legal floor. Specific numerical thresholds (24-hour median target, 7-day P99 ceiling, 1 % exceedance rate trigger) are **proposed in v3.5 as starting points**, not externally validated. The DPIA's policy threshold takes precedence where it differs (the DPIA-stated period is the contractual gate; these numbers are starting points for that DPIA conversation). Indicative; require local calibration before contractual use.
>
> - **Pre-deployment gate:** vendor demonstrates per-storage-location deletion telemetry; one end-to-end deletion test passes prior to go-live; DPIA cross-references the policy threshold.
> - **Continuous monitoring:** monthly median TTD ≤ DPIA-stated threshold (typically 24 hours); P99 ≤ 7 days; encounters-exceeding-threshold rate < 1 %; per-storage-location compliance ≥ 99.5 %.
> - **Pause / escalation trigger:** any single non-exception retention beyond DPIA threshold; OR median TTD > DPIA threshold in any month; OR per-storage-location compliance < 95 % (cascades to GV.PD-1 compliance failure). All three are reportable as IG incidents.

**Novel Thinking / Implications**

> 💡 "Audio is deleted after sign-off" is a policy statement that only has governance value if it's actually measured. The gap between policy and practice on deletion is often substantial - audio persists in backup systems, error logs, annotation pipelines, and quality monitoring infrastructure long after the "deletion" event. Making time-to-deletion a measured metric rather than a policy assertion is the minimum required for the NHS IG guidance to have operational effect.

---

### GV.PD-3 🟢 Transcript Retention Compliance

Parallel metric to Audio Time-to-Deletion, but for transcripts. Often treated as less sensitive than audio - and therefore retained longer - but transcripts are in many ways more risky because they are structured, searchable, and readily consumable by downstream systems. A transcript of a consultation discussing mental health, substance use, or safeguarding concerns is arguably more sensitive than the audio because it removes the friction of listening and enables programmatic analysis.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.PD-3 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | NHSE IG guidance on ambient scribing (March 2026); UK GDPR Article 5(1)(e) |

**Why this tier?**

> Direct compliance requirement. Should be measured in parallel with Audio Time-to-Deletion. Often more operationally tractable because transcripts are typically held in vendor-controlled systems rather than distributed storage.

**Formal Definition**

```
For each transcript: retention duration = t_current - t_consultation_end. Retention policy specifies maximum duration for each purpose: summary generation (typically hours), review support (typically days), quality monitoring (variable, documented in DPIA). Compliance = |transcripts_retained_within_policy| / |total_transcripts|. Report per retention purpose - aggregating different retention justifications obscures policy adherence.
```

**Reference Standard**

> Same DPIA + privacy notice authority as [GV.PD-1](#gv-pd-1). Retention purposes MUST be enumerated in the DPIA with a maximum retention period per purpose; an unenumerated purpose is not a valid retention basis. "Compliance" is per-purpose, per-storage-location, and verified the same way as GV.PD-1: cryptographic erasure or physical deletion, not logical deletion. Storage locations in scope add: deployer-side analytics warehouses, research databases (where consent permits), and any redaction-pipeline intermediates.

**Operational Specification**

> - **Window:** continuous, monthly reporting.
> - **Population:** all transcripts produced during the window.
> - **Per-purpose, per-storage-location reporting MANDATORY:** the matrix of {retention purpose × storage location} is the unit of reporting. "Quality monitoring" as a single retention purpose without sub-categorisation does not satisfy this requirement; quality monitoring must be decomposed (e.g. "vendor model retraining", "deployer audit trail", "incident review") with separate retention periods per sub-purpose.
> - **Cross-system retention chain MANDATORY:** transcript derivatives (extracted entities, redacted variants, embedding vectors) tracked under the same purpose, with retention period inherited from the source unless explicitly DPIA'd otherwise.
> - **Verification:** parallel to GV.PD-1; independent verification annual minimum.

**Threshold Guidance**

> ⚠️ **Provenance:** UK GDPR purpose-limitation underpins the requirement to enumerate retention purposes; specific numbers (≥ 3 distinct purposes, ≥ 99.5 % monthly compliance, ≥ 90 %-of-volume quality-monitoring sub-categorisation, < 95 % escalation trigger) are **proposed in v3.3 as starting points**, not externally validated. Indicative; require local calibration before contractual use.
>
> - **Pre-deployment gate:** DPIA enumerates ≥ 3 distinct retention purposes with periods; vendor architecture diagram shows transcript flow through every named storage location with retention period at each.
> - **Continuous monitoring:** monthly per-purpose, per-storage-location compliance ≥ 99.5 %; "quality monitoring" sub-categorisation alone covers ≥ 90 % of transcript volume (a vendor whose only purpose is "quality monitoring" is failing this gate).
> - **Pause / escalation trigger:** any unenumerated retention purpose discovered in production, OR any per-purpose compliance < 95 %.

**Limitations**

> Retention for "quality monitoring" is often a catch-all that effectively keeps transcripts indefinitely. Tightening this requires specific retention periods per monitoring purpose - this is now an explicit Operational Specification requirement. Cross-system retention (transcript in vendor system, derived metadata in deployer analytics, redacted version in research database) creates a tangled retention picture.

**Novel Thinking / Implications**

> 💡 Transcripts are the highest-value/highest-risk intermediate representation in AVT. They contain everything said, in structured form, searchable, and often retained for longer than either the audio or the final note. An attacker who compromises transcript storage has far more exposure than one who compromises the final clinical records. Retention minimisation for transcripts is arguably more important than for audio, but it's rarely treated that way in DPIAs.

---

### GV.PD-4 🟡 Data Minimisation Score

Whether the AVT system processes only the minimum data necessary for its function. Includes: does the system transmit full audio to cloud when local processing would suffice? Does it retain intermediate outputs (full transcript) when only the summary is needed?

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.PD-4 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | UK GDPR Article 5(1)(c) data minimisation; DGX Spark / local processing potential |

**Why this tier?**

> UK GDPR data minimisation principle. Periodic architectural review of what data is processed, transmitted, and retained vs what is necessary.

**Formal Definition**

```
DMS = data_necessary / data_processed. Ideal DMS = 1.0. Track per data type: audio, transcript, summary, coded data, metadata. Architecture assessment: local vs cloud processing; data transmitted vs data retained; intermediate outputs vs final outputs.
```

**Limitations**

> Defining 'necessary' is contested - vendors argue cloud processing is necessary for quality; privacy advocates argue local processing is sufficient for many use cases.

**Novel Thinking / Implications**

> 💡 The DGX Spark and similar edge AI hardware create a genuine architectural choice: local processing minimises data exposure but may limit model capability. The data minimisation score should drive architectural decisions - if local processing meets quality thresholds, cloud transmission of full audio is unnecessary and non-compliant with minimisation principles.

---

### GV.PD-5 🟡 PII Extraction Attack Success Rate

Adversarial privacy testing: the rate at which a determined attacker can extract patient personal data from the deployed AVT system through model interaction. Includes prompt-based extraction (crafted queries that coax the model to reproduce training content), inversion attacks (reconstructing inputs from outputs), and side-channel extraction. Complements the Membership Inference Attack AUC metric - MIA tells you whether a specific patient was in training; PII extraction tells you what content about them can be recovered.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.PD-5 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | IEEE S&P 2023 LLM PII leakage study; OWASP LLM Top 10 (Sensitive Information Disclosure) |

**Why this tier?**

> Vendor-side red-team testing requirement. Deployers cannot independently test model-internal privacy properties. Should be a procurement requirement with results provided by vendor or independent assessor.

**Formal Definition**

```
Success Rate = |PII_items_successfully_extracted| / |PII_items_attempted|. Attack categories: (1) direct prompting ("what did the patient say about their family history?"); (2) completion-based extraction (prompting partial records and measuring reconstruction); (3) inversion attacks on embeddings; (4) canary extraction using known inserted content. Report per attack category - aggregate success rate obscures category-specific weaknesses.
```

**Limitations**

> Defining the attack surface is itself contested. A test suite that looks adequate today may be outdated tomorrow. Vendors may resist third-party red-teaming on competitive grounds. Extraction that is theoretically possible but requires massive query budgets may or may not be a practical concern depending on threat model.

**Novel Thinking / Implications**

> 💡 The OWASP LLM Top 10 lists Sensitive Information Disclosure as a standard vulnerability class, but most AVT vendors have not engaged with it as a distinct security category - privacy is typically treated as "we don't train on customer data" rather than as an active red-teaming target. The shift from passive privacy posture to adversarial privacy testing is the maturity marker. A vendor who has never had their system red-teamed for PII extraction should not be deployed into NHS clinical settings.

---

### GV.PD-6 🟡 Re-identification Risk Assessment

Structured assessment of the risk that de-identified data retained for quality improvement, research, or secondary use can be re-identified. Applies to any dataset derived from AVT operation - anonymised transcripts for model quality review, de-identified notes for research, aggregate statistics that may become identifying at small sample sizes. Standard privacy methodology applied to AVT-specific data flows.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.PD-6 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Deployer, Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | ICO anonymisation code of practice; NIST privacy framework |

**Why this tier?**

> Standard privacy methodology. Should be part of any DPIA for secondary uses. Periodic reassessment required as new data are added and as re-identification techniques evolve.

**Formal Definition**

```
Per retained dataset: assess re-identification risk against standard criteria - (1) direct identifiers present or removed? (2) quasi-identifiers (age, postcode, date, rare condition) combinable to identify individuals? (3) k-anonymity achieved and at what k? (4) l-diversity for sensitive attributes? (5) differential privacy applied? (6) motivated intruder test - could a determined attacker re-identify individuals given reasonably available auxiliary information? Overall risk rating: low / medium / high / unacceptable. Threshold for retention: risk must be low or medium with explicit justification.
```

**Limitations**

> Re-identification risk is probabilistic and depends on what auxiliary information an attacker has access to. Small clinical populations (rare conditions, small practices) are re-identifiable from very little information. "De-identified" is not the same as "anonymous".

**Novel Thinking / Implications**

> 💡 A single NHS practice with 5,000 patients has very few patients with any given rare condition - sometimes just one. A "de-identified" transcript mentioning that condition is trivially re-identifiable by anyone with access to the practice's patient list. Re-identification risk assessment forces this question into visibility during DPIA rather than treating de-identification as a technical checkbox.

---

### GV.PD-7 🟡 Training Data Inclusion Status

Clear documentation of whether deployer audio, transcripts, or notes are used by the vendor for model training or fine-tuning. Distinct from the existing Sub-Processor Transparency metric (which covers processing activity) and from privacy policies (which often hedge this question). This metric requires an explicit binary answer: is NHS data flowing into the vendor's training pipeline, yes or no, with documented consent basis if yes.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.PD-7 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | UK GDPR transparency requirements; derived from emerging AVT procurement practice |

**Why this tier?**

> Procurement gate. Should be explicitly answered in vendor contracts, not left to policy ambiguity. Annual reassessment on contract renewal.

**Formal Definition**

```
Status recorded as: (a) No - deployer data not used for any training or fine-tuning; (b) Yes - used for training with specified consent basis and opt-out mechanism; (c) Derived - used for aggregated statistics or distilled features without retaining source data. Each status has different governance implications. Documentation must specify which model components may be trained (ASR, summariser, coder) and which data types (audio, transcripts, notes, metadata). Vendor attestation required; independent verification is not currently feasible.
```

**Limitations**

> Verification relies on vendor attestation. The distinction between "training" and "quality improvement" can be blurred by vendors in ways that obscure actual data flows. Aggregate statistics derived from training data may themselves carry privacy risk.

**Novel Thinking / Implications**

> 💡 Many NHS AVT contracts are ambiguous about training data flows because vendors benefit from keeping the option open and deployers often don't ask explicitly. Making this a Tier 2 procurement metric forces the question into contract negotiations. The patient-level consequence is that AVT-using consultations may effectively contribute to training the next generation of commercial AI systems - and patients should know this if it's happening. This is a transparency obligation the existing taxonomy's consent metrics don't capture.

---

### GV.PD-8 🟢 Consent Verification Accuracy

Whether patients are actually informed about AVT use as required by CQC Mythbuster 109 (implied consent is sufficient, but patients must be informed). Measures both process compliance and patient understanding.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.PD-8 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Patient Experience |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Continuous, Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
| **Source** | CQC Mythbuster 109; NHSE IG guidance; common law implied consent requirements |

**Why this tier?**

> CQC Mythbuster 109 requires patients to be informed. Process compliance is measurable today. Understanding gap is harder but periodic survey is feasible.

**Formal Definition**

```
Process compliance = |consultations_where_patient_informed| / |total_AVT_consultations|. Understanding rate = |patients_who_can_describe_AVT_use| / |patients_surveyed| (periodic audit). Gap = process_compliance - understanding_rate reveals 'informed but not understanding' problem.
```

**Reference Standard**

> Two distinct sources combined:
>
> - **Process compliance** inherits the reference standard from [GV.CR-2 Verbal Notification Compliance](#gv-cr-2) — the deployer-approved patient notification script with the four content elements (what / what / who / how) delivered before AVT activation
> - **Understanding rate** is measured by structured patient survey. **No validated AVT-specific patient-comprehension instrument exists at the time of v3.6.** Deployers should either (a) select the closest healthcare-IT-comprehension instrument (e.g. eHealth Literacy items adapted for AVT context, Decision Conflict Scale items) and document the adaptation as a limitation, or (b) commission a deployer-defined survey reviewed by the IG team containing at least four comprehension items mapped to the [GV.CR-2 Verbal Notification Compliance](#gv-cr-2) content elements (what / what / who / how)
>
> The headline metric is the **gap** (process compliance minus understanding rate), not either rate alone. Gap > 25 percentage points triggers a substantive review; the consent model's legitimacy depends on understanding, not just notification (per the Novel Thinking section). Cross-link to [IO.PX-1 Patient Opt-Out Rate](#io-px-1) — opt-out behaviour disaggregated by demographics may indicate where the understanding gap is concentrated even before survey detects it.

**Operational Specification**

> - **Window:** continuous for process compliance (inherits from GV.CR-2); quarterly periodic audit for understanding rate.
> - **Population for understanding survey MANDATORY:** ≥ 30 patients per practice per quarter for survey method, with stratification across demographic axes (age band, primary language, deprivation index where available). Pure aggregate sampling masks the failure modes that matter — language and literacy are the predictable understanding-rate diminishers.
> - **Three sub-metrics MANDATORY:** process compliance rate (continuous from GV.CR-2), understanding rate (quarterly), and the gap. Any rate reported alone insufficient.
> - **Demographic disaggregation MANDATORY for understanding rate:** stratification by primary language, age band, ethnicity, and where available deprivation index. The aggregate understanding rate hides the failure pattern; disparities are the metric's value.
> - **Survey instrument declaration MANDATORY:** the survey instrument used must be declared (validated published instrument vs deployer-defined). Deployer-defined instruments must be reviewed by the IG team and document at least four comprehension items mapping to GV.CR-2 content elements.

**Threshold Guidance**

> ⚠️ **Provenance:** the gap-as-headline framing carries from the existing Novel Thinking section and CQC Mythbuster 109's "informed" requirement. Specific numerical thresholds (25-percentage-point gap trigger, ≥ 30 patients/quarter survey floor, demographic-disparity-2× alert) are **proposed in v3.5 as starting points**, not externally validated. The understanding rate is the harder measurement and the survey instrument choice will materially affect the result; require local calibration before contractual use.
>
> - **Pre-deployment gate:** GV.CR-2 process-compliance gate met; survey instrument selected and reviewed by IG team; quarterly survey schedule established.
> - **Continuous monitoring:** monthly process compliance from GV.CR-2; quarterly understanding rate; gap reported every quarter with demographic breakdown. Alert when aggregate gap > 25 percentage points OR any demographic axis shows understanding rate < practice mean by ≥ 20 percentage points.
> - **Pause / escalation trigger:** gap > 40 percentage points sustained two quarters (consent model legitimacy in question); OR any demographic axis shows understanding rate < 50 % (the consent model is failing for that population, not just under-performing).

**Novel Thinking / Implications**

> 💡 The gap between 'informed' and 'understanding' is the critical measure. A practice achieving 100% process compliance (every patient is told) may still have 30% understanding (patients don't grasp what AVT does with their speech). The consent model's legitimacy depends on understanding, not just notification.

---

### GV.PD-9 🟢 Cross-Border Data Transfer Compliance

Does AVT processing involve data transfer outside UK/EU? UK GDPR Article 46 requires appropriate safeguards for international transfers. Cloud-hosted AVT vendors may process data in US or other jurisdictions.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.PD-9 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | UK GDPR Article 46; Schrems II implications |

**Why this tier?**

> Legal compliance requirement. Must be assessed at procurement. Non-compliance is a regulatory breach.

**Formal Definition**

```
Audit data flow: (1) Where is audio processed? (2) Where are model inferences performed? (3) Where is data stored? (4) Where do support staff access data? For each non-UK location, verify Article 46 safeguards (SCCs, adequacy decisions, BCRs).
```

**References**

- **UK GDPR**: UK GDPR Article 46 - appropriate safeguards for international transfers

**Limitations**

> Vendor data flow transparency varies. Sub-processors may transfer data without main vendor visibility.

**Novel Thinking / Implications**

> 💡 Cloud-hosted AVT often involves transfers to US-based hyperscaler infrastructure. The Schrems II ruling complicates US transfers significantly. Many AVT vendors don't fully document their data flows - a compliance gap that becomes a deployer liability under UK GDPR.

---

### GV.PD-10 🟢 Subject Access Request Fulfilment

Can the deployer fulfil patient SAR requests for AVT-related data within statutory timeframes (one calendar month under UK GDPR)? Includes audio if retained, transcripts, intermediate outputs, and the final note.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.PD-10 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | UK GDPR Article 15 right of access |

**Why this tier?**

> Legal compliance requirement. Must be tested before go-live to confirm vendor supports SAR fulfilment workflow.

**Formal Definition**

```
SAR Fulfilment Rate = |SARs_completed_within_30_days| / |total_SARs|. Sub-criteria: (1) Can deployer locate all AVT data for a patient? (2) Can it be exported in usable format? (3) Within statutory timeframe? Target: 100% within 30 days.
```

**Reference Standard**

> UK GDPR Article 15 is the legal floor; ICO 30-day timeline is the statutory window (extendable by two months for complex requests with patient notification). "All AVT data for a patient" = every personal-data instance reachable via the storage-location enumeration in [GV.PD-1 Audio Retention Compliance](#gv-pd-1) plus [GV.VT-7 Sub-Processor Transparency](#gv-vt-7) — including audio, transcripts, AI-generated notes, edit history, telemetry-derived metadata, and any sub-processor-held copies. "Usable format" requires structured machine-readable export of structured data plus searchable text export of free-text content; PDF-only export of audio metadata is not "usable" for the patient's own access purposes. Cross-link to [GV.PD-11 Right to Erasure Compliance](#gv-pd-11) — the same data-locating capability underpins both rights.

**Operational Specification**

> - **Window:** continuous SAR-by-SAR tracking with quarterly compliance reporting.
> - **Population:** every SAR received that includes AVT-related data (denominator: SARs received, not consultations).
> - **Three sub-metric reporting MANDATORY:** locate-rate (deployer can find all AVT data), export-rate (data exportable in usable format), and timeliness-rate (completed within 30 days). Aggregate alone is not sufficient — failure mode (couldn't find / found but couldn't export / found and exported too slowly) drives different remediation.
> - **Synthetic SAR test pre-deployment MANDATORY:** at least one synthetic SAR processed end-to-end before go-live, exercising every storage location and sub-processor in the architecture. Failures discovered in this test are remediated before live SARs occur, not after.
> - **Sub-processor cooperation tracked separately:** SAR fulfilment depends on sub-processors providing their data; cooperation latency per sub-processor recorded. Vendors should contractually commit sub-processors to deployer's SAR timeline.
> - **Complex-request extension logged:** any SAR using the two-month extension provision logged with reason; pattern of extensions on AVT-related SARs is a signal that the locate-rate or export-rate is failing.

**Threshold Guidance**

> ⚠️ **Provenance:** the 30-day target and 100 % locate/export expectation derive from UK GDPR Article 15 and ICO guidance. The synthetic-SAR pre-deployment test is **proposed in v3.5 as a starting point** to bring SAR readiness into the procurement gate (rather than discovering at first live SAR). Specific numerical thresholds are largely cited; the pre-deployment test cadence and the extension-pattern alert are the proposed elements. Indicative; require local calibration before contractual use.
>
> - **Pre-deployment gate:** synthetic SAR test passes — every storage location returns data; export format usable; full processing within 30 days. Gaps remediated before go-live.
> - **Continuous monitoring:** quarterly per-sub-metric reporting; locate-rate ≥ 100 % (any SAR where AVT data could not be located is a failure regardless of timeliness); export-rate ≥ 100 %; timeliness-rate ≥ 95 % (allowing for legitimate complex-request extensions).
> - **Pause / escalation trigger:** any SAR where AVT data could not be located within the deployer's known architecture (this is a regulatory failure under Article 15); OR timeliness-rate < 90 % in any quarter (suggests operational capacity failure); OR > 30 % of AVT-related SARs using the two-month extension (suggests systematic locate/export failure rather than legitimate complexity).

**Novel Thinking / Implications**

> 💡 When a patient submits a SAR, the deployer must provide all personal data including AVT-generated material and any retained audio. If the vendor doesn't provide patient-level export, the deployer cannot fulfil their statutory obligation. This should be a procurement question, not discovered after the first SAR.

---

### GV.PD-11 🟢 Right to Erasure Compliance

If a patient requests erasure under UK GDPR Article 17, can audio, transcripts, and intermediate outputs actually be deleted? Backup systems, vendor caches, and downstream secondary uses complicate this.

**Applicability note.** Article 17 rights are narrowly applicable for AVT processing conducted for individual care: the UK GDPR exemptions for public-task, public-health, preventative/occupational medicine, medical diagnosis, and health/social-care provision mean erasure of material held strictly for individual-care purposes is typically *not* exercisable as a statutory right (NHSE IG guidance Mar-2026). The capability must still exist for cases where erasure does apply - secondary use, research data derived from AVT, training-data inclusion under GV.PD-7, and case-by-case best-interest determinations - which is why this remains a pre-deployment gate.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.PD-11 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | UK GDPR Article 17 right to erasure; NHSE IG guidance on ambient scribing (Mar-2026) for individual-care exemption scope |

**Why this tier?**

> Pre-deployment gate to establish the scope, Article 17 applicability exemptions, and technical limitations of erasure. The statutory right is narrowly applicable for individual-care AVT processing but the capability must exist for cases where it does apply (secondary use, training-data withdrawal, dispute resolution). Tier 1 because understanding what erasure *can* and *cannot* deliver is a mandatory input to the DPIA and the privacy notice.

**Formal Definition**

```
Erasure Test: process a synthetic erasure request through the system. Verify deletion in: primary storage, backups, vendor caches, model training pipelines, downstream secondary use. Verification Rate = locations confirmed deleted / total locations.
```

**Reference Standard**

> UK GDPR Article 17 with the NHSE IG March 2026 individual-care exemption scope is the legal floor. The locations enumeration inherits from [GV.PD-1 Audio Retention Compliance](#gv-pd-1) plus three Article-17-specific additions:
>
> - **Model training pipelines** — any AVT data ingested for model fine-tuning, validation set construction, or A/B testing
> - **Downstream secondary use** — research databases, quality-monitoring archives, business-intelligence pipelines
> - **Sub-processor systems** — every entity in the [GV.VT-7 Sub-Processor Transparency](#gv-vt-7) discovered set
>
> Three classes of erasure outcome MUST be distinguished: **deletable** (data can be cryptographically erased or physically deleted at all named locations); **anonymisable** (data can be irreversibly de-identified to the ICO standard, suitable for research-database carve-outs); **technically irreversible** (data cannot be removed — typically applies to influence on already-trained models). The taxonomy and the privacy notice MUST disclose the irreversible class explicitly per the Novel Thinking section. Cross-link to [GV.PD-7 Training Data Inclusion Status](#gv-pd-7) — patients should know at consent time whether their data may end up in the irreversible class.

**Operational Specification**

> - **Window:** one-off pre-deployment gate; mandatory re-test on architectural change (new sub-processor, new training pipeline, new secondary-use destination).
> - **Population for synthetic test:** at least one synthetic patient record exercised end-to-end through every named location in the enumeration above. Production erasure-rate also tracked for the (small) population of in-scope live erasure requests.
> - **Three-class outcome reporting MANDATORY:** every erasure-test location classified deletable / anonymisable / technically-irreversible. Aggregate "verification rate" alone hides the irreversible-class failure mode.
> - **Privacy-notice cross-check MANDATORY:** the technically-irreversible class enumerated at procurement must match the disclosure in the privacy notice. Drift between the two (locations becoming irreversible without privacy-notice update) is itself a flag.
> - **Article-17-exempt vs in-scope:** every erasure request classified as exempt (individual-care purpose, public-task carve-out) or in-scope (secondary use, research, training data, best-interest case). The exempt class is logged with reason but not subject to the same fulfilment expectation as in-scope.
> - **Sub-processor cooperation tracked:** parallel to [GV.PD-10 Subject Access Request Fulfilment](#gv-pd-10) — sub-processor latency per erasure request recorded.

**Threshold Guidance**

> ⚠️ **Provenance:** the three-class outcome distinction (deletable / anonymisable / technically-irreversible) is **proposed in v3.5** as a way to operationalise the Novel Thinking section's observation that some erasure requests cannot be fulfilled even in principle. The Article 17 exemption framing is cited (NHSE IG March 2026). Specific numerical thresholds are largely binary (privacy-notice match, synthetic-test coverage); the proposed elements are the three-class taxonomy and the privacy-notice cross-check. Indicative; require local calibration before contractual use.
>
> - **Pre-deployment gate:** synthetic erasure test passes — every storage location classified into one of the three outcome classes; technically-irreversible class enumerated and matched to the privacy notice; sub-processor cooperation timelines documented.
> - **Continuous monitoring:** in-scope erasure requests fulfilled within 30 days at deletable locations and 30 days at anonymisable locations; technically-irreversible-class size stable (any growth means a new location was added without classification — a flag).
> - **Pause / escalation trigger:** any in-scope erasure request where a deletable location fails to delete (regulatory failure under Article 17); OR any newly added location not classified into the three-class taxonomy before processing personal data; OR drift between technically-irreversible class and privacy-notice disclosure (procurement-time disclosure failure).

**Novel Thinking / Implications**

> 💡 The hard case: if audio from a patient was used to fine-tune the vendor's model, can that influence be removed? Probably not - and this should be disclosed in the privacy notice. Patients should know that consenting to AVT may include effectively irreversible inclusion of their voice in model training. This is a transparency obligation that current AVT consent processes rarely address.

---

### GV.OP-1 🟢 Documentation Time per Consultation

Most cited benefit metric. Tells you nothing about safety. 'Time saved' alone is meaningless - pair with quality.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.OP-1 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Day Zero Baseline, Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | Widely used; critiqued Coiera & Fraile-Navarro 2026 |

**Why this tier?**

> Most widely measured benefit metric. Tells you nothing about safety but essential for demonstrating value proposition. Must be reported alongside quality metrics.

**Formal Definition**

```
DT = t_doc_end - t_doc_start. Quality-adjusted: report alongside PDSQI-9 or hallucination rate. TS = DT_pre - DT_post. Meaningful only if quality stable/improving.
```

**Reference Standard**

> EPR + AVT product telemetry. "Documentation start" = first keystroke or first AVT activation in the note's edit session, whichever is earlier. "Documentation end" = clinician signature event on the note. Time spent reviewing AVT-generated content **counts as documentation time**; the metric measures total clinician note-effort, not just typing time. The metric MUST be reported alongside a quality companion metric ([TP.SN-3 PDSQI-9](#tp-sn-3), [TP.SN-5 Hallucination Rate](#tp-sn-5), or equivalent) - DT in isolation is not interpretable per Coiera & Fraile-Navarro 2026.

**Operational Specification**

> - **Window:** weekly aggregate per clinician, with continuous monitoring trajectory.
> - **In-consultation vs out-of-consultation breakdown MANDATORY:** documentation completed during the patient encounter reported separately from documentation completed after the patient has left. AVT systems can reduce in-consultation time while increasing out-of-consultation time - aggregating the two hides the failure mode.
> - **After-hours boundary MANDATORY:** documentation completed outside the clinician's scheduled clinical hours is tracked under [GV.OP-2 Pyjama Time / After-Hours EHR Use](#gv-op-2), not under DT. Both metrics must be reported together; reporting DT alone risks hiding burden displacement.
> - **Per-clinician baseline MANDATORY:** the deployment baseline is the median weekly DT across the first 4 weeks of clinician live use. Time-saved (TS) calculations reference this per-clinician baseline, not a pooled cohort baseline (parallel to [HL.HF-1 Edit Rate](#hl-hf-1)).
> - **Aggregation:** report median DT and the time-saved (TS) trajectory; do not collapse to a single number without quality companion metric.

**Threshold Guidance**

> ⚠️ **Provenance:** the requirement to pair DT with a quality companion metric and the in/out-of-consultation breakdown framing follow from Coiera & Fraile-Navarro 2026 and the RSET 'time is not automatically convertible' caution cited above. Specific thresholds (4-week baseline window, 25 % TS trigger for review, 0 % out-of-consultation TS rule-out) are **proposed in v3.4 as starting points**, not externally validated. Indicative; require local calibration before contractual use.
>
> - **Pre-deployment / Day Zero baseline:** establish per-clinician DT median across the first 4 weeks of live use, with separate medians for in-consultation and out-of-consultation segments. Quality companion metric measured concurrently.
> - **Continuous monitoring:** weekly DT trajectory per clinician; report TS only when paired with quality companion metric. Flag for review: TS > 25 % from baseline (the magnitude triggers a quality cross-check, not a celebration).
> - **Pause / review trigger:** any TS reported without quality data; OR in-consultation TS > 0 paired with out-of-consultation DT increase (suggests burden displacement to after-hours, not reduction); OR TS positive while quality companion metric (PDSQI-9, hallucination rate) deteriorates.

**References**

- **Critique**: Coiera & Fraile-Navarro (2026)
- **RSET**: 'Time is not automatically convertible into money, productivity, or better care'

**Limitations**

> Says nothing about safety. The Operational Specification's pairing requirement makes this gap visible at every reporting cycle but does not eliminate it - the metric still measures effort, not value.

**Novel Thinking / Implications**

> 💡 'Saved 3 min and maintained >98% PDSQI-9' is meaningful. 'Saved 3 min' alone is not.

---

### GV.OP-2 🟡 Pyjama Time / After-Hours EHR Use

Clinician time spent on EHR and documentation work outside of scheduled clinical hours. Standard burnout-adjacent metric from the Sinsky et al. literature. Applied to AVT assessment, it measures whether documentation burden that was shifted from in-consultation to after-consultation (a known pattern with review-before-signing workflows) has simply moved the burden to outside working hours rather than reducing it.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.OP-2 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Day Zero Baseline, Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
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

> 💡 This is the metric that catches the most common AVT failure mode for clinician wellbeing: the system reduces typing time during consultations but creates after-hours review work that the clinician was not previously doing. In-consultation time savings are visible and marketable; after-hours burden is invisible and unpaid. A deployment that shows documentation time saved per consultation should also show pyjama time decreased - if only the first moves, the value proposition is shifted burden, not reduced burden.

---

### GV.OP-3 🟡 Note Turnaround Time

Elapsed time from consultation end to note availability in the EPR, measured from the clinician's perspective rather than the pipeline's internal latency. Extends the existing Full-Pipeline Latency Budget (which is a technical metric) into an operational workflow metric that directly affects review quality. If the note arrives after the clinician has started the next patient, review happens later in lower-quality conditions or not at all.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.OP-3 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | Standard operational workflow metric; extends Full-Pipeline Latency Budget |

**Why this tier?**

> Operational metric derivable from EPR workflow data. Directly affects review quality and therefore safety. Should be continuously monitored and reported.

**Formal Definition**

```
Turnaround Time = t_note_available_in_EPR - t_consultation_end. Report distribution: median, P50, P90, P99. Clinically relevant threshold: proportion of notes available before the start of the next patient's consultation. A turnaround time distribution with long tails creates selective review failure - the notes most delayed are the ones most likely to be approved without meaningful review.
```

**Limitations**

> End of consultation is not always cleanly timestamped. Network conditions, EPR availability, and other operational factors affect turnaround independent of AVT processing time.

**Novel Thinking / Implications**

> 💡 The existing Full-Pipeline Latency Budget captures technical processing time; note turnaround captures the clinically meaningful delay. The difference is everything else - queueing, EPR write-back latency, user interface delays, notification lag. A vendor who optimises only their pipeline latency without addressing end-to-end turnaround is optimising for the wrong metric.

---

### GV.OP-4 🟡 Documentation Workload Composite

Composite metric grouping Documentation Time per Consultation, Pyjama Time, and Note Turnaround Time into a single workload assessment. The family-level metric for documentation burden. Reports change in total workload rather than change in individual components - which is the number that matters for the value proposition and clinician wellbeing assessment.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.OP-4 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Day Zero Baseline, Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
| **Source** | Sinsky et al. extended to AVT context; NHS workforce wellbeing frameworks |

**Why this tier?**

> Composite metric built from component metrics measured separately. Quarterly rollup enables trajectory reporting to clinical leadership without requiring separate measurement work.

**Formal Definition**

```
Workload Composite = w1 × Documentation_Time + w2 × Pyjama_Time + w3 × Verification_Burden. Weights reflect relative clinical significance; default equal weights. Per-clinician and aggregate reporting. Change metric: ΔWorkload = Workload_post_AVT - Workload_pre_AVT. Negative ΔWorkload = genuine net reduction; positive = net increase despite in-consultation savings.
```

**Limitations**

> Aggregation hides component-level patterns. A composite that stays stable may mask simultaneous decrease in documentation time and increase in pyjama time - the stable number obscures the pattern shift. Report composite alongside components, not instead of them.

**Novel Thinking / Implications**

> 💡 The composite is the honest answer to "did AVT reduce workload?" that the individual metrics cannot give alone. A practice reporting "saved 3 minutes per consultation" without composite reporting is answering a convenient question; a practice reporting composite workload change is answering the real one. Clinical leadership and commissioners should request composite reporting rather than selective component reporting.

---

### GV.OP-5 🟢 System Availability / Uptime

Percentage operational. NAS: ≥99.5% during consultation hours.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.OP-5 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

### GV.OP-6 🟢 Adoption Rate & Selective Use Patterns

Who uses AVT and for which consultations. Selective patterns reveal practical system boundaries.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.OP-6 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

### GV.OP-7 🟡 Cost per Consultation

Total cost including licence, infrastructure, training, and governance overhead. Often under-reported by vendors who quote licence costs only without including operational burden.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.OP-7 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

> 💡 Vendor quotes typically include licence cost only. The full cost of operating AVT includes substantial governance overhead - CSO time, training, audit, incident response. Practices that compute true cost per consultation often find the value proposition is much weaker than vendor materials suggest.

---

### GV.OP-8 🔵 Governance & Maintenance Burden

Clinician and admin time spent on AVT-related tasks: template updates, error reporting, incident investigation, audit, training delivery. Per week per clinician using AVT.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.OP-8 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

### GV.OP-9 🟡 Training Time per Clinician

Initial and refresher training hours required per clinician. Affects both adoption (high training burden = slow adoption) and ongoing operational cost.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.OP-9 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

### GV.EN-1 🔵 Energy Consumption per Clinical Note

Electrical energy cost of generating a single clinical note, measured in watt-hours. Depends on model architecture, hosting infrastructure, and query complexity. Published benchmarks for general-purpose LLM inference range from 0.42 Wh for simple queries to 29 Wh for complex prompts - a 70× range that makes provider choice consequential for total energy footprint.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.EN-1 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
| **Source** | Jegham et al., arXiv 2505.09598 (2025) - "How Hungry is AI?" |

**Why this tier?**

> Vendor-side measurement. Not deployer-actionable today but reportable. NHS procurement will increasingly ask this question as Net Zero commitments mature.

**Formal Definition**

```
Energy per Note (Wh) = total_inference_energy / number_of_notes_generated. Measured at the inference infrastructure level. Per-model reporting required because architecture choice dominates the metric. Break down into: ASR energy, summarisation energy, coding energy. Scale: multiply by annual note volume to estimate annual energy cost of deployment.
```

**Limitations**

> Vendor access to per-note energy telemetry is typically not exposed to customers. Hosting infrastructure varies, making direct vendor comparison difficult. Published benchmarks use standardised prompts that don't reflect real clinical usage patterns.

**Novel Thinking / Implications**

> 💡 At the NHS scale (potentially millions of consultations per year using AVT), even small per-note energy differences compound into substantial total footprint. An NHS-wide AVT deployment using a 29 Wh/note model consumes ~70× more energy than the same deployment on a 0.42 Wh/note model. This is not a dominant clinical assurance question but it is a material procurement question under NHS Net Zero - and reporting it creates the data visibility that lets procurement use it.

---

### GV.EN-2 🔵 Carbon Emissions per Inference

Greenhouse gas emissions per clinical note, measured in grams of CO₂-equivalent. Distinct from energy consumption because carbon intensity depends on the hosting region's electricity grid - the same model hosted in a coal-heavy grid vs a renewable-heavy grid has very different carbon footprint despite identical energy use. Relevant to NHS Net Zero procurement and to EU-market vendors under corporate sustainability reporting requirements.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.EN-2 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
| **Source** | Mistral AI lifecycle assessment; Jegham et al. 2025 - grid carbon intensity adjustment |

**Why this tier?**

> Vendor-reported metric. NHS Net Zero relevant for procurement. Cannot be measured by deployers.

**Formal Definition**

```
gCO₂e per Note = energy_per_note × grid_carbon_intensity(hosting_region, time). Report: (a) current grid intensity at hosting location; (b) marginal emissions (electricity that would not have been consumed without this inference); (c) embodied emissions amortised over model lifetime. NHS procurement comparison: total annual gCO₂e = gCO₂e_per_note × annual_note_volume. Compare against NHS trust carbon budgets to contextualise.
```

**Limitations**

> Grid carbon intensity data are approximate and vary by time of day. Marginal vs average emissions methodology is contested. Embodied emissions from model training are difficult to attribute to individual inferences.

**Novel Thinking / Implications**

> 💡 Hosting region choice is a lever NHS procurement could use: a vendor hosted in regions with lower-carbon grids has lower per-note emissions for identical models. This creates a potential procurement criterion distinct from clinical performance - and may create pressure for vendors to offer UK or low-carbon hosting options as a Net Zero differentiator. Whether NHS procurement will actually weight this remains to be seen.

---

### GV.EN-3 🔵 Water Consumption per Query

Water consumed by data centre cooling infrastructure per clinical note inference. Measured in millilitres. Increasingly required for NHS Net Zero procurement given water stress considerations in parts of the UK and in cloud hosting regions globally. Less visible than energy and carbon but material at AVT-deployment scale.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.EN-3 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
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

### GV.TC-1 🟢 Clinician Training Completion Rate

Percentage of AVT-using clinicians who have completed required training modules: vendor product training, local induction (review-before-signing, known failure modes, error reporting, opt-out processes), and periodic refresher training.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.TC-1 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Day Zero Baseline, Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | NAS Day Zero requirements; standard clinical governance |

**Why this tier?**

> Governance requirement. No clinician should use AVT without completing required training. Binary compliance metric - 100% is the only acceptable target.

**Formal Definition**

```
TCR = |clinicians_fully_trained| / |clinicians_using_AVT|. Fully trained = completed all required modules within validity period. Track by module: vendor training, local induction, failure mode awareness, refresher. TCR < 100% = governance non-compliance.
```

**Reference Standard**

> Authoritative source: the deployer's clinical governance training record (LMS or equivalent), with module catalogue mapped against the NAS Day Zero training requirements and local induction policy. Four mandatory modules MUST be enumerated:
>
> - **M1: Vendor product training** — system mechanics, activation, opt-out, error reporting per the specific AVT product
> - **M2: Local induction** — review-before-signing workflow, opt-out and dissent procedures (cross-link [GV.CR-1 Patient Dissent Recording Rate](#gv-cr-1) and [GV.CR-2 Verbal Notification Compliance](#gv-cr-2)), incident-reporting pathway
> - **M3: Failure-mode awareness** — AVT-specific failure modes (hallucination/omission asymmetry, speaker misattribution, accent-related accuracy variation, complacency trajectory, system-unavailable fallback)
> - **M4: Refresher** — annual re-engagement on M1-M3 with updates reflecting deployed system changes
>
> "Completed" requires evidenced engagement, not just course-record entry. Module-completion timestamps recorded; minimum-engagement-time floors specified per module to prevent "5-minute completion".

**Operational Specification**

> - **Window:** continuous; monthly compliance reporting per practice / per clinician.
> - **Population:** every clinician using AVT (denominator). Clinicians who have stopped using AVT but remain on the practice register are excluded with reason.
> - **Per-module reporting MANDATORY:** four sub-rates (M1/M2/M3/M4 completion). Aggregate TCR alone is insufficient — a clinician missing M3 (failure-mode awareness) is a different risk from one missing M4 (refresher overdue).
> - **Validity periods MANDATORY (per module):** M1 valid for the lifetime of the deployed system version (revoked on major vendor product upgrade per [GV.SG-1 Model Version Tracking](#gv-sg-1)); M2 valid until significant local-policy change; M3 valid 12 months; M4 must be completed within 12 months of the previous engagement (rolling).
> - **Engagement-time floor MANDATORY:** minimum 30 minutes recorded engagement on M3 specifically (the failure-mode-awareness module is the most subject to "click-through" completion); 15 minutes on M1; 20 minutes on M2.
> - **Coverage check:** any clinician active on AVT in the previous 30 days appears in the denominator. Late-onboarders given a 14-day grace window from first AVT use to completion of M1 + M2.

**Threshold Guidance**

> ⚠️ **Provenance:** the four-module structure follows from the existing Formal Definition and the NAS Day Zero requirements cited in Source. The AVT-specific failure-mode list in M3 carries from the Novel Thinking section. Specific numerical thresholds (30/20/15-minute engagement floors, 12-month refresher cadence, 14-day onboarding grace, 100 % gate) are **proposed in v3.5 as starting points**, not externally validated. Indicative; require local calibration against the deployer's clinical governance framework before contractual use.
>
> - **Pre-deployment / Day Zero gate:** every clinician scheduled to use AVT has M1 + M2 + M3 complete within validity periods; M4 not yet applicable for new starters.
> - **Continuous monitoring:** monthly per-module TCR ≥ 100 %; alert on any clinician active on AVT with any module out of date by > 14 days.
> - **Pause / escalation trigger:** any clinician using AVT with M3 (failure-mode awareness) missing or stale (this is the safety-critical module — operational use without it is a governance failure regardless of M1/M2/M4 status); OR aggregate TCR < 95 % at the practice level for any module sustained two consecutive months.

**Limitations**

> Completion ≠ competence. A clinician who completed e-learning in 5 minutes has 'completed' training but may not have learned anything. The Operational Specification's engagement-time floors prevent the most blatant click-through pattern but cannot test actual understanding; pair with [GV.TC-2 Failure Mode Awareness Score](#gv-tc-2) for an outcome-side check on whether training has produced competence.

**Novel Thinking / Implications**

> 💡 Training should include AVT-specific failure modes that differ from general AI awareness: hallucination vs omission asymmetry, speaker misattribution patterns, accent-related accuracy variation, the complacency trajectory, and what to do when the system is unavailable. Generic 'AI awareness' training is insufficient.

---

### GV.TC-2 🟡 Failure Mode Awareness Score

Clinician knowledge of AVT-specific failure modes: can they identify hallucination, omission, speaker misattribution, and coding errors? Tested via scenario-based assessment, not self-report.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.TC-2 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Day Zero Baseline, Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
| **Source** | Proposed - extends error injection concept to training assessment |

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

### GV.TC-3 🟡 Refresher Training & CPD Compliance

Ongoing competency maintenance: are clinicians completing periodic refresher training that incorporates new failure modes discovered through operational monitoring and incident reports?

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.TC-3 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
| **Source** | Standard clinical governance CPD requirements; applied to AVT |

**Why this tier?**

> Ongoing competency maintenance. Content should be data-driven from operational monitoring. Annual minimum, triggered by model updates.

**Formal Definition**

```
Compliance = |clinicians_current_on_refresher| / |clinicians_using_AVT|. Refresher content must be updated to include: (a) locally discovered failure modes, (b) national safety alerts, (c) model update implications, (d) new attack vectors. Frequency: minimum annually, triggered by model updates.
```

**Limitations**

> Refresher fatigue - clinicians already have substantial CPD requirements. AVT-specific refresher competes for limited time. Must be efficient and clinically relevant.

**Novel Thinking / Implications**

> 💡 Refresher content should be data-driven: if edit-pattern monitoring reveals a new failure mode (e.g. systematic omission of safety-netting advice), the refresher should include examples of that specific failure. Generic refresher training is less effective than targeted, evidence-based updates.

---

### GV.TC-4 🔵 Trainee Impact Assessment

Does AVT use during training affect junior clinician skill development? GMC educational standards consideration. If trainees learn to consult with AVT from day one, they may not develop documentation skills the profession traditionally relied on.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.TC-4 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Academic, National Body |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
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

> 💡 This is the medical education question that should be answered before AVT becomes ubiquitous in training environments. If trainees lose documentation skills, the workforce loses resilience - what happens when AVT is unavailable, malfunctioning, or contraindicated? Medical Royal Colleges should be tracking this.

---

### GV.TC-5 🟡 Training Material Currency

Is training content updated to reflect newly discovered failure modes from operational monitoring? Static training that doesn't incorporate lessons from incidents misses opportunities to prevent recurrence.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.TC-5 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | Standard training governance |

**Why this tier?**

> Operational governance metric. Should be tracked as part of incident-to-training feedback loop.

**Formal Definition**

```
Training Currency = days since last update of training materials. Coverage of recent failure modes: |recent_failure_modes_covered_in_training| / |recent_failure_modes_identified|. Target: training updated within 90 days of any new failure mode discovery.
```

**Limitations**

> Requires connection between operational monitoring and training update process - often disconnected.

**Novel Thinking / Implications**

> 💡 Training that doesn't evolve with operational experience is a missed opportunity. When a new failure mode is discovered (e.g. systematic omission of safety-netting in a particular context), the training should be updated within weeks, not years.

---

### GV.VT-1 🟢 Model Change Notification Compliance

Whether the vendor notifies deployers of model updates before deployment, with sufficient detail to assess impact. Stanford framework finding: 'many vendors do not yet provide the access or telemetry necessary.'

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.VT-1 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | Stanford monitoring framework; three-layer surveillance model |

**Why this tier?**

> Should be a contractual requirement in NHS procurement. The three-layer surveillance model depends on it. Without vendor notification, governance is reactive.

**Formal Definition**

```
Compliance rate = |updates_notified_before_deployment| / |total_updates_deployed|. Notification quality: must include (a) what changed, (b) expected impact on outputs, (c) validation results on clinical benchmarks. Lead time: minimum 14 days before production deployment for major updates.
```

**Reference Standard**

> Vendor change-event log paired with deployer notification record. The change-event taxonomy follows [GV.SG-1 Model Version Tracking](#gv-sg-1) — the six versioned components (ASR / LLM weights / prompt / retrieval / safety classifier / fine-tunes). A "notification" requires written communication to the named deployer contact (not generic vendor newsletter or status page) containing the four mandatory content elements (a-d below). Cross-link to MHRA Post-Market Surveillance Regulations 2024 (SI 2024 No. 1368): changes meeting the "substantial" threshold trigger separate regulatory notification obligations and MUST be flagged as such.

**Operational Specification**

> - **Window:** continuous; per-change-event tracking with monthly compliance reporting.
> - **Population:** every change-event recorded by [GV.SG-1](#gv-sg-1) telemetry. Denominator is change-events, not calendar months.
> - **Severity classification MANDATORY:** every change classified as **major** (component-level rewrite, scope expansion, retraining with new data, regulatory-substantial), **moderate** (incremental retraining, prompt revision, retrieval index update), or **minor** (bug fix, performance optimisation without behavioural change). Lead-time requirements differ per severity (Threshold Guidance below).
> - **Four mandatory content elements per notification:** (a) what changed (component, version-from, version-to); (b) expected impact (clinical-benchmark deltas, edge cases, known failure modes affected); (c) validation results (named benchmarks, test corpora, sample sizes); (d) deployer action required (re-run [GV.SG-2 Model Update Impact Score](#gv-sg-2), schedule [GV.CR-6 Safety Case](#gv-cr-6) update, etc.). Notifications missing any element count as non-compliant regardless of timing.
> - **Substantial-change flag MANDATORY:** any change meeting MHRA PMS substantial-change criteria flagged in the notification with regulatory reference; absence of flag where one applies is a separate compliance failure (regulatory, not contractual).
> - **Per-deployment notification:** notifications addressed to the named contract contact, not posted to a status page. Deployer-side acknowledgement timestamp recorded.

**Threshold Guidance**

> ⚠️ **Provenance:** the 14-day lead time for major updates carries from the existing Formal Definition. The four-element notification content schema synthesises Stanford monitoring framework requirements (cited Source) with MHRA PMS notification practice. Specific numerical thresholds per severity (14 / 7 / 0 days, 100 % content-element gate) are **proposed in v3.5 as starting points**, not externally validated. Indicative; require local calibration against contractual SLA before procurement use.
>
> - **Pre-deployment gate (procurement):** vendor contractually commits to the four-element schema and the per-severity lead times below; vendor demonstrates a recent change-event with full notification on file.
> - **Continuous monitoring:** major changes notified ≥ 14 days before deployment; moderate changes ≥ 7 days; minor changes ≥ 0 days (post-hoc notification acceptable). Per-element completeness = 100 % across all severities. Substantial-change flag present on every applicable change.
> - **Pause / escalation trigger:** any major change deployed without prior notification; OR any substantial-change-flag-applicable change deployed without the regulatory flag (this is a regulatory event); OR per-element completeness < 95 % over a rolling 90-day window.

**References**

- **Stanford**: [Keyes et al. (2025) - Stanford monitoring framework](https://arxiv.org/abs/2512.09048)

**Limitations**

> Vendor compliance is only verifiable if independent monitoring can detect undisclosed model changes - which requires model version tracking infrastructure. The Operational Specification's reliance on [GV.SG-1](#gv-sg-1) telemetry surfaces this dependency: the metric is only as reliable as the per-component versioning the vendor exposes.

**Novel Thinking / Implications**

> 💡 This should be a contractual requirement in NHS procurement, not a voluntary practice. The three-layer surveillance model depends on it: national detection → regional evaluation → local monitoring. Without vendor notification, the entire surveillance chain is reactive rather than proactive.

---

### GV.VT-2 🟡 Telemetry Provision Completeness

Whether the vendor provides the operational data needed for deployer-side monitoring: per-inference logging, confidence scores, model version per output, intermediate outputs for error attribution, and demographic performance data.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.VT-2 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

> Vendors may resist due to commercial sensitivity or technical cost. Telemetry provision must be contractually specified - voluntary provision is unreliable.

**Novel Thinking / Implications**

> 💡 This is the meta-metric: without adequate telemetry, most other continuous monitoring metrics are unmeasurable. Telemetry provision completeness should be a procurement gate - if a vendor cannot provide minimum telemetry, the system cannot be governed, and deployment should not proceed.

---

### GV.VT-3 🔵 Benchmark & Evaluation Data Accessibility

Whether the vendor provides access to benchmarking infrastructure: test datasets, evaluation scripts, baseline results, and the ability for deployers to run independent evaluations.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.VT-3 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | Proposed - vendors currently self-evaluate with proprietary benchmarks |

**Why this tier?**

> Aspirational. Vendors self-evaluate on proprietary benchmarks. National NHS AVT benchmark suite would transform assurance but doesn't yet exist.

**Formal Definition**

```
Accessibility score across dimensions: (a) test dataset availability, (b) evaluation script reproducibility, (c) baseline result transparency, (d) deployer ability to run independent benchmarks, (e) third-party audit access. Binary per dimension; composite = sum/5.
```

**Limitations**

> Vendors argue test datasets contain proprietary or sensitive data. Standardised NHS-specific benchmarks don't yet exist. Third-party evaluation infrastructure requires investment.

**Novel Thinking / Implications**

> 💡 The fundamental transparency problem: vendors evaluate their own systems on their own benchmarks and report their own results. Independent evaluation requires benchmark accessibility. A national NHS AVT benchmark suite - with standardised test encounters, ground truth annotations, and evaluation scripts - would transform the assurance landscape from vendor self-assessment to independent verification.

---

### GV.VT-4 🟡 Audit Trail Completeness

Whether the system maintains a complete, tamper-evident audit trail from audio input to EPR output - sufficient for retrospective incident investigation, complaint resolution, and regulatory inspection.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.VT-4 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

### GV.VT-5 🟢 Incident Disclosure Compliance

Does the vendor disclose security incidents, model failures, and known issues to deployers in a timely manner? Includes both incidents at the vendor and incidents discovered at other deployer sites that may affect this deployer.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.VT-5 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | Standard security incident disclosure practice |

**Why this tier?**

> Should be a contractual requirement. Without timely incident disclosure, deployers cannot respond to vendor-side security issues.

**Formal Definition**

```
Disclosure Timeliness = t_disclosed - t_incident_known_by_vendor. Disclosure Completeness = |required_information_provided| / |required_information_categories|. Required: incident description, affected functionality, mitigation, recommended actions.
```

**Reference Standard**

> Authoritative source: vendor incident log paired with deployer notification record. `t_incident_known_by_vendor` is the earliest of: (a) vendor's own detection telemetry; (b) report from another deployer; (c) external (e.g. researcher) disclosure. Vendor self-classification of "knowing time" is rebuttable — if independent evidence (security advisories, public disclosure, regulator notice) establishes earlier knowledge, that timestamp is authoritative. Cross-link to UK NIS regulations and ICO Article 33 timelines for data-breach incidents (72-hour deployer-side notification obligation cascades from vendor disclosure). Incident severity classified per a deployer-defined schema; default: critical (active patient safety risk or active data exposure), high (potential exposure pending mitigation), medium (vulnerability disclosed and patched), low (informational).

**Operational Specification**

> - **Window:** continuous; per-incident tracking with monthly compliance reporting.
> - **Population:** every incident the vendor knows about, with cross-deployer scope explicit (an incident at deployer A that affects deployer B's exposure must reach deployer B).
> - **Severity classification MANDATORY:** every incident classified critical / high / medium / low with disclosure-timeline expectations differing per severity.
> - **Five mandatory content elements:** (a) incident description with affected components named per [GV.SG-1](#gv-sg-1) taxonomy; (b) affected functionality and known scope of impact; (c) mitigation in progress or completed (with timeline); (d) recommended deployer actions; (e) cross-deployer scope (which deployers / configurations / use cases are affected). The fifth element is the most commonly omitted — vendors often disclose in vendor-frame ("we patched X") without translating to deployer impact ("you should check Y in your deployment"). Notifications missing any element count as non-compliant regardless of timing.
> - **Update cadence MANDATORY:** initial disclosure plus material updates as new information emerges; final closure report on resolution. A single one-off notification without updates is non-compliant where the incident has not been resolved.
> - **Escalation path MANDATORY:** named deployer contact for critical and high incidents; vendor must demonstrate the escalation path was used, not just the standard support inbox.

**Threshold Guidance**

> ⚠️ **Provenance:** the four-element framing carries from the existing Formal Definition; the fifth element (cross-deployer scope) and the severity-driven timelines synthesise standard security incident disclosure practice (cited Source) with ICO Article 33 cascade logic. Specific numerical thresholds (24-hour critical, 72-hour high, 7-day medium, 30-day low; 100 % five-element gate) are **proposed in v3.5 as starting points**, not externally validated. Indicative; require local calibration against contractual SLA before procurement use.
>
> - **Pre-deployment gate (procurement):** vendor contractually commits to severity-classified disclosure timelines and the five-element content schema; named deployer contact recorded; one tabletop test of the disclosure path.
> - **Continuous monitoring:** critical incidents disclosed ≤ 24 hours from `t_known`; high ≤ 72 hours; medium ≤ 7 days; low ≤ 30 days. Five-element completeness = 100 %. Escalation path used for every critical and high incident.
> - **Pause / escalation trigger:** any critical incident disclosed > 72 hours after `t_known` (regardless of severity-classification target); OR any incident where independent evidence shows vendor knew earlier than disclosed `t_known`; OR cross-deployer-scope element missing on incidents affecting multiple deployments. All three are contract-breach triggers.

**Limitations**

> Vendor incentives often favour minimising disclosure. Requires contractual specification. The Operational Specification's rebuttable-knowing-time clause and cross-deployer-scope mandate make the most common evasion patterns explicit, but verification still depends on the deployer's ability to detect independent evidence of earlier knowledge — itself an asymmetric capability problem.

**Novel Thinking / Implications**

> 💡 When a security incident occurs at the vendor (e.g. the Mindgard jailbreak disclosures), affected deployers need to know quickly to assess their own exposure. Vendors often delay disclosure or provide minimal information. Contractual specification of disclosure timeframes and content is necessary.

---

### GV.VT-6 🟡 Exit & Data Portability Provisions

When a deployer terminates their contract, can they export their data, audit trails, and configurations in usable formats? Vendor lock-in is a governance risk that affects switching costs and competitive procurement.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.VT-6 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

### GV.VT-7 🟢 Sub-Processor Transparency

Does the vendor disclose all third parties with access to data: cloud providers, model providers, annotation services, support contractors? UK GDPR Article 28 requires this. Each sub-processor is a potential data exposure point.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.VT-7 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | UK GDPR Article 28 |

**Why this tier?**

> Legal compliance requirement under UK GDPR Article 28. Must be assessed at procurement and monitored for changes.

**Formal Definition**

```
Audit vendor's sub-processor list against actual data access. Completeness = |disclosed_subprocessors| / |actual_subprocessors|. Verification: review data flow diagrams, cloud architecture, support contracts. Each sub-processor should have its own data protection assessment.
```

**Reference Standard**

> Vendor's published sub-processor list (the disclosed set) audited against the actual data-access surface (the discovered set). The discovered set is constructed from: (a) data-flow diagrams; (b) cloud architecture (IaaS/PaaS providers, CDN, log aggregation, monitoring telemetry); (c) third-party model providers (e.g. foundation-model APIs); (d) annotation, labelling, or human-review services; (e) support, customer-success, and engineering contractors with production-data access; (f) backup and disaster-recovery providers; (g) sub-sub-processors named in any of the above's published lists. UK GDPR Article 28(2) is the legal floor; "sub-processor" here includes any entity that processes personal data on the vendor's instructions, regardless of how the vendor labels the relationship internally. Each sub-processor in scope must have its own DPA in place ([GV.PD-9 Cross-Border Data Transfer Compliance](#gv-pd-9) cross-link for non-UK locations).

**Operational Specification**

> - **Window:** continuous; quarterly audit cadence with notification-driven re-audits on any vendor sub-processor change.
> - **Population:** every sub-processor with any data-access path (transitively). The discovered set explicitly extends to sub-sub-processors — a vendor's cloud provider's storage region's sub-contractor for backup is in scope if it can reach personal data.
> - **Per-sub-processor reporting MANDATORY:** for each sub-processor: name, processing purpose, data categories, location, DPA status (in-place / signed / pending), Article 46 safeguard (where non-UK). Aggregate completeness ratio insufficient — the failure pattern (which sub-processor is undisclosed) matters more than the count.
> - **Discovery method MANDATORY:** the deployer's verification method MUST be declared (data-flow diagram review / cloud-architecture audit / contract trace / penetration test). Pure self-certification by the vendor is not Tier 1 sufficient; some independent verification step required.
> - **Change-notification mandate:** vendor contract MUST specify advance notice of sub-processor changes ([GV.VT-1 Model Change Notification Compliance](#gv-vt-1) cross-link); change-events tracked per sub-processor with notification timestamps.
> - **Materiality flag:** sub-processors handling personal data classified material; sub-processors handling only metadata or aggregated telemetry classified non-material. Material sub-processors required to be in scope; non-material classification must be evidenced.

**Threshold Guidance**

> ⚠️ **Provenance:** the seven-source discovered-set framing follows from UK GDPR Article 28(2) and standard DPIA practice; the materiality distinction synthesises ICO guidance on processor obligations. Specific numerical thresholds (quarterly audit cadence, 30-day pre-change notification, 100 % material-sub-processor disclosure gate) are **proposed in v3.5 as starting points**, not externally validated. Indicative; require local calibration against the deployer's IG framework before contractual use.
>
> - **Pre-deployment gate (procurement):** vendor publishes complete sub-processor list with the per-sub-processor information schema above; deployer-side verification step completed (not vendor self-cert alone); DPAs in place for every material sub-processor.
> - **Continuous monitoring:** quarterly discovered-set vs disclosed-set audit; per-material-sub-processor DPA status reviewed annually; change-event notifications received ≥ 30 days before sub-processor change for material entries.
> - **Pause / escalation trigger:** any material sub-processor undisclosed (regulatory failure under Article 28(2), not contractual); OR any material sub-processor without an in-place DPA; OR sub-processor change without prior notification (contractual breach where the contract specifies notification obligation).

**References**

- **UK GDPR**: UK GDPR Article 28 - processor obligations including sub-processor disclosure

**Limitations**

> Vendors often have complex, evolving sub-processor arrangements. Disclosure may not be complete or up-to-date. The Operational Specification's discovered-set framework makes the discovery method explicit; it does not eliminate the asymmetric-information problem that a vendor knows its supply chain better than the deployer can reconstruct it.

**Novel Thinking / Implications**

> 💡 Each sub-processor is a data processing entity that must comply with UK GDPR. If the vendor uses an undisclosed sub-processor (e.g. an offshore annotation service), this is both a compliance failure and a potential security risk. Disclosure should be a contractual requirement with notification obligations for changes.

---

### GV.VT-8 🟡 Intermediate Output Access

Whether the vendor provides contractual access to intermediate pipeline outputs - the raw transcript, the diarised transcript, the pre-coding summary, the model-internal confidence scores - rather than exposing only the final note. Prerequisite for the existing Error Attribution Analysis metric, and necessary for meaningful incident investigation. Without intermediate outputs, when an error is discovered in the final note, the investigation cannot determine which pipeline stage introduced it.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.VT-8 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | Prerequisite for existing Error Attribution Analysis metric; Stanford monitoring framework |

**Why this tier?**

> Procurement gate. Should be contractually specified. Required for any deployer intending to run Error Attribution Analysis, Chain of Custody traces, or Safety-Critical Information Chain of Custody (which is Tier 2 in the existing taxonomy but depends on intermediate output access to be executable).

**Formal Definition**

```
Access assessed across stages: (1) raw ASR transcript; (2) diarised transcript with speaker labels; (3) pre-summarisation processing outputs; (4) generated summary before coding; (5) coding suggestions before selection; (6) final output; (7) model confidence scores per stage. Access granularity: on-demand for individual encounters (required for incident investigation); bulk export for audit (required for Error Attribution Analysis); real-time streaming (optional, useful for monitoring). Binary per stage; target is full access to stages 1–6 on demand, with confidence scores (7) as advanced capability.
```

**Limitations**

> Vendors resist intermediate output access on commercial grounds - the intermediate outputs reveal pipeline architecture and model choices. Contractual access may be granted at high cost or with usage restrictions. Without independent verification, deployers cannot confirm that the "intermediate outputs" provided are authentic rather than reconstructions.

**Novel Thinking / Implications**

> 💡 Many of the highest-value metrics in this taxonomy - Error Attribution Analysis, Source-to-Record Concordance, Safety-Critical Information Chain of Custody, Error Cascade Analysis - depend on intermediate output access that vendors rarely provide. Making this a procurement gate creates pressure for vendors to either provide access or compete on terms with those who do. Without contractual intermediate output access, most sophisticated assurance metrics are theoretical rather than operational.

---

### ES.ME-1 🔵 Proximal vs Distal Outcome Distinction

The most important structural critique: measuring easy things and assuming they correlate with hard things. Require causal logic models.

| Dimension | Value |
|-----------|-------|
| **Reference** | ES.ME-1 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | National Body, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
| **Source** | Coiera & Fraile-Navarro 2026; NIHR RSET |

**Why this tier?**

> Structural critique of the evaluation field. Not a metric to implement but a framework for assessing all other metrics. National/academic responsibility.

**Formal Definition**

```
Proximal P = {WER, edit_rate, doc_time}. Distal D = {safety events, care quality, patient outcomes}. For each pᵢ, require causal model: pᵢ → [mechanism] → dⱼ with evidence. Burden on vendors/deployers to demonstrate P→D.
```

**References**

- **Editorial**: Coiera & Fraile-Navarro (2026) - JMIR Med Inform
- **RSET**: NIHR RSET Phase 1

**Limitations**

> Distal outcomes slow to manifest, hard to attribute.

**Novel Thinking / Implications**

> 💡 National evaluation standard should require explicit causal logic models with burden of proof on vendors. ES.ME-1 names that burden; [ES.ME-9 Causal Model Operationalisation](#es-me-9) makes it a measurable procurement requirement, and [ES.ME-8 Outcome Evidence Commitment Status](#es-me-8) measures whether the distal evidence is being generated. See also [Outcomes Boundary](#outcomes-boundary) for the explicit scope statement.

---

### ES.ME-2 🔵 Inter-Rater Reliability Baseline

Clinician agreement ceiling. VeriFact exceeds it (92.7% vs 88.5%). When automated metrics beat humans, what does that mean?

| Dimension | Value |
|-----------|-------|
| **Reference** | ES.ME-2 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Academic |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

### ES.ME-3 🔵 Metric Interaction Analysis

Do the metrics in the taxonomy correlate or conflict? A system optimised for low edit rate might achieve it through over-summarisation that increases omission rate. Multi-metric monitoring requires understanding interactions.

| Dimension | Value |
|-----------|-------|
| **Reference** | ES.ME-3 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | National Body, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
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

> 💡 Without interaction analysis, governance can drive perverse outcomes. A practice told to reduce edit rate might pressure clinicians to edit less - but the AI hasn't improved, so the underlying error rate is unchanged. Edit rate goes down, hallucination rate goes up. This is the kind of failure that interaction analysis catches.

---

### ES.ME-4 🟡 Goodhart's Law Monitoring

When a metric becomes a target, does it cease to be a good measure? Specifically tracking whether metrics are being gamed - optimised in ways that satisfy the metric without achieving the underlying goal.

| Dimension | Value |
|-----------|-------|
| **Reference** | ES.ME-4 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Regional (ICB) |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
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

### ES.ME-5 🔵 Coverage Gap Analysis

What failure modes are not captured by any metric in the taxonomy? Periodic review of incidents to identify metric blindspots. The taxonomy itself must evolve as new failure modes emerge.

| Dimension | Value |
|-----------|-------|
| **Reference** | ES.ME-5 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | National Body, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
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

> 💡 The taxonomy is not static. As AVT evolves and new failure modes emerge, the taxonomy must evolve to cover them. Coverage gap analysis is the mechanism for this evolution - every incident should prompt the question 'would our metrics have caught this?' If not, that's a gap to fill.

---

### ES.ME-6 🔵 LLM-Judge Bias Quantification

Systematic measurement of known biases in LLM-as-a-Judge evaluation: position bias (prefers first response in pairwise comparison), verbosity bias (prefers longer responses), self-enhancement bias (prefers outputs from the same model family), and fine-grained scoring unreliability (inconsistent discrimination at high score ranges). Required for interpreting LLM-Judge metrics responsibly. The Croxford et al. 2025 study found GPT-o3-mini achieving ICC 0.818 with human evaluators on PDSQI-9 - but a separate Rwanda clinical LLM evaluation study found LLM judges correlated more strongly with non-expert than expert annotators, indicating that apparent reliability may reflect alignment with a particular class of evaluator rather than with ground truth.

| Dimension | Value |
|-----------|-------|
| **Reference** | ES.ME-6 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Academic, National Body |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | Croxford et al. 2025 (npj Digital Medicine); Rwanda clinical LLM evaluation study |

**Why this tier?**

> Research-grade meta-evaluation. Academic and national body responsibility. Not routinely performed but necessary for anyone relying on LLM-as-a-Judge outputs for safety-critical decisions.

**Formal Definition**

```
Bias tests: (1) Position bias - reverse pairwise ordering and measure agreement with original judgment (perfect judge = 100% consistency under reversal); (2) Verbosity bias - compare judgments on pairs matched on quality but varying in length; (3) Self-enhancement - test judge on outputs from its own model family vs other families; (4) Score range reliability - measure inter-rater agreement at high scores (e.g. 4 vs 5 on Likert) vs across full range. Composite: bias-adjusted reliability = raw reliability corrected for each bias type.
```

**Limitations**

> Bias testing requires carefully constructed adversarial test sets. Results don't transfer across judge models or domains. Bias adjustments are approximations, not corrections.

**Novel Thinking / Implications**

> 💡 The Rwanda finding is the uncomfortable one: LLM judges may correlate well with human evaluators while correlating poorly with ground truth. This is the worst failure mode for evaluation - apparent reliability that validates a biased assessment. Any deployment relying on LLM-as-a-Judge for safety decisions (not just for efficiency) needs to have run bias quantification and documented the residual uncertainty. Otherwise the high ICC number is theatrical rather than informative.

---

### ES.ME-7 🔵 Automated-Human Metric Concordance

Systematic measurement of how well automated metrics correlate with expert human evaluation across deployments. Meta-metric that validates (or invalidates) the automated metrics themselves. Without concordance measurement, automated metrics are running on the assumption that they track what human experts would measure - but the ROUGE Kendall-Tau finding of 0.080 with human clinical judgment (Croxford et al. 2025) shows that assumption can be wildly wrong.

| Dimension | Value |
|-----------|-------|
| **Reference** | ES.ME-7 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | National Body, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
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

> 💡 This is the metric that polices the other metrics. Without concordance data, the taxonomy's automated metrics are running on an unverified assumption that they measure what human experts measure. The ROUGE finding is the canonical example of that assumption failing - a metric in widespread use has essentially zero correlation with clinical judgment and is used anyway because it's easy to compute. Periodic concordance measurement should be a national evaluation programme responsibility, and any metric with concordance < 0.3 should be explicitly flagged in the taxonomy as inadequate as a standalone indicator.

---

### ES.ME-8 🟡 Outcome Evidence Commitment Status

Whether the vendor and deployer have committed - contractually, via published protocol, or via post-market surveillance plan - to evaluating the actual clinical outcomes of AVT deployment. Operationalises the boundary set by [Outcomes Boundary](#outcomes-boundary): this taxonomy does not measure clinical outcomes, but it can measure whether outcome evaluation is in train.

| Dimension | Value |
|-----------|-------|
| **Reference** | ES.ME-8 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate; reviewed annually |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Documentary |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer, National Body |
| **Maturity** | Emerging |
| **Outcome Type** | Process |
| **Applicability** | General Healthcare AI |
| **Source** | This taxonomy v3.3; T.E.S.T. Section B Clinical Effectiveness (50 pts RCT validation); MHRA Post-Market Surveillance Regulations 2024 |

**Why this tier?**

> A deployment cannot satisfy T.E.S.T. Gold without RCT or sufficiently powered NHS pilot evidence. Procurement above pilot scale should require demonstrable commitment to outcome evaluation even where the evidence is not yet available. Tier 2 because it is documentary - no instrumentation - and because pilots and small-site deployments may legitimately not yet have outcome studies in train.

**Formal Definition**

```
Composite of four binary checks against documentary evidence:
  C1 = clinical-trial protocol registered (ISRCTN, ClinicalTrials.gov, or equivalent)
       OR equivalent NHS pilot study protocol with pre-registered primary outcome
  C2 = post-market surveillance plan exists and names patient-outcome signals
       (incident rate, diagnostic accuracy, medication errors, etc.)
       distinct from technical-performance signals
  C3 = data-collection infrastructure exists at deployment site sufficient to detect
       change in named outcome signals (baseline data; case ascertainment method;
       comparator arm or pre/post design)
  C4 = vendor contractually committed to share post-market outcome data with
       deployer and (where applicable) with national bodies
Score = number of checks passed (0-4). Tier 2 expectation: ≥ 2 of 4 at procurement;
≥ 3 of 4 within 12 months of deployment.
```

**Limitations**

> Documentary; does not verify the *quality* of the protocol or the *power* of the study. A registered trial may be underpowered, badly designed, or never report results. C2 and C3 are vendor-asserted unless deployer audits them. Treats commitment as a proxy for eventual evidence; that proxy can fail (the [Roadmap as Graveyard](#outcomes-boundary) risk - protocols register but evidence never lands). Pair with periodic re-check of whether registered studies are progressing.

**Novel Thinking / Implications**

> 💡 The honest answer to "does this AVT improve patient outcomes?" is almost always "we don't know yet" - because the field has not produced the evidence and most deployments are not generating it. ES.ME-8 forces that uncertainty into the open at procurement. A vendor scoring 0/4 is selling on technical-performance evidence alone; a vendor scoring 4/4 has committed to producing the evidence the field is missing. Either is acceptable as long as the deployer chooses with eyes open. The metric does not establish clinical benefit - it establishes whether anyone is trying to.

---

### ES.ME-9 🟡 Causal Model Operationalisation

Whether the vendor has documented an explicit causal chain from the proximal metrics in this taxonomy (or its own equivalents) to the distal outcomes claimed at procurement. Makes [ES.ME-1 Proximal vs Distal Outcome Distinction](#es-me-1)'s "burden of proof" requirement operational.

| Dimension | Value |
|-----------|-------|
| **Reference** | ES.ME-9 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate; updated when outcome claims change |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Documentary |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Process |
| **Applicability** | General Healthcare AI |
| **Source** | This taxonomy v3.3; ES.ME-1 (proximal/distal causal-logic framework); Coiera & Fraile-Navarro 2026 (structural critique) |

**Why this tier?**

> Vendors making outcome claims at procurement (faster documentation, fewer errors, improved patient experience) should be required to specify the causal chain by which their proximal performance translates to those outcomes. Without that chain, the procurement claim is unfalsifiable. Tier 2 because it is documentary and one-off; the burden is on the vendor making the claim, not on continuous measurement.

**Formal Definition**

```
For each outcome claim O made at procurement (e.g. "reduces documentation time",
"reduces medication errors", "improves patient experience"):
  S1 = vendor names the proximal metrics P_1..P_n that, if measured, would constitute
       evidence for or against O (where P_i are drawn from this taxonomy or named
       vendor-specific equivalents with comparable definitions)
  S2 = vendor specifies the mechanism linking each P_i to O (the causal step from
       proximal performance to distal outcome - e.g. "lower hallucination rate
       reduces clinician verification burden which reduces after-hours review which
       reduces documentation time outside consultations")
  S3 = vendor cites or commits to producing evidence for each linking mechanism
       (literature, internal study, external trial)
  S4 = vendor identifies known confounders and threats to the causal claim
       (Hawthorne effects, selection bias, secular trends, concurrent interventions)
Score per claim = number of stages documented (0-4). Composite for the deployment =
mean score across all outcome claims. Tier 2 expectation: ≥ 3 of 4 on every claim
made at procurement.
```

**Limitations**

> Documentary; does not verify that the cited mechanisms are plausible or supported. Vendors can produce a causal model that *looks* coherent but is empirically wrong (the ROUGE precedent: a metric in widespread use with Kendall-Tau 0.080 against clinical judgment). The metric forces the model into the open; deployer review still required. Becomes meaningful only when paired with [ES.ME-7 Automated-Human Metric Concordance](#es-me-7) for the proximal links and [ES.ME-8 Outcome Evidence Commitment Status](#es-me-8) for the distal evidence.

**Novel Thinking / Implications**

> 💡 This metric exposes a common procurement failure mode: vendors making outcome claims ("reduces clinician burnout", "improves patient outcomes") backed by proximal evidence ("our hallucination rate is 1.5%") with no documented causal chain connecting the two. The chain may be sound, weak, or nonexistent - but without it being written down, the deployer cannot evaluate the claim. Forcing the chain into the procurement documentation does not validate it; it makes validation possible. Deployers who require this metric can compare causal models across vendors and identify which are operating on evidence and which on assumption.

---
