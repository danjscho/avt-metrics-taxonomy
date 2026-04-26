# v3.6 — Applicability Alignment + Duplication Review + v3.5 Follow-ups

## Context

v3.5 shipped 2026-04-25 with 25 of 43 Tier 1 metrics tightened (Wave 1 compliance/governance + Wave 2 privacy-chain). A self-review surfaced four follow-up items, and the user identified two architectural improvements worth landing before more tightening:

1. **Applicability-on-metric alignment.** Currently each metric carries 11 dimensions in its table (Reference, Priority Tier, Cadence, Pipeline Layer, Assurance Question, Measurement Method, Lifecycle Phases, Responsible Actors, Maturity, Outcome Type, Source). The 12th conceptual axis — Applicability classification (AVT-Specific / AVT-Contextualised / General Healthcare AI) — lives separately in `taxonomy/_applicability.md` as a lookup table. This is an architectural inconsistency: every other axis is stored on the metric; this one is stored on a parallel file. Contributors adding a metric must remember to update both files; the parser has to merge two sources.

2. **Duplication review.** With 216 metrics across 20 groups there are likely overlapping constructs (e.g. TP.SN-5 Hallucination Rate / TP.SN-7 Confabulation Detection / TP.SN-8 VeriFact Factual Verification all measure facets of factual support). A systematic per-pair audit within groups (and cross-group where flagged) produces a research artefact paralleling the v3.4 tightening classification — surfaces candidates without committing to fixes.

3. **v3.5 follow-up items.** The self-review on v3.5 named four small honesty / structural issues sitting on the shipped release. These are cheap to fix and worth clearing before v3.7's pipeline tightening so they don't accumulate. (Judgement call: could defer to v3.7 if you want v3.6 kept tight to the alignment theme — see Phase D below.)

