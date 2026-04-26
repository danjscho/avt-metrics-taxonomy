# v3.8 — NHSE AVT Registry Mapping + Audit-Tooling Hygiene + Documentation Drift + Selected Roadmap Promotions

## Context

v3.7 shipped on 2026-04-26 with the Calibration & Context principle, six pipeline-narrow tightenings, three redundancy-pair restructures as parent + sub-parts, and the US-flavour reframe of the TP.CC family. Counts: 215 metrics, 43/93/79 tier split, 30/42 Tier 1 constructs tightened (31/43 individual entries). The release was substantial, and four areas have surfaced for v3.8.

**1. NHSE AVT Self-Certified Supplier Registry mapping.** The registry is **live** (first cohort of 19 vendors listed January 2026, expanded to 23 by April 2026; applications reopen indefinitely from 3 February 2026). The taxonomy already references it via a single metric — [GV.CR-4 AVT Supplier Registry Listing Verification](taxonomy/part-e/nhs-compliance-regulatory.md) — but we have not properly mapped it as a framework alongside the twelve already in [_standards-mapping.md](taxonomy/_standards-mapping.md). Researching the registry surfaced four categorical gaps: Cyber Essentials Plus has no metric; self-certification provenance / evidence-pack freshness has no metric; pricing transparency for the National Commercial & Procurement Hub has no metric; the registry's "AI/LLM-specific monitoring beyond baseline" criteria are referenced but not yet published. The first three are addressable in v3.8; the fourth is a watch-list item.

**2. Audit-tooling gaps that allow data-quality drift.** Self-review identified two genuine silent-failure modes: `audit.py` checks Maturity field *presence* but not that the value is one of the four canonical strings (Established / Emerging / Vendor-Proprietary / Proposed/Novel) — non-canonical values pass silently. Same problem for Source — never validated for presence let alone quality. With 215 metrics, drift here is invisible until a downstream tool breaks.

**3. Documentation drift after v3.7.** README still says "v3.6, 216 metrics, 25 of 43 Tier 1 tightened". The site `docs/index.md` is even more stale (claims v3.1, 214 metrics). `_how-to-use.md` Tier 2 count is still 94 not 93. Multiple files have version drift.

**4. v3.7 carry-forwards.** [HL.HF-3a Review-Before-Signing Rate](taxonomy/part-c/human-factors-workflow.md) was promoted to a Tier 1 sub-part in v3.7 but not tightened — completing it in v3.8 reaches 32/43 individual / 31/42 constructs. [GV.TC-1 ↔ GV.TC-3](taxonomy/part-e/training-competency.md) overlap question deferred from v3.6 duplication review needs resolution.

**Roadmap promotions explicitly deferred.** v3.8 does **not** promote any of the 89 candidates in `_gaps.md`. User direction (2026-04-26): a big roadmap review will follow v3.8, after the registry mapping has had time to settle and potentially reframe which candidates matter most. Registry research already surfaced four categorical gaps (Cyber Essentials, evidence-pack freshness, pricing transparency, AI/LLM-specific monitoring) — three of those become real metrics in v3.8 Phase 2, but they are registry-driven rather than roadmap-driven. Existing roadmap candidates (GV.CR-12 Board-Level AI Governance, GV.SG-19 Systems-Based Incident Analysis, TP.WB-11 PRSB Semantic Completeness, and the other 86) stay queued and will be reviewed as a coherent set in a dedicated future release.

**Why now:** the registry mapping has external currency (a live procurement scheme that vendors and deployers are already working through), the audit gaps risk silent drift, the documentation staleness undermines reader trust, and the carry-forwards close known incomplete work from v3.7. None depend on each other; they can be sequenced for review-friendliness.

**Intended outcome:** taxonomy maps to thirteen frameworks; audit catches Maturity / Source drift; documentation is consistent; HL.HF-3a is tightened; v3.7 cross-cutting consistency improvements applied. Roadmap review left for a dedicated release.

---

## Phase 0 — Documentation drift sweep

Quick-wins. Low-risk; lands first to clear the staleness.

### 0.1 Version + count updates

