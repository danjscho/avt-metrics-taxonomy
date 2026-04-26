# v3.7 — Calibration & Context + Pipeline Tightening + Duplication Action + Bespoke Deferred-Pool Scoping

## Context

This plan opens with a new **Phase 0** — establishing context-dependent calibration as a first-class principle of the taxonomy via a new cross-cutting file `_calibration-and-context.md`, parallel to `_outcomes-boundary.md`. The principle is currently scattered across "Adapting to Local Context" prose, Threshold Guidance Provenance preludes, and individual Limitations sections; it has never been said as a top-level taxonomy-wide commitment. A reader landing on the Tier 1 Quick Reference cold could fairly read it as a fixed checklist, when in practice tier assignments and threshold numbers should be calibrated against deployment setting before contractual use.

The remaining three phases (renumbered from the original draft) cover pipeline narrow tightening, action on the v3.6 duplication review, and bespoke deferred-pool scoping. Phase 1 is detailed enough to execute against today; Phase 2 and Phase 3 remain sketched until kick-off because they depend on user sign-off (Phase 2 redundancy decisions) or external feedback (Phase 3 deferred-metric prioritisation).

After v3.6 the state is:
- 25/43 Tier 1 metrics tightened (no change in v3.6)
- Applicability now a 12th dimension on every metric
- Duplication review artefact frozen at `archive/v3.6-duplication-review.md`
- Cross-reference anchor audit check enforcing the v3.5 follow-up fix

The v3.4 classification artefact identified three remaining tightening buckets:
- **6 pipeline narrow candidates** (TP.ASR-12, TP.ASR-13, TP.WB-2, TP.WB-3, TP.WB-4, TP.SN-20) — pattern fits but applied narrowly
- **5 pattern-may-not-fit deferred** (GV.OP-6, GV.SG-9, GV.SG-11, GV.SG-13, HL.HF-3) — bespoke per-metric work
- **8 TIGHT** — explicitly not planned for tightening

**Why now:** the calibration principle should land before further tightening — once the principle is documented, every subsequent tightened metric can reference it as the reason its threshold numbers are starting points rather than fixed gates. Doing it as Phase 0 of v3.7 (rather than as a v3.6.1 hotfix) keeps the plan-on-branch convention and lets the principle compose with the duplication action and pipeline tightening that follow.

**Intended outcome:** explicit calibration-and-context principle landed as a first-class cross-cutting file; Tier 1 tightening passes the 30/43 mark via pipeline narrow tightening; duplication-review findings actioned with user sign-off; at least 1–2 of the 5 deferred metrics scoped and progressed.

---

## Phase 0 — Calibration & Context principle

### 0.1 New cross-cutting file

**File:** `taxonomy/_calibration-and-context.md`. Sits parallel to `_outcomes-boundary.md` in the assembled document order. Build.py FILES list update: insert immediately after `_outcomes-boundary.md`.

**Content sketch (final wording during execution):**

- **What's calibrated** — tier assignments, threshold numbers (pre-deployment gate, monitoring alert, pause / escalation), mandatory vs optional sub-metric breakdowns, audit cadences, sample-size floors. None of these are universal; they reflect a default deployment context that any specific deployment will need to revisit.
- **What's not calibrated** — the metric constructs themselves, the dimensional axes (Pipeline Layer / Assurance Question / Measurement Method / etc.), the Outcomes Boundary, the metric reference IDs. These are stable; calibration changes the parameters, not the structure.
- **Six deployment-setting axes** that calibration should respond to:
  - **Specialty mix** — acute vs primary care vs mental health vs paediatrics; emergency vs routine; high-stakes diagnostic vs documentation-heavy. A paediatric outpatient clinic and an A&E majors ward should not measure hallucination rate against the same threshold.
  - **Patient population** — EAL prevalence, deprivation index, accessibility needs (dysarthria, aphasia, hearing impairment), multi-party consultations (interpreter, family). Demographic-disaggregated metrics rise from Tier 2 to Tier 1 where the population's distribution is uneven.
  - **Platform maturity** — single-vendor vs mixed-vendor portfolio; integrated EHR vs federated; v1.0 vendor product vs mature deployment with N years of telemetry. Cross-platform fairness metrics shift up where platforms are mixed.
  - **Governance capacity** — embedded CSO presence, regional CCIO support, IG team depth, audit-function maturity. Audit cadences and sample-size floors are not feasible at the same level for a 4-clinician practice and a 200-clinician Trust.
  - **Risk appetite** — the DPIA-stated retention window, the contractual SLA tightness, the deployer's institutional appetite for IG-incident reportability. Threshold *gate* values are at the deployer's risk appetite; the taxonomy provides starting points, not regulator-issued numbers.
  - **Volume / scale** — per-clinician disaggregation, sampled vs full audit, weekly vs monthly cadence — feasibility shifts with the count of consultations per clinician per week. A solo GP and a Trust-scale ED workflow have different floors for "statistically meaningful".
