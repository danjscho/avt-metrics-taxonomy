## Named Metric Families

Some metrics in the taxonomy are clusters of related entries that measure facets of a shared construct. The taxonomy names these clusters as **named metric families** so the relationship is visible structurally rather than implied by adjacency in the catalogue. Family membership is recorded as a `Family` field in each member metric's dimensions table; this page is the canonical home for family-level framing prose, member lists, and cross-cluster breakdowns.

Family membership is **not** a tier, lifecycle, or applicability claim — it's a construct-level grouping. A family can span multiple clusters; members keep their original cluster placement and ref-IDs. Members are listed below in tier order then ref-ID order.

The taxonomy distinguishes two grouping kinds:

- **Named metric families** (this page) — parent-construct groupings that may span sub-clusters, with their own framing prose. Audit-enforced via the `Family` dimension.
- **Sub-clusters** — thematic groupings within an existing group, with an italic 1–2 sentence intro before the first sub-cluster member. Sub-clusters are not surfaced in CSV/JSON downloads; they live inside cluster files.

The two are deliberately different: named families are a structural taxonomy concern surfaced everywhere; sub-clusters are a within-group readability aid.

---

## Clinical Content Fidelity

**Construct:** whether the generated note faithfully represents the clinical content of the source consultation. The family decomposes hallucination, omission, confabulation, polarity reversal, and uncertainty stripping as distinct subtypes with distinct clinical implications.

**Cluster placement:** Summarisation / NLP (single-cluster).

**Why a family.** Aggregate "hallucination rate" obscures three things: (1) the existence of distinct error subtypes with different clinical implications; (2) the difference between factuality and faithfulness; (3) the reason that aggregate rates can mask serious category-specific failures. Subtypes have different root causes (ASR vs LLM vs diarisation) and different mitigations.

**Subtypes (from CREOLA + AutoscriberValidate, regrouped).** The CREOLA framework ([Asgari-Tortus-2025]) defines four hallucination subtypes — *fabrication, negation, causality, contextual* — and three omission subtypes (*current issues, past medical / family / social, information-and-plan*). Drawing on that 4+3 original plus AutoscriberValidate analysis (medRxiv 2026), this taxonomy uses the following five cross-cutting subtypes for the Clinical Content Fidelity family. Each maps onto Asgari's structure but regroups for clinical-decision-relevance and to align with dedicated downstream metrics where they exist. **The five-subtype regrouping is a v4.2 taxonomy-side framing, not Asgari's published structure** — the source-attested taxonomy is the 4+3 above.

- **Fabrication** (Asgari "fabrication") — completely invented clinical content with no basis in the source. Fictional examination findings are the canonical example. Most dangerous.
- **Context conflation** (closest to Asgari "contextual") — content misattributed between different parts of the conversation or between speakers, e.g. one patient's symptom attributed to another's discussion in a multi-encounter session. Compounds diarisation errors.
- **Incorrect negation** (Asgari "negation") — polarity reversal of a clinical assertion, e.g. "no chest pain" rendered as "chest pain". Measured by the dedicated **TP.SN-15** Negation Handling Accuracy metric in this family. Directly causes clinical harm via phantom allergies, eliminated presenting symptoms, and inverted medication instructions.
- **Speculation or inference beyond source** (closest to Asgari "causality") — plausible but unverifiable content that extends beyond what was discussed, e.g. adding a likely diagnosis the clinician never stated. The summariser is exercising clinical judgment it shouldn't.
- **Certainty inflation** (taxonomy-extension; not a dedicated CREOLA subtype) — clinician uncertainty markers ("possibly", "consistent with", "rule out") stripped from the note, converting hedged observations into definitive statements. Measured by the dedicated **TP.SN-20** Uncertainty Marker Preservation metric in this family.

Subtypes have different root causes (ASR vs LLM vs diarisation) and different mitigations. An aggregate "hallucination rate" of 2% means very different things if 90% of the errors are speculation vs if 90% are fabrications.

