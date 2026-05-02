### PI.PP-1 🔵 Speaker-Attributed Transcript Accuracy

Combined ASR + diarisation: was the right text assigned to the right person? Neither WER nor DER alone captures this - a transcript can have low WER and low DER but still misattribute a critical utterance.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.PP-1 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR + Diarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Identified as compound metric gap - neither WER nor DER alone captures this |

**Why this tier?**

> Novel compound metric exposing multiplicative degradation invisible to WER or DER alone. Requires aligned utterance-level ground truth with both text and speaker labels.

**Formal Definition**

```
SATA = |utterances where text correct AND speaker correct| / |total utterances|. Spans ASR (was the text right?) and diarisation (was the speaker right?). A correct transcription misattributed to the wrong speaker is as dangerous as a wrong transcription. Component decomposition: if WER and DER errors are independent, SATA ≈ (1-WER) × (1-SAE), exposing multiplicative degradation invisible to either metric alone.
```

**Code: Speaker-attributed accuracy**

```python
def speaker_attributed_accuracy(utterances):
    """
    Each utterance: {ref_text, hyp_text, ref_speaker, hyp_speaker}
    Both text AND speaker must be correct for a 'pass'.
    """
    correct = 0
    for u in utterances:
        text_ok = u["ref_text"].strip().lower() == u["hyp_text"].strip().lower()
        spk_ok = u["ref_speaker"] == u["hyp_speaker"]
        if text_ok and spk_ok:
            correct += 1
    sata = correct / len(utterances) if utterances else 0
    return {
        "sata": round(sata, 4),
        "text_only_accuracy": round(
            sum(1 for u in utterances
                if u["ref_text"].strip().lower() == u["hyp_text"].strip().lower())
            / len(utterances), 4),
        "speaker_only_accuracy": round(
            sum(1 for u in utterances
                if u["ref_speaker"] == u["hyp_speaker"])
            / len(utterances), 4),
        "compound_gap": "multiplicative" 
            if sata < min(
                sum(1 for u in utterances if u["ref_text"].strip().lower()==u["hyp_text"].strip().lower())/len(utterances),
                sum(1 for u in utterances if u["ref_speaker"]==u["hyp_speaker"])/len(utterances)
            ) else "additive"
    }
```

**Limitations**

> Requires aligned utterance-level ground truth with both text and speaker labels. Most benchmarks provide one or the other.

**Novel Thinking / Implications**

> 💡 This is the first point where component metrics compound. Vendors reporting WER and DER separately can mask combined degradation. A system with 5% WER and 5% DER could have 10% speaker-attributed errors if the error populations overlap, or up to 10% if they don't. Only this combined metric reveals the actual risk.

---

### PI.PP-2 🟡 Multi-Party Conversation Robustness

Combined ASR + diarisation degradation when >2 speakers present: interpreter, family member, student, MDT. Most benchmarks assume dyadic (2-speaker) encounters.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.PP-2 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR + Diarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Identified in NHS consultation pattern analysis - interpreter-mediated, family-present, and MDT consultations are common |

**Why this tier?**

> Vendor should test and publish performance curves by speaker count. Deployers with frequent multi-party consultations (interpreters, MDT) should request this data.

**Formal Definition**

```
Robustness(n) = SATA(n speakers) / SATA(2 speakers). Values < 1.0 indicate multi-party degradation. Report per n = {2, 3, 4, 5+}. NHS consultations frequently involve 3+ parties.
```

**Limitations**

> Test scenarios with >2 speakers are expensive to construct and annotate. Real NHS multi-party audio is rarely available for benchmarking.

**Novel Thinking / Implications**

> 💡 This is the 'validated use envelope' question in acoustic form. If the system was benchmarked on 2-speaker consultations, any multi-party use is technically off-label. Vendors should publish performance curves by speaker count.

---

### PI.PP-3 🔵 Information Extraction Yield

Spans ASR + summarisation: what proportion of clinically relevant content in source audio survives through transcription AND into the generated note? Captures the combined loss from ASR errors and summarisation omissions.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.PP-3 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | ASR + Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Identified as structural gap - component metrics don't capture cross-stage information loss |

**Why this tier?**

> Requires expert annotation of source audio - expensive. Best suited for national evaluation programme or academic pilot.

**Formal Definition**

```
IEY = |clinical_items_in_note| / |clinical_items_in_audio|. Clinical items identified by expert annotation of source audio. IEY decomposes: IEY = Yield_ASR × Yield_summarisation. If ASR drops a drug name AND summarisation doesn't compensate, the loss multiplies.
```

**Code: Information extraction yield**

