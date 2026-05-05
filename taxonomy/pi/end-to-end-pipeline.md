### PI.E2E-1 🔵 Source-to-Record Concordance

End-to-end: comparing original consultation audio directly against the final EPR entry, bypassing all intermediate representations. This is what actually matters for patient safety.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.E2E-1 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | Proposed as the ultimate AVT safety metric - captures cumulative pipeline effect |

**Why this tier?**

> The ultimate safety metric but requires expert annotation of source audio. Best suited for national evaluation programme. Periodic deployer sampling (e.g. 10 encounters/quarter) is feasible but resource-intensive.

**Formal Definition**

```
SRC = |clinical_items(audio) ∩ clinical_items(EPR)| / |clinical_items(audio)|. Unlike component metrics, SRC captures cumulative loss AND cumulative gain (contextual inference by the summariser). Must be measured per safety-critical category: medications, allergies, diagnoses, plan.
```

**Code: Source-to-record concordance framework**

```python
def source_to_record_concordance(
    audio_clinical_items: dict,   # expert-annotated from audio
    epr_clinical_items: dict,     # extracted from final EPR entry
    categories=("medications","allergies","diagnoses","plan","red_flags")
):
    """
    End-to-end: did what was said reach the record?
    Per-category concordance with safety weighting.
    """
    results = {}
    safety_weights = {
        "medications": 10, "allergies": 10,
        "diagnoses": 7, "plan": 5, "red_flags": 10
    }
    weighted_score = 0
    total_weight = 0

    for cat in categories:
        audio = set(audio_clinical_items.get(cat, []))
        epr = set(epr_clinical_items.get(cat, []))
        if not audio:
            continue
        preserved = audio & epr
        lost = audio - epr       # in audio, not in record
        added = epr - audio      # in record, not in audio

        cat_concordance = len(preserved) / len(audio)
        w = safety_weights.get(cat, 1)
        weighted_score += cat_concordance * w
        total_weight += w

        results[cat] = {
            "concordance": round(cat_concordance, 3),
            "preserved": list(preserved),
            "lost": list(lost),         # safety-critical omissions
            "added": list(added),       # potential hallucinations
        }

    results["weighted_overall"] = round(weighted_score / total_weight, 3) if total_weight else 0
    return results
```

**Limitations**

