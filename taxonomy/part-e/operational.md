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

**Threshold Guidance**

> ⚠️ **Provenance:** the requirement to pair DT with a quality companion metric and the in/out-of-consultation breakdown framing follow from [Coiera-Fraile-Navarro-JMIR-2026] and the [NIHR-RSET] 'time is not automatically convertible' caution cited above. Specific thresholds (4-week baseline window, 25 % TS trigger for review, 0 % out-of-consultation TS rule-out) are **proposed in v3.4 as starting points**, not externally validated. Indicative; require local calibration before contractual use.
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

