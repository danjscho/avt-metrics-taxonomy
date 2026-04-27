# AVT Metrics Taxonomy - Underspecification Warnings (Pass 2)

Fifteen additions to existing metric entries in the taxonomy. Each flags a specific measurement-science gap with literature evidence, using a consistent three-tier severity scheme.

## Severity scheme

- **Tier A - No established methodology.** The concept is referenced in the literature but has no operationalised definition, no validated instrument, and no published measurement protocol. Requires definitional work before it can be reliably measured at all.
- **Tier B - Concept defined, no AVT-specific validation.** The construct is well-understood and measurement approaches exist in related fields, but have not been validated for ambient scribe contexts. Interim measurement is possible with explicit caveats.
- **Tier C - Technically defined, clinical validity unproven or disproven.** The metric has a rigorous computational definition and is widely reported, but published evidence shows it correlates poorly with clinical quality or is implemented with non-standardised inputs that prevent cross-vendor comparison.

## Format convention

Each warning is formatted as a labelled block quote to match the existing taxonomy style ("Why this tier?", "Limitations", "Novel Thinking / Implications"):

```
**⚠️ Underspecification Warning (Tier X - short characterisation)**

> [Body text]
```

Placement convention: insert the warning **after the existing Limitations block, before Novel Thinking / Implications** (or at the end of the entry if Novel Thinking is absent). This keeps the warning visible when readers scan Limitations but clearly separated from the drafter's more speculative "Novel Thinking" observations.

## Summary of additions

| # | Target metric | Section | Severity |
|---|---|---|---|
| 1 | ROUGE Scores | Summarisation / NLP | C |
| 2 | BERTScore | Summarisation / NLP | C |
| 3 | Hallucination Rate | Summarisation / NLP | B |
| 4 | LLM-as-a-Judge (PDSQI-9 Proxy) | Summarisation / NLP | C |
| 5 | Diarisation Error Rate | Diarisation | C |
| 6 | Demographic-Disaggregated WER | ASR / Transcription | C |
| 7 | Medical Word Error Rate (M-WER) | ASR / Transcription | B |
| 8 | Clinical Keyword Error Rate (CK-ER) | ASR / Transcription | B |
| 9 | Cognitive Load Assessment | Human Factors & Workflow | B |
| 10 | Trust Calibration Survey | Human Factors & Workflow | B |
| 11 | Automation Bias Detection (Error Injection) | Human Factors & Workflow | B |
| 12 | Trust Halo Decay Rate | Human Factors & Workflow | A |
| 13 | Note Review Fatigue Trajectory | Human Factors & Workflow | A |
| 14 | Off-Label Use Detection Rate | Safety & Governance | A |
| 15 | Clinical Decision Equivalence | End-to-End Pipeline | B |

Tier distribution of warnings: **3 Tier A, 7 Tier B, 5 Tier C.**

---

# 1. ROUGE Scores

**Section:** Summarisation / NLP
**Placement:** After the existing Limitations block ("Measures lexical overlap, not clinical accuracy...")

**⚠️ Underspecification Warning (Tier C - technically rigorous, clinically invalid)**

> Published evidence demonstrates near-zero correlation between ROUGE and human clinical judgment in clinical summarisation evaluation. Croxford et al. (2025, npj Digital Medicine) reported ROUGE-L Kendall-Tau of just 0.080 with expert clinician scoring on clinical diagnosis generation - indistinguishable from random for practical purposes. A separate investigation of automated metrics for medical note generation (ar5iv 2305.17364) documented catastrophic failure modes with Spearman ρ between −0.66 and −0.77 in some medical contexts, meaning higher ROUGE scores actively correlated with worse human judgments. The root cause is that string matching penalises clinically valid paraphrase and rewards surface overlap regardless of clinical meaning. **ROUGE must not be used as a standalone clinical quality indicator.** Retain only for technical benchmarking, and always report alongside a validated clinical instrument (PDSQI-9, CREOLA, or LLM-as-a-Judge with bias quantification).

---

# 2. BERTScore

**Section:** Summarisation / NLP
**Placement:** After the existing Limitations block ("Linguistic similarity ≠ clinical correctness...")

**⚠️ Underspecification Warning (Tier C - better than ROUGE but insufficient alone)**