> Requires expert annotation of source audio as ground truth. Expensive and labour-intensive. Cannot scale to continuous monitoring without automation (which doesn't yet exist for audio→clinical-item extraction).

**Novel Thinking / Implications**

> 💡 This is the metric the entire field should be targeting but almost nobody measures. Every other metric is a proxy for this one. VeriFact gets close by checking against existing EHR, but source-to-record concordance checks against what was actually said - a fundamentally stronger test. A national benchmark programme could fund periodic SRC audits as the definitive AVT safety assessment.

---

### PI.E2E-2 🔵 Cumulative Information Yield

The positive framing of source-to-record concordance: what proportion of the clinical information present in the source audio successfully survives the entire pipeline and appears in the final EPR record. Where Source-to-Record Concordance measures preservation rate (how much was preserved), Cumulative Information Yield measures the distributional yield across clinical categories - so it exposes systematic category bias (e.g. a system that yields 95% on medications but 60% on psychosocial content).

|Dimension              |Value                                                                            |
|-----------------------|---------------------------------------------------------------------------------|
| **Reference** | PI.E2E-2 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research                                                   |
|**Measurement Cadence**|Periodic audit                                                                   |
|**Pipeline Layer**     |End-to-End                                                                       |
|**Assurance Question** |Safety                                                                           |
|**Measurement Method** |Hybrid                                                                           |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                                   |
|**Responsible Actors** |Academic, National Body                                                          |
|**Maturity**           |Proposed / Novel                                                                 |
|**Outcome Type**       |Distal                                                                           |
|**Applicability**      |AVT-Contextualised                                                               |
|**Source**             |Extension of existing Source-to-Record Concordance with categorical yield decomposition|

**Why this tier?**

> Resource-intensive evaluation requiring expert annotation of source audio, organised into categorical yield rather than binary preservation. Best suited for national evaluation programme. Per-category reporting reveals systematic content bias invisible to aggregate preservation metrics.

**Formal Definition**

```
For each clinical category c ∈ C = {medications, allergies, diagnoses, symptoms, plan, safety_netting, social_context, psychosocial, red_flags}: Yield(c) = |items_in_c_present_in_record| / |items_in_c_in_source|. Composite: Yield_weighted = Σ w_c × Yield(c), where w_c are clinical importance weights. Report per-category breakdown alongside composite - the aggregate obscures category bias.
```

**Limitations**

> Categorical annotation of source audio is even more labour-intensive than binary annotation. Category boundaries are contested (is "stopped smoking 5 years ago" social context or relevant history?). Weight assignment for the composite is subjective.

**Novel Thinking / Implications**

> 💡 The most common finding in ambient scribe evaluation is systematic yield bias toward clinical content the model recognises as "medical" (medications, symptoms, diagnoses) and away from content it treats as peripheral (social context, psychosocial factors, patient concerns that don't map to a code). This bias is invisible to concordance metrics that treat all clinical items equally - but it has direct consequences for patient-centred care and safeguarding. Per-category yield reporting makes the bias visible and actionable.

### PI.E2E-3 🔵 Error Propagation / Cascade Analysis

End-to-end: tracking how a single upstream error amplifies or gets corrected through subsequent stages. An ASR misrecognition could be caught by the summariser (correction) or cascade into wrong coding and wrong EPR entry (amplification).

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.E2E-3 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Proposed - analogous to fault propagation analysis in safety engineering |

**Why this tier?**

> Requires controlled error injection and intermediate output access. Vendor-side testing or academic research. Deployers cannot perform without vendor cooperation.

**Formal Definition**

```
For each error e introduced at stage s: Propagation(e) ∈ {corrected, preserved, amplified}. Cascade Factor CF = Σ errors_in_final / Σ errors_at_source. CF < 1 = net error correction; CF > 1 = net error amplification. Report per error type and per stage transition.
```

**Code: Error cascade tracking**

```python
def trace_error_cascade(
    injected_errors: list[dict],  # {stage, error_type, content}
    stage_outputs: dict            # {stage_name: output_text}
):
    """
    Track injected errors through pipeline stages.
    Requires controlled error injection at specific stages.
    Illustrative: error_persists / error_amplified are stand-ins
    for project-specific comparison helpers (e.g. fuzzy string
    match, semantic similarity, or domain-specific item match).
    """
    STAGES = ["asr", "diarisation", "summarisation", "coding", "writeback"]
    cascade_results = []

    for error in injected_errors:
        trace = {"source": error, "fate": []}
        for stage in STAGES[STAGES.index(error["stage"])+1:]:
            output = stage_outputs[stage]
            if error_persists(error["content"], output):
                if error_amplified(error["content"], output):
                    trace["fate"].append({"stage": stage, "status": "amplified"})
                else:
                    trace["fate"].append({"stage": stage, "status": "preserved"})
            else:
                trace["fate"].append({"stage": stage, "status": "corrected"})
                break  # error corrected, stop tracing

        trace["final_status"] = trace["fate"][-1]["status"] if trace["fate"] else "source_only"
        cascade_results.append(trace)

    cf = sum(1 for r in cascade_results if r["final_status"] != "corrected") / len(cascade_results)
    return {"cascade_factor": round(cf, 3), "traces": cascade_results}
```

**Limitations**

> Requires controlled error injection and intermediate output access. Most vendors treat the pipeline as a black box.

**Novel Thinking / Implications**

> 💡 This is the AVT equivalent of fault propagation analysis in traditional safety engineering. The cascade factor tells you whether the multi-stage architecture is net-safe (CF < 1, stages catch each other's errors) or net-dangerous (CF > 1, errors compound). A vendor claiming their summariser 'compensates for ASR errors' should demonstrate CF < 1 with data.

---

### PI.E2E-4 🟡 Safety-Critical Information Chain of Custody

End-to-end per-item trace for highest-risk content: did this specific allergy survive ASR → diarisation → summarisation → coding → EPR field? A per-item trace, not a statistical rate.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.E2E-4 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | Proposed - analogous to chain-of-custody in evidence management and traceability in safety-critical systems |

**Why this tier?**

> Quarterly CSO audit: pick 10 safety-critical items from sampled consultations, trace each through pipeline. Manual but feasible. Directly tests whether the system preserves what matters most.

**Formal Definition**

```
For each safety-critical item i ∈ {allergies, medications, dosages, red-flags}: Custody(i) = [present_at_ASR, present_at_diarisation, present_at_summary, present_at_coding, present_at_EPR]. Complete chain: all TRUE. Broken chain: identify break point.
```

**Code: Chain of custody trace**

```python
def chain_of_custody(item: str, stage_outputs: dict) -> dict:
    """
    Trace a safety-critical item through every pipeline stage.
    Returns the chain status and break point if applicable.
    Illustrative: item_present is a stand-in for a domain-specific
    matcher (substring, normalised concept ID match, or coded-entry
    lookup depending on stage representation).
    """
    STAGES = ["transcript", "diarised_transcript", "summary",
              "coded_entries", "epr_record"]
    chain = {}
    break_point = None

    for stage in STAGES:
        present = item_present(item, stage_outputs.get(stage, ""))
        chain[stage] = present
        if not present and break_point is None:
            break_point = stage

    return {
        "item": item,
        "chain_complete": all(chain.values()),
        "chain": chain,
        "break_point": break_point,
        "risk_level": "critical" if break_point in ["coded_entries", "epr_record"]
                      else "high" if break_point in ["summary"]
                      else "medium" if break_point else "none"
    }

# Example: trace penicillin allergy through pipeline
result = chain_of_custody(
    item="penicillin allergy",
    stage_outputs={
        "transcript": "...allergic to penicillin...",
        "diarised_transcript": "PATIENT: ...allergic to penicillin...",
        "summary": "Allergies: penicillin",
        "coded_entries": "91936005 | Allergy to penicillin",
        "epr_record": "Allergy field: Penicillin"
    }
)
```

**Limitations**

> Requires access to intermediate outputs (transcript, diarised transcript, summary, codes) - most vendors expose only the final note. Per-item tracing is manual without automation.

**Novel Thinking / Implications**

> 💡 This is the audit methodology that a CSO should be able to perform. Pick 10 safety-critical items from a sample of consultations and trace each through the pipeline. If any chain breaks, you know exactly where the system fails. This should be a Day Zero acceptance test and a quarterly audit procedure.

---

### PI.E2E-5 🔵 Compound Demographic Performance

End-to-end: demographic performance gap measured at the final output, not just at ASR. ASR bias against an accent might be corrected by summarisation (context inference) or amplified (hallucination to fill gaps).

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.E2E-5 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Fairness & Equity |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, National Body |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | Proposed - extends demographic-disaggregated WER to end-to-end measurement |

**Why this tier?**

> Extends demographic WER to end-to-end measurement. Requires demographic-linked evaluation at final output level. National programme candidate.

**Formal Definition**

```
For demographic group g: E2E_gap = Quality(g_majority) - Quality(g_minority) measured on final note quality, not intermediate WER. Compare: E2E_gap vs ASR_gap. If E2E_gap > ASR_gap: pipeline amplifies bias. If E2E_gap < ASR_gap: pipeline partially compensates.
```

**Limitations**

> Requires demographic-linked evaluation data at the final output level, not just ASR. Even more resource-intensive than disaggregated WER.

**Novel Thinking / Implications**

> 💡 The critical question: does the pipeline as a whole reduce or amplify demographic disparities? A system could have biased ASR but fair summarisation (compensating), or fair ASR but biased summarisation (introducing new disparities). Only end-to-end demographic measurement reveals the net effect.

---

### PI.E2E-6 🔵 Semantic Drift Accumulation

End-to-end: measuring cumulative meaning transformation across stages. Each stage subtly transforms meaning - 'occasional chest tightness on stairs' → 'chest pain on exertion'. Each individual transformation may be defensible; the cumulative drift may not be.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.E2E-6 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Proposed - inspired by signal processing concept of cumulative distortion |

**Why this tier?**

> Research metric. Embedding-based similarity is a crude proxy for clinical meaning preservation. Conceptually important but not operationally ready.

**Formal Definition**

```
Drift(audio, note) = 1 - SemanticSimilarity(meaning(audio), meaning(note)). Decompose per stage: Drift_total = Σ Drift(stage_n, stage_n+1). Track: local_drift (each stage) vs cumulative_drift (end-to-end). If cumulative >> Σ local: drift interactions are non-linear.
```

**Code: Semantic drift measurement**

```python
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def measure_semantic_drift(stage_texts: dict) -> dict:
    """
    Measure meaning transformation between pipeline stages.
    stage_texts: ordered dict of {stage_name: text}
    """
    stages = list(stage_texts.keys())
    embeddings = {s: model.encode(t) for s, t in stage_texts.items()}

    # Per-stage drift (adjacent stages)
    local_drifts = {}
    for i in range(len(stages)-1):
        s1, s2 = stages[i], stages[i+1]
        cos_sim = np.dot(embeddings[s1], embeddings[s2]) / (
            np.linalg.norm(embeddings[s1]) * np.linalg.norm(embeddings[s2]))
        local_drifts[f"{s1}→{s2}"] = round(1 - cos_sim, 4)

    # End-to-end drift
    e2e_sim = np.dot(embeddings[stages[0]], embeddings[stages[-1]]) / (
        np.linalg.norm(embeddings[stages[0]]) * np.linalg.norm(embeddings[stages[-1]]))

    return {
        "local_drifts": local_drifts,
        "cumulative_drift": round(1 - e2e_sim, 4),
        "sum_local": round(sum(local_drifts.values()), 4),
        "non_linearity": round((1-e2e_sim) - sum(local_drifts.values()), 4),
        "alert": (1 - e2e_sim) > 0.3  # calibrate threshold
    }
```

**Limitations**

> Embedding-based similarity is a crude proxy for clinical meaning preservation. Two texts can be semantically distant but clinically equivalent (appropriate medical abstraction) or semantically close but clinically different (subtle dosage change).

**Novel Thinking / Implications**

> 💡 Not all drift is bad - 'occasional tightness going upstairs' → 'exertional chest pain' is appropriate medical abstraction. The question is whether the drift preserves clinical decision-relevance. A clinically-aware drift metric would weight drift on safety-critical elements higher than drift on contextual description.

---

### PI.E2E-7 🟡 Pipeline Non-Determinism / Reproducibility

End-to-end: if you re-process the same audio, do you get the same output? Each stochastic component introduces variance. Compound variance could mean the same consultation produces materially different notes on different runs.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.E2E-7 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Proposed - standard practice in safety-critical software testing but not yet applied to AVT pipelines |

**Why this tier?**

> Vendor should test: process same audio N times, verify safety-critical items are identical across runs. Deployer should request results. Non-deterministic safety items = deployment blocker.

**Formal Definition**

```
Process same audio N times (N ≥ 10). Reproducibility R = mean pairwise similarity across N outputs. Variance V = 1 - R. Safety-critical reproducibility: R_safety = proportion of runs where all safety-critical items (medications, allergies) are identical across all outputs.
```

**Code: Reproducibility testing**

```python
from itertools import combinations
import numpy as np

def test_reproducibility(audio_path: str, pipeline, n_runs: int = 10):
    """
    Process same audio N times, measure output variance.
    Illustrative: text_similarity and extract_safety_items are
    stand-ins — wire to a real similarity function (e.g. embedding
    cosine) and a clinical NER/extractor for production use.
    """
    outputs = [pipeline.process(audio_path) for _ in range(n_runs)]

    # Pairwise similarity
    pairs = list(combinations(range(n_runs), 2))
    similarities = [
        text_similarity(outputs[i], outputs[j])
        for i, j in pairs
    ]

    # Safety-critical item consistency
    safety_items_per_run = [
        extract_safety_items(out)  # medications, allergies, diagnoses
        for out in outputs
    ]
    # All runs must agree on safety items
    safety_consistent = all(
        s == safety_items_per_run[0]
        for s in safety_items_per_run
    )

    return {
        "mean_similarity": round(np.mean(similarities), 4),
        "min_similarity": round(min(similarities), 4),
        "variance": round(1 - np.mean(similarities), 4),
        "safety_items_consistent": safety_consistent,
        "n_unique_medication_sets": len(set(
            frozenset(s.get("medications", []))
            for s in safety_items_per_run
        )),
        "alert": not safety_consistent
    }
```

**Limitations**

> Computationally expensive (N × full pipeline runs). Temperature=0 doesn't guarantee determinism with batched inference. Some variation may be acceptable for non-safety content.

**Novel Thinking / Implications**

> 💡 If the same consultation produces different medication lists on different runs, the system is fundamentally unsuitable for safety-critical use regardless of its average accuracy. Safety-critical reproducibility (identical safety items across all runs) should be a hard pre-deployment gate, not a soft recommendation.

---

### PI.E2E-8 🔵 Error Attribution Analysis

End-to-end: when an error appears in the final output, which stage introduced it? Essential for improvement but requires intermediate output logging most vendors don't expose.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.E2E-8 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Proposed - analogous to root cause analysis in incident investigation |

**Why this tier?**

> Requires vendor to expose intermediate outputs. Essential for systematic improvement but most vendors treat the pipeline as a black box.

**Formal Definition**

```
For each error e in final output: Attribution(e) = stage s where e first appears OR where correct content was last present. If e not in transcript → ASR error. If in transcript but not in summary → summarisation error. Requires full intermediate output chain.
```

**Limitations**

> Requires vendors to expose intermediate outputs (raw transcript, diarised transcript, pre-coding summary). Most treat the pipeline as a black box. Contractual transparency requirements needed.

**Novel Thinking / Implications**

> 💡 Without error attribution, you can't improve the system rationally. Is the hallucination rate driven by ASR feeding garbled text to the summariser, or by the summariser inventing content from clean transcript? The intervention is completely different. Vendors should be contractually required to provide intermediate output access for error attribution audits.

---

### PI.E2E-9 🔵 Clinical Decision Equivalence

End-to-end: does the final note support the same clinical decisions a clinician present at the consultation would make? The ultimate distal outcome metric connecting documentation to patient safety.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.E2E-9 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Academic, National Body |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | Proposed - the ultimate validity test for clinical documentation |

**Why this tier?**

> Gold-standard distal outcome metric. Extremely resource-intensive (blinded clinician decision comparison). National research programme candidate.

**Formal Definition**

```
Present note to blinded clinician(s). Clinician makes clinical decisions (diagnosis, plan, prescribing) based solely on note. Compare with decisions of clinician who observed original consultation. Equivalence = |decisions_matching| / |total_decisions|. Per category: diagnostic, therapeutic, safety-netting, follow-up.
```

**Limitations**

> Extremely resource-intensive: requires blinded clinical decision-making from multiple clinicians. Inter-clinician variation in decision-making adds noise. Simulated decisions may not reflect real-world behaviour.

**⚠️ Underspecification Warning (Tier B - conceptually essential, operationally impractical)**

> Clinical Decision Equivalence is conceptually the most important metric in the taxonomy for distal outcome validation - it directly tests whether AVT-generated notes support the same clinical decisions as direct observation, which is what AVT ultimately needs to do to be safe. But measurement methodology is extremely resource-intensive: blinded clinical decision-making from multiple clinicians per case, inter-clinician variation adding noise, simulated decision contexts differing from real-world behaviour under time pressure. No validated protocol exists. No threshold for "adequate equivalence" has been established. Best interpreted as a target for national or academic evaluation programmes rather than deployer-level assessment. When operationalised, the study design must specify: (a) number of clinicians per case and selection criteria; (b) blinding methodology and how information leakage is prevented; (c) decision categories assessed (diagnostic, therapeutic, safety-netting, follow-up); (d) agreement metric (kappa, per-category accuracy, weighted agreement); (e) clinical complexity stratification; (f) handling of inter-clinician disagreement in the ground-truth condition.

**Novel Thinking / Implications**

> 💡 This is the metric that closes the proximal-distal gap. If a note produced by AVT leads to the same clinical decisions as direct observation, the documentation is functionally safe regardless of WER, ROUGE, or any other proxy metric. This should be the gold-standard validation for any AVT claiming clinical deployment readiness.

---

### PI.E2E-10 🟡 Full-Pipeline Latency Budget

End-to-end: total time from consultation end to note availability in EPR, broken down by stage. Not just ASR RTF - the full wait before a clinician can review.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.E2E-10 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Proposed as operational metric - RTF alone doesn't capture full workflow impact |

**Why this tier?**

> Operational metric deployers can measure: time from consultation end to note availability. Directly affects review quality - if note arrives after next patient, review suffers.

**Formal Definition**

```
L_total = Σ L_stage for stages ∈ {ASR, diarisation, summarisation, coding, write-back, EPR rendering}. Report: L_total distribution (P50, P95, P99). Per-stage breakdown identifies bottlenecks. Clinical constraint: L_total should be < time between consultations.
```

**Limitations**

> End-to-end latency depends on infrastructure (network, cloud processing, EPR API speed) not just AI model performance.

**Novel Thinking / Implications**

> 💡 If the note isn't available before the next patient arrives, the clinician either reviews it later (losing context) or doesn't review it at all (rubber-stamping). Latency directly affects the quality of human oversight. The pipeline latency budget should be a deployment acceptance criterion.

---

### PI.E2E-11 🟡 Pipeline Failure Recovery

When one stage fails (e.g. diarisation crashes), what does the system produce? Graceful degradation vs catastrophic failure. Most metrics assume the pipeline runs to completion - but partial failures are common in production.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.E2E-11 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Standard fault tolerance testing applied to AVT pipelines |

**Why this tier?**

> Important pre-deployment safety test. Vendor responsibility but should be a procurement question.

**Formal Definition**

```
For each pipeline stage, simulate failure and assess: (1) Does the system produce output? (2) Is the output flagged as degraded? (3) Is the failure logged? (4) Is the clinician notified? Score: graceful = output produced, flagged, logged, notified.
```

**Limitations**

> Requires controlled failure injection at specific pipeline stages. Most vendors test happy path more than failure modes.

**Novel Thinking / Implications**

> 💡 The dangerous failure mode is silent degradation: the pipeline produces output that looks normal but is built on a failed component. A diarisation failure could cause all speech to be attributed to the clinician - producing a confident-looking note with completely wrong attribution. The clinician reviewing the note has no signal that anything went wrong. Pre-deployment testing must include controlled failure injection.

---

### PI.E2E-12 🔵 Round-Trip Information Loss

If the AVT-generated note were used to reconstruct the original consultation, how much would be lost? An information-theoretic complement to source-to-record concordance - measures total information preserved through the pipeline.

| Dimension | Value |
|-----------|-------|
| **Reference** | PI.E2E-12 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | End-to-End |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Specific |
| **Source** | Information theory applied to clinical documentation |

**Why this tier?**

> Research metric. Theoretically interesting but not operationally measurable at scale.

**Formal Definition**

```
Round-Trip Loss = 1 - I(audio; note) / H(audio), where I is mutual information and H is entropy. In practice: have a clinician attempt to answer specific questions about the consultation using only the note vs the full audio; compare answer accuracy.
```

**Limitations**

> Theoretical metric; practical measurement is approximate. Information loss is not always bad - appropriate medical abstraction is loss in the technical sense.

**Novel Thinking / Implications**

> 💡 Different from source-to-record concordance because it asks about all information, not just clinical items. Includes contextual information that may matter for safeguarding, family dynamics, patient understanding - content that AVT systems systematically strip but that clinicians sometimes rely on.

---

