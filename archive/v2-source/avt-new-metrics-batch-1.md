# AVT Metrics Taxonomy - New Metric Entries (Batch 1)

New metrics drafted in the existing taxonomy house style, organised by target section for direct integration. Batch 1 covers Parts A and B (technical pipeline and pipeline interactions).

**Contents**
- ASR / Transcription - 2 new metrics
- Diarisation → new **Conversation Analysis** sub-cluster - 5 new metrics
- Summarisation / NLP - 4 new metrics
- Clinical Coding - 8 new metrics
- EPR Write-back - 2 new metrics

**Total this batch: 21 entries**

---

# Part A - Technical Pipeline additions

## ASR / Transcription (+2)

### 🟡 Error Transmission Rate

Proportion of ASR transcription errors that survive into the final clinical note. Distinct from end-to-end accuracy because it isolates the ASR→NLP propagation step - a system with high raw WER but strong contextual inference in the summariser can have a low transmission rate, while a system with low WER and literal summarisation can still transmit every error it makes.

|Dimension              |Value                                                                  |
|-----------------------|-----------------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 - Recommended                                                 |
|**Measurement Cadence**|Periodic audit                                                         |
|**Pipeline Layer**     |ASR + Summarisation                                                    |
|**Assurance Question** |Fidelity & Accuracy                                                    |
|**Measurement Method** |Computational                                                          |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                         |
|**Responsible Actors** |Vendor                                                                 |
|**Maturity**           |Emerging                                                               |
|**Outcome Type**       |Proximal                                                               |
|**Source**             |Anderson et al., Mayo Clinic Proceedings Digital Health, 2025 (OHSU 5-platform study found 19.5% transmission rate)|

**Why this tier?**

> Vendor metric requiring intermediate output access. Measurable when raw transcript and final note are both available for comparison. Valuable diagnostic because it distinguishes ASR-bottleneck systems from summarisation-bottleneck systems - the intervention is completely different in each case.

**Formal Definition**

```
ETR = |ASR_errors_present_in_final_note| / |ASR_errors_in_raw_transcript|. ETR = 0 means the summariser corrects every ASR error (unlikely). ETR = 1 means the summariser transmits every error unchanged. ETR > 1 is possible if summariser amplification adds errors beyond the ASR baseline. Compute per error category (numeric, drug name, negation, demographic) - the overall rate obscures category-specific failure modes.
```

**Limitations**

> Requires access to raw transcript and final note with alignment between the two. Not all vendors expose the intermediate transcript. Error categorisation requires NER infrastructure.

**Novel Thinking / Implications**

> 💡 The OHSU finding that 19.5% of ASR errors reach the final note suggests the summariser provides meaningful but imperfect error correction. The more interesting question is *which* errors transmit: if safety-critical errors transmit at higher rates than stylistic errors, the summariser is learning the wrong patterns. Transmission rate disaggregated by error category is more useful than the aggregate.

-----

### 🟡 ASR Confidence Exposure

Whether the ASR system exposes per-token or per-segment confidence scores to downstream consumers - both the summariser and the clinician reviewing. Different from the existing ASR Confidence Calibration metric, which asks whether confidence scores are *accurate*. Exposure asks whether they are *available at all*. Well-calibrated confidence locked inside the vendor's infrastructure provides no downstream benefit.

|Dimension              |Value                                                           |
|-----------------------|----------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 - Recommended                                          |
|**Measurement Cadence**|One-off gate                                                    |
|**Pipeline Layer**     |ASR / Transcription                                             |
|**Assurance Question** |Safety                                                          |
|**Measurement Method** |Human Review                                                    |
|**Lifecycle Phases**   |Pre-deployment                                                  |
|**Responsible Actors** |Vendor                                                          |
|**Maturity**           |Proposed / Novel                                                |
|**Outcome Type**       |Proximal                                                        |
|**Source**             |Derived from Abridge Linked Evidence architecture; confidence-based routing literature|

**Why this tier?**

> Pre-deployment architectural question. Should be a procurement requirement for any AVT system where confidence-based review routing or uncertainty display is intended. Without exposure, the rest of the confidence-based safety architecture cannot be built.

**Formal Definition**

```
Exposure assessed on three levels: (1) Internal - confidence scores exist but are not exposed; (2) Downstream - confidence scores passed to summariser for internal use; (3) Clinician-visible - low-confidence segments highlighted in the review interface. Target: Level 3 for any safety-critical deployment. Binary per level; report highest level achieved.
```

