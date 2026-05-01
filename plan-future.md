# Future work — taxonomy backlog

A running list of cross-release improvements that don't fit the current release plan. Items here are deferred work, not blocked work — promote to a release plan when ready to execute.

Format per item: short title, status, context (the *why*), and starting points (where to look in the codebase / what to consider first).

---

## 1. Interactive metric explorer — demo first, permanent later

**Status:** queued — wanted as a quick demo artefact, with a path to a permanent site feature.

**Context:** The catalogue is 218 metrics across 20 groups, each tagged with 12 dimensions (Priority Tier, Cadence, Pipeline Layer, Assurance Question, Measurement Method, Lifecycle Phase, Responsible Actor, Maturity, Outcome Type, Applicability, plus the Reference ID and Source). Linear reading misses the cross-cuts: *"what's the Tier 1 deployer-owned set?"*, *"which metrics are continuous vs one-off?"*, *"how does the safety-question coverage differ between technical-pipeline and governance groups?"*. An interactive visualisation — filterable by tier, group, and the other dimensions — would make the catalogue legible at a glance and is demo-able to stakeholders in a way the markdown isn't.

The user wants a **scrappy demo soon** but with the understanding that this is likely to become **a permanent site feature later**. That framing matters: a throwaway demo can hardcode whatever it likes, but if the demo is the prototype for a permanent feature, a few decisions are worth making deliberately rather than by accident.

**Decisions to make deliberately even in the demo phase:**
- **Data source.** The CSV/JSON downloads (already produced by `parse.py` since v3.8.3, with `part_name` field) are the natural feed. Using them rather than scraping the markdown means the demo benefits automatically from any future schema additions and stays consistent with what downstream users see.
- **Hosting model.** A pure client-side static page (data baked in or fetched from `/downloads/*.json`) is the lowest-friction path and lets the demo live alongside the existing site without backend changes. A separate Streamlit / Observable / similar app is faster to prototype but harder to fold into the permanent site later — worth picking the embeddable path early.
- **Filter axes vs visual axes.** The 12 dimensions are too many to all be visual at once. Likely split: 2–3 are *visual* (e.g. tier as colour, group on one axis, cadence on the other), the rest are *filters*. Picking which goes where shapes what questions the visualisation answers — for the demo, lean to questions stakeholders actually ask, not exhaustive coverage.
- **Drill-down.** Each metric tile/cell should link back to the rendered taxonomy page for that metric (the existing site already has per-metric pages with anchors). That's the bridge from "exploration" to "reading the actual definition" and is the thing that makes the visualisation more than a wall chart.

**Starting points:**
- Data feed: `taxonomy/build.py` and `parse.py` already emit CSV/JSON with all 12 dimensions plus `part_name`. The existing site downloads page (live-derived per v3.8.1) is the canonical feed.
- Quickest demo path: a single static HTML page with a JS chart library (D3, Observable Plot, or Vega-Lite — Vega-Lite has the lowest code-to-output ratio for tier-by-group small-multiples and similar). Hosted at `site/explorer.html` or similar.
- Reference visualisations worth looking at before designing: NIST AI RMF crosswalk views; FAIR Principles dashboards; the OWASP LLM Top 10 site's filter UI. None are perfect matches but each shows one kind of metric-catalogue navigation.
- For the permanent path: think about whether the explorer becomes the *primary* navigation entry-point for the site or a secondary "explore" tab. If primary, the existing TOC-driven nav becomes redundant for many users — that's a bigger UX decision worth surfacing before committing.

**Demo-vs-permanent split, suggested:**
- *Demo (now):* one static HTML page, hardcoded data feed, 2–3 charts (tier × group, cadence × actor, an interactive filter table), drill-down links to existing per-metric pages. Build for demo screenshots and one-off stakeholder walk-through.
- *Permanent (later):* same page promoted to a first-class site feature, fed live from build outputs, integrated with site nav, accessibility-reviewed, mobile-friendly, citable URL. Treat the demo as scaffolding, not the finished thing.

The thing to avoid: building the demo, getting positive stakeholder reaction, and then having the demo become the permanent feature by inertia without the deliberate design pass. Flag explicitly when promoting from demo to permanent that the second pass is needed.

---

## 2. Fix AVT Registry table to have a tier column

**Status:** queued.

**Context:** The NHSE AVT Self-Certified Supplier Registry was added as the 13th standards-mapping framework in v3.8 (see [project_v3_8_release.md](.claude/projects/-home-djs-projects-claude-avt-taxonomy/memory/project_v3_8_release.md) and `archive/plans/plan-v3.8.md`). The corresponding registry table currently does not carry a Priority Tier column, so registry-driven metrics can't be filtered or rolled up by tier the way the rest of the catalogue can. Adding the column makes the registry consistent with the standards-mapping convention used elsewhere.

**Starting points:**
- The registry table is in the standards-mapping section — grep `taxonomy/` for "AVT Self-Certified" or "Supplier Registry".
- Compare column structure with the other 12 frameworks already in standards-mapping for consistency.
- Tier values for existing registry-driven metrics (GV.SC-12 Cyber Essentials Plus, GV.VT-13 Evidence Pack Freshness, GV.VT-14 Indicative Pricing Transparency) are in their metric files and can be lifted directly.

