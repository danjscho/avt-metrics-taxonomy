# v3.3 — Outcomes Boundary + Tier 1 Definitional Tightening (Phase 1+2)

## Context

The v3.2 release (just merged to `main`, tag `v3.2`) shipped the modular restructure, MkDocs Material site, RSET + NHSE IG external coverage audits, NHS T.E.S.T. mapping, and the consolidated 89-candidate roadmap. A subsequent critique surfaced two structural weaknesses that v3.2 didn't address:

1. **Outcome blindness.** All 214 metrics measure process, structure, or surrogates. Zero address actual clinical outcomes (diagnostic accuracy change, patient safety incident change, downstream care quality). T.E.S.T. Section B awards 50 points for RCT/clinical-validation evidence; the taxonomy has no scaffold for it. The taxonomy's own [ES.ME-1 Proximal vs Distal Outcome Distinction](../../projects/claude/avt-taxonomy/taxonomy/part-f/meta-evaluation.md) acknowledges the gap (cites Coiera & Fraile-Navarro 2026) but does nothing to close it.

2. **Definitional looseness in Tier 1.** A sample of 20 of 43 Tier 1 metrics found ~65% LOOSE (formal definition uses unoperationalised terms like "supported", "appropriate", "accurate" without specifying reference standard, measurement window, population, or thresholds) and ~7% SURROGATE (proxy without bounded proxy gap). Vendors reading these can comply selectively; cross-vendor comparability is broken. Existing Tier A/B/C underspecification warnings catch concept-level uncertainty but miss operational-definition gaps.

v3.3 addresses both with a focused, honest pass. Scope is deliberately narrow — outcomes boundary frames the work; tightening proves the new pattern on the highest-value Tier 1 metrics; Phase 3 + the deferred 15-metric pool are explicitly punted to v3.4.

**Why now:** the user is considering using the taxonomy in practice (procurement / Trust deployment evaluation). v3.2 is shippable but a sceptical clinical safety officer or measurement scientist would land both criticisms. v3.3 closes the credibility-critical gaps without inflating scope.

**Intended outcome:** taxonomy that an NHS procurement lead can defend on Monday morning — Tier 1 metrics that two vendors will measure the same way, an explicit boundary around what the taxonomy assures vs what national bodies must validate, and a transparent forward plan for the rest.

---

## Phase A — Outcomes Boundary (smaller, frames everything else)

### A1. Author the out-of-scope statement

**New file:** `taxonomy/_outcomes-boundary.md` (cross-cutting, sits alongside `_responsible-ai-lens.md` and `_standards-mapping.md`).

Content (sketch — final wording during execution):

- **What this taxonomy assures:** technical fidelity, documentation accuracy, clinician oversight, hazard identification, governance compliance, deployment safety. Process + structure + surrogates.
- **What it does not:** clinical outcome validation. RCT-grade evidence that AVT improves diagnostic accuracy, reduces adverse events, or changes downstream care quality is *out of scope*. Reasoning: outcome validation requires multi-site randomised designs, longitudinal follow-up, and case-mix controls that no individual deployer is equipped to run; it is the responsibility of national research bodies (NIHR RSET), regulatory frameworks (MHRA PMS, NICE ESF Tier C evidence requirements), and vendors pursuing formal clinical claims.
- **What deployers should do instead:** require vendors to commit to post-market outcome studies (see new ES.ME-8/9 below); require T.E.S.T. Section B RCT evidence (50 pts) where Gold certification is sought; treat proximal metrics as deployment-safety signals, not as evidence of clinical benefit.
- **Cross-references:** ES.ME-1 (proximal/distal causal logic), T.E.S.T. Section B (RCT scoring), MHRA PMS (effectiveness evidence requirements).

**Build integration:** add `_outcomes-boundary.md` to `taxonomy/build.py` ordered list (between `_responsible-ai-lens.md` and `_standards-mapping.md`). Add to `_contents.md` under a new "Cross-cutting" section if one doesn't already exist, otherwise alongside other underscore files.

### A2. Two ES.ME meta-metrics (commitment, not measurement)

These are *not* outcome metrics — they measure whether the infrastructure for outcome evaluation exists. That's what the taxonomy can honestly assess.

