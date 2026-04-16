## Summarisation / NLP

*Transcript → clinical note. Where most safety-critical evaluation science concentrates.*

**Tier breakdown**: 🟢 4 Tier 1 · 🟡 8 Tier 2 · 🔵 8 Tier 3

### Family: Reference-Based Text Similarity

> **Parent construct** — the family of metrics that compare generated text to a reference text and report a similarity score. Technically rigorous; clinically weak.
>
> The next two metrics are the most widely reported automated metrics in the clinical NLG literature, and the most dangerously misleading when used in isolation. Grouping them makes explicit what the published evidence has shown repeatedly: **reference-based text similarity is a poor proxy for clinical quality in ambient scribe evaluation.**
>
> **Two implementations, one underlying limitation.** ROUGE and BERTScore differ in their matching algorithms — ROUGE uses n-gram overlap, BERTScore uses contextual embedding similarity — but they share the same fundamental weakness: they measure how closely the generated text resembles a reference text, not whether it represents clinical reality. A note can be clinically accurate while differing substantially from the reference (because the reference itself is one of many valid ways to document the encounter), or clinically wrong while closely matching the reference (because the reference was itself generated from a flawed transcript).
>
> **The published evidence is clear and damning.** Three specific findings from peer-reviewed clinical evaluation studies should govern how these metrics are used:
>
> - **ROUGE-L achieved a Kendall-Tau of 0.080** with human expert clinical judgment on clinical diagnosis generation — indistinguishable from random for practical purposes (ar5iv 2305.17364). Croxford et al. (2025, npj Digital Medicine) confirmed this pattern in clinical summarisation evaluation.
> - **Catastrophic failure modes for ROUGE** were documented with Spearman ρ between −0.66 and −0.77 in some medical contexts — meaning higher ROUGE scores actively correlated with *worse* human judgments.
> - **BERTScore-R achieved Pearson 0.62 with omission rate** (Croxford et al. 2025), which is materially better than ROUGE but still insufficient as a standalone quality indicator, and the correlation is with one specific error type rather than with overall clinical quality.
>
> The root cause is the same for both: string matching (ROUGE) and semantic similarity (BERTScore) penalise clinically valid paraphrase and reward surface overlap regardless of clinical meaning.
>
> **Why the family still exists in the taxonomy.** These metrics retain value in three specific roles: (1) technical benchmarking and regression testing during model development, where the goal is to detect regression in string or semantic overlap against a stable reference; (2) minimum-floor screening at pre-deployment, where a system scoring very badly on both is unlikely to be clinically adequate even if passing is not sufficient; (3) cross-model comparison where the reference is held constant, which controls for the reference-dependence problem. None of these roles justify using the family as the primary quality indicator in deployed clinical assurance.
>
> **The architectural rule.** Reference-based similarity metrics must be reported alongside a validated clinical instrument — PDSQI-9, CREOLA error taxonomy, or an LLM-as-a-Judge protocol that has been subjected to bias quantification. They must never be reported in isolation as evidence of clinical quality. A vendor reporting ROUGE or BERTScore as their primary or only quality metric should be treated as a procurement red flag: either they do not understand the measurement-science gap in their own field, or they are choosing the metric that flatters their system regardless of clinical relevance. Neither is compatible with NHS clinical deployment.
>
> **Metrics in this family:**
> - 🟡 **ROUGE Scores** — n-gram overlap. Technically rigorous; Kendall-Tau 0.080 with clinical judgment. Retain for benchmarking only.
> - 🔵 **BERTScore** — contextual embedding similarity. Better than ROUGE (Pearson 0.62 with omission rate) but still insufficient alone.

---

### TP.SN-1 🟡 ROUGE Scores

N-gram overlap between generated and reference text. Demonstrably inadequate for clinical safety evaluation.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-1 |
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

**⚠️ Underspecification Warning (Tier C — technically rigorous, clinically invalid)**

> Published evidence demonstrates near-zero correlation between ROUGE and human clinical judgment in clinical summarisation evaluation. Croxford et al. (2025, npj Digital Medicine) reported ROUGE-L Kendall-Tau of just 0.080 with expert clinician scoring on clinical diagnosis generation — indistinguishable from random for practical purposes. A separate investigation of automated metrics for medical note generation (ar5iv 2305.17364) documented catastrophic failure modes with Spearman ρ between −0.66 and −0.77 in some medical contexts, meaning higher ROUGE scores actively correlated with worse human judgments. The root cause is that string matching penalises clinically valid paraphrase and rewards surface overlap regardless of clinical meaning. **ROUGE must not be used as a standalone clinical quality indicator.** Retain only for technical benchmarking, and always report alongside a validated clinical instrument (PDSQI-9, CREOLA, or LLM-as-a-Judge with bias quantification).

