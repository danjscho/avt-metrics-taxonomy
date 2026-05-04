### TP.DI-1 🟡 Diarisation Error Rate (DER)

Proportion of audio time with incorrect speaker labels. Combines missed speech, false alarm, and speaker confusion.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.DI-1 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Diarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | [Wang-ADS-Eval-2025]; standard diarisation literature |

**Why this tier?**

> Vendor pre-deployment metric. Deployer should request results, especially for multi-party scenarios relevant to their clinical context.

**Formal Definition**

```
DER = (FA + MISS + SPKR_ERR) / TOTAL. FA = false alarm time, MISS = missed speech, SPKR_ERR = speaker confusion. Optionally with 0.25s collar tolerance. NIST md-eval is the standard scorer.
```

**Code: DER via pyannote**

```python
from pyannote.metrics.diarization import DiarizationErrorRate

metric = DiarizationErrorRate(collar=0.25)
der = metric(reference_annotation, hypothesis_annotation)
# Returns: {'diarization error rate': 0.12,
#            'false alarm': 0.03,
#            'missed detection': 0.04,
#            'confusion': 0.05}
```

**References**

- **Scoring tool**: [dscore-Ryant]
- **SCRIBE**: [Wang-ADS-Eval-2025]

**Limitations**

> Challenging in multi-party consultations. Most benchmarks assume two speakers.

**⚠️ Underspecification Warning (Tier C - standard methodology, absent clinical context)**

> DER has a rigorous technical definition (NIST RT evaluation protocol). The dominant non-clinical diarisation benchmarks are AMI (multi-party meeting audio) and CALLHOME (telephone conversation); reported SOTA DER values vary widely by system, decoder, collar, and protocol — see published diarisation surveys for specific configurations rather than treating any single number as canonical. **No clinical-specific benchmarks exist** for the multi-party consultations routinely encountered in NHS practice. No validated link has been established between DER and downstream clinical documentation quality — a low DER does not guarantee accurate speaker attribution on clinically significant utterances, and a moderate DER may be acceptable if the errors concentrate on non-clinical content. Word-level DER (WDER) is more clinically relevant than time-based DER but is rarely reported by vendors. Require WDER from vendors and request reporting stratified by utterance type: clinician instruction, patient symptom report, family contextual information, medication discussion. The aggregate DER number in isolation is technically correct but clinically uninterpretable.

---

### TP.DI-2 🟡 Speaker Attribution Accuracy

Percentage of utterances assigned to correct speaker. Misattributed medication instructions directly cause prescribing errors.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.DI-2 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Diarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | [Wang-ADS-Eval-2025] |

**Why this tier?**

> Vendor pre-deployment. Safety-critical for medication attribution but deployer cannot independently measure.

**Formal Definition**

```
SAA = |U_correct| / |U_total|. Unlike DER (time-based), SAA is utterance-based. Compute separately for medication-related utterances: SAA_med.
```

**References**

- **SCRIBE**: [Wang-ADS-Eval-2025]

**Limitations**

> Multi-party scenarios poorly benchmarked.

**Novel Thinking / Implications**

> 💡 Medication instruction misattribution (patient reports vs clinician prescribes) deserves separate measurement as a safety-critical sub-class.

---

### TP.DI-3 🟡 Speaker Count Accuracy

Does the system correctly identify how many speakers are present? Particularly important for distinguishing 2-speaker (validated) from 3+-speaker (out-of-envelope) consultations. Over-counting fragments single speakers; under-counting merges distinct speakers.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.DI-3 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Diarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Standard diarisation evaluation |

**Why this tier?**

> Vendor pre-deployment metric. Important for any deployer routinely operating with multi-party consultations.

**Formal Definition**

```
Speaker Count Accuracy = |encounters_with_correct_count| / |total_encounters|. Detailed: |estimated_speakers - actual_speakers|. Mean Absolute Error preferred over binary accuracy.
```

**Limitations**

> Speaker count is often unknown in advance and itself estimated. Multiple ground truth annotators may disagree on speaker count for marginal cases.

**Novel Thinking / Implications**

> 💡 Speaker count is the gateway to multi-party robustness. If the system thinks there are 2 speakers when there are actually 3 (interpreter, family member), the third speaker's content is misattributed to one of the others - silently changing the clinical meaning of utterances.

---

### TP.DI-4 🔵 Speaker Boundary Precision

Temporal accuracy of where one speaker stops and another starts. Affects attribution at turn boundaries - words at the edge of a turn may be attributed to the wrong speaker.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.DI-4 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Diarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Standard diarisation literature |

**Why this tier?**

> Vendor research metric. Important for understanding diarisation quality but not directly actionable by deployers.

**Formal Definition**

```
Boundary Precision = mean temporal error (ms) between predicted and actual speaker change points. Report as distribution. NIST scoring uses 250ms collar; tighter collars expose boundary precision better.
```

**Limitations**

