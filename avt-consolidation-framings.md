# AVT Metrics Taxonomy — Consolidation Framings (Pass 1)

Four parent-construct introductory paragraphs that group related metrics into families, plus "see also" cross-references to add to the individual entries within each family. The goal is to make the family structure explicit without renaming or restructuring any existing entries.

## Design principles

**Framings sit before the first metric of each family.** Each framing is a short structured block that introduces the family, explains why the grouping matters, identifies the distinct subtypes, and names the individual metrics that belong. Readers encountering the first metric in the family get the context immediately.

**Format convention.** Each framing uses this structure to match the existing taxonomy style without overshadowing the metric entries themselves:

```
### Family: [Name]

> **Parent construct** — [One-sentence definition.]
>
> [2–4 paragraph framing covering what the family measures, the subtype taxonomy, and why grouping matters.]
>
> **Metrics in this family:** [List with tier icons and short positioning]
```

**Cross-references use a consistent "See also" footer.** Added at the end of each metric entry within a family, before the next entry begins:

```
*See also: [related metric 1], [related metric 2], [related metric 3] — all members of the [Family Name] family.*
```

This keeps the cross-references visible but clearly distinguished from the metric content itself.

**No renaming.** None of the existing metrics are renamed. The family framing is additive context, not a restructuring. This preserves all existing references and document search behaviour.

---

## Summary

| # | Family | Target section | Member metrics | Cross-refs to add |
|---|---|---|---|---|
| 1 | Clinical Content Fidelity | Summarisation / NLP | 5 existing | 5 |
| 2 | Post-Generation Correction | Human Factors & Workflow | 4 existing | 4 |
| 3 | Clinical Transcription Accuracy | ASR / Transcription | 3 existing | 3 |
| 4 | Reference-Based Text Similarity | Summarisation / NLP | 2 existing | 2 |

---

# Family 1 — Clinical Content Fidelity

**Target location:** Summarisation / NLP section. Insert immediately before the existing `### 🟢 Hallucination Rate` subsection.

**Member metrics (existing):**
- Hallucination Rate (🟢 Tier 1)
- Omission Rate (🟢 Tier 1)
- Confabulation Detection (Support × Severity) (🔵 Tier 3, vendor-proprietary)
- Negation Handling Accuracy (🟢 Tier 1)
- Uncertainty Marker Preservation (🟢 Tier 1)

**Framing to insert:**

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

### Cross-references to add within the family

Add to the end of each of the five metric entries, before the next entry begins:

**Hallucination Rate:**
> *See also: Omission Rate, Confabulation Detection, Negation Handling Accuracy, Uncertainty Marker Preservation — all members of the Clinical Content Fidelity family. The CREOLA subtype taxonomy (Fabrication / Context Conflation / Incorrect Negation / Speculation / Certainty Inflation) provides the structural decomposition.*

**Omission Rate:**
> *See also: Hallucination Rate, Confabulation Detection, Negation Handling Accuracy, Uncertainty Marker Preservation — all members of the Clinical Content Fidelity family. Omission is the faithfulness failure that cannot be detected without source-linked evidence (see Linked Evidence / Provenance Tracing).*

**Confabulation Detection (Support × Severity):**
> *See also: Hallucination Rate, Omission Rate, Negation Handling Accuracy, Uncertainty Marker Preservation — all members of the Clinical Content Fidelity family. The Support × Severity axes formalise what the aggregate Hallucination Rate metric leaves implicit.*

**Negation Handling Accuracy:**
> *See also: Hallucination Rate, Omission Rate, Confabulation Detection, Uncertainty Marker Preservation — all members of the Clinical Content Fidelity family. Negation failure is one subtype (Incorrect Negation) made explicit as a dedicated metric because of its direct clinical harm potential.*

