# Part F — Evaluation Science

## Meta-evaluation

*Are we measuring what matters? Structural critique of proximal vs distal outcomes and evaluation science itself.*

**Tier breakdown**: 🟡 1 Tier 2 · 🔵 6 Tier 3

### 🔵 Proximal vs Distal Outcome Distinction

The most important structural critique: measuring easy things and assuming they correlate with hard things. Require causal logic models.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | National Body, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Source** | Coiera & Fraile-Navarro 2026; NIHR RSET |

**Why this tier?**

> Structural critique of the evaluation field. Not a metric to implement but a framework for assessing all other metrics. National/academic responsibility.

**Formal Definition**

```
Proximal P = {WER, edit_rate, doc_time}. Distal D = {safety events, care quality, patient outcomes}. For each pᵢ, require causal model: pᵢ → [mechanism] → dⱼ with evidence. Burden on vendors/deployers to demonstrate P→D.
```

**References**

- **Editorial**: Coiera & Fraile-Navarro (2026) — JMIR Med Inform
- **RSET**: NIHR RSET Phase 1

**Limitations**

> Distal outcomes slow to manifest, hard to attribute.

**Novel Thinking / Implications**

> 💡 National evaluation standard should require explicit causal logic models with burden of proof on vendors.

---

### 🔵 Inter-Rater Reliability Baseline

Clinician agreement ceiling. VeriFact exceeds it (92.7% vs 88.5%). When automated metrics beat humans, what does that mean?

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Academic |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | VeriFact; MedHELM |

**Why this tier?**

> Research calibration baseline. Essential for interpreting automated metrics but an academic activity, not a deployer responsibility.

**Formal Definition**

```
Cohen's κ (k=2) or Fleiss' κ (k>2). ICC(2,1) for continuous ratings. VeriFact: 92.7% vs 88.5% inter-clinician. MedHELM: ICC 0.47 vs 0.43.
```

**References**

