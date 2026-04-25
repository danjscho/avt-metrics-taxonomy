## EPR Write-back

*Data to permanent record. Where errors become patient safety events.*

**Tier breakdown**: 🟢 4 Tier 1 · 🟡 2 Tier 2 · 🔵 1 Tier 3

### Write-back Safety sub-cluster

*The four Tier 1 metrics that must pass before any AVT system writes to a live patient record. Each addresses a distinct failure mode at the EPR integration boundary: content correctness (Write-back Fidelity), pipeline reliability (Integration Error Rate), field routing (Field Mapping Accuracy), and data update semantics (Update vs Append Behaviour). All are pre-deployment gates; all are safety-critical.*

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
> - **Semantic equivalence** - the value preserves clinical meaning. For coded categories (c-e) semantic equivalence requires preservation of the coded concept (e.g. SNOMED CT identifier match, not just string match); for free text (a) it requires preservation of every clinically relevant proposition per the [TP.SN-6 Omission Rate](#tpsn-6-omission-rate) reference standard
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
