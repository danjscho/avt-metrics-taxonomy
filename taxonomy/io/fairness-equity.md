### IO.FE-1 🟡 Deployment Equity Index

Whether AVT creates two-tier documentation quality across practices. Track against deprivation indices.

| Dimension | Value |
|-----------|-------|
| **Reference** | IO.FE-1 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Regional (ICB), National Body |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
| **Source** | [NHS-LLM-Framework] wider impact |

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

### IO.FE-2 🟡 Accent Taxonomy Standardisation

Meta-metric assessing whether demographic-disaggregated WER uses a sociolinguistically informed accent taxonomy appropriate for NHS populations, rather than ad-hoc or inappropriate categorisations. The FAccT 2024 critique of ASR accent categorisation highlighted that race-based, geography-based, and native/non-native categories are systematically flawed proxies for the actual acoustic variation that affects ASR performance. For NHS deployment, a meaningful taxonomy must cover British regional accents, South Asian English varieties, West African English, Caribbean English, Eastern European English, and other varieties representative of NHS patient populations.

|Dimension              |Value                                                         |
|-----------------------|--------------------------------------------------------------|
| **Reference** | IO.FE-2 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                        |
|**Measurement Cadence**|One-off gate                                                  |
|**Pipeline Layer**     |ASR / Transcription                                           |
|**Assurance Question** |Fairness & Equity                                             |
|**Measurement Method** |Human Review                                                  |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                |
|**Responsible Actors** |Vendor, National Body                                         |
|**Maturity**           |Proposed / Novel                                              |
|**Outcome Type**       |Proximal                                                      |
|**Applicability**      |AVT-Specific                                                  |
|**Source**             |[FAccT-2024-ASR-Accent-Critique]; sociolinguistics literature|

**Why this tier?**

> Prerequisite for meaningful fairness assessment. Without a defensible taxonomy, Demographic-Disaggregated WER numbers are not comparable across vendors and may hide rather than reveal bias.

**Formal Definition**

```
Assessment against criteria: (1) Sociolinguistic validity - categories correspond to identifiable phonological communities, not political or racial groupings; (2) NHS relevance - categories include varieties actually present in NHS patient populations; (3) Sample adequacy - each category has sufficient evaluation data for stable WER estimation; (4) Documentation - categorisation methodology is transparent and replicable. Binary pass/fail per criterion; composite = all four must pass.
```

**Limitations**

> Sociolinguistic categorisation is itself contested. Any taxonomy makes choices that can be critiqued. The alternative - no categorisation - is worse because it hides all disparities.

**Novel Thinking / Implications**

> 💡 The hardest form of bias to fix is bias that cannot be measured, and ad-hoc accent categorisation produces unmeasurable bias. An NHS-specific accent taxonomy is infrastructure that would benefit every deployed AVT system - a national body responsibility that would pay for itself quickly. Without it, every vendor's Demographic-Disaggregated WER is self-reported against self-chosen categories, and independent verification is impossible.

### IO.FE-3 🟡 Clinical Domain Performance Variance

Accuracy variation across specialties and complexity. Compound boundary risk: degradation multiplies across dimensions.

| Dimension | Value |
|-----------|-------|
| **Reference** | IO.FE-3 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

### IO.FE-4 🔵 Intersectional Performance

Accuracy at the intersection of demographic dimensions (e.g. elderly EAL women). Single-axis disaggregation misses compound disadvantage - a system may perform adequately on each dimension separately but fail badly at intersections.

| Dimension | Value |
|-----------|-------|
| **Reference** | IO.FE-4 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor, National Body |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

> 💡 An elderly, EAL, female patient with limited health literacy may be at the worst-case intersection for AVT accuracy - yet single-axis metrics for elderly, EAL, female, and low-literacy patients may all look acceptable individually. Intersectional analysis reveals this compound disadvantage. Required by population health equity but rarely measured.

---

### IO.FE-5 🔵 Intersectional Compound Fairness Score

Extension of the existing Intersectional Performance metric using the FAIR-MED Compound Fairness Score methodology. Where Intersectional Performance measures accuracy at each demographic intersection, Compound Fairness Score calculates whether disadvantage compounds multiplicatively or additively - that is, whether the intersection performs worse than would be predicted by adding the individual demographic disadvantages.

|Dimension              |Value                                                                                |
|-----------------------|-------------------------------------------------------------------------------------|
| **Reference** | IO.FE-5 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research                                                       |
|**Measurement Cadence**|Periodic audit                                                                       |
|**Pipeline Layer**     |Cross-cutting                                                                        |
|**Assurance Question** |Fairness & Equity                                                                    |
|**Measurement Method** |Computational                                                                        |
|**Lifecycle Phases**   |Periodic Audit                                                                       |
|**Responsible Actors** |Vendor, National Body, Academic                                                      |
|**Maturity**           |Emerging                                                                             |
|**Outcome Type**       |Distal                                                                               |
|**Applicability**      |General Healthcare AI                                                                |
|**Source**             |[FAIR-MED-Springer-2025] (Bias Detection and Fairness Evaluation in Healthcare Focused XAI)|

**Why this tier?**

> Research-grade methodology requiring substantial demographic-linked data. National evaluation or vendor pre-deployment. Complements rather than replaces single-axis fairness metrics.

