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

User reviewed `archive/v3.6-duplication-review.md` on 2026-04-26 and confirmed:

- **Redundancy candidates handled as sub-parts under a single parent metric** (a/b/c suffix scheme). Goal: keep both implementations under a coherent parent construct without information loss.
- **Cross-references / new family framings handled mechanically** for the ~15 overlapping-but-not-framed pairs.
- **US-flavour audit** added: brief sweep of the 216 metrics for US-isms (wRVU, Medicare-style references, E/M coding); each surfaced metric handled by adding NHS framing rather than removal.

### 2.1 Redundancy as sub-parts (3 candidates, sub-parts approach)

For the three flagged redundancy candidates, a parent metric is introduced at the natural ID position absorbing the existing metrics as sub-parts (`-Na` / `-Nb`):

| Parent | Sub-parts | Construct | Retired IDs |
|---|---|---|---|
| **TP.SN-7 Factual Verification** | TP.SN-7a Confabulation Detection (Support × Severity) → was TP.SN-7; TP.SN-7b VeriFact Factual Verification → was TP.SN-8 | Two implementations of factual support verification (Abridge framework / Chung et al. 2025 instrument) | TP.SN-8 |
| **TP.SN-9 LLM-Judge Methodology** | TP.SN-9a LLM-as-a-Judge (PDSQI-9 Proxy) → was TP.SN-9; TP.SN-9b MedHELM LLM-Jury → was TP.SN-10 | Two configurations of LLM-judge methodology (single judge / ensemble jury); paired with [ES.ME-6 LLM-Judge Bias Quantification](#es-me-6) for meta-evaluation | TP.SN-10 |
| **HL.HF-3 Inadequate-Review Detection** | HL.HF-3a Review-Before-Signing Rate → was HL.HF-3; HL.HF-3b Time-to-Sign Distribution → was HL.HF-4 | Two telemetry approaches to detecting inadequate clinician review (binary edit/scroll/dwell signal / TTS distribution); v3.4 already mandated pairing | HL.HF-4 |

**Locked design decisions:**

- **Deprecate, don't renumber.** Retired IDs (TP.SN-8, TP.SN-10, HL.HF-4) are NOT reused; the integer sequence carries gaps. Reasoning: reference IDs are a public API — every prior taxonomy version, the standards-mapping file, the v3.4 Tier 1 classification artefact, the v3.6 duplication review, and any external citation references the existing IDs. Renumbering breaks them all; deprecation breaks none. Retired IDs get a one-line redirect note in the metric file ("Retired in v3.7; see TP.SN-7b") and the audit emits a known-retired-IDs status line.
- **Parent metric introduced as a new construct heading at the natural ID position.** Parent inherits the dimension table from the most-Tier-elevated child (e.g. TP.SN-7 inherits from TP.SN-7a, the existing Tier 3 entry). The parent provides the construct framing; sub-parts provide the implementation detail.
- **Tightening status carries forward:** HL.HF-3a was previously not-tightened (was HL.HF-3); HL.HF-3b was previously *tightened* in v3.4 (was HL.HF-4). After v3.7 Phase 2.1, HL.HF-3b retains its tightened-pattern sub-blocks. The parent HL.HF-3 itself does not carry the tightening pattern (sub-parts do); audit needs updating to recognise this.

**Audit / parser refactoring:**

- `parse.py` METRIC_HEADING regex extended to recognise `-N{a,b,c}` suffix as a sub-part of parent `-N`. New `Metric.parent_ref_id` field for sub-parts; new `Metric.is_parent` flag for parents.
- `audit.py check_numbering` updated to allow gaps in the integer sequence iff the gap ID appears in a known-retired-IDs list (loaded from a new `taxonomy/_retired-ids.md` registry). Each retired ID has a redirect note pointing at the new ID.
- `audit.py check_tightening_pattern` updated: tightening pattern can sit on either the parent (single-implementation metrics) or any sub-part (multi-implementation parents); the sub-parts of a parent metric can be independently tightened or not.
- `audit.py check_metric_cross_references` updated: anchors of form `tp-sn-7a` resolve to sub-parts; anchors of form `tp-sn-7` resolve to parents.
- `taxonomy/_retired-ids.md`: new registry file recording every retired ID with its redirect target. v3.7 registers TP.SN-8 → TP.SN-7b, TP.SN-10 → TP.SN-9b, HL.HF-4 → HL.HF-3b, plus the TP.CC-8 retirement from Phase 2.3 below.

**Wire-ups:**

- Standards-mapping references to TP.SN-8, TP.SN-10, HL.HF-4 updated to the new sub-part IDs (mechanical search/replace).
- `_responsible-ai-lens.md`, `_gaps.md`, `_outcomes-boundary.md` swept for legacy ID references.
- Existing Tier 1 quick reference updated: HL.HF-3 (now parent) listed once with sub-parts inline; HL.HF-4 removed as separate entry.
- Tightened-count manifest after Phase 2.1: HL.HF-3b carries forward its tightening (was HL.HF-4); the count of tightened-things stays effectively the same but is now disaggregated by sub-part where applicable.

**Verification:**

- Parent + sub-parts render correctly in the assembled monolithic markdown
- Retired IDs in `_retired-ids.md` audit-clean; broken-cross-reference check passes (any old `#tp-sn-8` link is either fixed or flagged)
- Site smoke-test: parent and sub-part anchors both resolve

### 2.2 Cross-references and new family framings (~15 pairs)

Mechanical: add See-also lines or lightweight sub-cluster framings to the overlapping-but-not-framed pairs surfaced in `archive/v3.6-duplication-review.md`. No metric IDs change. Examples:

- TP.ASR-10 ↔ TP.ASR-11 (calibration vs exposure; mutual See-also)
- TP.CC-1 ↔ TP.CC-2 (general code accuracy vs concept-mapping accuracy; framing note)
- TP.DI-3 ↔ TP.DI-4 (speaker count vs boundary precision; See-also)
- HL.HF-12 ↔ HL.HF-13 (skill attenuation vs cognitive offloading; Sociotechnical sub-cluster note)
- HL.HF-6 ↔ HL.HF-19 (in-context vs counterfactual automation-bias detection; See-also)
- IO.PX-2 ↔ IO.PX-8 (perceived accuracy vs comprehension; See-also)
- IO.PX-3 ↔ IO.PX-4 (emotional content vs cultural-linguistic; See-also)
- IO.FE-1 ↔ IO.FE-8 (within-deployment vs cross-platform fairness; See-also)
- GV.OP-1 ↔ GV.OP-3 (in-clinician-time vs in-record-time; cross-reference making distinction explicit)
- GV.SG-7 ↔ GV.SG-8 (P₁/P₂ vs DeepScore; Risk-Quantification sub-cluster note)
- GV.SG-15 ↔ GV.SG-16 (incident correction vs SPI escalation latency; See-also)
- GV.SG-9 ↔ GV.SG-16 (SPI thresholds vs response time; explicit pairing)
- GV.SC-1 ↔ GV.SC-2 ↔ GV.SC-6 (Injection Resistance sub-cluster note)
- GV.SC-3 ↔ GV.SC-7 (audio-input adversarial threats; See-also)
- GV.SC-8 ↔ GV.SC-9 ↔ GV.SC-11 (Privacy Attack Surface sub-cluster note)
- GV.VT-2 ↔ GV.VT-3 ↔ GV.VT-4 (Data-Access sub-cluster note: telemetry / benchmark / audit)
- ES.ME-2 ↔ ES.ME-7 (inter-rater ceiling vs concordance against ceiling; See-also)
- ES.ME-3 ↔ ES.ME-4 (interaction analysis vs gaming detection; See-also)
- TP.SN-12 ↔ GV.VT-4 (cross-group: per-summary provenance vs forensic audit trail; See-also)
- HL.HF-6 ↔ ES.ME-4 (cross-group: automation bias vs Goodhart gaming; See-also)

Adjacent candidates also resolved here:

- HL.HF-1 ↔ HL.HF-11 (v3.4 mandate substantially overlaps): HL.HF-11 retained as a separate metric; cross-reference note distinguishing aggregate-edit-rate-with-clinician-disaggregation (HF-1) from explicit-variance-quantification (HF-11)
- GV.TC-1 (M4 module) ↔ GV.TC-3 (Refresher / CPD Compliance): cross-reference distinguishing the integrated-completion-tracking view from the refresher-cadence-specific view; both retained

### 2.3 US-flavour audit and resolution

User direction (2026-04-26): "make sure they acknowledge the need for NHS framing — don't necessarily get rid of the metrics."

**Approach:** brief audit of all 216 metrics for US-flavour content (wRVU, Medicare, E/M coding, US-payer references, ICD-10-CM US conventions, etc.). For each surfaced metric, two outcomes possible:

- **Reframe:** add explicit NHS framing while keeping the US construct as named analogue (e.g. SNOMED specificity shift, with E/M called out as US analogue)
- **Fold:** retire the metric ID and absorb its content into a more NHS-applicable parent (option β from kick-off)

**Known starting candidates:**

- **TP.CC-7 ↔ TP.CC-8** (option β — fold): TP.CC-8 E/M Level Shift Monitoring is essentially a US-specific specialisation of TP.CC-7 Coding Inflation Detection's SPC-based drift detection. KL-divergence and demographic-disaggregation content from TP.CC-8 folds into TP.CC-7 (which gets renamed to "Coding Drift Detection" or kept as Coding Inflation Detection with NHS framing strengthened). TP.CC-8 retired with redirect note.
- **TP.CC-10 wRVU / Tariff Impact Attribution** (likely reframe): wRVU is US Medicare; UK equivalent is HRG / NHS tariff. Rename to "HRG / Tariff Impact Attribution" with wRVU called out as US analogue; preserve the construct but shift the framing.
- **TP.CC-3 ICD-10 / ICD-11 Full-Specificity Precision** (probable reframe): ICD-10-CM (US) vs ICD-10 (UK SNOMED-mapped); already references both but worth confirming the framing emphasises UK use.

**Audit method:**

- grep across all metric files for `wRVU`, `Medicare`, `E/M`, `tariff`, `ICD-10-CM`, `CMS`, `US payer`, `US setting` and adjacent terms
- read each surfaced metric for genuine US-flavour content vs incidental references
- per metric: reframe (default) or fold (only if redundant against an existing NHS-applicable metric)
- each fold requires user sign-off per the Phase 2.1 redundancy convention

**Output:** small registry of US-flavour findings appended to `archive/v3.6-duplication-review.md` (or new `archive/v3.7-us-flavour-audit.md` if the count justifies it).

**Locked decision:** the audit will identify all candidates; the user signs off per metric on reframe vs fold before any retirement.

**Effort across Phase 2:** 3–5 days (Phase 2.1 most of the work due to parser/audit refactoring; Phase 2.2 mechanical; Phase 2.3 1–2 days depending on count of US-flavour findings).

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

**Phase 2.1 (sub-parts):**
- `taxonomy/part-a/summarisation-nlp.md` (TP.SN-7, TP.SN-7a, TP.SN-7b → restructure; TP.SN-9, TP.SN-9a, TP.SN-9b → restructure; TP.SN-8 / TP.SN-10 retired with redirect notes)
- `taxonomy/part-c/human-factors-workflow.md` (HL.HF-3, HL.HF-3a, HL.HF-3b → restructure; HL.HF-4 retired with redirect note)
- `taxonomy/parse.py` (METRIC_HEADING regex, sub-part parent linkage, retired-ID handling)
- `taxonomy/audit.py` (`check_numbering` allows retired-ID gaps; `check_tightening_pattern` recognises sub-parts; `check_metric_cross_references` resolves sub-part anchors)
- `taxonomy/_retired-ids.md` (new registry)
- `taxonomy/_standards-mapping.md`, `taxonomy/_responsible-ai-lens.md`, `taxonomy/_gaps.md`, `taxonomy/_outcomes-boundary.md` (legacy ID sweep)
- `taxonomy/_tier-1-quick-reference.md` (HL.HF-3 parent listing; HL.HF-4 removed)

**Phase 2.2 (cross-references):**
- ~15 metric files across all parts; mechanical See-also / sub-cluster framing additions

**Phase 2.3 (US-flavour audit):**
- `taxonomy/part-a/clinical-coding.md` (TP.CC-7 reframed; TP.CC-8 retired and folded; TP.CC-10 reframed; TP.CC-3 reviewed)
- Other metric files surfaced by the audit
- `taxonomy/_retired-ids.md` (TP.CC-8 entry added)
- `archive/v3.7-us-flavour-audit.md` (or appended to `archive/v3.6-duplication-review.md`)

**Phase 3:**
- TBD per metric chosen

**Phase 4:**
- `CHANGELOG.md`, `taxonomy/_header.md`, `taxonomy/_how-to-use.md`, `README.md`

---

## Verification (end-to-end, sketch)

1. Build + audit clean throughout
2. **Phase 0:** new `_calibration-and-context.md` appears in assembled `avt-metrics-taxonomy.md` between Outcomes Boundary and Roadmap; all five wire-in surfaces resolve their cross-references via the cross-reference audit check; the principle is named (not just buried) at every surface — README, header, how-to-use, tier-1-quickref, outcomes-boundary
3. **Phase 1:** Tightening status manifest reaches **31/43** after Phase 1 (counting parents whose tightenable sub-parts are tightened, e.g. HL.HF-3 counts as tightened iff HL.HF-3b retains its tightening; TBD for double-counted cases)
4. **Phase 2.1:** Three parent metrics rendered correctly with sub-parts (TP.SN-7/-7a/-7b, TP.SN-9/-9a/-9b, HL.HF-3/-3a/-3b); three retired IDs (TP.SN-8, TP.SN-10, HL.HF-4) appear in `_retired-ids.md` with redirect notes; audit allows the integer gaps; cross-reference audit catches any orphaned legacy-ID anchors. HL.HF-3b retains its v3.4 tightening pattern; HL.HF-3 parent does not need tightening pattern itself.
5. **Phase 2.2:** ~15 cross-reference / framing additions land; cross-reference audit clean
6. **Phase 2.3:** US-flavour audit produces a frozen registry (in archive/); each surfaced metric is either reframed (default) or folded (with user sign-off); TP.CC-8 retired and folded into TP.CC-7 (option β); registry covers the 216-metric sweep
7. **Phase 3:** scope of addressed deferred metrics named explicitly; remaining deferred metrics named in CHANGELOG for v3.8+
8. v3.5 / v3.6 follow-ups status — confirm none reopened by v3.7 changes
9. CHANGELOG v3.7 entry names the deferred metrics not addressed (so v3.8+ scope is auto-tracked); names every retired ID and its redirect; names every reframed metric

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
2. **Phase 2.1 redundancy-as-sub-parts confirmed:** sub-parts approach (a/b/c suffix) for the 3 redundancy candidates; deprecate-don't-renumber for retired IDs (TP.SN-8, TP.SN-10, HL.HF-4); registry in new `_retired-ids.md`. User confirmed 2026-04-26.
3. **Phase 2.3 US-flavour audit confirmed:** sweep all 216 metrics; reframe to acknowledge NHS context as default, fold only where redundant against an existing NHS-applicable metric (TP.CC-7/-8 as the known case, option β). User direction 2026-04-26: "make sure they acknowledge the need for NHS framing — don't necessarily get rid of the metrics."
4. **Has v3.5 / v3.6 attracted external feedback?** If yes, that may reframe Phase 2 or Phase 3 priorities.
5. **Phase 3 priorities — which of the 5 deferred metrics to address first?** GV.SG-11 (LFPSE-AVT taxonomy) is the most externally-relevant; HL.HF-3 (review-quality bound) is the most internally-coherent given v3.5's HL.HF-1 / HL.HF-4 pairing. Note: v3.7 Phase 2.1 promotes HL.HF-3 to a parent metric; the "review-quality bound" question now sits at the parent-construct level, which may simplify or complicate Phase 3 — review at kick-off.
6. **HL.HF-3 tightening status post-Phase 2.1.** HL.HF-3b inherits v3.4 tightening (was HL.HF-4). HL.HF-3a was previously not-tightened. Decision: does HL.HF-3a warrant tightening as part of Phase 1 (since it's a Tier 1 metric currently in the not-tightened set), or stays not-tightened pending Phase 3 review-quality-bound work? Default: tighten in Phase 1 if the work is mechanically straightforward; otherwise carry into Phase 3.
