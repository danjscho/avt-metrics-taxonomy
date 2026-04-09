# AVT Metrics Taxonomy — New Metric Entries (Batch 2)

Batch 2 covers the remainder of Part B and all of Parts C and D.

**Contents**
- End-to-End Pipeline — 1 new metric
- Human Factors & Workflow → new **Sociotechnical & Resilience** sub-cluster — 4 new metrics
- Patient Experience → new **Patient Clinical Outcomes** sub-cluster — 4 new metrics
- Fairness & Equity — 3 new metrics

**Total this batch: 12 entries**

---

# Part B — Pipeline Interactions additions

## End-to-End Pipeline (+1)

### 🔵 Cumulative Information Yield

The positive framing of source-to-record concordance: what proportion of the clinical information present in the source audio successfully survives the entire pipeline and appears in the final EPR record. Where Source-to-Record Concordance measures preservation rate (how much was preserved), Cumulative Information Yield measures the distributional yield across clinical categories — so it exposes systematic category bias (e.g. a system that yields 95% on medications but 60% on psychosocial content).

|Dimension              |Value                                                                            |
|-----------------------|---------------------------------------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                                                   |
|**Measurement Cadence**|Periodic audit                                                                   |
|**Pipeline Layer**     |End-to-End                                                                       |
|**Assurance Question** |Safety                                                                           |
|**Measurement Method** |Hybrid                                                                           |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                                   |
|**Responsible Actors** |Academic, National Body                                                          |
|**Maturity**           |Proposed / Novel                                                                 |
|**Outcome Type**       |Distal                                                                           |
|**Source**             |Extension of existing Source-to-Record Concordance with categorical yield decomposition|

**Why this tier?**

> Resource-intensive evaluation requiring expert annotation of source audio, organised into categorical yield rather than binary preservation. Best suited for national evaluation programme. Per-category reporting reveals systematic content bias invisible to aggregate preservation metrics.

**Formal Definition**

```
For each clinical category c ∈ C = {medications, allergies, diagnoses, symptoms, plan, safety_netting, social_context, psychosocial, red_flags}: Yield(c) = |items_in_c_present_in_record| / |items_in_c_in_source|. Composite: Yield_weighted = Σ w_c × Yield(c), where w_c are clinical importance weights. Report per-category breakdown alongside composite — the aggregate obscures category bias.
```

**Limitations**

> Categorical annotation of source audio is even more labour-intensive than binary annotation. Category boundaries are contested (is "stopped smoking 5 years ago" social context or relevant history?). Weight assignment for the composite is subjective.

**Novel Thinking / Implications**