**Formal Definition**

```
For demographic axes A₁, A₂, ..., Aₙ with performance gaps gap(Aᵢ): expected intersection gap under additive model = Σ gap(Aᵢ); actual intersection gap = observed gap at intersection ∩Aᵢ. Compound Fairness Score CFS = actual_gap / expected_additive_gap. CFS > 1 indicates multiplicative compounding (intersection is worse than sum of parts); CFS ≈ 1 indicates additive; CFS < 1 indicates sub-additive. Multiplicative compounding is the warning signal for worst-case population failures.
```

**Limitations**

> Requires large enough samples at every demographic intersection for stable estimation - often infeasible for rare intersections. Additive model assumption may not hold even in fair systems. Interpretation is statistical rather than mechanistic.

**Novel Thinking / Implications**

> 💡 Single-axis fairness can miss compound disadvantage entirely. A system that performs acceptably on "elderly", "EAL", "female", and "low literacy" as separate categories may perform catastrophically on the intersection. The compound fairness score tests whether this is happening and quantifies how bad it is. For NHS populations where intersectional disadvantage is the rule rather than the exception, single-axis metrics alone are insufficient.

### IO.FE-6 🔵 Rare Presentation Handling

Accuracy on uncommon clinical presentations vs common ones. Long-tail performance matters disproportionately for diagnostic safety - the rare presentation that's missed is the most dangerous one to miss.

| Dimension | Value |
|-----------|-------|
| **Reference** | IO.FE-6 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

> 💡 AVT systems trained on common presentations will perform best on common presentations and worst on rare ones. But rare presentations are exactly where clinical decision support matters most - the unusual case that benefits from accurate documentation. Long-tail performance should be a procurement question, not just average performance.

---

### IO.FE-7 🔵 Health Literacy Performance Variation

Does AVT performance vary with patient health literacy level? Medically sophisticated patients use clinical terminology that ASR handles well; patients describing symptoms in lay terms may be harder to transcribe and summarise accurately.

| Dimension | Value |
|-----------|-------|
| **Reference** | IO.FE-7 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
| **Source** | Health literacy and equity research |

**Why this tier?**

> Important equity dimension but conceptually and methodologically novel.

**Formal Definition**

```
Compare accuracy on: (1) patients using clinical terminology; (2) patients using lay terms for the same conditions. Performance Gap = accuracy_clinical_terms - accuracy_lay_terms. Significant gap indicates the system rewards health literacy - an equity concern.
```

**Limitations**

> Health literacy is hard to measure. Distinguishing 'lay terms' from 'clinical terms' is not always clean.

**Novel Thinking / Implications**

> 💡 If AVT performs better when patients use clinical language, the system rewards health literacy and disadvantages patients who describe symptoms in everyday terms. This compounds existing health inequalities - the patients who already face barriers to healthcare get less accurate documentation as well. This is an equity dimension that single-axis demographic metrics miss.

---

---

### IO.FE-8 🔵 Cross-Platform Fairness Consistency

Whether fairness properties are consistent across multiple AVT platforms deployed within the same ICB or trust. Differential bias between vendors is itself an equity concern - if Practice A uses Vendor X (which performs well on majority populations but poorly on minority populations) and Practice B uses Vendor Y (with the opposite bias profile), patients experience different quality of documentation depending on which practice happens to serve them.

|Dimension              |Value                                                              |
|-----------------------|-------------------------------------------------------------------|
| **Reference** | IO.FE-8 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research                                     |
|**Measurement Cadence**|Periodic audit                                                     |
|**Pipeline Layer**     |Cross-cutting                                                      |
|**Assurance Question** |Fairness & Equity                                                  |
|**Measurement Method** |Computational                                                      |
|**Lifecycle Phases**   |Periodic Audit                                                     |
|**Responsible Actors** |Regional (ICB), National Body                                      |
|**Maturity**           |Proposed / Novel                                                   |
|**Outcome Type**       |Distal                                                             |
|**Applicability**      |General Healthcare AI                                              |
|**Source**             |Extension of existing Cross-Practice Variance Coefficient into equity dimension|

**Why this tier?**

> Regional or national metric. Requires cross-vendor evaluation on equivalent test data. Only meaningful where multiple platforms are deployed across an integrated care system.

**Formal Definition**

```
For each vendor v in the ICB's deployed platforms: compute demographic-disaggregated performance profile P_v. Cross-Platform Fairness Consistency = variance of P_v across vendors for each demographic group. High variance = patients experience differential fairness depending on which practice (and which vendor) they attend. Report per demographic group; worst-case group determines the equity-consistency floor for the ICB.
```

**Limitations**

> Requires standardised test data available for use against multiple vendors - which currently doesn't exist for NHS. Vendors may resist independent cross-comparison. Aggregation across practices raises information governance questions.

**Novel Thinking / Implications**

> 💡 The current NHS AVT landscape allows ICBs to have multiple vendors deployed across their patch. If those vendors have different fairness profiles, the ICB is effectively running an uncontrolled experiment where patient outcomes depend on which GP they happened to register with. This is invisible to single-vendor fairness metrics and can only be detected by cross-platform comparison. Commissioning should consider fairness consistency as a portfolio-level property, not just a single-vendor property.
