## Clinical Coding

*SNOMED/Read code assignment. Individual care + population data quality.*

**Tier breakdown**: 🟡 2 Tier 2 · 🔵 2 Tier 3

### 🟡 SNOMED Code Accuracy

AI-suggested code correctness. Precision, recall, and F1 reported separately for diagnosis, medication, procedure codes.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Clinical Coding |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Day Zero Baseline, Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard clinical audit; NAS baselines |

**Why this tier?**

> Standard clinical audit. Recommended at Day Zero baseline and quarterly thereafter. Deployer-measurable with existing audit skills.

**Formal Definition**

```
Precision = |C_correct ∩ C_generated| / |C_generated|. Recall = |C_correct ∩ C_generated| / |C_reference|. F1 = harmonic mean. Report per code category.
```

**References**

- **SNOMED CT**: [SNOMED International](https://www.snomed.org/)

**Limitations**

> Requires clinician audit. Small samples.

---

### 🟡 Coding Inflation Detection

Systematic upcoding monitoring via SPC. In NHS, primary risk is data quality corruption of epidemiological data, QOF, and population health.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Clinical Coding |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Regional (ICB), National Body |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Source** | US payer countermeasures; NHS risk analysis |

**Why this tier?**

> Regional (ICB) monitoring using SPC on coding distributions. Requires pre-AVT baseline. National data integrity implication.

**Formal Definition**

```
SPC on pre/post-AVT code distributions. Track: code density (avg codes/encounter), severity shift, novel code rate. Flag if >2σ from baseline for ≥4 weeks (Western Electric rules).
```

**Code: SPC-based coding drift**

```python
import numpy as np

def coding_drift_spc(pre_counts, post_counts):
    mu = np.mean(pre_counts)
    sigma = np.std(pre_counts, ddof=1)
    ucl = mu + 3 * sigma  # upper control limit
    uwl = mu + 2 * sigma  # upper warning limit
    alerts = []
    for i, val in enumerate(post_counts):
        if val > ucl:
            alerts.append({"week": i+1, "rule": "3σ_breach"})
        if i >= 7 and all(v > mu for v in post_counts[i-7:i+1]):
            alerts.append({"week": i+1, "rule": "8_consecutive"})
    return {"baseline_mean": mu, "alerts": alerts}
```

**Limitations**

> NHS coding incentives differ from US.

**Novel Thinking / Implications**

> 💡 Risk is data quality: systematically different codes corrupt epidemiological data, QOF, population health analytics.

---

### 🔵 Code Specificity Index

Whether suggested codes are at appropriate hierarchy level. SNOMED has multiple specificity levels for the same concept; AI may default to over-general (loses detail) or over-specific (introduces false precision) codes inappropriately.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Clinical Coding |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | SNOMED CT hierarchy semantics; clinical audit methodology |

**Why this tier?**

> Requires clinical judgement and SNOMED hierarchy expertise. Suitable for periodic clinical audit.

**Formal Definition**

```
For each suggested code, compute hierarchical distance from clinically appropriate code. Specificity Index = mean signed distance: positive = over-specific, negative = over-general, zero = appropriate. Track distribution across coding categories.
```

**Limitations**

> Defining 'appropriate' specificity requires clinical judgement. The same condition may warrant different specificity in different contexts (e.g. primary care vs specialist).

**Novel Thinking / Implications**

> 💡 Over-specific coding is the more insidious problem: AI may code 'chest pain' as 'precordial chest pain' when the patient simply said 'pain in my chest'. The over-specific code carries information that wasn't in the source — a form of coded hallucination. Under-specific coding loses information but is more obviously a quality issue.

---

### 🔵 Code Suggestion Latency

Time from note generation to code suggestion availability. Affects coding workflow integration — if coding suggestions arrive too late, clinicians have moved on to the next patient and won't engage with them.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Clinical Coding |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard latency metric |

**Why this tier?**

> Operational metric. Important for adoption but not safety-critical.

**Formal Definition**

```
Latency = t_codes_available - t_note_generated. Report distribution. Threshold: P95 < 30 seconds for in-consultation review; < 5 minutes for next-patient batch review.
```

**Limitations**

> Latency requirements depend on workflow integration model.

---

