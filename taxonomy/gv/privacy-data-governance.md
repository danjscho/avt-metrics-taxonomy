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
| **Source** | [UK-GDPR] Article 5(1)(e) storage limitation; [NHSE-IG-Guidance-2026-03] |

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

**Trigger Conditions**

> ⚠️ **Provenance:** the IG-incident reportability framing follows from [UK-GDPR] storage-limitation requirements and the existing [NHSE-IG-Guidance-2026-03] framework. Specific numerical thresholds (≥ 99.5 % monthly compliance, < 95 % escalation trigger, annual independent verification cadence) are **proposed in v3.3 as starting points**, not externally validated. Indicative; require local calibration against DPIA risk appetite before contractual use.
>
> - **Pre-deployment gate:** vendor produces a deletion-verification protocol covering every storage location in the architecture; deployer DPIA cross-references the protocol; one end-to-end deletion test passes prior to go-live.
> - **Continuous monitoring:** monthly compliance ≥ 99.5 % per storage location; alert on any single non-exception retention beyond policy; quarterly audit of exception log.
> - **Pause / escalation trigger:** any storage-location compliance < 95 % in any month, OR any unlogged retention beyond policy detected. Both are reportable as IG incidents per the existing NHSE IG framework.
>
> Specific numerical starting points are deployment-context-dependent and live in [Threshold Reference: GV.PD-1](../thresholds.md#gv-pd-1). Treat them as starting points to calibrate locally — not as contractual gates.



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
| **Source** | [NHSE-IG-Guidance-2026-03]; [UK-GDPR] Article 5(1)(e) storage limitation |

**Why this tier?**

> Direct compliance requirement. Measurable through vendor-provided deletion telemetry. Binary-ish: deletion within policy timeframe or not. Should be continuously monitored rather than periodically audited.

**Formal Definition**

```
Time-to-Deletion = t_deletion_verified - t_consultation_end. Report distribution: median, P95, P99, and count of encounters exceeding policy threshold. Verification requirement: deletion confirmed in primary storage, caches, backups, and any downstream analytic systems. Policy threshold per deployer: typically 24 hours to 7 days depending on DPIA. Compliance = proportion of encounters with verified deletion within threshold.
```

**Reference Standard**

> Inherits the storage-location enumeration and deletion-method definition from [GV.PD-1 Audio Retention Compliance](#gv-pd-1): primary vendor storage, backups and DR, vendor logs, downstream analytic systems, deployer-side caches, and named sub-processor systems per [GV.VT-7 Sub-Processor Transparency](#gv-vt-7). "Deletion" means cryptographic erasure or physical deletion (not logical/flagged-deleted). `t_consultation_end` is the clinician signature event on the AVT-generated note (sign-off triggers deletion under [NHSE-IG-Guidance-2026-03]); `t_deletion_verified` is the timestamp at which deletion is confirmed across every named storage location, not the timestamp at which deletion was initiated. Where the deployer's DPIA carves out retention for a named purpose, that purpose extends `t_deletion_verified` only for the carved-out subset and only for the carved-out duration.

**Operational Specification**

> - **Window:** continuous; monthly distribution reporting.
> - **Population:** every consultation audio captured during the window. No sampling — this is a compliance metric.
> - **Distribution reporting MANDATORY:** median, P95, P99, AND count of encounters exceeding policy threshold (the tail is the safety signal, not the median). Per-storage-location distribution where the architecture allows; otherwise the slowest-location time is the headline.
> - **Per-storage-location verification MANDATORY:** time-to-deletion measured against every storage location named in the GV.PD-1 enumeration. A median of 6 hours that hides 100 % retention in backups (where deletion never occurs) is non-compliant.
> - **Carve-out logging MANDATORY:** any audio retained beyond standard threshold under a DPIA carve-out logged with reason, duration, and re-deletion target date. Carved-out audio tracked in a separate distribution from standard audio; aggregating the two hides policy adherence.
> - **Deletion-verification method MANDATORY:** parallel to GV.PD-1 — vendor self-attestation alone insufficient; periodic independent verification (third-party audit, deployer-witnessed deletion test, or cryptographic proof via key destruction).

**Trigger Conditions**

> ⚠️ **Provenance:** the post-sign-off deletion expectation derives from [NHSE-IG-Guidance-2026-03]; [UK-GDPR] Article 5(1)(e) storage-limitation provides the legal floor. Specific numerical thresholds (24-hour median target, 7-day P99 ceiling, 1 % exceedance rate trigger) are **proposed in v3.5 as starting points**, not externally validated. The DPIA's policy threshold takes precedence where it differs (the DPIA-stated period is the contractual gate; these numbers are starting points for that DPIA conversation). Indicative; require local calibration before contractual use.
>
> - **Pre-deployment gate:** vendor demonstrates per-storage-location deletion telemetry; one end-to-end deletion test passes prior to go-live; DPIA cross-references the policy threshold.
> - **Continuous monitoring:** monthly median TTD ≤ DPIA-stated threshold (typically 24 hours); P99 ≤ 7 days; encounters-exceeding-threshold rate < 1 %; per-storage-location compliance ≥ 99.5 %.
> - **Pause / escalation trigger:** any single non-exception retention beyond DPIA threshold; OR median TTD > DPIA threshold in any month; OR per-storage-location compliance < 95 % (cascades to GV.PD-1 compliance failure). All three are reportable as IG incidents.
>
> Specific numerical starting points are deployment-context-dependent and live in [Threshold Reference: GV.PD-2](../thresholds.md#gv-pd-2). Treat them as starting points to calibrate locally — not as contractual gates.



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
| **Source** | [NHSE-IG-Guidance-2026-03]; [UK-GDPR] Article 5(1)(e) |

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

**Trigger Conditions**

> ⚠️ **Provenance:** [UK-GDPR] purpose-limitation underpins the requirement to enumerate retention purposes; specific numbers (≥ 3 distinct purposes, ≥ 99.5 % monthly compliance, ≥ 90 %-of-volume quality-monitoring sub-categorisation, < 95 % escalation trigger) are **proposed in v3.3 as starting points**, not externally validated. Indicative; require local calibration before contractual use.
>
> - **Pre-deployment gate:** DPIA enumerates ≥ 3 distinct retention purposes with periods; vendor architecture diagram shows transcript flow through every named storage location with retention period at each.
> - **Continuous monitoring:** monthly per-purpose, per-storage-location compliance ≥ 99.5 %; "quality monitoring" sub-categorisation alone covers ≥ 90 % of transcript volume (a vendor whose only purpose is "quality monitoring" is failing this gate).
> - **Pause / escalation trigger:** any unenumerated retention purpose discovered in production, OR any per-purpose compliance < 95 %.
>
> Specific numerical starting points are deployment-context-dependent and live in [Threshold Reference: GV.PD-3](../thresholds.md#gv-pd-3). Treat them as starting points to calibrate locally — not as contractual gates.



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
| **Source** | [UK-GDPR] Article 5(1)(c) data minimisation; DGX Spark / local processing potential |

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
| **Source** | [IEEE-S-and-P-2023-LLM-PII-Leakage]; [OWASP-LLM-Top-10] (Sensitive Information Disclosure) |

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
| **Source** | [ICO] anonymisation code of practice; [NIST-Privacy-Framework] |

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
| **Measurement Cadence** | One-off gate; Periodic audit; Event-triggered |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | [UK-GDPR] transparency requirements; derived from emerging AVT procurement practice |

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
| **Family** | NHSE IG Attestation |
| **Source** | [CQC-Mythbuster-109]; [NHSE-IG-Guidance-2026-03]; common law implied consent requirements |

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
> - **Understanding rate** is measured by structured patient survey. **No validated AVT-specific patient-comprehension instrument exists at the time of v3.7.** Deployers should either (a) select the closest healthcare-IT-comprehension instrument (e.g. eHealth Literacy items adapted for AVT context, Decision Conflict Scale items) and document the adaptation as a limitation, or (b) commission a deployer-defined survey reviewed by the IG team containing at least four comprehension items mapped to the [GV.CR-2 Verbal Notification Compliance](#gv-cr-2) content elements (what / what / who / how)
>
> The headline metric is the **gap** (process compliance minus understanding rate), not either rate alone. Gap > 25 percentage points triggers a substantive review; the consent model's legitimacy depends on understanding, not just notification (per the Novel Thinking section). Cross-link to [IO.PX-1 Patient Opt-Out Rate](#io-px-1) — opt-out behaviour disaggregated by demographics may indicate where the understanding gap is concentrated even before survey detects it.

**Operational Specification**

> - **Window:** continuous for process compliance (inherits from GV.CR-2); quarterly periodic audit for understanding rate.
> - **Population for understanding survey MANDATORY:** ≥ 30 patients per practice per quarter for survey method, with stratification across demographic axes (age band, primary language, deprivation index where available). Pure aggregate sampling masks the failure modes that matter — language and literacy are the predictable understanding-rate diminishers.
> - **Three sub-metrics MANDATORY:** process compliance rate (continuous from GV.CR-2), understanding rate (quarterly), and the gap. Any rate reported alone insufficient.
> - **Demographic disaggregation MANDATORY for understanding rate:** stratification by primary language, age band, ethnicity, and where available deprivation index. The aggregate understanding rate hides the failure pattern; disparities are the metric's value.
> - **Survey instrument declaration MANDATORY:** the survey instrument used must be declared (validated published instrument vs deployer-defined). Deployer-defined instruments must be reviewed by the IG team and document at least four comprehension items mapping to GV.CR-2 content elements.

**Trigger Conditions**

> ⚠️ **Provenance:** the gap-as-headline framing carries from the existing Novel Thinking section and [CQC-Mythbuster-109]'s "informed" requirement. Specific numerical thresholds (25-percentage-point gap trigger, ≥ 30 patients/quarter survey floor, demographic-disparity-2× alert) are **proposed in v3.5 as starting points**, not externally validated. The understanding rate is the harder measurement and the survey instrument choice will materially affect the result; require local calibration before contractual use.
>
> - **Pre-deployment gate:** GV.CR-2 process-compliance gate met; survey instrument selected and reviewed by IG team; quarterly survey schedule established.
> - **Continuous monitoring:** monthly process compliance from GV.CR-2; quarterly understanding rate; gap reported every quarter with demographic breakdown. Alert when aggregate gap > 25 percentage points OR any demographic axis shows understanding rate < practice mean by ≥ 20 percentage points.
> - **Pause / escalation trigger:** gap > 40 percentage points sustained two quarters (consent model legitimacy in question); OR any demographic axis shows understanding rate < 50 % (the consent model is failing for that population, not just under-performing).
>
> Specific numerical starting points are deployment-context-dependent and live in [Threshold Reference: GV.PD-8](../thresholds.md#gv-pd-8). Treat them as starting points to calibrate locally — not as contractual gates.



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
| **Family** | NHSE IG Attestation |
| **Source** | [UK-GDPR] Article 46; [Schrems-II] implications |

**Why this tier?**

> Legal compliance requirement. Must be assessed at procurement. Non-compliance is a regulatory breach.

**Formal Definition**

```
Audit data flow: (1) Where is audio processed? (2) Where are model inferences performed? (3) Where is data stored? (4) Where do support staff access data? For each non-UK location, verify Article 46 safeguards (SCCs, adequacy decisions, BCRs).
```

**References**

- **UK GDPR**: [UK-GDPR] Article 46 — appropriate safeguards for international transfers

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
| **Source** | [UK-GDPR] Article 15 right of access |

**Why this tier?**

> Legal compliance requirement. Must be tested before go-live to confirm vendor supports SAR fulfilment workflow.

**Formal Definition**

```
SAR Fulfilment Rate = |SARs_completed_within_30_days| / |total_SARs|. Sub-criteria: (1) Can deployer locate all AVT data for a patient? (2) Can it be exported in usable format? (3) Within statutory timeframe? Target: 100% within 30 days.
```

**Reference Standard**

> [UK-GDPR] Article 15 is the legal floor; [ICO] 30-day timeline is the statutory window (extendable by two months for complex requests with patient notification). "All AVT data for a patient" = every personal-data instance reachable via the storage-location enumeration in [GV.PD-1 Audio Retention Compliance](#gv-pd-1) plus [GV.VT-7 Sub-Processor Transparency](#gv-vt-7) — including audio, transcripts, AI-generated notes, edit history, telemetry-derived metadata, and any sub-processor-held copies. "Usable format" requires structured machine-readable export of structured data plus searchable text export of free-text content; PDF-only export of audio metadata is not "usable" for the patient's own access purposes. Cross-link to [GV.PD-11 Right to Erasure Compliance](#gv-pd-11) — the same data-locating capability underpins both rights.

**Operational Specification**

> - **Window:** continuous SAR-by-SAR tracking with quarterly compliance reporting.
> - **Population:** every SAR received that includes AVT-related data (denominator: SARs received, not consultations).
> - **Three sub-metric reporting MANDATORY:** locate-rate (deployer can find all AVT data), export-rate (data exportable in usable format), and timeliness-rate (completed within 30 days). Aggregate alone is not sufficient — failure mode (couldn't find / found but couldn't export / found and exported too slowly) drives different remediation.
> - **Synthetic SAR test pre-deployment MANDATORY:** at least one synthetic SAR processed end-to-end before go-live, exercising every storage location and sub-processor in the architecture. Failures discovered in this test are remediated before live SARs occur, not after.
> - **Sub-processor cooperation tracked separately:** SAR fulfilment depends on sub-processors providing their data; cooperation latency per sub-processor recorded. Vendors should contractually commit sub-processors to deployer's SAR timeline.
> - **Complex-request extension logged:** any SAR using the two-month extension provision logged with reason; pattern of extensions on AVT-related SARs is a signal that the locate-rate or export-rate is failing.

**Trigger Conditions**

> ⚠️ **Provenance:** the 30-day target and 100 % locate/export expectation derive from [UK-GDPR] Article 15 and [ICO] guidance. The synthetic-SAR pre-deployment test is **proposed in v3.5 as a starting point** to bring SAR readiness into the procurement gate (rather than discovering at first live SAR). Specific numerical thresholds are largely cited; the pre-deployment test cadence and the extension-pattern alert are the proposed elements. Indicative; require local calibration before contractual use.
>
> - **Pre-deployment gate:** synthetic SAR test passes — every storage location returns data; export format usable; full processing within 30 days. Gaps remediated before go-live.
> - **Continuous monitoring:** quarterly per-sub-metric reporting; locate-rate ≥ 100 % (any SAR where AVT data could not be located is a failure regardless of timeliness); export-rate ≥ 100 %; timeliness-rate ≥ 95 % (allowing for legitimate complex-request extensions).
> - **Pause / escalation trigger:** any SAR where AVT data could not be located within the deployer's known architecture (this is a regulatory failure under Article 15); OR timeliness-rate < 90 % in any quarter (suggests operational capacity failure); OR > 30 % of AVT-related SARs using the two-month extension (suggests systematic locate/export failure rather than legitimate complexity).
>
> Specific numerical starting points are deployment-context-dependent and live in [Threshold Reference: GV.PD-10](../thresholds.md#gv-pd-10). Treat them as starting points to calibrate locally — not as contractual gates.



**Novel Thinking / Implications**

> 💡 When a patient submits a SAR, the deployer must provide all personal data including AVT-generated material and any retained audio. If the vendor doesn't provide patient-level export, the deployer cannot fulfil their statutory obligation. This should be a procurement question, not discovered after the first SAR.

---

### GV.PD-11 🟢 Right to Erasure Compliance

If a patient requests erasure under UK GDPR Article 17, can audio, transcripts, and intermediate outputs actually be deleted? Backup systems, vendor caches, and downstream secondary uses complicate this.

**Applicability note.** Article 17 rights are narrowly applicable for AVT processing conducted for individual care: the [UK-GDPR] exemptions for public-task, public-health, preventative/occupational medicine, medical diagnosis, and health/social-care provision mean erasure of material held strictly for individual-care purposes is typically *not* exercisable as a statutory right ([NHSE-IG-Guidance-2026-03]). The capability must still exist for cases where erasure does apply - secondary use, research data derived from AVT, training-data inclusion under GV.PD-7, and case-by-case best-interest determinations - which is why this remains a pre-deployment gate.

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
| **Source** | [UK-GDPR] Article 17 right to erasure; [NHSE-IG-Guidance-2026-03] for individual-care exemption scope |

**Why this tier?**

> Pre-deployment gate to establish the scope, Article 17 applicability exemptions, and technical limitations of erasure. The statutory right is narrowly applicable for individual-care AVT processing but the capability must exist for cases where it does apply (secondary use, training-data withdrawal, dispute resolution). Tier 1 because understanding what erasure *can* and *cannot* deliver is a mandatory input to the DPIA and the privacy notice.

**Formal Definition**

```
Erasure Test: process a synthetic erasure request through the system. Verify deletion in: primary storage, backups, vendor caches, model training pipelines, downstream secondary use. Verification Rate = locations confirmed deleted / total locations.
```

**Reference Standard**

> [UK-GDPR] Article 17 with the [NHSE-IG-Guidance-2026-03] individual-care exemption scope is the legal floor. The locations enumeration inherits from [GV.PD-1 Audio Retention Compliance](#gv-pd-1) plus three Article-17-specific additions:
>
> - **Model training pipelines** — any AVT data ingested for model fine-tuning, validation set construction, or A/B testing
> - **Downstream secondary use** — research databases, quality-monitoring archives, business-intelligence pipelines
> - **Sub-processor systems** — every entity in the [GV.VT-7 Sub-Processor Transparency](#gv-vt-7) discovered set
>
> Three classes of erasure outcome MUST be distinguished: **deletable** (data can be cryptographically erased or physically deleted at all named locations); **anonymisable** (data can be irreversibly de-identified to the [ICO] anonymisation standard, suitable for research-database carve-outs); **technically irreversible** (data cannot be removed — typically applies to influence on already-trained models). The taxonomy and the privacy notice MUST disclose the irreversible class explicitly per the Novel Thinking section. Cross-link to [GV.PD-7 Training Data Inclusion Status](#gv-pd-7) — patients should know at consent time whether their data may end up in the irreversible class.

**Operational Specification**

> - **Window:** one-off pre-deployment gate; mandatory re-test on architectural change (new sub-processor, new training pipeline, new secondary-use destination).
> - **Population for synthetic test:** at least one synthetic patient record exercised end-to-end through every named location in the enumeration above. Production erasure-rate also tracked for the (small) population of in-scope live erasure requests.
> - **Three-class outcome reporting MANDATORY:** every erasure-test location classified deletable / anonymisable / technically-irreversible. Aggregate "verification rate" alone hides the irreversible-class failure mode.
> - **Privacy-notice cross-check MANDATORY:** the technically-irreversible class enumerated at procurement must match the disclosure in the privacy notice. Drift between the two (locations becoming irreversible without privacy-notice update) is itself a flag.
> - **Article-17-exempt vs in-scope:** every erasure request classified as exempt (individual-care purpose, public-task carve-out) or in-scope (secondary use, research, training data, best-interest case). The exempt class is logged with reason but not subject to the same fulfilment expectation as in-scope.
> - **Sub-processor cooperation tracked:** parallel to [GV.PD-10 Subject Access Request Fulfilment](#gv-pd-10) — sub-processor latency per erasure request recorded.

**Trigger Conditions**

> ⚠️ **Provenance:** the three-class outcome distinction (deletable / anonymisable / technically-irreversible) is **proposed in v3.5** as a way to operationalise the Novel Thinking section's observation that some erasure requests cannot be fulfilled even in principle. The Article 17 exemption framing is cited ([NHSE-IG-Guidance-2026-03]). Specific numerical thresholds are largely binary (privacy-notice match, synthetic-test coverage); the proposed elements are the three-class taxonomy and the privacy-notice cross-check. Indicative; require local calibration before contractual use.
>
> - **Pre-deployment gate:** synthetic erasure test passes — every storage location classified into one of the three outcome classes; technically-irreversible class enumerated and matched to the privacy notice; sub-processor cooperation timelines documented.
> - **Continuous monitoring:** in-scope erasure requests fulfilled within 30 days at deletable locations and 30 days at anonymisable locations; technically-irreversible-class size stable (any growth means a new location was added without classification — a flag).
> - **Pause / escalation trigger:** any in-scope erasure request where a deletable location fails to delete (regulatory failure under Article 17); OR any newly added location not classified into the three-class taxonomy before processing personal data; OR drift between technically-irreversible class and privacy-notice disclosure (procurement-time disclosure failure).
>
> Specific numerical starting points are deployment-context-dependent and live in [Threshold Reference: GV.PD-11](../thresholds.md#gv-pd-11). Treat them as starting points to calibrate locally — not as contractual gates.



**Novel Thinking / Implications**

> 💡 The hard case: if audio from a patient was used to fine-tune the vendor's model, can that influence be removed? Probably not - and this should be disclosed in the privacy notice. Patients should know that consenting to AVT may include effectively irreversible inclusion of their voice in model training. This is a transparency obligation that current AVT consent processes rarely address.

---


### GV.PD-12 🟡 Training Data Representativeness Documentation

Documentation of whether the AVT system's training data covers the intended patient population across demographic and clinical-setting strata — age, ethnicity, accent, comorbidity profile, deprivation, and care-setting mix. The metric is the foundational pre-condition for downstream bias-mitigation work: a deployer cannot defensibly run [TP.ASR-4 Demographic-Disaggregated WER] or [IO.FE-1 Deployment Equity Index] without first knowing whether the training data could plausibly support equivalent performance across strata.

|Dimension              |Value                                                   |
|-----------------------|---------------------------------------------------------|
| **Reference** | GV.PD-12 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                   |
|**Measurement Cadence**|One-off gate; Event-triggered                            |
|**Pipeline Layer**     |Cross-cutting                                            |
|**Assurance Question** |Fairness                                                 |
|**Measurement Method** |Human Review                                             |
|**Lifecycle Phases**   |Pre-deployment                                           |
|**Responsible Actors** |Vendor                                                   |
|**Maturity**           |Emerging                                                 |
|**Outcome Type**       |Proximal                                                 |
|**Applicability**      |General Healthcare AI                                    |
|**Source**             |[MHRA-SaMD] GMLP principle 3 (representative datasets); FTS Performance & Monitoring Response — "boundaries and bias"|

**Why this tier?**

> Tier 2 because the metric tests documentation, not in-use performance — actual representativeness shows up in stratified performance metrics during deployment. The pre-deployment documentation is necessary but not sufficient for fairness assurance. Closely tied to the MHRA GMLP principle 3 expectation; deployers who skip this step inherit whatever the vendor decided was "representative".

**Formal Definition**

```
Pass per criterion: (1) Training data corpus characterised by language, accent / dialect, age, sex, ethnicity, deprivation strata; (2) Clinical setting mix documented (primary care / outpatient / inpatient / virtual modality); (3) Specialty mix documented; (4) Known under-representation acknowledged with mitigation plan; (5) Statement on synthetic / augmented data proportion if used. Full pass = all five.
```

**Limitations**

> Vendor-curated documentation is not independently auditable in most cases — training data is commercial-confidential. The metric verifies that documentation is internally consistent and explicitly engages the GMLP principle 3 expectations; it cannot verify that the documentation is empirically true. Independent audit (third-party data-card review) is the harder check and is currently rare.

**Novel Thinking / Implications**

> 💡 Training data representativeness documentation is the upstream control for the entire fairness assurance stack. Without it, every downstream stratified-performance disparity could be either a deployment-time artefact or a built-in training failure, and there is no way to tell. Making the documentation a Tier 2 gate forces vendors to own the upstream answer; deployers can then triage where stratified-performance gaps are coming from.

---

### GV.PD-13 🟢 Privacy Notice Currency & Completeness

Whether the deploying organisation's published privacy notices have been updated to include AVT-specific processing — at minimum the lawful basis, controller / processor relationship, retention timelines for audio and transcripts, and the existence of any post-deployment training use. The metric is binary per privacy-notice instance, with currency tested against the AVT deployment date and any subsequent material change.

**Change history:** v5.5.0 (Source row updated — `(section ref to be added on next pass)` placeholder replaced with topic-cited content reference; the parent NHSE IG guidance hub does not currently expose a stable section anchor).

|Dimension              |Value                                                   |
|-----------------------|---------------------------------------------------------|
| **Reference** | GV.PD-13 |
|**Priority Tier**      |🟢 Tier 1 - Minimum Viable                                |
|**Measurement Cadence**|Periodic audit; Event-triggered                                  |
|**Pipeline Layer**     |Cross-cutting                                            |
|**Assurance Question** |Privacy                                                  |
|**Measurement Method** |Human Review                                             |
|**Lifecycle Phases**   |Pre-deployment, Continuous                               |
|**Responsible Actors** |Deployer                                                 |
|**Maturity**           |Established                                              |
|**Outcome Type**       |Proximal                                                 |
|**Applicability**      |General Healthcare AI                                    |
|**Family**             |NHSE IG Attestation|
|**Source**             |[NHSE-IG-Guidance-2026-03] — privacy notice / AVT-processing transparency content (topic-cited; parent hub no stable section anchor); UK GDPR Art 13/14|

**Why this tier?**

> Tier 1 because the cost is low and the obligation is named. Privacy notice currency is a UK GDPR Article 13/14 obligation that pre-exists AVT; the AVT-specific update is a small marginal task. Deployers who go live with AVT without updating their privacy notice are operating outside the legal basis they claim to operate under.

**Formal Definition**

```
Pass per criterion: (1) Each public-facing privacy notice (organisation-level + service-level if separate) includes an AVT-specific section; (2) Lawful basis stated explicitly (typically Article 6(1)(e) public task + Article 9(2)(h) provision of healthcare); (3) Controller / processor relationship named with vendor identified; (4) Retention periods stated for audio, transcript, and any model-training-use data; (5) Notice version-dated and dated within 12 months of last review or material change. Full pass = all five; a single missing item is a fail.
```

**Limitations**

> The metric tests the deployer-published privacy notice; it does not test whether patients have actually read or understood it (that would belong under IO.PX patient-experience metrics).

**Novel Thinking / Implications**

> 💡 Privacy notice currency is the smallest-cost Tier 1 item in the v5.3 pull-through set — a deployer who fails it has likely failed the broader IG-readiness check too. Treating it as a separately-measured Tier 1 metric makes the failure visible early, before it becomes the trailing indicator that an AVT rollout was rushed past its IG governance.

---

### GV.PD-14 🟡 SAR Deletion-Pause Interaction

Whether the deployer's Subject Access Request handling and AVT data-deletion processes interact correctly: when a SAR is opened on a patient with active AVT-derived data, deletion of that patient's audio / transcript is paused for the duration of the SAR and resumed only after the SAR is formally closed. NHSE IG explicitly requires this interaction; it is distinct from [GV.PD-2 Audio Time-to-Deletion] which tests the routine deletion timeline in the absence of a SAR.

**Change history:** v5.5.0 (Source row updated — `(section ref to be added on next pass)` placeholder replaced with topic-cited content reference; the parent NHSE IG guidance hub does not currently expose a stable section anchor).

|Dimension              |Value                                                   |
|-----------------------|---------------------------------------------------------|
| **Reference** | GV.PD-14 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                   |
|**Measurement Cadence**|Periodic audit; Event-triggered                                  |
|**Pipeline Layer**     |Cross-cutting                                            |
|**Assurance Question** |Privacy                                                  |
|**Measurement Method** |Human Review                                             |
|**Lifecycle Phases**   |Pre-deployment, Continuous                               |
|**Responsible Actors** |Deployer; Vendor                                         |
|**Maturity**           |Emerging                                                 |
|**Outcome Type**       |Proximal                                                 |
|**Applicability**      |General Healthcare AI                                    |
|**Family**             |NHSE IG Attestation|
|**Source**             |[NHSE-IG-Guidance-2026-03] — data subject rights / SAR-handling content (topic-cited; parent hub no stable section anchor); UK GDPR Art 12-22 (data subject rights)|

**Why this tier?**

> Tier 2 because SAR-active deletion-pause is an interaction-test rather than a standing-state-test, and therefore tested by scenario walk-through rather than continuous monitoring. Wrong behaviour here destroys evidence the patient is entitled to — a serious failure mode but a rare one in practice.

**Formal Definition**

```
Scenario walk-through: (1) Open a synthetic SAR against a test patient with active AVT-derived data approaching the GV.PD-2 deletion threshold; (2) Verify deletion is paused via the deployer's SAR-handling SOP and any vendor-side pause flag; (3) Verify SAR response can include the AVT-derived data; (4) Close the synthetic SAR; (5) Verify deletion resumes within the GV.PD-2 cadence from SAR-close, not from original creation. Full pass = all five.
```

**Limitations**

> Scenario testing is sample-based and infrequent; the real-world failure mode (a SAR opened during a deletion countdown that does not pause) only surfaces when a real SAR is mishandled. Dependence on vendor-side cooperation is a known weakness — if the vendor's data-flow does not expose a pause flag, the pause has to happen at the deployer-mediated layer only, which may not catch every copy.

**Novel Thinking / Implications**

> 💡 The SAR / deletion interaction is the kind of regulatory edge case that does not surface in any single-process audit — both processes pass on their own. Making it a separately-measured Tier 2 metric forces the deployer to test the interaction explicitly, which is the only way to discover whether the SOP and the vendor data-flow actually compose correctly under stress.

---

### GV.PD-15 🟡 Right-to-Restrict Tooling Support

Whether the deploying organisation's AVT-side tooling supports the UK GDPR Article 18 right-to-restrict — data marked, retained, but not actively processed — distinct from the right-to-erasure already tested by [GV.PD-11 Erasure Workflow Coverage]. Restriction is a less-common rights request but explicitly named in the NHSE IG guidance; the deployer needs the ability to tag a patient's AVT-derived data such that it is preserved for evidence purposes but excluded from any model-training, analytics, or downstream re-processing.

**Change history:** v5.5.0 (Source row updated — `(section ref to be added on next pass)` placeholder replaced with topic-cited content reference; the parent NHSE IG guidance hub does not currently expose a stable section anchor).

|Dimension              |Value                                                   |
|-----------------------|---------------------------------------------------------|
| **Reference** | GV.PD-15 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                   |
|**Measurement Cadence**|Periodic audit; Event-triggered                                  |
|**Pipeline Layer**     |Cross-cutting                                            |
|**Assurance Question** |Privacy                                                  |
|**Measurement Method** |Human Review                                             |
|**Lifecycle Phases**   |Pre-deployment, Continuous                               |
|**Responsible Actors** |Deployer; Vendor                                         |
|**Maturity**           |Emerging                                                 |
|**Outcome Type**       |Proximal                                                 |
|**Applicability**      |General Healthcare AI                                    |
|**Family**             |NHSE IG Attestation|
|**Source**             |[NHSE-IG-Guidance-2026-03] — data subject rights / restriction tooling content (topic-cited; parent hub no stable section anchor); UK GDPR Art 18|

**Why this tier?**

> Tier 2 because restriction requests are infrequent in practice but the absence of supporting tooling is a deployment-blocking gap when one is raised. The deployer cannot manufacture a restriction capability after the fact.

**Formal Definition**

```
Pass per criterion: (1) AVT-side tooling exposes a "restrict" flag distinguishable from "erase"; (2) Restricted records are excluded from any vendor-side training, analytics, or re-processing pipeline; (3) Restricted records remain accessible for evidence / SAR / audit purposes; (4) Restriction can be lifted via documented reversal procedure; (5) Audit trail of restriction events maintained. Full pass = all five.
```

**Limitations**

> Vendor-side support for the restrict flag is the load-bearing technical dependency. Many AVT vendors implement erasure but not restriction; deployers using such vendors will fail this metric until vendor capability catches up. Future minor release should consider whether to break out a vendor-capability sub-metric explicitly.

**Novel Thinking / Implications**

> 💡 The right-to-restrict is the least-exercised data subject right in routine deployment, which means it is also the most likely to be silently absent from vendor capability. Making it a separately-measured Tier 2 metric surfaces the gap before a patient request makes it an emergency.

---

### GV.PD-16 🟢 Decommissioning Data Handling Compliance

When an AVT deployment is wound down — whether by deployer choice, vendor retirement ([GV.VT-15 Retirement Notification Compliance](#gv-vt-15)), or contract termination ([GV.VT-6 Exit & Data Portability Provisions](#gv-vt-6)) — what happens to audio, transcripts, AI-generated notes, telemetry, and any patient data the vendor or deployer retained? This metric covers the *data-handling* dimension of decommissioning: every storage location named in the deployment's [GV.PD-1 Audio Retention Compliance](#gv-pd-1) enumeration must follow a defined wind-down procedure with deletion or migration documented per location.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.PD-16 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | One-off gate; Event-triggered |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Operational extension of [GV.PD-1] retention enumeration; promoted from `_gaps.md` P5-Lifecycle "Decommissioning plan" entry; [DCB0160] Stage 7 (decommissioning) |

**Why this tier?**

> Decommissioning is the moment when retention compliance is most likely to silently fail — vendor backups linger past their stated retention window; deployer-side caches retain audio derivatives indefinitely; sub-processors aren't actively decommissioned. Without a Tier 1 gate covering this, the v3.x retention metrics (GV.PD-1/-2/-3) hold for the operational period but break the moment a deployment ends. Tier 1 because the regulatory exposure (UK GDPR storage limitation; NHSE IG guidance; DCB0160 Stage 7) does not pause when an AVT product is retired.

**Formal Definition**

```
Compliance gate (pre-deployment) = the deployer's DPIA + contract specify a decommissioning data-handling procedure covering: (a) per-storage-location wind-down rules (deletion, anonymisation, or migration to a successor system); (b) deletion-verification method per location; (c) sub-processor decommissioning cooperation; (d) timeline for completion; (e) audit trail format.

Per-event compliance (when decommissioning occurs) = (every storage location in the GV.PD-1 enumeration has a documented disposition AND deletion-verification or migration-confirmation evidence on file AND completion within contracted timeline).

Disposition options per location: (i) deletable — cryptographically erased or physically deleted; (ii) anonymisable — irreversibly de-identified to ICO standard; (iii) migratable — moved to a deployer-controlled or successor-vendor system with a documented data-portability evidence trail; (iv) technically irreversible — flagged and disclosed (parallel to GV.PD-11 Right to Erasure Compliance's three-class outcome distinction).
```

**Reference Standard**

> Inherits the storage-location enumeration from [GV.PD-1 Audio Retention Compliance](#gv-pd-1): primary vendor storage, vendor backups and DR, vendor logs, downstream analytic systems, deployer-side caches, named sub-processor systems per [GV.VT-7 Sub-Processor Transparency](#gv-vt-7), model training pipelines per [GV.PD-11 Right to Erasure Compliance](#gv-pd-11), and any data ingested for fine-tuning per [GV.PD-7 Training Data Inclusion Status](#gv-pd-7). The decommissioning procedure is documented in the deployer's DPIA + procurement contract + DCB0160 Stage 7 retirement section before go-live; the per-event compliance is verified against that documentation at decommissioning. Cross-link to [DCB0129] / [DCB0160] retirement provisions and to [SI-2024-1368] post-market surveillance closure for any MHRA-classified component.

**Operational Specification**

> - **Window:** procurement contract review (one-off gate); per-event tracking when decommissioning occurs.
> - **Three sub-metrics MANDATORY:** (a) procedure-document gate (is the wind-down procedure documented in DPIA + contract pre-deployment?); (b) per-location disposition coverage (does every GV.PD-1 storage location have a documented disposition?); (c) execution compliance (was the actual wind-down completed within the contracted timeline with deletion-verification evidence?).
> - **Per-storage-location reporting MANDATORY:** the matrix of {storage location × disposition outcome} is the unit of reporting. Aggregate "compliance rate" alone hides the failure mode (e.g. backups retained indefinitely while primary storage was deleted).
> - **Sub-processor cooperation tracked:** every sub-processor in the [GV.VT-7](#gv-vt-7) discovered set has its own disposition evidence on file; sub-processor non-cooperation logged with reason.
> - **Verification method MANDATORY:** parallel to [GV.PD-1](#gv-pd-1); vendor self-attestation alone is not Tier 1 sufficient. Independent verification required: cryptographic proof of key destruction, third-party audit, or deployer-witnessed deletion test for at least one location per disposition category.
> - **Three-class outcome reporting MANDATORY:** parallel to [GV.PD-11 Right to Erasure Compliance](#gv-pd-11); every storage location classified as deletable / anonymisable / migratable / technically-irreversible. The technically-irreversible class enumerated explicitly with the disclosure obligation (e.g. influence on already-trained models that cannot be reversed).

**Trigger Conditions**

> ⚠️ **Provenance:** the per-storage-location framing inherits from [GV.PD-1 Audio Retention Compliance](#gv-pd-1) and [GV.PD-11 Right to Erasure Compliance](#gv-pd-11)'s three-class outcome distinction. The procurement-time documentation gate carries from [GV.CR-7 DPIA Template Completion Rate](#gv-cr-7) and [DCB0160] Stage 7. Specific timeline thresholds (90-day completion target for deletion; 180-day target including sub-processor cascade; 100 % per-location disposition gate) are **proposed in v4.0.2 as starting points**, not externally validated. Indicative; require local calibration against the deployer's DPIA risk appetite and contractual SLA before procurement use.
>
> - **Pre-deployment gate (procurement):** wind-down procedure documented in DPIA + contract; per-storage-location dispositions enumerated; deletion-verification methods specified per location; sub-processor cooperation timelines specified.
> - **Per-event monitoring:** decommissioning events trigger logging of (a) per-location disposition completion, (b) deletion-verification evidence per location, (c) timeline compliance. Aggregate compliance reported per decommissioning event.
> - **Pause / escalation trigger:** any decommissioning event where a primary-storage or named sub-processor location lacks disposition evidence (regulatory failure under [UK-GDPR] storage limitation); OR completion timeline exceeded by > 50 %; OR per-location disposition coverage < 95 % at completion.
>
> Specific numerical starting points are deployment-context-dependent and live in [Threshold Reference: GV.PD-16](../thresholds.md#gv-pd-16). Treat them as starting points to calibrate locally — not as contractual gates.



**Limitations**

> Decommissioning is a low-frequency event (most AVT deployments do not decommission within their first contract term), which means execution-compliance evidence is sparse. The procedure-document gate sub-metric is the load-bearing pre-deployment measurement; the execution sub-metrics activate only when decommissioning occurs. Vendor cooperation at decommissioning is also harder to enforce than at deployment (the contractual relationship is ending); deployer leverage on lingering backups, sub-processor decommissioning, and training-data fate is constrained. The metric makes the surface visible but does not solve the enforcement-at-the-end problem.

**Novel Thinking / Implications**

> 💡 Decommissioning data handling is the regulatory failure mode that has not yet surfaced at scale because the AVT vendor market is too young — most vendors haven't been retired or replaced. The first few cases will reveal whether the v3.9 retention metrics (GV.PD-1/-2/-3/-11) actually hold past the operational period, or whether they're operationally measured but architecturally undefended for end-of-life. Treating decommissioning as Tier 1 from now means deployers writing procurement contracts today specify wind-down procedures explicitly; treating it as Tier 2 means we'll discover the gaps when something goes wrong.

---

### GV.PD-17 🟡 DPIA Justification Quality

Independent review of the substantive quality of the AVT Data Protection Impact Assessment's purpose-justification — typically by the deploying organisation's Caldicott Guardian. **Sub-part of the DPIA construct paired with [GV.CR-7 DPIA Template Completion Rate](#gv-cr-7)**: GV.CR-7 is the parent (structural completion of all template sections); this metric is the substantive Caldicott Principle 1 ("justify the purpose") sub-part that completion alone cannot pass. The metric outputs a graded review (sufficient / needs revision / insufficient) with Guardian sign-off as the binding gate. Both checks are needed because a DPIA can be structurally complete and substantively weak on purpose justification.

**Change history:** v5.4.0 (formalised parent + sub-part relationship with GV.CR-7 — explicit pairing language added; cross-cluster placement preserved because GV.CR-7 is a compliance-attestation gate while GV.PD-17 is a privacy-data-governance substantive review).

|Dimension              |Value                                                   |
|-----------------------|---------------------------------------------------------|
| **Reference** | GV.PD-17 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                   |
|**Measurement Cadence**|Periodic audit; Event-triggered                                  |
|**Pipeline Layer**     |Cross-cutting                                            |
|**Assurance Question** |Privacy                                                  |
|**Measurement Method** |Human Review                                             |
|**Lifecycle Phases**   |Pre-deployment, Continuous                               |
|**Responsible Actors** |Deployer; Caldicott Guardian                             |
|**Maturity**           |Established                                              |
|**Outcome Type**       |Proximal                                                 |
|**Applicability**      |General Healthcare AI                                    |
|**Source**             |[Caldicott] Principle 1 (justify the purpose); UK Caldicott Guardian Manual; NDG guidance|

**Why this tier?**

> Tier 2 because the metric extends an existing Tier 1 metric (GV.CR-7) — completing a DPIA is the gate; reviewing its purpose-justification is the recommended next layer. Deployers with mature IG can reasonably elevate this to Tier 1 internally; the taxonomy keeps it at Tier 2 because not all deployments have access to a Caldicott Guardian's review capacity.

**Formal Definition**

```
Pass per criterion: (1) DPIA purpose-justification reviewed by named Caldicott Guardian (or equivalent IG senior); (2) Reviewer's verdict recorded (sufficient / needs revision / insufficient); (3) Where verdict is "needs revision" or "insufficient", revision tracked to closure or deployment paused; (4) Annual re-review tied to [GV.PD-13 Privacy Notice Currency] cycle; (5) Reviewer verdict accessible to incident-investigation processes if a future complaint relates to purpose justification. Full pass = all five.
```

**Limitations**

> Reviewer judgement is qualitative; two Caldicott Guardians may reach different verdicts on the same DPIA. The metric does not enforce a specific rubric — deferred to local Guardian practice — which means cross-deployer comparability is limited. Future minor release may add a structured rubric if national IG practice converges on one.

**Novel Thinking / Implications**

> 💡 The completion-vs-quality gap is one of the most consistent pattern in IG metrics: a fully-completed DPIA can still be substantively wrong on purpose justification. Caldicott Guardian review is the structural mechanism the NHS already has for catching this; making it a separately-measured Tier 2 metric forces the review to happen on a documented cadence rather than only when something goes wrong.

---

### GV.PD-18 🟢 Information Asset Register Completeness

Whether the deploying organisation maintains an Information Asset Register (IAR) that includes the AVT system as a named information asset with a documented owner, lawful basis, retention period, sub-processor list, and risk classification. NHSE IG section 8 explicitly requires AVT-deploying organisations to register the system as an information asset alongside their other clinical-system assets — the IAR is the index that ties together DPIA, sub-processor disclosure, retention timing, and incident escalation.

**Change history:** v5.5.0 (Source row updated — `(section ref to be added on next pass)` placeholder replaced with topic-cited content reference; the parent NHSE IG guidance hub does not currently expose a stable section anchor).

|Dimension              |Value                                                   |
|-----------------------|---------------------------------------------------------|
| **Reference** | GV.PD-18 |
|**Priority Tier**      |🟢 Tier 1 - Minimum Viable                                |
|**Measurement Cadence**|Periodic audit; Event-triggered                          |
|**Pipeline Layer**     |Cross-cutting                                            |
|**Assurance Question** |Privacy                                                  |
|**Measurement Method** |Human Review                                             |
|**Lifecycle Phases**   |Pre-deployment, Continuous                               |
|**Responsible Actors** |Deployer                                                 |
|**Maturity**           |Established                                              |
|**Outcome Type**       |Proximal                                                 |
|**Applicability**      |General Healthcare AI                                    |
|**Family**             |NHSE IG Attestation                                      |
|**Source**             |[NHSE-IG-Guidance-2026-03] — information asset register / IAO-naming content (topic-cited; the unverified 'section 8' placeholder from v5.4.0 is dropped — parent hub no stable section anchor); NDG Data Security Standards|

**Why this tier?**

> Tier 1 because the IAR is the structural index that ties the rest of the IG-attestation surface together — without an entry, the AVT deployment is invisible to the IG team's incident escalation, SAR-handling, and audit-cycle workflows. The cost of compliance is small (an IAR row), the cost of non-compliance is high (the system is governed only by ad-hoc memory). Member of the [NHSE IG Attestation family](../families.md#nhse-ig-attestation).

**Formal Definition**

```
Pass per criterion: (1) AVT system listed in the organisation's Information Asset Register; (2) Named Information Asset Owner (IAO) documented; (3) Lawful basis stated (typically Article 6(1)(e) + Article 9(2)(h)); (4) Retention period stated, consistent with [GV.PD-1] / [GV.PD-2] / [GV.PD-3]; (5) Sub-processor list referenced (consistent with [GV.VT-7]); (6) Risk classification documented (typically aligned with the DPIA risk rating); (7) IAR entry version-dated within 12 months. Full pass = all seven.
```

**Limitations**

> The metric tests that the IAR entry exists and is internally consistent — it does not test whether the IAR entry is empirically accurate (e.g. whether the listed retention period actually matches operational reality). Pair with [GV.PD-1] / [GV.PD-2] / [GV.PD-3] for empirical verification of the retention claims.

**Novel Thinking / Implications**

> 💡 The IAR is the IG team's index into the AVT deployment — without it, every other IG-attestation metric is operating on a system the IG team has no formal record of. NHSE AI early-adopter inspections have repeatedly found AVT deployments that passed individual IG checks but were not registered as information assets, which made cross-cutting questions ("show me all systems handling Special Category data") impossible to answer accurately. Making this Tier 1 makes the index visible.

