### TP.WB-1 🟢 Write-back Fidelity

Data transfer accuracy to EPR structured fields. Where errors become patient safety events - hallucinated allergy in allergy field propagates to all future decisions.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.WB-1 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | One-off gate; Continuous |
| **Pipeline Layer** | Downstream Write-back |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Critical gap - no standardised FHIR R4 write-back in NHS primary care |

**Change history:** v5.1.0 (Cadence updated to multi-value `One-off gate; Continuous` to reflect that body describes both the highest-priority pre-deployment gate AND continuous monthly auditing of safety-critical fidelity in production traffic; v5.1 also introduces `Event-triggered` as a fourth Cadence enum value and makes the dimension semicolon-separated).

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
> - **Semantic equivalence** - the value preserves clinical meaning. For coded categories (c-e) semantic equivalence requires preservation of the coded concept (e.g. [SNOMED-CT] identifier match, not just string match); for free text (a) it requires preservation of every clinically relevant proposition per the [TP.SN-6 Omission Rate](#tp-sn-6) reference standard
> - **No content addition** - the value introduces no information absent from the AVT output. Hallucinated content reaching a structured field counts as a write-back failure even where the same content in free text would be a TP.SN-5 hallucination
>
> Inter-rater target on test-case construction: ICC ≥ 0.85 (write-back fidelity is a more constrained task than free-text fidelity; higher reliability expected).

**Operational Specification**

> - **Test corpus MANDATORY:** ≥ 200 test cases per target EPR system, balanced across the five categories with safety-critical categories (medications / allergies / problem-list) over-represented (≥ 40 cases each).
> - **Pre-deployment gate per EPR:** fidelity tested against every EPR system in scope at the deployment site. A vendor-asserted "EMIS-compatible" claim does not transfer to SystmOne without re-test.
> - **Population for continuous monitoring:** sampled production write-backs reviewed against a clinician-authored gold standard at a frequency proportional to write-back volume (minimum monthly audit; weekly for high-volume deployments).
> - **Per-category reporting MANDATORY:** report fidelity by category (a)-(e) with safety-critical categories reported separately. Aggregate-only reporting hides the failure modes that matter most.
> - **Failure-mode classification MANDATORY:** every failure classified as (i) wrong field, (ii) correct field, wrong content (omission), (iii) correct field, wrong content (addition / hallucination), (iv) structural mismatch (e.g. coded concept missing, unit error). Type (iii) on safety-critical fields is a critical incident regardless of frequency.

**Trigger Conditions**

> ⚠️ **Provenance:** the zero-tolerance posture on type-(iii) failures into safety-critical fields follows from the clinical-safety logic in the Why-this-tier and Novel Thinking sections (a hallucinated allergy in an allergy field is a system-level safety failure). Specific numbers (100 % safety-critical gate, ≥ 95 % free-text gate, ≥ 99 % monthly audit floor, ≥ 200 cases per EPR) are **proposed in v3.3 as starting points**, not externally validated. Indicative; require local calibration before contractual use.
>
> - **Pre-deployment gate (per EPR):** safety-critical category fidelity = 100 % on the test corpus; free-text fidelity ≥ 95 %; zero type-(iii) failures on any safety-critical field.
> - **Continuous monitoring:** monthly audited fidelity ≥ 99 % on safety-critical categories; alert on any type-(iii) failure detected in production traffic (no rate threshold - single instance is alert-worthy).
> - **Pause trigger:** any type-(iii) failure on allergy or medication-dose fields confirmed in production; or aggregate safety-critical fidelity < 95 % in any monthly audit cycle.
>
> Specific numerical starting points are deployment-context-dependent and live in [Threshold Reference: TP.WB-1](../thresholds.md#tp-wb-1). Treat them as starting points to calibrate locally — not as contractual gates.



**References**

- **IM1**: [NHS-IM1-Interface-Assurance]

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
| **Pipeline Layer** | Downstream Write-back |
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

**Reference Standard**

> Pipeline telemetry from the AVT product, the integration middleware (where present), and the target EPR. An "integration error" is any write-back attempt that does not result in a complete, conformant target-EPR record. Three error types distinguished:
>
> - **Failed (hard error)** — the write-back attempt threw an explicit error; no record created or partial record rejected by the EPR. Example: API timeout, FHIR resource validation rejection, authentication failure
> - **Partial** — record created but with missing fields the source data should have populated. Example: free-text body written but coded medications dropped; allergies field truncated due to length limit
> - **Degraded (soft failure)** — record created with all expected fields but with quality degradation. Example: SNOMED codes silently substituted with parent / generic codes due to mapping failure; structured data downgraded to free-text fallback
>
> Cross-link to [TP.WB-1 Write-back Fidelity](#tp-wb-1) — TP.WB-1 measures content correctness given successful integration; TP.WB-2 measures integration-itself success rate. The two together cover "did it write" (TP.WB-2) and "did it write correctly" (TP.WB-1).

**Operational Specification**

> - **Window:** continuous; daily aggregate per integration endpoint, monthly compliance reporting per EPR system in scope.
> - **Per-error-type reporting MANDATORY:** three sub-rates (failed / partial / degraded) reported separately. Aggregate IER hides the failure pattern: a 0.005 aggregate that is 100 % degraded reads very differently from a 0.005 aggregate that is 100 % failed.
> - **Per-EPR stratification MANDATORY:** parallel to TP.WB-1's per-EPR test corpus — IER measured against every EPR system in scope at the deployment site (EMIS, SystmOne, Epic, others). Aggregating across EPRs masks system-specific integration weaknesses.
> - **Severity classification MANDATORY:** every error event classified by clinical impact: **critical** (safety-critical content lost or degraded — allergies, medications, dosages, problem-list entries); **moderate** (clinically meaningful content lost — exam findings, history, plan items); **benign** (presentation-only content lost — formatting, ordering, free-text style). Critical-rate reported separately as the leading safety indicator.
> - **Soft-failure detection method MANDATORY:** the deployer's method for detecting degraded write-backs (where the EPR accepts the record but quality has been silently downgraded) MUST be documented. Methods in order of rigour: (i) sampled human review of write-back outputs against AVT-generated content; (ii) automated comparison of written-to-EPR content against AVT-generated content via diff; (iii) vendor self-attestation. Method (iii) is not Tier 1 sufficient alone.

**Trigger Conditions**

> ⚠️ **Provenance:** the IER < 0.001 SLA target carries from the existing Formal Definition and standard integration-monitoring practice. Specific numerical thresholds per error type (failed < 0.0005, partial < 0.0003, degraded < 0.0002 by default; critical-rate zero-tolerance for the partial / degraded classes on safety-critical content) are **proposed in v3.7 as starting points**, not externally validated. Per the [Calibration & Context principle](#calibration-context), require local calibration against contractual SLA before procurement use.
>
> - **Pre-deployment gate (per EPR):** vendor demonstrates the three-error-type telemetry; soft-failure detection method documented; one end-to-end integration test passes per error type prior to go-live; zero critical-class events on the test corpus.
> - **Continuous monitoring:** daily IER per error type per EPR ≤ SLA target; alert on any critical-class event detected (single instance, regardless of overall rate); alert if any error-type rate drifts > 50 % above per-EPR baseline sustained 7 days.
> - **Pause / escalation trigger:** any critical-class event on safety-critical content (allergy / medication / dose) confirmed in production; OR aggregate IER > 5 × SLA target on any EPR for 24 hours; OR degraded-class soft-failure detection cadence falls below documented method (loss of monitoring capability is itself an escalation event).
>
> Specific numerical starting points are deployment-context-dependent and live in [Threshold Reference: TP.WB-2](../thresholds.md#tp-wb-2). Treat them as starting points to calibrate locally — not as contractual gates.



**Limitations**

> Soft failures harder to detect than hard failures. The Operational Specification's mandatory soft-failure detection method makes this gap explicit at procurement; it does not solve it. Detection method (iii) (vendor self-attestation) is the most common in current deployments and the most epistemically weak — moving to method (i) or (ii) is itself a calibration target deployers should track.

---

### TP.WB-3 🟢 Field Mapping Accuracy

Does content land in the correct EPR field even when content is correct? A correctly transcribed allergy written to the free-text consultation field rather than the allergies field is a system failure with safety implications - the allergy won't trigger drug interaction checks.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.WB-3 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | One-off gate; Continuous |
| **Pipeline Layer** | Downstream Write-back |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Identified as distinct failure mode within write-back |

**Change history:** v5.1.0 (Cadence updated to multi-value `One-off gate; Continuous` to reflect both the safety-critical pre-deployment test AND ongoing continuous-monitoring of mapping accuracy in production traffic).

**Why this tier?**

> Safety-critical pre-deployment test. Wrong-field placement of safety-critical content (allergies, medications) bypasses downstream safety mechanisms entirely.

**Formal Definition**

```
For each clinical item: Mapping Accuracy = (item correctly identified) AND (mapped to correct EPR field). Distinct from content accuracy. Categories: allergies, medications, problems, observations, free-text. Critical failures: safety-critical content in non-safety-critical fields.
```

**Reference Standard**

> Inherits the per-EPR test corpus and the structural-equivalence definition from [TP.WB-1 Write-back Fidelity](#tp-wb-1) — TP.WB-3 is the field-correctness specialised case ("right field"). The reference is a per-EPR field-map document maintained by the deployer (or vendor with deployer sign-off) naming the canonical target field for each clinical-item type, including the legitimate-multi-target carve-outs:
>
> - **Single-target categories** — allergies, medications, problems, observations. Each clinical-item type has a single canonical EPR field; landing elsewhere is a mapping failure.
> - **Multi-target categories with rules** — clinical content that may legitimately appear in more than one field (e.g. a smoking history may go into both the social-history structured field AND the consultation note free-text). The field-map document MUST name the rule per category (must-go-to-both / either-acceptable / preferred-with-fallback) so that what counts as "correct" is unambiguous.
> - **Free-text catchall** — content that has no structured target. The field-map document MUST identify which categories fall here per EPR; an allergy landing in free-text on a system that supports a structured allergy field is a critical failure.
>
> Inter-rater target on field-map authoring: ICC ≥ 0.85 between deployer reviewer and vendor reviewer. Where they disagree, the deployer reviewer's call is authoritative.

**Operational Specification**

> - **Per-EPR field map MANDATORY:** authored before pre-deployment gate; reviewed annually or on EPR version change. Without the field-map document, "correct field" has no operational definition.
> - **Per-category reporting MANDATORY:** five sub-rates (allergies / medications / problems / observations / free-text) reported separately. Aggregate-only reporting hides the failure pattern that matters.
> - **Critical-failure classification MANDATORY:** safety-critical content (allergies, medications, doses, problem-list entries) landing in non-safety-critical fields (consultation note free-text, history free-text) is a critical-class failure regardless of frequency. Critical-rate reported separately as a leading safety indicator.
> - **Test corpus inheritance:** uses the same ≥ 200-cases-per-EPR test corpus as TP.WB-1, with per-test-case expected-target-field annotation. Pre-deployment gate runs both metrics on the same corpus.
> - **Failure-mode classification:** each failure recorded as (i) wrong field same category (e.g. allergy to wrong allergy sub-field); (ii) wrong category (e.g. allergy to medication); (iii) free-text fallback when structured target available; (iv) multi-target rule violation. Type (iii) on safety-critical categories is a critical-class failure (silent safety-mechanism bypass per the Novel Thinking section).

**Trigger Conditions**

> ⚠️ **Provenance:** the safety-critical-content-in-non-safety-critical-fields zero-tolerance posture follows from the clinical-safety logic in TP.WB-3's Why-this-tier and Novel Thinking sections (and TP.WB-1's parallel framing). Specific numerical thresholds (100 % safety-critical-category gate, ≥ 95 % per-category gate, type-(iii) zero-tolerance) are **proposed in v3.7 as starting points**, not externally validated. Per the [Calibration & Context principle](#calibration-context), the per-EPR field-map content is highly deployment-dependent — local calibration is the substantive work here, not the threshold numbers.
>
> - **Pre-deployment gate (per EPR):** field-map document complete and signed off; safety-critical-category mapping accuracy = 100 % on test corpus; per-category accuracy ≥ 95 % each; zero type-(iii) safety-critical failures.
> - **Continuous monitoring:** monthly audited mapping accuracy ≥ 99 % on safety-critical categories; alert on any type-(iii) safety-critical failure detected in production traffic (no rate threshold — single instance is alert-worthy); alert if any per-category rate falls below 90 % in any audit cycle.
> - **Pause / escalation trigger:** any type-(iii) failure on allergy or medication-dose categories confirmed in production; OR aggregate safety-critical-category mapping accuracy < 95 % in any monthly audit cycle.
>
> Specific numerical starting points are deployment-context-dependent and live in [Threshold Reference: TP.WB-3](../thresholds.md#tp-wb-3). Treat them as starting points to calibrate locally — not as contractual gates.



**Limitations**

> Requires clear ground truth on which field each item should land in. Some items legitimately belong in multiple fields. The Operational Specification's mandatory per-EPR field-map document makes this requirement explicit; it does not eliminate the authoring burden, which is genuinely substantial for a multi-EPR deployment.

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
| **Pipeline Layer** | Downstream Write-back |
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

**Reference Standard**

> Per-EPR + per-category behaviour-rule document, authored by the deployer with vendor sign-off. The rule document specifies the **expected behaviour** per (clinical-item-category × update-context) cell, where:
>
> - **Update context** is one of: (a) new content where existing record has no entry; (b) new content semantically equivalent to existing entry; (c) new content adding to existing entry (e.g. new allergy added to existing list); (d) new content contradicting / superseding existing entry (e.g. resolved problem); (e) new content with lower information density than existing (e.g. brief mention where detailed prior history exists).
> - **Categories** are the same five as [TP.WB-3 Field Mapping Accuracy](#tp-wb-3): allergies, medications, problems, observations, free-text.
>
> Each cell has an expected behaviour: **overwrite** (replace existing), **append** (add alongside, preserving existing), **merge** (semantic combine, e.g. consolidate equivalent entries), **skip** (do nothing). Cells without explicit rules default to skip-with-flag (record the proposed update but do not apply, surface to clinician for review).
>
> Inter-rater target on rule authoring: ICC ≥ 0.85 between deployer reviewer and vendor reviewer. Where they disagree, the deployer reviewer's call is authoritative; the disagreement itself is logged.
>
> **Critical failure modes** (single-instance pause triggers):
> - **Overwriting with less complete data on safety-critical categories** (allergies, medications, problems) — context (e) above on safety-critical categories must default to skip-with-flag, never overwrite
> - **Skipping a legitimate update on safety-critical categories** — context (a) on safety-critical must always result in append; failure to write a new allergy is a silent safety event
> - **Duplicate-without-merge on safety-critical categories** — context (b) on safety-critical must result in merge, not append; appending a duplicate medication entry is an alert-fatigue source that contributes to downstream prescribing errors

**Operational Specification**

> - **Per-EPR + per-category rule document MANDATORY:** authored before pre-deployment gate; reviewed annually or on EPR schema change. Without the document, "correctness" has no operational definition.
> - **Test corpus MANDATORY:** ≥ 50 test cases per (category × update-context) cell — i.e. ≥ 50 cases × 5 categories × 5 contexts = ≥ 1250 test cases per EPR. Test cases exercise both expected-behaviour-honoured and adversarial edge cases (rapid successive updates, contradictory updates, ambiguous semantic equivalence).
> - **Per-cell reporting MANDATORY:** behaviour correctness reported per (category × context) cell. Aggregate-only reporting hides exactly the cells where the safety failures live (safety-critical category × overwrite-with-less-data context).
> - **Duplicate-detection windowing MANDATORY:** the deployer's duplicate-detection logic (does an entry written 2 minutes ago count as duplicate? 2 hours? 2 days?) MUST be documented with the windowing rule. Without explicit windowing, duplicate / merge cells are operationally meaningless.
> - **Skip-with-flag pathway MANDATORY:** the workflow for surfacing skip-with-flag events to the clinician MUST be documented and tested at pre-deployment. Skip-without-flag is a silent failure of the metric.

**Trigger Conditions**

> ⚠️ **Provenance:** the four-behaviour taxonomy and the safety-critical critical-failure classification follow from the existing Formal Definition and Novel Thinking. Specific numerical thresholds (≥ 50 cases per cell, 100 % safety-critical critical-failure-mode gate, ≥ 95 % per-cell gate elsewhere) are **proposed in v3.7 as starting points**, not externally validated. Per the [Calibration & Context principle](#calibration-context), the rule-document content is the substantive calibration work; the threshold numbers are starting points for that work.
>
> - **Pre-deployment gate (per EPR):** rule document complete and signed off; test corpus passes with zero safety-critical critical-failure-mode events; per-cell behaviour correctness ≥ 95 % across all cells; skip-with-flag pathway tested end-to-end.
> - **Periodic audit:** quarterly review of production-traffic update behaviour against the rule document; alert on any safety-critical critical-failure-mode event detected (single instance); alert if any (category × context) cell falls below 90 % correctness in any audit cycle.
> - **Pause / escalation trigger:** any safety-critical critical-failure-mode event confirmed in production (overwrite-with-less-data on allergies / medications / problems; skipped legitimate addition; duplicate-without-merge on safety-critical category); OR aggregate safety-critical-category cell correctness < 95 % in any audit cycle.
>
> Specific numerical starting points are deployment-context-dependent and live in [Threshold Reference: TP.WB-4](../thresholds.md#tp-wb-4). Treat them as starting points to calibrate locally — not as contractual gates.



**Limitations**

> Correct behaviour is context-dependent and varies by EPR system. Each EPR has different conventions for structured data updates. The Operational Specification's mandatory per-EPR rule document makes this requirement explicit and visible; the authoring burden is genuinely substantial (per-EPR × per-category × per-context grid) and is itself a calibration cost. The duplicate-detection-windowing rule remains a deployment-context call — there is no externally validated standard windowing convention.

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
| **Pipeline Layer** | Downstream Write-back |
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

Validated conformance of generated structured data against FHIR R4 profiles. FHIR is increasingly the interoperability standard for NHS EPRs; systems that produce technically parseable but profile-non-conformant resources create silent integration failures downstream. FHIR-structured output generally retains more clinical detail than legacy free-text-only or HL7 v2 formats, but retention is not the same as profile conformance — a record can preserve content while violating the profile that downstream systems rely on.

|Dimension              |Value                                    |
|-----------------------|-----------------------------------------|
| **Reference** | TP.WB-6 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                   |
|**Measurement Cadence**|Continuous                               |
|**Pipeline Layer**     |Downstream Write-back |
|**Assurance Question** |Fidelity & Accuracy                      |
|**Measurement Method** |Computational                            |
|**Lifecycle Phases**   |Pre-deployment, Continuous               |
|**Responsible Actors** |Vendor                                   |
|**Maturity**           |Established                              |
|**Outcome Type**       |Proximal                                 |
|**Applicability**      |AVT-Contextualised                       |
|**Source**             |[FHIR-UK-Core] R4 validation tooling|

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
|**Pipeline Layer**     |Downstream Write-back |
|**Assurance Question** |Fidelity & Accuracy                       |
|**Measurement Method** |Computational                             |
|**Lifecycle Phases**   |Pre-deployment, Continuous                |
|**Responsible Actors** |Vendor                                    |
|**Maturity**           |Established                               |
|**Outcome Type**       |Proximal                                  |
|**Applicability**      |AVT-Contextualised                        |
|**Source**             |[openEHR-Foundation]; [openEHR-Clinical-Knowledge-Manager] archetype library|

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

---

### TP.WB-8 🟢 PRSB Semantic Completeness

Proportion of PRSB-mandatory information elements present in AVT-generated output, evaluated against the applicable PRSB standard for the consultation type — Core Information Standard (CIS), Outpatient Letter, Discharge Summary, etc. The metric is the cross-framework heavyweight: the same construct surfaces under DTAC C4 (interoperability), FHIR UK Core (extension conformance), CQC Regulation 17 (good governance — adequate records), and PRSB itself. AVT systems that produce FHIR-conformant output but miss PRSB-mandatory information elements pass the structural-conformance metrics (TP.WB-1 / TP.WB-6) while failing the semantic-completeness one this metric tests.

|Dimension              |Value                                                   |
|-----------------------|---------------------------------------------------------|
| **Reference** | TP.WB-8 |
|**Priority Tier**      |🟢 Tier 1 - Minimum Viable                                |
|**Measurement Cadence**|Continuous; Event-triggered                              |
|**Pipeline Layer**     |Downstream Write-back                                    |
|**Assurance Question** |Quality                                                  |
|**Measurement Method** |Computational                                            |
|**Lifecycle Phases**   |Pre-deployment, Continuous                               |
|**Responsible Actors** |Vendor; Deployer                                         |
|**Maturity**           |Established                                              |
|**Outcome Type**       |Proximal                                                 |
|**Applicability**      |General Healthcare AI                                    |
|**Source**             |[PRSB] Core Information Standard; PRSB Outpatient Letter Standard; PRSB Discharge Summary Standard|

**Why this tier?**

> Tier 1 because of cross-framework leverage — DTAC C4 + FHIR UK Core + CQC Regulation 17 + PRSB itself all converge on this construct. A deployer who passes structural FHIR validation but fails PRSB semantic completeness is producing records that are technically interoperable but clinically inadequate. The metric is the most leverage-per-measurement item in the v5.3.0 pull-through set.

**Formal Definition**

```
For each AVT-generated record matched to a PRSB standard applicable to the consultation type, compute:
  completeness_i = |present_mandatory_elements_i| / |total_mandatory_elements_per_standard|
PRSB Semantic Completeness = mean(completeness_i) across the sampled set, stratified by consultation type / PRSB standard.
Reported per standard. A consultation that maps to no PRSB standard is excluded from the denominator.
```

**Limitations**

> Mandatory-element identification depends on the PRSB standards being machine-readable; not all standards expose a complete machine-readable element list, so part of the matching is done by structured human review of a sampled set. Vendor implementations of the same PRSB standard may map elements differently, which affects per-standard comparability. Stratification by consultation type matters: a primary-care AVT scoring well on CIS may score poorly on Outpatient Letter; a single composite hides this.

**Novel Thinking / Implications**

> 💡 PRSB semantic completeness is the cross-framework gap that the structural-conformance metrics cannot catch. A FHIR-conformant Composition resource can be mandatory-element-incomplete and still validate; a PRSB-complete record can fail FHIR validation. Both metrics are needed; making PRSB semantic completeness a Tier 1 metric in its own right pairs it with TP.WB-6 (FHIR R4 Resource Conformance Rate) at the same priority and forces deployers to evaluate both.