**Novel Thinking / Implications**

> 💡 Necessary but not sufficient pre-deployment screen. Tells you almost nothing about clinical safety.

*See also: BERTScore — both members of the Reference-Based Text Similarity family. Both metrics measure surface or semantic similarity to a reference text, not clinical quality. Always report alongside a validated clinical instrument (PDSQI-9, CREOLA, or LLM-as-a-Judge with bias quantification).*

---

### TP.SN-2 🔵 BERTScore

Semantic similarity via contextual embeddings. More meaning-aware than ROUGE but still linguistic, not clinical.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-2 |
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

**⚠️ Underspecification Warning (Tier C — better than ROUGE but insufficient alone)**

> BERTScore-R achieves approximately Pearson 0.62 correlation with omission rate in clinical summarisation (Croxford et al. 2025) — materially better than ROUGE but still inadequate as a standalone clinical quality indicator. The underlying limitation is the same as ROUGE: semantic similarity is not clinical correctness. A note can be semantically close to the reference while missing a clinically critical element, or semantically distant while conveying the same clinical meaning through appropriate medical abstraction. BERTScore is useful as one input to a multi-metric assessment but should never be reported as the primary quality finding. Pair with PDSQI-9 or an LLM-as-a-Judge protocol that has been subjected to bias quantification.

*See also: ROUGE Scores — both members of the Reference-Based Text Similarity family. BERTScore is materially better than ROUGE as a text similarity metric but shares the fundamental limitation: semantic closeness to a reference is not clinical correctness. Always report alongside a validated clinical instrument.*

---

### TP.SN-3 🟡 PDSQI-9 (Physician Documentation Quality Instrument)

Nine-item validated rubric. Gold standard for human evaluation — now automatable via LLM-as-a-Judge.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-3 |
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

### TP.SN-4 🟡 CREOLA Error Taxonomy Scores

Structured error categories: omission, addition, incorrect — with sub-types. 12,999 annotated sentences. Now underpins Tortus automated guardrails.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-4 |
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

### Family: Clinical Content Fidelity