- **How to apply the principle** — practical guidance:
  - Read the metric's Reference Standard / Operational Specification / Threshold Guidance (where present) as the **default calibration**, not the universal answer
  - Read the ⚠️ Provenance prelude carefully — cited thresholds carry external authority; proposed-as-starting-points thresholds are explicitly the calibration surface
  - Document the local calibration in the deployer's governance file alongside the DPIA and Clinical Safety Case; auditors should see both the taxonomy default and the local calibration with reasoning for differences
  - Any Tier 1 metric promoted *down* (treated as Tier 2 because of low-risk context) requires explicit justification; Tier 2/3 promoted *up* (treated as Tier 1 because of elevated context risk) is encouraged and lower-friction
- **What this is not** — not an excuse to disregard Tier 1 metrics; not a way to argue threshold numbers are negotiable in vendor contracts (the contractual gate is the deployer's local calibration, not the taxonomy's starting point); not a way to avoid the Outcomes Boundary's national-research-body responsibilities.
- **Cross-references** — explicit pointers to `_outcomes-boundary.md` (parallel principle, different boundary), `_how-to-use.md` "Adapting to Local Context" (existing prose, now subsidiary to this principle), the per-metric Threshold Guidance pattern (calibration in action).

### 0.2 Wire-ins to existing surfaces

Five edits, each pointing at the new file rather than restating. Goal: the principle is one canonical statement; surfaces link.

- **`README.md`** — add a bullet to "What this is for" naming the calibration principle as a top-level commitment alongside the Outcomes Boundary; in each per-audience section (procurement officer, vendor, developer, researcher) add one sentence reminding the reader the Tier 1 list and Threshold Guidance numbers are calibration starting points.
- **`taxonomy/_header.md`** — extend the count narrative with one clause: "...alongside the [Outcomes Boundary](#outcomes-boundary), v3.7 establishes the [Calibration & Context](#calibration-context) principle: tier assignments and threshold numbers are calibration starting points, not universal gates."
- **`taxonomy/_how-to-use.md`** — promote the existing "Adapting to Local Context" section. Top-line cross-reference to `_calibration-and-context.md`. The existing prose stays as practical guidance subsidiary to the new principle file; minor edit to align language.
- **`taxonomy/_tier-1-quick-reference.md`** — top-of-page callout (≤3 sentences): "This list is a calibrated starting point, not a fixed checklist. Local deployment context (specialty mix, patient population, platform maturity, governance capacity, risk appetite, volume) shifts both tier assignments and threshold numbers. See the [Calibration & Context principle](#calibration-context) for how to apply this."
- **`taxonomy/_outcomes-boundary.md`** — add a paragraph naming the parallel: outcomes-validation is *out of scope*; tier assignments and threshold numbers are *in scope* but *context-dependent*. The two principles together describe what the taxonomy assures and how it should be calibrated when applied.

### 0.3 Build wiring

`taxonomy/build.py` FILES list: insert `_calibration-and-context.md` immediately after `_outcomes-boundary.md`. The pair sits together as cross-cutting principle documents.

No parser changes (the new file has no structured data); no new audit check (the audit cannot verify "did the deployer calibrate properly"; the Provenance prelude on tightened metrics already does the per-metric audit work).

### 0.4 Verification