```python
def information_extraction_yield(
    audio_items: list[str],     # expert-annotated clinical items from audio
    transcript_items: list[str], # clinical items found in transcript
    note_items: list[str]        # clinical items found in final note
):
    """
    Two-stage yield: audio→transcript→note.
    Items matched via clinical concept normalisation.
    """
    yield_asr = len(set(audio_items) & set(transcript_items)) / len(audio_items)
    yield_summ = len(set(transcript_items) & set(note_items)) / len(transcript_items) if transcript_items else 0
    yield_e2e = len(set(audio_items) & set(note_items)) / len(audio_items)

    return {
        "yield_asr": round(yield_asr, 3),
        "yield_summarisation": round(yield_summ, 3),
        "yield_end_to_end": round(yield_e2e, 3),
        "compound_loss": round(1 - yield_e2e, 3),
        "loss_attribution": {
            "lost_at_asr": round(1 - yield_asr, 3),
            "lost_at_summarisation": round(yield_asr - yield_e2e, 3),
        }
    }
```

**Limitations**

> Requires expert annotation of source audio to establish ground truth clinical items. Expensive and subjective.

**Novel Thinking / Implications**

> 💡 The key insight: summarisation can sometimes compensate for ASR errors (inferring the right drug from context), or it can amplify them (hallucinating a plausible but wrong drug to fill the gap). IEY captures both - the net yield is what matters clinically.

---

### PI.PP-4 🔵 Noise-to-Note Resilience

Spans ASR + summarisation: how gracefully does the final note quality degrade as audio quality worsens? Tests whether the summarisation layer can compensate for degraded transcription.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.PP-4 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR + Summarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Proposed for pre-deployment testing - NHS clinical environments have variable acoustics |

**Why this tier?**

> Vendor pre-deployment testing across controlled noise levels. Deployer cannot easily measure but should request test results for relevant acoustic conditions.

**Formal Definition**

```
Resilience(SNR) = NoteQuality(SNR) / NoteQuality(clean). Tested across audio quality levels: clean, mild noise (SNR 20dB), moderate (10dB), severe (5dB), masked speech. Graceful degradation: resilience > 0.8 at moderate noise.
```

**Limitations**

> Requires controlled audio degradation testing which is rarely part of vendor validation. Real-world noise profiles (NHS waiting rooms, home visits, telephone) vary widely.

**Novel Thinking / Implications**

> 💡 NHS environments are acoustically diverse: GP consulting rooms, telephone consultations, home visits, hospital wards. A system validated in a quiet room may fail in a busy practice. Noise resilience should be part of the validated use envelope.

---

### PI.PP-5 🔵 Epistemic Status Preservation

Spans diarisation + summarisation: does the note correctly distinguish what was reported by the patient vs observed by the clinician vs inferred by the AI? 'Patient reports headache' vs 'headache noted' vs 'headache' have different clinical meanings.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.PP-5 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Diarisation + Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Identified as critical clinical documentation quality dimension not captured by existing metrics |

**Why this tier?**

> Novel metric at intersection of diarisation and summarisation. Clinically significant but measurement methodology not yet standardised.

**Formal Definition**

```
For each clinical assertion a in the note, epistemic status E(a) ∈ {patient-reported, clinician-observed, inferred, unknown}. Preservation rate = |assertions with correct E| / |total assertions|. Requires correct speaker attribution (diarisation) feeding into summarisation that maintains the distinction.
```

**Code: Epistemic status classification**

```python
EPISTEMIC_MARKERS = {
    "patient_reported": [
        "patient reports", "patient states", "patient describes",
        "complains of", "says", "reports", "history of"
    ],
    "clinician_observed": [
        "on examination", "observed", "noted", "found",
        "examination reveals", "O/E"
    ],
    "inferred": [
        "likely", "possibly", "consistent with",
        "suggestive of", "probable"
    ]
}

def classify_epistemic_status(assertion: str) -> str:
    text = assertion.lower()
    for status, markers in EPISTEMIC_MARKERS.items():
        if any(m in text for m in markers):
            return status
    return "unknown"  # no marker = ambiguous

def epistemic_preservation_rate(ref_assertions, gen_assertions):
    """Compare epistemic status in reference vs generated note."""
    correct = 0
    for ref, gen in zip(ref_assertions, gen_assertions):
        if classify_epistemic_status(ref) == classify_epistemic_status(gen):
            correct += 1
    return correct / len(ref_assertions) if ref_assertions else 0
```

**Limitations**

> Epistemic status annotation requires clinical expertise. Automated classification via markers is crude - many assertions lack explicit markers.

**Novel Thinking / Implications**

> 💡 This is clinically significant: 'patient reports chest pain' documents subjective experience; 'chest pain' in the note without qualification implies objective finding. If diarisation misattributes patient speech to clinician, the summariser may strip the 'reports' qualifier, silently changing the epistemic status. This compounds two different error types into a clinical safety risk invisible to either WER or hallucination rate.

---

### PI.PP-6 🔵 Diarisation-Stratified WER

WER computed separately for each speaker after diarisation. Captures the compound effect of diarisation errors on per-speaker accuracy measurement. A speaker whose utterances are frequently misattributed will have artificially inflated WER even if the underlying ASR is accurate.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.PP-6 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR + Diarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Compound metric exposing diarisation impact on ASR measurement |

**Why this tier?**

> Research-grade compound metric. Useful for vendor system improvement but not deployer-actionable.

**Formal Definition**