- [README.md](README.md): seven places state v3.6 / 216 / 25-of-43; update to v3.7 / 215 / 30-of-42 constructs (or 31-of-43 individual entries — pick the construct framing for headline narrative). Tag history adds v3.7 entry. Citation example bumps version. Last-updated stamp.
- [docs/index.md](docs/index.md): currently shows v3.1 / 214 metrics — completely stale. Update to v3.7 / 215 / 43-93-79.
- [taxonomy/_how-to-use.md](taxonomy/_how-to-use.md): Tier 2 count "94 metrics" → 93. Tightened-metric list updated to 30 + sub-parts framing.
- Confirm no other `_*.md` files have stale counts post-v3.7.

### 0.2 Verification

- All version strings consistent across README, _header.md, _how-to-use.md, _summary.md, _contents.md, _applicability.md, docs/index.md
- Build clean; audit clean; site smoke-test shows correct version on landing page

---

## Phase 1 — Audit-tooling hygiene

Two new audit checks closing silent-failure modes.

### 1.1 `check_maturity_values`

- Add `EXPECTED_MATURITY_VALUES = {"Established", "Emerging", "Vendor-Proprietary", "Proposed / Novel"}` constant to `taxonomy/audit.py`
- New check function `check_maturity_values(all_metrics)` — every countable metric's `Maturity` dimension value must be in the set. Non-canonical → ERROR with metric ID and observed value.
- Wire into `main()` alongside existing checks.
- Smoke-test under fault injection: change one Maturity to "Partly Established" → audit fires `invalid-maturity` ERROR; restore.

### 1.2 `check_source_presence`

- New check function `check_source_presence(all_metrics)` — every countable metric must have a non-empty `Source` dimension row. Missing or blank → ERROR.
- Wire into `main()`.
- Smoke-test: blank a Source row → audit fires; restore.

### 1.3 Verification

- Audit clean on the v3.7 corpus after both checks added (means the existing 215 metrics all pass the new floors)
- Both fault-injection tests fire the right finding category
- CHANGELOG entry names the new check categories

---

## Phase 2 — NHSE AVT Registry mapping (new framework #13)

### 2.1 Add NHSE AVT Registry section to `_standards-mapping.md`

The standards-mapping document currently maps 12 frameworks. Add a 13th section for the **NHSE AVT Self-Certified Supplier Registry**, modelled on the existing T.E.S.T. and DTAC sections. Content (sketch — final wording during execution):

- **Publisher / status / scope** — NHS England (Transformation Directorate / Digital); live since January 2026; self-certification (preliminary completion checks only, NHSE does not endorse listed suppliers); evidence published via National Commercial and Procurement Hub for adopting trusts to inspect.
- **Vendor requirement categories** — table of 13 categories (MHRA Class I, DCB0129, DTAC, DSPT, Cyber Essentials, UK GDPR / DPIA, post-market surveillance, real-world benefit evidence, EPR integration capability, scalability evidence, performance/monitoring response document, indicative pricing matrix, AI/LLM-specific monitoring criteria — last unpublished).
- **Mapping table** — registry-requirement-category → existing taxonomy metric IDs, parallel to T.E.S.T. mapping in v3.2. Most categories already have coverage from prior framework mappings; gaps flagged explicitly.
- **Locked decisions** — registry treated as an integration / aggregation layer over existing frameworks (DTAC, DSPT, DCB0129, MHRA, etc.); GV.CR-4 stays as the explicit hook; new metrics added in Phase 2.2 below.
- **Currency note** — explicit "last researched 2026-04-26; AI/LLM-specific sub-criteria not yet published; revisit when NHSE publishes detail."

### 2.2 Three new metrics for registry-driven gaps

These are roadmap promotions specific to the registry mapping. Before drafting, confirm none collide with existing IDs (the `_gaps.md` registry lists candidates by proposed ID; check for conflicts with current Part E IDs).

- **GV.SC-12 Cyber Essentials Plus Certification Status** (🟡 Tier 2, AVT-Contextualised, in [security-adversarial-robustness.md](taxonomy/part-e/security-adversarial-robustness.md)). Binary check on certification currency; recertification cadence; in-scope component coverage. Cyber Essentials is a registry listing requirement and the NHSE has elevated it to expected baseline; it sits naturally in security and is currently absent from the taxonomy.
- **GV.VT-9 Evidence Pack Freshness** (🟡 Tier 2, in [vendor-transparency-contractual.md](taxonomy/part-e/vendor-transparency-contractual.md)). Currency of vendor's published evidence pack on the National Commercial & Procurement Hub; date of last attestation; cadence rule; signed-declaration provenance. Closes the self-certification-integrity gap.
- **GV.VT-10 Indicative Pricing Transparency** (🟡 Tier 2, in same file). Publication and currency of indicative pricing matrix per registry requirement; price-list coverage of declared use cases; transparency score against deployer's contracted scope.

