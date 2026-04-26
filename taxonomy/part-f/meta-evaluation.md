### ES.ME-1 🔵 Proximal vs Distal Outcome Distinction

The most important structural critique: measuring easy things and assuming they correlate with hard things. Require causal logic models.

| Dimension | Value |
|-----------|-------|
| **Reference** | ES.ME-1 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | National Body, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
| **Source** | Coiera & Fraile-Navarro 2026; NIHR RSET |

**Why this tier?**

> Structural critique of the evaluation field. Not a metric to implement but a framework for assessing all other metrics. National/academic responsibility.

**Formal Definition**

```
Proximal P = {WER, edit_rate, doc_time}. Distal D = {safety events, care quality, patient outcomes}. For each pᵢ, require causal model: pᵢ → [mechanism] → dⱼ with evidence. Burden on vendors/deployers to demonstrate P→D.
```

**References**

- **Editorial**: Coiera & Fraile-Navarro (2026) - JMIR Med Inform
- **RSET**: NIHR RSET Phase 1

**Limitations**

> Distal outcomes slow to manifest, hard to attribute.

**Novel Thinking / Implications**

> 💡 National evaluation standard should require explicit causal logic models with burden of proof on vendors. ES.ME-1 names that burden; [ES.ME-9 Causal Model Operationalisation](#es-me-9) makes it a measurable procurement requirement, and [ES.ME-8 Outcome Evidence Commitment Status](#es-me-8) measures whether the distal evidence is being generated. See also [Outcomes Boundary](#outcomes-boundary) for the explicit scope statement.

---

### ES.ME-2 🔵 Inter-Rater Reliability Baseline

Clinician agreement ceiling. VeriFact exceeds it (92.7% vs 88.5%). When automated metrics beat humans, what does that mean?

| Dimension | Value |
|-----------|-------|
| **Reference** | ES.ME-2 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Academic |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
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

### ES.ME-3 🔵 Metric Interaction Analysis

Do the metrics in the taxonomy correlate or conflict? A system optimised for low edit rate might achieve it through over-summarisation that increases omission rate. Multi-metric monitoring requires understanding interactions.

| Dimension | Value |
|-----------|-------|
| **Reference** | ES.ME-3 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | National Body, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
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

> 💡 Without interaction analysis, governance can drive perverse outcomes. A practice told to reduce edit rate might pressure clinicians to edit less - but the AI hasn't improved, so the underlying error rate is unchanged. Edit rate goes down, hallucination rate goes up. This is the kind of failure that interaction analysis catches.

---

### ES.ME-4 🟡 Goodhart's Law Monitoring

When a metric becomes a target, does it cease to be a good measure? Specifically tracking whether metrics are being gamed - optimised in ways that satisfy the metric without achieving the underlying goal.

| Dimension | Value |
|-----------|-------|
| **Reference** | ES.ME-4 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Regional (ICB) |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
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

### ES.ME-5 🔵 Coverage Gap Analysis

What failure modes are not captured by any metric in the taxonomy? Periodic review of incidents to identify metric blindspots. The taxonomy itself must evolve as new failure modes emerge.

| Dimension | Value |
|-----------|-------|
| **Reference** | ES.ME-5 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | National Body, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
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

> 💡 The taxonomy is not static. As AVT evolves and new failure modes emerge, the taxonomy must evolve to cover them. Coverage gap analysis is the mechanism for this evolution - every incident should prompt the question 'would our metrics have caught this?' If not, that's a gap to fill.

---

### ES.ME-6 🔵 LLM-Judge Bias Quantification

Systematic measurement of known biases in LLM-as-a-Judge evaluation: position bias (prefers first response in pairwise comparison), verbosity bias (prefers longer responses), self-enhancement bias (prefers outputs from the same model family), and fine-grained scoring unreliability (inconsistent discrimination at high score ranges). Required for interpreting LLM-Judge metrics responsibly. The Croxford et al. 2025 study found GPT-o3-mini achieving ICC 0.818 with human evaluators on PDSQI-9 - but a separate Rwanda clinical LLM evaluation study found LLM judges correlated more strongly with non-expert than expert annotators, indicating that apparent reliability may reflect alignment with a particular class of evaluator rather than with ground truth.

| Dimension | Value |
|-----------|-------|
| **Reference** | ES.ME-6 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Academic, National Body |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | Croxford et al. 2025 (npj Digital Medicine); Rwanda clinical LLM evaluation study |

**Why this tier?**

> Research-grade meta-evaluation. Academic and national body responsibility. Not routinely performed but necessary for anyone relying on LLM-as-a-Judge outputs for safety-critical decisions.

**Formal Definition**

```
Bias tests: (1) Position bias - reverse pairwise ordering and measure agreement with original judgment (perfect judge = 100% consistency under reversal); (2) Verbosity bias - compare judgments on pairs matched on quality but varying in length; (3) Self-enhancement - test judge on outputs from its own model family vs other families; (4) Score range reliability - measure inter-rater agreement at high scores (e.g. 4 vs 5 on Likert) vs across full range. Composite: bias-adjusted reliability = raw reliability corrected for each bias type.
```

**Limitations**

> Bias testing requires carefully constructed adversarial test sets. Results don't transfer across judge models or domains. Bias adjustments are approximations, not corrections.

**Novel Thinking / Implications**

> 💡 The Rwanda finding is the uncomfortable one: LLM judges may correlate well with human evaluators while correlating poorly with ground truth. This is the worst failure mode for evaluation - apparent reliability that validates a biased assessment. Any deployment relying on LLM-as-a-Judge for safety decisions (not just for efficiency) needs to have run bias quantification and documented the residual uncertainty. Otherwise the high ICC number is theatrical rather than informative.

---

### ES.ME-7 🔵 Automated-Human Metric Concordance

Systematic measurement of how well automated metrics correlate with expert human evaluation across deployments. Meta-metric that validates (or invalidates) the automated metrics themselves. Without concordance measurement, automated metrics are running on the assumption that they track what human experts would measure - but the ROUGE Kendall-Tau finding of 0.080 with human clinical judgment (Croxford et al. 2025) shows that assumption can be wildly wrong.

| Dimension | Value |
|-----------|-------|
| **Reference** | ES.ME-7 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | National Body, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
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

> 💡 This is the metric that polices the other metrics. Without concordance data, the taxonomy's automated metrics are running on an unverified assumption that they measure what human experts measure. The ROUGE finding is the canonical example of that assumption failing - a metric in widespread use has essentially zero correlation with clinical judgment and is used anyway because it's easy to compute. Periodic concordance measurement should be a national evaluation programme responsibility, and any metric with concordance < 0.3 should be explicitly flagged in the taxonomy as inadequate as a standalone indicator.

---

### ES.ME-8 🟡 Outcome Evidence Commitment Status

Whether the vendor and deployer have committed - contractually, via published protocol, or via post-market surveillance plan - to evaluating the actual clinical outcomes of AVT deployment. Operationalises the boundary set by [Outcomes Boundary](#outcomes-boundary): this taxonomy does not measure clinical outcomes, but it can measure whether outcome evaluation is in train.

| Dimension | Value |
|-----------|-------|
| **Reference** | ES.ME-8 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate; reviewed annually |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Documentary |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer, National Body |
| **Maturity** | Emerging |
| **Outcome Type** | Process |
| **Applicability** | General Healthcare AI |
| **Source** | This taxonomy v3.3; T.E.S.T. Section B Clinical Effectiveness (50 pts RCT validation); MHRA Post-Market Surveillance Regulations 2024 |

**Why this tier?**

> A deployment cannot satisfy T.E.S.T. Gold without RCT or sufficiently powered NHS pilot evidence. Procurement above pilot scale should require demonstrable commitment to outcome evaluation even where the evidence is not yet available. Tier 2 because it is documentary - no instrumentation - and because pilots and small-site deployments may legitimately not yet have outcome studies in train.

**Formal Definition**

```
Composite of four binary checks against documentary evidence:
  C1 = clinical-trial protocol registered (ISRCTN, ClinicalTrials.gov, or equivalent)
       OR equivalent NHS pilot study protocol with pre-registered primary outcome
  C2 = post-market surveillance plan exists and names patient-outcome signals
       (incident rate, diagnostic accuracy, medication errors, etc.)
       distinct from technical-performance signals
  C3 = data-collection infrastructure exists at deployment site sufficient to detect
       change in named outcome signals (baseline data; case ascertainment method;
       comparator arm or pre/post design)
  C4 = vendor contractually committed to share post-market outcome data with
       deployer and (where applicable) with national bodies
Score = number of checks passed (0-4). Tier 2 expectation: ≥ 2 of 4 at procurement;
≥ 3 of 4 within 12 months of deployment.
```

**Limitations**

> Documentary; does not verify the *quality* of the protocol or the *power* of the study. A registered trial may be underpowered, badly designed, or never report results. C2 and C3 are vendor-asserted unless deployer audits them. Treats commitment as a proxy for eventual evidence; that proxy can fail (the [Roadmap as Graveyard](#outcomes-boundary) risk - protocols register but evidence never lands). Pair with periodic re-check of whether registered studies are progressing.

**Novel Thinking / Implications**

> 💡 The honest answer to "does this AVT improve patient outcomes?" is almost always "we don't know yet" - because the field has not produced the evidence and most deployments are not generating it. ES.ME-8 forces that uncertainty into the open at procurement. A vendor scoring 0/4 is selling on technical-performance evidence alone; a vendor scoring 4/4 has committed to producing the evidence the field is missing. Either is acceptable as long as the deployer chooses with eyes open. The metric does not establish clinical benefit - it establishes whether anyone is trying to.

---

### ES.ME-9 🟡 Causal Model Operationalisation

Whether the vendor has documented an explicit causal chain from the proximal metrics in this taxonomy (or its own equivalents) to the distal outcomes claimed at procurement. Makes [ES.ME-1 Proximal vs Distal Outcome Distinction](#es-me-1)'s "burden of proof" requirement operational.

| Dimension | Value |
|-----------|-------|
| **Reference** | ES.ME-9 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate; updated when outcome claims change |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Documentary |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Process |
| **Applicability** | General Healthcare AI |
| **Source** | This taxonomy v3.3; ES.ME-1 (proximal/distal causal-logic framework); Coiera & Fraile-Navarro 2026 (structural critique) |

**Why this tier?**

> Vendors making outcome claims at procurement (faster documentation, fewer errors, improved patient experience) should be required to specify the causal chain by which their proximal performance translates to those outcomes. Without that chain, the procurement claim is unfalsifiable. Tier 2 because it is documentary and one-off; the burden is on the vendor making the claim, not on continuous measurement.

**Formal Definition**

```
For each outcome claim O made at procurement (e.g. "reduces documentation time",
"reduces medication errors", "improves patient experience"):
  S1 = vendor names the proximal metrics P_1..P_n that, if measured, would constitute
       evidence for or against O (where P_i are drawn from this taxonomy or named
       vendor-specific equivalents with comparable definitions)
  S2 = vendor specifies the mechanism linking each P_i to O (the causal step from
       proximal performance to distal outcome - e.g. "lower hallucination rate
       reduces clinician verification burden which reduces after-hours review which
       reduces documentation time outside consultations")
  S3 = vendor cites or commits to producing evidence for each linking mechanism
       (literature, internal study, external trial)
  S4 = vendor identifies known confounders and threats to the causal claim
       (Hawthorne effects, selection bias, secular trends, concurrent interventions)
Score per claim = number of stages documented (0-4). Composite for the deployment =
mean score across all outcome claims. Tier 2 expectation: ≥ 3 of 4 on every claim
made at procurement.
```

**Limitations**

> Documentary; does not verify that the cited mechanisms are plausible or supported. Vendors can produce a causal model that *looks* coherent but is empirically wrong (the ROUGE precedent: a metric in widespread use with Kendall-Tau 0.080 against clinical judgment). The metric forces the model into the open; deployer review still required. Becomes meaningful only when paired with [ES.ME-7 Automated-Human Metric Concordance](#es-me-7) for the proximal links and [ES.ME-8 Outcome Evidence Commitment Status](#es-me-8) for the distal evidence.

**Novel Thinking / Implications**

> 💡 This metric exposes a common procurement failure mode: vendors making outcome claims ("reduces clinician burnout", "improves patient outcomes") backed by proximal evidence ("our hallucination rate is 1.5%") with no documented causal chain connecting the two. The chain may be sound, weak, or nonexistent - but without it being written down, the deployer cannot evaluate the claim. Forcing the chain into the procurement documentation does not validate it; it makes validation possible. Deployers who require this metric can compare causal models across vendors and identify which are operating on evidence and which on assumption.

---