```
For each speaker s: WER_s = standard WER on utterances correctly attributed to speaker s. Compare with global WER: if WER_s >> WER_global for some speaker, diarisation errors are degrading per-speaker accuracy.
```

**Limitations**

> Requires aligned reference with both transcription and speaker labels.

**Novel Thinking / Implications**

> 💡 Reveals whether ASR errors are systematic or attribution artifacts. If patient WER is much higher than clinician WER, the question becomes: is patient speech harder to transcribe, or are patient utterances being attributed to the clinician (which would put them in the 'wrong' WER calculation)?

---

### PI.PP-7 🟡 Concept Extraction Concordance

Spans summarisation + coding: do the SNOMED codes match the clinical concepts in the free-text note? An internal consistency check that doesn't need source audio - the note and its codes should agree.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.PP-7 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation + Coding |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Proposed as automated internal consistency check - no ground truth needed |

**Why this tier?**

> Uniquely valuable: automated self-consistency check requiring no ground truth. Can run on every encounter. Orphan codes (coded but not in text) are strong hallucination signals.

**Formal Definition**

```
Concordance = |concepts_in_text ∩ concepts_in_codes| / |concepts_in_text ∪ concepts_in_codes|. Discordance types: (a) coded but not in text (orphan code); (b) in text but not coded (missing code). Both are quality signals with different risk profiles.
```

**Code: Text-code concordance check**

```python
from medcat.cat import CAT

cat = CAT.load_model_pack("medcat_snomed_model.zip")

def concept_concordance(note_text: str, assigned_codes: set[str]):
    """
    Compare NER-extracted concepts from free text
    against assigned SNOMED codes.
    """
    doc = cat.get_entities(note_text)
    text_concepts = {
        ent["cui"] for ent in doc["entities"].values()
        if ent["acc"] > 0.7  # confidence threshold
    }

    overlap = text_concepts & assigned_codes
    orphan_codes = assigned_codes - text_concepts  # coded but not in text
    missing_codes = text_concepts - assigned_codes  # in text but not coded

    concordance = len(overlap) / len(text_concepts | assigned_codes) if (text_concepts | assigned_codes) else 1.0

    return {
        "concordance": round(concordance, 3),
        "orphan_codes": list(orphan_codes),   # potential hallucinated codes
        "missing_codes": list(missing_codes),  # potential coding omissions
        "alert": len(orphan_codes) > 0         # orphans are higher risk
    }
```

**Limitations**

> NER extraction quality limits accuracy. Some codes are legitimately more specific than free-text descriptions.

**Novel Thinking / Implications**

> 💡 This is uniquely valuable because it requires no ground truth - it's a self-consistency check that can run on every encounter. An orphan code (coded but not mentioned in text) is a strong signal for hallucinated coding. A missing code (mentioned but not coded) is a completeness gap. Both can be detected without human review.

---

### PI.PP-8 🔵 End-of-Utterance Timing Accuracy

Whether the system correctly identifies where an utterance ends. Affects both diarisation (turn boundaries) and summarisation (sentence boundaries). Misalignment causes content fragmentation across utterances or merging of distinct utterances.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.PP-8 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR + Diarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Standard speech processing metric |

**Why this tier?**

> Vendor research metric. Affects multiple downstream stages.

**Formal Definition**

```
EOU Timing Error = mean temporal error (ms) between predicted and actual utterance boundaries. Different from speaker boundary precision - EOU timing is within-speaker pauses that should/shouldn't be treated as utterance breaks.
```

**Limitations**

> Defining 'correct' utterance boundaries is itself contested. Conversational speech doesn't always have clean utterance breaks.

**Novel Thinking / Implications**

> 💡 EOU errors propagate: a missed boundary causes two utterances to merge, which then have to be diarised as one (potentially with conflicting speakers) and summarised as one (potentially conflating two clinical concepts).

---

### PI.PP-9 🟡 Structured/Free-Text Consistency

Spans summarisation + write-back: does the coded allergy entry agree with allergies mentioned in the free-text note? Does the medication list match medications discussed in the narrative?

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.PP-9 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation + Write-back |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Identified as post-write-back automated safety check |

**Why this tier?**

> Automated post-write-back guardrail requiring no ground truth. If structured allergy field disagrees with narrative text, something has gone wrong. Deployer-implementable.

**Formal Definition**

```
For each structured field category f ∈ {allergies, medications, diagnoses}: Consistency(f) = |items_in_structured(f) ∩ items_in_freetext| / |items_in_structured(f) ∪ items_in_freetext|. Inconsistencies: (a) in structured but not free text - unexplained entries; (b) in free text but not structured - missed structuring.
```

**Limitations**

> Requires NER capable of matching free-text mentions to structured field entries. Partial mentions (e.g. 'penicillin allergy' in text vs SNOMED allergy code) need fuzzy matching.

**Novel Thinking / Implications**

> 💡 This is a post-write-back guardrail that can run automatically. If the allergy field says 'penicillin' but the note never mentions penicillin, something has gone wrong - either the note omitted it (summarisation failure) or the structured entry is hallucinated (coding/write-back failure). Either way, it needs review.

---

