# Changelog

## v3.8.4 (2026-04-26)

Tooling-only patch — fixes site-wide version banner drift.

- **Site-wide banner now live-derived.** The mkdocs-material announce banner in `overrides/main.html` was hardcoded as `Draft v3.1` since the v3.1 release and had been silently stale through six subsequent releases (v3.2 → v3.8.3). `build_site._refresh_announce_banner()` now regenerates the override on every build using `SITE_VERSION`.
- **Template-token substitution in source files.** `_header.md` (and any future cross-cutting source file that wants the live version) can use `{{TAXONOMY_VERSION}}` / `{{TAXONOMY_DATE}}` placeholders, which both `build.py` (monolith assembly) and `build_site.py` (docs population) substitute at build time. Single source of truth = `parse.TAXONOMY_VERSION` + `parse.TAXONOMY_DATE`.
- **`parse.TAXONOMY_DATE` constant** added alongside the existing `TAXONOMY_VERSION`. Bumped together at release.
- **README.md** version stamps bumped to v3.8.4 (banner / current-draft / citation example / last-updated stamp).

No taxonomy content changes; audit clean; counts unchanged.

## v3.8.3 (2026-04-26)

Tooling-only patch.

- **CSV / JSON downloads now include `part_name`** alongside the existing `part` letter. The CSV had `part=A` but no human-readable label; reading metrics.csv in isolation gave you no way to know "A" meant "The Technical Pipeline". New `part_name` column / JSON field carries the full name (e.g. `"The Technical Pipeline"`, `"System Governance"`).
- **Single source of truth for part names.** `PART_NAMES` dict moved from `build_site.py` (where it was duplicated as `PART_TITLES`) to `parse.py`. `Metric.part_name` is a property; `build_site.PART_TITLES` is now derived. Renaming a part is a one-line edit.
- **Single source of truth for the version stamp.** New `parse.TAXONOMY_VERSION` consumed by `build.py` (JSON `version` field, previously hardcoded `"v3.2-dev"` — stale by 6 releases) and `build_site.SITE_VERSION` (landing + downloads citation). `pyproject.toml` version bumped manually to match at release.

No taxonomy content changes; audit clean; counts unchanged at 218 / 43-96-79.

## v3.8.2 (2026-04-26)

Tooling-only patch — adds reproducible local-development setup and documents the build pipeline.