**Uncertainty Marker Preservation:**
> *See also: Hallucination Rate, Omission Rate, Confabulation Detection, Negation Handling Accuracy — all members of the Clinical Content Fidelity family. Certainty Inflation is the subtype most likely to cause diagnostic anchoring in downstream clinicians reading the note.*

---

# Family 2 — Post-Generation Correction

**Target location:** Human Factors & Workflow section. Insert immediately before the existing `### 🟢 Edit Rate (% Notes Edited)` subsection.

**Member metrics (existing):**
- Edit Rate (% Notes Edited) (🟢 Tier 1)
- Edit Type Classification (🟡 Tier 2)
- Edit Location Distribution (🟡 Tier 2)
- Edit-Pattern Monitoring at Scale (🔵 Tier 3, vendor-proprietary)

**Framing to insert:**

---

### Family: Post-Generation Correction

> **Parent construct** — what clinicians do to AI-generated notes between generation and sign-off, and what that behaviour tells us about both AI quality and human oversight.
>
> The next four metrics all measure human correction of AI output but at different levels of resolution. Treating them as independent metrics misses the fact that they form a four-tier family, where each tier adds diagnostic depth at the cost of additional measurement infrastructure. A deployer with limited governance capacity can start at the first tier and add tiers as maturity grows.
>
> **Four tiers of increasing resolution:**
>
> 1. **Binary — was the note edited at all?** Cheapest to collect from EPR workflow telemetry. System-level monitoring metric. Useful for trending but clinically uninformative in isolation — a low edit rate can mean excellent AI or inadequate review, and only triangulation with other metrics distinguishes them. This is the Edit Rate metric.
>
> 2. **Magnitude — how much was edited?** Measured via edit distance (Levenshtein, TER, HTER, or compression-based). Adds signal about the scale of correction effort. Critical refinement: distinguish **semantic edits** (changing clinical meaning — adding a missed symptom, correcting a drug name) from **stylistic edits** (formatting, phrasing preference). Compression-based edit distance (arXiv 2024) has been shown to correlate better with actual human effort than raw Levenshtein because it captures the structural nature of the change. Magnitude is implicit in the Edit Type Classification metric, which decomposes edits into categories that map to magnitude.
>
> 3. **Effort and locus — what kind of work, and where in the note?** Measured via Edit Type Classification (additions / deletions / modifications / structural) and Edit Location Distribution (which sections of the note attract the most edits). Tells you which failure modes are active: predominantly additions indicate an omission problem; predominantly deletions indicate a hallucination problem; concentration in the "plan" section indicates the AI extracts facts well but struggles with clinical reasoning. This is where the family becomes diagnostic rather than just descriptive.
>
> 4. **Longitudinal pattern — how is the behaviour changing over time?** The Edit-Pattern Monitoring at Scale metric (Abridge, across 1M+ encounters per week) captures fleet-wide edit dynamics and is the most scalable quality signal currently available — but it is locked inside one vendor's proprietary infrastructure. The open research question is whether similar pattern monitoring can be built as an open standard.
>
> **A severity taxonomy for edits.** Not all edits carry equal weight. Adapted from CREOLA and edit-pattern disclosures, edits fall into four severity categories:
>
> - **Safety-critical correction** — fixing a fabricated medication, corrected allergy, reversed negation, or wrong dose. These are the edits that prevent harm.
> - **Clinical addition** — adding a missed symptom, examination finding, or plan element. Quality improvement, not harm prevention.
> - **Stylistic preference** — clinician preference for phrasing, structure, or formatting. Often the majority of edits by count but the minority by safety value.
> - **Structural reorganisation** — moving content between sections, consolidating or splitting points. Quality improvement.
>
> Aggregate edit rate treats all four categories equally. A system with a 30% edit rate consisting mostly of safety-critical corrections is in much worse state than a system with a 60% edit rate consisting mostly of stylistic preference — but the raw numbers invert the assessment. Edit Type Classification is the metric in this family that makes severity visible.
>
> **The complacency trajectory.** The family has a temporal dimension that individual measurements miss. At Day Zero, edit rate is a quality signal — higher rates mean more errors being caught. Over months, as clinicians develop trust in the system, edit rate declines — but the decline could reflect either improving AI or increasing complacency, and distinguishing them requires triangulation. This is why Edit Rate is a Tier 1 continuous metric but must be read alongside Review-Before-Signing Rate, Time-to-Sign Distribution, and periodic Automation Bias Detection error injection. Edit rate alone is an ambiguous signal; the family is diagnostic.
>
> **Metrics in this family:**
> - 🟢 **Edit Rate (% Notes Edited)** — tier 1 binary. The entry point; cheapest and most widely measured. Must be triangulated to interpret.
> - 🟡 **Edit Type Classification** — tier 3 diagnostic decomposition. Reveals failure mode (omission-dominant vs hallucination-dominant vs stylistic).
> - 🟡 **Edit Location Distribution** — tier 3 locus analysis. Reveals which sections of the note the AI handles well vs poorly.
> - 🔵 **Edit-Pattern Monitoring at Scale** — tier 4 longitudinal fleet-level monitoring. Vendor-proprietary; informs what a national standard should require of all vendors.