---

## 3. Versioning strategy across the project (metrics, tier selections, site, repo)

**Status:** scoping — needs a design decision before implementation.

**Context:** The repo currently has a single version line (`TAXONOMY_VERSION` in `parse.py`, surfaced into `_header.md`, the site banner, and CSV/JSON downloads since v3.8.4). That single version covers everything: catalogue content, tier selections, website, build tooling, gap lists. As the project matures this is starting to crack at the seams — they all change at different cadences and have different downstream-user contracts:

- **Metrics** are edited in place. When a definition tightens, the new version overwrites the old. There's no per-metric history beyond `git log`, which is workable for maintainers but opaque to deployers / vendors who cite the taxonomy and need to know which definition of a metric they implemented against. The v3.7 deprecate-don't-renumber pattern (TP.CC-7/8 → parent + sub-parts) is a partial answer; per-metric versioning (e.g. `TP.AC-1 v2`, with a changelog block) would let downstream users pin to a specific definition.
- **Tier selections** are arguably a distinct artefact. A clinical-safety officer selecting Tier 1 minimum metrics for an assurance package is making a different commitment than the catalogue-author tightening a Formal Definition. Tier selections might warrant their own versioning so that "the Tier 1 minimum set as of v3.8" is a stable reference even if individual metric definitions evolve.
- **Site** is currently versioned with the catalogue (the banner reads the same `TAXONOMY_VERSION`), but site-only patches (v3.8.1, v3.8.2, v3.8.3, v3.8.4) have already had to use point-release sub-versions because the catalogue didn't change. That's a sign the coupling is too tight — the site changes for tooling / cosmetic / deploy reasons that shouldn't bump the catalogue version.
- **Repo** (build tooling, audit.py, parse.py, CI) is currently invisible from a versioning perspective — bug fixes ship without any version mark. For a public artefact this is fine; for downstream consumers building against the CSV/JSON it is not, since a `parse.py` change can alter the schema (cf. v3.8.3 adding `part_name`) without any version signal beyond the patch number on the catalogue.

The design question is whether to:
- **(a) Single version, status quo** — keep one version line, accept the coupling, document the convention better. Cheap, but the cracks will widen.
- **(b) Per-axis versioning** — e.g. `catalogue: v3.9 / tier-set: v2 / site: v1.4 / tooling: v2.1`. More honest but more cognitive load.
- **(c) Hybrid: catalogue version + tier-set version, single site/tooling line** — the load-bearing cases (catalogue content, tier selections) get independent versions; the rest stay coupled.
- **(d) SemVer for the whole repo with strict change-class rules** — `MAJOR.MINOR.PATCH` where MAJOR = breaking change to citations / catalogue structure, MINOR = additive metric work, PATCH = site/tooling. Disambiguates by class of change rather than by axis.
- **(e) Per-metric versioning combined with one of the above** — orthogonal: each metric has its own version stamp regardless of the overall scheme.

There's no obviously-right answer; this needs an explicit design decision and probably a short ADR-style write-up before implementation.

**Starting points:**
- Read the v3.8.x release sub-numbering convention in the memory entries ([project_v3_8_1_site_fixes.md](.claude/projects/-home-djs-projects-claude-avt-taxonomy/memory/project_v3_8_1_site_fixes.md) through [v3_8_4](.claude/projects/-home-djs-projects-claude-avt-taxonomy/memory/project_v3_8_4_banner_live_derived.md)) — those four point releases are the clearest evidence that the current single-version scheme is being stretched.
- Look at how comparable taxonomies / standards bodies handle this. SNOMED CT has separate version lines for the international edition vs national extensions; HL7 FHIR has a release version + a profile version + an implementation guide version. ICD-11 has annual minor revisions distinct from major editions. Worth picking 2–3 reference models and seeing which fits the AVT taxonomy's downstream-use patterns.
- Look at the v3.7 deprecate-don't-renumber pattern in [project_v3_7_release.md](.claude/projects/-home-djs-projects-claude-avt-taxonomy/memory/project_v3_7_release.md) and the relevant TP.CC-7/8 → parent + sub-parts refactor — that's the closest existing precedent for per-metric lineage.
- Lighter-weight alternatives to consider before committing to a full scheme: a "Last-tightened" date field in each Dimensions table; a Changes section per metric; a release-by-release diff table at the catalogue level; a "Tier set as-of" timestamp in `_tier-1-quick-reference.md`.
- Trade-off to think about: every additional version axis is overhead at every edit. The right answer might be no more than one or two extra axes, not five.

**Decision needed before implementation:** which scheme. This shouldn't be a Claude call — it's a project-direction decision. Surface as an explicit design question to the user when this item is promoted to a release.

---

## 4. Full Tier 1 gap review and minimum-set construction (post-agreement)

**Status:** queued — needs explicit go-ahead before starting.