> BERTScore-R achieves approximately Pearson 0.62 correlation with omission rate in clinical summarisation (Croxford et al. 2025) - materially better than ROUGE but still inadequate as a standalone clinical quality indicator. The underlying limitation is the same as ROUGE: semantic similarity is not clinical correctness. A note can be semantically close to the reference while missing a clinically critical element, or semantically distant while conveying the same clinical meaning through appropriate medical abstraction. BERTScore is useful as one input to a multi-metric assessment but should never be reported as the primary quality finding. Pair with PDSQI-9 or an LLM-as-a-Judge protocol that has been subjected to bias quantification.

---

# 3. Hallucination Rate

**Section:** Summarisation / NLP
**Placement:** After the existing Limitations block ("Definition varies. No standard severity weighting."), before Novel Thinking / Implications

**⚠️ Underspecification Warning (Tier B - conceptually central, definitionally unstable)**

> The term "hallucination" has no universally accepted operational definition in clinical NLG. The CREOLA framework (Asgari et al., npj Digital Medicine 2025) explicitly identifies this ambiguity as a fundamental measurement challenge. Reported rates across the published literature range from 1–3% in deployed ambient scribe studies to 43–67% in adversarial LLM clinical benchmarks - a span that largely reflects methodological differences rather than true performance variation. Only two public reference datasets exist for AVT hallucination evaluation (ACI Bench, PriMock), which limits cross-study comparability. Promising recent work: the CHECK framework (arXiv 2506.11129) reduced hallucination from 31% to 0.3% using information-theoretic classification with AUC 0.95–0.96 and is a candidate standard for operational definition. Until a consensus definition emerges, require reporting of: (a) the specific subtype taxonomy used (CREOLA or equivalent); (b) inter-rater reliability on the taxonomy; (c) the reference dataset; (d) the severity classification scheme.

---

# 4. LLM-as-a-Judge (PDSQI-9 Proxy)

**Section:** Summarisation / NLP
**Placement:** After the existing Limitations block ("One LLM evaluating another = correlated failure modes..."), before Novel Thinking / Implications

**⚠️ Underspecification Warning (Tier C - high measured reliability, unknown validity)**

> LLM-as-a-Judge has documented biases that are rarely quantified in published deployment: position bias (prefers the first response in pairwise comparison), verbosity bias (prefers longer responses), self-enhancement bias (prefers outputs from the same model family as the judge), and fine-grained scoring unreliability (inconsistent discrimination at the high end of Likert scales). The headline Croxford et al. (2025) finding of GPT-o3-mini achieving ICC 0.818 with human evaluators on PDSQI-9 should be read alongside a separate Rwanda clinical LLM evaluation study that found LLM judges correlated more strongly with non-expert than expert annotators - apparent reliability that may reflect alignment with a particular class of evaluator rather than with clinical ground truth. This is the most uncomfortable possibility in automated evaluation: high ICC with humans that does not generalise to correctness. Any deployment relying on LLM-as-a-Judge for safety-relevant decisions should run the proposed **LLM-Judge Bias Quantification** metric (see Meta-evaluation section) and document residual uncertainty before treating judge outputs as substitutes for expert review.

---

# 5. Diarisation Error Rate

**Section:** Diarisation
**Placement:** After the existing Limitations block ("Challenging in multi-party consultations. Most benchmarks assume two speakers.")

**⚠️ Underspecification Warning (Tier C - standard methodology, absent clinical context)**

> DER has a rigorous technical definition (NIST RT evaluation protocol) and established general benchmarks (AMI ~7.2%, CALLHOME ~12.4%), but **no clinical-specific benchmarks exist** for the multi-party consultations routinely encountered in NHS practice. No validated link has been established between DER and downstream clinical documentation quality - a low DER does not guarantee accurate speaker attribution on clinically significant utterances, and a moderate DER may be acceptable if the errors concentrate on non-clinical content. Word-level DER (WDER) is more clinically relevant than time-based DER but is rarely reported by vendors. Require WDER from vendors and request reporting stratified by utterance type: clinician instruction, patient symptom report, family contextual information, medication discussion. The aggregate DER number in isolation is technically correct but clinically uninterpretable.

---

# 6. Demographic-Disaggregated WER

**Section:** ASR / Transcription
**Placement:** After the existing Limitations block ("Vendors control test datasets. No independent UK-representative speech corpus exists at scale."), before Novel Thinking / Implications

**⚠️ Underspecification Warning (Tier C - well-defined structure, ad hoc categorisation)**