---

### Cross-references to add within the family

**Edit Rate (% Notes Edited):**
> *See also: Edit Type Classification, Edit Location Distribution, Edit-Pattern Monitoring at Scale — all members of the Post-Generation Correction family. Edit Rate is the binary entry point; the other metrics add diagnostic depth. Interpret alongside Review-Before-Signing Rate and Time-to-Sign Distribution to distinguish improving AI from increasing complacency.*

**Edit Type Classification:**
> *See also: Edit Rate, Edit Location Distribution, Edit-Pattern Monitoring at Scale — all members of the Post-Generation Correction family. Type classification is where the family becomes diagnostic rather than just descriptive: predominantly additions indicate an omission-dominant failure mode; predominantly deletions indicate a hallucination-dominant mode.*

**Edit Location Distribution:**
> *See also: Edit Rate, Edit Type Classification, Edit-Pattern Monitoring at Scale — all members of the Post-Generation Correction family. Locus analysis complements type classification: what kind of edit combined with where in the note identifies specific failure modes that either dimension alone would miss.*

**Edit-Pattern Monitoring at Scale:**
> *See also: Edit Rate, Edit Type Classification, Edit Location Distribution — all members of the Post-Generation Correction family. Pattern monitoring operates at the fleet level to detect shifts invisible to any single deployer; informs what a national standard should require all vendors to provide.*

---

# Family 3 — Clinical Transcription Accuracy

**Target location:** ASR / Transcription section. Insert immediately before the existing `### 🟡 Word Error Rate (WER)` subsection.

**Member metrics (existing):**
- Word Error Rate (WER) (🟡 Tier 2)
- Medical Word Error Rate (M-WER) (🔵 Tier 3)
- Clinical Keyword Error Rate (CK-ER) (🔵 Tier 3)

**Framing to insert:**

---

### Family: Clinical Transcription Accuracy