**Context:** The catalogue is at 218 metrics with 43 in Tier 1 (`Minimum Viable`), but Tier 1 was built up incrementally rather than as a coherent minimum-viable set with explicit coverage criteria. A full review of `_gaps.md` (cross-referenced against the existing Tier 1 metrics and the Tier 1 Quick Reference) would identify whether the current 43 actually constitute a defensible minimum-viable assurance set, or whether there are coverage holes that need filling.

This is a substantial body of work and should not start without an explicit user decision on scope and criteria — hence the "after agreement" qualifier in the original ask.

**Starting points:**
- The existing Tier 1 set is summarised in `taxonomy/_tier-1-quick-reference.md` (organised by responsible actor).
- Gaps file at [taxonomy/_gaps.md](taxonomy/_gaps.md) lists known coverage holes by category (P1–P5).
- The v3.3 Tier 1 classification work in `archive/v3.3-tier1-classification.md` is the closest existing artefact to a Tier 1 review and frames where the gaps are likely to be.
- Decision points to surface before starting: what counts as "minimum viable" coverage (every assurance question? every pipeline layer? every responsible actor?), and what threshold of evidence promotes a gap into a metric.

---

## 5. Verify code snippets *and* Formal Definitions against sources

**Status:** queued.

**Context:** Two adjacent bodies of content carry the same provenance risk and should be reviewed together:

1. **Code snippets** — roughly a dozen metrics include them (e.g. the `pyannote` DER snippet at TP.DI-1, scikit-learn calibration code at calibration metrics, the stigmatising-language detection lexicon at TP.SN-24). Authored by Claude during earlier integration passes; not independently verified against cited sources or run end-to-end.
2. **Formal Definition blocks** — every metric has one, and many were authored or edited by Claude in the same passes. The mathematical / operational definition is the load-bearing part of each metric — if it doesn't match what the cited source actually defines, downstream implementers will measure something subtly different from what the catalogue claims to standardise. The v3.9 Phase 2 URL review surfaced multiple cases where Source-row *claims* didn't match the cited paper; the same drift is plausible in Formal Definitions and has not yet been checked.

The two need to be verified **as a pair, per metric**, not as two separate sweeps. The snippet should implement the definition, and the definition should match the cited source — checking either in isolation misses the cross-consistency case where snippet and definition agree with each other but both diverge from the source.

**Starting points:**
- For code: grep `taxonomy/` for code blocks (` ```python ` and other language tags). Check imports / API surface against the current version of the cited library (pyannote, scikit-learn, dscore, FHIR validators, etc.).
- For definitions: every metric file has a **Formal Definition** block — these are the primary review target, not an afterthought. Compare the formula / operational rule in the block against the Source-row citation.
- Cross-consistency check, per metric: (a) does the snippet implement the Formal Definition? (b) does the Formal Definition match the cited source? Both must hold.
- Likely high-yield places to start: the pipeline metrics in part-a (where the most code lives and the most precise mathematical definitions sit), and the calibration / fairness metrics in part-d (where formulas are most load-bearing and most paper-derived).
- Sequencing: definitions are the larger surface area (every metric) and the higher-risk content (the standardisation contract). If the work has to be split, do definitions first, snippets second.

---

## 6. Metrics around deprecation and decommissioning

**Status:** queued — partially in `_gaps.md` already.

**Context:** Two relevant gaps already exist at [taxonomy/_gaps.md:182-183](taxonomy/_gaps.md#L182-L183) under "P5 - Lifecycle":
- "Decommissioning plan" (Medium priority)
- "Model retirement criteria" (Low priority)

So this is **promote-from-gaps-to-metrics** rather than identify-new-gaps. The ask covers the lifecycle end of the AVT system: when a vendor announces end-of-life, when a deployer chooses to decommission, when a model is retired or replaced — what assurance metrics are needed for the wind-down? This connects to the existing GV.VT-1 Model Change Notification Compliance work (which covers updates) but explicitly extends it to retirement events, which the existing metrics do not cover.

**Starting points:**
- Look at the two existing gap entries first — see whether they already define enough to lift into draft metrics.
- Consider whether decommissioning is one metric or several: notification of retirement (vendor → deployer), data-handling on decommission (clinical record retention, training data fate), continuity of access to historical AI-generated content, transition planning.
- Cross-check against MHRA Post-Market Surveillance regs and DCB0129/0160 retirement provisions — there may be regulatory expectations to align with.
- Adjacent existing metrics: GV.VT-1 (change notification), GV.SG-1 (version tracking) — retirement events should plug into the same telemetry surfaces.

---

## How to use this file

- **Adding items:** follow the format above. Lead with status, then *why*, then *starting points*. Don't write the implementation here — that goes in a release plan when the item is promoted.
- **Promoting to a release:** when an item is ready to execute, lift it into the relevant `plan-vX.Y.md` and either remove it from this file or mark its status as "in flight in vX.Y".
- **Removing items:** if an item turns out to be obsolete, redundant, or already done, delete it with a brief commit message explaining why. Keep this file focused on actual deferred work, not historical record (that's what `archive/` is for).
