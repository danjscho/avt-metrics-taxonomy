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
| **Source** | Widely used; critiqued [Coiera-Fraile-Navarro-JMIR-2026] |

**Why this tier?**

> Most widely measured benefit metric. Tells you nothing about safety but essential for demonstrating value proposition. Must be reported alongside quality metrics.

**Formal Definition**

```
DT = t_doc_end - t_doc_start. Quality-adjusted: report alongside PDSQI-9 or hallucination rate. TS = DT_pre - DT_post. Meaningful only if quality stable/improving.
```

**Reference Standard**

> EPR + AVT product telemetry. "Documentation start" = first keystroke or first AVT activation in the note's edit session, whichever is earlier. "Documentation end" = clinician signature event on the note. Time spent reviewing AVT-generated content **counts as documentation time**; the metric measures total clinician note-effort, not just typing time. The metric MUST be reported alongside a quality companion metric ([TP.SN-3 PDSQI-9](#tp-sn-3), [TP.SN-5 Hallucination Rate](#tp-sn-5), or equivalent) - DT in isolation is not interpretable per [Coiera-Fraile-Navarro-JMIR-2026].

**Operational Specification**

> - **Window:** weekly aggregate per clinician, with continuous monitoring trajectory.
> - **In-consultation vs out-of-consultation breakdown MANDATORY:** documentation completed during the patient encounter reported separately from documentation completed after the patient has left. AVT systems can reduce in-consultation time while increasing out-of-consultation time - aggregating the two hides the failure mode.
> - **After-hours boundary MANDATORY:** documentation completed outside the clinician's scheduled clinical hours is tracked under [GV.OP-2 Pyjama Time / After-Hours EHR Use](#gv-op-2), not under DT. Both metrics must be reported together; reporting DT alone risks hiding burden displacement.
> - **Per-clinician baseline MANDATORY:** the deployment baseline is the median weekly DT across the first 4 weeks of clinician live use. Time-saved (TS) calculations reference this per-clinician baseline, not a pooled cohort baseline (parallel to [HL.HF-1 Edit Rate](#hl-hf-1)).
> - **Aggregation:** report median DT and the time-saved (TS) trajectory; do not collapse to a single number without quality companion metric.

**Trigger Conditions**

> ⚠️ **Provenance:** the requirement to pair DT with a quality companion metric and the in/out-of-consultation breakdown framing follow from [Coiera-Fraile-Navarro-JMIR-2026] and the [NIHR-RSET] 'time is not automatically convertible' caution cited above. Specific thresholds (4-week baseline window, 25 % TS trigger for review, 0 % out-of-consultation TS rule-out) are **proposed in v3.4 as starting points**, not externally validated. Indicative; require local calibration before contractual use.
>
> - **Pre-deployment / Day Zero baseline:** establish per-clinician DT median across the first 4 weeks of live use, with separate medians for in-consultation and out-of-consultation segments. Quality companion metric measured concurrently.
> - **Continuous monitoring:** weekly DT trajectory per clinician; report TS only when paired with quality companion metric. Flag for review: TS > 25 % from baseline (the magnitude triggers a quality cross-check, not a celebration).
> - **Pause / review trigger:** any TS reported without quality data; OR in-consultation TS > 0 paired with out-of-consultation DT increase (suggests burden displacement to after-hours, not reduction); OR TS positive while quality companion metric (PDSQI-9, hallucination rate) deteriorates.
>
> Specific numerical starting points are deployment-context-dependent and live in [Threshold Reference: GV.OP-1](../thresholds.md#gv-op-1). Treat them as starting points to calibrate locally — not as contractual gates.



**References**

- **Critique**: [Coiera-Fraile-Navarro-JMIR-2026]
- **RSET**: [NIHR-RSET] — 'Time is not automatically convertible into money, productivity, or better care'

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
| **Source** | [Sinsky-Mayo-EHR-Studies] (concept: physician time-allocation); [Sinsky-Adler-Milstein-EHR-Logs-2020] (methodology: audit-log-derived activity metrics); American Medical Association EHR use studies |

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

*See also: Documentation Time per Consultation - paired metric. GV.OP-1 measures clinician note-effort time (start-of-doc to signature); GV.OP-3 measures end-to-end record-availability time (consultation end to EPR availability). Easily confused; the names invite it.*

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
| **Source** | [Sinsky-Mayo-EHR-Studies] extended to AVT context; NHS workforce wellbeing frameworks |

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
| **Source** | Standard SLA; [NAS-Day-Zero-SPI-internal] |

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


### GV.OP-14 🟡 Historical Output Continuity

After an AVT product is retired, replaced, or decommissioned, can clinicians and patients still access the AI-generated content (notes, transcripts, structured codings) that was committed to clinical records during the deployment's operational period? Distinct from [GV.PD-16 Decommissioning Data Handling Compliance](#gv-pd-16) (which covers *deletion* of operational data on decommissioning) — this metric covers the inverse case: data that *should* persist (i.e. the clinical records produced during operational use) and remain accessible after the product is gone.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.OP-14 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate + per-event |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | Promoted from `_gaps.md` P5-Lifecycle "Decommissioning plan" entry; complements [GV.VT-15 Retirement Notification Compliance](#gv-vt-15) and [GV.PD-16 Decommissioning Data Handling Compliance](#gv-pd-16) |

**Why this tier?**

> Clinical records are durable: a note signed in the EPR in 2026 must remain accessible for the patient's clinical lifetime, regardless of whether the AVT vendor that helped produce it is still in business. The continuity question — *can the deployer still serve up that note as evidence of decision-making, or has the AVT layer's retirement broken the audit trail?* — is medium-stakes (continuity of care, medico-legal evidence preservation) but not as time-sensitive as the GV.VT-15 / GV.PD-16 events themselves. Tier 2 because the failure mode is recoverable (alternative records of the same consultation usually exist) and because the pre-deployment gate (does the contract specify post-retirement read-access?) is the load-bearing part; per-event verification only matters when retirement actually happens.

**Formal Definition**

```
Compliance gate (pre-deployment) = the deployer's procurement contract specifies post-retirement access provisions for: (a) AI-generated content committed to the EPR (must remain accessible from the EPR independent of the AVT vendor); (b) audit trail / provenance metadata (linked-evidence provenance per TP.SN-12 must remain dereferenceable); (c) any structured-data commitments (FHIR resources per TP.WB-6, openEHR per TP.WB-7).

Per-event compliance (when retirement occurs) = (every committed-record category remains accessible AND the audit trail dereferences correctly AND patient-facing access is preserved) for the contractual access window.

Three sub-metrics: (i) EPR-commit independence (does the AI-generated content live in the EPR record without runtime dependency on the vendor?); (ii) provenance dereference (do TP.SN-12 evidence-link mappings still resolve?); (iii) patient-portal access preservation (can patients still see AI-generated content shared with them, e.g. via SAR or patient portal?).
```

**Reference Standard**

> Inherits the EPR-commit envelope from [TP.WB-1 Write-back Fidelity](#tp-wb-1): once an AI-generated note is committed to the EPR, the EPR is the system of record. This metric verifies that the commit is *complete* — that no field, attachment, or cross-reference depends on the AVT vendor's continuing presence at read time. Specific dependencies to check: (i) provenance metadata (linked-evidence per [TP.SN-12 Evidence Linking Coverage](#tp-sn-12)) — are the source-segment references stored in the EPR, or do they resolve only via vendor APIs?; (ii) confidence scores (per [TP.ASR-11 ASR Confidence Exposure](#tp-asr-11)) — are they committed as field values or rendered live from vendor systems?; (iii) audit trails (per [GV.VT-4 Audit Trail Completeness](#gv-vt-4)) — does the vendor hold the only copy?

**Operational Specification**

> - **Window:** procurement contract review (one-off gate); per-event tracking when retirement occurs.
> - **Three sub-metrics MANDATORY:** (a) commit-completeness gate (does every AI-generated artefact land in the EPR with no vendor-runtime dependency?); (b) provenance-dereference compliance (do evidence links and audit trails remain accessible?); (c) patient-access preservation (does the patient portal / SAR pathway continue to surface AI-generated content?).
> - **Pre-deployment verification MANDATORY:** synthetic-retirement test before go-live — disconnect the AVT vendor for 24 hours and verify that committed records remain readable in the EPR, the audit trail still dereferences, and the patient-portal pathway continues to function. Failures discovered in this test are remediated before go-live, not after.
> - **Cross-link to retirement notification:** every retirement event triggered by [GV.VT-15 Retirement Notification Compliance](#gv-vt-15) activates this metric's per-event verification. The vendor-side migration plan (per GV.VT-15's mandatory content element (iv)) MUST address the three sub-metrics above.
> - **Contractual access window MANDATORY:** the procurement contract specifies the minimum period during which the vendor will support read-access to historical content post-retirement (typical floor: 7 years to align with NHS clinical-record retention).

**Trigger Conditions**

> ⚠️ **Provenance:** the EPR-as-system-of-record framing carries from [TP.WB-1 Write-back Fidelity](#tp-wb-1) and the broader v3.x write-back metrics. The 7-year contractual access window aligns with NHS clinical-record retention but is **proposed in v4.0.2 as a starting point** for AVT deployments; specialty-specific retention rules may apply (paediatric records up to 25 years, mental health to 20). Specific thresholds (24-hour synthetic-retirement test, 100 % three-sub-metric pre-deployment gate, 95 % provenance-dereference compliance per-event) are **proposed in v4.0.2 as starting points**, not externally validated.
>
> - **Pre-deployment gate:** synthetic-retirement test passes — committed records readable; provenance links resolve; patient-portal access preserved. Contract specifies post-retirement access window ≥ 7 years (or specialty-appropriate floor).
> - **Per-event monitoring:** retirement events trigger logging of (a) commit-completeness verification rerun, (b) provenance-dereference rate at retirement-day +30, (c) patient-portal access verification. Aggregate compliance reported per retirement event.
> - **Pause / escalation trigger:** synthetic-retirement test reveals any committed-content category that cannot be read without the vendor running (pre-deployment gate failure); OR per-event provenance-dereference rate < 90 % at retirement-day +30; OR patient-portal access pathway degrades.
>
> Specific numerical starting points are deployment-context-dependent and live in [Threshold Reference: GV.OP-14](../thresholds.md#gv-op-14). Treat them as starting points to calibrate locally — not as contractual gates.



**Limitations**

> Architecture-dependent: deployments where AI-generated content is properly committed to the EPR with all provenance metadata co-located fare well on this metric; deployments where the EPR holds only a pointer to vendor-hosted content are structurally exposed regardless of the contractual access window. Many vendor implementations split the difference (note text in EPR; provenance lookup via vendor API). The metric makes the architecture-vs-contract trade-off visible but cannot resolve it — the architectural choice is made at procurement, before the contract addresses retirement.
>
> Distinct from but related to [GV.VT-6 Exit & Data Portability Provisions](#gv-vt-6), which measures contract-clause completeness; this metric measures whether the *underlying architecture* supports the post-retirement access the contract describes. Both are needed: a contract guaranteeing post-retirement access for content that's architecturally vendor-runtime-dependent is not an effective guarantee.

**Novel Thinking / Implications**

> 💡 Vendor retirement is the AVT-procurement failure mode the field hasn't faced at scale. When it does — whether because a vendor exits, pivots, or is acquired and consolidated — the question that surfaces will not be "did we have the right contract clauses?" but "can we still read the notes?" Treating historical-output continuity as a Tier 2 metric — verified pre-deployment via a synthetic-retirement test — moves the discovery to procurement time, where the architectural choice can still be made. Without the synthetic-retirement test, deployers learn at retirement time which of their commit-completeness assumptions were correct.
