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
> - **Understanding rate** is measured by structured patient survey. **No validated AVT-specific patient-comprehension instrument exists at the time of v3.7.** Deployers should either (a) select the closest healthcare-IT-comprehension instrument (e.g. eHealth Literacy items adapted for AVT context, Decision Conflict Scale items) and document the adaptation as a limitation, or (b) commission a deployer-defined survey reviewed by the IG team containing at least four comprehension items mapped to the [GV.CR-2 Verbal Notification Compliance](#gv-cr-2) content elements (what / what / who / how)
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

