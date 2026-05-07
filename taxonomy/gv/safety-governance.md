### GV.SG-1 🟢 Model Version Tracking

Logging which model version produces each output. Foundation for all continuous metrics - without it, performance changes are uninterpretable.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SG-1 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous; Event-triggered |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | [Keyes-Stanford-Monitoring-2025] |

**Change history:** v5.1.0 (Cadence updated to multi-value `Continuous; Event-triggered` — every model component change is itself the trigger for re-tracking, and the per-inference logging is the continuous component).

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
> - **Regulatory cross-link MANDATORY:** any change classified as "substantial" under [SI-2024-1368] (MHRA Post-Market Surveillance regulations) must be flagged in the change-event record with the regulatory reference, and surfaced through [GV.VT-1 Model Change Notification Compliance](#gv-vt-1).

**Trigger Conditions**

> ⚠️ **Provenance:** the monitoring framing carries from the Novel Thinking section and [Keyes-Stanford-Monitoring-2025] (three-principle monitoring framework: system integrity, performance, impact); the MHRA PMS regulatory tie-in derives from [SI-2024-1368] in force from 16 June 2025. Specific numerical thresholds (24-hour notification target, 14-day notification escalation, 100 % per-component versioning gate) are **proposed in v3.4 as starting points**, not externally validated. Indicative; require local calibration against contractual SLA before procurement use.
>
> - **Pre-deployment gate:** vendor demonstrates per-component versioning on a representative sample of inferences; change-event log schema documented; notification process documented and contractually committed.
> - **Continuous monitoring:** per-inference component-version coverage = 100 % (any inference missing a versioned component is a defect, not a rate); median deployer-notification latency ≤ 24 hours from change-event; alert if any change-event remains unnotified > 7 days.
> - **Pause / escalation trigger:** any inference produced without complete per-component version log; OR any change-event unnotified > 14 days; OR any "substantial" MHRA-PMS-relevant change deployed without prior deployer notification (this is a regulatory event, not just an operational one).
>
> Specific numerical starting points are deployment-context-dependent and live in [Threshold Reference: GV.SG-1](../thresholds.md#gv-sg-1). Treat them as starting points to calibrate locally — not as contractual gates.



**References**

- **Stanford**: [Keyes-Stanford-Monitoring-2025]

**Limitations**

> Not contractually mandated in most NHS procurement. The Operational Specification's per-component versioning requirement makes this gap visible at procurement-time but does not close it - vendors can decline to log all six components, in which case the deployer is choosing to forgo Tier 1 assurance for that part of the stack.

**Novel Thinking / Implications**

> 💡 NHS-context three-tier surveillance shape (taxonomy-original; distinct from the Keyes et al. three-principle monitoring framework that this metric's Source row anchors to): detected nationally (contractual), evaluated regionally (benchmark), monitored locally (edit-pattern shift).

---

### GV.SG-2 🟡 Model Update Impact Score

Standardised before/after on update. Governance: vendor notifies → regional benchmark → local monitoring.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SG-2 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Event-triggered |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Regional (ICB) |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | [NAS-Day-Zero-SPI-internal]; [Keyes-Stanford-Monitoring-2025] |

**Why this tier?**

> Triggered by model version changes. Requires vendor notification and deployer/regional benchmark suite. The Keyes et al. monitoring framework (system integrity / performance / impact) depends on this.

**Formal Definition**

```
Impact IS = Σ w_m × (metric_new - metric_old) / metric_old. Mandatory re-evaluation if IS < -0.05 on any safety metric.
```

**References**

- **NAS**: [NAS-Day-Zero-SPI-internal] (taxonomy-author's prior framing, internal source)
- **Stanford**: [Keyes-Stanford-Monitoring-2025] — three-principle monitoring framework (system integrity, performance, impact)

**Limitations**

> Requires vendor notification + deployer benchmark capacity.

**Novel Thinking / Implications**

> 💡 Benchmark suite should be nationally standardised for cross-site comparison.

---

### Longitudinal Drift & Model Contamination sub-cluster

*Addresses the temporal dimension of model assurance that the current taxonomy handles only partially. Where the existing Model Version Tracking and Model Update Impact Score metrics cover notified changes, these metrics cover silent drift, contamination of future training pipelines by AI-generated content, and the regulatory frameworks (FDA PCCP, NICE ESF 2022 AI updates) that increasingly require pre-specified change control plans.*

---

### GV.SG-3 🟢 Performance Degradation Detection Latency

Time delay between the onset of model performance degradation and its detection by the monitoring infrastructure. Distinct from the existing Model Update Impact Score, which measures the effect of notified updates at a known switchover point. This metric addresses silent degradation - performance decay that occurs without any vendor notification or identifiable event, from causes including data drift, infrastructure changes, or subtle model updates that are not disclosed.

|Dimension              |Value                                                              |
|-----------------------|-------------------------------------------------------------------|
| **Reference** | GV.SG-3 |
|**Priority Tier**      |🟢 Tier 1 - Minimum Viable                                             |
|**Measurement Cadence**|Continuous                                                         |
|**Pipeline Layer**     |Cross-cutting                                                      |
|**Assurance Question** |Safety                                                             |
|**Measurement Method** |Computational                                                      |
|**Lifecycle Phases**   |Continuous                                                         |
|**Responsible Actors** |Regional (ICB), National Body                                      |
|**Maturity**           |Proposed / Novel                                                   |
|**Outcome Type**       |Proximal                                                           |
|**Applicability**      |General Healthcare AI                                              |
|**Source**             |[NICE-ESF] 2022 AI-specific updates; drift detection literature|

**Change history:** v5.3.0 (promoted to Tier 1: MHRA Class 1 post-market surveillance — FTS notice Step 1.i directly requires PMS evidence; ongoing performance-degradation detection is a baseline expectation, not best-practice).

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
|**Lifecycle Phases**   |Pre-deployment                                    |
|**Responsible Actors** |Vendor                                                            |
|**Maturity**           |Emerging                                                          |
|**Outcome Type**       |Proximal                                                          |
|**Applicability**      |General Healthcare AI                                             |
|**Source**             |[FDA-PCCP-Guidance-2024]; [NICE-ESF] 2022 AI-specific additions|

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

The proportion of training or fine-tuning data that is itself AI-generated clinical content - either directly (notes written by earlier versions of the same AVT system used to train successors) or indirectly (clinical records that have been shaped by AI suggestions even where the final text was human-edited). Known in the machine learning literature as "model autophagy disorder" or "MAD". [He-AI-Contamination-Pathology-2026] (medRxiv preprint, February 2026) demonstrates progressive vocabulary collapse and disappearance of rare clinical findings (e.g. pneumothorax, effusion) across recursive training generations on AI-generated clinical content, with false-reassurance rates tripling and AI documentation rendered clinically unreliable within a small number of generations.

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
|**Source**             |[Alemohammad-MAD-2023]; [Shumailov-Curse-of-Recursion]; [He-AI-Contamination-Pathology-2026]|

**Change history:** v4.4 (re-attributed the model-autophagy claims to the actual He et al. medRxiv 2026 paper via the new [He-AI-Contamination-Pathology-2026] catalogue handle; replaced an unverifiable specific "98.9% by generation 4" number with the qualitative findings the paper does support).

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

Medical device safety paradigm for LLMs. Applies the Kalinich et al. 2025 simulation-based PRA framework — demonstrated on suicide-risk chatbot safety classification across 14 open-source models — to AVT contexts.

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
| **Source** | [Kalinich-LLM-SaMD-PRA-2025] (PRA framework demonstrated on suicide-risk chatbot safety, applied here to AVT) |

**Why this tier?**

> Research methodology. First published PRA for LLM-SaMD. Important for DCB0129 maturity but requires clinical harm pathway modelling that doesn't yet exist for AVT.

**Formal Definition**

```
P₁ = P(hazardous output | normal use). P₂ = P(harm | hazardous output). Risk R = P₁ × P₂ × Severity. P₂ requires clinical harm pathway modelling with probability attenuation at each stage.
```

**References**

- [Kalinich et al. 2025](https://www.medrxiv.org/content/10.1101/2025.11.10.25339903v1) — simulation-based PRA framework, 14 open-source LLMs (Qwen / Gemma / LLaMA, 270M–70B), evaluated on suicide-ideation / therapy-request / therapy-like-interaction safety classification. Provides P₁ and P₂ estimation methodology that GV.SG-7 applies to AVT.

**Limitations**

> Validated on open-source only. Commercial AVT = black box.

**Novel Thinking / Implications**

> 💡 For DCB0129: translating error rates into P₁/P₂ makes safety cases quantitative, not just qualitative.

---

### GV.SG-8 🔵 DeepScore (Defect-Free Rate)

Two-tier: Major Defect-Free Rate + Critical Defect-Free Rate. Vendor-disclosed evaluation scale (~135,900 notes per [DeepScore] methodology page). Sound approach but proprietary definitions.

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
| **Source** | [DeepScribe] |

**Why this tier?**

> Vendor-proprietary (DeepScribe). Sound two-tier severity approach but proprietary definitions prevent cross-vendor comparison.

**Formal Definition**

```
MDFR = |N_no_major| / |N_total|. CDFR = |N_no_critical| / |N_total|. Vendor-specific severity definitions - not aligned to external standard.
```

**References**

- **DeepScore**: [DeepScore] (vendor whitepaper; not a peer-reviewed academic preprint)

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
| **Source** | [AMLAS-AAIP]; [NAS-Day-Zero-SPI-internal] |

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
| **Source** | Compound boundary risk model; [NHS-LLM-Framework] |

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
| **Source** | [LFPSE] national reporting |

**Why this tier?**

> Established national reporting. The ultimate lagging indicator - by the time this metric moves, harm has occurred. Needs dedicated LFPSE category for AI/AVT incidents.

**Formal Definition**

```
IR = N_incidents / N_encounters. Stratify by severity. Currently no LFPSE taxonomy code for AI/AVT - coded under general documentation errors.
```

**References**

- **LFPSE**: [LFPSE] (NHS Learn From Patient Safety Events)

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

**Trigger Conditions**

> ⚠️ **Provenance:** the leading-vs-lagging indicator framing carries from the patient safety literature cited in Source. The two-source construction (active + inferred via [HL.HF-1](#hl-hf-1)) is **proposed in v3.5** as a way to address the well-documented under-reporting problem in clinical near-miss capture. Specific numerical thresholds (25 % active-to-inferred floor, ratio thresholds vs LFPSE) are **proposed in v3.5 as starting points**, not externally validated. Indicative; require local calibration against safety-culture baseline before contractual use.
>
> - **Pre-deployment / Day Zero baseline:** establish baseline active near-miss rate and inferred near-miss rate during the first 4 weeks; record per-category breakdown; pair with concurrent LFPSE rate.
> - **Continuous monitoring:** weekly two-source reporting; monthly cross-validation; alert when active-to-inferred ratio < 25 % sustained two months (under-reporting culture flag); alert when near-miss-to-LFPSE ratio falls (rising LFPSE without rising near-miss = review layer is failing, not improving).
> - **Pause / escalation trigger:** LFPSE rate rises while near-miss rate stays flat or falls (the leading indicator should rise BEFORE the lagging indicator if review is functioning); OR safety-critical-category near-miss rate falls > 50 % from baseline without corresponding documented system improvement (suggests complacency, cross-link [HL.HF-1 Edit Rate](#hl-hf-1) trajectory).
>
> Specific numerical starting points are deployment-context-dependent and live in [Threshold Reference: GV.SG-14](../thresholds.md#gv-sg-14). Treat them as starting points to calibrate locally — not as contractual gates.



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

*See also: SPI Escalation Response Time - paired latency metric. GV.SG-15 measures the time to fix a single confirmed incident; GV.SG-16 measures the time to escalate an SPI threshold breach.*

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
| **Source** | Operational extension of [AMLAS-AAIP] |

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

*See also: Safety Performance Indicators with Thresholds (DSCMS), Time-to-Correct - GV.SG-16 measures the response time to GV.SG-9 threshold breaches; meaningless without the SPI framework GV.SG-9 defines. Pair with GV.SG-15 as parallel response-latency metrics for different event types.*

---

### GV.SG-17 🟢 Hazard Log Completeness

DCB0129 requires a hazard log. Is it actually maintained and updated as new failure modes are discovered operationally? A static hazard log written at deployment and never updated is a compliance failure with safety implications.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.SG-17 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous; Event-triggered |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | [DCB0129] compliance requirement |

**Why this tier?**

> Regulatory requirement under DCB0129. Tier 1 because it's a compliance obligation, not a recommendation. Should be linked to operational monitoring.

**Formal Definition**

```
Hazard Log Currency = (date_of_last_update - today) in days. Hazard Coverage = |operationally_observed_failure_modes_in_log| / |total_observed_failure_modes|. Currency target: updated within 30 days of any new failure mode discovery.
```

**References**

- **DCB0129**: [DCB0129] hazard log requirement

**Limitations**

> Requires connecting operational monitoring to hazard log update process - often disconnected in current practice.

**Novel Thinking / Implications**

> 💡 DCB0129 hazard logs are often written once at deployment and forgotten. As operational monitoring discovers new failure modes (through edit pattern analysis, near-miss reporting, incident investigation), these should be added to the hazard log with mitigations. A hazard log that hasn't been updated in 6 months is either a perfect system or a compliance failure - and almost certainly the latter.

---

### GV.SG-18 🟡 PCCP Documentation Completeness

Whether the vendor's Predetermined Change Control Plan (PCCP) covers the full lifecycle obligations expected of an adaptive AI medical device — pre-specified change types, performance acceptance thresholds, regression test suite, fairness/equity acceptance criteria, rollback procedure, and audit-trail requirements. PCCPs are the structural mechanism by which retrained or fine-tuned AVT models update without requiring a new regulatory submission per change. **Sub-part of the PCCP construct paired with [GV.CR-9 FDA PCCP-Equivalent Pre-Defined Acceptance Criteria](#gv-cr-9)**: GV.CR-9 is the parent (substantive quality of the criteria); this metric is the structural-completeness counterpart. Both are needed for full PCCP assurance.

**Change history:** v5.4.0 (formalised parent + sub-part relationship with GV.CR-9 — GV.CR-9 is parent (substantive quality), GV.SG-18 is sub-part (structural completeness); Limitations updated to reflect formalised relationship).

|Dimension              |Value                                                   |
|-----------------------|---------------------------------------------------------|
| **Reference** | GV.SG-18 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                   |
|**Measurement Cadence**|One-off gate; Event-triggered                            |
|**Pipeline Layer**     |Cross-cutting                                            |
|**Assurance Question** |Safety                                                   |
|**Measurement Method** |Human Review                                             |
|**Lifecycle Phases**   |Pre-deployment                                           |
|**Responsible Actors** |Vendor                                                   |
|**Maturity**           |Emerging                                                 |
|**Outcome Type**       |Proximal                                                 |
|**Applicability**      |General Healthcare AI                                    |
|**Source**             |[MHRA-SaMD] AI Airlock + Change Programme; [FDA-PCCP-Guidance-2024] (cross-aligned)|

**Why this tier?**

> Tier 2 because PCCP applies specifically to adaptive / retrained models — not all AVT vendors update model weights post-deployment. For vendors that do, PCCP completeness is gate-level: a vendor that retrains without a documented change plan is operating outside the regulatory regime that legitimises post-deployment updates. As the structural-completeness sub-part of the PCCP construct, this metric is paired with the parent [GV.CR-9](#gv-cr-9) which tests the substantive quality of acceptance criteria.

**Formal Definition**

```
Pass per criterion: (1) PCCP scope statement enumerating which change types are pre-authorised (e.g. retraining cadence, threshold tuning, dictionary updates) and which require new submission; (2) Performance acceptance thresholds quantitative and pre-specified; (3) Regression test suite defined and version-controlled; (4) Fairness / equity acceptance criteria included; (5) Rollback procedure with named trigger conditions; (6) Audit-trail commitment for every PCCP-scope change. Full pass = all six.
```

**Limitations**

> Pairs with [GV.CR-9](#gv-cr-9) — the parent. This metric focuses on structural completeness of the documented plan; GV.CR-9 focuses on the meaningful quality of the criteria. The pairing is formalised in v5.4.0; both metrics are needed because a structurally complete PCCP can still have substantively weak criteria (and vice versa). Cross-cluster placement (CR vs SG) preserves the assurance-question split: GV.CR-9 sits in compliance-regulatory because it tests procurement-time quality; GV.SG-18 sits in safety-governance because it tests deployment-lifecycle structural completeness.

**Novel Thinking / Implications**

> 💡 PCCP completeness is the deployer's only practical lever to verify that vendor-side change control will hold up under inspection. Without a complete PCCP, every model update is a regulatory event the deployer has no visibility into until something goes wrong.

---

