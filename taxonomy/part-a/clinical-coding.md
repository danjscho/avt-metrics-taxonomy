## Clinical Coding

*SNOMED/Read code assignment. Individual care + population data quality.*

**Tier breakdown**: 🟢 1 Tier 1 · 🟡 8 Tier 2 · 🔵 3 Tier 3

### Coding Fidelity sub-cluster

*Accuracy of individual code assignment across NHS terminology systems - SNOMED CT, ICD-10/11, OPCS-4, and dm+d. Each metric addresses a different coding standard or a different failure mode (wrong code, non-existent code, wrong specificity level, wrong concept mapping). Together they answer the question: when the system assigns a code, is it the right code at the right level of specificity in the right terminology?*

### TP.CC-1 🟡 SNOMED Code Accuracy

AI-suggested code correctness. Precision, recall, and F1 reported separately for diagnosis, medication, procedure codes.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.CC-1 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
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

### TP.CC-2 🟡 SNOMED CT Concept Mapping Accuracy

Accuracy of the mapping from extracted clinical entities in free-text to the correct SNOMED CT concept ID. Distinct from the existing SNOMED Code Accuracy metric, which measures whether the assigned code is clinically correct. Concept mapping measures whether the system correctly resolves "chest pain" to the correct SNOMED concept (29857009 - chest pain) rather than a near-miss concept (102588006 - chest discomfort). The boundary between correct and near-miss is where most mapping errors occur.

|Dimension              |Value                                                                    |
|-----------------------|-------------------------------------------------------------------------|
| **Reference** | TP.CC-2 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                                   |
|**Measurement Cadence**|Periodic audit                                                           |
|**Pipeline Layer**     |Clinical Coding                                                          |
|**Assurance Question** |Fidelity & Accuracy                                                      |
|**Measurement Method** |Computational                                                            |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                           |
|**Responsible Actors** |Vendor                                                                   |
|**Maturity**           |Established                                                              |
|**Outcome Type**       |Proximal                                                                 |
|**Source**             |NLP2FHIR pipeline literature; John Snow Labs FHIR-Ready AI; MedCAT benchmarks|

**Why this tier?**

> Vendor pre-deployment metric. Should be reported alongside SNOMED Code Accuracy. Essential for NHS interoperability as ambient scribes increasingly drive structured data entry.

**Formal Definition**

```
For each extracted clinical mention m: mapping function M(m) → SNOMED concept ID. Accuracy = |correctly_mapped| / |total_mentions|. Additional measures: (a) Exact Match Rate - mapped to exactly the reference concept; (b) Hierarchical Match Rate - mapped to an ancestor or descendant within 2 levels of reference; (c) Semantic Type Match Rate - mapped to correct semantic category. Report all three because acceptable mapping depth depends on context.
```

**Limitations**

> "Correct" mapping is context-dependent - sometimes a more general concept is preferable to an over-specific one. Ground truth annotation requires SNOMED expertise. NHS-specific subset mappings add complexity (not all SNOMED concepts are in the UK Edition).

**Novel Thinking / Implications**

> 💡 Concept mapping is where most structured data failures occur in ambient scribes. The surface text can look correct while the underlying code points to a subtly different concept. A clinician reviewing the free-text note won't notice that the coded entry resolves to "chest discomfort" rather than "chest pain" - but the downstream analytics, safety alerts, and QOF calculations will.

### TP.CC-3 🟡 ICD-10 / ICD-11 Full-Specificity Precision

Precision of ICD coding at maximum digit specificity, reported separately from category-level accuracy. Performance typically degrades sharply at full specificity compared to 3-character category level. The Hybrid-Code v2 framework reported 93% accuracy at 3-character level but only 82% at full specificity - the difference representing systematic specificity errors that aggregate metrics hide.