> **Parent construct** — whether the generated note faithfully represents the clinical content of the source consultation.
>
> The next five metrics measure different facets of a single underlying construct. Treating them as unrelated obscures three important things: the existence of distinct error subtypes with different clinical implications, the difference between factuality and faithfulness, and the reason that aggregate rates can mask serious category-specific failures.
>
> **Subtypes are not substitutes.** The CREOLA framework (Asgari et al., npj Digital Medicine 2025) and the AutoscriberValidate analysis (medRxiv 2026) identify at least five distinct error subtypes within this family, each with different clinical implications and different mitigations:
>
> - **Fabrication** — completely invented clinical content with no basis in the source. CREOLA data attribute 43% of observed hallucinations to this subtype. Fictional examination findings are the canonical example. Most dangerous.
> - **Context conflation** — content misattributed between different parts of the conversation or between speakers, e.g. one patient's symptom attributed to another's discussion in a multi-encounter session. Compounds diarisation errors.
> - **Incorrect negation** — polarity reversal of a clinical assertion, e.g. "no chest pain" rendered as "chest pain". Measured by the dedicated Negation Handling Accuracy metric in this family. Directly causes clinical harm via phantom allergies, eliminated presenting symptoms, and inverted medication instructions.
> - **Speculation or inference beyond source** — plausible but unverifiable content that extends beyond what was discussed, e.g. adding a likely diagnosis the clinician never stated. The summariser is exercising clinical judgment it shouldn't.
> - **Certainty inflation** — clinician uncertainty markers ("possibly", "consistent with", "rule out") stripped from the note, converting hedged observations into definitive statements. Measured by the Uncertainty Marker Preservation metric in this family.
>
> Subtypes have different root causes (ASR vs LLM vs diarisation) and different mitigations. An aggregate "hallucination rate" of 2% means very different things if 90% of the errors are speculation vs if 90% are fabrications.
>
> **Factuality and faithfulness are distinct dimensions within the family.** Factuality is world-correctness: does the statement match clinical reality? Faithfulness is source-correctness: does the statement match what was discussed? A note can be factually correct but unfaithful (the summariser inferred a correct diagnosis the clinician never stated) or faithful but factually incorrect (the summariser accurately captured the clinician's mistake). For ambient scribes, **faithfulness is the primary assurance concern** because the scribe's job is to represent the consultation, not to exercise clinical judgment. A system that silently corrects clinician errors or adds information the clinician did not state has exceeded its safe operating scope regardless of whether the resulting statement is factually true.
>
> **Recommendation for measurement.** When measuring content fidelity in periodic audit, require subtype reporting rather than aggregate rate only. A single headline number hides the distribution that matters for intervention. Vendors reporting only aggregate rates should be asked to provide the CREOLA subtype breakdown or equivalent.
>
> **Metrics in this family:**
> - 🟢 **Hallucination Rate** — the aggregate rate of generated content unsupported by source. Entry point to the family. *See underspecification warning re: definitional instability.*
> - 🟢 **Omission Rate** — the silent killer. Arguably more dangerous than hallucination because omissions are invisible to the reviewer looking at a clean-looking note.
> - 🔵 **Confabulation Detection (Support × Severity)** — vendor-proprietary two-axis approach (Abridge) that stratifies by evidence support and clinical severity. Methodologically superior where available.
> - 🟢 **Negation Handling Accuracy** — measures the Incorrect Negation subtype as a dedicated metric because of its direct clinical harm potential.
> - 🟢 **Uncertainty Marker Preservation** — measures the Certainty Inflation subtype as a dedicated metric because certainty inflation is the more dangerous direction of epistemic drift.

---

### TP.SN-5 🟢 Hallucination Rate

Proportion of generated content unsupported by source. Currently defined inconsistently across vendors.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-5 |
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

**⚠️ Underspecification Warning (Tier B — conceptually central, definitionally unstable)**

> The term "hallucination" has no universally accepted operational definition in clinical NLG. The CREOLA framework (Asgari et al., npj Digital Medicine 2025) explicitly identifies this ambiguity as a fundamental measurement challenge. Reported rates across the published literature range from 1–3% in deployed ambient scribe studies to 43–67% in adversarial LLM clinical benchmarks — a span that largely reflects methodological differences rather than true performance variation. Only two public reference datasets exist for AVT hallucination evaluation (ACI Bench, PriMock), which limits cross-study comparability. Promising recent work: the CHECK framework (arXiv 2506.11129) reduced hallucination from 31% to 0.3% using information-theoretic classification with AUC 0.95–0.96 and is a candidate standard for operational definition. Until a consensus definition emerges, require reporting of: (a) the specific subtype taxonomy used (CREOLA or equivalent); (b) inter-rater reliability on the taxonomy; (c) the reference dataset; (d) the severity classification scheme.

**Novel Thinking / Implications**

> 💡 NAS proposes <2% major hallucination Day Zero SPI, ≥5% pause trigger. 'Major' needs operational definition.

*See also: Omission Rate, Confabulation Detection, Negation Handling Accuracy, Uncertainty Marker Preservation — all members of the Clinical Content Fidelity family. The CREOLA subtype taxonomy (Fabrication / Context Conflation / Incorrect Negation / Speculation / Certainty Inflation) provides the structural decomposition.*

---

### TP.SN-6 🟢 Omission Rate

Clinically relevant source content absent from note. More dangerous than hallucination — omissions are invisible to the reviewer.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-6 |
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

*See also: Hallucination Rate, Confabulation Detection, Negation Handling Accuracy, Uncertainty Marker Preservation — all members of the Clinical Content Fidelity family. Omission is the faithfulness failure that cannot be detected without source-linked evidence (see Linked Evidence / Provenance Tracing).*

---

### TP.SN-7 🔵 Confabulation Detection (Support × Severity)

Two-axis classification: evidential support × clinical severity. Abridge model achieves 97% detection. Produces risk matrix, not single rate.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-7 |
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

*See also: Hallucination Rate, Omission Rate, Negation Handling Accuracy, Uncertainty Marker Preservation — all members of the Clinical Content Fidelity family. The Support × Severity axes formalise what the aggregate Hallucination Rate metric leaves implicit.*

---

### TP.SN-8 🔵 VeriFact Factual Verification

Automated EHR fact-checking via RAG + LLM-as-a-Judge. 92.7% agreement with clinicians (exceeds inter-clinician 88.5%). Open-source, locally deployable.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-8 |
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

### TP.SN-9 🟡 LLM-as-a-Judge (PDSQI-9 Proxy)

Reasoning LLMs scoring documentation at 27× speed (22s vs 600s). Enables 100% note evaluation.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-9 |
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

**⚠️ Underspecification Warning (Tier C — high measured reliability, unknown validity)**

> LLM-as-a-Judge has documented biases that are rarely quantified in published deployment: position bias (prefers the first response in pairwise comparison), verbosity bias (prefers longer responses), self-enhancement bias (prefers outputs from the same model family as the judge), and fine-grained scoring unreliability (inconsistent discrimination at the high end of Likert scales). The headline Croxford et al. (2025) finding of GPT-o3-mini achieving ICC 0.818 with human evaluators on PDSQI-9 should be read alongside a separate Rwanda clinical LLM evaluation study that found LLM judges correlated more strongly with non-expert than expert annotators — apparent reliability that may reflect alignment with a particular class of evaluator rather than with clinical ground truth. This is the most uncomfortable possibility in automated evaluation: high ICC with humans that does not generalise to correctness. Any deployment relying on LLM-as-a-Judge for safety-relevant decisions should run the proposed **LLM-Judge Bias Quantification** metric (see Meta-evaluation section) and document residual uncertainty before treating judge outputs as substitutes for expert review.

**Novel Thinking / Implications**

> 💡 27× speed enables 100% evaluation. But meta-problem: correlated blindspots between evaluator and evaluated.

---

### TP.SN-10 🔵 MedHELM LLM-Jury

121 tasks, 22 subcategories. LLM-jury ICC 0.47 exceeds clinician-clinician 0.43. Capability gate, not deployment evidence.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-10 |
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

### TP.SN-11 🔵 MEDIC Cross-Examination

One LLM interrogates another to detect hallucinations without references. Identifies the 'knowledge-execution gap'.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-11 |
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

### TP.SN-12 🟡 Linked Evidence / Provenance Tracing

Every text span linked to source audio. Architectural safety property — transforms review from 'looks right?' to 'is this supported?'

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-12 |
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

### TP.SN-13 🔵 SCRIBE Framework Composite

First comprehensive multi-modal AVT evaluation: simulation + computational + human + LLM. Minimum standard for pre-deployment.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-13 |
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

### TP.SN-14 🟡 Template Modification Underspecification Score

INSYTE underspecification delta when clinicians modify AVT templates. Every modification potentially invalidates the safety case.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-14 |
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

### TP.SN-15 🟢 Negation Handling Accuracy

Does the summary correctly preserve negations? 'No chest pain' vs 'chest pain' is a clinically critical distinction that LLMs commonly mishandle, particularly when negation is far from the negated concept.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-15 |
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

*See also: Hallucination Rate, Omission Rate, Confabulation Detection, Uncertainty Marker Preservation — all members of the Clinical Content Fidelity family. Negation failure is one subtype (Incorrect Negation) made explicit as a dedicated metric because of its direct clinical harm potential.*

---

### TP.SN-16 🟡 Temporal Accuracy

Preservation of when things happened. 'Patient had chest pain three weeks ago' vs 'patient has chest pain' is the difference between historical and presenting complaint. LLMs frequently collapse temporal markers when summarising.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-16 |
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

### TP.SN-17 🟡 Temporal Event Ordering Accuracy

Accuracy of reconstructing the chronological sequence of clinical events from non-linear conversation. Patients rarely describe symptoms in temporal order — they jump between current symptoms, historical episodes, family history, and future concerns. The summary must impose a coherent timeline. Distinct from the existing Temporal Accuracy metric, which covers tense and time-marker preservation at the sentence level; this metric covers event sequencing across the whole note.

|Dimension              |Value                                                   |
|-----------------------|--------------------------------------------------------|
| **Reference** | TP.SN-17 |
|**Priority Tier**      |🟡 Tier 2 — Recommended                                  |
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

### TP.SN-18 🟡 Quantifier Preservation

Preservation of clinical qualifiers: 'occasional', 'frequent', 'constant', 'mild', 'moderate', 'severe', 'intermittent'. LLMs often drop or paraphrase these, losing diagnostic information that affects clinical reasoning.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-18 |
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

### Family: Medication Safety Thread

> **Parent construct** — the family of metrics that track medication information accuracy across the full pipeline, from spoken consultation to structured EPR record. Medication errors are the canonical safety-critical failure mode in clinical documentation AI.
>
> Unlike the other families in this taxonomy, the Medication Safety Thread spans multiple pipeline layers and multiple groups: extraction and event classification at the summarisation layer, terminology coding at the clinical coding layer, and downstream outcome monitoring at the patient experience layer. The family exists because a medication error can originate at any of these stages, and measuring only one stage gives false assurance about the others.
>
> **The safety argument.** A medication mentioned in consultation passes through at least four processing stages before it affects patient care: (1) ASR must transcribe the drug name, dose, and frequency correctly; (2) the summariser must extract these attributes and classify the medication event (start, stop, change); (3) the clinical coder must map to the correct dm+d concept; (4) the EPR write-back must place the medication data in the correct structured field. An error at any stage propagates — and the stages are tested by different metrics in different groups. The family framing makes the end-to-end thread visible.
>
> **Metrics in this family:**
> - 🟡 **Medication Attribute Extraction F1** (Summarisation / NLP) — per-attribute accuracy for drug name, dose, route, frequency, duration, indication
> - 🟡 **Medication Event Classification** (Summarisation / NLP) — classification of medication actions: start, stop, increase, decrease, continue
> - 🟡 **dm+d Medication Coding Accuracy** (Clinical Coding) — mapping to NHS dm+d terminology; currency against quarterly updates
> - 🔵 **Medication Error Rate Differential** (Patient Experience) — downstream outcome: pre/post AVT medication error rates

### TP.SN-19 🟡 Medication Attribute Extraction F1

Per-attribute accuracy for each component of a medication reference: drug name, dose, route, frequency, duration, indication, and start/stop dates. Each attribute is scored independently with its own F1. The medication as a whole is only fully correct if all attributes are correct — and aggregate medication accuracy masks systematic attribute-level failures (e.g. systems that get drug names right but frequencies wrong).

|Dimension              |Value                                                        |
|-----------------------|-------------------------------------------------------------|
| **Reference** | TP.SN-19 |
|**Priority Tier**      |🟡 Tier 2 — Recommended                                       |
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

> 💡 Aggregate medication accuracy is a misleading single number. A system with 95% medication accuracy could be getting drug names right 99% of the time and doses right 92% of the time — and the 8% dose error rate is the safety-critical finding. Attribute-level breakdown is necessary for safety assurance.

### TP.SN-20 🟢 Uncertainty Marker Preservation

Does the summary maintain clinician diagnostic uncertainty ('possibly', 'suggestive of', 'consistent with', 'rule out', 'unlikely to be') rather than collapsing to definitive statements? Loss of uncertainty markers creates false certainty in the record.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-20 |
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

*See also: Hallucination Rate, Omission Rate, Confabulation Detection, Negation Handling Accuracy — all members of the Clinical Content Fidelity family. Certainty Inflation is the subtype most likely to cause diagnostic anchoring in downstream clinicians reading the note.*

---

### TP.SN-21 🟡 Medication Event Classification

Classification of medication *actions* discussed in a consultation: start, stop, increase, decrease, continue, hold, restart, allergy/contraindication. Distinct from medication attribute extraction, which captures what the medication is; event classification captures what is being *done* with it. A medication mentioned as "we'll stop this one" is not the same as "we'll keep this one" — the attributes may be identical but the clinical action is opposite.

|Dimension              |Value                                              |
|-----------------------|---------------------------------------------------|
| **Reference** | TP.SN-21 |
|**Priority Tier**      |🟡 Tier 2 — Recommended                             |
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

> 💡 The start↔stop confusion is the canonical AVT safety nightmare. A consultation discussion of "we're going to stop your warfarin and start apixaban instead" that is silently inverted by the summariser produces a note that documents starting warfarin and stopping apixaban — both incorrect, both dangerous, and neither flagged by attribute-level accuracy metrics. Event classification should be a mandatory safety gate.

### TP.SN-22 🔵 Style & Format Consistency

Does the system produce notes in the same structure each time? Inconsistency increases cognitive load for review and makes it harder for clinicians to develop efficient review patterns.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-22 |
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

### TP.SN-23 🔵 Length Appropriateness

Over-summarisation (losing detail) vs under-summarisation (verbatim transcript). Should be calibrated to consultation complexity — a 5-minute follow-up needs less than a 30-minute new patient assessment.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.SN-23 |
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

---

### TP.SN-24 🟡 Stigmatising Language Replication Rate

Proportion of AI-generated notes that reproduce biased or stigmatising language patterns learned from training data. Distinct from the existing Cultural & Linguistic Appropriateness metric, which covers broader sensitivity issues. This metric specifically tracks whether the system has learned to generate language like "drug-seeking", "non-compliant", "frequent flyer", "difficult patient" — terms which research shows appear disproportionately in notes about specific patient populations.

|Dimension              |Value                                                                       |
|-----------------------|----------------------------------------------------------------------------|
| **Reference** | TP.SN-24 |
|**Priority Tier**      |🟡 Tier 2 — Recommended                                                      |
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
