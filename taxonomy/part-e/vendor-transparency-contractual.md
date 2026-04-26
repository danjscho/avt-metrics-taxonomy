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

> Vendor change-event log paired with deployer notification record. The change-event taxonomy follows [GV.SG-1 Model Version Tracking](#gvsg-1-model-version-tracking) — the six versioned components (ASR / LLM weights / prompt / retrieval / safety classifier / fine-tunes). A "notification" requires written communication to the named deployer contact (not generic vendor newsletter or status page) containing the four mandatory content elements (a-d below). Cross-link to MHRA Post-Market Surveillance Regulations 2024 (SI 2024 No. 1368): changes meeting the "substantial" threshold trigger separate regulatory notification obligations and MUST be flagged as such.

**Operational Specification**

> - **Window:** continuous; per-change-event tracking with monthly compliance reporting.
> - **Population:** every change-event recorded by [GV.SG-1](#gvsg-1-model-version-tracking) telemetry. Denominator is change-events, not calendar months.
> - **Severity classification MANDATORY:** every change classified as **major** (component-level rewrite, scope expansion, retraining with new data, regulatory-substantial), **moderate** (incremental retraining, prompt revision, retrieval index update), or **minor** (bug fix, performance optimisation without behavioural change). Lead-time requirements differ per severity (Threshold Guidance below).
> - **Four mandatory content elements per notification:** (a) what changed (component, version-from, version-to); (b) expected impact (clinical-benchmark deltas, edge cases, known failure modes affected); (c) validation results (named benchmarks, test corpora, sample sizes); (d) deployer action required (re-run [GV.SG-2 Model Update Impact Score](#gvsg-2-model-update-impact-score), schedule [GV.CR-6 Safety Case](#gvcr-6-clinical-safety-case-completeness) update, etc.). Notifications missing any element count as non-compliant regardless of timing.
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

> Vendor compliance is only verifiable if independent monitoring can detect undisclosed model changes - which requires model version tracking infrastructure. The Operational Specification's reliance on [GV.SG-1](#gvsg-1-model-version-tracking) telemetry surfaces this dependency: the metric is only as reliable as the per-component versioning the vendor exposes.

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
> - **Five mandatory content elements:** (a) incident description with affected components named per [GV.SG-1](#gvsg-1-model-version-tracking) taxonomy; (b) affected functionality and known scope of impact; (c) mitigation in progress or completed (with timeline); (d) recommended deployer actions; (e) cross-deployer scope (which deployers / configurations / use cases are affected). The fifth element is the most commonly omitted — vendors often disclose in vendor-frame ("we patched X") without translating to deployer impact ("you should check Y in your deployment"). Notifications missing any element count as non-compliant regardless of timing.
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

> Vendor's published sub-processor list (the disclosed set) audited against the actual data-access surface (the discovered set). The discovered set is constructed from: (a) data-flow diagrams; (b) cloud architecture (IaaS/PaaS providers, CDN, log aggregation, monitoring telemetry); (c) third-party model providers (e.g. foundation-model APIs); (d) annotation, labelling, or human-review services; (e) support, customer-success, and engineering contractors with production-data access; (f) backup and disaster-recovery providers; (g) sub-sub-processors named in any of the above's published lists. UK GDPR Article 28(2) is the legal floor; "sub-processor" here includes any entity that processes personal data on the vendor's instructions, regardless of how the vendor labels the relationship internally. Each sub-processor in scope must have its own DPA in place ([GV.PD-9 Cross-Border Data Transfer Compliance](#gvpd-9-cross-border-data-transfer-compliance) cross-link for non-UK locations).

**Operational Specification**

> - **Window:** continuous; quarterly audit cadence with notification-driven re-audits on any vendor sub-processor change.
> - **Population:** every sub-processor with any data-access path (transitively). The discovered set explicitly extends to sub-sub-processors — a vendor's cloud provider's storage region's sub-contractor for backup is in scope if it can reach personal data.
> - **Per-sub-processor reporting MANDATORY:** for each sub-processor: name, processing purpose, data categories, location, DPA status (in-place / signed / pending), Article 46 safeguard (where non-UK). Aggregate completeness ratio insufficient — the failure pattern (which sub-processor is undisclosed) matters more than the count.
> - **Discovery method MANDATORY:** the deployer's verification method MUST be declared (data-flow diagram review / cloud-architecture audit / contract trace / penetration test). Pure self-certification by the vendor is not Tier 1 sufficient; some independent verification step required.
> - **Change-notification mandate:** vendor contract MUST specify advance notice of sub-processor changes ([GV.VT-1 Model Change Notification Compliance](#gvvt-1-model-change-notification-compliance) cross-link); change-events tracked per sub-processor with notification timestamps.
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
