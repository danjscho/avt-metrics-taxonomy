## Fairness & Equity

*Population-level justice: demographic performance, deployment equity, domain coverage.*

**Tier breakdown**: 🟡 2 Tier 2 · 🔵 3 Tier 3

### 🟡 Deployment Equity Index

Whether AVT creates two-tier documentation quality across practices. Track against deprivation indices.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Regional (ICB), National Body |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | NHSE LLM framework wider impact |

**Why this tier?**

> Regional (ICB) monitoring. Track AVT deployment against deprivation indices. Commissioning equity question. Requires cross-organisational data.

**Formal Definition**

```
Correlation r(AVT_deployed, IMD_decile). Positive correlation = deployment inequity. Target: access independent of deprivation (r ≈ 0).
```

**Limitations**

> Requires cross-organisational data.

**Novel Thinking / Implications**

> 💡 If adoption correlates with affluence, technology amplifies inequalities.

---

### 🟡 Clinical Domain Performance Variance

Accuracy variation across specialties and complexity. Compound boundary risk: degradation multiplies across dimensions.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Compound boundary risk model |

**Why this tier?**

> Vendor should test across clinical domains. Deployers extending beyond primary care should request domain-specific performance data.

**Formal Definition**

```
Accuracy A(d) per clinical domain d. PV = Var(A(d)). Compound risk: performance in untested (domain, population, setting) degrades as product of boundary crossings.
```

**Limitations**

> All-domain testing impractical. Risk-based prioritisation needed.

**Novel Thinking / Implications**

> 💡 System tested in adult primary care urban England ≠ safe for paediatric ENT rural Wales.

---

### 🔵 Intersectional Performance

Accuracy at the intersection of demographic dimensions (e.g. elderly EAL women). Single-axis disaggregation misses compound disadvantage — a system may perform adequately on each dimension separately but fail badly at intersections.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor, National Body |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Intersectionality literature applied to AI fairness |

**Why this tier?**

> Important fairness dimension but requires large demographic-linked datasets and careful statistical analysis.

**Formal Definition**

```
For each intersection of demographic categories (age x ethnicity x language x gender x deprivation): compute accuracy if sample size permits. Identify worst-performing intersections. Compare with single-axis metrics to detect compound disadvantage.
```

**Limitations**

> Sample sizes at intersections may be too small for reliable measurement. Requires substantial demographic-linked evaluation data.

**Novel Thinking / Implications**

> 💡 An elderly, EAL, female patient with limited health literacy may be at the worst-case intersection for AVT accuracy — yet single-axis metrics for elderly, EAL, female, and low-literacy patients may all look acceptable individually. Intersectional analysis reveals this compound disadvantage. Required by population health equity but rarely measured.

---

### 🔵 Rare Presentation Handling

Accuracy on uncommon clinical presentations vs common ones. Long-tail performance matters disproportionately for diagnostic safety — the rare presentation that's missed is the most dangerous one to miss.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Long-tail performance analysis from machine learning literature |

**Why this tier?**

> Important but requires evaluation data spanning the long tail of clinical presentations.

**Formal Definition**

```
Stratify test data by presentation frequency. Compute accuracy for: common (top 10% of presentations), moderate (10-50%), rare (50-95%), very rare (bottom 5%). Long-tail Performance Ratio = accuracy_rare / accuracy_common.
```

**Limitations**

> Requires large evaluation dataset with rare presentations. Sample sizes for very rare conditions may be too small for reliable measurement.

**Novel Thinking / Implications**

> 💡 AVT systems trained on common presentations will perform best on common presentations and worst on rare ones. But rare presentations are exactly where clinical decision support matters most — the unusual case that benefits from accurate documentation. Long-tail performance should be a procurement question, not just average performance.

---

### 🔵 Health Literacy Performance Variation

Does AVT performance vary with patient health literacy level? Medically sophisticated patients use clinical terminology that ASR handles well; patients describing symptoms in lay terms may be harder to transcribe and summarise accurately.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Health literacy and equity research |

**Why this tier?**

> Important equity dimension but conceptually and methodologically novel.

**Formal Definition**

```
Compare accuracy on: (1) patients using clinical terminology; (2) patients using lay terms for the same conditions. Performance Gap = accuracy_clinical_terms - accuracy_lay_terms. Significant gap indicates the system rewards health literacy — an equity concern.
```

**Limitations**

> Health literacy is hard to measure. Distinguishing 'lay terms' from 'clinical terms' is not always clean.

**Novel Thinking / Implications**

> 💡 If AVT performs better when patients use clinical language, the system rewards health literacy and disadvantages patients who describe symptoms in everyday terms. This compounds existing health inequalities — the patients who already face barriers to healthcare get less accurate documentation as well. This is an equity dimension that single-axis demographic metrics miss.

---