- Build clean; the new file appears in `avt-metrics-taxonomy.md` between Outcomes Boundary and the Roadmap
- Audit clean; counts unchanged (216 metrics, 43/94/79, 25/43 tightened)
- Spot-read each surfacing point as the named persona (Tier 1 reader, header reader, how-to-use reader, README arrival): does the calibration principle land before they form a fixed-checklist mental model?
- Cross-reference anchor audit check passes (the new file's anchors should resolve from the surfacing points)

---

## Phase 1 — Pipeline narrow tightening (6 metrics, was Phase A)

These are the v3.4-classified pipeline candidates: TP.ASR-12 Hallucination-Under-Noise Rate, TP.ASR-13 Numeric Accuracy, TP.WB-2 Integration Error Rate, TP.WB-3 Field Mapping Accuracy, TP.WB-4 Update vs Append Behaviour, TP.SN-20 Uncertainty Marker Preservation.

Different shape from compliance/governance (v3.5) — these are technical-pipeline metrics with narrow underspecified facets rather than wholesale loose definitions. The pattern (Reference Standard / Operational Specification / Threshold Guidance with ⚠️ Provenance prelude) still applies, but the substance per metric is targeted:

- **TP.ASR-12** — test-corpus sample sizes per non-speech category; severity weighting on spurious clinical content
- **TP.ASR-13** — sub-metric reference standards (date-format canonicalisation, unit normalisation); critical-numeric pause threshold
- **TP.WB-2** — partial-vs-degraded boundary; per-EPR stratification (parallel to TP.WB-1's v3.3 tightening); error-type taxonomy
- **TP.WB-3** — explicit field-map per-EPR reference; safety-critical categorisation cross-link to TP.WB-1
- **TP.WB-4** — correct-behaviour decision rule per context; duplicate-detection windowing; safety-critical override
- **TP.SN-20** — certainty-direction asymmetric weighting (inflation more dangerous than deflation, per existing Limitations)

After v3.7 Phase A: tightening status reaches **31/43 Tier 1** (from 25/43).

**Effort:** ~3–4 days, comparable to v3.5 Wave 1.

---

## Phase 2 — Act on duplication-review findings (input: v3.6 Phase B artefact, was Phase B)

**Sketch only — detailed planning at v3.7 kick-off.**

The v3.6 duplication review will produce a frozen artefact at `archive/v3.6-duplication-review.md` classifying every metric pair as `distinct` / `overlapping` / `redundant`. v3.7 acts on the findings:

- **`overlapping` pairs** — document the relationship explicitly in metric prose (e.g. cross-references, family or sub-cluster framing where genuinely warranted). Most likely outcome: 5–10 metrics get a See-also or family-framing addition; no structural changes.
- **`redundant` pairs** — review with user before any merges. Likely 0–5 candidates surfaced. Decision options per pair:
  - Merge (one metric absorbs the other, retired metric's content folded in, ID retired with redirect note)
  - Explicit-distinct call (clarify in prose why they are not redundant despite appearing so)
  - Cut (one metric removed entirely; rare, requires explicit user sign-off because metric IDs are stable)

**Locked decision (now):** any redundancy merges or cuts in v3.7 require explicit user sign-off per pair. Plan-mode pause before action.

**Effort:** highly variable, 0–5 days depending on count of redundancy candidates.

---

## Phase 3 — Bespoke deferred-pool scoping (input: v3.4 classification + v3.6 duplication review, was Phase C)

**Sketch only — detailed planning at v3.7 kick-off.**

The 5 pattern-may-not-fit metrics each need bespoke shape:

- **GV.OP-6 Adoption Rate & Selective Use Patterns** — the SUI threshold question is more about consultation-type taxonomy than tightening; needs a SUI-specific framing
- **GV.SG-9 Safety Performance Indicators with Thresholds (DSCMS)** — the metric *is* the threshold framework; tightening sub-blocks would be redundant, but the SPI taxonomy itself could be operationalised
- **GV.SG-11 Adverse Event / Incident Rate (LFPSE)** — LFPSE taxonomy gap acknowledged but not bridged; needs an LFPSE-AVT taxonomy proposal, not standard tightening
- **GV.SG-13 Assurance Debt Accumulation Rate** — surrogate-without-bounded-proxy-gap; needs the proxy gap bounded explicitly
- **HL.HF-3 Review-Before-Signing Rate** — the T_min thresholds are concrete but unvalidated; surrogate for review *quality*; needs a quality-bound or pairing rule

**Likely v3.7 scope:** scope and progress 1–2 of these (probably GV.SG-11 LFPSE-AVT taxonomy and HL.HF-3 quality-bound), defer the rest to v3.8+. Each is a research-grade proposal in its own right, not a mechanical tightening.

**Decision deferred to v3.7 kick-off:** which of the 5 to address first, based on (a) external feedback if any v3.5/v3.6 release attracts user comment, (b) whether the v3.6 duplication review reframes any of them.

**Effort:** ~5–10 days for 2 metrics, depending on substance.

---

## Phase 4 — Release wrap (was Phase D)

CHANGELOG v3.7 entry covers all four phases (Phase 0 + Phases 1, 2, 3). Header version bump. Tightened-count narrative in `_how-to-use.md` updated. README.md updated to reflect v3.7 status and the new Calibration & Context principle.

Counts may change if Phase 2 includes any merges (decreases total from 216) or cuts. Tier split likely unchanged.

### Branching

- Branch `v3-7-calibration-and-pipeline-tightening` off `main@v3.6`
- Phase 0 as 2 commits (one for the new file, one for the wire-ins)
- Phase 1 as 1–2 commits
- Phase 2 as N commits depending on findings (one per merge/decision; AskUserQuestion / pause before each redundancy action)
- Phase 3 as 1 commit per addressed deferred metric
- Phase 4 as final commit
- `--no-ff` merge, tag `v3.7`

---

## Critical files (sketch)

**Phase 0:**
- `taxonomy/_calibration-and-context.md` (new, principle file)
- `taxonomy/build.py` (FILES list — insert after `_outcomes-boundary.md`)
- `taxonomy/_header.md`, `taxonomy/_how-to-use.md`, `taxonomy/_tier-1-quick-reference.md`, `taxonomy/_outcomes-boundary.md`, `README.md` (wire-in surfaces)

**Phase 1:**
- `taxonomy/part-a/asr-transcription.md` (TP.ASR-12, TP.ASR-13)
- `taxonomy/part-a/epr-write-back.md` (TP.WB-2, TP.WB-3, TP.WB-4)
- `taxonomy/part-a/summarisation-nlp.md` (TP.SN-20)

**Phase 2:**
- TBD per duplication-review findings

**Phase 3:**
- TBD per metric chosen

**Phase 4:**
- `CHANGELOG.md`, `taxonomy/_header.md`, `taxonomy/_how-to-use.md`, `README.md`

---

## Verification (end-to-end, sketch)

1. Build + audit clean throughout
2. **Phase 0:** new `_calibration-and-context.md` appears in assembled `avt-metrics-taxonomy.md` between Outcomes Boundary and Roadmap; all five wire-in surfaces resolve their cross-references via the cross-reference audit check; the principle is named (not just buried) at every surface — README, header, how-to-use, tier-1-quickref, outcomes-boundary
3. **Phase 1:** Tightening status manifest reaches **31/43** after Phase 1
4. **Phase 2:** Duplication-review actions traceable to the v3.6 artefact (every redundancy decision references the pair from the artefact); user sign-off recorded per merge/cut decision
5. **Phase 3:** scope of addressed deferred metrics named explicitly; remaining deferred metrics named in CHANGELOG for v3.8+
6. v3.5 / v3.6 follow-ups status — confirm none reopened by v3.7 changes
7. CHANGELOG v3.7 entry names the deferred metrics not addressed (so v3.8+ scope is auto-tracked)

---

## Out of scope (defer to v3.8+)

- Tier 2 / Tier 3 tightening — Tier 1 hasn't even completed yet; the pattern hasn't been validated against non-Tier-1 metrics
- Outcomes layer extension beyond ES.ME-8/9
- Roadmap (`_gaps.md`) candidate promotion — 89 candidates remain queued
- Stakeholder review process / public release — that's a separate workstream not yet scoped here
- Site-side improvements (procurement wizard, filter-by-context, etc. — flagged in earlier critique as missing but not on the tightening pipeline)

---

## Open questions for v3.7 kick-off

1. **Phase 0 scope confirmed:** strong/structural option (new `_calibration-and-context.md` cross-cutting file); six deployment-setting axes (specialty / population / platform / governance / risk appetite / volume) as the structural frame. User confirmed 2026-04-26.
2. **Has v3.5 / v3.6 attracted external feedback?** If yes, that may reframe Phase 2 or Phase 3 priorities.
3. **Phase 2 sign-off cadence.** Locked decision: any redundancy merges or cuts in v3.7 require explicit user sign-off per pair. Pause before each action.
4. **Which of the 5 deferred metrics to address first in Phase 3?** GV.SG-11 (LFPSE-AVT taxonomy) is the most externally-relevant; HL.HF-3 (review-quality bound) is the most internally-coherent given v3.5's HL.HF-1 / HL.HF-4 pairing. Pick one or both at kick-off.