**Why now:** the alignment work fixes a real source-of-truth ambiguity that gets harder to resolve every release; the duplication audit produces an input artefact for v3.7+ scoping (parallels v3.4's classification document); the v3.5 follow-ups close known issues while context is fresh.

**Intended outcome:** every metric carries its own applicability classification (parser drops the lookup); a frozen duplication review document identifies overlap/redundancy candidates without acting on them; the four v3.5 follow-ups are addressed.

---

## Phase A — Applicability-on-metric alignment

### A1. Add Applicability dimension to every metric

Add an **Applicability** row to every metric's dimension table, immediately after **Outcome Type** (the existing 10th row before Source). Values: `AVT-Specific` / `AVT-Contextualised` / `General Healthcare AI` — exact strings from the existing `_applicability.md` taxonomy.

The values come from `_applicability.md` itself — every metric is already classified there. The work is mechanical: extract the per-metric value from `_applicability.md`, write it into the metric's dimension table.

**Scope: 216 metrics across 20 group files.**

### A2. parse.py extension

Add `applicability` to the parsed Metric fields. Extraction is via the same generic dimension-row regex already used for the other 10 axes. Audit constants `EXPECTED_APPLICABILITY` already exist; they just need to be reconciled against per-metric values rather than against the standalone file.

### A3. audit.py — new check `applicability-presence` and reconciliation

- New audit check: every metric has an `Applicability` row in its dimension table. Missing row = ERROR.
- Update existing `check_applicability_totals` to derive totals from per-metric values rather than from `_applicability.md`. Cross-validate against `_applicability.md` declared totals during the transition release; once stable in v3.7, the standalone `_applicability.md` totals become a derived view.
- Constants `EXPECTED_APPLICABILITY = {"AVT-Specific": 48, "AVT-Contextualised": 77, "General Healthcare AI": 91}` continue to gate the totals.

### A4. `_applicability.md` becomes a derived presentation

The classification rationale prose stays (it's the document that explains *why* the three classes exist and what they mean — that's not metric-resident content). The per-metric tables become derivable from the metrics themselves. For v3.6 the file stays human-edited; v3.7 (or later) can move to script-generated tables driven by `dist/metrics.json`.

### A5. Verification

- `python3 taxonomy/build.py` clean; `dist/metrics.json` contains an `applicability` field on every metric
- `python3 taxonomy/audit.py` clean — applicability-presence check passes for all 216 metrics; derived totals match declared totals (48 / 77 / 91 / 216)
- Spot-check 5 metrics across different groups: dimension table includes Applicability row with correct value
- Smoke-test fault injection: remove Applicability row from one metric → audit fails with `applicability-presence` ERROR

---

## Phase B — Duplication review (research artefact)

### B1. Methodology

**Within-group sweep first.** Overlap is much more likely within a group than across (same authors, same source material). For each of the 20 group files, list every metric pair and classify:

- **distinct** — different constructs, different data sources, no measurement overlap. Default classification.
- **overlapping** — different views of the same underlying construct OR shared data sources where reporting one would meaningfully inform the other. Example candidate: GV.PD-1 Audio Retention Compliance and GV.PD-2 Audio Time-to-Deletion.
- **redundant** — same construct measured the same way; one should be merged into or cut in favour of the other.

**Then cross-group for flagged candidates.** For metrics flagged `overlapping` or `redundant` within their group, check whether they also overlap with metrics in other groups. The Demographic Equity Disaggregation family already cross-cuts; that's a known pattern. Look for un-named cross-group overlaps.

### B2. Candidate hot-spots (informed guess pre-audit)

- **TP.SN family** — Hallucination Rate (TP.SN-5), Omission Rate (TP.SN-6), Confabulation Detection (TP.SN-7), VeriFact (TP.SN-8), MedHELM (TP.SN-10), MEDIC (TP.SN-11), CHECK in TP.SN-5's prose. All facets of factual support / clinical accuracy.
- **HL.HF Edit family** — Edit Rate, Edit Type, Edit Location, Edit-Pattern Monitoring at Scale. The family framing exists; the question is whether the four sub-metrics genuinely measure different things or whether some are decorative.
- **GV.PD retention chain** — GV.PD-1 (Compliance) and GV.PD-2 (Time-to-Deletion) is the obvious pair. After v3.5's tightening they are now explicitly cross-linked, but the question of whether they're genuinely two metrics or one metric with two views is open.
- **GV.SG.SafetyPerformance** — Adverse Event Rate (GV.SG-11), Near-Miss Rate (GV.SG-14), Time-to-Correct (GV.SG-15), DSCMS SPI thresholds (GV.SG-9). Leading-vs-lagging structure is intentional but should be documented as such.
- **TP.CC coding family** — SNOMED Code Accuracy (TP.CC-1), SNOMED Concept Mapping (TP.CC-2), Code Specificity (TP.CC-11). Possibly distinct, possibly nested.

### B3. Output document

`archive/v3.6-duplication-review.md` (frozen at v3.6 ship date). Per-group tables listing pairs with classification + one-sentence reasoning. Final tally:

| Bucket | Count | v3.7+ disposition |
|---|---|---|
| distinct | (most) | No action |
| overlapping | TBD | Document the relationship explicitly in metric prose; consider family / sub-cluster framing |
| redundant | TBD (likely 0–5) | Merge / cut decisions in v3.7 with explicit user sign-off |

### B4. Verification

- Document exists at `archive/v3.6-duplication-review.md` covering all 20 groups
- Every overlapping/redundant flag has explicit reasoning
- Cross-group overlap section covers the candidates surfaced by the within-group sweep
- v3.7 scope clearly stated (e.g. "5 redundancy candidates flagged for review; recommendation: review with user before any merges")

---

## Phase C — v3.5 follow-up items

The four issues identified in the v3.5 self-review:

### C1. Cross-reference anchor validation

The v3.5 cohort introduced many internal cross-references (e.g. `[GV.SG-2 Model Update Impact Score](#gvsg-2-model-update-impact-score)`). I haven't validated the anchor format actually resolves under MkDocs Material. Add an audit check:

- For every Markdown link of the form `[...](#anchor)` in any metric body, confirm the anchor resolves to an existing metric heading (using the `parse.py`-extracted slug logic from `build_site.py`).
- Output as ERROR if unresolved (not WARN — broken links are a quality signal users will see).
- Sweep all 25 tightened metrics, not just v3.5 — fixes any latent issues from v3.3 / v3.4 too.

### C2. GV.CR-5 carve-out circularity

The metric assumes a regional CCIO with capacity to escalate to. The CIO/CCIO guidance v2 (Jan 2026) doesn't necessarily provide that. Add a Limitations addendum acknowledging the assumption — one paragraph, not a structural change.

### C3. GV.CR-6 30-day window honesty fix

I wrote that DCB0129 sections 2-5 must be updated within 30 days of a trigger event. DCB0129 says "must be current" without specifying 30 days. The Threshold Guidance Provenance line marks the 30-day number as proposed-as-starting-point, but the Operational Specification reads as if it's a regulatory expectation. Reword the Op Spec sentence to make the gap more visible: "30 days (proposed; DCB0129 itself does not specify a numeric window — see Threshold Guidance Provenance)".

### C4. GV.PD-8 survey-instrument honesty

I wrote "validated published instrument, or where unavailable, a deployer-defined survey." There is almost certainly no validated AVT-specific patient-comprehension instrument. Reword to acknowledge this directly: "No validated AVT-specific patient-comprehension instrument exists; deployers should select the closest healthcare-IT-comprehension instrument and document the limitation, or commission a deployer-defined survey reviewed by the IG team."

### C5. Verification

- `audit.py` cross-reference check passes after fixing any unresolved anchors
- Three prose updates land cleanly (build clean, audit clean)
- v3.5 follow-up section in CHANGELOG v3.6 entry names what was fixed

---

## Phase D — Repo-root README.md

The repo currently has `taxonomy/README.md` (developer-oriented build guide) but no `README.md` at the repository root — the file GitHub renders as the landing page when someone arrives at the project URL. This is a visibility gap: the project is published, the MkDocs site exists, but the GitHub-arrival experience is "no README, browse the directory."

### D1. Author the repo-root README.md

**File:** `README.md` at repo root.

**Audience and tone:** someone landing on the GitHub URL cold — could be a clinician, a procurement officer, a developer, or a researcher. Lead with what the project is and why; secondary detail for each audience.

**Sections (sketch — final wording during execution):**

1. **One-paragraph project description** — "Healthcare metrics taxonomy for assuring NHS Ambient Voice Technology systems. 216 metrics across 20 groups covering audio capture through to EPR write-back, plus governance, human factors, equity, and meta-evaluation. Draft v3.6 — under active review, not yet stakeholder-approved."

2. **Quick links** — published site (when URL stable), `avt-metrics-taxonomy.md` for the monolithic markdown, `dist/metrics.csv` and `dist/metrics.json` for structured data, `CHANGELOG.md` for release history.

3. **What's in scope vs out of scope** — three-bullet summary linking to the [Outcomes Boundary](taxonomy/_outcomes-boundary.md) document (this taxonomy assures deployment safety; clinical-outcome validation is national-research-body work).

4. **Per-audience entry points:**
   - **Procurement officer / clinical safety officer** — start with the Tier 1 Quick Reference; the 25/43 tightened metrics carry concrete Reference Standard / Operational Specification / Threshold Guidance sub-blocks; the Provenance preludes flag which thresholds are cited vs proposed-as-starting-points.
   - **Vendor** — see standards-mapping for the 12 framework alignments (DTAC, DSPT, DCB0129/0160, MHRA, NICE, NHS T.E.S.T., FHIR UK Core, CQC, PSIRF, PRSB, Caldicott, NHS England LLM Evaluation Framework).
   - **Developer / contributor** — see `taxonomy/README.md` for the build pipeline, `taxonomy/audit.py` for the structural audit, the `archive/` for plans and classification artefacts.
   - **Researcher** — see `_responsible-ai-lens.md` for DSIT AI Playbook and ethical-theme mappings; `_gaps.md` for the 89-candidate roadmap; `archive/v3.3-tier1-classification.md` for the LOOSE/TIGHT/SURROGATE classification.

5. **Build / audit one-liner** — `python3 taxonomy/build.py && python3 taxonomy/audit.py`.

6. **Status / version** — current draft version, last release date, link to CHANGELOG. Note that draft status means content / tier assignments / cross-references may change.

7. **Citation guidance** — how to cite this draft (e.g. "Schofield D, AVT Metrics Taxonomy v3.6, [URL], 2026") with the explicit warning that the draft is not a settled standard.

8. **Contributions / contact** — minimum: GitHub issues for proposed gaps and corrections; reference the CONTRIBUTING flow if one exists (or note it doesn't yet).

9. **Licence** — TBD if not already declared elsewhere; check before writing this section.

### D2. Verification

- File exists at repo root; renders correctly on GitHub
- Every internal link resolves (use the cross-reference audit check from Phase C)
- Spot-read each per-audience section as the named persona — does it actually point at what they need?
- One-liner build/audit command works copy-pasted

### D3. Maintenance commitment

The repo-root README needs to track version-bumps and major structural changes. Add a one-line note at the bottom: "Last updated: v3.6 / [date]." This is a low-effort discipline; v3.7's release-wrap should refresh it.

---

## Phase E — Release wrap

CHANGELOG v3.6 entry covers Phases A, B, C, D with explicit deferrals to v3.7. Header version bump to v3.6 / [date]. `_how-to-use.md` updated to mention the new Applicability dimension once the alignment is in place. Repo-root `README.md` references the new version.

Counts unchanged at the metric level (216 / 43-94-79). Manifest after v3.6 unchanged at 25/43 tightened.

### Branching

- Branch `v3-6-applicability-alignment-and-duplication` off `main@v3.5`
- Phase A as 1–2 commits (the 216 dimension-table edits will probably sub-divide by part directory)
- Phase B as 1 commit (artefact creation)
- Phase C as 1 commit per follow-up (4 commits) so each fix is reviewable independently
- Phase D as 1 commit (repo-root README)
- Phase E as final commit (CHANGELOG + header + how-to-use)
- `--no-ff` merge, tag `v3.6`
- All commits 🦞-prefixed

---

## Critical files

**Phase A:**
- All 20 `taxonomy/part-*/*.md` group files (Applicability row added to every metric)
- `taxonomy/parse.py` (extract Applicability from dimension table)
- `taxonomy/audit.py` (new `check_applicability_presence`; update `check_applicability_totals` to derive from per-metric)

**Phase B:**
- `archive/v3.6-duplication-review.md` (new research artefact)

**Phase C:**
- `taxonomy/audit.py` (cross-reference anchor check)
- `taxonomy/part-e/nhs-compliance-regulatory.md` (GV.CR-5 Limitations addition; GV.CR-6 Op Spec rewording)
- `taxonomy/part-e/privacy-data-governance.md` (GV.PD-8 reference-standard rewording)
- Any metric with broken cross-references identified by the new audit check

**Phase D:**
- `README.md` (new, at repo root)

**Phase E:**
- `CHANGELOG.md`
- `taxonomy/_header.md`
- `taxonomy/_how-to-use.md`

---

## Verification (end-to-end)

1. Build clean: `python3 taxonomy/build.py` reports 216 metrics; `dist/metrics.json` contains Applicability on every metric
2. Audit clean: zero findings; derived applicability totals match (48 / 77 / 91 / 216); cross-reference anchor check passes
3. Spot-check fault injection: remove an Applicability row → audit fails appropriately; restore
4. Spot-check fault injection: introduce a broken `[...](#nonexistent)` link → audit fails; restore
5. Duplication artefact exists, covers all 20 groups, classifies every within-group pair
6. CHANGELOG v3.6 entry exists, names the v3.5 follow-ups fixed, defers to v3.7 explicitly where needed

---

## Out of scope (defer to v3.7)

- Pipeline narrow tightening (TP.ASR-12, TP.ASR-13, TP.WB-2/-3/-4, TP.SN-20)
- Acting on duplication findings (merges or cuts) — Phase B produces the artefact, v3.7 acts on it with user sign-off
- Pattern-may-not-fit deferred metrics (GV.OP-6, GV.SG-9/-11/-13, HL.HF-3) — bespoke per-metric work, scoped after Phase B duplication review may reframe some
- Outcomes layer extension beyond ES.ME-8/9
- Roadmap (`_gaps.md`) — 89 candidates remain queued
