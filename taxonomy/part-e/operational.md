## Operational

*System performance, adoption, efficiency. Necessary but not sufficient for assurance.*

**Tier breakdown**: 🟢 3 Tier 1 · 🟡 2 Tier 2 · 🔵 1 Tier 3

### 🟢 Documentation Time per Consultation

Most cited benefit metric. Tells you nothing about safety. 'Time saved' alone is meaningless — pair with quality.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Day Zero Baseline, Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Widely used; critiqued Coiera & Fraile-Navarro 2026 |

**Why this tier?**

> Most widely measured benefit metric. Tells you nothing about safety but essential for demonstrating value proposition. Must be reported alongside quality metrics.

**Formal Definition**

```
DT = t_doc_end - t_doc_start. Quality-adjusted: report alongside PDSQI-9 or hallucination rate. TS = DT_pre - DT_post. Meaningful only if quality stable/improving.
```

**References**

- **Critique**: Coiera & Fraile-Navarro (2026)
- **RSET**: 'Time is not automatically convertible into money, productivity, or better care'

**Limitations**

> Says nothing about safety.

**Novel Thinking / Implications**

> 💡 'Saved 3 min and maintained >98% PDSQI-9' is meaningful. 'Saved 3 min' alone is not.

---

### 🟢 System Availability / Uptime

Percentage operational. NAS: ≥99.5% during consultation hours.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard SLA; NAS SPI |

**Why this tier?**

> Standard SLA monitoring. NAS Day Zero SPI (≥99.5%). Automated, zero-burden continuous metric.

**Formal Definition**

```
A = (T_operational - T_down) / T_operational × 100. Include degraded: A_eff = (T_op - T_down - T_degraded) / T_op × 100.
```

**Limitations**

> Binary misses degraded performance.

---

### 🟢 Adoption Rate & Selective Use Patterns

Who uses AVT and for which consultations. Selective patterns reveal practical system boundaries.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
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

### 🟡 Cost per Consultation

Total cost including licence, infrastructure, training, and governance overhead. Often under-reported by vendors who quote licence costs only without including operational burden.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
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

> 💡 Vendor quotes typically include licence cost only. The full cost of operating AVT includes substantial governance overhead — CSO time, training, audit, incident response. Practices that compute true cost per consultation often find the value proposition is much weaker than vendor materials suggest.

---

### 🔵 Governance & Maintenance Burden

Clinician and admin time spent on AVT-related tasks: template updates, error reporting, incident investigation, audit, training delivery. Per week per clinician using AVT.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
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

### 🟡 Training Time per Clinician

Initial and refresher training hours required per clinician. Affects both adoption (high training burden = slow adoption) and ongoing operational cost.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
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