> **Parent construct** — how accurately the ASR layer transcribes the source audio, with clinical significance weighting that reflects the asymmetric cost of errors on clinical vs non-clinical content.
>
> The next three metrics form one family of increasing clinical sophistication. Treating them as separate unrelated metrics obscures the progression: each one answers the same fundamental question — *how many words did the ASR get wrong, and how bad were the wrong ones?* — at a different level of clinical awareness.
>
> **Three implementation levels of one construct:**
>
> 1. **Raw WER** — all word errors weighted equally. A misheard "the" counts the same as a misheard drug name. Technically rigorous and widely reported, but clinically uninformative because a 5% WER could be safe or dangerous depending on which words are wrong. Acceptable as a technical benchmark and for cross-system comparison on common test sets; inadequate as a clinical safety indicator.
>
> 2. **Medical WER (M-WER)** — errors weighted by whether the token belongs to a clinically significant class (drug names, dosages, diagnoses, safety-critical terminology). Reveals whether the system preserves the content that matters most, independent of filler and non-clinical speech accuracy. Abridge's **Medical Term Recall (MTR)** and DeepScribe's **Medical Word Hit Rate** are functionally equivalent implementations of the same underlying construct, even though they are reported under different names — a vendor reporting MTR is reporting the same thing as a vendor reporting M-WER, with different clinical term lists and weighting schemes. The **⚠️ Underspecification Warning** applies: no standardised clinical significance ontology exists, so cross-vendor M-WER comparison is not currently meaningful.
>
> 3. **Clinical Keyword Error Rate (CK-ER)** — binary per clinical keyword: was each safety-critical term captured correctly, yes or no? A more actionable variant of M-WER that can run as an automated guardrail on every encounter. Better suited to continuous monitoring than to benchmarking because its sensitivity depends entirely on the keyword dictionary used.
>
> **Cross-vendor comparability problem.** All three tiers suffer from the same fundamental issue: **without a standardised clinical term list or significance ontology, vendor-reported values are not directly comparable**. A vendor claiming 95% M-WER against one term list is not comparable to another vendor claiming 95% against a different term list. Cross-vendor procurement comparisons should either use a nationally standardised term list (which does not yet exist for NHS) or explicitly require the vendor to publish their term list and provenance alongside the reported value. This is a candidate area for NHS England or equivalent national body specification work — a canonical clinical term list mapped to SNOMED safety-critical concept classes would make the family's metrics meaningful as procurement signals for the first time.
>
> **How this family relates to other ASR metrics in the taxonomy.** Three ASR metrics sit outside this family because they measure different things:
>
> - **Character Error Rate (CER)** is orthogonal — it measures error rate at character level rather than word level, and is used to detect subword errors in medical terminology (e.g. "amoxicillin" vs "amoxycillin") that WER at the word level misses.
> - **Demographic-Disaggregated WER** and **Speaker-Stratified WER** are disaggregation axes that can be applied to any of the three metrics in this family. You can compute raw WER disaggregated by accent, or M-WER disaggregated by speaker role, etc.
> - **Numeric Accuracy** is a category-specific extension that measures accuracy on numbers (dosages, dates, vital signs). Treat it as a mandatory companion metric to Clinical Transcription Accuracy because numeric errors have outsized clinical consequences.
>
> **Metrics in this family:**
> - 🟡 **Word Error Rate (WER)** — level 1, raw. Necessary as a technical benchmark; insufficient alone for clinical safety.
> - 🔵 **Medical Word Error Rate (M-WER)** — level 2, significance-weighted. Reveals whether clinical content is preserved. Underspecified pending a standardised ontology.
> - 🔵 **Clinical Keyword Error Rate (CK-ER)** — level 3, per-keyword binary. Usable as an automated guardrail on every encounter. Underspecified pending a standardised keyword dictionary.

---

### Cross-references to add within the family

**Word Error Rate (WER):**
> *See also: Medical WER (M-WER), Clinical Keyword Error Rate (CK-ER) — all members of the Clinical Transcription Accuracy family. Raw WER is level 1 of the family; the other two add clinical weighting but require a standardised significance ontology that does not yet exist.*

**Medical Word Error Rate (M-WER):**
> *See also: Word Error Rate (WER), Clinical Keyword Error Rate (CK-ER) — all members of the Clinical Transcription Accuracy family. Abridge's Medical Term Recall (MTR) and DeepScribe's Medical Word Hit Rate are functionally equivalent implementations of this metric reported under different names; a vendor reporting any of these is reporting the same construct with different term lists.*

**Clinical Keyword Error Rate (CK-ER):**
> *See also: Word Error Rate (WER), Medical WER (M-WER) — all members of the Clinical Transcription Accuracy family. CK-ER is the most actionable variant — binary per keyword, suited to running as an automated guardrail — but is most sensitive to the choice of keyword dictionary.*