**Limitations**

> End-to-end neural ASR systems may produce confidence scores that are poorly calibrated (see existing ASR Confidence Calibration metric). Exposure without calibration can be actively misleading - a clinician seeing "95% confidence" on a 70%-accurate segment has worse situational awareness than a clinician seeing no score at all.

**Novel Thinking / Implications**

> 💡 Confidence display is the architectural prerequisite for intelligent review. A reviewer who can see which words or segments the system is uncertain about can focus their attention there. A reviewer looking at a flat wall of text must review everything equally - which in practice means reviewing nothing carefully. Clinician-visible confidence should be a standard AVT interface element, not an advanced feature.

-----

## Diarisation - new Conversation Analysis sub-cluster (+5)

*Multi-role identification, code-switching, turn-taking in overlap, addressee recognition, and clinically weighted attribution. Extends the existing diarisation metrics (which focus on speaker counts and boundaries) into the semantics of multi-party clinical dialogue.*

### 🟡 Speaker Role Identification F1

Accuracy of classifying speakers into clinical roles - clinician, patient, family member, nurse, interpreter, student - rather than just distinguishing anonymous speakers. Distinct from the existing Speaker Attribution Accuracy metric, which measures whether an utterance is assigned to the correct speaker *given that roles are known*. Role identification is the prerequisite step.

|Dimension              |Value                                                                |
|-----------------------|---------------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 - Recommended                                               |
|**Measurement Cadence**|One-off gate                                                         |
|**Pipeline Layer**     |Diarisation                                                          |
|**Assurance Question** |Safety                                                               |
|**Measurement Method** |Computational                                                        |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                       |
|**Responsible Actors** |Vendor                                                               |
|**Maturity**           |Emerging                                                             |
|**Outcome Type**       |Proximal                                                             |
|**Source**             |mpathic.ai clinical ASR benchmark 2025; extends standard diarisation |

**Why this tier?**

> Safety-relevant whenever AVT is used outside simple dyadic consultations. Interpreter-mediated, family-present, and multidisciplinary scenarios are common in NHS practice. Role identification errors cause medication attribution errors and epistemic status inversions (patient reports vs clinician observes).

**Formal Definition**

```
Per-role precision, recall, and F1. Role set R ⊇ {clinician, patient, family_member, nurse, interpreter, student, other}. F1_macro = mean F1 across roles. Report per-role breakdown because aggregate hides minority-role failures (interpreter role is often the lowest-performing and the most safety-critical for attribution). Require minimum 0.90 F1 for clinician and patient roles; 0.80 for other identified roles.
```

**Limitations**

> Role identification often relies on content cues (who asks questions, who describes symptoms) rather than voice characteristics, which means errors correlate with atypical consultations - exactly where they matter most. Role-labelled ground truth is rarely available in clinical speech corpora.

**Novel Thinking / Implications**

