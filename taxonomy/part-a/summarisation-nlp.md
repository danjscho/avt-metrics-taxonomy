## Summarisation / NLP

*Transcript → clinical note. Where most safety-critical evaluation science concentrates.*

**Tier breakdown**: 🟢 4 Tier 1 · 🟡 8 Tier 2 · 🔵 8 Tier 3

### 🟡 ROUGE Scores

N-gram overlap between generated and reference text. Demonstrably inadequate for clinical safety evaluation.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Lin 2004; inadequacy shown by Croxford et al. 2025 |

**Why this tier?**

> Vendor provides. Necessary but demonstrably insufficient alone. Should be a minimum floor, not a primary quality indicator.

**Formal Definition**

```
ROUGE-N recall = Σ Count_match(gram_n) / Σ Count(gram_n) over reference. ROUGE-L uses longest common subsequence. All range [0,1]; higher = greater overlap. Does NOT capture clinical correctness.
```

**Code: ROUGE with clinical caveat**

```python
from rouge_score import rouge_scorer

scorer = rouge_scorer.RougeScorer(
    ['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)

reference = """Patient presents with 3-day history of productive
cough, fever 38.5C. Started amoxicillin 500mg TDS for 5 days."""
hypothesis = """Patient has had a cough for 3 days with fever.
Prescribed antibiotics."""

scores = scorer.score(reference, hypothesis)
# NOTE: hypothesis omits specific drug name and dose —
# a safety-critical omission — but still scores ~0.58 ROUGE-1.
# This is exactly why ROUGE is insufficient for clinical eval.
```

**References**

