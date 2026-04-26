## Outcomes Boundary

This section is an explicit scope statement: what this taxonomy assures, what it does not, and where the responsibility for the rest lies. The intent is to prevent a common failure mode in clinical AI governance — passing every metric in a deployment-assurance framework and reading that as evidence of clinical benefit, when the framework was never designed to measure benefit at all.

### What this taxonomy assures

The 215 metrics measure the conditions under which an AVT system can be deployed safely and operated responsibly:

- **Technical fidelity** — does the system transcribe, diarise, summarise, and write back accurately enough for the intended clinical use? (Parts A and B)
- **Documentation quality** — do generated notes preserve clinical content, negation, uncertainty, and structure? (Part A — Summarisation / NLP)
- **Clinician oversight** — do clinicians review, edit, and sign in ways that catch system errors? (Part C — Human Factors)
- **Equitable performance** — does the system work across demographic groups, accents, disabilities, and clinical settings? (Part D — Fairness & Equity)
- **Hazard identification and incident response** — are safety events detected, investigated, and learned from? (Part E — Safety & Governance)
- **Compliance and governance** — privacy, consent, data protection, regulatory classification, vendor transparency, training, business continuity. (Part E)
- **Measurement quality** — is the evaluation methodology itself sound? (Part F — Meta-evaluation)

These are **process, structure, and proximal-outcome measures**. They tell a deployer whether the system is *operating as specified* and whether the conditions for safe use are in place.

### What this taxonomy does not assure

**Clinical outcome validation is out of scope.** This taxonomy does not contain, and is not designed to contain, metrics that establish:

- Whether AVT use changes diagnostic accuracy in real practice
- Whether AVT use changes the rate or severity of patient safety incidents
- Whether AVT use changes downstream care quality, patient outcomes, or population health
- Whether AVT use changes clinician decision-making in ways that benefit (or harm) patients
- Whether AVT delivers the cost-effectiveness claimed at procurement

These are **distal-outcome questions**. They require infrastructure that no individual deployer can provide alone: multi-site randomised trial designs, longitudinal follow-up, case-mix controls, baseline incident data of sufficient power to detect change, and independence from the vendor whose product is being evaluated.

### Why the boundary

Three reasons this is drawn explicitly rather than left implicit:

1. **The field has not solved outcome measurement for clinical AI generally, and AVT specifically.** Coiera & Fraile-Navarro (2026) name this as a structural gap. Adding outcome metrics to a deployment taxonomy does not produce outcome evidence; it produces the appearance of coverage. That risks substituting framework completeness for empirical evidence.

2. **Outcome validation belongs to bodies with the right authority and reach.** National research bodies (e.g. NIHR RSET), regulators with post-market surveillance powers (MHRA), evidence-standards frameworks (NICE ESF Tier C clinical-management evidence), and vendors pursuing formal regulatory claims are the appropriate actors. This taxonomy can require deployers to ensure those processes are in train; it cannot substitute for them.

3. **Process compliance is not clinical benefit.** A deployment passing all 43 Tier 1 metrics in this taxonomy is *assured of deployment safety* — that the system is configured, monitored, governed, and overseen correctly. It is not assured of *clinical benefit*. The taxonomy makes that distinction visible so deployers, vendors, and procurement leads do not conflate the two.

### What deployers should do instead

For the questions this taxonomy does not answer, deployers should:

- **Require post-market outcome studies** in vendor contracts. The two new meta-metrics in this v3.3 release operationalise this requirement: [ES.ME-8 Outcome Evidence Commitment Status](#es-me-8) measures whether a vendor has committed (protocol, registration, post-market surveillance plan) to outcome evaluation; [ES.ME-9 Causal Model Operationalisation](#es-me-9) measures whether the vendor has specified how the proximal metrics in this taxonomy connect to claimed distal outcomes.
- **Require T.E.S.T. Section B RCT evidence** where Gold certification (national-scale deployment) is sought. T.E.S.T. awards 50 of 420 points for clinical validation through RCTs or sufficiently powered NHS pilot studies; this taxonomy treats that evidence as input to procurement, not output of measurement.
- **Treat proximal metrics as deployment-safety signals, not as evidence of clinical benefit.** Hallucination rate is a safety-floor signal; edit rate is a workflow-and-attention signal; cumulative information yield is a fidelity signal. None of these establish that the deployed system improves care.
- **Consult [ES.ME-1 Proximal vs Distal Outcome Distinction](#es-me-1)** for the causal-logic framework that names what proximal-to-distal evidence vendors must supply, and what this taxonomy's metrics do and do not establish.

### Relationship to the Calibration & Context principle

The Outcomes Boundary and the [Calibration & Context principle](#calibration-context) are deliberately complementary commitments with very different grain:

- **The Outcomes Boundary is a hard limit.** Clinical-outcome validation (RCT-grade evidence that AVT changes diagnostic accuracy, patient safety incidents, or downstream care quality) is *out of scope* for this taxonomy regardless of deployment context. Calibration cannot bring distal-outcome validation into the deployer's scope; that boundary stays with national research bodies, MHRA post-market surveillance, NICE Tier C clinical-management evidence, and vendor regulatory claims. A deployer cannot localise their way around it.
- **The Calibration & Context principle is a soft instruction.** Tier assignments and threshold numbers are *in scope* but *deployer-calibrated*. The published defaults reflect a generic deployment context; six named axes (specialty mix, patient population, platform maturity, governance capacity, risk appetite, volume / scale) shift them in real settings. Local calibration is expected, documented, and reviewable — but it operates *within* the in-scope set of metrics, never to import work that the Boundary marks as out-of-scope.

A reader finishing the Calibration principle alone might infer that thresholds are endlessly flexible; a reader finishing the Outcomes Boundary alone might infer that Tier 1 is a hard pass/fail. Read together, the right interpretation is: the structural commitments (what's measured, what's out of scope) are firm; the parameter values (which tier, what threshold) are local. Deployers using this taxonomy should read both — the Boundary to understand what it cannot rely on the taxonomy to deliver, and the Calibration principle to understand the scope it does have to adapt the published defaults to its own context.

### Cross-references

- **ES.ME-1 Proximal vs Distal Outcome Distinction** — names the causal-logic burden on vendors
- **ES.ME-8 Outcome Evidence Commitment Status** — operationalises outcome-study commitment as a metric
- **ES.ME-9 Causal Model Operationalisation** — operationalises the proximal-to-distal causal chain as a metric
- **[Calibration & Context principle](#calibration-context)** — parallel principle for in-scope-but-context-dependent calibration
- **NHS T.E.S.T. Framework Section B** — Clinical Effectiveness benefit domain (90 pts of 420), with 50 pts gated on RCT evidence; see [Standards Mapping § NHS T.E.S.T.](#nhs-test-framework-technology-evaluation-safety-test)
- **MHRA Software and AI as a Medical Device** — Post-Market Surveillance (WP4 + SI 2024 No. 1368) effectiveness-evidence requirements

### Future direction

This boundary may need revisiting if (a) NHS England, NIHR, or an equivalent body publishes a national outcome-evaluation framework for AVT that this taxonomy can map to; (b) the field converges on a defensible set of distal outcome metrics with validated measurement protocols; or (c) the proximal metrics in this taxonomy are themselves shown by clinical evidence to be inadequate proxies for the outcomes that matter. Until then, the boundary stays explicit.

---