> Published demographic WER reporting uses ad-hoc accent categorisation that has been systematically critiqued. A FAccT 2024 paper identified race-based, geography-based, and native/non-native categories as poor proxies for the actual acoustic variation that affects ASR performance - they are demographically convenient but phonologically arbitrary. No standardised maximum acceptable disparity threshold exists across the field; the NAS 5 percentage point target is a proposed rather than evidence-based threshold. For NHS context, a defensible taxonomy must include at minimum: British regional accents (with meaningful sub-categorisation), South Asian English varieties (distinct from "Indian English" as a single category), West African English, Caribbean English, and Eastern European English - none of which are consistently present in vendor-reported demographic WER data. The accompanying **Accent Taxonomy Standardisation** metric (Fairness & Equity) assesses whether the categorisation itself is defensible before the disaggregation numbers become meaningful.

---

# 7. Medical Word Error Rate (M-WER)

**Section:** ASR / Transcription
**Placement:** After the existing Limitations block ("No standardised clinical significance ontology exists. Weight assignment is inherently subjective."), before Novel Thinking / Implications

**⚠️ Underspecification Warning (Tier B - no standardised weighting ontology)**

> M-WER requires a weighting ontology defining the clinical significance of token classes. **No such ontology is standardised for NHS or international use.** Abridge's Medical Term Recall (MTR) and DeepScribe's Medical Word Hit Rate are functionally equivalent implementations that use different proprietary term lists and different weighting schemes - so a vendor claiming "95% MTR" cannot be directly compared with another claiming "95% M-WER". A national body standard mapping SNOMED safety-critical concept classes to weight values would make vendor benchmarks comparable and is a candidate for NHS England or equivalent commissioning. Until then, require vendors to disclose (a) their term list and provenance, (b) the weighting scheme, and (c) the reference dataset used for M-WER computation. Refuse to compare M-WER values across vendors without this disclosure.

---

# 8. Clinical Keyword Error Rate (CK-ER)

**Section:** ASR / Transcription
**Placement:** After the existing Limitations block ("Requires ground-truth keyword annotation. Keyword list must be maintained as terminology evolves."), before Novel Thinking / Implications

**⚠️ Underspecification Warning (Tier B - same standardisation gap as M-WER)**

> CK-ER depends on a clinical significance ontology defining which terms are keywords - no standardised ontology exists. The vendor or deployer implementing CK-ER chooses which terms count, and the resulting metric is only as good as that choice. Different keyword lists produce materially different CK-ER values for the same system, which prevents cross-vendor comparison and makes local benchmarks difficult to interpret. This metric sits in the same standardisation gap as M-WER: it is conceptually sound but requires national body specification of a canonical keyword ontology mapped to SNOMED safety-critical concept classes before it can be reported in a comparable way. In the interim, document the keyword dictionary used and its provenance when reporting CK-ER.

---

# 9. Cognitive Load Assessment

**Section:** Human Factors & Workflow
**Placement:** After the existing Limitations block ("Self-report. Adds burden."), before Novel Thinking / Implications

**⚠️ Underspecification Warning (Tier B - generic validation, no AVT-specific calibration)**

> NASA-TLX is validated generically with acceptable individual-setting ICC of 0.71–0.81 (lower for group settings). However, for AVT specifically: no subscale selection protocol exists, no consensus on measurement timing (during encounter / immediately after charting / end of day / end of week), no documentation-specific adaptation of the instrument, and no established thresholds for "acceptable" cognitive load in AVT review tasks. The 60.7% reduction in composite cognitive load reported in a 2024 Abridge study is a point estimate with no reference scale for clinical interpretation - "60% less" of an undefined baseline is not directly actionable. Use NASA-TLX as an interim measure, specify the timing and subscale selection used, and avoid comparing raw scores across studies that use different protocols. The proposed **Verification Burden** metric (Human Factors & Workflow) is intended to capture a more specific construct that may ultimately prove more actionable than global cognitive load.

---

# 10. Trust Calibration Survey

**Section:** Human Factors & Workflow
**Placement:** After the existing Limitations block ("Self-report bias. Must triangulate with behavioural metrics."), before Novel Thinking / Implications

**⚠️ Underspecification Warning (Tier B - concept defined, no AVT-validated instrument)**

