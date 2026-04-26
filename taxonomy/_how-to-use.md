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

### Applicability dimension

Every metric carries an **Applicability** row in its dimension table (added in v3.6) classifying it as one of:

- **AVT-Specific** (48 metrics) — only meaningful for ambient voice technology; would not transfer to other clinical AI without significant reformulation
- **AVT-Contextualised** (77 metrics) — has wider relevance to clinical AI but needs AVT-specific context to be operational
- **General Healthcare AI** (91 metrics) — applies to clinical AI generally; AVT is one application

Use the classification when reading the taxonomy as a whole: the `AVT-Specific` set is the irreducible core of *this* taxonomy; the `General Healthcare AI` set is the part most likely to be reused by adjacent assurance frameworks. The classification is also exposed as a column in `dist/metrics.csv` for downstream filtering. The summary tables in [`_applicability.md`](#applicability-classification) provide the per-group breakdown.

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