Each metric written with the v3.7 tightening pattern from inception (Reference Standard / Operational Specification / Threshold Guidance with ⚠️ Provenance prelude and `[Calibration & Context principle](#calibration-context)` cross-reference). Maturity = Established (registry mechanics) or Emerging (where the metric anticipates registry detail not yet published).

### 2.3 Update GV.CR-4 to cross-reference the new framework section

GV.CR-4 currently treats the registry as a known external scheme. Add Operational Specification and Threshold Guidance sub-blocks (this is the metric becoming tightened); cross-reference the new `_standards-mapping.md § NHSE AVT Registry` section; cross-reference the three new metrics from 2.2.

### 2.4 Header / how-to-use updates

- `_header.md` count narrative extends to "thirteen mapped frameworks" (was twelve); v3.7 → v3.8 version stamp.
- `_how-to-use.md` Tier 2 count 93 → 96 (+3 from new registry-gap metrics).
- `_applicability.md` totals updated for the +3 new metrics (likely +2 AVT-Contextualised, +1 General Healthcare AI; depends on exact classification).

### 2.5 Verification

- Build clean; audit clean.
- New metrics carry full tightening pattern (caught by `check_tightening_pattern` if missing).
- Standards-mapping renders correctly on site with new section.
- Cross-reference audit (`check_metric_cross_references`) validates new internal links.
- Tightening manifest reaches 33-34/45 (depending on whether GV.CR-4 tightening is counted alongside the three new metrics).

---

## Phase 3 — HL.HF-3a tightening + GV.TC-1/TC-3 redundancy resolution

Two carry-forwards from v3.7.

### 3.1 Tighten HL.HF-3a Review-Before-Signing Rate

HL.HF-3a was promoted to a Tier 1 sub-part in v3.7 Phase 2.1 but did not receive the tightening pattern. The pattern fits — the construct is well-understood (binary edit / scroll / dwell-above-threshold telemetry signal); the v3.7 Inadequate-Review Detection parent already provides framing.

- Reference Standard: EPR + AVT product telemetry; the binary signal is the per-note presence of any of (a) edit event, (b) scroll event, (c) dwell time exceeding T_min = max(15s, 3s × word_count / 100). Inter-rater target on event-classification ICC ≥ 0.90 (mechanical signal; tighter than human-judgement metrics).
- Operational Specification: per-clinician baseline; per-note granularity; window weekly; pairing with HL.HF-3b TTS distribution mandatory (rubber-stamping signal lives in conjunction); T_min calibration locked per deployment context (specialty mix shifts the threshold per the Calibration & Context principle).
- Threshold Guidance: NAS Day Zero ≥95 % gate, <85 % pause trigger (cited); per-clinician baseline alert if rate falls > 10pp from established baseline (proposed in v3.8 as starting point); pause trigger when HL.HF-3a < 85 % AND HL.HF-3b TTS_norm P5 < 0.5 s/word (rubber-stamping confirmed in conjunction).

After this, parent HL.HF-3 reaches "fully tightened" in the manifest (both sub-parts tightened), promoting HL.HF-3 from "not-tightened" to "tightened" at the construct level.

### 3.2 Resolve GV.TC-1 (M4 module) ↔ GV.TC-3 overlap

v3.5 tightening of GV.TC-1 enumerated four mandatory training modules with M4 = Refresher / CPD. GV.TC-3 is a separate metric for Refresher Training & CPD Compliance. Question deferred from v3.6 duplication review: is GV.TC-3 now subsumed?

- Read both metrics' current Operational Specifications carefully.
- Decision options: **(a) fold** — TC-3 retired, M4 absorbs CPD-specific compliance structure; **(b) keep with framing** — TC-3 carries CPD-accreditation-body linkage and recency-window structure not in TC-1's M4; explicit cross-reference + framing note distinguishing.
- **Locked decision**: requires user sign-off per the Phase 2.1 sub-parts convention. Plan-mode pause if option (a) merge needed.