|Dimension              |Value                                       |
|-----------------------|--------------------------------------------|
| **Reference** | TP.CC-3 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                      |
|**Measurement Cadence**|Periodic audit                              |
|**Pipeline Layer**     |Clinical Coding                             |
|**Assurance Question** |Fidelity & Accuracy                         |
|**Measurement Method** |Computational                               |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit              |
|**Responsible Actors** |Vendor                                      |
|**Maturity**           |Emerging                                    |
|**Outcome Type**       |Proximal                                    |
|**Source**             |Hybrid-Code v2 (arXiv 2512.23743); WHO ICD-11 implementation guidance|

**Why this tier?**

> Vendor pre-deployment. Should be reported at multiple specificity levels (3-char, 4-char, full). Important for secondary care deployment and research data quality.

**Formal Definition**

```
Report precision at each specificity level independently: P_3char, P_4char, P_full. Specificity Degradation = P_3char - P_full. Values > 10 percentage points indicate the system systematically fails at high specificity. For ICD-11, which has more granular specificity than ICD-10, report per specificity depth.
```

**Limitations**

> Full-specificity coding requires clinical judgement that may exceed what is documented in the consultation. Some codes are legitimately unreachable from the source material - the consultation didn't contain enough information. Distinguishing unreachable codes from model errors requires careful reference construction.

**Novel Thinking / Implications**

> 💡 Over-specific coding is a form of clinical hallucination: the system generates specificity that wasn't present in the source. Under-specific coding is information loss. Both are quality issues, and they require different interventions. Reporting only aggregate accuracy conflates them.

### TP.CC-4 🟡 OPCS-4 Procedure Coding Accuracy

Accuracy of OPCS-4 procedure code assignment from consultation documentation. NHS-specific - the OPCS-4 classification (Office of Population Censuses and Surveys, 4th revision) is the mandatory procedure coding standard for NHS secondary care. **No published AI benchmarks currently exist for OPCS-4 coding** despite it being essential for NHS deployment.

|Dimension              |Value                                         |
|-----------------------|----------------------------------------------|
| **Reference** | TP.CC-4 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                        |
|**Measurement Cadence**|Periodic audit                                |
|**Pipeline Layer**     |Clinical Coding                               |
|**Assurance Question** |Fidelity & Accuracy                           |
|**Measurement Method** |Computational                                 |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                |
|**Responsible Actors** |Vendor                                        |
|**Maturity**           |Proposed / Novel                              |
|**Outcome Type**       |Proximal                                      |
|**Source**             |NHS Digital OPCS-4 coding standards; gap identified in published AVT literature|

**Why this tier?**

> Critical for NHS secondary care deployment. Should be a procurement requirement but cannot currently be assessed against published benchmarks - deployers must require vendor evidence on their specific cases.

**Formal Definition**

```
Precision, Recall, F1 at OPCS-4 code level. Specificity breakdown: chapter level (first character), category (first 2 characters), sub-category (3 characters), full code. Report per clinical chapter because procedure complexity varies dramatically (codes in Chapter V - Nervous System - are harder than Chapter W - Bones & Joints).
```

**Limitations**

> No public NHS-representative benchmark dataset for OPCS-4 coding exists. Vendors must construct their own evaluation, which creates comparability problems. Ground truth annotation requires specialist NHS coding expertise.

**Novel Thinking / Implications**

> 💡 The absence of any published OPCS-4 AI benchmark is itself a diagnostic finding about the state of the field. Ambient scribe vendors focused on the US market optimise for ICD-10 and CPT; NHS-specific standards are an afterthought. This is a strong argument for NHS England to commission a national OPCS-4 benchmark dataset as infrastructure investment - without it, NHS secondary care AVT deployment is operating without evidence.

### TP.CC-5 🟡 dm+d Medication Coding Accuracy

Accuracy of Dictionary of Medicines and Devices (dm+d) coding for medications discussed in consultations. NHS-specific - dm+d is the mandatory NHS medication terminology, maintained by NHS BSA, and essential for medication safety, interoperability, and prescribing workflows. **Like OPCS-4, no published AI benchmarks exist for dm+d coding**.

