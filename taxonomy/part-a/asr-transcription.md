## ASR / Transcription

*Audio → text. Foundational accuracy everything depends on.*

**Tier breakdown**: 🟢 2 Tier 1 · 🟡 6 Tier 2 · 🔵 4 Tier 3

### Family: Clinical Transcription Accuracy

> **Parent construct** - how accurately the ASR layer transcribes the source audio, with clinical significance weighting that reflects the asymmetric cost of errors on clinical vs non-clinical content.
>
> The next three metrics form one family of increasing clinical sophistication. Treating them as separate unrelated metrics obscures the progression: each one answers the same fundamental question - *how many words did the ASR get wrong, and how bad were the wrong ones?* - at a different level of clinical awareness.
>
> **Three implementation levels of one construct:**
>
> 1. **Raw WER** - all word errors weighted equally. A misheard "the" counts the same as a misheard drug name. Technically rigorous and widely reported, but clinically uninformative because a 5% WER could be safe or dangerous depending on which words are wrong. Acceptable as a technical benchmark and for cross-system comparison on common test sets; inadequate as a clinical safety indicator.
>
> 2. **Medical WER (M-WER)** - errors weighted by whether the token belongs to a clinically significant class (drug names, dosages, diagnoses, safety-critical terminology). Reveals whether the system preserves the content that matters most, independent of filler and non-clinical speech accuracy. Abridge's **Medical Term Recall (MTR)** and DeepScribe's **Medical Word Hit Rate** are functionally equivalent implementations of the same underlying construct, even though they are reported under different names - a vendor reporting MTR is reporting the same thing as a vendor reporting M-WER, with different clinical term lists and weighting schemes. The **⚠️ Underspecification Warning** applies: no standardised clinical significance ontology exists, so cross-vendor M-WER comparison is not currently meaningful.
>
> 3. **Clinical Keyword Error Rate (CK-ER)** - binary per clinical keyword: was each safety-critical term captured correctly, yes or no? A more actionable variant of M-WER that can run as an automated guardrail on every encounter. Better suited to continuous monitoring than to benchmarking because its sensitivity depends entirely on the keyword dictionary used.
>
> **Cross-vendor comparability problem.** All three tiers suffer from the same fundamental issue: **without a standardised clinical term list or significance ontology, vendor-reported values are not directly comparable**. A vendor claiming 95% M-WER against one term list is not comparable to another vendor claiming 95% against a different term list. Cross-vendor procurement comparisons should either use a nationally standardised term list (which does not yet exist for NHS) or explicitly require the vendor to publish their term list and provenance alongside the reported value. This is a candidate area for NHS England or equivalent national body specification work - a canonical clinical term list mapped to SNOMED safety-critical concept classes would make the family's metrics meaningful as procurement signals for the first time.
>
> **How this family relates to other ASR metrics in the taxonomy.** Three ASR metrics sit outside this family because they measure different things:
>
> - **Character Error Rate (CER)** is orthogonal - it measures error rate at character level rather than word level, and is used to detect subword errors in medical terminology (e.g. "amoxicillin" vs "amoxycillin") that WER at the word level misses.
> - **Demographic-Disaggregated WER** and **Speaker-Stratified WER** are disaggregation axes that can be applied to any of the three metrics in this family. You can compute raw WER disaggregated by accent, or M-WER disaggregated by speaker role, etc.
> - **Numeric Accuracy** is a category-specific extension that measures accuracy on numbers (dosages, dates, vital signs). Treat it as a mandatory companion metric to Clinical Transcription Accuracy because numeric errors have outsized clinical consequences.
>
> **Metrics in this family:**
> - 🟡 **Word Error Rate (WER)** - level 1, raw. Necessary as a technical benchmark; insufficient alone for clinical safety.
> - 🔵 **Medical Word Error Rate (M-WER)** - level 2, significance-weighted. Reveals whether clinical content is preserved. Underspecified pending a standardised ontology.
> - 🔵 **Clinical Keyword Error Rate (CK-ER)** - level 3, per-keyword binary. Usable as an automated guardrail on every encounter. Underspecified pending a standardised keyword dictionary.