> Precise boundary annotation is labour-intensive. Inter-annotator agreement on exact boundaries is itself imperfect.

**Novel Thinking / Implications**

> 💡 Boundary errors are the most common cause of speaker attribution errors at turn boundaries. The first or last word of a turn is the most likely to be misattributed - and often these are the words that carry clinical meaning ('yes' to a question about symptoms, 'no' to a question about allergies).

---

---

### Conversation Analysis sub-cluster

*Multi-role identification, code-switching, turn-taking in overlap, addressee recognition, and clinically weighted attribution. Extends the existing diarisation metrics (which focus on speaker counts and boundaries) into the semantics of multi-party clinical dialogue.*

---

### TP.DI-5 🟡 Speaker Role Identification F1

Accuracy of classifying speakers into clinical roles - clinician, patient, family member, nurse, interpreter, student - rather than just distinguishing anonymous speakers. Distinct from the existing Speaker Attribution Accuracy metric, which measures whether an utterance is assigned to the correct speaker *given that roles are known*. Role identification is the prerequisite step.

|Dimension              |Value                                                                |
|-----------------------|---------------------------------------------------------------------|
| **Reference** | TP.DI-5 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                               |
|**Measurement Cadence**|One-off gate                                                         |
|**Pipeline Layer**     |Diarisation                                                          |
|**Assurance Question** |Safety                                                               |
|**Measurement Method** |Computational                                                        |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                       |
|**Responsible Actors** |Vendor                                                               |
|**Maturity**           |Emerging                                                             |
|**Outcome Type**       |Proximal                                                             |
|**Applicability**      |AVT-Specific                                                         |
|**Source**             |[mpathic-Clinical-ASR-Benchmark-2025]; extends standard diarisation |

**Why this tier?**

> Safety-relevant whenever AVT is used outside simple dyadic consultations. Interpreter-mediated, family-present, and multidisciplinary scenarios are common in NHS practice. Role identification errors cause medication attribution errors and epistemic status inversions (patient reports vs clinician observes).

**Formal Definition**

```
Per-role precision, recall, and F1. Role set R ⊇ {clinician, patient, family_member, nurse, interpreter, student, other}. F1_macro = mean F1 across roles. Report per-role breakdown because aggregate hides minority-role failures (interpreter role is often the lowest-performing and the most safety-critical for attribution). Taxonomy-proposed gates (require local calibration before contractual use): F1 ≥ 0.90 for clinician and patient roles; F1 ≥ 0.80 for other identified roles.

⚠️ Provenance: these specific F1 floors are taxonomy-proposed in v4.2 as starting-point gates, not externally attested. The mpathic Clinical ASR Benchmark cited in the Source row defines per-role / per-attribution evaluation methodology but does not publish specific F1 thresholds. Per the Calibration & Context principle, require local calibration against the deployment's role mix and consultation style.
```

**Limitations**

> Role identification often relies on content cues (who asks questions, who describes symptoms) rather than voice characteristics, which means errors correlate with atypical consultations - exactly where they matter most. Role-labelled ground truth is rarely available in clinical speech corpora.

**Novel Thinking / Implications**