| Ref | Title | Tier | What it measures |
|---|---|---|---|
| **ES.ME-8** | Outcome Evidence Commitment Status | 🟡 2 | Has the vendor committed (contractually or via published protocol) to a pre/post or RCT outcome study? Is a clinical trial protocol registered? Is post-market surveillance with outcome capture planned? Binary checkboxes with evidence required. |
| **ES.ME-9** | Causal Model Operationalisation | 🟡 2 | Has the vendor specified the causal chain (e.g. ASR accuracy → note quality → clinician decision quality → patient outcome) and identified which proximal metrics in this taxonomy serve as proxies for which distal outcomes? Aligns with ES.ME-1's "burden of proof on vendors" requirement and makes it operational. |

**Format:** standard taxonomy entry — dimensions table, Why this tier?, Formal Definition, Limitations, Novel Thinking. Code snippet optional (probably not appropriate for these — they're documentation checks, not computational).

**Tier 2** because they're "Recommended" — not safety-critical pre-deployment gates, but expected for any procurement above pilot scale. Placement: `taxonomy/part-f/meta-evaluation.md`, appended to existing 7 metrics.

### A3. Wire to existing structure

- **ES.ME-1** prose: small revision — clarify that ES.ME-1 names the burden of proof, ES.ME-8/9 measure whether vendors have met it. No metric ID changes, no renumbering.
- **`_standards-mapping.md` T.E.S.T. Section B**: update the row for benefit domain 1 (Clinical Effectiveness — RCT validation 50 pts) to reference ES.ME-8 as the closest proxy, with explicit note that the metric measures *commitment*, not the RCT evidence itself.
- **`_summary.md`**: 214 → 216 metrics; tier counts 43 / 92 + 2 / 79 → **43 / 94 / 79**.
- **`_contents.md`**: Meta-evaluation count 7 → 9.
- **`_applicability.md`**: increment categories these two land in (probably "General Healthcare AI" + "Cross-cutting").
- **`audit.py`**: should pass without modification (parser is generic) — but verify after build.

### A4. Verification

- `python3 taxonomy/build.py` — clean, 216 metrics
- `python3 taxonomy/audit.py` — clean
- New file `_outcomes-boundary.md` appears in the assembled `avt-metrics-taxonomy.md`
- `dist/metrics.json` contains ES.ME-8 and ES.ME-9
- Site builds (smoke test only — no need to deploy)

---

## Phase B — Tier 1 Definitional Tightening (Phase 1+2 from earlier scoping)

### B1. The tightening template

Add three structured sub-blocks to each tightened metric, *between* "Formal Definition" and "Limitations":

```
**Reference Standard**
> What counts as ground truth. Tool / dataset / human-review protocol; inter-rater
> reliability target where applicable.

**Operational Specification**
> - Measurement window (per-note, per-encounter, per-day, per-clinician, etc.)
> - Population scope (all consultations, sampled, exclusions)
> - Severity / category breakdown if applicable, with mandatory reporting requirement
> - Aggregation rule (weighted vs unweighted)

**Threshold Guidance**
> - Pre-deployment gate value
> - Continuous monitoring alert threshold
> - Pause / escalation trigger
```

This pattern lifts existing-but-buried content (much of which already lives in the prose Limitations / Novel Thinking / Underspecification Warning sections) into a discoverable, comparable structure. It does not invent new science — it makes existing knowledge actionable.

### B2. Phase 1 — five safety-critical metrics

| Ref | File | Why first |
|---|---|---|
| **TP.SN-5** Hallucination Rate | `taxonomy/part-a/summarisation-nlp.md` | The most visibly underspecified Tier 1; cited in critiques; existing Tier B warning provides much of the raw material |
| **TP.SN-6** Omission Rate | `taxonomy/part-a/summarisation-nlp.md` | Same "supported by transcript" definition problem; pairs naturally with TP.SN-5 |
| **TP.SN-15** Negation Handling Accuracy | `taxonomy/part-a/summarisation-nlp.md` | "Negation marker" undefined (explicit / implicit / hedged / conditional / historical); high clinical-safety stakes |
| **HL.HF-1** Edit Rate | `taxonomy/part-c/human-factors-workflow.md` | "Edit" undefined (any keystroke vs semantic vs clinically meaningful); baseline undefined; surrogate-without-bounded-proxy-gap |
| **TP.WB-1** Write-back Fidelity | `taxonomy/part-a/epr-write-back.md` | "Fidelity" undefined; structural vs semantic equivalence not distinguished |

**Friction expectation:** moderate. Vendors typically *have* subtype/severity data; resistance will be to making it mandatory in reporting.

### B3. Phase 2 — four compliance/consent metrics

| Ref | File | Why |
|---|---|---|
| **GV.PD-1** Audio Retention Compliance | `taxonomy/part-e/privacy-data-governance.md` | "Compliant retention" undefined re: which standard, audit window |
| **GV.PD-3** Transcript Retention Compliance | `taxonomy/part-e/privacy-data-governance.md` | Same as above for transcripts |
| **GV.CR-1** Patient Dissent Recording Rate | `taxonomy/part-e/nhs-compliance-regulatory.md` | "Dissent" definition (verbal / formal / opt-out checkbox), recording window |
| **GV.CR-2** Verbal Notification Compliance | `taxonomy/part-e/nhs-compliance-regulatory.md` | What counts as compliant verbal notification; audit method |

**Friction expectation:** low. These are often already operationalised in DPIAs and IG documentation; tightening just imports that into the metric.

### B4. Worked example (Phase 1, applied to TP.SN-5)

Existing definition:
```
HR = |S_unsupported| / |S_total|, where S_total = atomic propositions in generated note,
S_unsupported = subset not evidentially supported by source transcript.
Severity: benign (formatting), moderate (non-safety addition), critical (fabricated clinical content).
```

Tightened (sketch — final wording during execution):

```
**Reference Standard**
> Source transcript is primary ground truth. Atomic propositions classified
> {Fully Supported, Partially Supported, Unsupported} via structured clinician review
> using CREOLA subtype taxonomy (Asgari et al. 2025). Unsupported = hallucination.
> Inter-rater reliability target: ICC ≥ 0.75 on the subtype classification.
> NLI-based automated detection (e.g. CHECK framework, arXiv 2506.11129) acceptable
> as a primary screen if reported AUC ≥ 0.90 against human-reviewed reference set.

**Operational Specification**
> - Window: per-note (not per-sentence aggregate), all atomic propositions.
> - Population: all clinical consultations during the measurement period;
>   exclude transcription failures (ASR confidence < 0.7).
> - Subtype reporting MANDATORY: aggregate rate plus CREOLA subtype breakdown
>   (Fabrication / Context Conflation / Incorrect Negation / Speculation /
>   Certainty Inflation).
> - Severity classification MANDATORY (benign / moderate / critical).
> - Weighted aggregate: HR_w = (0.1·benign + 0.5·moderate + 1.0·critical) / N_total.

**Threshold Guidance**
> - Pre-deployment gate: HR_w ≤ 2 % on representative 500-note test set;
>   critical-subtype rate < 0.5 %.
> - Continuous monitoring: weekly HR_w; alert if > 3 % sustained two weeks
>   or any new critical subtype.
> - Pause trigger: critical-subtype rate ≥ 5 % or HR_w > 5 % for three consecutive days.
```

The Tier B underspecification warning **stays** — it documents the field-level concept instability — but is now backed by an operational specification that lets a deployer act despite the instability.

### B5. Cross-cutting changes

- **`_summary.md`**: add a short note that nine Tier 1 metrics now carry the structured Reference Standard / Operational Specification / Threshold Guidance pattern, and that this pattern will be extended in v3.4.
- **`_how-to-use.md`**: add one paragraph explaining the new sub-block structure to readers ("for tightened metrics, the Operational Specification block is what your vendor must comply with; the Threshold Guidance block is what triggers escalation").
- **`audit.py`**: optional — could add a check that flags Tier 1 metrics *missing* the three new sub-blocks, so the rest can be visibly tracked. Decision deferred to execution: if the parser already handles arbitrary blocks (it does, per `parse.py`), then a separate audit check is the right place. Otherwise punt to v3.4.
- **CHANGELOG v3.3 entry**: explain the pattern, list the 9 tightened metrics, declare the remaining ~21 LOOSE/SURROGATE Tier 1 metrics as v3.4 scope.

### B6. Verification

- For each of the 9 tightened metrics: a competent reviewer reading only the metric entry should be able to specify the measurement to a vendor without further consultation.
- `audit.py` passes.
- Build clean; metric count unchanged for tightened metrics (216 total after Phase A).
- Spot-check three of the nine in the rendered site to confirm formatting holds.

---

## Phase C — Forward declaration

Add a "Known follow-ups" section at the end of CHANGELOG v3.3 (or append to `_outcomes-boundary.md`) explicitly naming what's deferred:

- **Phase 3 tightening (4 operational/proxy metrics)**: GV.OP-1, HL.HF-4, IO.PX-1, GV.SG-1.
- **Remaining LOOSE/SURROGATE Tier 1 pool (~17 metrics)**: identified during the v3.3 pass; full list and disposition in v3.4.
- **Outcomes layer**: explicitly *not* extended beyond ES.ME-8/9 — reaffirm out-of-scope position.
- **Roadmap**: 89 candidates remain in `_gaps.md`; v3.3 does not promote any of them to metrics.

This gives anyone using v3.3 in earnest a clear forward roadmap and prevents the "is this finished?" ambiguity.

---

## Critical files

**Phase A:**
- `taxonomy/_outcomes-boundary.md` (new)
- `taxonomy/part-f/meta-evaluation.md` (append ES.ME-8, ES.ME-9; tweak ES.ME-1 prose)
- `taxonomy/build.py` (add new file to ordered list)
- `taxonomy/_contents.md`, `_summary.md`, `_applicability.md` (count updates)
- `taxonomy/_standards-mapping.md` (T.E.S.T. Section B row update)

**Phase B:**
- `taxonomy/part-a/summarisation-nlp.md` (TP.SN-5, TP.SN-6, TP.SN-15)
- `taxonomy/part-a/epr-write-back.md` (TP.WB-1)
- `taxonomy/part-c/human-factors-workflow.md` (HL.HF-1)
- `taxonomy/part-e/privacy-data-governance.md` (GV.PD-1, GV.PD-3)
- `taxonomy/part-e/nhs-compliance-regulatory.md` (GV.CR-1, GV.CR-2)
- `taxonomy/_how-to-use.md` (one paragraph on the tightening pattern)
- `taxonomy/_summary.md` (note the pattern)

**Release:**
- `CHANGELOG.md` (v3.3 entry)

---

## Functions & utilities to reuse

- `taxonomy/parse.py` — already extracts metric structure from markdown; the new sub-blocks will parse as additional sections within each metric's body. No parser changes expected.
- `taxonomy/build.py` — generic file-list assembly; only needs the new `_outcomes-boundary.md` added to the order.
- `taxonomy/audit.py` — generic structural checks (ID uniqueness, tier consistency, dimension table completeness). Should pass unchanged. Optional v3.3 enhancement: a check that flags Tier 1 metrics not yet using the tightening pattern, so v3.4 scope is auto-tracked.
- `taxonomy/_gaps.md` parser registration in `parse.py` `_GAP_SECTIONS` — unchanged; nothing in v3.3 modifies the roadmap structure.

---

## Branching & release

Match the v3.2 pattern:
- Branch: `v3-3-outcomes-and-tightening` off `main@v3.2`
- Phase A as one or two commits; Phase B as 2-3 commits (Phase 1 metrics, Phase 2 metrics, then cross-cutting); CHANGELOG entry as final commit
- Merge with `--no-ff`, tag `v3.3`
- All commits 🦞-prefixed

---

## Verification (end-to-end)

1. **Build clean:** `python3 taxonomy/build.py` reports 216 metrics across 20 groups; `dist/summary.json` shows `43 / 94 / 79` tier split.
2. **Audit clean:** `python3 taxonomy/audit.py` — zero findings.
3. **Boundary statement readable:** `_outcomes-boundary.md` is in the assembled monolithic markdown and renders on the site.
4. **ES.ME-8 / ES.ME-9 parsed:** `dist/metrics.json` contains both with correct tier and dimensions.
5. **Tightening pattern visible:** spot-check TP.SN-5, HL.HF-1, GV.CR-1 in `avt-metrics-taxonomy.md` — three sub-blocks present, formatted consistently.
6. **Procurement-officer test (qualitative):** read TP.SN-5 cold and answer the six questions previously listed (definition of "supported", reference standard, severity weighting, measurement window, subtype reporting, thresholds). All six should be answerable from the metric entry.
7. **Site smoke test:** `python3 taxonomy/build_site.py` (or whatever drives MkDocs) succeeds; no broken cross-references.
8. **CHANGELOG:** v3.3 entry exists, lists tightened metrics by ID, declares Phase 3 + remaining pool as v3.4 scope.