**Faithfulness vs factuality.** For ambient scribes, **faithfulness is the primary assurance concern** because the scribe's job is to represent the consultation, not to exercise clinical judgment. A system that silently corrects clinician errors or adds information the clinician did not state has exceeded its safe operating scope regardless of whether the resulting statement is factually true.

**Members of this family (5):**

- 🟢 **TP.SN-5** Hallucination Rate — aggregate rate; entry point to the family
- 🟢 **TP.SN-6** Omission Rate — clinically relevant source content absent from note
- 🔵 **TP.SN-7** Factual Verification — parent of TP.SN-7a/-7b sub-parts
- 🟢 **TP.SN-15** Negation Handling Accuracy — polarity-reversal detection
- 🟢 **TP.SN-20** Uncertainty Marker Preservation — certainty inflation detection

**Recommendation for measurement.** When measuring content fidelity in periodic audit, require subtype reporting rather than aggregate rate only. A single headline number hides the distribution that matters for intervention.

---

## Reference-Based Text Similarity

**Construct:** surface or semantic similarity to a reference text. Both members of this family measure linguistic similarity, not clinical correctness.

**Cluster placement:** Summarisation / NLP (single-cluster).

**Why a family.** Both metrics share a fundamental limitation that the family framing makes explicit: semantic closeness to a reference is **not** clinical correctness. A note that is closer to the reference can still be factually wrong; a note that diverges from the reference can still be clinically equivalent. Both metrics should always be reported alongside a validated clinical instrument (PDSQI-9, CREOLA, or LLM-as-a-Judge with bias quantification).

**Members of this family (2):**

- 🟡 **TP.SN-1** ROUGE Scores — n-gram overlap; surface-level
- 🔵 **TP.SN-2** BERTScore — contextual-embedding semantic similarity; better than ROUGE but shares the underlying limitation

---

## Clinical Transcription Accuracy

**Construct:** word-error-rate metrics applied at different vocabulary scopes — total transcript, medical terms, and clinical keywords — to surface errors hidden by aggregate WER.

**Cluster placement:** ASR / Transcription (single-cluster).

**Why a family.** Aggregate WER on a clinical transcript can be 5% while the medical terms within it have 20% error and a single critical-keyword error masks the whole evaluation. The family framing makes the layered evaluation explicit.

**Members of this family (3):**

- 🟡 **TP.ASR-1** Word Error Rate (WER) — aggregate transcript-level WER
- 🔵 **TP.ASR-2** Medical Word Error Rate (M-WER) — restricted to medical-terminology tokens
- 🔵 **TP.ASR-3** Clinical Keyword Error Rate (CK-ER) — restricted to safety-critical clinical keywords

---

## Post-Generation Correction

**Construct:** clinician edits to AVT output as a workflow signal — rate, type, location, and pattern. The family treats post-generation editing as a measurable workflow surface rather than just an accuracy artefact.

**Cluster placement:** Human Factors & Workflow (single-cluster).

**Why a family.** Edit rate alone is descriptive; the diagnostic value comes from the four facets together — *what is being edited, what kind of edits, where in the note, and how the pattern is changing over time*. Edit Rate is the binary entry point; the other three add diagnostic depth.

**Members of this family (4):**

- 🟢 **HL.HF-1** Edit Rate (% Notes Edited) — the binary entry-point signal
- 🟡 **HL.HF-2** Edit Type Classification — additions / deletions / modifications / structural
- 🟡 **HL.HF-7** Edit Location Distribution — *where* in the note edits concentrate
- 🔵 **HL.HF-5** Edit-Pattern Monitoring at Scale — temporal and cross-clinician edit pattern analysis

**Diagnostic shape.** Predominantly additions indicate an omission-dominant failure mode; predominantly deletions indicate a hallucination-dominant mode. Trajectory matters more than absolute value: a falling edit rate over time may reflect improving AI **or** increasing complacency — interpret alongside Review-Before-Signing Rate and Time-to-Sign Distribution to distinguish.

