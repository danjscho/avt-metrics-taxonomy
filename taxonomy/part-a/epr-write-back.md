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