- **VeriFact**: [Chung et al. (2025)](https://ai.nejm.org/doi/full/10.1056/AIdbp2500418)
- **MedHELM**: [Bedi et al. (2025)](https://arxiv.org/abs/2505.23802)

**Limitations**

> Clinicians don't agree with each other. Any metric inherits this ceiling.

**Novel Thinking / Implications**

> 💡 When automated metric exceeds inter-clinician agreement: better than humans, or systematically biased in a correlated way?

---

### 🔵 Metric Interaction Analysis

Do the metrics in the taxonomy correlate or conflict? A system optimised for low edit rate might achieve it through over-summarisation that increases omission rate. Multi-metric monitoring requires understanding interactions.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | National Body, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Multi-metric evaluation literature |

**Why this tier?**

> Research-grade meta-analysis. National body responsibility.

**Formal Definition**

```
For each pair of metrics (m1, m2): compute correlation across deployments. Identify: (1) reinforcing pairs (improving both); (2) trade-off pairs (optimising one degrades the other); (3) confounded pairs (apparent correlation but distinct causes).
```

**Limitations**

> Requires data across multiple deployments to identify systematic interactions. Single-deployer analysis is underpowered.

**Novel Thinking / Implications**

> 💡 Without interaction analysis, governance can drive perverse outcomes. A practice told to reduce edit rate might pressure clinicians to edit less — but the AI hasn't improved, so the underlying error rate is unchanged. Edit rate goes down, hallucination rate goes up. This is the kind of failure that interaction analysis catches.

---

### 🟡 Goodhart's Law Monitoring

When a metric becomes a target, does it cease to be a good measure? Specifically tracking whether metrics are being gamed — optimised in ways that satisfy the metric without achieving the underlying goal.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Regional (ICB) |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Goodhart's Law applied to clinical AI metrics |

**Why this tier?**

> Important meta-governance check. Should be part of periodic audit to ensure metrics remain meaningful.

**Formal Definition**

```
For each Tier 1 metric: identify gaming strategies that could satisfy the metric without improving safety. Audit for evidence of gaming. Examples: edit rate gaming via no-op edits; review-before-signing gaming via auto-scroll; opt-out gaming via not informing patients.
```

**Limitations**

> Gaming detection is itself a research problem. Sophisticated gaming may be undetectable.

**Novel Thinking / Implications**

> 💡 Every metric in this taxonomy is potentially gameable. Edit rate can be gamed by trivial edits. Review-before-signing can be gamed by auto-scrolling. The question isn't whether gaming will happen but whether the governance framework detects and addresses it. Periodic audit should specifically look for gaming patterns, not just metric values.

---

### 🔵 Coverage Gap Analysis

What failure modes are not captured by any metric in the taxonomy? Periodic review of incidents to identify metric blindspots. The taxonomy itself must evolve as new failure modes emerge.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | National Body, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Standard safety engineering coverage analysis |

**Why this tier?**

> Meta-governance responsibility. National body should maintain the taxonomy as new failure modes emerge.

**Formal Definition**

```
For each incident or near-miss: identify which metrics would have detected it. Coverage Gap = |incidents_undetected_by_taxonomy| / |total_incidents|. Drives taxonomy evolution: gaps indicate new metrics needed.
```

**Limitations**

> Requires structured incident analysis and taxonomy maintenance process.

**Novel Thinking / Implications**

> 💡 The taxonomy is not static. As AVT evolves and new failure modes emerge, the taxonomy must evolve to cover them. Coverage gap analysis is the mechanism for this evolution — every incident should prompt the question 'would our metrics have caught this?' If not, that's a gap to fill.

---

### 🔵 LLM-Judge Bias Quantification

Systematic measurement of known biases in LLM-as-a-Judge evaluation: position bias (prefers first response in pairwise comparison), verbosity bias (prefers longer responses), self-enhancement bias (prefers outputs from the same model family), and fine-grained scoring unreliability (inconsistent discrimination at high score ranges). Required for interpreting LLM-Judge metrics responsibly. The Croxford et al. 2025 study found GPT-o3-mini achieving ICC 0.818 with human evaluators on PDSQI-9 — but a separate Rwanda clinical LLM evaluation study found LLM judges correlated more strongly with non-expert than expert annotators, indicating that apparent reliability may reflect alignment with a particular class of evaluator rather than with ground truth.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Academic, National Body |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Croxford et al. 2025 (npj Digital Medicine); Rwanda clinical LLM evaluation study |

**Why this tier?**

> Research-grade meta-evaluation. Academic and national body responsibility. Not routinely performed but necessary for anyone relying on LLM-as-a-Judge outputs for safety-critical decisions.

**Formal Definition**

```
Bias tests: (1) Position bias — reverse pairwise ordering and measure agreement with original judgment (perfect judge = 100% consistency under reversal); (2) Verbosity bias — compare judgments on pairs matched on quality but varying in length; (3) Self-enhancement — test judge on outputs from its own model family vs other families; (4) Score range reliability — measure inter-rater agreement at high scores (e.g. 4 vs 5 on Likert) vs across full range. Composite: bias-adjusted reliability = raw reliability corrected for each bias type.
```

**Limitations**

> Bias testing requires carefully constructed adversarial test sets. Results don't transfer across judge models or domains. Bias adjustments are approximations, not corrections.

**Novel Thinking / Implications**

> 💡 The Rwanda finding is the uncomfortable one: LLM judges may correlate well with human evaluators while correlating poorly with ground truth. This is the worst failure mode for evaluation — apparent reliability that validates a biased assessment. Any deployment relying on LLM-as-a-Judge for safety decisions (not just for efficiency) needs to have run bias quantification and documented the residual uncertainty. Otherwise the high ICC number is theatrical rather than informative.

---

### 🔵 Automated-Human Metric Concordance

Systematic measurement of how well automated metrics correlate with expert human evaluation across deployments. Meta-metric that validates (or invalidates) the automated metrics themselves. Without concordance measurement, automated metrics are running on the assumption that they track what human experts would measure — but the ROUGE Kendall-Tau finding of 0.080 with human clinical judgment (Croxford et al. 2025) shows that assumption can be wildly wrong.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | National Body, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Source** | Standard meta-evaluation methodology; Croxford et al. 2025 (ROUGE Kendall-Tau 0.080) |

**Why this tier?**

> Meta-evaluation requiring paired automated and human assessment data. National evaluation programme responsibility. Establishes the evidence base for treating automated metrics as trustworthy proxies.

**Formal Definition**

```
For each automated metric m in deployed use: collect a sample of N encounters scored by both m and by expert human evaluators using a validated instrument (e.g. PDSQI-9, CREOLA taxonomy). Compute correlation (Pearson, Spearman, Kendall's tau). Concordance Threshold: metric is "adequate as proxy" only if correlation > 0.5. Metrics with correlation < 0.3 should not be used as standalone quality indicators regardless of technical sophistication. Report concordance per metric with confidence intervals.
```

**Limitations**

> Requires paired human-automated scoring, which is expensive. Inter-human agreement is itself imperfect, creating a ceiling on achievable concordance. Results may not transfer across deployment contexts (a metric that concords well in primary care may fail in secondary care).

**Novel Thinking / Implications**

> 💡 This is the metric that polices the other metrics. Without concordance data, the taxonomy's automated metrics are running on an unverified assumption that they measure what human experts measure. The ROUGE finding is the canonical example of that assumption failing — a metric in widespread use has essentially zero correlation with clinical judgment and is used anyway because it's easy to compute. Periodic concordance measurement should be a national evaluation programme responsibility, and any metric with concordance < 0.3 should be explicitly flagged in the taxonomy as inadequate as a standalone indicator.

---