- **`pyproject.toml` + `uv.lock` committed.** Project now uses [uv](https://docs.astral.sh/uv/) for Python environment management. `uv sync` creates a `.venv` matching CI exactly. Lockfile is committed for reproducibility.
- **CI workflow uses uv.** `.github/workflows/site.yml` swapped from `pip install` to `uv sync --frozen` + `uv run`. Removes the package-list drift risk between local and CI.
- **Local-development docs.** New "Local development — build and serve the site" section in `taxonomy/README.md` walks through the three-step recipe (`uv sync` → `uv run python taxonomy/build.py` → `uv run python taxonomy/build_site.py` → `uv run mkdocs serve`) and explains where the `dist/` files come from. Quick version added to root `README.md` developer section.
- **`.gitignore`:** added `.venv/`. (`dist/`, `docs/`, `site/` already ignored.)

No taxonomy content changes; no audit findings; counts unchanged.

## v3.8.1 (2026-04-26)

Site-only patch release — no taxonomy content changes. Fixes broken cross-page links and download issues surfaced by reviewing the `mkdocs serve` output:

- **Cross-cutting principle pages now in nav**: `_outcomes-boundary.md` and `_calibration-and-context.md` were authored as separate source files but never mapped into the rendered site. Every `[Calibration & Context principle](#calibration-context)` and `[Outcomes Boundary](#outcomes-boundary)` link from a group page resolved to nowhere. Mapped both into `docs/` and added to the nav under "Cross-cutting".
- **Two orphan crosscut pages added to nav**: the auto-generated NHSE AVT Registry and NHS T.E.S.T. by-standard pages were rendered but missing from the nav block. Added to "Cross-cut views → By standard".
- **Cross-page metric anchor rewriting**: bare `#tp-ac-1`-style references from one group page to a metric on a different group page are now rewritten to `<other-group>.md#tp-ac-1` at build time. The catalogue is parsed once and cached; sub-part suffixes (`-a`, `-b`) handled. Closes ~50 broken anchors that existed in the source taxonomy but only resolved in the monolith build.
- **Sub-part anchor regex**: `add_metric_anchors` regex extended to capture trailing letter suffixes so `### HL.HF-3a` lands `id="hl-hf-3a"` on the rendered page (previously slugged as `hl-hf-3`).
- **External-link rewrites for strict mode**: `[CHANGELOG.md](CHANGELOG.md)` → `changelog.md` (in-docs), `[README.md](README.md)` → GitHub blob URL, `[archive/<file>.md]` → GitHub blob URL. `mkdocs build --strict` was previously failing with three warnings; now passes.
- **Live-derived downloads page**: replaced hardcoded `v3.1` citation example and "214 metrics" / "83 gaps" counts with values pulled from `parse.summary()` and a single `SITE_VERSION` constant. Same for the landing page version stamp.
- **Stale slug fixes in CHANGELOG**: three legacy anchor refs (`#gvcr-6-...`, `#hlhf-1-...`, `#gvpd-1-...`) updated to current `#gv-cr-6` / `#hl-hf-1` / `#gv-pd-1` form so the cross-page rewrite resolves them to the right metric pages.

Counts unchanged: 218 metrics, 43/96/79 tier split, 32/42 Tier 1 tightened, 13 frameworks. Audit clean. `mkdocs build --strict` now exits 0.

## v3.8 (2026-04-26)

Adds the NHS England AVT Self-Certified Supplier Registry as the **13th mapped framework**, three registry-driven metrics, two new audit checks, and a tightening completion of HL.HF-3a (promoting the HL.HF-3 parent construct to fully tightened). Counts: 215 → **218 metrics**, tier split 43/93/79 → **43/96/79**, **32 of 42 Tier 1 constructs tightened**, 12 → **13 frameworks**.

Roadmap promotions explicitly deferred — user direction holds all 89 `_gaps.md` candidates for a dedicated future release after the registry mapping has time to settle and may reframe priorities.

### Phase 0 — Documentation drift sweep

User-facing files updated for v3.7-shipped state: `README.md` (v3.6 → v3.7; 216 → 215; "25 of 43" → "30 of 42 constructs"; tag history; citation example; last-updated stamp), `docs/index.md` (was wildly stale at v3.1; now v3.7 / 215 with correct framework list), `_outcomes-boundary.md` (216 → 215), `_privacy-data-governance.md` GV.PD-8 reference text (v3.6 → v3.7).

### Phase 1 — Audit-tooling hygiene

Two new `audit.py` checks closing silent-failure modes:

- **`check_maturity_values`** — Maturity dimension must hold one of the four canonical enum values (Established / Emerging / Vendor-Proprietary / Proposed/Novel). Pre-v3.8 audit only checked presence; non-canonical values like "Partly Established" silently passed.
- **`check_source_presence`** — Source row must be non-empty. Pre-v3.8 audit checked row presence but not value content.

New `EXPECTED_MATURITY_VALUES` constant. Smoke-tested under fault injection.

### Phase 2 — NHSE AVT Registry mapping

#### Phase 2.1 — Standards-mapping section (13th framework)

New section in `_standards-mapping.md` for the NHS England AVT Self-Certified Supplier Registry — live since January 2026 (first cohort 19 vendors, expanded to 23 by April 2026; applications reopen indefinitely from 3 February 2026). Self-certification scheme; NHSE undertakes preliminary completion checks only and does not endorse listed suppliers; evidence published via the National Commercial & Procurement Hub.

13-row vendor requirements table cross-referencing each registry category to existing framework mappings (DTAC, DSPT, DCB0129, MHRA, NHS T.E.S.T., NHS LLM Framework). 11 of 13 categories already covered by existing metrics; 2 had genuine gaps closed by Phase 2.2; 1 self-certification-integrity gap closed by Phase 2.2; 1 placeholder for AI/LLM-specific sub-criteria (NHSE has not yet published detail).

Standards-mapping preamble updated: 214 → 215 metrics; twelve → thirteen frameworks. Section positioned immediately after NHS T.E.S.T. since both are AVT-specific procurement tools.

#### Phase 2.2 — Three new registry-driven metrics

- **GV.SC-12 Cyber Essentials Plus Certification Status** (Tier 2; Security & Adversarial Robustness; AVT-Contextualised). Closes registry req #5 gap. Three sub-metrics (status / currency / in-scope coverage); annual cadence per IASME scheme; per-sub-processor coverage cross-linked to GV.VT-7. Limitations name the AI-specific threat surface that Cyber Essentials Plus does **not** cover.
- **GV.VT-13 Evidence Pack Freshness** (Tier 2; Vendor Transparency & Contractual; AVT-Specific). Closes self-certification-integrity gap. Quarterly Hub-publication review; Fresh / Aging / Stale per-component classification; signed-declaration-provenance check. Cross-linked to GV.CR-4 — VT-13 measures evidence pack quality, CR-4 measures listing.
- **GV.VT-14 Indicative Pricing Transparency** (Tier 2; Vendor Transparency & Contractual; AVT-Specific). Closes registry req #12 gap. Three sub-metrics (published / coverage / currency); deployer-side scope-alignment audit; ±20% materiality threshold on contracted use cases.

All three drafted with the v3.7 tightening pattern from inception (Reference Standard / Operational Specification / Threshold Guidance + ⚠️ Provenance prelude + Calibration & Context cross-reference).

**ID-allocation note:** GV.VT-9/-10/-11/-12 were already reserved by `_gaps.md` roadmap entries (proposed metrics from MHRA SaMD/AIaMD and NHS T.E.S.T. mappings). New metrics use GV.VT-13/-14 to preserve those slots. New "Reserved IDs (roadmap-allocated)" section added to `_retired-ids.md`; `audit.py` refactored (`_load_skipped_ids_sections`) to load both retired and reserved IDs; manifest output prints them on separate lines.

#### Phase 2.3 — GV.CR-4 tightening

GV.CR-4 (AVT Supplier Registry Listing Verification) now carries the v3.7 tightening pattern. Three mandatory sub-metrics (listing status / scope alignment / attestation currency); self-certification disclosure mandatory at every verification; multi-product handling; delisting watch.

### Phase 3 — Carry-forwards

#### Phase 3.1 — HL.HF-3a tightening

HL.HF-3a Review-Before-Signing Rate was promoted to a Tier 1 sub-part in v3.7 Phase 2.1 but did not yet carry the tightening pattern. v3.8 adds Reference Standard / Operational Specification / Threshold Guidance with mandatory pairing to HL.HF-3b (rubber-stamping detection lives in the conjunction). The parent HL.HF-3 (Inadequate-Review Detection) now classified as **tightened** in the manifest since both sub-parts carry the pattern.

#### Phase 3.2 — GV.TC-1 / GV.TC-3 redundancy resolution

v3.6 duplication review flagged GV.TC-3 (Refresher & CPD Compliance) as adjacent to GV.TC-1's M4 module after v3.5 tightening. Decision recorded: **option (b) keep both with explicit framing**. New "Relationship to GV.TC-1" section on GV.TC-3 distinguishes:

- GV.TC-1 M4 = process-compliance (per-clinician completion rate against the rolling validity window)
- GV.TC-3 = content-currency (the four update sources: locally discovered failure modes, national safety alerts, model-update implications, new attack vectors)

Headline reporting should pair the two; either alone is incomplete. No metric retired.

### Phase 4 — Cross-cutting consistency

- **Calibration ↔ Outcomes Boundary cross-references** strengthened. Soft-vs-hard distinction now explicit: Outcomes Boundary is a hard limit (calibration cannot import out-of-scope work); Calibration is a soft instruction (parameter values are local within the in-scope set).
- **`build_site.py` parent-handling consistency:** v3.6/v3.7 review found 5 places using `parse_all_metrics()` without consistent parent filtering. Audited each call site; one (`build_crosscuts`) was incorrectly including parents in applicability cross-cuts (would land in 'Unclassified'). Now filters to countable_metrics. Three other call sites correctly include parents (cross-reference resolution by name; ref_id → group_file lookup; related-metric chip generation).
- **`_landing_page` template fixes:** hardcoded "v3.1", "11 healthcare and AI standards", and applicability counts (48/77/89) replaced with live values derived from `parse.summary()` and `countable_metrics`. Prevents v3.7 → v3.8 docs/index.md staleness pattern from recurring.

### Counts

- **218 metrics** (was 215; +3 from Phase 2.2)
- Tier split **43 / 96 / 79** (Tier 2 +3 from Phase 2.2; Tier 1 and Tier 3 unchanged)
- 20 groups unchanged
- **32 of 42 Tier 1 constructs tightened** (was 30/42; HL.HF-3 promoted to tightened via Phase 3.1; GV.CR-4 tightened via Phase 2.3). Individual entries: 33 of 43 (counting sub-parts).
- Applicability: AVT-Specific 48 → **50** (+2 from GV.VT-13/-14); AVT-Contextualised 76 → **77** (+1 from GV.SC-12); General Healthcare AI 91 unchanged.
- Frameworks mapped: 12 → **13**.
- Roadmap unchanged at 89 candidates (no promotions in v3.8).

### Deferred to v3.9+

- **Big roadmap review** — 89 `_gaps.md` candidates held for a dedicated future release after the registry mapping settles. Three previously-flagged high-leverage candidates (GV.CR-12 Board-Level AI Governance, GV.SG-19 Systems-Based Incident Analysis, TP.WB-11 PRSB Semantic Completeness) remain queued.
- **NHSE registry AI/LLM-specific sub-criteria** — req #13 placeholder; NHSE detail not yet published.
- **Remaining 4 of 5 v3.4 deferred-pool metrics** (GV.OP-6, GV.SG-9, GV.SG-11, GV.SG-13) — bespoke per-metric scoping owed.
- **Remaining ~10 cross-reference / framing additions** from the v3.6 duplication review.
- **Outcomes layer** stays at ES.ME-8/9.

---

## v3.7 (2026-04-26)

Establishes the **Calibration & Context principle** as a first-class taxonomy commitment alongside the Outcomes Boundary; tightens 6 pipeline narrow Tier 1 metrics; restructures 3 redundancy candidates as parent-with-sub-parts; reframes US-flavour metrics with NHS-primary framing. Tightened-count manifest reaches 30/42 (constructs); flat tightened count is 31/43 (sub-parts). Headline metric count 216 → 215 (TP.CC-8 folded).

### Phase 0 — Calibration & Context principle

New cross-cutting file `taxonomy/_calibration-and-context.md` parallel to `_outcomes-boundary.md`. Names the structural commitment that **tier assignments and threshold numbers are calibration starting points, not universal gates**, and provides:

- Six deployment-setting calibration axes: specialty mix, patient population, platform maturity, governance capacity, risk appetite, volume / scale
- Practical guidance on documenting local calibration in the deployer's governance file (taxonomy default + local calibration + axis driving the change + named decision-maker)
- Promotion-up-vs-promotion-down asymmetry — promoting Tier 2/3 to Tier 1 is encouraged with one-line justification; promoting Tier 1 down requires substantive risk assessment
- Explicit boundaries on what calibration is *not* — not an excuse to disregard Tier 1; not a basis for negotiating contracted thresholds; not a way around the Outcomes Boundary

Wired into 5 surfacing points so the principle is visible where readers actually look:

- `_header.md` — count narrative names the principle alongside the Outcomes Boundary
- `_how-to-use.md` — "Adapting to Local Context" gets a top-line cross-reference; existing prose stays as practical examples subsidiary to the principle
- `_tier-1-quick-reference.md` — top-of-page ⚠️ callout: "this list is a calibrated starting point, not a fixed checklist"
- `_outcomes-boundary.md` — new "Relationship to the Calibration & Context principle" section explaining the parallel
- `README.md` — new bullet in Quick links; new paragraph in "What this is for"; per-audience reminder sentences

### Phase 1 — Pipeline narrow tightening (6 metrics)

Apply the Reference Standard / Operational Specification / Threshold Guidance pattern (with ⚠️ Provenance prelude) to the six pipeline narrow candidates from the v3.4 classification artefact:

- **TP.ASR-12 Hallucination-Under-Noise Rate** — five-category test corpus (silence / music / environmental / non-clinical-speech / clinical-adjacent ambient); per-category asymmetric-failure reporting; severity classification with critical = spurious clinical content
- **TP.ASR-13 Numeric Accuracy** — five-sub-type reference standards (integer / decimal / unit / date / range) with explicit canonicalisation rules; dosage accuracy as zero-tolerance critical sub-metric
- **TP.WB-2 Integration Error Rate** — three error types (failed / partial / degraded); per-EPR stratification; soft-failure detection method documented at procurement
- **TP.WB-3 Field Mapping Accuracy** — per-EPR field-map document mandatory with multi-target rules; type-(iii) silent-safety-bypass classification
- **TP.WB-4 Update vs Append Behaviour** — per-EPR (category × update-context) rule grid (5×5 = 25 cells); three critical-failure-mode classes; skip-with-flag pathway mandatory
- **TP.SN-20 Uncertainty Marker Preservation** — five-level epistemic ladder (definite / probable / possible / unlikely / negated) plus conditional uncertainty; asymmetric severity weighting (inflation > deflation)

Tightened count: 25/43 → 31/43 flat sub-parts (30/42 constructs after Phase 2.1 sub-part promotions).

### Phase 2.1 — Redundancy as sub-parts (3 candidates)

Restructure three redundancy pairs from the v3.6 duplication review as **parent + sub-parts** so neither implementation is lost and the relationship is explicit:

- **TP.SN-7 Factual Verification** (parent) absorbs:
  - **TP.SN-7a Confabulation Detection (Support × Severity)** — was TP.SN-7 (Abridge two-axis classifier; vendor-proprietary)
  - **TP.SN-7b VeriFact Factual Verification** — was TP.SN-8 (Stanford RAG + LLM-as-Judge; open-source, locally deployable)
  - The two are complementary instruments for the same construct (factual support); running both provides stronger assurance than either alone.
- **TP.SN-9 LLM-Judge Methodology** (parent) absorbs:
  - **TP.SN-9a LLM-as-a-Judge (PDSQI-9 Proxy)** — was TP.SN-9 (single-judge; 27× speed for continuous evaluation)
  - **TP.SN-9b MedHELM LLM-Jury** — was TP.SN-10 (ensemble jury; pre-deployment capability gate)
- **HL.HF-3 Inadequate-Review Detection** (parent) absorbs:
  - **HL.HF-3a Review-Before-Signing Rate** — was HL.HF-3 (binary edit/scroll/dwell signal)
  - **HL.HF-3b Time-to-Sign Distribution** — was HL.HF-4 (TTS distribution; retains v3.4 tightening pattern)

**Locked design decision:** deprecate-don't-renumber. Retired IDs (TP.SN-8, TP.SN-10, HL.HF-4) are not reused — every prior taxonomy version, the standards-mapping file, the v3.4 / v3.6 artefacts, and any external citation references the existing IDs. The integer sequences carry gaps (TP.SN sequence ... -7a, -7b, (gap at -8), -9a, -9b, (gap at -10), -11 ...). New file `taxonomy/_retired-ids.md` records every retirement with redirect target and reason; the audit reads this registry and tolerates the gaps.

**Audit / parser refactor:**

- `parse.py` METRIC_HEADING regex extended to recognise sub-part suffix (e.g. TP.SN-7a)
- New `Metric.is_subpart` and `Metric.parent_ref_id` properties
- `audit.py` METRIC_HEADING + REF_ROW regexes extended; new `is_parent_metric` / `parent_id` / `is_subpart_id` helpers; new `classify_parent_tightening` (parent counts as tightened iff every sub-part is tightened)
- `check_numbering` loads `_retired-ids.md` and tolerates retired-ID gaps; duplicate detection switched to exact-ref-id rather than base-integer
- `check_tightening_pattern` excludes parent metrics from the partial-state ERROR check (parents carry construct framing in the body, not the tightening pattern)
- `emit_tightening_manifest` uses parent-aware classifier; emits `Retired IDs: ...` status line
- `build.py` and `parse.summary()` exclude parents from headline counts via `countable_metrics` helper
- New audit constants document the count shift

### Phase 2.2 — Targeted cross-references (4 metric pairs)

Add See-also lines to the highest-value paired metrics from the v3.6 duplication review, in the audit-parser-friendly format (italic *See also: NameA, NameB - prose*):

- TP.ASR-10 ↔ TP.ASR-11 (calibration vs exposure of ASR confidence)
- GV.OP-3 → GV.OP-1 (record-availability time vs clinician note-effort time)
- GV.SG-15 ↔ GV.SG-16 (incident-correction latency vs SPI-breach escalation latency)
- GV.SG-16 → GV.SG-9 (escalation response time has GV.SG-9 SPI framework as a direct dependency)

Remaining ~10 cross-reference candidates from the v3.6 duplication review deferred to v3.8+ (recorded in `archive/v3.6-duplication-review.md` as the remaining set).

### Phase 2.3 — US-flavour audit and reframe

Sweep across all 216 metrics for US-flavour content. Three findings:

- **TP.CC-7** — reframed as **Coding Drift Detection (NHS framing)**; methodology unchanged but framing focus is data-quality corruption (QOF, HES, population-health analytics), not US revenue extraction. US E/M-upcoding literature called out as methodological precedent.
- **TP.CC-8 E/M Level Shift Monitoring** — folded into TP.CC-7 (option β from kick-off). KL-divergence and demographic-disaggregation methodology absorbed into TP.CC-7's new Operational Specification. TP.CC-8 retired with redirect to TP.CC-7 in `_retired-ids.md`.
- **TP.CC-10** — reframed as **HRG / Tariff Impact Attribution (NHS framing)**; NHS PbR / HRG context primary, US wRVU / CMS Medicare called out as methodological precedent.

Other US-flagged grep matches (DSCMS, MIMIC-III, Duke/MedStar citations) were ambient citation references rather than US-flavour content; no change needed.

### Phase 3 — deferred to v3.8+

The 5 pattern-may-not-fit metrics (GV.OP-6, GV.SG-9, GV.SG-11, GV.SG-13, HL.HF-3) need bespoke per-metric scoping that v3.7's already substantial scope didn't accommodate. Deferred to v3.8+ kick-off where each metric will be scoped individually. Note that HL.HF-3 has now been promoted to a parent construct (Phase 2.1) — its v3.7 framing already addresses some of the v3.4-flagged review-quality-bound concerns; v3.8 may find HL.HF-3 partially or fully resolved.

### Counts

- Headline metric count: 216 → **215** (TP.CC-8 retired and folded; not replaced as a sub-part since the methodology rolled into TP.CC-7)
- Tier split: 43 / 94 / 79 → **43 / 93 / 79** (TP.CC-8 was Tier 2)
- 20 groups unchanged
- Clinical Coding group: 12 → 11 metrics
- Applicability: AVT-Specific 48 unchanged; AVT-Contextualised 77 → 76; General Healthcare AI 91 unchanged
- Tightened-count manifest: **30/42** Tier 1 constructs (parents counted as units; HL.HF-3 not-tightened because HL.HF-3a not yet tightened; TP.SN-7 / TP.SN-9 parents not-tightened because they were Tier 3 / Tier 2 with no prior tightening pattern). Sub-part flat count: 31/43 individually tightened.

`audit.py` baseline updated for new totals; build clean; audit clean. Three audit checks introduced or extended in this release: parser/regex extension for sub-parts; `check_numbering` retired-ID tolerance; manifest parent-aware classifier.

### Cross-cutting

- `taxonomy/_header.md` v3.6 → v3.7 / 2026-04-26; narrative names the Calibration & Context principle and the six axes
- `taxonomy/_how-to-use.md` Adapting-to-Local-Context section now opens with a cross-reference to the principle file
- `taxonomy/_summary.md`, `_contents.md`, `_applicability.md` updated for the new totals (215 / 43-93-79; Clinical Coding 11)
- `taxonomy/_responsible-ai-lens.md`, `_calibration-and-context.md`, `_gaps.md` swept for legacy ID references (HL.HF-3 → HL.HF-3a; HL.HF-4 → HL.HF-3b; TP.SN-8 → TP.SN-7b; TP.SN-10 → TP.SN-9b)
- `taxonomy/_tier-1-quick-reference.md` ⚠️ callout naming the Calibration & Context principle

### Deferred to v3.8+

- **Phase 3 bespoke deferred-pool scoping:** 1-2 of GV.OP-6, GV.SG-9, GV.SG-11, GV.SG-13, HL.HF-3 (the latter partially addressed by Phase 2.1 parent-construct framing; reassess at kick-off)
- **HL.HF-3a tightening** — now a Tier 1 sub-part not yet carrying the pattern; v3.8 should consider tightening it alongside Phase 3
- **Remaining ~10 cross-reference / framing additions** from the v3.6 duplication review (see `archive/v3.6-duplication-review.md`)
- **Outcomes layer** stays at ES.ME-8/9
- **Roadmap** (`_gaps.md`) untouched in v3.7 — 89 candidates still queued

---

## v3.6 (2026-04-26)

Architectural alignment, duplication-review research artefact, four v3.5 self-review follow-ups, and a repo-root README. No new metrics; no new tightenings. Counts unchanged at 216 metrics, 43 / 94 / 79; tightened count unchanged at 25/43.

### Phase A — Applicability-on-metric alignment

Adds an **Applicability** row to every metric's dimension table (216 metrics across 20 group files), placed immediately after Outcome Type. Values (AVT-Specific / AVT-Contextualised / General Healthcare AI) extracted from the existing `_applicability.md` classification tables.

`taxonomy/parse.py` now sources `metric.applicability` from the dimension table — consistent with every other axis. The legacy `parse_applicability` lookup against `_applicability.md` is renamed to `parse_applicability_legacy` and retained only for audit cross-validation; `annotate_applicability()` becomes an idempotent no-op safety net for any caller that hasn't migrated.

`taxonomy/audit.py` gains `check_applicability_presence` (every metric must carry the row, value must be one of the three valid labels) and reworks `check_applicability_totals` to derive totals from per-metric dimension-table values (the new source of truth). Cross-validation against `_applicability.md` declared totals continues as a transition-period WARN.

The classification rationale prose in `_applicability.md` stays; per-metric tables become derivable. v3.7+ may move them to script generation.

### Phase B — Duplication review (research artefact)

[`archive/v3.6-duplication-review.md`](archive/v3.6-duplication-review.md) classifies every within-group metric pair as `distinct` / `overlapping` / `redundant`, with cross-group analysis for surfaced candidates. Frozen at v3.6 ship date; **no metrics changed**.

Headline findings:

- **3 redundancy candidates** flagged for v3.7 review with explicit user sign-off:
  - **TP.SN-7 Confabulation Detection ↔ TP.SN-8 VeriFact** — same construct (factual verification), different instruments
  - **TP.SN-9 LLM-as-a-Judge ↔ TP.SN-10 MedHELM LLM-Jury** — same construct (LLM-judge methodology), different ensemble configurations
  - **HL.HF-3 Review-Before-Signing ↔ HL.HF-4 Time-to-Sign Distribution** — both detect inadequate review (v3.4 already mandates pairing)
- 2 adjacent candidates: HL.HF-1 ↔ HL.HF-11 (v3.4 mandate substantially overlaps); GV.TC-1 M4 module ↔ GV.TC-3 (v3.5 tightening overlaps)
- ~15 overlapping-but-not-framed pairs flagged for v3.7 lightweight cross-reference additions (See-also, sub-cluster notes)
- Most apparent overlap turned out to be already framed — named families / sub-clusters and v3.3-v3.5 tightenings did substantial framing work; the artefact records this rather than re-flagging

v3.7 Phase B disposition split into B.1 (redundancy review with user sign-off, expected 0–2 merges) and B.2 (mechanical cross-reference additions).

### Phase C — v3.5 follow-up items

**C.1 Cross-reference anchor validation.** Inspection revealed that internal cross-references inside metric bodies were using a collapsed-prefix-with-heading-text-suffix format (e.g. `#gvsg-2-model-update-impact-score`) when the rendered site uses explicit anchors of form `#gv-sg-2`. **58 broken cross-references** were silently failing on the site. All mass-fixed. New audit check `check_metric_cross_references` validates every metric-shaped link against the set of real metric anchors; non-metric anchors (group anchors, section anchors) are skipped. Smoke-tested under fault injection.

A genuine forward-reference was caught in the process: IO.PX-1 referenced `GV.CR-14` (a roadmap candidate, not yet a real metric). Replaced with a prose pointer to the roadmap.

**C.2 GV.CR-5 carve-out circularity.** Limitations section now acknowledges that the regional CCIO escalation pathway assumes capacity that the CIO/CCIO guidance v2 (Jan 2026) does not mandate or fund. Where capacity is absent, the metric's escalation route is non-operational; deployers should document the gap and surface via routes other than this metric (e.g. ICS digital risk register).

**C.3 GV.CR-6 30-day window honesty fix.** The Operational Specification's 30-day post-trigger update requirement now explicitly notes that DCB0129 itself does not specify a numeric window — the 30 days is proposed in v3.5 (already covered in Threshold Guidance Provenance), not a regulatory expectation.

**C.4 GV.PD-8 survey-instrument honesty.** The reference-standard sub-block now explicitly states no validated AVT-specific patient-comprehension instrument exists at the time of v3.6, with two named options: (a) adapt the closest healthcare-IT-comprehension instrument with documented adaptation, or (b) commission a deployer-defined survey reviewed by the IG team mapping to GV.CR-2 content elements.

### Phase D — Repo-root README.md

New [`README.md`](README.md) at the repository root for the GitHub-arrival experience. Per-audience entry points (procurement officer, vendor, developer, researcher); quick links to the published site, monolithic markdown, structured data, and the Outcomes Boundary; status / version block with full tag history; citation guidance with explicit draft warning; contributing pointer (GitHub issues until a CONTRIBUTING file exists); licence TBD with explicit "draft work shared for early feedback" framing pending a licence declaration.

### Counts and audit

- 216 metrics; 43 / 94 / 79 tier split; **25 / 43** Tier 1 metrics tightened — all unchanged from v3.5.
- Three audit checks introduced or reworked: `check_applicability_presence` (new), `check_applicability_totals` (rewritten to derive from per-metric values), `check_metric_cross_references` (new).
- Build clean; audit clean. All four checks fire under fault injection.

### Cross-cutting

- `taxonomy/_header.md` bumped to v3.6 / 2026-04-26 with narrative covering applicability alignment + duplication review + cross-reference audit
- `taxonomy/_how-to-use.md` adds an Applicability dimension paragraph naming the three labels and their counts (48 / 77 / 91)

### Deferred to v3.7

- **Phase A — Pipeline narrow tightening (6 metrics):** TP.ASR-12, TP.ASR-13, TP.WB-2, TP.WB-3, TP.WB-4, TP.SN-20 → would reach 31/43 tightened
- **Phase B — Action on duplication-review findings:** B.1 redundancy review with user sign-off (expected 0–2 merges); B.2 mechanical cross-reference additions to the ~15 overlapping-but-not-framed pairs
- **Phase C — Bespoke deferred-pool scoping:** scope and progress 1–2 of GV.OP-6, GV.SG-9, GV.SG-11, GV.SG-13, HL.HF-3 (each needs bespoke shape; standard pattern is the wrong fit for some)
- 8 TIGHT metrics will not be tightened (pattern would be structural cleanup, not substantive)
- Outcomes layer stays at ES.ME-8/9; the [Outcomes Boundary](#outcomes-boundary) position holds
- Roadmap (`_gaps.md`) untouched in v3.6 — 89 candidates still queued

---

## v3.5 (2026-04-25)

Tightens 12 additional Tier 1 metrics — the two highest-value waves identified in the v3.4 classification artefact. Tightened count: **13/43 → 25/43**. No new metrics; counts unchanged at 216.

### Wave 1 — Compliance/governance core (8 metrics)

The metrics a procurement officer reads first; loose definitions here had the highest practical cost for vendor-comparable evidence:

- **GV.CR-5 ICB Engagement Documentation** — three sub-metrics (notification sent / acknowledged / conditions on file); latency reporting; carve-out logging with regional CCIO escalation after two unanswered notifications.
- **GV.CR-6 Clinical Safety Case Completeness** — per-DCB0129-section reporting (8 sections); named CSO author requirement; differentiated currency windows (sections 2-5 within 30 days of trigger event; sections 1, 6, 8 annual; section 7 live-current); 24-month external-review cadence.
- **GV.CR-7 DPIA Template Completion Rate** — per-section + DPO sign-off binary; significant-change definition mandatory; reconciliation against [GV.CR-6 Clinical Safety Case](#gv-cr-6) hazard list — DPIA risks must be cross-mappable to safety-case hazards.
- **GV.TC-1 Clinician Training Completion Rate** — four-module enumeration (M1 vendor / M2 local induction / M3 failure-mode awareness / M4 refresher) with per-module validity periods; engagement-time floors (30/20/15 min) prevent click-through completion; M3 as safety-critical pause trigger.
- **GV.VT-1 Model Change Notification Compliance** — severity-classified lead times (major ≥ 14d / moderate ≥ 7d / minor ≥ 0d); five-element notification content schema; MHRA PMS substantial-change cross-link with separate compliance failure for missing flag.
- **GV.VT-5 Incident Disclosure Compliance** — severity-driven timelines (24h critical / 72h high / 7d medium / 30d low); rebuttable knowing-time clause; cross-deployer scope mandated as fifth content element (most commonly omitted in vendor-frame disclosures).
- **GV.VT-7 Sub-Processor Transparency** — seven-source discovered-set framework (cloud / model providers / annotation services / contractors / backups / sub-sub-processors); materiality classification; vendor self-cert insufficient — independent verification step required.
- **GV.SG-14 Near-Miss Reporting Rate** — two-source construction (active reports + inferred via [HL.HF-1](#hl-hf-1) safety-critical edit detection); active-to-inferred ratio as safety-culture diagnostic; pause when LFPSE rate rises but near-miss flat or falling.

### Wave 2 — Privacy-chain completion (4 metrics)

Closes the v3.3 storage-location enumeration cascade and completes the privacy lifecycle (deletion → consent → access → erasure):

- **GV.PD-2 Audio Time-to-Deletion** — inherits storage-location enumeration from [GV.PD-1](#gv-pd-1), making the v3.3 cascade explicit; sign-off as `t_consultation_end` per NHSE IG; carve-out logging tracked separately from standard distribution.
- **GV.PD-8 Consent Verification Accuracy** — gap (process compliance minus understanding rate) as the headline metric, not either rate alone; survey instrument declaration mandatory; ≥ 30 patients/quarter floor; demographic disaggregation reveals where understanding fails.
- **GV.PD-10 Subject Access Request Fulfilment** — three sub-metrics (locate / export / timeliness) reported separately; **synthetic SAR test mandatory pre-deployment**, exercising every storage location and sub-processor; extension-pattern alert detects systematic locate/export failure.
- **GV.PD-11 Right to Erasure Compliance** — three-class outcome distinction (deletable / anonymisable / technically-irreversible) operationalises the existing observation that some erasure cannot be fulfilled even in principle; privacy-notice cross-check; Article 17 individual-care exemption scope explicitly handled per NHSE IG March 2026.

### Counts and audit

- 216 metrics; 43 / 94 / 79 tier split (unchanged — v3.5 is structural like v3.4).
- Tightening status now: **25/43 Tier 1 metrics tightened**.
- Audit clean; both v3.4 enforcement checks (`tightening-pattern-presence`, `threshold-provenance-presence`) pass on all 25 tightened metrics.

### Cross-cutting

- `taxonomy/_header.md` bumped to v3.5 / 2026-04-25 with the updated tightened-count
- `taxonomy/_how-to-use.md` updated to list 25 tightened metrics and to repoint v3.6+ scope to the audit output (the 18 remaining Tier 1 metrics: 8 TIGHT, 6 pipeline candidates, 5 deferred)

### Deferred to v3.6+

- 6 pipeline narrow tightening candidates: TP.ASR-12, TP.ASR-13, TP.WB-2, TP.WB-3, TP.WB-4, TP.SN-20
- 5 pattern-may-not-fit deferred: GV.OP-6, GV.SG-9, GV.SG-11, GV.SG-13, HL.HF-3 (each has a structural feature that means the standard pattern is the wrong shape — bespoke per-metric scoping needed)
- 8 TIGHT metrics will not be tightened (pattern would be structural cleanup, not substantive)
- Outcomes layer stays at ES.ME-8/9; the [Outcomes Boundary](#outcomes-boundary) position holds
- Roadmap (`_gaps.md`) untouched in v3.5 — 89 candidates still queued

---

## v3.4 (2026-04-25)

Three deliverables completing the v3.3 tightening work and making the conventions machine-enforced. No new metrics, no new gap-roadmap candidates. Counts unchanged: 216 metrics, tier split 43 / 94 / 79.

### Phase A — Audit-side enforcement

Two new checks in `taxonomy/audit.py` promote the v3.3 conventions from documentation to machine-enforced:

- **`check_tightening_pattern`** — every Tier 1 metric must carry all three tightening sub-blocks (`Reference Standard`, `Operational Specification`, `Threshold Guidance`) or none of them. Mixed (partial) state is an ERROR. Preserves cohort integrity: a metric is either tightened or not, no half-states.
- **`check_threshold_provenance`** — every metric classified as 'tightened' must open its Threshold Guidance block with a `⚠️ **Provenance**` line within the first 400 characters. Closes the honesty gap surfaced by the v3.3 self-review.

`audit.py` also emits a Tier 1 tightening status manifest after the tier counts:

```
Tier 1 tightening status: 13/43 tightened.
  Tightened: GV.CR-1, GV.CR-2, GV.OP-1, GV.PD-1, GV.PD-3, GV.SG-1,
             HL.HF-1, HL.HF-4, IO.PX-1, TP.SN-15, TP.SN-5, TP.SN-6, TP.WB-1
  Not tightened: [30 metric IDs]
```

v3.5+ scope is now derived from this output rather than from CHANGELOG prose. Future contributors see the deferred set in the audit log, not buried in a release note.

The Metric dataclass gained a `body` field (heading-to-next-heading content) so sub-block detection runs on parsed bodies rather than re-reading files.

### Phase B — Phase 3 tightening (4 operational/proxy metrics)

Apply the Reference Standard / Operational Specification / Threshold Guidance pattern (with ⚠️ Provenance prelude written in from the start) to the operational/proxy class — different shape from the safety class (Phase B.1, v3.3) and compliance class (Phase B.2, v3.3):

- **GV.OP-1 Documentation Time per Consultation** — defines doc start/end timestamps; in-consultation vs out-of-consultation breakdown mandatory; pairing with quality companion metric (PDSQI-9 / hallucination rate) mandatory; pause trigger when time-saved positive but quality deteriorates or burden displaces to after-hours.
- **HL.HF-4 Time-to-Sign Distribution** — TTS_norm distribution (P5 / P10 / median / P90) per clinician mandatory; pairing with HL.HF-1 substantive edit rate mandatory (rubber-stamping signal lives in the conjunction); per-clinician baseline; note-complexity stratification.
- **IO.PX-1 Patient Opt-Out Rate** — distinguishes registration-level from per-encounter opt-out (cross-link to GV.CR-1); demographic disaggregation mandatory with χ² + Holm correction; trajectory + disparity-ratio thresholds; the disparities are the metric's value, not the absolute rate.
- **GV.SG-1 Model Version Tracking** — six-component versioning mandatory (ASR / LLM weights / prompt / retrieval / safety classifier / fine-tunes); change-event log structure mandatory; deployer-notification latency monitored; MHRA PMS substantial-change cross-link.

Tightened count: 9/43 → **13/43**.

### Phase C — Full Tier 1 LOOSE classification

`archive/v3.3-tier1-classification.md` (new) classifies every Tier 1 metric not yet tightened as **TIGHT** (8), **LOOSE** (18), or **SURROGATE-and-LOOSE** (3, also LOOSE) with one-sentence per-metric reasoning. The artefact is frozen at v3.4 ship date and is the input to v3.5+ scoping.

Suggested v3.5+ waves identified in the artefact:

- **v3.5 Wave 1 (8 compliance/governance core metrics):** GV.CR-5, GV.CR-6, GV.CR-7, GV.TC-1, GV.VT-1, GV.VT-5, GV.VT-7, GV.SG-14
- **v3.5 Wave 2 (4 privacy-chain completion metrics):** GV.PD-2, GV.PD-8, GV.PD-10, GV.PD-11
- **v3.6+ pipeline narrow tightening (6 metrics):** TP.ASR-12, TP.ASR-13, TP.WB-2, TP.WB-3, TP.WB-4, TP.SN-20
- **Deferred / pattern-may-not-fit (5 metrics):** GV.OP-6, GV.SG-9, GV.SG-11, GV.SG-13, HL.HF-3

The v3.4 release does **not** promote these — it stops at the audit boundary. v3.5 will pick the wave it wants based on stakeholder input.

### Cross-cutting

- `taxonomy/_header.md` bumped to v3.4 / 2026-04-25 with reference to the audit-side enforcement and the published classification
- `taxonomy/_how-to-use.md` updated to list 13 tightened metrics and to point readers at `audit.py` output for current status rather than the prose
- 8 of 30 not-yet-tightened Tier 1 metrics are classified TIGHT and explicitly will not be tightened — the pattern is structural, not substantive, for these

### Counts

Unchanged: 216 metrics, 43 / 94 / 79 tier split, 20 groups. v3.4 is structural, not additive.

`audit.py` baseline updated; build clean; audit clean (both new checks pass on the 13 tightened metrics).

### Deferred to v3.5+

- Tightening of remaining LOOSE metrics per the classification waves above
- Outcomes layer stays at ES.ME-8/9; the [Outcomes Boundary](#outcomes-boundary) position holds
- Roadmap (`_gaps.md`) untouched in v3.4 — 89 candidates still queued

---

## v3.3 (2026-04-25)

Two structural changes addressing critique findings on v3.2: an explicit outcomes boundary and a definitional-tightening pattern applied to nine Tier 1 metrics. No new gap-roadmap candidates are promoted in this release.

### Outcomes Boundary

New cross-cutting file `taxonomy/_outcomes-boundary.md` makes the scope of the taxonomy explicit:

- **What this taxonomy assures:** technical fidelity, documentation quality, clinician oversight, equitable performance, hazard identification, governance compliance, measurement quality. Process, structure, and proximal-outcome measures.
- **What it does not:** clinical-outcome validation - whether AVT changes diagnostic accuracy, patient safety incident rates, downstream care quality, or clinical reasoning. That work belongs to national research bodies (e.g. NIHR RSET), regulators with post-market surveillance powers (MHRA), evidence-standards frameworks (NICE ESF Tier C), and vendors pursuing formal clinical claims.
- **Why drawn explicitly:** to prevent the failure mode where passing every metric in a deployment-assurance taxonomy is read as evidence of clinical benefit.

Two new Tier 2 meta-metrics in Part F operationalise the boundary at procurement:

- **ES.ME-8 Outcome Evidence Commitment Status** - 4-check composite for whether vendor and deployer have committed to outcome evaluation (registered protocol or NHS pilot; PMS plan naming patient-outcome signals distinct from technical-performance signals; baseline data infrastructure; contractual commitment to share results).
- **ES.ME-9 Causal Model Operationalisation** - 4-stage check that each vendor outcome claim is backed by a documented causal chain from proximal performance to distal outcome, with cited mechanisms and named confounders.

ES.ME-1 Proximal vs Distal Outcome Distinction prose updated to point at ES.ME-8/9 as making its "burden of proof on vendors" requirement operational. T.E.S.T. Section B Clinical Effectiveness mapping row updated to reference ES.ME-8 as the closest taxonomy proxy for the 50-point RCT-validation item (commitment, not the evidence itself).

### Tier 1 Definitional Tightening (9 metrics)

Adds three structured sub-blocks to nine Tier 1 metrics where loose definitions previously allowed vendor-selective compliance and non-comparable evidence:

- **Reference Standard** - what counts as ground truth, with inter-rater reliability target where applicable
- **Operational Specification** - measurement window, population, mandatory breakdowns (subtype, severity, category, per-storage-location, per-clinician), aggregation rule
- **Threshold Guidance** - pre-deployment gate, continuous-monitoring alert, pause / escalation trigger

The pattern lifts existing-but-buried content (Tier B underspecification warnings, Limitations, Novel Thinking) into discoverable structured sub-blocks. No new measurement science is invented; existing knowledge is made actionable.

**Phase 1 - five safety-critical metrics:**
- TP.SN-5 Hallucination Rate (CREOLA subtype mandatory; weighted aggregate HR_w; gate ≤ 2 %, pause ≥ 5 % sustained)
- TP.SN-6 Omission Rate (per-CREOLA-category breakdown mandatory; allergies / red-flags / dose / safety-netting critical by default)
- TP.SN-15 Negation Handling Accuracy (negation-type scope explicit; ≥ 200-sentence adversarial test set; allergy-category zero-failure gate)
- HL.HF-1 Edit Rate (substantive vs stylistic distinction; per-clinician baseline mandatory; safety-critical edit rate as separate leading indicator)
- TP.WB-1 Write-back Fidelity (structural / semantic / no-addition decomposition; per-EPR ≥ 200-case test corpus; type-(iii) hallucination into safety-critical fields as binary defect)

**Phase 2 - four compliance/consent metrics:**
- GV.PD-1 Audio Retention Compliance (per-storage-location reporting; cryptographic erasure not logical deletion; independent verification annual minimum)
- GV.PD-3 Transcript Retention Compliance (purpose enumeration mandatory; "quality monitoring" decomposition required; transcript derivatives tracked under same chain)
- GV.CR-1 Patient Dissent Recording Rate (dissent-event scope explicit; coverage-check sampling required when recorded rate implausibly low; per-clinician disaggregation)
- GV.CR-2 Verbal Notification Compliance (four content elements mandatory; method declaration mandatory; ≥ 30 patients/recordings per clinician per quarter)

`taxonomy/_how-to-use.md` adds a paragraph explaining the sub-block structure to readers and lists the nine tightened metrics.

### Counts

- 214 → 216 metrics (+2 from ES.ME-8/9)
- Tier split 43 / 92 / 79 → **43 / 94 / 79**
- 20 groups unchanged
- Meta-evaluation group: 7 → 9 metrics
- Applicability: AVT-Specific 48, AVT-Contextualised 77, General Healthcare AI 89 → 91, total 216

`audit.py` baseline updated; build clean; audit clean.

### Deferred to v3.4

The v3.3 critique work identified ~30 of 43 Tier 1 metrics as LOOSE or SURROGATE (definitional rigour audit, sampled 20 of 43). v3.3 tightens 9 of those; the remainder are deferred:

- **Phase 3 - operational/proxy (4 metrics):** GV.OP-1 Documentation Time per Consultation, HL.HF-4 Time-to-Sign Distribution, IO.PX-1 Patient Opt-Out Rate, GV.SG-1 Model Version Tracking
- **Remaining LOOSE Tier 1 pool (~17 metrics):** scope to be confirmed in v3.4 via a full rather than sampled audit
- **Outcomes layer:** explicitly *not* extended beyond ES.ME-8/9; the [Outcomes Boundary](#outcomes-boundary) position stands
- **Roadmap:** 89 candidates remain in `_gaps.md`; v3.3 promotes none

### Repository hygiene

- `taxonomy/_header.md` updated to v3.3 / 2026-04-25 with reference to the new structural elements
- Plan file `plan-v3.3.md` lives at repo root during the release; will move to `archive/` on completion per the established convention

### Post-release clarification (2026-04-25)

Self-review of v3.3 surfaced an honesty gap in the Threshold Guidance blocks: some numerical thresholds derive from cited sources (e.g. NAS Day Zero SPI, UK GDPR storage limitation, NHSE IG guidance), but others were proposed during v3.3 as starting points without external validation. The original blocks did not consistently distinguish the two, risking over-trust by procurement officers reading the numbers as authoritative.

A ⚠️ **Provenance** prelude was added to each of the nine Threshold Guidance blocks naming which thresholds are cited and which are proposed-as-starting-points, and stating that all numbers require local calibration before contractual use. `_how-to-use.md` updated to explain the distinction. No metric IDs, dimensions, or substantive content changed.

This clarification is a small follow-up to v3.3 rather than a new tag. v3.4 will add an `audit.py` check that flags Threshold Guidance blocks missing the Provenance prelude, so the convention becomes machine-enforced.

---

## v3.2 (2026-04-22)

No new metrics in the taxonomy (still 214 across 20 groups; tier split unchanged 43/92/79). This release restructures the repository around a build pipeline, publishes a documentation site, extends coverage with two external audits and a second AVT-specific framework, and consolidates the roadmap.

### Parser and structured build outputs

New `taxonomy/parse.py` parses every metric from its dimension table (no frontmatter migration needed — derive, don't duplicate). `build.py` now emits to `dist/`:

- `metrics.csv` - 214 flat rows for spreadsheet / BI use
- `metrics.json` - structured catalogue
- `gaps.json` - 89 roadmap candidates with origin tags
- `summary.json` - headline counts

Audit tool (`taxonomy/audit.py`) kept green across the whole release.

### Documentation site (MkDocs Material)

Published as GitHub Pages. Key features:

- One page per group (20 group pages), metrics as anchors
- Tier 1 Quick Reference auto-generated from source
- Per-standard cross-cut pages (one per framework)
- Related-metrics footer on every group page
- Glossary, RSS feed, downloads page (CSV/JSON)
- `mike` version switcher; GitHub Actions deploy
- Site polish: draft banner, Part kicker, applicability quick access, collapsible icon legend, consistent header shape, em-dash sweep

### External coverage audits

Two external-source coverage audits landed alongside the existing 12-framework standards mapping:

- **RSET external review** (Nuffield Trust AVT taxonomy, Feb 2026) — 9 accepted, 4 deferred
- **NHSE IG alignment audit** (Mar 2026) — 4 accepted

Audits archived under `archive/`; findings consolidated into the single roadmap file.

### NHS T.E.S.T. Framework mapping

Added the NHS T.E.S.T. (Technology Evaluation Safety Test) framework to the standards mapping — the AVT-specific ICS-level procurement assurance framework from GOSH/NHS London/C&W/UCL (v11.17625SS, June 2025). Brings total mapped frameworks to twelve.

- **Section A** (platform assurance, 22 binary requirements): 18 directly or strongly covered by existing metrics; 3 are process/product-feature criteria (not metric-shaped); 1 novel gap (translation)
- **Section B** (benefits assessment, 420 points across 12 domains): all 12 domains have at least partial coverage
- **6 novel gap candidates added** to the roadmap: TP.SN-26 (AI Translation Accuracy), GV.PD-15 (Training Data Anonymisation Provenance), GV.OP-13 (Total Cost of Ownership), GV.VT-11 (Multi-Specialty Validation Coverage), IO.FE-9 (Virtual-Care Modality Stratified Performance), GV.VT-12 (Sovereign AI Disclosure)
- Authoritative PDF stored under `reference-docs/` for offline reference

Strongest alignment: T.E.S.T. requirement 18 names three exact taxonomy metrics (hallucination rate, omission rate, WER); requirement 22 (drift) maps directly to the Longitudinal Drift sub-cluster.

### Roadmap consolidation

All gap analyses unified into `taxonomy/_gaps.md`:

- Single source of truth across five origins: RSET, NHSE IG, Standards Mapping, NHS T.E.S.T., Responsible AI Lens
- 89 total candidates (85 accepted/proposed + 4 deferred with preserved reasoning)
- Entry states (`proposed` / `accepted` / `deferred` / `rejected`) so dismissals are durable
- Parsed into `gaps.json` by origin for programmatic use
- Prose gap sections in `_standards-mapping.md` and `_responsible-ai-lens.md` now point here instead of duplicating content

### Repository hygiene

- `.gitignore`: added `.claude/` (local workspace) and the unused 5MB GOSH AAI report; build artefacts (`dist/`, `docs/`, `site/`) already ignored
- `METHODOLOGY.md`: reusable recipe for applying this taxonomy structure to new assurance domains
- `reference-docs/`: new location for authoritative source PDFs cited by mappings

---

## v3.1 (2026-04-18)

### Source Audit Tool

New `taxonomy/audit.py` - parses every group file and verifies:

- Every metric heading has a matching **Reference** row in its dimension table
- Heading tier icon matches the **Priority Tier** row
- Reference-ID prefix matches the group file (e.g. `TP.AC-*` only in `audio-capture.md`)
- No duplicate reference IDs; numbering is contiguous per group
- Tier totals reconcile with `_summary.md` declarations (43 / 92 / 79)
- 214 total metrics across 20 group files
- `_applicability.md` counts sum to 214 (48 + 77 + 89)
- Every metric listed in `_tier-1-quick-reference.md` exists and is still Tier 1
- "See also" cross-references resolve to a known metric (by name or abbreviation)
- All 8 required dimensions present on every metric

Baseline audit at v3.1 tag: **zero findings**. Run `python taxonomy/audit.py` before any future content change.



### Extended Standards Mapping

Added assertion-level or higher-level mapping for seven additional NHS/UK standards. Mapping only - no new metrics added to taxonomy; gaps flagged for future consideration.

**Assertion-level (formal standards):**
- **MHRA SaMD / AIaMD** - Change Programme workstreams (WP1–WP11), SI 2024 No. 1368 Post-Market Surveillance (in force June 2025), Transparency Guiding Principles (June 2024), GMLP 10 principles (Oct 2021)
- **NICE Evidence Standards Framework for DHTs (ECD7)** - all 21 numbered standards across 5 lifecycle areas, Tier A/B/C classification, AI-specific provisions (Standards 4, 5, 6, 15, 16)
- **FHIR UK Core / INTEROPen** - STU1/STU2/STU3 release status, per-profile conformance, UK-specific extensions (NHS Number verification, Ethnic Category, etc.), refinement of TP.WB-6 to mean UK Core not generic FHIR R4

**Higher-level summary:**
- **CQC Assessment for AI** - GP Mythbuster 109 baseline assertions, Five Key Questions (Safe/Effective/Caring/Responsive/Well-led), CSO expectations (flagged as emerging 2025–26)
- **Patient Safety Incident Response Framework (PSIRF)** - four PSIRF principles, response types (AAR, PSII, SEIPS), engagement and board oversight requirements
- **PRSB Clinical Documentation Standards** - Core Information Standard, Outpatient Letter, Discharge, etc.; common header set; narrative vs structured trade-off; relationship to FHIR UK Core
- **Caldicott Principles (2020 revision)** - all 8 principles with direct metric mapping (Principle 8 maps directly to existing GV.CR-1/2/3), Caldicott Guardian role, NDG statutory context

### Proposed New Metrics (Not Yet Implemented)

28 candidate metrics flagged across the 7 new standards to close identified gaps:
- 5 from MHRA (classification, PCCP, PMS reports, transparency, training data)
- 5 from NICE ESF (tier classification, silent mode, subgroup drift, cost-effectiveness, budget impact)
- 3 from FHIR UK Core (per-resource conformance, UK extensions, STU version targeting)
- 4 from CQC (board governance, CSO capacity, AI complaints, Reg 17 record quality)
- 4 from PSIRF (SEIPS analysis, compassionate engagement, Just Culture, learning tracking)
- 4 from PRSB (semantic completeness, narrative preservation, AIS capture, legal status)
- 3 from Caldicott (DPIA justification, consultation appropriateness, per-item necessity)

Distribution: 6 × Tier 1, 19 × Tier 2, 3 × Tier 3. Highest-leverage addition: **TP.WB-11 PRSB Semantic Completeness** (appears as gap across multiple standards).

### New Responsible AI Lens Document

New cross-cutting file `taxonomy/_responsible-ai-lens.md` providing a policy-intent view of the taxonomy complementary to standards mapping and applicability classification.

**Part A: DSIT AI Playbook for the UK Government (Feb 2025) - 10 principles:**
- P1 (Know AI and its limitations), P2 (Lawful/ethical), P3 (Security), P4 (Meaningful human control), P5 (Lifecycle management), P6 (Right tool for the job), P7 (Open and collaborative), P8 (Commercial colleagues), P9 (Skills and expertise), P10 (Organisation policies and assurance)
- Each principle has narrative + metric table + gap notes

**Part B: Six Responsible AI Ethical Themes** (AI Regulation White Paper five + Playbook-added sixth):
- T1 (Safety, Security and Robustness), T2 (Transparency and Explainability), T3 (Fairness), T4 (Accountability and Governance), T5 (Contestability and Redress), T6 (Societal Wellbeing and Public Good)
- Each theme has narrative + metric table + trade-off notes

**Part C: Coverage Matrix** - 25 policy-lever metrics that cross-cut 3+ principles/themes simultaneously. Five "megas" cross 5–6 axes: GV.SG-11 (Adverse Event/LFPSE), GV.VT-4 (Audit Trail), GV.CR-3 (AI Content Labelling), HL.HF-1 (Edit Rate), IO.PX-1 (Patient Opt-Out).

**Part D: Gaps** - 20 principle-level + 18 theme-level gaps identified; cross-referenced to Proposed New Metrics. Societal Wellbeing (T6) has highest gap concentration; P6 (Right tool) and P7 (Openness) weakest principles.

### Build

- `build.py` now assembles from 28 files (was 27) - added `_responsible-ai-lens.md`
- All 214 metric reference IDs preserved; no existing metrics changed
- Tier counts unchanged: 43 Tier 1 / 92 Tier 2 / 79 Tier 3
- All metric references in new sections validated against assembled taxonomy

---

## v3.0 (unreleased)

### Reference IDs
- Every metric now carries a unique reference ID in the format `{Part}.{Group}-{Number}` (e.g. `TP.AC-1`, `GV.CR-7`)
- IDs appear in both the metric heading and the dimensions table
- Part abbreviations: TP (Technical Pipeline), PI (Pipeline Interactions), HL (Human Layer), IO (Impact & Outcomes), GV (System Governance), ES (Evaluation Science)
- 20 group abbreviations documented in the Reference IDs section of How to Use
- Reference key legend added to How to Use section

### Applicability Classification
- New cross-cutting section classifying all 214 metrics by applicability:
  - **AVT-Specific** (48 metrics, 22%) - meaningful only with the audio pipeline
  - **AVT-Contextualised** (77 metrics, 36%) - general concept, AVT-tuned definition
  - **General Healthcare AI** (89 metrics, 42%) - applicable to any clinical AI system
- Summary and per-part breakdown tables included
- Full per-metric classification table with reference IDs

### New Metric Families
- **Medication Safety Thread** (4 metrics: TP.SN-19, TP.SN-21, TP.CC-5, IO.PX-10) - cross-cutting family tracking medication accuracy from summarisation through coding to patient outcomes
- **Demographic Equity Disaggregation** (7 metrics: TP.ASR-4, TP.ASR-5, TP.CC-9, PI.E2E-5, IO.FE-2, IO.FE-4, IO.FE-5) - cross-cutting family applying demographic disaggregation across pipeline layers

### New Sub-clusters
- **Write-back Safety** (4 metrics: TP.WB-1 through TP.WB-4) - the four Tier 1 pre-deployment gates at the EPR integration boundary
- **Coding Fidelity** (7 metrics: TP.CC-1 through TP.CC-6 plus TP.CC-11) - accuracy of individual code assignment across NHS terminology systems

### Standards Mapping
- New cross-cutting section with assertion-level mapping to four NHS/regulatory frameworks:
  - **DTAC v2.0** - all 5 sections (C1 Clinical Safety, C2 Data Protection, C3 Technical Security, C4 Interoperability, D1 Usability)
  - **DSPT v8** - all 10 National Data Guardian standards with individual assertion mapping
  - **DCB0129/DCB0160** - all 7 clinical safety lifecycle stages
  - **NHS England LLM Evaluation & Monitoring Framework v0.2.2** - all 30 dimensions across 3 groups (flagged as draft)
- Gap summary identifying 9 areas where standards require coverage the taxonomy doesn't provide
- Coverage summary identifying 8 areas where the taxonomy extends beyond all standards

### Count Corrections
- Tier breakdown corrected from 42/87/85 to **43/92/79** (Tier 1/Tier 2/Tier 3) in Summary and How to Use
- Human Factors & Workflow metric count corrected from 20 to **19** in Contents
- EPR Write-back tier breakdown corrected from "4 Tier 1 · 1 Tier 2" to **4 Tier 1 · 2 Tier 2 · 1 Tier 3**
- Clinical Coding tier breakdown corrected from "2 Tier 2 · 2 Tier 3" to **1 Tier 1 · 8 Tier 2 · 3 Tier 3**

### Build
- `build.py` now assembles from 27 files (was 25) - added `_applicability.md` and `_standards-mapping.md`
- Family count: 6 (was 4)
- Sub-cluster count: 6 (was 4)
- Unaffiliated metrics: 189 (was 200)

---

## v2.0

- 214 metrics across 20 groups (was 151 metrics across 18 groups in v1)
- 63 new metrics added in batches 1-4
- 2 new groups: NHS Compliance & Regulatory, Environmental & Sustainability
- 4 named metric families: Clinical Content Fidelity, Post-Generation Correction, Clinical Transcription Accuracy, Reference-Based Text Similarity
- 4 sub-clusters: Conversation Analysis, Sociotechnical & Resilience, Patient Clinical Outcomes, Longitudinal Drift & Model Contamination
- 15 underspecification warnings across Tiers A/B/C
- Tier 1 Quick Reference section organised by responsible actor

## v1.0

- Initial release: 151 metrics across 18 groups
- Modular file structure with `build.py` assembler
- Monolithic source split into `taxonomy/` directory