> Multiple candidate instruments exist for trust calibration in clinical AI (TIAS, HATAS, AITI-H), but **none are validated specifically for ambient scribe contexts**. A 2024 Dokkyo Medical University review concluded that there are currently no accurate and objective measures available for evaluating trust calibration in clinical AI deployments. No thresholds exist for defining "appropriately calibrated" trust, and no empirical integration has been established between subjective trust measures and behavioural proxies (edit rate, review time, error detection) that would allow triangulation. Adapt TIAS or HATAS for AVT context as an interim measure, document the adaptation explicitly, and flag the absence of formal validation when reporting results. Pair with the existing behavioural complacency indicators (Edit Rate, Time-to-Sign, Review-Before-Signing) rather than relying on the survey instrument alone.

---

# 11. Automation Bias Detection (Error Injection)

**Section:** Human Factors & Workflow
**Placement:** After the existing Limitations block ("Ethical complexity. Must ensure errors intercepted before permanent record."), before Novel Thinking / Implications

**⚠️ Underspecification Warning (Tier B - strong concept, ad hoc protocols)**

> Automation bias is well-defined conceptually (Parasuraman & Manzey, *Human Factors* 2010) but measurement protocols in clinical AI remain ad hoc. Most published studies use vignette-based designs comparing diagnostic accuracy with and without AI assistance; there is no standardised measurement protocol for production AVT systems operating under real clinical time pressure. No consensus exists on acceptable automation bias rate thresholds - one computational pathology study reported a 7% rate without specifying whether that was concerning or within expected bounds for the task. An active RCT (NCT07328815) is testing nudge interventions but results are not yet available. Until standardised production protocols emerge, document explicitly: (a) the injection methodology (how errors are generated), (b) the injection rate, (c) the severity distribution of injected errors, (d) the detection criteria (what counts as "caught"), (e) the timing of assessment. Changes to any of these make values incomparable across audits.

---

# 12. Trust Halo Decay Rate

**Section:** Human Factors & Workflow
**Placement:** After the existing Limitations block ("Longitudinal measurement required."), before Novel Thinking / Implications

**⚠️ Underspecification Warning (Tier A - no validated measurement in clinical AI)**

> The trust halo effect is well-established in cognitive psychology but has **not been operationalised for clinical AI or AVT specifically**. The concept substantially overlaps with automation bias, and the empirical boundary between the two constructs is not established - it is unclear whether they should be measured as distinct phenomena or as facets of a common over-reliance construct. No validation studies exist. No measurement instruments have been adapted from cognitive psychology to the clinical AI context. Two viable paths forward: (a) define a specific experimental paradigm (e.g. testing whether positive experience with transcription accuracy transfers uncritically to trust in clinical summarisation accuracy, which is a different capability) and build validation evidence from there, or (b) fold the construct into the broader automation bias / over-reliance family until the measurement science matures enough to distinguish it meaningfully. Until one of these is done, any reported values should carry explicit acknowledgement of the definitional uncertainty.

---

# 13. Note Review Fatigue Trajectory

**Section:** Human Factors & Workflow
**Placement:** After the existing Limitations block ("Confounded with case mix variation..."), before Novel Thinking / Implications

**⚠️ Underspecification Warning (Tier A - underlying concept unoperationalised)**

> The broader concept of attention drift across a clinician's reviewing session has **no operationalised definition in AVT literature**. The Cognitive Drift Index (Frontiers in Neuroscience 2025) measures information consumers' judgment shifts in unrelated domains, not clinician review vigilance. A 2026 KevinMD essay described "the slow erosion of clinical humility" qualitatively but offered no measurement approach. No published study has established a detection methodology, thresholds, or relationship to patient safety outcomes. Proposed interim operationalisation for this taxonomy - to be treated as a working definition pending empirical validation - is a composite of (a) declining review time per note over a session, (b) reduced edit rate trajectory within sessions, and (c) reduced error detection rate in periodic injection testing stratified by time-of-session. This proposal has not been validated; deployers using it should document the operational definition applied and treat results as exploratory rather than diagnostic.

---

# 14. Off-Label Use Detection Rate

**Section:** Safety & Governance
**Placement:** After the existing Limitations block ("Requires clear validated envelope definition."), before Novel Thinking / Implications

**⚠️ Underspecification Warning (Tier A - no established methodology)**