|Dimension              |Value                                                     |
|-----------------------|----------------------------------------------------------|
| **Reference** | TP.CC-5 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                    |
|**Measurement Cadence**|Periodic audit                                            |
|**Pipeline Layer**     |Clinical Coding                                           |
|**Assurance Question** |Safety                                                    |
|**Measurement Method** |Computational                                             |
|**Lifecycle Phases**   |Pre-deployment, Continuous                                |
|**Responsible Actors** |Vendor                                                    |
|**Maturity**           |Proposed / Novel                                          |
|**Outcome Type**       |Proximal                                                  |
|**Source**             |NHS BSA dm+d standard; gap identified in published AVT literature|

**Why this tier?**

> Safety-critical for any AVT writing medication data back to the EPR. Should be a procurement requirement with vendor attestation. Monitoring required as dm+d is updated quarterly - a model trained against an old version will systematically fail on newer medications.

**Formal Definition**

```
Per medication mention: correct mapping to dm+d VMP (Virtual Medicinal Product), AMP (Actual Medicinal Product), VMPP (Virtual Medicinal Product Pack), or AMPP (Actual Medicinal Product Pack) depending on the level required by the EPR write-back. Currency Check: proportion of reference medications that exist in the current dm+d release. Drift = proportion of codes generated that no longer exist in the current dm+d release.
```

**Limitations**

> Mapping from spoken medication name to dm+d concept involves disambiguation (brand vs generic, different strengths, different formulations). Spoken names rarely contain enough specificity to uniquely identify a dm+d code without additional context.

**Novel Thinking / Implications**

> 💡 dm+d is updated quarterly. Any AVT system with a static model is by definition accumulating vocabulary drift against the current standard. A system trained two years ago has approximately eight releases of drift. Currency should be a contractual requirement - vendors should commit to a maximum acceptable drift against the live dm+d.

---

### TP.CC-6 🟢 Code Hallucination Rate

Rate at which the system generates codes that do not exist in the target code set. Distinct from all other coding error metrics because a non-existent code is not a "wrong" code - it is a structural error. The code looks valid syntactically but resolves to nothing. The Hybrid-Code v2 framework explicitly targeted "zero-hallucination coding" because this failure mode is both detectable and unambiguously wrong.

|Dimension              |Value                                                |
|-----------------------|-----------------------------------------------------|
| **Reference** | TP.CC-6 |
|**Priority Tier**      |🟢 Tier 1 - Minimum Viable                            |
|**Measurement Cadence**|Continuous                                           |
|**Pipeline Layer**     |Clinical Coding                                      |
|**Assurance Question** |Safety                                               |
|**Measurement Method** |Computational                                        |
|**Lifecycle Phases**   |Pre-deployment, Continuous                           |
|**Responsible Actors** |Vendor, Deployer                                     |
|**Maturity**           |Emerging                                             |
|**Outcome Type**       |Proximal                                             |
|**Source**             |Hybrid-Code v2 (arXiv 2512.23743) - neuro-symbolic verification approach|

**Why this tier?**

> Architecturally preventable failure mode - there is no reason a production system should generate non-existent codes. Should be a hard zero-tolerance metric validated pre-deployment and monitored continuously. Automated detection is trivial (lookup against the code set).

**Formal Definition**

```
Code Hallucination Rate = |generated_codes_not_in_target_code_set| / |total_generated_codes|. Target: 0.0. Any non-zero value indicates architectural failure - the system should be constrained to generate only valid codes via lookup or constrained decoding. Report per code set (SNOMED, ICD, OPCS-4, dm+d) because constraint enforcement may vary.
```

**Code: Code hallucination check**

```python
def code_hallucination_rate(generated_codes, code_set):
    """
    Returns rate of codes that don't exist in the target code set.
    Should be 0 for any production system.
    """
    valid_codes = set(code_set)
    hallucinated = [c for c in generated_codes if c not in valid_codes]
    rate = len(hallucinated) / len(generated_codes) if generated_codes else 0
    return {
        "rate": rate,
        "hallucinated_codes": hallucinated,
        "alert": rate > 0,
        "severity": "CRITICAL" if rate > 0 else "OK"
    }
```

