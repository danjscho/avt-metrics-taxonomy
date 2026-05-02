### IO.PX-1 🟢 Patient Opt-Out Rate

Percentage declining AVT. Disaggregate by demographics to reveal equity issues in consent model.

| Dimension | Value |
|-----------|-------|
| **Reference** | IO.PX-1 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Patient Experience |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | [NAS-Day-Zero-SPI-internal]; [CQC-Mythbuster-109] |

**Why this tier?**

> Deployer-measurable from practice records. Low-burden continuous monitoring. Rising rates signal trust issues. Demographic disaggregation reveals consent model equity.

**Formal Definition**

```
OOR = |P_optout| / |P_offered|. χ² test for independence between opt-out and demographic group. Significant association = inequitable consent model.
```

**Reference Standard**

> EPR + AVT product workflow telemetry. Two distinct opt-out events MUST be tracked separately:
>
> - **Registration-level opt-out** - patient declines AVT use across all encounters with the practice (status set in patient record)
> - **Per-encounter opt-out** - patient declines AVT for a specific consultation while remaining eligible elsewhere (cross-link to [GV.CR-1 Patient Dissent Recording Rate](#gv-cr-1))
>
> Aggregating the two hides the underlying signal. The denominator `P_offered` is the count of patients to whom AVT use was offered (not consultations); a patient declining once and accepting later contributes once to numerator and once to denominator. Pre-conditions for inclusion: the patient was demonstrably informed (cross-link to [GV.CR-2 Verbal Notification Compliance](#gv-cr-2)) - undocumented offers are excluded with reason.

**Operational Specification**

> - **Window:** continuous; monthly aggregate per practice and per clinician.
> - **Population:** all patients offered AVT during the window. Excludes patients for whom AVT was not offered (e.g. consultation type explicitly carved out under proposed metric *GV.CR-14 Consultation-Type Appropriateness Assessment* — see Roadmap — when implemented).
> - **Demographic disaggregation MANDATORY:** opt-out rate stratified by age band, sex, ethnicity, and primary language at minimum. Disability status and deprivation index where the data is available. Aggregate-only reporting hides the equity signal that is the metric's primary purpose.
> - **Statistical test MANDATORY:** χ² (or Fisher's exact for small cells) test for independence between opt-out and each demographic axis, with multiple-comparison correction (Holm-Bonferroni or FDR) across axes. Report both raw rates and significance.
> - **Trajectory MANDATORY:** monthly opt-out rate trajectory per practice; rising aggregate rate is a separate signal from disparate rate, and both matter.

**Threshold Guidance**

> ⚠️ **Provenance:** the demographic-disaggregation requirement and the equity-not-preference framing follow from the [NAS-Day-Zero-SPI-internal] and [CQC-Mythbuster-109] cited above, plus the existing Novel Thinking section. Specific numerical thresholds (5 % aggregate alert, 2× demographic-disparity ratio trigger, χ² p < 0.05 with Holm correction) are **proposed in v3.4 as starting points**, not externally validated. The metric's value is in the disparities it reveals, not in any absolute opt-out target; require local calibration before contractual use.
>
> - **Pre-deployment / Day Zero baseline:** establish baseline opt-out rate disaggregated by the demographic axes above; document any historical signal in the practice population that should be expected to carry over.
> - **Continuous monitoring alert:** monthly aggregate opt-out rate rises > 2 percentage points from per-practice baseline; OR any demographic axis shows opt-out ratio ≥ 2× the practice mean with χ² (Holm-corrected) p < 0.05.
> - **Pause / review trigger:** demographic disparity ≥ 3× the practice mean sustained two consecutive months on any axis (signals systematic equity failure in the consent model, not noise); OR aggregate opt-out rate rises > 5 percentage points (signals trust deterioration). Pair with [GV.CR-2 Verbal Notification Compliance](#gv-cr-2) to test whether the consent model is the cause.

**References**

- **CQC**: Mythbuster 109: implied consent sufficient but patients must be informed

**Limitations**

> Low opt-out ≠ informed consent. The demographic-disaggregation requirement in the Operational Specification surfaces equity issues that aggregate rate hides; it does not address the upstream concern that opt-out rates depend on the quality of notification (covered by GV.CR-2) and on patient understanding of what they are declining (no current metric).

**Novel Thinking / Implications**

> 💡 Higher opt-out in specific demographics = equity issue in consent model, not just preference.

---

### IO.PX-2 🔵 Patient-Perceived Accuracy

When patients are shown their AVT-generated notes, do they recognise the consultation? Distinct from clinician-judged accuracy - patients may identify omissions or distortions that clinicians miss because they were the speakers.

| Dimension | Value |
|-----------|-------|
| **Reference** | IO.PX-2 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Patient Experience |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | Patient-centred care evaluation methodology |

**Why this tier?**

> Important but resource-intensive. Best suited for periodic structured study rather than routine measurement.

**Formal Definition**

```
Patient survey after note generation: 'Does this note accurately reflect our conversation?' (5-point Likert, plus free-text comments). Accuracy Rate = proportion answering 'accurate' or 'very accurate'. Comments analysed for systematic complaint patterns.
```

**Limitations**

> Requires patient access to notes and willingness to provide feedback. Patient understanding of clinical documentation conventions varies.

**Novel Thinking / Implications**

> 💡 Patients are the only assessor who knows what was actually said in the consultation from their own perspective. They notice when their concerns were minimised, when the clinician's interpretation differs from their own, and when emotional content was stripped. With patient access to records becoming standard (NHS App), patient-perceived accuracy is increasingly important for trust in the clinical record.

---

### IO.PX-3 🔵 Emotional Content Preservation

Does the note capture the patient's emotional state when clinically relevant? AVT systems trained on standard clinical notes may strip affective content that matters for mental health, end-of-life care, safeguarding, and complex consultations.

| Dimension | Value |
|-----------|-------|
| **Reference** | IO.PX-3 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Patient Experience |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | Identified gap in clinical AI evaluation - affective content is systematically deprioritised |

**Why this tier?**

> Critical for specific clinical contexts (mental health, palliative care, safeguarding) but not universally applicable.

**Formal Definition**

```
For consultations involving emotional content (annotated): proportion of clinically relevant emotional markers preserved in summary. Categories: distress, grief, fear, ambivalence, hope. Required for: mental health, end-of-life, safeguarding, life-limiting illness consultations.
```

**Limitations**

> Emotional content annotation is subjective. Different clinical contexts have different requirements for affective documentation.

**Novel Thinking / Implications**

> 💡 AVT systems trained on standard primary care notes have learned that emotional content is rarely documented. When deployed in mental health, palliative care, or safeguarding contexts, this learned behaviour becomes a serious gap. The patient who said 'I just don't know how I'll cope' deserves to have that documented - but the AI may strip it as non-clinical content.

---

### IO.PX-4 🔵 Cultural & Linguistic Appropriateness

Does the note use language that respects the patient's cultural and linguistic context? Important for shared records that patients can access. Includes avoiding stigmatising language and respecting how patients describe their own conditions.

| Dimension | Value |
|-----------|-------|
| **Reference** | IO.PX-4 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Patient Experience |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
| **Source** | Patient-centred care literature; growing concern with patient access to records |

**Why this tier?**

> Important quality dimension but requires structured audit by appropriate reviewers.

**Formal Definition**

```
Audit for: (1) stigmatising language ('drug-seeking', 'non-compliant', 'frequent flyer'); (2) cultural assumptions; (3) translation of patient's own terms into clinical jargon when patient access is enabled. Proportion of notes flagged in audit.
```

**Limitations**

> Cultural appropriateness is highly context-dependent. Audit requires diverse reviewers.

**Novel Thinking / Implications**

> 💡 AVT systems trained on legacy clinical notes may perpetuate language patterns that are inappropriate when patients can read their own records. The language that was acceptable when notes were clinician-only is sometimes unacceptable when notes are shared. This is a quiet failure mode - the AI is faithfully reproducing patterns from its training data that need to change.

---

### IO.PX-5 🔵 Chilling Effect Assessment

Whether AVT suppresses sensitive disclosures. Most under-researched risk - population-level safety issue if record becomes systematically biased.

| Dimension | Value |
|-----------|-------|
| **Reference** | IO.PX-5 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Patient Experience |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | [NHS-LLM-Framework] gap analysis |

**Why this tier?**

> The most under-researched AVT risk but extremely difficult to measure - detecting information that wasn't shared. Requires carefully designed qualitative research.

**Formal Definition**

```
Disclosure Rate Ratio DRR = DR_AVT / DR_noAVT for sensitive categories (mental health, substance use, sexual health, domestic abuse). DRR < 1.0 = chilling effect. Mixed-methods: quantitative + qualitative.
```

**Limitations**

> Detecting information not shared requires careful qualitative research.

**Novel Thinking / Implications**

> 💡 If AVT suppresses sensitive disclosures, the record becomes systematically biased - missing exactly the information that matters most.

---

### IO.PX-6 🔵 Therapeutic Relationship Impact

How AVT affects consultation quality. Net impact depends on whether review is in-consultation or post-consultation.

| Dimension | Value |
|-----------|-------|
| **Reference** | IO.PX-6 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Patient Experience |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | Consultation quality literature |

**Why this tier?**

> Subjective, context-dependent. Positive novelty effect masks longer-term changes. Research priority but not routine deployer measurement.

**Formal Definition**

```
Multi-dimensional: (1) PCQ-18 adapted; (2) Clinician engagement scale; (3) Eye contact ratio; (4) Consultation duration. Pre/post crossover design.
```

**Limitations**

> Novelty effect may mask long-term changes.

**Novel Thinking / Implications**

> 💡 Marketed as freeing clinicians, but review-before-signing creates new post-consultation task. Workflow design determines the outcome.

---

---

### Patient Clinical Outcomes sub-cluster

*Direct addressing of the Coiera & Fraile-Navarro (JMIR Med Inform February 2026) critique that the AVT evaluation field measures proximal metrics and assumes they correlate with patient outcomes. This sub-cluster makes the distal outcome measurement explicit.*

---

### IO.PX-7 🟡 Full Attentiveness Rate

Proportion of consultation time during which the clinician is fully attentive to the patient, measured objectively rather than through self-report. Distinct from the existing Therapeutic Relationship Impact metric, which captures subjective perception. Stults et al. (2025) reported an increase from 57.9% to 93.0% with ambient AI - a large effect size that, if reproducible, represents one of the strongest AVT benefit signals currently available.

|Dimension              |Value                                                           |
|-----------------------|----------------------------------------------------------------|
| **Reference** | IO.PX-7 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                          |
|**Measurement Cadence**|Periodic audit                                                  |
|**Pipeline Layer**     |Cross-cutting                                                   |
|**Assurance Question** |Patient Experience                                              |
|**Measurement Method** |Passive Observational                                           |
|**Lifecycle Phases**   |Day Zero Baseline, Periodic Audit                               |
|**Responsible Actors** |Deployer, Academic                                              |
|**Maturity**           |Emerging                                                        |
|**Outcome Type**       |Proximal                                                        |
|**Applicability**      |AVT-Contextualised                                              |
|**Source**             |See-also [Stults-2025] (clinician self-reported attentiveness gains; different construct from objective time-on-task)|

**Why this tier?**

> Observable with time-motion methodology (TimeCat or equivalent). Day Zero baseline enables pre/post comparison. Important for establishing genuine patient experience improvement rather than self-reported improvement.

**Formal Definition**

```
Full Attentiveness = t_eye_contact + t_active_listening + t_direct_engagement / t_total_consultation. Measured via TimeCat observation, video analysis, or (where accepted by patients) automated gaze tracking. Baseline pre-AVT vs post-AVT comparison. Report as distribution across consultations, not just mean - the clinically relevant improvement is often in the tail (consultations where the clinician was previously heavily divided between patient and screen).
```

**Limitations**

> Observation methodology is labour-intensive. Observer effects change clinician behaviour. Eye contact patterns are culturally variable and not always a valid proxy for attention. Patient consent required for video or automated tracking.

**Novel Thinking / Implications**

> 💡 This is probably the strongest candidate for a positive AVT benefit metric that isn't subject to the Coiera critique. Unlike documentation time saved (which says nothing about patient outcome), attentiveness is directly related to the therapeutic alliance, to patient disclosure, and to shared decision-making. If the Stults et al. finding is reproducible, it becomes the primary argument for AVT adoption on quality-of-care grounds rather than efficiency grounds.

---

### IO.PX-8 🔵 Patient Comprehension of AI-Generated Summaries

When AI-generated clinical summaries are shared with patients (via NHS App, patient portals, or printed after-visit summaries), do patients actually understand them? Distinct from the existing Patient-Perceived Accuracy metric, which measures recognition ("does this match our conversation?"). Comprehension measures whether the patient can correctly state what the summary says about their condition, medications, and next steps.

|Dimension              |Value                                                                    |
|-----------------------|-------------------------------------------------------------------------|
| **Reference** | IO.PX-8 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research                                           |
|**Measurement Cadence**|Periodic audit                                                           |
|**Pipeline Layer**     |Summarisation                                                            |
|**Assurance Question** |Patient Experience                                                       |
|**Measurement Method** |Survey                                                                   |
|**Lifecycle Phases**   |Periodic Audit                                                           |
|**Responsible Actors** |Deployer, Academic                                                       |
|**Maturity**           |Proposed / Novel                                                         |
|**Outcome Type**       |Distal                                                                   |
|**Applicability**      |General Healthcare AI                                                    |
|**Source**             |Health literacy research; growing relevance as patient access to records expands|

**Why this tier?**

> Important as patient-facing summaries become routine. Research-grade measurement methodology required. Best suited for periodic structured study.

**Formal Definition**

```
Patient Comprehension Test: after receiving an AI-generated summary, patient is asked structured questions about: (1) primary diagnosis or problem identified; (2) medications prescribed and their purpose; (3) follow-up actions required; (4) warning signs requiring re-contact. Comprehension Rate = |correctly_answered_questions| / |total_questions|. Disaggregate by health literacy level, age, language, and education to detect differential comprehension.
```

**Limitations**

> Requires patient time and willingness. Cultural and language barriers affect comprehension measurement itself. Summaries generated for clinical purposes may use language appropriate for clinicians but inaccessible to patients - this is a separable design question from AVT accuracy.

**Novel Thinking / Implications**

> 💡 With NHS App access making records patient-facing by default, AI-generated summaries written in clinical language become a health literacy barrier. A summary that is technically correct but uses "dyspnoea" instead of "breathlessness" is accurate from an AVT evaluation standpoint but opaque to the patient. Comprehension measurement should drive a design choice: should AVT generate two versions (clinical record + patient summary) or one version written for both audiences?

---

### IO.PX-9 🔵 Downstream Diagnostic Accuracy

Whether clinicians making subsequent decisions based on AVT-generated notes arrive at the same diagnostic and management conclusions they would have reached if they had access to the original consultation. Measured through controlled clinical reasoning studies where clinicians work from AVT notes vs verbatim transcripts vs direct observation. The distal outcome metric Coiera & Fraile-Navarro argue is missing from current AVT evaluation.

|Dimension              |Value                                                             |
|-----------------------|------------------------------------------------------------------|
| **Reference** | IO.PX-9 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research                                    |
|**Measurement Cadence**|Periodic audit                                                    |
|**Pipeline Layer**     |End-to-End                                                        |
|**Assurance Question** |Safety                                                            |
|**Measurement Method** |Human Review                                                      |
|**Lifecycle Phases**   |Periodic Audit                                                    |
|**Responsible Actors** |Academic, National Body                                           |
|**Maturity**           |Proposed / Novel                                                  |
|**Outcome Type**       |Distal                                                            |
|**Applicability**      |General Healthcare AI                                             |
|**Source**             |[Coiera-Fraile-Navarro-JMIR-2026]                                 |

**Why this tier?**

> Gold-standard distal outcome metric. Extremely resource-intensive. National research programme responsibility. Complements the existing Clinical Decision Equivalence metric by focusing specifically on diagnostic rather than management decisions.

**Formal Definition**

```
Blinded multi-clinician study design: same clinical case presented in three conditions - (a) clinician observes consultation directly, (b) clinician reads AVT-generated note, (c) clinician reads verbatim transcript. Each clinician makes diagnostic and differential diagnostic choices. Downstream Diagnostic Accuracy = agreement between conditions. Primary metric: κ between AVT condition and direct observation condition. Secondary metric: discrepancies stratified by clinical complexity.
```

**Limitations**

> Very expensive - requires multiple blinded clinicians per case, clinical reasoning time, and careful study design. Inter-clinician variation in diagnostic reasoning adds noise. Simulated decision-making may not reflect real-world behaviour under time pressure.

**Novel Thinking / Implications**

> 💡 This is the metric that answers the question "does AVT preserve the clinical signal?" If clinicians reading AVT-generated notes make different diagnostic decisions than clinicians who observed the original consultation, all the proximal metrics (WER, edit rate, documentation time) are at best partially informative and at worst misleading. The Coiera critique is that the field has been measuring proxies and assuming they correlate with this - without evidence. This metric is the evidence.

---

### IO.PX-10 🔵 Medication Error Rate Differential

Pre/post AVT comparison of medication errors at the practice or trust level, including wrong-drug, wrong-dose, wrong-frequency, allergy-related, and interaction-related errors. The ultimate distal outcome that medication documentation accuracy ultimately serves. If AVT improves medication documentation (per attribute-level metrics) but medication errors don't decrease, the documentation improvement is not reaching the patient.

|Dimension              |Value                                                                |
|-----------------------|---------------------------------------------------------------------|
| **Reference** | IO.PX-10 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research                                       |
|**Measurement Cadence**|Periodic audit                                                       |
|**Pipeline Layer**     |End-to-End                                                           |
|**Assurance Question** |Safety                                                               |
|**Measurement Method** |Hybrid                                                               |
|**Lifecycle Phases**   |Day Zero Baseline, Periodic Audit                                    |
|**Responsible Actors** |National Body, Academic                                              |
|**Maturity**           |Proposed / Novel                                                     |
|**Outcome Type**       |Distal                                                               |
|**Applicability**      |General Healthcare AI                                                |
|**Source**             |[Coiera-Fraile-Navarro-JMIR-2026] (critique); patient safety outcome literature; [LFPSE] medication categories|

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