---

# Family 4 — Reference-Based Text Similarity

**Target location:** Summarisation / NLP section. Insert immediately before the existing `### 🟡 ROUGE Scores` subsection.

**Member metrics (existing):**
- ROUGE Scores (🟡 Tier 2)
- BERTScore (🔵 Tier 3)

**Framing to insert:**

---

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

### Cross-references to add within the family

**ROUGE Scores:**
> *See also: BERTScore — both members of the Reference-Based Text Similarity family. Both metrics measure surface or semantic similarity to a reference text, not clinical quality. Always report alongside a validated clinical instrument (PDSQI-9, CREOLA, or LLM-as-a-Judge with bias quantification).*

**BERTScore:**
> *See also: ROUGE Scores — both members of the Reference-Based Text Similarity family. BERTScore is materially better than ROUGE as a text similarity metric but shares the fundamental limitation: semantic closeness to a reference is not clinical correctness. Always report alongside a validated clinical instrument.*

---

# Integration notes

**Order of integration matters.** These framings reference some of the new metrics from the drafting batches (the CREOLA subtype taxonomy is in the existing Confabulation Detection entry; the "compression-based edit distance" reference is drafter addition; Verification Burden and other new metrics are referenced implicitly). None of the cross-references will break if the new metrics are integrated first, but the framings read best if applied after the new entries are in place.

**Summary section update.** The existing Summary section's "By Priority Tier" and "By Maturity" breakdowns do not currently include any family-level grouping. Consider adding a third breakdown after integration:

```
### By Metric Family

- **Clinical Content Fidelity**: 5 metrics (hallucination, omission, and related fidelity measures)
- **Post-Generation Correction**: 4 metrics (edit rate, type, location, pattern monitoring)
- **Clinical Transcription Accuracy**: 3 metrics (WER, M-WER, CK-ER)
- **Reference-Based Text Similarity**: 2 metrics (ROUGE, BERTScore)
- **Unaffiliated**: [remainder] metrics (those not part of a named family)
```

This makes the family structure visible at the taxonomy level rather than only at individual entry level.

**Table of contents update.** The existing Contents section lists subsections by topic. The family framings are not subsections in their own right — they are introductory text before existing metrics — so they don't need separate TOC entries. But it may be worth adding a brief note to the Contents section explaining the family convention:

```
*Several groups contain named metric families — clusters of related metrics that measure facets of a shared construct. Family framings appear before the first metric of each family and provide the parent-construct context. Individual metrics within a family carry "See also" cross-references to other members.*
```

**Interaction with the underspecification warnings from Pass 2.** Several metrics in these families carry Tier B or Tier C underspecification warnings from Pass 2 (ROUGE Tier C, BERTScore Tier C, Hallucination Rate Tier B, M-WER Tier B, CK-ER Tier B). The family framings reinforce and contextualise those warnings rather than conflicting with them — the Reference-Based Text Similarity framing is essentially an expanded version of the ROUGE and BERTScore warnings. If both passes are applied together, the warnings can be slightly shortened to avoid repetition since the family framing now carries the broader context.

**What the family framings do NOT do.** They do not:
- Rename any existing metrics
- Restructure the section ordering
- Move any metric to a different section
- Merge any entries

All of those changes would break document search, external references, and taxonomy consumers. The framings are additive context only.

---

**Pass 1 complete: 4 family framings + 14 cross-reference footers drafted.**

Next pass available:
- **Pass 3** (cross-cutting additions — ACI Bench / PriMock resource gap callout; Summary section updates to reflect new groups, sub-clusters, and the family structure from this pass; Tier 1 Quick Reference updates to reflect the 9 new Tier 1 metrics; new-group introductory paragraphs for NHS Compliance & Regulatory and Environmental & Sustainability)