---

## Medication Safety Thread

**Construct:** medication information accuracy across the full pipeline, from spoken consultation to structured EPR record. Medication errors are the canonical safety-critical failure mode in clinical documentation AI.

**Cluster placement:** cross-cutting (Summarisation / NLP → Clinical Coding → Patient Experience).

**Why a family.** Unlike the other families, the Medication Safety Thread spans multiple pipeline layers and multiple groups: extraction and event classification at the summarisation layer, terminology coding at the clinical coding layer, and downstream outcome monitoring at the patient experience layer. A medication error can originate at any of these stages, and measuring only one stage gives false assurance about the others.

**The safety argument.** A medication mentioned in consultation passes through at least four processing stages before it affects patient care: (1) ASR must transcribe the drug name, dose, and frequency correctly; (2) the summariser must extract these attributes and classify the medication event (start, stop, change); (3) the clinical coder must map to the correct dm+d concept; (4) the EPR write-back must place the medication data in the correct structured field. An error at any stage propagates — and the stages are tested by different metrics in different groups. The family framing makes the end-to-end thread visible.

**Members of this family (4):**

- 🟡 **TP.SN-19** Medication Attribute Extraction F1 — per-attribute accuracy for drug name, dose, route, frequency, duration, indication
- 🟡 **TP.SN-21** Medication Event Classification — classification of medication actions (start, stop, increase, decrease, continue)
- 🟡 **TP.CC-5** dm+d Medication Coding Accuracy — mapping to NHS dm+d terminology; currency against quarterly updates
- 🔵 **IO.PX-10** Medication Error Rate Differential — downstream outcome: pre/post AVT medication error rates

---

## Demographic Equity Disaggregation

**Construct:** applying demographic disaggregation to pipeline performance, measuring whether system quality varies across population subgroups. The underlying principle is the same at every layer: compute the base metric separately for each demographic group, then quantify the gap.

**Cluster placement:** cross-cutting (ASR → Clinical Coding → End-to-End → Fairness & Equity).

**Why a family.** Disparity in AVT performance can hide in any layer: an ASR system can have lower WER on dominant-accent speech, a coder can have lower SNOMED-coding accuracy on rare-presentation queries, and end-to-end performance can degrade compoundingly across demographic intersections. The family makes the disaggregation thread visible across pipeline stages.

**Disaggregation axes.** Most family members operate on the same set of demographic variables: accent/dialect, first language, age band, sex, ethnicity, deprivation quintile, and speech characteristics (rate, volume, disorder). The specific axes depend on the base metric and available data. The NAS framework proposes a maximum 5 percentage-point gap across groups as a starting threshold.

**Members of this family (7):**

- 🟢 **TP.ASR-4** Demographic-Disaggregated WER
- 🔵 **TP.ASR-5** Speaker-Stratified WER
- 🟡 **TP.CC-9** Coding Equity Index
- 🟢 **IO.FE-1** Deployment Equity Index
- 🟡 **IO.FE-2** Accent Taxonomy Standardisation
- 🔵 **IO.FE-4** Intersectional Performance
- 🔵 **IO.FE-5** Intersectional Compound Disadvantage Score

---

## NHSE IG Attestation { #nhse-ig-attestation }

*(new in v5.4.0)*

**Construct:** documentation and operational verification that AVT deployments comply with NHS England's March 2026 Information Governance Guidance — the binding deployer-side IG framework named transitively by the FTS notice 069369-2025 ("the guidance issued by NHS England"). The family spans transparency, consent, data subject rights, and lawful processing.

**Cluster placement:** cross-cutting (Compliance & Regulatory + Privacy & Data Governance).

**Why a family.** The 10 metrics share a single underlying construct — *did the deployer operationalise NHSE IG March 2026 across the AVT lifecycle?* — but live in different clusters because the assurance-question split puts compliance attestations in GV.CR and data-governance attestations in GV.PD. Cross-cluster placement is preserved; the family framing makes the IG-attestation thread visible.