### 3.3 Verification

- HL.HF-3a tightening: audit shows HL.HF-3 parent now "tightened" in the construct manifest; HL.HF-3a individually tightened
- TC-1/TC-3 resolution recorded explicitly (in metric prose if option b; in `_retired-ids.md` if option a)
- Tightened count: 30/42 → 31/42 constructs (HL.HF-3 promoted)

---

## Phase 4 — Cross-cutting consistency improvements (low-leverage but hygiene)

### 4.1 Calibration & Context ↔ Outcomes Boundary cross-references

Both files mention the other now (added during v3.7), but the sub-section in `_outcomes-boundary.md` could be stronger in articulating the soft-vs-hard distinction (Outcomes Boundary is a hard limit; Calibration is a soft instruction). Light edit, ~50 words.

### 4.2 build_site.py parent-handling consistency

Per the v3.6/v3.7 review, `build_site.py` uses `parse_all_metrics()` in seven places without consistent filtering for parents. Audit each call site and apply the right filter:

- **Anchor generation** (`add_metric_anchors`): countable metrics only (parents don't need their own anchors; sub-parts get `-Na` anchors)
- **Metric-collection for tables**: explicit choice — countable only for headline counts; all-metrics for cross-reference lookups
- **Per-page rendering**: sub-parts shown under parent's section in the rendered group page

Audit: anchor collisions checked across the 215-metric corpus + 3 parents. If any collision found, flagged as ERROR.

### 4.3 Verification

- Site smoke-test: parent and sub-part anchors render correctly; cross-references resolve
- No anchor collisions detected
- Visual inspection of HL.HF-3 / TP.SN-7 / TP.SN-9 group pages shows construct framing + sub-parts in clear sequence

---

## Phase 5 — Release wrap

CHANGELOG v3.8 entry; header version bump; `_how-to-use.md` mention of registry mapping; README per-audience sections updated for the new framework.

Counts after v3.8 (estimated):
- Metrics: 215 + 3 (Phase 2.2 registry-gap) - 0 to 1 (Phase 3.2 GV.TC-3 fold if user signs off) = **217 to 218**
- Tier split: 43 / 96 / 79 (or 43 / 95 / 79 if TC-3 folds, since TC-3 is Tier 2)
- Tightened constructs: 30/42 → ~32-33 (HL.HF-3 from Phase 3.1 + GV.CR-4 from Phase 2.3 + the three Phase 2.2 registry metrics if their patterns count from inception)
- Frameworks mapped: 12 → **13**

### Branching

- Branch `v3-8-registry-and-hygiene` off `main@v3.7`
- Phase 0 as 1 commit (documentation drift sweep)
- Phase 1 as 1 commit (audit checks)
- Phase 2 as 2-3 commits (standards-mapping section; new metrics; GV.CR-4 update)
- Phase 3 as 2 commits (HL.HF-3a tightening; TC-1/TC-3 resolution)
- Phase 4 as 1 commit (cross-cutting consistency)
- Phase 5 as final commit (CHANGELOG + header)
- `--no-ff` merge, tag `v3.8`
- All commits 🦞-prefixed

---

## Critical files

**Phase 0:**
- `README.md`, `docs/index.md`, `taxonomy/_how-to-use.md`

**Phase 1:**
- `taxonomy/audit.py` (two new check functions + constants)

**Phase 2:**
- `taxonomy/_standards-mapping.md` (new NHSE AVT Registry section)
- `taxonomy/part-e/security-adversarial-robustness.md` (GV.SC-12 new)
- `taxonomy/part-e/vendor-transparency-contractual.md` (GV.VT-9, GV.VT-10 new)
- `taxonomy/part-e/nhs-compliance-regulatory.md` (GV.CR-4 tightening + cross-references)
- `taxonomy/_header.md`, `_how-to-use.md`, `_applicability.md`, `_contents.md` (count updates)

**Phase 3:**
- `taxonomy/part-c/human-factors-workflow.md` (HL.HF-3a tightening)
- `taxonomy/part-e/training-competency.md` (GV.TC-3 fold or framing)
- `taxonomy/_retired-ids.md` (if GV.TC-3 retired)

**Phase 4:**
- `taxonomy/_outcomes-boundary.md` (cross-reference strengthening)
- `taxonomy/build_site.py` (parent-handling consistency)

**Phase 5:**
- `CHANGELOG.md`
- `taxonomy/_header.md`
- `taxonomy/_how-to-use.md`
- `README.md`

---

## Verification (end-to-end)

1. Build + audit clean throughout
2. Phase 0: every version-stamp file consistent (v3.8 / 2026-04-XX); all count references match the post-v3.8 totals
3. Phase 1: both new audit checks fire under fault injection (non-canonical Maturity; missing Source); restore both
4. Phase 2: standards-mapping section renders with thirteenth framework; three new registry-gap metrics carry full tightening pattern; cross-reference audit clean for new anchors
5. Phase 3: HL.HF-3 parent appears in "tightened" list of audit manifest (both sub-parts now tightened); TC-1/TC-3 resolution traceable in CHANGELOG and metric prose / retired-ids
6. Phase 4: site smoke-test for parent + sub-part anchors; no collisions
7. CHANGELOG v3.8 entry names every change; v3.9+ deferrals explicit (the big roadmap review; registry AI/LLM-specific sub-criteria when NHSE publishes detail; remaining ~7 cross-reference candidates from v3.6 duplication review; remaining 4 of 5 deferred-pool metrics from v3.4 classification)
8. `_gaps.md` candidate count unchanged at 89 — v3.8 promotes none; the registry-driven metrics in Phase 2 are framework-driven, not roadmap-driven

---

## Out of scope (defer to v3.9+)

- **Big roadmap review** — explicit user direction (2026-04-26): defer all 89 `_gaps.md` roadmap candidates to a dedicated future release after the registry mapping has had time to settle. The registry may reframe which candidates matter most. Three previously-flagged high-leverage candidates (GV.CR-12 Board-Level AI Governance, GV.SG-19 Systems-Based Incident Analysis, TP.WB-11 PRSB Semantic Completeness) stay queued.
- AI/LLM-specific NHSE registry sub-criteria — flagged for monitoring; spec not yet published
- Remaining 4 of 5 v3.4 deferred-pool metrics (GV.OP-6, GV.SG-9, GV.SG-11, GV.SG-13) — bespoke per-metric scoping; v3.8 addresses HL.HF-3a only
- Tier 2 / Tier 3 systematic tightening — Tier 1 not complete
- Site-side improvements (procurement wizard, filter-by-context) — flagged in earlier critique
- Outcomes-layer extension beyond ES.ME-8/9
- Stakeholder review process / public release

---

## Open questions for v3.8 kick-off

1. **GV.TC-1 / GV.TC-3 disposition (Phase 3.2)** — fold (option a) or keep with framing (option b)? Requires user sign-off per the v3.7 Phase 2.1 redundancy convention. Default: option (b) keep with framing unless review confirms TC-3 adds nothing beyond TC-1's M4 reporting.
2. **NHSE registry "AI/LLM-specific monitoring" placeholder** — published detail is pending. Should v3.8 add a placeholder metric flagged "watch-list" with the registry pointer, or wait? Default: wait; document the gap in `_standards-mapping.md` § NHSE AVT Registry without a metric.
3. **HL.HF-3 manifest accounting** — once HL.HF-3a is tightened in Phase 3.1, the parent HL.HF-3 promotes from not-tightened to tightened. Confirm the manifest counts this as +1 construct (not +2 sub-parts) per the v3.7 convention.
4. **Confirmed locked decisions (recorded for the kick-off):**
   - Phase 4 (selected roadmap promotions) explicitly removed from v3.8 scope. Roadmap review deferred to a dedicated future release. (User direction 2026-04-26.)
   - Three Phase 2.2 registry-gap metrics (GV.SC-12, GV.VT-9, GV.VT-10) are registry-driven, not roadmap-driven, and are in scope.

---

## Estimated effort

- Phase 0: half day (mechanical staleness fixes)
- Phase 1: half day (two audit checks + smoke-tests)
- Phase 2: 2-3 days (registry research is done; metric drafting + standards-mapping section + count updates)
- Phase 3: 1-2 days (HL.HF-3a tightening + TC-1/TC-3 resolution depending on option)
- Phase 4: 1 day (cross-cutting consistency)
- Phase 5: half day (release wrap)

**Total: ~5-7 days**, narrower than v3.7. Roadmap review deferred allows a tighter, more reviewable release focused on registry mapping + hygiene.