> Off-label use of AVT has **no established detection methodology** in the published literature. The concept borrows from pharmaceutical regulation, but AVT "indicated use" boundaries are rarely defined precisely enough to determine when specific use is off-label. A 2025 Morgan Lewis legal analysis highlighted the liability risk but provided no detection framework. No use-case taxonomy exists to define intended vs off-label boundaries. No monitoring approach has been proposed in peer-reviewed literature. This metric requires definitional work before operational implementation is possible: deployers should, in collaboration with vendors, specify the validated use envelope (specialties, patient populations, acuity levels, languages, consultation modes) and build usage-pattern monitoring against that envelope rather than attempting to measure "off-label use" as an isolated concept. Consider operationalising as the proposed **Work-as-Imagined vs Work-as-Done Gap** metric (Human Factors & Workflow) which provides a more structured framework for detecting adaptation, workaround, and scope creep.

---

# 15. Clinical Decision Equivalence

**Section:** End-to-End Pipeline
**Placement:** After the existing Limitations block ("Extremely resource-intensive..."), before Novel Thinking / Implications

**⚠️ Underspecification Warning (Tier B - conceptually essential, operationally impractical)**

> Clinical Decision Equivalence is conceptually the most important metric in the taxonomy for distal outcome validation - it directly tests whether AVT-generated notes support the same clinical decisions as direct observation, which is what AVT ultimately needs to do to be safe. But measurement methodology is extremely resource-intensive: blinded clinical decision-making from multiple clinicians per case, inter-clinician variation adding noise, simulated decision contexts differing from real-world behaviour under time pressure. No validated protocol exists. No threshold for "adequate equivalence" has been established. Best interpreted as a target for national or academic evaluation programmes rather than deployer-level assessment. When operationalised, the study design must specify: (a) number of clinicians per case and selection criteria; (b) blinding methodology and how information leakage is prevented; (c) decision categories assessed (diagnostic, therapeutic, safety-netting, follow-up); (d) agreement metric (kappa, per-category accuracy, weighted agreement); (e) clinical complexity stratification; (f) handling of inter-clinician disagreement in the ground-truth condition.

---

# Integration notes

**Where to add these to the Summary section.** The existing Summary section has a "By Maturity" breakdown (Established / Emerging / Vendor-Proprietary / Proposed / Novel). I'd recommend adding a parallel "Underspecification Flags" breakdown after this, with three numbers: "Tier A (no methodology): 3 metrics · Tier B (no AVT validation): 7 metrics · Tier C (clinical validity unproven): 5 metrics". This gives readers a quick read on where the measurement-science gaps sit without having to scan every entry.

**Hallucination Rate special case.** Hallucination Rate is currently Tier 1 (Minimum Viable) in the taxonomy. The Tier B underspecification warning does not invalidate that tier assignment - the metric is essential to measure even though its definition is unstable - but readers of the Tier 1 Quick Reference should see the warning. Consider adding a brief flag to the Tier 1 Quick Reference entry for Hallucination Rate: "⚠️ See underspecification warning in full entry - definition is not yet standardised".

**Cross-references to the new metrics.** Several warnings reference new metrics from the drafting batches (Accent Taxonomy Standardisation, LLM-Judge Bias Quantification, Verification Burden, Work-as-Imagined vs Work-as-Done Gap). Those cross-references only work after the new metrics are integrated - if this pass is applied before the new-metric integration, the cross-references will need to be placeholder text or removed temporarily.

**Tier A metrics as candidates for deprecation or reframing.** Off-Label Use Detection Rate, Trust Halo Decay Rate, and Note Review Fatigue Trajectory are all Tier A - they have no established methodology. Worth considering whether to (a) keep them as aspirational markers of gaps the field needs to fill, or (b) deprecate them from the operational taxonomy and move them into a separate "Research frontier" appendix. I've kept them in place because their presence surfaces the gaps visibly, but that's a judgement call you may want to revisit when you do pass 3.

---

**Pass 2 complete: 15 underspecification warnings drafted.**

Next passes available:
- **Pass 1** (consolidation framings - four parent-construct paragraphs for Clinical Content Fidelity, Post-Generation Correction, Clinical Transcription Accuracy, Reference-Based Text Similarity)
- **Pass 3** (cross-cutting additions - ACI Bench / PriMock resource gap callout, Summary and Tier 1 Quick Reference updates, new-group introductory paragraphs for NHS Compliance & Regulatory and Environmental & Sustainability)