**Members of this family (11):**

- 🟢 **GV.CR-1** Patient Dissent Recording Rate — per-encounter dissent recording and respect
- 🟢 **GV.CR-2** Verbal Notification Compliance — proportion of consultations where verbal notification was delivered
- 🟢 **GV.CR-3** AI-Generated Content Labelling Compliance — labelling of AI-generated record content
- 🟢 **GV.CR-7** DPIA Template Completion Rate — structural completion of NHSE March 2026 DPIA template *(parent of GV.PD-17 sub-part)*
- 🟡 **GV.CR-13** Refusal Impact-Explanation Quality — quality of clinician explanation of how refusal affects care *(Maturity: Proposed/Novel pending piloted rubric)*
- 🟢 **GV.PD-8** Consent Verification Accuracy — lawful basis verification at the point of care
- 🟢 **GV.PD-9** Cross-Border Data Transfer Compliance — adequacy checks for any cross-border processing
- 🟢 **GV.PD-13** Privacy Notice Currency & Completeness — privacy-notice version-currency and AVT-specific content
- 🟡 **GV.PD-14** SAR Deletion-Pause Interaction — scenario test of SAR + deletion process composition
- 🟡 **GV.PD-15** Right-to-Restrict Tooling Support — UK GDPR Article 18 tooling distinct from erasure
- 🟢 **GV.PD-18** Information Asset Register Completeness — NHSE IG section 8 IAR registration with owner, lawful basis, retention, sub-processor, risk classification *(new in v5.4.0)*

**Outstanding follow-ups.** GV.CR-13's rubric remains placeholder (Maturity: Proposed/Novel) until a national pilot lands — section ref convention since v5.5.0 is *topic-cited* against [NHSE-IG-Guidance-2026-03] because the parent guidance hub does not currently expose a stable section anchor. If a stable per-section URL becomes available, member Source rows can be re-tightened to use it.

---

## PRSB Semantic Completeness & Write-back Fidelity { #prsb-semantic-completeness-and-write-back-fidelity }

*(new in v5.4.0)*

**Construct:** end-to-end write-back assurance from AVT output generation through EHR persistence — testing content fidelity, field mapping accuracy, structural FHIR conformance, and mandatory information element presence per PRSB standard and consultation type. The family spans output quality, integration correctness, and clinical adequacy of the final record.

**Cluster placement:** Downstream Write-back (single-cluster).

**Why a family.** Write-back is a stack: a record can pass structural FHIR validation but fail PRSB semantic completeness (technically interoperable, clinically inadequate); it can pass content fidelity but fail field mapping (correct content in the wrong place); it can pass all three of those and still miss the PRSB-mandatory elements that make it a good clinical record. The family framing names the layered assurance: each member tests a distinct failure mode that the others cannot catch.

**The four-stage stack:**

- **Output capture** — did the summarisation output get captured accurately in the EHR? *(Write-back Fidelity)*
- **Field placement** — are structured fields routed to the correct EHR fields? *(Field Mapping Accuracy)*
- **Structural validation** — does the EHR data conform to FHIR R4 resource schema? *(FHIR R4 Resource Conformance Rate)*
- **Clinical completeness** — are the mandatory information elements per PRSB standard present? *(PRSB Semantic Completeness)*

**Cross-framework leverage.** The family spans the write-back layer and directly addresses Regulation 17 ("good governance — adequate records") in the CQC Assessment framework, alongside DTAC C4 (interoperability), FHIR UK Core (extension conformance), and PRSB itself.

**Members of this family (4):**

- 🟢 **TP.WB-1** Write-back Fidelity — content fidelity of AVT output captured in the EHR
- 🟢 **TP.WB-3** Field Mapping Accuracy — structured field routing
- 🟡 **TP.WB-6** FHIR R4 Resource Conformance Rate — structural schema validation
- 🟢 **TP.WB-8** PRSB Semantic Completeness — mandatory information element presence per PRSB standard