---

### TP.ASR-1 🟡 Word Error Rate (WER)

Standard ASR accuracy metric. Treats all word errors equally - a misheard 'the' counts the same as a misheard drug name.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-1 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard ASR literature; used in SCRIBE framework (Wang et al. 2025) |

**Why this tier?**

> Vendor should provide pre-deployment. Deployers should request but cannot independently measure without ground-truth transcripts.

**Formal Definition**

```
WER = (S + D + I) / N, where S = substitutions, D = deletions, I = insertions, N = total words in reference transcript. Computed via minimum edit distance (Levenshtein) alignment between hypothesis and reference. Values > 1.0 are possible when insertions exceed reference length.
```

**Code: WER via jiwer**

```python
from jiwer import wer, process_words

reference = "the patient reports chest pain radiating to left arm"
hypothesis = "the patient reports chess pain radiating to left hand"

error_rate = wer(reference, hypothesis)
# error_rate = 0.2 (2 substitutions / 10 words)

# For corpus-level WER across multiple utterances:
out = process_words(references_list, hypotheses_list)
corpus_wer = out.wer  # macro-averaged across utterances
```

**References**

- **NIST scoring toolkit**: [SCTK - NIST Speech Recognition Scoring Toolkit](https://github.com/usnistgov/SCTK)
- **Original**: Woodard & Nelson (1982), NBS Report

**Limitations**

> Clinically uninformative - does not weight by clinical significance. A 5% WER could be safe or dangerous depending on which words are wrong.

*See also: Medical WER (M-WER), Clinical Keyword Error Rate (CK-ER) - all members of the Clinical Transcription Accuracy family. Raw WER is level 1 of the family; the other two add clinical weighting but require a standardised significance ontology that does not yet exist.*

---

### TP.ASR-2 🔵 Medical Word Error Rate (M-WER)

Weighted WER where errors on clinically significant tokens carry higher penalty. Requires a clinical significance ontology to define token weights.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-2 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, National Body |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Proposed in OxonFair extension analysis |

**Why this tier?**

> No standardised clinical significance ontology exists. Requires national body to define weighting standard before it becomes actionable.

**Formal Definition**

```
M-WER = Σ(wᵢ · eᵢ) / Σ(wᵢ), where wᵢ is the clinical significance weight for token i, and eᵢ ∈ {0,1} indicates whether token i was incorrectly transcribed. Weights assigned from clinical ontology: safety-critical tokens (drug names, dosages, allergies) receive w >> 1; filler words receive w ≈ 0.1.
```

**Code: M-WER weighted computation**

```python
import numpy as np
from jiwer import process_words

# Clinical significance weights by SNOMED concept class
WEIGHTS = {
    "drug_name": 10.0, "dosage": 10.0,
    "allergy": 8.0, "diagnosis": 7.0,
    "red_flag_symptom": 9.0, "anatomy": 5.0,
    "filler": 0.1, "default": 1.0,
}

def classify_token(token, clinical_ner_model):
    """Map token to clinical significance class via NER."""
    entity = clinical_ner_model.predict(token)
    return WEIGHTS.get(entity, WEIGHTS["default"])

def medical_wer(ref_tokens, hyp_tokens, ner_model):
    """Compute weighted Medical WER."""
    weighted_errors = 0.0
    weighted_total = 0.0
    for i, ref_token in enumerate(ref_tokens):
        w = classify_token(ref_token, ner_model)
        weighted_total += w
        if i >= len(hyp_tokens) or ref_token != hyp_tokens[i]:
            weighted_errors += w
    return weighted_errors / weighted_total if weighted_total > 0 else 0
```

**References**

- **Concept origin**: Proposed in OxonFair healthcare voice fairness extension analysis
- **Related**: [Semantic Word Error Rate for clinical ASR (Li et al. 2022)](https://arxiv.org/abs/2207.13135)

**Limitations**

> No standardised clinical significance ontology exists. Weight assignment is inherently subjective.

**⚠️ Underspecification Warning (Tier B - no standardised weighting ontology)**

> M-WER requires a weighting ontology defining the clinical significance of token classes. **No such ontology is standardised for NHS or international use.** Abridge's Medical Term Recall (MTR) and DeepScribe's Medical Word Hit Rate are functionally equivalent implementations that use different proprietary term lists and different weighting schemes - so a vendor claiming "95% MTR" cannot be directly compared with another claiming "95% M-WER". A national body standard mapping SNOMED safety-critical concept classes to weight values would make vendor benchmarks comparable and is a candidate for NHS England or equivalent commissioning. Until then, require vendors to disclose (a) their term list and provenance, (b) the weighting scheme, and (c) the reference dataset used for M-WER computation. Refuse to compare M-WER values across vendors without this disclosure.

**Novel Thinking / Implications**

> 💡 A national body could define a standardised M-WER weighting ontology mapped to SNOMED safety-critical concept classes, making vendor benchmarks comparable.

*See also: Word Error Rate (WER), Clinical Keyword Error Rate (CK-ER) - all members of the Clinical Transcription Accuracy family. Abridge's Medical Term Recall (MTR) and DeepScribe's Medical Word Hit Rate are functionally equivalent implementations of this metric reported under different names; a vendor reporting any of these is reporting the same construct with different term lists.*

---

### TP.ASR-3 🔵 Clinical Keyword Error Rate (CK-ER)

Focused accuracy for high-stakes clinical terminology. Binary: was the keyword captured correctly or not?

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-3 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Derived from OxonFair healthcare voice fairness analysis |

**Why this tier?**

> Proposed automated guardrail. Technically feasible but requires curated keyword dictionaries and clinical NER infrastructure not yet available.

**Formal Definition**

```
CK-ER = 1 - (|K_correct| / |K_reference|), where K_reference = clinical keywords in reference (identified by NER), K_correct = subset correctly captured. Partial matches use Levenshtein similarity threshold δ ≥ 0.85.
```

**Code: CK-ER guardrail check**

```python
from medcat.cat import CAT
from Levenshtein import ratio as lev_ratio

cat = CAT.load_model_pack("path/to/medcat_model.zip")
SIMILARITY_THRESHOLD = 0.85

def extract_clinical_keywords(text):
    doc = cat.get_entities(text)
    return {ent["source_value"].lower(): ent
            for ent in doc["entities"].values()
            if ent["types"] in {"drug","dosage","allergy","diagnosis"}}

def clinical_keyword_error_rate(reference, hypothesis):
    ref_kw = extract_clinical_keywords(reference)
    hyp_kw = extract_clinical_keywords(hypothesis)
    if not ref_kw: return 0.0
    correct = sum(1 for kw in ref_kw
                  if any(lev_ratio(kw, h) >= SIMILARITY_THRESHOLD
                         for h in hyp_kw))
    return 1.0 - (correct / len(ref_kw))
```

**References**

- **Clinical NER**: [MedCAT: Medical Concept Annotation Tool](https://github.com/CogStack/MedCAT)

**Limitations**

> Requires ground-truth keyword annotation. Keyword list must be maintained as terminology evolves.

**⚠️ Underspecification Warning (Tier B - same standardisation gap as M-WER)**

> CK-ER depends on a clinical significance ontology defining which terms are keywords - no standardised ontology exists. The vendor or deployer implementing CK-ER chooses which terms count, and the resulting metric is only as good as that choice. Different keyword lists produce materially different CK-ER values for the same system, which prevents cross-vendor comparison and makes local benchmarks difficult to interpret. This metric sits in the same standardisation gap as M-WER: it is conceptually sound but requires national body specification of a canonical keyword ontology mapped to SNOMED safety-critical concept classes before it can be reported in a comparable way. In the interim, document the keyword dictionary used and its provenance when reporting CK-ER.

**Novel Thinking / Implications**

> 💡 Could run as automated post-transcription guardrail on every encounter without human review.

*See also: Word Error Rate (WER), Medical WER (M-WER) - all members of the Clinical Transcription Accuracy family. CK-ER is the most actionable variant - binary per keyword, suited to running as an automated guardrail - but is most sensitive to the choice of keyword dictionary.*

---

### Family: Demographic Equity Disaggregation

> **Parent construct** - the family of metrics that apply demographic disaggregation to pipeline performance, measuring whether system quality varies across population subgroups. The underlying principle is the same at every layer: compute the base metric separately for each demographic group, then quantify the gap.
>
> This family spans the full pipeline because equity failures can originate at any stage. ASR accuracy may vary by accent; summarisation quality may vary by consultation style correlated with ethnicity; coding completeness may systematically differ across patient populations. Measuring equity at only one layer provides false assurance - a system that transcribes equitably may still summarise or code inequitably.
>
> **The disaggregation axes.** Most metrics in this family operate on the same set of demographic variables: accent/dialect, first language, age band, sex, ethnicity, deprivation quintile, and speech characteristics (rate, volume, disorder). The specific axes depend on the base metric and available data. The NAS framework proposes a maximum 5 percentage-point gap across groups as a starting threshold.
>
> **Metrics in this family:**
> - 🟡 **Demographic-Disaggregated WER** (ASR / Transcription) - WER by accent, language, age, speech characteristics
> - 🔵 **Speaker-Stratified WER** (ASR / Transcription) - WER by speaker role (clinician vs patient)
> - 🟡 **Coding Equity Index** (Clinical Coding) - whether AVT-driven coding changes are equitable across demographics
> - 🔵 **Compound Demographic Performance** (End-to-End Pipeline) - intersectional performance at full-pipeline level
> - 🟡 **Accent Taxonomy Standardisation** (Fairness & Equity) - standardised accent/dialect categorisation for disaggregation
> - 🔵 **Intersectional Performance** (Fairness & Equity) - performance at demographic intersections
> - 🔵 **Intersectional Compound Fairness Score** (Fairness & Equity) - formal intersectional fairness quantification

### TP.ASR-4 🟡 Demographic-Disaggregated WER

WER by accent group, first language, age band, and speech characteristics. NAS proposes max 5pp gap across groups.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-4 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, National Body |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | NAS framework Day Zero SPIs; NHSE IG guidance (March 2026) |

**Why this tier?**

> NAS framework requirement. Should be requested from vendor at procurement and re-tested periodically. Essential for equity assurance but requires demographic test data.

**Formal Definition**

```
For each demographic group g ∈ G, compute WER_g independently. Equity gap Δ = max(WER_g) - min(WER_g). NAS threshold: Δ < 0.05 (5 percentage points). Use bootstrap CIs given small group sizes.
```

**Code: Disaggregated WER with equity gap**

```python
import pandas as pd
from jiwer import wer
import numpy as np

def disaggregated_wer(df, ref_col, hyp_col, demo_col):
    results = {}
    for group, gdf in df.groupby(demo_col):
        refs = gdf[ref_col].tolist()
        hyps = gdf[hyp_col].tolist()
        results[group] = {"wer": wer(refs, hyps), "n": len(gdf)}
    wer_vals = [r["wer"] for r in results.values()]
    equity_gap = max(wer_vals) - min(wer_vals)
    return {
        "per_group": results,
        "equity_gap": equity_gap,
        "threshold_met": equity_gap < 0.05,  # NAS 5pp
        "worst_group": max(results, key=lambda g: results[g]["wer"]),
    }
```

**References**

- **ASR bias**: [Koenecke et al. (2020) - Racial disparities in automated speech recognition, PNAS](https://doi.org/10.1073/pnas.1915768117)
- **NAS framework**: NAS Day Zero SPIs; NHSE IG guidance (March 2026)

**Limitations**

> Vendors control test datasets. No independent UK-representative speech corpus exists at scale.

**⚠️ Underspecification Warning (Tier C - well-defined structure, ad hoc categorisation)**

> Published demographic WER reporting uses ad-hoc accent categorisation that has been systematically critiqued. A FAccT 2024 paper identified race-based, geography-based, and native/non-native categories as poor proxies for the actual acoustic variation that affects ASR performance - they are demographically convenient but phonologically arbitrary. No standardised maximum acceptable disparity threshold exists across the field; the NAS 5 percentage point target is a proposed rather than evidence-based threshold. For NHS context, a defensible taxonomy must include at minimum: British regional accents (with meaningful sub-categorisation), South Asian English varieties (distinct from "Indian English" as a single category), West African English, Caribbean English, and Eastern European English - none of which are consistently present in vendor-reported demographic WER data. The accompanying **Accent Taxonomy Standardisation** metric (Fairness & Equity) assesses whether the categorisation itself is defensible before the disaggregation numbers become meaningful.

**Novel Thinking / Implications**

> 💡 A national independent speech corpus reflecting NHS patient demographics would make vendor-reported demographic WER meaningful rather than self-assessed.

---

### TP.ASR-5 🔵 Speaker-Stratified WER

Separate WER for clinician vs patient speech. Patient speech is more diagnostically important and typically harder to transcribe.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-5 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | OxonFair extension analysis |

**Why this tier?**

> Novel proposal. Requires accurate diarisation as prerequisite and speaker-labelled ground truth that rarely exists.

**Formal Definition**

```
Given diarised transcript with speaker labels, compute WER independently per role. Clinical risk asymmetry ratio R = WER_patient / WER_clinician. R > 1.0 means the clinically riskier speech is less accurately captured.
```

**References**

- **Concept origin**: Identified in OxonFair extension analysis

**Limitations**

> Requires accurate diarisation as prerequisite.

**Novel Thinking / Implications**

> 💡 Misheard patient speech is more dangerous than misheard clinician speech. Speaker-stratified reporting would expose this asymmetry.

---

### TP.ASR-6 🟡 Error Transmission Rate

Proportion of ASR transcription errors that survive into the final clinical note. Distinct from end-to-end accuracy because it isolates the ASR→NLP propagation step - a system with high raw WER but strong contextual inference in the summariser can have a low transmission rate, while a system with low WER and literal summarisation can still transmit every error it makes.

|Dimension              |Value                                                                  |
|-----------------------|-----------------------------------------------------------------------|
| **Reference** | TP.ASR-6 |
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

### TP.ASR-7 🟡 Real-Time Factor (RTF)

Processing speed relative to audio duration. RTF < 1.0 = faster than real-time.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-7 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard ASR performance metric |

**Why this tier?**

> Vendor provides. Useful for operational monitoring but not safety-critical in isolation.

**Formal Definition**

```
RTF = T_processing / T_audio. For streaming ASR, report both first-token latency and full-utterance RTF.
```

**Limitations**

> Measures speed, not quality.

---

### TP.ASR-8 🟡 Character Error Rate (CER)

Character-level edit distance between reference and hypothesis. More sensitive than WER for medical terminology where subword errors are common: 'amoxicillin' vs 'amoxycillin' has WER=1 but CER=1/12. Particularly important for drug names, anatomical terms, and proper nouns.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-8 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard ASR literature |

**Why this tier?**

> Vendor should report alongside WER. Useful for identifying systems that struggle specifically with medical terminology spelling.

**Formal Definition**

```
CER = (S_c + D_c + I_c) / N_c, where S_c, D_c, I_c are character-level substitutions, deletions, insertions, and N_c is total characters in reference. Computed via character-level Levenshtein alignment. CER < WER typically because partial matches contribute fewer errors.
```

**Code: CER via jiwer**

```python
from jiwer import cer

reference = 'patient prescribed amoxicillin 500mg'
hypothesis = 'patient prescribed amoxycillin 500mg'

# WER would be 1/5 = 0.20 (one word wrong)
char_error_rate = cer(reference, hypothesis)
# CER ~ 0.027 (1 char wrong out of 37)
```

**References**

- **CER vs WER**: Standard ASR literature; particularly relevant for morphologically rich domains

**Limitations**

> CER and WER measure different things - neither is universally better. CER can underweight serious errors (a wrong drug name with similar spelling has low CER but high clinical risk).

**Novel Thinking / Implications**

> 💡 CER and WER should be reported together. A system with low WER but high CER is making many minor errors; a system with high WER but low CER is making fewer but more substantial errors. The clinical implications differ.

---

### TP.ASR-9 🟡 Out-of-Vocabulary (OOV) Rate

Proportion of tokens the ASR model doesn't recognise as valid vocabulary. New drug names, novel diagnoses, proper nouns, and recently approved medications are systematically OOV in older models. High OOV rate predicts systematic clinical accuracy gaps.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-9 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard speech recognition literature |

**Why this tier?**

> Should be re-tested when dm+d updates and when model versions change. Vendors should commit to maintenance schedule for vocabulary currency.

**Formal Definition**

```
OOV Rate = |tokens_not_in_vocab| / |total_tokens|. Compute against the ASR's lexicon. For end-to-end neural ASR, OOV manifests as decomposition into subword units which may produce nonsense. Track per encounter and per clinical category (drugs, diagnoses, procedures).
```

**Limitations**

> End-to-end neural ASR systems don't have explicit vocabularies - OOV is harder to define. Subword tokenisation means any word can be 'represented' but may not be transcribed correctly.

**Novel Thinking / Implications**

> 💡 Newly approved drugs (every quarter, MHRA approves new medicines) are by definition OOV until the model is updated. A model trained two years ago will systematically fail on the latest oncology agents, biologics, and recently licensed treatments. OOV rate against the current dm+d should be a procurement question.

---

### TP.ASR-10 🟡 ASR Confidence Calibration

Whether the ASR's stated confidence scores correlate with actual accuracy. A poorly-calibrated ASR that reports 95% confidence on 70%-accurate output is dangerous because downstream consumers (summariser, clinician) trust the output inappropriately.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-10 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Machine learning calibration literature |

**Why this tier?**

> Vendor should test and report. Confidence calibration is a prerequisite for confidence-based filtering and human review routing.

**Formal Definition**

```
For each confidence bin b in [0.5, 0.6, ..., 1.0], compute actual_accuracy(b) = correct_predictions(b) / total_predictions(b). Calibration Error = sum |b - actual_accuracy(b)| weighted by bin frequency. Perfect calibration: ECE = 0. Reliable systems: ECE < 0.05.
```

**References**

- **Calibration**: [Guo et al. (2017) - On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599)

**Limitations**

> Modern neural ASR systems are typically miscalibrated (overconfident). Calibration can be improved post-hoc but most vendors don't expose confidence scores at all.

**Novel Thinking / Implications**

> 💡 If confidence scores are exposed and well-calibrated, downstream systems can route low-confidence segments for human review. If they're miscalibrated or absent, the AVT cannot signal its own uncertainty - which means the clinician must assume everything is equally reliable.

---

### TP.ASR-11 🟡 ASR Confidence Exposure

Whether the ASR system exposes per-token or per-segment confidence scores to downstream consumers - both the summariser and the clinician reviewing. Different from the existing ASR Confidence Calibration metric, which asks whether confidence scores are *accurate*. Exposure asks whether they are *available at all*. Well-calibrated confidence locked inside the vendor's infrastructure provides no downstream benefit.

|Dimension              |Value                                                           |
|-----------------------|----------------------------------------------------------------|
| **Reference** | TP.ASR-11 |
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

### TP.ASR-12 🟢 Hallucination-Under-Noise Rate

Rate at which the ASR generates plausible-sounding but fabricated text when fed noise, silence, or non-speech audio. Whisper is famously prone to this - it can produce coherent-looking transcriptions of pure silence. A distinct failure mode from substitution errors that creates content from nothing.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-12 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Koenecke et al. 2024 'Careless Whisper'; specific to neural end-to-end ASR architectures |

**Why this tier?**

> Critical pre-deployment test. Whisper-based systems are documented to hallucinate from silence - this must be tested before clinical use. Tier 1 because the failure mode is well-documented and the test is straightforward.

**Formal Definition**

```
Test corpus: known non-speech audio (silence, music, environmental noise, foreign language). Hallucination Rate = |outputs_containing_text| / |test_samples|. Severity weighted: spurious clinical content (drug names, symptoms) is more dangerous than spurious filler.
```

**References**

- **Whisper hallucinations**: [Koenecke et al. (2024) - Careless Whisper: Speech-to-Text Hallucination Harms](https://arxiv.org/abs/2402.08021)

**Limitations**

> Different from general hallucination rate at the summarisation layer. Specifically tests ASR architectural failure on silence/noise inputs.

**Novel Thinking / Implications**

> 💡 This is a specific architectural failure mode of neural ASR systems trained on aligned speech-text pairs. When fed audio that doesn't contain speech, they don't output silence - they output their best guess at what speech might have been there. The clinical implication: pauses in consultations, brief silences, or background noise can produce fabricated clinical content. Should be a hard pre-deployment test.

---

### TP.ASR-13 🟢 Numeric Accuracy

Accuracy specifically on numbers: dosages, dates, vital signs, lab values, durations. Numbers fail differently from words and have outsized clinical importance. '15mg' vs '50mg' is a tenfold dosing error invisible to standard WER weighting.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-13 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Identified as critical gap in clinical ASR evaluation |

**Why this tier?**

> Safety-critical and underspecified by current vendor reporting. Should be a Day Zero acceptance criterion. Numeric errors are disproportionately dangerous and should be reported separately from general WER.

**Formal Definition**

```
Numeric Accuracy = |numbers_correctly_transcribed| / |numbers_in_reference|. Compute separately for: integers, decimals, units (mg/g/ml/mcg), dates, ranges. Critical sub-metric: dosage accuracy (numeric value AND unit correct).
```

**Limitations**

> Requires NER to identify numeric tokens in reference and hypothesis. Spoken numbers are particularly error-prone ('fifteen' vs 'fifty', 'point five' vs 'five').

**Novel Thinking / Implications**

> 💡 The dosage error case is the canonical clinical AI safety nightmare. A standard WER calculation treats '15mg' and '50mg' as equally wrong as 'the' becoming 'a' - they're not. Numeric accuracy should be reported separately and a single dosage error should trigger immediate review of the entire encounter.

---

### TP.ASR-14 🔵 Punctuation & Capitalisation Accuracy

Accuracy of sentence boundary detection, punctuation, and capitalisation. Affects readability and downstream NLP. Misplaced sentence boundaries can completely change clinical meaning: 'no chest pain. Shortness of breath' vs 'no chest pain, shortness of breath' have different clinical implications.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.ASR-14 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | ASR / Transcription |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard ASR post-processing literature |

**Why this tier?**

> Vendor responsibility. Important for downstream NLP quality but harder to attribute clinical impact directly.

**Formal Definition**

```
Sentence boundary F1 = harmonic mean of precision and recall on sentence boundaries. Punctuation accuracy = |correct_punctuation_marks| / |total_punctuation_in_reference|. Capitalisation accuracy = |correct_case_decisions| / |total_words|.
```

**Limitations**

> Punctuation in clinical speech is often ambiguous - clinicians don't speak in clearly punctuated sentences. Reference annotations are themselves variable.

**Novel Thinking / Implications**

> 💡 Sentence boundary errors propagate into summarisation as compounded meaning changes. A misplaced full stop can split a single clinical concept across two summarised statements, or merge two distinct concepts into one.

---