- **Original**: [Lin (2004) — ROUGE: A Package for Automatic Evaluation of Summaries](https://aclanthology.org/W04-1013/)
- **Inadequacy**: Croxford et al. (2025) — LLM-as-Judge outperforms ROUGE/BERTScore

**Limitations**

> Measures lexical overlap, not clinical accuracy. Continued use as primary vendor marketing metric is a red flag.

**Novel Thinking / Implications**

> 💡 Necessary but not sufficient pre-deployment screen. Tells you almost nothing about clinical safety.

---

### 🔵 BERTScore

Semantic similarity via contextual embeddings. More meaning-aware than ROUGE but still linguistic, not clinical.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Zhang et al. 2020; Croxford et al. 2025 |

**Why this tier?**

> Research metric. Shown to correlate poorly with clinical quality judgements. Adds little beyond ROUGE for practical assurance.

**Formal Definition**

```
Token-level cosine similarity between contextual embeddings. Precision, Recall, F1 computed via greedy matching with optional IDF weighting. Layer selection affects results.
```

**Code: BERTScore with clinical model**

```python
from bert_score import score

P, R, F1 = score(
    cands=[hypothesis], refs=[reference],
    model_type="microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract",
    lang="en")
# F1 tensor — higher = more semantically similar
# BUT: semantic similarity ≠ clinical correctness
```

**References**

- **Paper**: [Zhang et al. (2020) — BERTScore](https://arxiv.org/abs/1904.09675)

**Limitations**

> Linguistic similarity ≠ clinical correctness. Correlates poorly with clinician judgements.

---

### 🟡 PDSQI-9 (Physician Documentation Quality Instrument)

Nine-item validated rubric. Gold standard for human evaluation — now automatable via LLM-as-a-Judge.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Stetson et al.; Croxford et al. 2025 |

**Why this tier?**

> Validated gold-standard rubric. Resource-intensive without LLM automation. Recommended for periodic audit (quarterly sample).

**Formal Definition**

```
Nine dimensions scored 1–5 Likert: Up-to-date, Accurate, Thorough, Useful, Organised, Comprehensible, Succinct, Synthesised, Internally consistent. Composite = mean across dimensions. Published IRR: ICC 0.43–0.68.
```

**References**

- **Instrument**: [Stetson et al. (2012) — PDSQI-9, JAMIA](https://doi.org/10.1197/jamia.M2248)
- **LLM automation**: Croxford et al. (2025) — GPT-o3-mini ICC 0.818

**Limitations**

> Resource-intensive without LLM automation. NHS-context validation of automated scoring needed.

**Novel Thinking / Implications**

> 💡 GPT-o3-mini ICC 0.818 opens automated PDSQI-9 at scale — needs independent NHS validation.

---

### 🟡 CREOLA Error Taxonomy Scores

Structured error categories: omission, addition, incorrect — with sub-types. 12,999 annotated sentences. Now underpins Tortus automated guardrails.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Deployer, Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Asgari et al. 2025 (Tortus/GOSH). Now underpins automated guardrails. |

**Why this tier?**

> Most granular UK-origin error taxonomy. Recommended for deployers with access to CREOLA platform or equivalent structured review.

**Formal Definition**

```
Hierarchical taxonomy: L1 — Omission, Addition, Incorrect. L2 sub-types: Omission → {key finding, medication, allergy, plan}; Addition → {unsupported claim, confabulated detail, inferred}; Incorrect → {wrong value, wrong attribution, wrong timing}. Each sentence gets error vector. Aggregate: rate per category, severity-weighted composite.
```

**References**

- **CREOLA**: Asgari et al. (2025) — Tortus / Great Ormond Street Hospital

**Limitations**

> Developed in secondary care paediatrics. Primary care transferability needs validation.

**Novel Thinking / Implications**

> 💡 CREOLA's transition from evaluation instrument to automated guardrail shows the evaluation-to-guardrail pipeline other vendors should replicate.

---

### 🟢 Hallucination Rate

Proportion of generated content unsupported by source. Currently defined inconsistently across vendors.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Continuous, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Various; Tortus 1.47% per sentence |

**Why this tier?**

> Core safety metric. NAS Day Zero SPI with <2% review and ≥5% pause thresholds. Every deployer must measure this through periodic clinical audit even if methodology is manual.

**Formal Definition**

```
HR = |S_unsupported| / |S_total|, where S_total = atomic propositions in generated note, S_unsupported = subset not evidentially supported by source transcript. Severity: benign (formatting), moderate (non-safety addition), critical (fabricated clinical content).
```

**Code: Hallucination detection via NLI**

```python
from transformers import pipeline

nli = pipeline("text-classification",
               model="microsoft/deberta-v3-large-mnli")

def check_hallucination(source, generated_sentences):
    results = []
    for sent in generated_sentences:
        verdict = nli(f"{source} [SEP] {sent}", truncation=True)
        label = verdict[0]["label"]
        results.append({
            "sentence": sent,
            "supported": label == "ENTAILMENT",
            "flag": label in ("NEUTRAL", "CONTRADICTION"),
        })
    hr = sum(1 for r in results if r["flag"]) / len(results)
    return hr, results
# NOTE: NLI is coarse — doesn't distinguish benign
# formatting from dangerous clinical fabrication.
```

**References**

- **Tortus data**: 1.47% per sentence (Asgari et al. 2025)
- **Abridge**: Support × severity matrix (Oberst et al. 2024/2025)

**Limitations**

> Definition varies. No standard severity weighting.

**Novel Thinking / Implications**

> 💡 NAS proposes <2% major hallucination Day Zero SPI, ≥5% pause trigger. 'Major' needs operational definition.

---

### 🟢 Omission Rate

Clinically relevant source content absent from note. More dangerous than hallucination — omissions are invisible to the reviewer.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Tortus 3.45%; CREOLA taxonomy |

**Why this tier?**

> Arguably more dangerous than hallucination because omissions are invisible to the reviewer. Must be included in periodic clinical note audit alongside hallucination rate.

**Formal Definition**

```
OR = |P_missing| / |P_reference|. P_reference = clinically relevant propositions in source. Clinical relevance per CREOLA: key findings, medications, allergies, plan elements, safety-netting, red-flags are mandatory.
```

**References**

- **Tortus**: 3.45% omission rate (Asgari et al. 2025)

**Limitations**

> Harder to detect than hallucination. Automated detection at scale unsolved.

**Novel Thinking / Implications**

> 💡 The silent killer. A clean-looking note gives no cue something is missing. Argues for source-linked evidence as structural safeguard.

---

### 🔵 Confabulation Detection (Support × Severity)

Two-axis classification: evidential support × clinical severity. Abridge model achieves 97% detection. Produces risk matrix, not single rate.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Vendor-Proprietary |
| **Outcome Type** | Proximal |
| **Source** | Abridge whitepaper (50,000+ training examples) |

**Why this tier?**

> Vendor-proprietary (Abridge). Methodologically superior two-axis approach but not independently implementable. Informs what a national standard should require.

**Formal Definition**

```
Each proposition p classified on: Support(p) ∈ {Fully Supported, Partially Supported, Unsupported, Contradicted} × Severity(p) ∈ {Benign, Moderate, Critical}. Risk R(p) = Support_weight × Severity_weight. Safety-critical quadrant: {Unsupported ∨ Contradicted} × {Critical}.
```

**References**

- **Abridge**: Oberst, Liang, Lipton (2024/2025) — 97% vs GPT-4o 82%

**Limitations**

> Proprietary. Not independently validated.

**Novel Thinking / Implications**

> 💡 Two-axis approach is methodologically superior. National standard should mandate dimensional approach even if implementation varies.

---

### 🔵 VeriFact Factual Verification

Automated EHR fact-checking via RAG + LLM-as-a-Judge. 92.7% agreement with clinicians (exceeds inter-clinician 88.5%). Open-source, locally deployable.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | LLM-as-Judge |
| **Lifecycle Phases** | Continuous, Periodic Audit |
| **Responsible Actors** | Deployer, National Body |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Chung et al., Stanford, Jan 2025; NEJM AI |

**Why this tier?**

> Most credible path to automated continuous monitoring but requires local EHR integration (FHIR R4 read access) and NHS-context validation. National pilot candidate.

**Formal Definition**

```
(1) Decompose text into atomic propositions (Llama 3.1 70B); (2) Retrieve EHR facts via BGE-M3 embeddings + Qdrant; (3) Classify each: Supported / Not Supported / Not Addressed. Validated: 100 MIMIC-III patients, 13,070 statements.
```

**Code: VeriFact conceptual pipeline**

```python
# https://github.com/philipchung/verifact

# Step 1: Decompose into atomic propositions
from verifact.decompose import PropDecomposer
decomposer = PropDecomposer(model="llama-3.1-70b")
props = decomposer.decompose(clinical_text)

# Step 2: Retrieve EHR evidence
from verifact.retrieve import EHRRetriever
retriever = EHRRetriever(
    embedding_model="BAAI/bge-m3",
    vector_db="qdrant",
    ehr_data=patient_records)

# Step 3: Classify each proposition
from verifact.verify import FactVerifier
verifier = FactVerifier(model="llama-3.1-70b")
for prop in props:
    evidence = retriever.retrieve(prop, top_k=5)
    result = verifier.classify(prop, evidence)
    # -> "Supported" | "Not Supported" | "Not Addressed"
```

**References**

- **NEJM AI**: [Chung et al. (2025) — VeriFact](https://ai.nejm.org/doi/full/10.1056/AIdbp2500418)
- **Code**: [GitHub — philipchung/verifact](https://github.com/philipchung/verifact)

**Limitations**

> Validated on MIMIC-III (US ICU). NHS primary care transferability untested. Requires FHIR R4 read access.

**Novel Thinking / Implications**

> 💡 Most credible path to automated continuous faithfulness monitoring. Open-source = no vendor dependency. National pilot would generate first independent continuous accuracy data.

---

### 🟡 LLM-as-a-Judge (PDSQI-9 Proxy)

Reasoning LLMs scoring documentation at 27× speed (22s vs 600s). Enables 100% note evaluation.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | LLM-as-Judge |
| **Lifecycle Phases** | Continuous, Periodic Audit |
| **Responsible Actors** | Deployer, National Body |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Croxford et al. 2025 |

**Why this tier?**

> 27× speed improvement enables practical scale. Recommended for deployers with API access. Needs NHS-context validation of scoring calibration.

**Formal Definition**

```
Reasoning LLM prompted with PDSQI-9 rubric scores each note on 9 dimensions. ICC = 0.818 (o3-mini) vs 0.43 (human-human). Non-reasoning models achieve substantially lower agreement.
```

**References**

- **Study**: Croxford et al. (2025) — npj Digital Medicine

**Limitations**

> One LLM evaluating another = correlated failure modes. Evaluation LLM should be different model family.

**Novel Thinking / Implications**

> 💡 27× speed enables 100% evaluation. But meta-problem: correlated blindspots between evaluator and evaluated.

---

### 🔵 MedHELM LLM-Jury

121 tasks, 22 subcategories. LLM-jury ICC 0.47 exceeds clinician-clinician 0.43. Capability gate, not deployment evidence.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | LLM-as-Judge |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor, National Body |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Bedi et al., Stanford CRFM, May 2025 |

**Why this tier?**

> Research benchmark for pre-deployment capability gating. Vendor responsibility. Value is as minimum capability floor, not deployment safety evidence.

**Formal Definition**

```
Holistic Evaluation of Language Models for Medicine. LLM-jury: panel of LLMs independently scores, aggregated via majority/mean. Available via Microsoft MedEvals on Azure AI Foundry.
```

**References**

- **Paper**: [Bedi et al. (2025) — MedHELM, Stanford CRFM](https://arxiv.org/abs/2505.23802)

**Limitations**

> Benchmarks ≠ deployment. MEDIC knowledge-execution gap is the critical caveat.

**Novel Thinking / Implications**

> 💡 Value is as minimum capability gate, not deployment safety evidence.

---

### 🔵 MEDIC Cross-Examination

One LLM interrogates another to detect hallucinations without references. Identifies the 'knowledge-execution gap'.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | LLM-as-Judge |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Kanithi et al. 2025 |

**Why this tier?**

> Research framework. Knowledge-execution gap finding is important but MEDIC methodology is not yet deployable outside research settings.

**Formal Definition**

```
Examiner LLM probes claims in target output, evaluates consistency. Knowledge-execution gap KE = benchmark_accuracy - operational_accuracy.
```

**References**

- **Paper**: Kanithi et al. (2025) — MEDIC

**Limitations**

> Correlated blindspots possible.

**Novel Thinking / Implications**

> 💡 Knowledge-execution gap: exam performance ≠ operational performance. Pre-deployment benchmarks are structurally insufficient.

---

### 🟡 Linked Evidence / Provenance Tracing

Every text span linked to source audio. Architectural safety property — transforms review from 'looks right?' to 'is this supported?'

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Vendor-Proprietary |
| **Outcome Type** | Proximal |
| **Source** | Abridge Linked Evidence |

**Why this tier?**

> Architectural safety property. Should be a procurement requirement — provenance tracing transforms review quality. Vendor must provide.

**Formal Definition**

```
For each span sᵢ, mapping M(sᵢ) → {(t_start, t_end)}. Requirements: Coverage (every span has ≥1 link), Relevance (linked segments contain evidence), Accessibility (≤2 interactions to inspect).
```

**References**

- **Abridge**: Abridge Linked Evidence architecture

**Limitations**

> Proprietary. Requires audio retention. Depends on clinician usage.

**Novel Thinking / Implications**

> 💡 National standard should require provenance tracing as architectural requirement.

---

### 🔵 SCRIBE Framework Composite

First comprehensive multi-modal AVT evaluation: simulation + computational + human + LLM. Minimum standard for pre-deployment.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Academic, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Wang et al. 2025 (Duke/MedStar) |

**Why this tier?**

> Comprehensive research framework. Should be the aspiration for pre-deployment evaluation but requires simulation infrastructure no NHS deployer currently has.

**Formal Definition**

```
Four modalities: (1) Simulated encounters with ground truth; (2) Computational metrics on outputs; (3) Structured clinician review; (4) LLM evaluation. Composite requires passing all four — no single modality compensates for another.
```

**References**

- **Paper**: [Wang et al. (2025) — SCRIBE, npj Digital Medicine](https://doi.org/10.1038/s41746-025-01449-w)

**Limitations**

> Complex to implement. Research framework, not deployable toolkit.

**Novel Thinking / Implications**

> 💡 Demonstrates no single modality is sufficient. Should be minimum pre-deployment standard.

---

### 🟡 Template Modification Underspecification Score

INSYTE underspecification delta when clinicians modify AVT templates. Every modification potentially invalidates the safety case.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer, Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | INSYTE analysis; DCB0129 gap |

**Why this tier?**

> Relevant whenever deployers allow template customisation. Must monitor if templates are configurable — every modification potentially invalidates the safety case.

**Formal Definition**

```
For default template T₀ with INSYTE underspecification U₀, modified template T' with U': ΔU = U' - U₀. If ΔU > threshold, modified template exits validated safety envelope → re-evaluation required under DCB0129.
```

**References**

- **INSYTE**: INSYTE autonomy classification — DCB0129 structural gap

**Limitations**

> Not yet operationalised for routine use.

**Novel Thinking / Implications**

> 💡 Hidden risk vector: template customisation as feature, but every modification potentially invalidates safety case.

---

### 🟢 Negation Handling Accuracy

Does the summary correctly preserve negations? 'No chest pain' vs 'chest pain' is a clinically critical distinction that LLMs commonly mishandle, particularly when negation is far from the negated concept.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Clinical NLP literature; identified as systematic LLM failure mode |

**Why this tier?**

> Safety-critical and well-documented LLM failure mode. Should be tested pre-deployment and periodically re-audited. Negation errors directly cause clinical harm.

**Formal Definition**

```
For each negated concept in reference: Negation Preserved = (concept appears in summary) AND (negation marker correctly attached). Negation Accuracy = |correctly_negated| / |total_negations|. Failure modes: dropped negation (becomes positive), added negation (becomes negative), wrong scope.
```

**References**

- **Negation in clinical NLP**: ConText algorithm (Harkema et al.); standard clinical NLP problem

**Limitations**

> Negation detection itself is imperfect. Clinical negation has subtleties: hedged negation ('unlikely to be'), conditional negation ('if no improvement'), historical negation ('previously denied').

**Novel Thinking / Implications**

> 💡 Negation handling is the single most clinically dangerous LLM failure mode. A summary that drops 'no' from 'no allergies' creates a phantom allergy. A summary that adds 'no' to 'has chest pain' eliminates a presenting symptom. Both can cause direct harm. This deserves dedicated testing with adversarially constructed test cases — sentences specifically designed to challenge negation handling.

---

### 🟡 Temporal Accuracy

Preservation of when things happened. 'Patient had chest pain three weeks ago' vs 'patient has chest pain' is the difference between historical and presenting complaint. LLMs frequently collapse temporal markers when summarising.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Clinical NLP literature on temporal expression extraction |

**Why this tier?**

> Important clinical distinction but harder to measure than negation. Requires temporal expression annotation. Should be part of periodic audit.

**Formal Definition**

```
For each temporal expression in reference: Temporal Accuracy = (time reference present in summary) AND (temporal relationship preserved). Categories: absolute time (dates), relative time (days/weeks ago), duration (for X days), tense (present/past/historical).
```

**Limitations**

> Temporal expressions are diverse and ambiguous. 'Recently' can mean different things in different clinical contexts.

**Novel Thinking / Implications**

> 💡 Temporal collapse is a subtle but dangerous failure mode. 'Patient had a heart attack five years ago' becoming 'patient has had a heart attack' loses the time information that distinguishes acute from historical. The clinical implications differ entirely. This is particularly relevant for problem list management — historical conditions should not be coded as active.

---

### 🟡 Quantifier Preservation

Preservation of clinical qualifiers: 'occasional', 'frequent', 'constant', 'mild', 'moderate', 'severe', 'intermittent'. LLMs often drop or paraphrase these, losing diagnostic information that affects clinical reasoning.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Identified as systematic LLM summarisation failure mode |

**Why this tier?**

> Important quality dimension that current metrics don't capture. Periodic audit recommended. Annotated test cases would be straightforward to construct.

**Formal Definition**

```
For each quantifier in reference: Quantifier Preservation = (quantifier present in summary) OR (semantically equivalent quantifier present). Track: dropped quantifiers, paraphrased quantifiers (acceptable), replaced quantifiers (unacceptable — changes severity).
```

**Limitations**

> Quantifier semantics are imprecise. Clinical training varies in how quantifiers are interpreted.

**Novel Thinking / Implications**

> 💡 'Occasional headaches' becoming 'headaches' loses the frequency information that distinguishes a normal variant from a clinical concern. 'Severe' becoming 'present' eliminates the severity assessment. These dropped qualifiers compound across the note — by the end, the clinical picture has been subtly distorted in ways that affect downstream decisions.

---

### 🟢 Uncertainty Marker Preservation

Does the summary maintain clinician diagnostic uncertainty ('possibly', 'suggestive of', 'consistent with', 'rule out', 'unlikely to be') rather than collapsing to definitive statements? Loss of uncertainty markers creates false certainty in the record.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Clinical NLP hedging/uncertainty literature |

**Why this tier?**

> Safety-critical: certainty inflation creates false diagnostic confidence in the record. Should be tested with adversarial cases as part of pre-deployment and periodic audit.

**Formal Definition**

```
For each uncertainty marker in reference: Marker Preservation = (uncertainty marker present in summary) AND (epistemic level preserved). Failure modes: certainty inflation (uncertain -> certain), certainty deflation (certain -> uncertain), marker substitution (changes epistemic meaning).
```

**Limitations**

> Uncertainty markers are subtle and easily missed by both humans and machines. The boundary between hedged and unhedged statements is fuzzy.

**Novel Thinking / Implications**

> 💡 Certainty inflation is the more dangerous direction. When 'possibly viral, consider antibiotics if no improvement' becomes 'viral, no antibiotics needed' the clinical management plan is fundamentally altered. The summariser has effectively made a diagnostic decision that the clinician explicitly hedged on. This connects to epistemic status preservation but is more granular.

---

### 🔵 Style & Format Consistency

Does the system produce notes in the same structure each time? Inconsistency increases cognitive load for review and makes it harder for clinicians to develop efficient review patterns.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Human factors literature on documentation consistency |

**Why this tier?**

> Quality of life metric. Important for review efficiency but not safety-critical.

**Formal Definition**

```
Structural similarity across notes from the same template/configuration. Section presence consistency, ordering consistency, formatting consistency (bullet vs prose, headers, etc.). Report as variance metric across encounters.
```

**Limitations**

> Some legitimate variation is desirable — different consultations need different structures. Distinguishing legitimate variation from inappropriate inconsistency is judgement-based.

**Novel Thinking / Implications**

> 💡 Cognitive load research shows that consistent visual structure dramatically improves review efficiency. A note that always has 'History' followed by 'Examination' followed by 'Plan' allows clinicians to develop scanning patterns. A note that varies its structure forces re-orientation each time, increasing review time and reducing review quality.

---

### 🔵 Length Appropriateness

Over-summarisation (losing detail) vs under-summarisation (verbatim transcript). Should be calibrated to consultation complexity — a 5-minute follow-up needs less than a 30-minute new patient assessment.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Identified as quality dimension not captured by accuracy metrics |

**Why this tier?**

> Continuous statistical monitoring is feasible but interpretation is context-dependent. Better suited for trend monitoring than threshold-based alerting.

**Formal Definition**

```
Length Ratio = note_length / consultation_duration. Appropriateness = correlation between length ratio and consultation complexity (measured by SNOMED concept count, problem count, or clinician complexity rating). Outliers (very short or very long for complexity) indicate calibration issues.
```

**Limitations**

> Appropriate length is subjective and varies by clinical context, specialty, and individual clinician preference.

**Novel Thinking / Implications**

> 💡 Over-summarisation is a quiet failure mode — the note looks clean but has lost necessary detail. Under-summarisation produces verbatim transcripts that defeat the purpose of AVT. Both can be detected statistically: a system that produces 200-word notes for both 5-minute and 30-minute consultations is not adapting appropriately.

---