> 💡 Role identification is more forgiving than individual speaker identification in one sense (you don't need to track specific individuals across sessions) but less forgiving in another (the consequences of confusing roles are semantic, not just attributional). A system that confuses "clinician" with "family member" in an interpreter-mediated consultation can end up attributing medication instructions to the wrong party.

-----

### 🔵 Clinical-Perspective HEWER (cpHEWER)

Hypothesis-Error Word Error Rate weighted by clinical importance of the utterance speaker-and-content combination. An error on a clinician's medication instruction is weighted much higher than an equivalent error on a family member's small-talk contribution. Introduced in the mpathic.ai benchmark as a clinically-aware alternative to standard diarisation error rate.

|Dimension              |Value                                       |
|-----------------------|--------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research              |
|**Measurement Cadence**|One-off gate                                |
|**Pipeline Layer**     |ASR + Diarisation                           |
|**Assurance Question** |Safety                                      |
|**Measurement Method** |Computational                               |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit              |
|**Responsible Actors** |Vendor, Academic                            |
|**Maturity**           |Emerging                                    |
|**Outcome Type**       |Proximal                                    |
|**Source**             |mpathic.ai clinical ASR benchmark 2025      |

**Why this tier?**

> Research metric. Requires both role-labelled ground truth and a clinical importance ontology - neither of which is standardised. Conceptually valuable but not operationally ready for routine deployment assessment.

**Formal Definition**

```
cpHEWER = Σ(w(role, content) × error(i)) / Σ w(role, content), where w is the clinical importance weight for the (speaker role, content type) combination. Weight matrix: clinician medication instruction = 10.0; clinician safety-netting = 10.0; patient red-flag symptom = 9.0; patient history = 5.0; family contextual information = 3.0; small talk = 0.1. Matrix requires clinical consensus.
```

**Limitations**

> Weight matrix is inherently subjective. No standardised matrix exists. Requires accurate role identification as prerequisite - compounds with Speaker Role Identification F1 errors. Benchmark datasets with the required role-and-content annotation do not exist at scale.

**Novel Thinking / Implications**

> 💡 cpHEWER is the diarisation-layer equivalent of Medical WER at the transcription layer: both attempt to weight errors by clinical consequence rather than treating all errors equally. The same standardisation gap applies - without a nationally agreed weight matrix, every vendor's cpHEWER number means something different. This is a candidate for national body specification work.

-----

### 🟡 Code-Switching Detection Rate

Accuracy of detecting within-utterance language switching - a speaker moving between English and another language mid-sentence or across turns. Common in NHS consultations with EAL patients and interpreter-mediated encounters. Code-switching confounds ASR because most systems are trained on single-language audio and may transcribe the non-English segments as phonetically similar English, or drop them entirely.

|Dimension              |Value                                                 |
|-----------------------|------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 - Recommended                                |
|**Measurement Cadence**|One-off gate                                          |
|**Pipeline Layer**     |ASR / Transcription                                   |
|**Assurance Question** |Fairness & Equity                                     |
|**Measurement Method** |Computational                                         |
|**Lifecycle Phases**   |Pre-deployment                                        |
|**Responsible Actors** |Vendor                                                |
|**Maturity**           |Established                                           |
|**Outcome Type**       |Proximal                                              |
|**Source**             |IJCAI-22 multi-party conversation survey; multilingual ASR literature|

**Why this tier?**

> Vendor pre-deployment characterisation. Important for any NHS deployment serving linguistically diverse populations. Should be a procurement question for practices with significant EAL populations.

**Formal Definition**

```
Per utterance with code-switching: (1) detected that switching occurred (binary); (2) correctly identified the secondary language (classification); (3) transcribed both-language segments accurately. Detection Rate = |correctly_detected_switches| / |total_switches|. Transcription Accuracy Post-Switch = per-language WER for non-English segments.
```

**Limitations**

> Requires evaluation data with annotated code-switching, which is rare. Most clinical speech corpora are monolingual. NHS-representative multilingual clinical speech does not exist as a public benchmark.

**Novel Thinking / Implications**

> 💡 Code-switching is a genuine equity dimension distinct from accent. A patient with fluent English who occasionally uses terms from their first language for culturally specific concepts (family roles, traditional remedies, culturally defined symptoms) should have those terms captured, not erased. A system that silently drops non-English tokens is performing lossy documentation with equity implications - and the clinician reviewing the note has no signal that anything was lost.

-----

### 🟡 Turn-Taking Accuracy in Overlap

Accuracy of attributing words spoken during overlapping speech - when two or more speakers are simultaneously active. The existing Speaker Overlap Rate metric measures how much overlap occurs; this metric measures how well the system handles it when it does. Most ASR+diarisation pipelines degrade substantially in overlap, with one speaker's content being dropped or merged into the other.

|Dimension              |Value                                          |
|-----------------------|-----------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 - Recommended                         |
|**Measurement Cadence**|One-off gate                                   |
|**Pipeline Layer**     |ASR + Diarisation                              |
|**Assurance Question** |Fidelity & Accuracy                            |
|**Measurement Method** |Computational                                  |
|**Lifecycle Phases**   |Pre-deployment                                 |
|**Responsible Actors** |Vendor                                         |
|**Maturity**           |Established                                    |
|**Outcome Type**       |Proximal                                       |
|**Source**             |ACL SIGDIAL 2023; standard overlap-aware ASR literature|

**Why this tier?**

> Vendor pre-deployment metric. Important for consultations with interruptions, family participation, or MDT discussions. Deployers should request overlap-specific evaluation results as part of procurement.

**Formal Definition**

```
TTA-O = |words_correctly_attributed_in_overlap| / |total_words_in_overlap|. Report alongside speaker overlap rate to contextualise. Compare with TTA-NonOverlap to quantify overlap-specific degradation: Overlap Degradation = TTA-NonOverlap - TTA-O. Values > 10 percentage points indicate the system handles overlap poorly.
```

**Limitations**

> Ground truth for overlapping speech is labour-intensive to annotate. Gold-standard transcripts of overlap often disagree among annotators. Detection of overlap segments is itself error-prone.

**Novel Thinking / Implications**

> 💡 Real clinical consultations contain 5-15% overlap. If the system handles overlap poorly and simply attributes the whole overlap to one speaker, the content from the "losing" speaker is silently dropped. A patient's quiet objection during a clinician's explanation ("but I can't afford that") may be lost entirely, with neither the clinician nor the review process aware it happened.

-----

### 🔵 Addressee Recognition Accuracy

In multi-party consultations, correctly identifying who the speaker is addressing - the patient, a specific family member, another clinician, or the room at large. Affects the pragmatic interpretation of utterances: "you should stop smoking" addressed to the patient is a clinical instruction; addressed to a family member present it is different content entirely.

|Dimension              |Value                                            |
|-----------------------|-------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research                   |
|**Measurement Cadence**|One-off gate                                     |
|**Pipeline Layer**     |Diarisation                                      |
|**Assurance Question** |Fidelity & Accuracy                              |
|**Measurement Method** |Computational                                    |
|**Lifecycle Phases**   |Pre-deployment                                   |
|**Responsible Actors** |Vendor, Academic                                 |
|**Maturity**           |Proposed / Novel                                 |
|**Outcome Type**       |Proximal                                         |
|**Source**             |Multi-party dialogue research; pragmatics literature|

**Why this tier?**

> Research frontier. No current AVT system explicitly models addressee. Academic research area - cannot be deployed in routine assessment today.

**Formal Definition**

```
For each utterance u in multi-party encounter: addressee(u) ∈ {patient, family_member_1, family_member_2, clinician, room}. Accuracy = |correctly_identified_addressee| / |total_utterances_in_multi_party_segments|. Requires turn-level annotation of addressee identity.
```

**Limitations**

> Addressee is often ambiguous even to humans - clinicians frequently address statements to "the room" without a specific target. Annotation inter-rater reliability is low. Technical solutions require multimodal input (gaze, body orientation) not available from audio alone.

**Novel Thinking / Implications**

> 💡 Addressee recognition is the pragmatic layer above speaker attribution. When a clinician turns to a family member and says "make sure she takes these at the same time each day", the instruction is for the family member, not the patient. If the AVT attributes this to the patient, the resulting note reads as a patient-directed instruction that the patient may not have even heard clearly. This kind of pragmatic misattribution is invisible to diarisation error rate but directly affects clinical documentation accuracy.

-----

## Summarisation / NLP additions (+4)

### 🟡 Temporal Event Ordering Accuracy

Accuracy of reconstructing the chronological sequence of clinical events from non-linear conversation. Patients rarely describe symptoms in temporal order - they jump between current symptoms, historical episodes, family history, and future concerns. The summary must impose a coherent timeline. Distinct from the existing Temporal Accuracy metric, which covers tense and time-marker preservation at the sentence level; this metric covers event sequencing across the whole note.

|Dimension              |Value                                                   |
|-----------------------|--------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 - Recommended                                  |
|**Measurement Cadence**|Periodic audit                                          |
|**Pipeline Layer**     |Summarisation                                           |
|**Assurance Question** |Safety                                                  |
|**Measurement Method** |Hybrid                                                  |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                          |
|**Responsible Actors** |Vendor, Deployer                                        |
|**Maturity**           |Emerging                                                |
|**Outcome Type**       |Proximal                                                |
|**Source**             |i2b2 2012 temporal challenge (F1 0.876 state of art); clinical temporal reasoning literature|

**Why this tier?**

> Important clinical reasoning dimension. Established benchmark methodology exists (i2b2). Periodic audit feasible with annotated test cases.

**Formal Definition**

```
Given a set of clinical events E extracted from source, and their true temporal ordering T_ref, compute the summary's inferred ordering T_hyp. Accuracy = Kendall's tau between T_ref and T_hyp. Report: pairwise ordering accuracy (what proportion of event pairs are correctly ordered), plus anchor events accuracy (events with absolute timestamps correctly placed).
```

**Limitations**

> Ground truth temporal annotation is labour-intensive. Some event orderings are legitimately ambiguous (patient doesn't remember). Automated temporal extraction for evaluation adds its own error.

**Novel Thinking / Implications**

> 💡 Event ordering is the difference between "patient had MI, then developed chest pain" and "patient developed chest pain, then had MI". Same events, completely different clinical meaning. Summarisation LLMs frequently collapse temporal structure when compressing, producing notes where causality is implied by proximity rather than by explicit ordering.

-----

### 🟡 Medication Attribute Extraction F1

Per-attribute accuracy for each component of a medication reference: drug name, dose, route, frequency, duration, indication, and start/stop dates. Each attribute is scored independently with its own F1. The medication as a whole is only fully correct if all attributes are correct - and aggregate medication accuracy masks systematic attribute-level failures (e.g. systems that get drug names right but frequencies wrong).

|Dimension              |Value                                                        |
|-----------------------|-------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 - Recommended                                       |
|**Measurement Cadence**|Periodic audit                                               |
|**Pipeline Layer**     |Summarisation                                                |
|**Assurance Question** |Safety                                                       |
|**Measurement Method** |Computational                                                |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                               |
|**Responsible Actors** |Vendor                                                       |
|**Maturity**           |Established                                                  |
|**Outcome Type**       |Proximal                                                     |
|**Source**             |n2c2 shared task benchmarks (attribute-level F1 >0.92 for strong systems)|

**Why this tier?**

> Established methodology. Should be a standard vendor pre-deployment metric. Periodic re-testing captures drug vocabulary currency.

**Formal Definition**

```
For each medication mention m with attributes A = {name, dose, route, frequency, duration, indication}: per-attribute precision and recall against reference. Composite: full-match rate = |medications_all_attributes_correct| / |total_medications|. Safety-critical: dose accuracy and frequency accuracy should be reported with CIs; any system below 0.95 on these should not deploy without enhanced review.
```

**Limitations**

> Requires NER infrastructure mapping to dm+d and SNOMED medication concepts. Annotation is labour-intensive. Free-text dosing instructions ("take as needed", "titrate to response") are harder to score than structured doses.

**Novel Thinking / Implications**

> 💡 Aggregate medication accuracy is a misleading single number. A system with 95% medication accuracy could be getting drug names right 99% of the time and doses right 92% of the time - and the 8% dose error rate is the safety-critical finding. Attribute-level breakdown is necessary for safety assurance.

-----

### 🟡 Medication Event Classification

Classification of medication *actions* discussed in a consultation: start, stop, increase, decrease, continue, hold, restart, allergy/contraindication. Distinct from medication attribute extraction, which captures what the medication is; event classification captures what is being *done* with it. A medication mentioned as "we'll stop this one" is not the same as "we'll keep this one" - the attributes may be identical but the clinical action is opposite.

|Dimension              |Value                                              |
|-----------------------|---------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 - Recommended                             |
|**Measurement Cadence**|Periodic audit                                     |
|**Pipeline Layer**     |Summarisation                                      |
|**Assurance Question** |Safety                                             |
|**Measurement Method** |Computational                                      |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                     |
|**Responsible Actors** |Vendor                                             |
|**Maturity**           |Established                                        |
|**Outcome Type**       |Proximal                                           |
|**Source**             |n2c2 2018 shared task on medication event classification|

**Why this tier?**

> Established methodology. Safety-critical because event misclassification directly causes prescribing errors. Should be standard vendor pre-deployment reporting.

**Formal Definition**

```
For each medication event discussed: classification into {start, stop, increase, decrease, continue, hold, restart, contraindication, refuse}. Multiclass F1 per class. Safety-critical confusions: start↔stop and increase↔decrease are the most dangerous failure modes. Report confusion matrix, not just aggregate accuracy.
```

**Limitations**

> Implicit medication events (not explicitly stated but inferred from context) are harder to classify than explicit statements. Conditional events ("stop this if symptoms worsen") require understanding conditional structure.

**Novel Thinking / Implications**

> 💡 The start↔stop confusion is the canonical AVT safety nightmare. A consultation discussion of "we're going to stop your warfarin and start apixaban instead" that is silently inverted by the summariser produces a note that documents starting warfarin and stopping apixaban - both incorrect, both dangerous, and neither flagged by attribute-level accuracy metrics. Event classification should be a mandatory safety gate.

-----

### 🟡 Stigmatising Language Replication Rate

Proportion of AI-generated notes that reproduce biased or stigmatising language patterns learned from training data. Distinct from the existing Cultural & Linguistic Appropriateness metric, which covers broader sensitivity issues. This metric specifically tracks whether the system has learned to generate language like "drug-seeking", "non-compliant", "frequent flyer", "difficult patient" - terms which research shows appear disproportionately in notes about specific patient populations.

|Dimension              |Value                                                                       |
|-----------------------|----------------------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 - Recommended                                                      |
|**Measurement Cadence**|Periodic audit                                                              |
|**Pipeline Layer**     |Summarisation                                                               |
|**Assurance Question** |Fairness & Equity                                                           |
|**Measurement Method** |Computational                                                               |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                              |
|**Responsible Actors** |Vendor, Deployer                                                            |
|**Maturity**           |Proposed / Novel                                                            |
|**Outcome Type**       |Distal                                                                      |
|**Source**             |Barcelona et al., JAMA Network Open 2025 (Black patients 2.54× odds of negative descriptors)|

**Why this tier?**

> Important fairness dimension, measurable today with a keyword/phrase dictionary plus contextual classification. Should be a standard vendor pre-deployment check and periodic audit.

**Formal Definition**

```
Stigmatising Language Rate = |notes_containing_stigmatising_terms| / |total_notes|. Dictionary based on published clinical language audit studies, updated periodically. Categories: non-adherence framing, drug-seeking framing, effort/character judgment, difficulty framing, dismissive framing. Disaggregate by patient demographics to detect bias amplification: Bias Ratio = rate_in_minority_population / rate_in_majority_population. Bias Ratio > 1.2 indicates disparate application.
```

**Code: Stigmatising language detection**

```python
STIGMATISING_LEXICON = {
    "non_adherence": ["non-compliant", "non-adherent", "refuses to",
                       "failed to comply", "poor compliance"],
    "drug_seeking": ["drug-seeking", "drug seeking", "narcotic seeking",
                      "opioid seeking"],
    "difficulty": ["difficult patient", "frequent flyer", "high utiliser",
                    "heartsink", "demanding"],
    "effort_judgment": ["not trying", "unmotivated", "poorly motivated",
                         "refuses to engage"],
    "dismissive": ["claims", "alleges", "reports pain but",
                    "supposedly", "apparently"],
}

def stigmatising_language_rate(notes, demographic_col=None):
    results = {"total": 0, "flagged": 0, "by_category": {},
               "by_demographic": {}}
    for note in notes:
        results["total"] += 1
        note_flagged = False
        for category, terms in STIGMATISING_LEXICON.items():
            if any(term in note["text"].lower() for term in terms):
                results["by_category"].setdefault(category, 0)
                results["by_category"][category] += 1
                note_flagged = True
        if note_flagged:
            results["flagged"] += 1
            if demographic_col and demographic_col in note:
                d = note[demographic_col]
                results["by_demographic"].setdefault(d, 0)
                results["by_demographic"][d] += 1
    results["rate"] = results["flagged"] / results["total"]
    return results
```

**Limitations**

> Dictionary-based detection misses novel stigmatising phrasings and over-flags legitimate uses (e.g. "non-adherent" may be clinically accurate in some contexts). Context-aware classification would be stronger but requires a trained classifier.

**Novel Thinking / Implications**

> 💡 AVT systems trained on legacy clinical notes have learned the biases present in those notes. When the same system generates notes for similar patient presentations, it reproduces the patterns. This is a quiet failure mode: the AI is faithfully reproducing exactly the language patterns the profession is trying to move away from. Detection is a necessary first step; mitigation requires vendor-side intervention in training data curation.

-----

## Clinical Coding additions (+8)

*Significant expansion from 4 to 12 metrics. Clinical coding is the single largest gap area in the current taxonomy - reflecting the rapid 2025-2026 shift in ambient scribe capability from pure note generation into automated or suggested coding, with implications for safety, revenue integrity, and data quality.*

### 🟡 SNOMED CT Concept Mapping Accuracy

Accuracy of the mapping from extracted clinical entities in free-text to the correct SNOMED CT concept ID. Distinct from the existing SNOMED Code Accuracy metric, which measures whether the assigned code is clinically correct. Concept mapping measures whether the system correctly resolves "chest pain" to the correct SNOMED concept (29857009 - chest pain) rather than a near-miss concept (102588006 - chest discomfort). The boundary between correct and near-miss is where most mapping errors occur.

|Dimension              |Value                                                                    |
|-----------------------|-------------------------------------------------------------------------|
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

-----

### 🟡 ICD-10 / ICD-11 Full-Specificity Precision

Precision of ICD coding at maximum digit specificity, reported separately from category-level accuracy. Performance typically degrades sharply at full specificity compared to 3-character category level. The Hybrid-Code v2 framework reported 93% accuracy at 3-character level but only 82% at full specificity - the difference representing systematic specificity errors that aggregate metrics hide.

|Dimension              |Value                                       |
|-----------------------|--------------------------------------------|
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

-----

### 🟡 OPCS-4 Procedure Coding Accuracy

Accuracy of OPCS-4 procedure code assignment from consultation documentation. NHS-specific - the OPCS-4 classification (Office of Population Censuses and Surveys, 4th revision) is the mandatory procedure coding standard for NHS secondary care. **No published AI benchmarks currently exist for OPCS-4 coding** despite it being essential for NHS deployment.

|Dimension              |Value                                         |
|-----------------------|----------------------------------------------|
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

-----

### 🟡 dm+d Medication Coding Accuracy

Accuracy of Dictionary of Medicines and Devices (dm+d) coding for medications discussed in consultations. NHS-specific - dm+d is the mandatory NHS medication terminology, maintained by NHS BSA, and essential for medication safety, interoperability, and prescribing workflows. **Like OPCS-4, no published AI benchmarks exist for dm+d coding**.

|Dimension              |Value                                                     |
|-----------------------|----------------------------------------------------------|
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

-----

### 🟢 Code Hallucination Rate

Rate at which the system generates codes that do not exist in the target code set. Distinct from all other coding error metrics because a non-existent code is not a "wrong" code - it is a structural error. The code looks valid syntactically but resolves to nothing. The Hybrid-Code v2 framework explicitly targeted "zero-hallucination coding" because this failure mode is both detectable and unambiguously wrong.

|Dimension              |Value                                                |
|-----------------------|-----------------------------------------------------|
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

-----

### 🟡 E/M Level Shift Monitoring

Monitoring of shifts in Evaluation & Management (E/M) coding levels pre- and post-AVT deployment. In US settings, E/M level shift has been a primary revenue impact channel; in NHS settings, the equivalent concern is SNOMED specificity shift and its effect on QOF, Hospital Episode Statistics, and population health analytics. Extension of the existing Coding Inflation Detection metric with a specific focus on tariff-relevant code distributions.

|Dimension              |Value                                                                                |
|-----------------------|-------------------------------------------------------------------------------------|
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

-----

### 🔵 wRVU / Tariff Impact Attribution

Attribution of workload or tariff-relevant coding changes to AVT specifically, separated from concurrent changes (training, policy updates, case mix shifts). Quasi-experimental methodology required. In NHS context, applies to PbR tariffs, QOF achievement, and secondary care activity-based funding.

|Dimension              |Value                                        |
|-----------------------|---------------------------------------------|
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

-----

### 🟡 Coding Equity Index

Whether AVT-driven changes in coding distribution are equitably spread across patient demographics or systematically benefit some populations more than others. If AVT improves coding completeness more for majority populations than for minority populations, it widens existing inequalities in data quality and downstream resource allocation.

|Dimension              |Value                                                 |
|-----------------------|------------------------------------------------------|
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

-----

## EPR Write-back additions (+2)

### 🟡 FHIR R4 Resource Conformance Rate

Validated conformance of generated structured data against FHIR R4 profiles. FHIR is increasingly the interoperability standard for NHS EPRs; systems that produce technically parseable but profile-non-conformant resources create silent integration failures downstream. The ADS/Harvard SPIE 2025 study reported 95% data field retention via FHIR vs ~70% for legacy formats - but retention is not the same as profile conformance.

|Dimension              |Value                                    |
|-----------------------|-----------------------------------------|
|**Priority Tier**      |🟡 Tier 2 - Recommended                   |
|**Measurement Cadence**|Continuous                               |
|**Pipeline Layer**     |EPR Write-back                           |
|**Assurance Question** |Fidelity & Accuracy                      |
|**Measurement Method** |Computational                            |
|**Lifecycle Phases**   |Pre-deployment, Continuous               |
|**Responsible Actors** |Vendor                                   |
|**Maturity**           |Established                              |
|**Outcome Type**       |Proximal                                 |
|**Source**             |FHIR R4 validation tooling; SPIE 14009E 2025 interoperability study|

**Why this tier?**

> Established methodology with open-source validators. Vendor pre-deployment requirement. Should be reported per FHIR profile used (UK Core, INTEROPen, local).

**Formal Definition**

```
For each generated FHIR resource: validate against the applicable profile using the official HL7 FHIR validator. Conformance Rate = |resources_passing_validation| / |total_resources|. Stratify by resource type (Condition, MedicationStatement, AllergyIntolerance, Observation) - failures often cluster in specific resource types. Target: 100% on safety-critical resource types.
```

**Limitations**

> Conformance to a profile does not guarantee clinical correctness - a valid but wrong medication code passes validation. Profile requirements may be under-specified for some NHS use cases.

**Novel Thinking / Implications**

> 💡 Profile conformance is a necessary but not sufficient condition for interoperability. The existing Write-back Fidelity metric measures whether content is correct; this metric measures whether the structural container is valid. Both can fail independently. A system that produces valid-but-wrong FHIR is dangerous; a system that produces right-but-invalid FHIR will fail to write-back silently.

-----

### 🔵 openEHR Archetype Conformance

Conformance of generated clinical data against openEHR archetypes for NHS trusts using openEHR-based EPR platforms. Less widespread than FHIR in UK primary care but relevant for specific secondary care deployments (particularly in mental health trusts and specialised services).

|Dimension              |Value                                     |
|-----------------------|------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research            |
|**Measurement Cadence**|Continuous                                |
|**Pipeline Layer**     |EPR Write-back                            |
|**Assurance Question** |Fidelity & Accuracy                       |
|**Measurement Method** |Computational                             |
|**Lifecycle Phases**   |Pre-deployment, Continuous                |
|**Responsible Actors** |Vendor                                    |
|**Maturity**           |Established                               |
|**Outcome Type**       |Proximal                                  |
|**Source**             |openEHR Foundation standards; Clinical Knowledge Manager archetype library|

**Why this tier?**

> Deployment context-specific. Tier 3 for most deployers but Tier 2 or even Tier 1 for trusts using openEHR-based platforms - context adjustment per the "Adapting to Local Context" section.

**Formal Definition**

```
For each generated composition: validate against the applicable openEHR archetype(s) and template(s). Report: archetype conformance rate (structural), terminology binding conformance (codes map to required terminology subset), cardinality compliance. Must validate both the composition structure and the path-based data bindings.
```

**Limitations**

> openEHR archetype validation tooling is less mature than FHIR validation. Archetype maintenance varies by trust. Cross-trust conformance may require different archetype versions.

**Novel Thinking / Implications**

> 💡 The UK has bifurcated EPR infrastructure: primary care is standardising on FHIR-based interoperability, while parts of secondary care (particularly the Code4Health-aligned trusts) have significant openEHR investment. AVT vendors focused on primary care may simply not support openEHR, making them structurally unsuitable for some secondary care deployments. This should be a procurement question rather than a post-contract discovery.

-----

# End of Batch 1

**Metrics drafted in this batch: 21**
- ASR / Transcription: 2
- Diarisation (new Conversation Analysis sub-cluster): 5
- Summarisation / NLP: 4
- Clinical Coding: 8
- EPR Write-back: 2

**Next batches (in taxonomy order)**
- Batch 2: End-to-End Pipeline (1) + Human Factors & Workflow including new Sociotechnical sub-cluster (4-5) + Patient Experience including new Clinical Outcomes sub-cluster (4) + Fairness & Equity (3) = ~13 entries
- Batch 3: Safety & Governance including Longitudinal Drift (4) + **NHS Compliance & Regulatory (new group, 10)** + Security & Adversarial Robustness (2) = ~16 entries
- Batch 4: Privacy & Data Governance (5) + Operational (3) + **Environmental & Sustainability (new group, 3)** + Vendor Transparency (1) + Meta-evaluation (2) = ~14 entries

Total after all batches: **~64 new metric entries**, consistent with the change plan's section-by-section additions.