> 💡 The most common finding in ambient scribe evaluation is systematic yield bias toward clinical content the model recognises as "medical" (medications, symptoms, diagnoses) and away from content it treats as peripheral (social context, psychosocial factors, patient concerns that don't map to a code). This bias is invisible to concordance metrics that treat all clinical items equally — but it has direct consequences for patient-centred care and safeguarding. Per-category yield reporting makes the bias visible and actionable.

-----

# Part C — Human Layer additions

## Human Factors & Workflow — new Sociotechnical & Resilience sub-cluster (+4)

*Systems-level constructs drawn from FRAM, Safety-II, and resilience engineering. These metrics assess the clinician-AVT joint cognitive system rather than AVT alone, and capture dimensions that standard human factors metrics miss — the gap between intended and actual practice, the hidden cost of verification, and the capacity to handle unexpected situations.*

### 🔵 Work-as-Imagined vs Work-as-Done Gap

The gap between how AVT is intended to be used (per procedures, training, and governance documentation) and how it is actually used in clinical practice. A construct from Hollnagel's FRAM methodology and the Safety-II tradition. Subsumes and generalises the existing Off-Label Use Detection metric — not every WAI/WAD gap is off-label, and not every adaptation is a safety problem, but the gap itself is diagnostically valuable.

|Dimension              |Value                                                                  |
|-----------------------|-----------------------------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                                         |
|**Measurement Cadence**|Periodic audit                                                         |
|**Pipeline Layer**     |Cross-cutting                                                          |
|**Assurance Question** |Safety                                                                 |
|**Measurement Method** |Hybrid                                                                 |
|**Lifecycle Phases**   |Periodic Audit                                                         |
|**Responsible Actors** |Deployer, Academic                                                     |
|**Maturity**           |Proposed / Novel                                                       |
|**Outcome Type**       |Distal                                                                 |
|**Source**             |Hollnagel FRAM methodology; JMIR 2026 SEIPS-based AVT evaluations      |

**Why this tier?**

> Research-grade metric requiring ethnographic observation and structured interview methodology. Not routinely measurable at deployer level. Academic or national evaluation programme responsibility.

**Formal Definition**

```
Three-step methodology: (1) Document WAI from training materials, SOPs, vendor guidance, and governance policies; (2) Observe WAD through shadowing, workflow analysis, and semi-structured clinician interviews; (3) Gap analysis — categorise deviations as {beneficial adaptation, neutral workaround, latent risk, active hazard}. Report gap count per category and exemplar descriptions rather than a single scalar — the qualitative detail is what supports intervention.
```

**Limitations**

> Ethnographic methods are resource-intensive and subjective. WAI is itself often poorly documented. Observer effects shape observed behaviour. Generalisation across practices is limited.

**Novel Thinking / Implications**

> 💡 Every complex sociotechnical system has a WAI/WAD gap — procedures can never fully specify practice. The Safety-II insight is that adaptations are not automatically failures; they are often what makes the system work at all. The diagnostic question is not "is there a gap?" (there always is) but "which gaps indicate genuine risk vs which indicate necessary adaptation that should be formalised back into WAI?" This metric surfaces the question; human judgment answers it.

-----

### 🟡 Verification Burden

The additional workload created by the need to verify AI-generated content against clinical reality — reading the note, cross-checking against the conversation, identifying errors, making corrections. Distinct from the existing Cognitive Load Assessment metric, which measures total effort. Verification burden is specifically the checking overhead that exists only because the output needs checking. A well-calibrated AVT system minimises this burden; a poorly-calibrated one shifts documentation time into verification time and may eliminate the apparent efficiency gain.

|Dimension              |Value                                                               |
|-----------------------|--------------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                              |
|**Measurement Cadence**|Periodic audit                                                      |
|**Pipeline Layer**     |Cross-cutting                                                       |
|**Assurance Question** |Human Factors                                                       |
|**Measurement Method** |Hybrid                                                              |
|**Lifecycle Phases**   |Day Zero Baseline, Periodic Audit                                   |
|**Responsible Actors** |Deployer, Academic                                                  |
|**Maturity**           |Emerging                                                            |
|**Outcome Type**       |Proximal                                                            |
|**Source**             |JMIR 2026 e86166 SEIPS-based evaluation; GOSH Phase 4 TimeCat data  |

**Why this tier?**

> Conceptually important — distinguishes apparent efficiency gain from actual efficiency gain — but requires time-motion observation methodology (TimeCat or equivalent). Day Zero baseline plus periodic re-measurement supports trajectory analysis.

**Formal Definition**

```
VB = t_review + t_correction + t_cross_reference, measured per consultation. Baseline pre-AVT: equivalent activities (proofreading own notes, referencing structured fields). Net Verification Cost = VB_AVT - VB_pre-AVT. Efficiency gain = (t_documentation_pre - t_documentation_AVT) - Net Verification Cost. A genuinely efficient system has positive net gain after accounting for verification burden.
```

**Limitations**

> TimeCat or equivalent time-motion methodology is labour-intensive. Verification activities are often interleaved with other work and hard to isolate. Self-report on verification time is unreliable because the activity is partly automatic.

**Novel Thinking / Implications**

> 💡 The marketing claim "AVT saves 3 minutes of documentation time per consultation" is meaningless without verification burden accounting. A system that saves 3 minutes of typing but adds 4 minutes of verification has negative net efficiency — and research suggests this scenario is common early in deployment before clinicians develop efficient review patterns. Verification burden should be reported alongside every documentation time saving claim, or the claim should not be reported at all.

-----

### 🔵 Resilience Capacities Assessment

Structured assessment of the clinician-AVT joint cognitive system against the four Safety-II resilience capacities: **responding** to unexpected events, **monitoring** for signs of degradation, **learning** from experience, and **anticipating** future challenges. From Hollnagel's resilience engineering framework. Applied not to AVT alone but to the combined human-machine system as it operates in context.

|Dimension              |Value                                                             |
|-----------------------|------------------------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                                    |
|**Measurement Cadence**|Periodic audit                                                    |
|**Pipeline Layer**     |Cross-cutting                                                     |
|**Assurance Question** |Safety                                                            |
|**Measurement Method** |Hybrid                                                            |
|**Lifecycle Phases**   |Periodic Audit                                                    |
|**Responsible Actors** |Deployer, National Body, Academic                                 |
|**Maturity**           |Proposed / Novel                                                  |
|**Outcome Type**       |Distal                                                            |
|**Source**             |Hollnagel Safety-II; FRAM methodology; resilience engineering literature|

**Why this tier?**

> Research framework applied at system level. Not a routine metric. National or academic responsibility for maturing the methodology into deployable assessment.

**Formal Definition**

```
Four capacity dimensions scored via structured scenario-based assessment and qualitative evaluation:
(1) Responding — when an AVT failure occurs mid-consultation (crash, silent degradation, wrong-patient data), how does the clinician-system respond? Recovery time, recovery completeness, downstream impact.
(2) Monitoring — what signals does the system provide that allow the clinician to detect degradation? Are those signals attended to in practice?
(3) Learning — when errors are discovered, how is that learning captured and integrated into future work? (Links to Hazard Log Completeness and Training Material Currency)
(4) Anticipating — does the deployer identify and prepare for foreseeable challenges (model updates, regulatory changes, novel failure modes)?
Score each capacity 1–5 with narrative justification. Composite is a profile, not a single number.
```

**Limitations**

> Assessment is qualitative and requires trained evaluators. Framework originally developed for complex sociotechnical systems (healthcare, aviation); application to AVT specifically is novel. Scoring inter-rater reliability has not been established for this application.

**Novel Thinking / Implications**

> 💡 Traditional safety metrics are Safety-I: counting failures and aiming for zero. Resilience metrics are Safety-II: assessing the capacity to handle failures that will inevitably occur. An AVT deployment with zero recorded incidents but weak resilience capacities is brittle — the first real test will reveal the gap. This metric family complements rather than replaces the incident-based metrics in Safety & Governance.

-----

### 🟡 AI-Off Performance Test

Scheduled exercises where clinicians document a clinical encounter without AVT assistance, and the resulting documentation is assessed for quality against baseline standards. Provides an operational implementation of the existing Clinical Documentation Skill Attenuation concept — instead of inferring skill degradation longitudinally, directly measure current unassisted capability. Also doubles as business continuity assurance: can the clinical team function if AVT is unavailable?

|Dimension              |Value                                                                                                 |
|-----------------------|------------------------------------------------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                                                                |
|**Measurement Cadence**|Periodic audit                                                                                        |
|**Pipeline Layer**     |Cross-cutting                                                                                         |
|**Assurance Question** |Human Factors                                                                                         |
|**Measurement Method** |Hybrid                                                                                                |
|**Lifecycle Phases**   |Day Zero Baseline, Periodic Audit                                                                     |
|**Responsible Actors** |Deployer                                                                                              |
|**Maturity**           |Proposed / Novel                                                                                      |
|**Outcome Type**       |Distal                                                                                                |
|**Source**             |Operationalisation of existing Clinical Documentation Skill Attenuation metric; Lancet Gastroenterology 2025 endoscopist AI-off study (ADR fell 28.4%→22.4% when AI removed)|

**Why this tier?**

> Operationally feasible for any deployer willing to commit protected time. More actionable than longitudinal skill attenuation measurement because it provides current state data. Should be scheduled at Day Zero baseline and repeated annually.

**Formal Definition**

```
Protocol: (1) Schedule defined exercises where clinicians document simulated or real consultations without AVT; (2) Documentation is scored using PDSQI-9 or equivalent validated instrument; (3) Score is compared against the clinician's pre-AVT baseline (if available) and against peer benchmarks. Trajectory Metric = score_current - score_baseline. Cohort Analysis: compare clinicians trained with AVT from day one against those who learned without it.
```

**Limitations**

> Protected time is expensive. Simulated consultations differ from real consultations. Clinicians who know they are being assessed may perform differently. Pre-AVT baseline is often not available for individual clinicians.

**Novel Thinking / Implications**

> 💡 The endoscopy AI-off finding (adenoma detection rate falling from 28.4% to 22.4% when AI was removed after a period of AI use) is the first robust real-world evidence of clinical deskilling from AI dependency. For ambient scribes, the equivalent question is whether clinicians lose the ability to write a clinically complete note unassisted after a period of AVT use. This is testable today. The business continuity case — can the practice function during a vendor outage? — is almost sufficient reason to run the test regardless of the deskilling question.

-----

# Part D — Impact & Outcomes additions

## Patient Experience — new Patient Clinical Outcomes sub-cluster (+4)

*Direct addressing of the Coiera & Fraile-Navarro (JMIR Med Inform February 2026) critique that the AVT evaluation field measures proximal metrics and assumes they correlate with patient outcomes. This sub-cluster makes the distal outcome measurement explicit.*

### 🟡 Full Attentiveness Rate

Proportion of consultation time during which the clinician is fully attentive to the patient, measured objectively rather than through self-report. Distinct from the existing Therapeutic Relationship Impact metric, which captures subjective perception. Stults et al. (2025) reported an increase from 57.9% to 93.0% with ambient AI — a large effect size that, if reproducible, represents one of the strongest AVT benefit signals currently available.

|Dimension              |Value                                                           |
|-----------------------|----------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                          |
|**Measurement Cadence**|Periodic audit                                                  |
|**Pipeline Layer**     |Cross-cutting                                                   |
|**Assurance Question** |Patient Experience                                              |
|**Measurement Method** |Passive Observational                                           |
|**Lifecycle Phases**   |Day Zero Baseline, Periodic Audit                               |
|**Responsible Actors** |Deployer, Academic                                              |
|**Maturity**           |Emerging                                                        |
|**Outcome Type**       |Proximal                                                        |
|**Source**             |Stults et al. 2025 (57.9%→93.0% improvement with ambient AI)     |

**Why this tier?**

> Observable with time-motion methodology (TimeCat or equivalent). Day Zero baseline enables pre/post comparison. Important for establishing genuine patient experience improvement rather than self-reported improvement.

**Formal Definition**

```
Full Attentiveness = t_eye_contact + t_active_listening + t_direct_engagement / t_total_consultation. Measured via TimeCat observation, video analysis, or (where accepted by patients) automated gaze tracking. Baseline pre-AVT vs post-AVT comparison. Report as distribution across consultations, not just mean — the clinically relevant improvement is often in the tail (consultations where the clinician was previously heavily divided between patient and screen).
```

**Limitations**

> Observation methodology is labour-intensive. Observer effects change clinician behaviour. Eye contact patterns are culturally variable and not always a valid proxy for attention. Patient consent required for video or automated tracking.

**Novel Thinking / Implications**

> 💡 This is probably the strongest candidate for a positive AVT benefit metric that isn't subject to the Coiera critique. Unlike documentation time saved (which says nothing about patient outcome), attentiveness is directly related to the therapeutic alliance, to patient disclosure, and to shared decision-making. If the Stults et al. finding is reproducible, it becomes the primary argument for AVT adoption on quality-of-care grounds rather than efficiency grounds.

-----

### 🔵 Patient Comprehension of AI-Generated Summaries

When AI-generated clinical summaries are shared with patients (via NHS App, patient portals, or printed after-visit summaries), do patients actually understand them? Distinct from the existing Patient-Perceived Accuracy metric, which measures recognition ("does this match our conversation?"). Comprehension measures whether the patient can correctly state what the summary says about their condition, medications, and next steps.

|Dimension              |Value                                                                    |
|-----------------------|-------------------------------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                                           |
|**Measurement Cadence**|Periodic audit                                                           |
|**Pipeline Layer**     |Summarisation                                                            |
|**Assurance Question** |Patient Experience                                                       |
|**Measurement Method** |Survey                                                                   |
|**Lifecycle Phases**   |Periodic Audit                                                           |
|**Responsible Actors** |Deployer, Academic                                                       |
|**Maturity**           |Proposed / Novel                                                         |
|**Outcome Type**       |Distal                                                                   |
|**Source**             |Health literacy research; growing relevance as patient access to records expands|

**Why this tier?**

> Important as patient-facing summaries become routine. Research-grade measurement methodology required. Best suited for periodic structured study.

**Formal Definition**

```
Patient Comprehension Test: after receiving an AI-generated summary, patient is asked structured questions about: (1) primary diagnosis or problem identified; (2) medications prescribed and their purpose; (3) follow-up actions required; (4) warning signs requiring re-contact. Comprehension Rate = |correctly_answered_questions| / |total_questions|. Disaggregate by health literacy level, age, language, and education to detect differential comprehension.
```

**Limitations**

> Requires patient time and willingness. Cultural and language barriers affect comprehension measurement itself. Summaries generated for clinical purposes may use language appropriate for clinicians but inaccessible to patients — this is a separable design question from AVT accuracy.

**Novel Thinking / Implications**

> 💡 With NHS App access making records patient-facing by default, AI-generated summaries written in clinical language become a health literacy barrier. A summary that is technically correct but uses "dyspnoea" instead of "breathlessness" is accurate from an AVT evaluation standpoint but opaque to the patient. Comprehension measurement should drive a design choice: should AVT generate two versions (clinical record + patient summary) or one version written for both audiences?

-----

### 🔵 Downstream Diagnostic Accuracy

Whether clinicians making subsequent decisions based on AVT-generated notes arrive at the same diagnostic and management conclusions they would have reached if they had access to the original consultation. Measured through controlled clinical reasoning studies where clinicians work from AVT notes vs verbatim transcripts vs direct observation. The distal outcome metric Coiera & Fraile-Navarro argue is missing from current AVT evaluation.

|Dimension              |Value                                                             |
|-----------------------|------------------------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                                    |
|**Measurement Cadence**|Periodic audit                                                    |
|**Pipeline Layer**     |End-to-End                                                        |
|**Assurance Question** |Safety                                                            |
|**Measurement Method** |Human Review                                                      |
|**Lifecycle Phases**   |Periodic Audit                                                    |
|**Responsible Actors** |Academic, National Body                                           |
|**Maturity**           |Proposed / Novel                                                  |
|**Outcome Type**       |Distal                                                            |
|**Source**             |Coiera & Fraile-Navarro, JMIR Med Inform February 2026            |

**Why this tier?**

> Gold-standard distal outcome metric. Extremely resource-intensive. National research programme responsibility. Complements the existing Clinical Decision Equivalence metric by focusing specifically on diagnostic rather than management decisions.

**Formal Definition**

```
Blinded multi-clinician study design: same clinical case presented in three conditions — (a) clinician observes consultation directly, (b) clinician reads AVT-generated note, (c) clinician reads verbatim transcript. Each clinician makes diagnostic and differential diagnostic choices. Downstream Diagnostic Accuracy = agreement between conditions. Primary metric: κ between AVT condition and direct observation condition. Secondary metric: discrepancies stratified by clinical complexity.
```

**Limitations**

> Very expensive — requires multiple blinded clinicians per case, clinical reasoning time, and careful study design. Inter-clinician variation in diagnostic reasoning adds noise. Simulated decision-making may not reflect real-world behaviour under time pressure.

**Novel Thinking / Implications**

> 💡 This is the metric that answers the question "does AVT preserve the clinical signal?" If clinicians reading AVT-generated notes make different diagnostic decisions than clinicians who observed the original consultation, all the proximal metrics (WER, edit rate, documentation time) are at best partially informative and at worst misleading. The Coiera critique is that the field has been measuring proxies and assuming they correlate with this — without evidence. This metric is the evidence.

-----

### 🔵 Medication Error Rate Differential

Pre/post AVT comparison of medication errors at the practice or trust level, including wrong-drug, wrong-dose, wrong-frequency, allergy-related, and interaction-related errors. The ultimate distal outcome that medication documentation accuracy ultimately serves. If AVT improves medication documentation (per attribute-level metrics) but medication errors don't decrease, the documentation improvement is not reaching the patient.

|Dimension              |Value                                                                |
|-----------------------|---------------------------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                                       |
|**Measurement Cadence**|Periodic audit                                                       |
|**Pipeline Layer**     |End-to-End                                                           |
|**Assurance Question** |Safety                                                               |
|**Measurement Method** |Hybrid                                                               |
|**Lifecycle Phases**   |Day Zero Baseline, Periodic Audit                                    |
|**Responsible Actors** |National Body, Academic                                              |
|**Maturity**           |Proposed / Novel                                                     |
|**Outcome Type**       |Distal                                                               |
|**Source**             |Coiera critique; patient safety outcome literature; LFPSE medication categories|

**Why this tier?**

> Longitudinal outcome metric requiring substantial baseline period and statistical controls. Not routinely measurable at single-practice level. National or regional evaluation responsibility.

**Formal Definition**

```
Medication Error Rate = |medication_errors_reported| / |total_prescriptions|, stratified by error type and severity. Differential = (rate_post_AVT - rate_pre_AVT) / rate_pre_AVT. Requires: (1) minimum 12-month pre-AVT baseline; (2) consistent reporting culture across periods; (3) adjustment for concurrent interventions. Use difference-in-differences against matched non-AVT controls where possible.
```

**Limitations**

> Medication errors are under-reported; reporting rates vary with safety culture; attribution to AVT requires careful controls. Low baseline rates mean large populations needed for statistical power.

**Novel Thinking / Implications**

> 💡 This closes the loop between AVT documentation accuracy and patient safety outcomes. The implicit theory of change for AVT safety is: better documentation → fewer medication errors → safer patients. Each link in that chain is assumed but not measured. This metric tests the final link directly. If it shows no effect, the proximal metrics need re-examination; if it shows effect, the proximal metrics are validated as meaningful safety signals.

-----

## Fairness & Equity additions (+3)

### 🔵 Intersectional Compound Fairness Score

Extension of the existing Intersectional Performance metric using the FAIR-MED Compound Fairness Score methodology. Where Intersectional Performance measures accuracy at each demographic intersection, Compound Fairness Score calculates whether disadvantage compounds multiplicatively or additively — that is, whether the intersection performs worse than would be predicted by adding the individual demographic disadvantages.

|Dimension              |Value                                                                                |
|-----------------------|-------------------------------------------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                                                       |
|**Measurement Cadence**|Periodic audit                                                                       |
|**Pipeline Layer**     |Cross-cutting                                                                        |
|**Assurance Question** |Fairness & Equity                                                                    |
|**Measurement Method** |Computational                                                                        |
|**Lifecycle Phases**   |Periodic Audit                                                                       |
|**Responsible Actors** |Vendor, National Body, Academic                                                      |
|**Maturity**           |Emerging                                                                             |
|**Outcome Type**       |Distal                                                                               |
|**Source**             |FAIR-MED: Bias Detection and Fairness Evaluation in Healthcare Focused XAI (Springer 2025)|

**Why this tier?**

> Research-grade methodology requiring substantial demographic-linked data. National evaluation or vendor pre-deployment. Complements rather than replaces single-axis fairness metrics.

**Formal Definition**

```
For demographic axes A₁, A₂, ..., Aₙ with performance gaps gap(Aᵢ): expected intersection gap under additive model = Σ gap(Aᵢ); actual intersection gap = observed gap at intersection ∩Aᵢ. Compound Fairness Score CFS = actual_gap / expected_additive_gap. CFS > 1 indicates multiplicative compounding (intersection is worse than sum of parts); CFS ≈ 1 indicates additive; CFS < 1 indicates sub-additive. Multiplicative compounding is the warning signal for worst-case population failures.
```

**Limitations**

> Requires large enough samples at every demographic intersection for stable estimation — often infeasible for rare intersections. Additive model assumption may not hold even in fair systems. Interpretation is statistical rather than mechanistic.

**Novel Thinking / Implications**

> 💡 Single-axis fairness can miss compound disadvantage entirely. A system that performs acceptably on "elderly", "EAL", "female", and "low literacy" as separate categories may perform catastrophically on the intersection. The compound fairness score tests whether this is happening and quantifies how bad it is. For NHS populations where intersectional disadvantage is the rule rather than the exception, single-axis metrics alone are insufficient.

-----

### 🔵 Cross-Platform Fairness Consistency

Whether fairness properties are consistent across multiple AVT platforms deployed within the same ICB or trust. Differential bias between vendors is itself an equity concern — if Practice A uses Vendor X (which performs well on majority populations but poorly on minority populations) and Practice B uses Vendor Y (with the opposite bias profile), patients experience different quality of documentation depending on which practice happens to serve them.

|Dimension              |Value                                                              |
|-----------------------|-------------------------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                                     |
|**Measurement Cadence**|Periodic audit                                                     |
|**Pipeline Layer**     |Cross-cutting                                                      |
|**Assurance Question** |Fairness & Equity                                                  |
|**Measurement Method** |Computational                                                      |
|**Lifecycle Phases**   |Periodic Audit                                                     |
|**Responsible Actors** |Regional (ICB), National Body                                      |
|**Maturity**           |Proposed / Novel                                                   |
|**Outcome Type**       |Distal                                                             |
|**Source**             |Extension of existing Cross-Practice Variance Coefficient into equity dimension|

**Why this tier?**

> Regional or national metric. Requires cross-vendor evaluation on equivalent test data. Only meaningful where multiple platforms are deployed across an integrated care system.

**Formal Definition**

```
For each vendor v in the ICB's deployed platforms: compute demographic-disaggregated performance profile P_v. Cross-Platform Fairness Consistency = variance of P_v across vendors for each demographic group. High variance = patients experience differential fairness depending on which practice (and which vendor) they attend. Report per demographic group; worst-case group determines the equity-consistency floor for the ICB.
```

**Limitations**

> Requires standardised test data available for use against multiple vendors — which currently doesn't exist for NHS. Vendors may resist independent cross-comparison. Aggregation across practices raises information governance questions.

**Novel Thinking / Implications**

> 💡 The current NHS AVT landscape allows ICBs to have multiple vendors deployed across their patch. If those vendors have different fairness profiles, the ICB is effectively running an uncontrolled experiment where patient outcomes depend on which GP they happened to register with. This is invisible to single-vendor fairness metrics and can only be detected by cross-platform comparison. Commissioning should consider fairness consistency as a portfolio-level property, not just a single-vendor property.

-----

### 🟡 Accent Taxonomy Standardisation

Meta-metric assessing whether demographic-disaggregated WER uses a sociolinguistically informed accent taxonomy appropriate for NHS populations, rather than ad-hoc or inappropriate categorisations. The FAccT 2024 critique of ASR accent categorisation highlighted that race-based, geography-based, and native/non-native categories are systematically flawed proxies for the actual acoustic variation that affects ASR performance. For NHS deployment, a meaningful taxonomy must cover British regional accents, South Asian English varieties, West African English, Caribbean English, Eastern European English, and other varieties representative of NHS patient populations.

|Dimension              |Value                                                         |
|-----------------------|--------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                        |
|**Measurement Cadence**|One-off gate                                                  |
|**Pipeline Layer**     |ASR / Transcription                                           |
|**Assurance Question** |Fairness & Equity                                             |
|**Measurement Method** |Human Review                                                  |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                |
|**Responsible Actors** |Vendor, National Body                                         |
|**Maturity**           |Proposed / Novel                                              |
|**Outcome Type**       |Proximal                                                      |
|**Source**             |FAccT 2024 critique of ASR accent categorisation; sociolinguistics literature|

**Why this tier?**

> Prerequisite for meaningful fairness assessment. Without a defensible taxonomy, Demographic-Disaggregated WER numbers are not comparable across vendors and may hide rather than reveal bias.

**Formal Definition**

```
Assessment against criteria: (1) Sociolinguistic validity — categories correspond to identifiable phonological communities, not political or racial groupings; (2) NHS relevance — categories include varieties actually present in NHS patient populations; (3) Sample adequacy — each category has sufficient evaluation data for stable WER estimation; (4) Documentation — categorisation methodology is transparent and replicable. Binary pass/fail per criterion; composite = all four must pass.
```

**Limitations**

> Sociolinguistic categorisation is itself contested. Any taxonomy makes choices that can be critiqued. The alternative — no categorisation — is worse because it hides all disparities.

**Novel Thinking / Implications**

> 💡 The hardest form of bias to fix is bias that cannot be measured, and ad-hoc accent categorisation produces unmeasurable bias. An NHS-specific accent taxonomy is infrastructure that would benefit every deployed AVT system — a national body responsibility that would pay for itself quickly. Without it, every vendor's Demographic-Disaggregated WER is self-reported against self-chosen categories, and independent verification is impossible.

-----

# End of Batch 2

**Metrics drafted in this batch: 12**
- End-to-End Pipeline: 1 (Cumulative Information Yield)
- Human Factors — Sociotechnical & Resilience sub-cluster: 4 (WAI/WAD Gap, Verification Burden, Resilience Capacities Assessment, AI-Off Performance Test)
- Patient Experience — Patient Clinical Outcomes sub-cluster: 4 (Full Attentiveness Rate, Patient Comprehension, Downstream Diagnostic Accuracy, Medication Error Rate Differential)
- Fairness & Equity: 3 (Intersectional Compound Fairness Score, Cross-Platform Fairness Consistency, Accent Taxonomy Standardisation)

**Running total across Batches 1–2: 33 of ~64 entries**

**Next**
- Batch 3: Safety & Governance — Longitudinal Drift sub-cluster (4) + **NHS Compliance & Regulatory (new group, 10)** + Security & Adversarial Robustness (2) = 16 entries
- Batch 4: Privacy & Data Governance (5) + Operational (3) + **Environmental & Sustainability (new group, 3)** + Vendor Transparency (1) + Meta-evaluation (2) = 14 entries