> 💡 Role identification is more forgiving than individual speaker identification in one sense (you don't need to track specific individuals across sessions) but less forgiving in another (the consequences of confusing roles are semantic, not just attributional). A system that confuses "clinician" with "family member" in an interpreter-mediated consultation can end up attributing medication instructions to the wrong party.

---

### TP.DI-6 🟡 Code-Switching Detection Rate

Accuracy of detecting within-utterance language switching - a speaker moving between English and another language mid-sentence or across turns. Common in NHS consultations with EAL patients and interpreter-mediated encounters. Code-switching confounds ASR because most systems are trained on single-language audio and may transcribe the non-English segments as phonetically similar English, or drop them entirely.

|Dimension              |Value                                                 |
|-----------------------|------------------------------------------------------|
| **Reference** | TP.DI-6 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                |
|**Measurement Cadence**|One-off gate                                          |
|**Pipeline Layer**     |ASR / Transcription                                   |
|**Assurance Question** |Fairness & Equity                                     |
|**Measurement Method** |Computational                                         |
|**Lifecycle Phases**   |Pre-deployment                                        |
|**Responsible Actors** |Vendor                                                |
|**Maturity**           |Established                                           |
|**Outcome Type**       |Proximal                                              |
|**Applicability**      |AVT-Specific                                          |
|**Source**             |[Sitaram-Code-Switching-Survey-2019]; multilingual ASR literature|

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

---

### TP.DI-7 🟡 Turn-Taking Accuracy in Overlap

Accuracy of attributing words spoken during overlapping speech - when two or more speakers are simultaneously active. The existing Speaker Overlap Rate metric measures how much overlap occurs; this metric measures how well the system handles it when it does. Most ASR+diarisation pipelines degrade substantially in overlap, with one speaker's content being dropped or merged into the other.

|Dimension              |Value                                          |
|-----------------------|-----------------------------------------------|
| **Reference** | TP.DI-7 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                         |
|**Measurement Cadence**|One-off gate                                   |
|**Pipeline Layer**     |ASR + Diarisation                              |
|**Assurance Question** |Fidelity & Accuracy                            |
|**Measurement Method** |Computational                                  |
|**Lifecycle Phases**   |Pre-deployment                                 |
|**Responsible Actors** |Vendor                                         |
|**Maturity**           |Established                                    |
|**Outcome Type**       |Proximal                                       |
|**Applicability**      |AVT-Specific                                   |
|**Source**             |[ACL-SIGDIAL-2023]; standard overlap-aware ASR literature|

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

---

### TP.DI-8 🔵 Clinician-Preferred HEWER (cpHEWER)

Clinician-Preferred Human-Evaluated Word Error Rate. A speaker-attribution-aware variant of HEWER (Human-Evaluated Word Error Rate) that combines transcription accuracy and speaker-attribution correctness into a single metric, while ignoring non-semantic deviations (filler words, regional spellings) that don't impact comprehension. Introduced in the [mpathic-Clinical-ASR-Benchmark-2025] poster as a clinically-aware alternative to standard WER and cpWER. The taxonomy extends cpHEWER with an explicit role-weighted variant for cross-vendor comparability — see Formal Definition.

|Dimension              |Value                                       |
|-----------------------|--------------------------------------------|
| **Reference** | TP.DI-8 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research              |
|**Measurement Cadence**|One-off gate                                |
|**Pipeline Layer**     |ASR + Diarisation                           |
|**Assurance Question** |Safety                                      |
|**Measurement Method** |Computational                               |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit              |
|**Responsible Actors** |Vendor, Academic                            |
|**Maturity**           |Emerging                                    |
|**Outcome Type**       |Proximal                                    |
|**Applicability**      |AVT-Specific                                |
|**Source**             |[mpathic-Clinical-ASR-Benchmark-2025]                     |

**Why this tier?**

> Research metric. Requires both role-labelled ground truth and a clinical importance ontology - neither of which is standardised. Conceptually valuable but not operationally ready for routine deployment assessment.

**Formal Definition**

```
cpHEWER (per [mpathic-Clinical-ASR-Benchmark-2025]) counts how many semantically meaningful words are wrong OR attributed to the wrong speaker — speaker-attribution-aware HEWER. The mpathic poster does not publish category-level weights.

Taxonomy-proposed extension (v4.2): role-weighted variant cpHEWER_w = Σ(w(role, content) × error(i)) / Σ w(role, content), where w is a clinical-importance weight for the (speaker role, content type) combination. Proposed starting-point weight matrix:
  clinician medication instruction = 10.0
  clinician safety-netting        = 10.0
  patient red-flag symptom        =  9.0
  patient history                 =  5.0
  family contextual information   =  3.0
  small talk                      =  0.1

⚠️ Provenance: cpHEWER itself is mpathic's published methodology. The role-weighted variant cpHEWER_w with the specific weight matrix above is taxonomy-proposed in v4.2 as a starting-point construction for cross-vendor comparability. Without a nationally agreed matrix, every vendor's cpHEWER_w would be incomparable; this is a candidate for national body specification work. Per the Calibration & Context principle, require local calibration before contractual use.
```

**Limitations**

> The taxonomy-proposed weight matrix is inherently subjective; no standardised matrix exists. cpHEWER_w requires accurate role identification as prerequisite — compounds with Speaker Role Identification F1 errors. Benchmark datasets with the required role-and-content annotation do not exist at scale.

**Novel Thinking / Implications**

> 💡 cpHEWER is the diarisation-layer equivalent of Medical WER at the transcription layer: both attempt to weight errors by clinical consequence rather than treating all errors equally. The same standardisation gap applies - without a nationally agreed weight matrix, every vendor's cpHEWER number means something different. This is a candidate for national body specification work.

---

### TP.DI-9 🔵 Addressee Recognition Accuracy

In multi-party consultations, correctly identifying who the speaker is addressing - the patient, a specific family member, another clinician, or the room at large. Affects the pragmatic interpretation of utterances: "you should stop smoking" addressed to the patient is a clinical instruction; addressed to a family member present it is different content entirely.

|Dimension              |Value                                            |
|-----------------------|-------------------------------------------------|
| **Reference** | TP.DI-9 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research                   |
|**Measurement Cadence**|One-off gate                                     |
|**Pipeline Layer**     |Diarisation                                      |
|**Assurance Question** |Fidelity & Accuracy                              |
|**Measurement Method** |Computational                                    |
|**Lifecycle Phases**   |Pre-deployment                                   |
|**Responsible Actors** |Vendor, Academic                                 |
|**Maturity**           |Proposed / Novel                                 |
|**Outcome Type**       |Proximal                                         |
|**Applicability**      |AVT-Specific                                     |
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