**Limitations**

> Requires current version of the target code set for lookup. Code set updates may temporarily create false positives (newly valid codes that haven't propagated). Does not detect codes that exist but are clinically wrong - that's captured by SNOMED Code Accuracy.

**Novel Thinking / Implications**

> 💡 This is a zero-tolerance metric. A non-existent code in a clinical record is a data quality failure that breaks downstream systems. The correct architectural response is constrained generation - the system should be structurally unable to produce a code outside the target code set. Any vendor reporting a non-zero hallucination rate is implicitly admitting that their generation is unconstrained, which is a procurement red flag.

### TP.CC-7 🟡 Coding Inflation Detection

Systematic upcoding monitoring via SPC. In NHS, primary risk is data quality corruption of epidemiological data, QOF, and population health.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.CC-7 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
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

### TP.CC-8 🟡 E/M Level Shift Monitoring

Monitoring of shifts in Evaluation & Management (E/M) coding levels pre- and post-AVT deployment. In US settings, E/M level shift has been a primary revenue impact channel; in NHS settings, the equivalent concern is SNOMED specificity shift and its effect on QOF, Hospital Episode Statistics, and population health analytics. Extension of the existing Coding Inflation Detection metric with a specific focus on tariff-relevant code distributions.

|Dimension              |Value                                                                                |
|-----------------------|-------------------------------------------------------------------------------------|
| **Reference** | TP.CC-8 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                                               |
|**Measurement Cadence**|Continuous                                                                           |
|**Pipeline Layer**     |Clinical Coding                                                                      |
|**Assurance Question** |Safety                                                                               |
|**Measurement Method** |Computational                                                                        |
|**Lifecycle Phases**   |Day Zero Baseline, Continuous                                                        |
|**Responsible Actors** |Regional (ICB), National Body                                                        |
|**Maturity**           |Emerging                                                                             |
|**Outcome Type**       |Distal                                                                               |
|**Source**             |npj Digital Medicine policy brief (Nature s41746-025-02272-z) - documented 3.0→4.1 diagnoses/encounter post-AVT|

**Why this tier?**

> Regional (ICB) and national monitoring. Deployers cannot assess population-level shifts from their own data alone. Requires pre/post AVT baseline and cross-practice aggregation.

**Formal Definition**

```
For each coding level or tariff-relevant category: compute pre-AVT baseline distribution and post-AVT distribution. Shift Index = KL divergence or earth-mover's distance between distributions. Flag categories with shift > 0.1 (magnitude calibrated to historical coding drift). Disaggregate by demographic and clinical complexity to identify selective amplification.
```

**Limitations**

> Requires pre-AVT baseline of sufficient duration (minimum 12 months) for seasonal pattern stability. Confounded with independent coding policy changes, QOF updates, and training interventions. Attribution to AVT specifically requires quasi-experimental design.

**Novel Thinking / Implications**

> 💡 The US evidence (14% HCC capture increase, 11% wRVU increase) is alarming because it's unclear whether the shift represents more complete capture (legitimate) or documentation-driven inflation (governance failure). In the NHS context, the same ambiguity applies: are we seeing better coding, or AVT-driven drift that will corrupt epidemiological data? Without monitoring, the distinction is invisible and the data integrity risk is absorbed silently.

### TP.CC-9 🟡 Coding Equity Index

Whether AVT-driven changes in coding distribution are equitably spread across patient demographics or systematically benefit some populations more than others. If AVT improves coding completeness more for majority populations than for minority populations, it widens existing inequalities in data quality and downstream resource allocation.

|Dimension              |Value                                                 |
|-----------------------|------------------------------------------------------|
| **Reference** | TP.CC-9 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                |
|**Measurement Cadence**|Periodic audit                                        |
|**Pipeline Layer**     |Clinical Coding                                       |
|**Assurance Question** |Fairness & Equity                                     |
|**Measurement Method** |Computational                                         |
|**Lifecycle Phases**   |Periodic Audit                                        |
|**Responsible Actors** |Regional (ICB), National Body                         |
|**Maturity**           |Proposed / Novel                                      |
|**Outcome Type**       |Distal                                                |
|**Source**             |Extension of existing Deployment Equity Index to coding dimension|

**Why this tier?**

> Regional or national responsibility. Requires demographic-linked coding data aggregated across practices. Important equity dimension currently invisible in AVT evaluation.

**Formal Definition**

```
For each coding category: compute the pre/post AVT change ratio per demographic group. Equity Ratio = max(change_ratio across groups) / min(change_ratio across groups). Values > 1.5 indicate disparate impact. Specifically monitor: condition coding completeness, severity coding, and comorbidity capture by ethnicity, age, deprivation, and EAL status.
```

**Limitations**

> Demographic-linked coding analysis requires data aggregation that may raise information governance concerns. Small group sizes at practice level require regional aggregation. Attribution to AVT specifically needs controls for confounders.

**Novel Thinking / Implications**

> 💡 If AVT makes the documented patient population look healthier for some demographics and more accurately unwell for others, the resource allocation implications compound existing health inequalities. This is an equity dimension that the existing taxonomy's fairness metrics don't capture - they focus on AVT accuracy across demographics, not on AVT's effect on the resulting data about those demographics.

### TP.CC-10 🔵 wRVU / Tariff Impact Attribution

Attribution of workload or tariff-relevant coding changes to AVT specifically, separated from concurrent changes (training, policy updates, case mix shifts). Quasi-experimental methodology required. In NHS context, applies to PbR tariffs, QOF achievement, and secondary care activity-based funding.

|Dimension              |Value                                        |
|-----------------------|---------------------------------------------|
| **Reference** | TP.CC-10 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research               |
|**Measurement Cadence**|Periodic audit                               |
|**Pipeline Layer**     |Clinical Coding                              |
|**Assurance Question** |Meta-evaluation                              |
|**Measurement Method** |Hybrid                                       |
|**Lifecycle Phases**   |Periodic Audit                               |
|**Responsible Actors** |Regional (ICB), National Body, Academic     |
|**Maturity**           |Proposed / Novel                             |
|**Outcome Type**       |Distal                                       |
|**Source**             |Extends E/M Level Shift Monitoring with causal attribution methodology|

**Why this tier?**

> Research-grade metric requiring quasi-experimental design. National or academic responsibility. Not routinely measurable at deployer level.

**Formal Definition**

```
Using difference-in-differences or synthetic control methodology: compare coding/tariff trajectories of AVT-adopting practices against matched non-adopting practices over the same period. Attribution Coefficient = (ΔAVT - ΔControl) / ΔControl. Positive values indicate AVT-driven shift; magnitude indicates size of effect. Confidence intervals essential given small sample sizes in practice-level comparisons.
```

**Limitations**

> Practice selection into AVT is not random - early adopters may differ systematically from non-adopters. Matching methodology is contested. Small sample sizes at practice level undermine statistical power.

**Novel Thinking / Implications**

> 💡 This is the metric that answers the governance question: is AVT making the coded data more accurate or more inflated? Without this attribution, every observed coding shift is ambiguous. National evaluation programmes are the only plausible venue for doing this properly - individual deployers cannot.

### TP.CC-11 🔵 Code Specificity Index

Whether suggested codes are at appropriate hierarchy level. SNOMED has multiple specificity levels for the same concept; AI may default to over-general (loses detail) or over-specific (introduces false precision) codes inappropriately.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.CC-11 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
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

> 💡 Over-specific coding is the more insidious problem: AI may code 'chest pain' as 'precordial chest pain' when the patient simply said 'pain in my chest'. The over-specific code carries information that wasn't in the source - a form of coded hallucination. Under-specific coding loses information but is more obviously a quality issue.

---

### TP.CC-12 🔵 Code Suggestion Latency

Time from note generation to code suggestion availability. Affects coding workflow integration - if coding suggestions arrive too late, clinicians have moved on to the next patient and won't engage with them.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.CC-12 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
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
