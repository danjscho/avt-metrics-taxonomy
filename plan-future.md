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

## 7. Citation grammar review — should inline links carry a human-readable name?

**Status:** queued — revisit after the v3.9 release lands and the catalogue + Phase 3 inline-linking has had a release cycle to sit.

**Context:** v3.9 settled on bare-handle inline links for the new citation grammar — `[NHSE-IG-Guidance-2026-03]`, `[UK-GDPR]`, `[DCB0129]`, etc. — with the catalogue entry in `_references.md` carrying the full bibliographic record. This is clean for audit (every handle resolves) and clean for the catalogue (single source of truth), but it has one cost: the inline reference reads as a slug, not as prose. A clinician scanning a Threshold Guidance block sees `[NHSE-IG-Guidance-2026-03]` rather than "NHSE IG guidance March 2026", and has to either know the slug-to-name mapping or click through to find out what the citation actually points at.

The alternative shape — **human-readable name + parenthetical handle** — would render as: "the NHSE IG guidance ([NHSE-IG-Guidance-2026-03])" or "UK GDPR Article 5(1)(e) ([UK-GDPR])". More readable in prose; more verbose to maintain; arguably duplicates information that the catalogue already holds. Other options worth considering:
- **Markdown reference-style links** with a display name: `[NHSE IG guidance][NHSE-IG-Guidance-2026-03]`. Render-time the name shows; the handle is the link target. Cost: more characters in source, but readers see the name not the slug.
- **Bare-name inline + audit on prose-handle correspondence.** Don't link at all in prose; rely on the Source row + catalogue. Cost: easier to drift over time.

The trade-off is **maintainer burden vs reader experience**. Bare handles are fine for maintainers who recognise them; human-readable forms are friendlier for first-time readers (which is most readers, for a public taxonomy).

**When to revisit:** after v3.9 ships and Phase 3 has been read by enough people for there to be evidence either way. Don't make this call mid-Phase 3 — sweeping ~110 blocks twice (once to bare handles, once to enriched form) is wasteful; better to land Phase 3 in the simpler shape, get feedback, decide.

**Starting points:**
- Sample reader test: pick 3 readers (one clinician, one IG officer, one taxonomy maintainer) and show them a Reference Standard block in both shapes. Ask which they'd prefer to read at speed.
- Consider partial adoption: human-readable form for prose-heavy contexts (Reference Standard, Threshold Guidance, Novel Thinking) but bare handles for compact contexts (Source rows, Provenance preludes). Mixed conventions are a maintainer cost but may be the right reader experience.
- Check what comparable taxonomies do. NIST AI RMF, NHS DTAC, and the OWASP LLM Top 10 each handle citation density differently — worth a brief scan for prior art before re-sweeping.

**Decision needed before re-sweep:** which shape, and whether to apply uniformly or contextually.

---

## 8. Threshold-numbers review — remove or reword "proposed as starting points" thresholds

**Status:** queued, **design exploration first**. The shape of the fix is not yet decided; this item is a problem statement plus a list of options, not a settled approach. High-priority for v3.10 because it touches the taxonomy's quantitative credibility, but the *how* needs deliberate work before any sweep.

**Context — what's currently in the document.** Most tightened Tier 1 metrics carry Threshold Guidance blocks with specific numerical thresholds — pre-deployment gates, continuous-monitoring alerts, pause/escalation triggers. Examples:

- "Substantive ER between 30 % and 80 % during the first 4 weeks; ER below 30 % in week 1 is a flag" (HL.HF-1 Edit Rate)
- "Monthly compliance ≥ 99.5 % per storage location; alert on any single non-exception retention" (GV.PD-1 Audio Retention Compliance)
- "≥ 50 samples per category, 0 critical / 1 % moderate / 5 % benign aggregate gates" (TP.ASR-12 ASR Hallucination — Non-Speech Audio)
- "30/20/15-minute engagement floors, 12-month refresher cadence, 100 % gate" (GV.TC-1 Training Completion)
- "P5 < 0.3 s/word pause trigger, 4-week baseline window, 10 % below-baseline rate alert" (HL.HF-3b Time-to-Sign Distribution)

These thresholds carry a `⚠️ Provenance` prelude that distinguishes **cited numbers** (e.g. UK GDPR storage-limitation, NHSE IG 30-day SAR window — externally validated) from **"proposed in v3.X as starting points"** (calibrated against the metric's clinical-safety logic during taxonomy authoring, but not externally validated). The Calibration & Context principle (`_calibration-and-context.md`) explicitly tells deployers these starting-point numbers require local calibration before contractual use.

**The risk.** A "proposed in v3.5 as a starting point" threshold reads as more grounded than it is once it's been sitting in the taxonomy for a few releases. The longer a number sits, the more it accretes apparent legitimacy through citation by deployers, vendors, and procurement leads. The Calibration & Context principle's framing ("starting point", "indicative", "require local calibration") is doing real work, but it's competing with the cognitive ease of reading a specific number and treating it as a default. Multiply this across ~25 Tier 1 metrics carrying tightening patterns, each with several starting-point numbers, and the taxonomy is exposed: a procurement contract can quote a number from the taxonomy that was never externally validated and derive defensible-looking weight from the citation.

**Why this matters more for a taxonomy than for, say, a vendor whitepaper.** A vendor can publish a benchmark threshold and own it; their reputation and product behaviour are tied to it. A taxonomy is a public assurance frame — its credibility depends on every claim being defensible, especially the ones that look quantitative. Numbers that aren't externally validated are exactly the citation-loop risk the v3.9 references-validity sweep was created to address; this is the same problem one layer deeper.

**The design space (not yet chosen).** Several shapes the fix could take, each with different reader-experience and maintainer-cost trade-offs:

- **Option 1 — Per-metric triage (a/b/c framework).** For each "proposed as starting points" threshold, decide:
  - **(a) Keep the number** if it has actual external grounding that wasn't surfaced clearly. Promote the citation.
  - **(b) Replace the number with calibration guidance** ("how to set the number" prose, e.g. *"compliance threshold should be set by the deployer's DPIA risk appetite and audit cycle; typical NHS digital compliance metrics target 99–99.9 % depending on consequence severity. Document the chosen number and the reasoning."*).
  - **(c) Drop the number entirely** where the construct doesn't actually need one (binary compliance gates, single-instance pause triggers).

  Heaviest touch — every metric is reviewed individually. Most defensible reader-experience outcome but the highest maintainer cost.

- **Option 2 — Wholesale removal.** Drop all "proposed as starting points" numbers across every Threshold Guidance block; rely entirely on the Calibration & Context principle for "set your own number" guidance. Lightest reader-experience cost (no fake authority); biggest reader-experience cost (deployers lose any starting frame). May force premature decision-making by deployers who don't have a baseline to start from.

- **Option 3 — Wholesale rewording without removal.** Keep all the numbers but rewrite Threshold Guidance prose so the calibration-required nature is unmissable. E.g. wrap every starting-point number in *"For a deployment matching the taxonomy's reference profile (medium-volume general practice, mature governance), this would be approximately X. Calibrate against your context."* Heavier than Option 2 but lighter than Option 1; the numbers stay but their status is harder to misread.

- **Option 4 — Section rename + structural separation.** Keep Threshold Guidance as a section but rename it (e.g. *"Calibration Guidance"* or *"Threshold-setting framework"*). Within each block, move externally-cited numbers to a separate "Cited threshold" sub-block and starting-point numbers to a "Starting-point — calibrate before use" sub-block. The structural break does work the prose alone struggles to do. Heaviest structural change.

- **Option 5 — Visual / typographic distinction.** Keep numbers and prose, but render starting-point numbers in a deliberately weaker visual treatment on the rendered site (italics, smaller font, callout box). Reader effort to read = reader effort to mistake-as-default. Cheapest to implement; relies on visual conventions that may not survive copy/paste into a procurement spec.

- **Option 6 — Hybrid.** Apply Option 1 (per-metric triage) but use Option 3's prose wrapping where (b) applies. Most likely real-world answer.

**The unresolved questions.**

1. **Are the starting-point numbers genuinely arbitrary, or are they better grounded than the prose admits?** Some "proposed in v3.X" numbers may have implicit grounding (NHS digital service availability targets, ICO breach windows, CQC inspection cadence) that the taxonomy author had in mind but didn't cite. A first pass should *surface this grounding where it exists* before deciding to drop or rewrite.

2. **Does the procurement context change what's safe?** If a deployer's contract pulls a starting-point number into the SLA, who carries the liability for the number being wrong? The taxonomy doesn't currently say; the Calibration & Context principle implies the deployer, but this is worth surfacing more explicitly.

3. **Does the audit need to enforce anything new?** Currently `audit.py` doesn't distinguish starting-point numbers from cited numbers in any structured way. A new audit check (`check_starting_point_numbers_have_calibration_guidance`?) would lock in whichever option is chosen.

**Starting points for the design exploration:**

- Enumerate the surface: `grep -rn "proposed in v3" taxonomy/` (~25–30 Provenance lines across the Tier 1 tightened metrics). For each, capture: the metric, the number, the surrounding prose, and whether the number maps to an external standard the author had in mind.
- Sample-test with a small set of readers (clinician, IG officer, procurement lead, vendor): show them a current Threshold Guidance block in each option's shape and ask which shape would *actually* drive them to calibrate vs. paste the number into a contract. Reader-experience evidence beats theoretical reasoning here.
- Cross-reference against `_calibration-and-context.md` so whichever option is chosen reinforces (rather than competes with) the existing principle.
- Decide whether this lands as a v3.x patch or v4.x — Option 1 (per-metric triage) is substantial enough to want a release of its own; Options 2/3/5 are surgical enough for a patch.

**Promote to a release plan when:** (i) a single option is chosen with reader-experience evidence backing it, AND (ii) the surface enumeration is complete (so we know what we're committing to). Until then this stays in plan-future as a problem statement, not a release item.

**v4.2 update:** Pass A / Pass B verification (plan-v4.2.md) flagged that several Tier 2/3 metrics outside the Tier 1 tightened set ALSO state engineering-default thresholds authoritatively without Provenance preludes. The v4.2 TP.AC sweep added preludes to ~6 such metrics, and the mpathic / Hybrid-Code / n2c2 fixes added preludes to several more across TP.DI, TP.SN, TP.CC. The surface enumeration this item depends on is therefore now larger than the original ~25–30 Provenance lines — closer to ~40 across both the Tier 1 tightenings and the v4.2 additions. The reviewer of v4.2 explicitly raised whether the taxonomy should be publishing thresholds at all (vs. saying "these should be derived locally") — this option now sits above the existing Option 1–6 design space as a more radical alternative worth weighing. **Add Option 7: Drop all numerical thresholds; provide only calibration framework + reasoning prompts.** The v4.2-added preludes are deliberately non-load-bearing rewordings — they preserve the numbers as proposed-as-starting-points so they're easy to remove wholesale if Option 7 wins, or to keep with stronger framing if Option 3/6 wins.

---

## 9. ISO and BSI standards — where do they play a role?

**Status:** queued — design exploration. The taxonomy currently engages with NHS / UK / EU regulatory frameworks (DTAC, DSPT, DCB0129/0160, MHRA SaMD, NICE ESF, FHIR UK Core, CQC, PSIRF, PRSB, Caldicott, NHS T.E.S.T., NHSE AVT Registry, NHS LLM Framework — 13 frameworks) plus a smattering of academic / vendor citations. **ISO and BSI standards are almost entirely absent**, even though they're the international layer that sits underneath several of the NHS frameworks and increasingly underpins NHS procurement on the AI side.

**Current state.** ISO / BSI / IEC are mentioned in exactly two places in the taxonomy:

- One row inside the NICE ESF mapping table (`_standards-mapping.md`) cites BS EN 62304, IEC 82304-1, ISO 13485, IEC 62366-1 as expected best-practice references for medical device software safety, quality, and usability — but the row is just listing what NICE expects, not making the standards mappable themselves.
- The Retrieved-date format note in `_references.md` (ISO 8601 — incidental, not relevant).

That's it. Neither **ISO/IEC 42001** (AI management system, 2023 — already showing up in NHS AI procurement asks) nor **BS 30440** (BSI's healthcare-AI validation framework, 2023 — explicitly designed for the assurance use case this taxonomy serves) is engaged with. Several of the NHS frameworks the taxonomy *does* map (DTAC, DCB0129/0160) have ISO/BSI underpinnings the taxonomy doesn't surface.

**What's potentially relevant.** Without committing to mapping any of them yet, the candidates are:

- **BS 30440 (2023)** — *Validation framework for the use of artificial intelligence within healthcare*. BSI-published. Explicitly the same problem space this taxonomy occupies; arguably the closest international peer. Worth understanding *first* and deciding whether to (a) map alongside the other 13 frameworks, (b) cite as a parent / peer framework that the taxonomy specialises for AVT, or (c) leave alone if scope-incompatible.
- **ISO/IEC 42001 (2023)** — *AI management system*. The AI equivalent of ISO 27001 / 9001. Increasingly cited in NHS digital procurement. Organisation-level rather than product-level, so may map at the deployer-side governance dimensions (GV.SG, GV.VT) rather than at individual metrics.
- **ISO/IEC 23894 (2023)** — *AI guidance on risk management*. Companion to ISO 31000. Relevant to GV.SG-7 (PRA framework) and the broader governance cluster.
- **ISO/IEC 5259 series (2024–)** — *AI data quality*. Relevant to TP.SN training-data and clinical-coding dimensions.
- **ISO 14971** — *Medical device risk management*. Already implicit in DCB0129; the taxonomy could surface the lineage.
- **IEC 62304** *(BS EN 62304 in UK form)* — *Medical device software lifecycle*. Underpins the SaMD frame; partially surfaced via MHRA SaMD mapping but not directly engaged.
- **IEC 82304-1** — *Health software product safety*. The newer general-software-not-classified-as-device standard; relevant for AVT vendors not pursuing SaMD classification.
- **IEC 62366-1** — *Medical device usability engineering*. Already mentioned once in NICE-ESF row; could anchor HL.HF (human factors) cluster more directly.
- **ISO/IEC 27001 / 27701** — *Information security / privacy management*. Already adjacent to DSPT; mapping could clarify which DSPT assertions are direct ISO 27001 controls vs. NHS-specific extensions.

**The unresolved questions.**

1. **Scope decision.** Does the taxonomy *map* ISO/BSI standards (treat them as 14th, 15th, … frameworks alongside DTAC/DSPT/etc.) or *cite* them (acknowledge them as parent / peer references that NHS frameworks build on, without taking on the maintenance cost of full mappings)? Mapping is heavy — each framework section in `_standards-mapping.md` is ~40–80 lines per framework, plus per-criterion taxonomy links. Citing is light — a single section in `_standards-mapping.md` titled "International standards lineage" listing the relevant ISOs/BSIs and which NHS frameworks operationalise them.
2. **AI-specific vs medical-device standards.** ISO/IEC 42001 and BS 30440 are explicitly AI-specific; ISO 14971 / IEC 62304 are general medical-device standards that AI happens to sit inside. The two cohorts have different mapping shapes — AI-specific standards have direct per-metric relevance; general medical-device standards anchor the SaMD lineage but don't generate metric-level rows. Worth deciding the cohorts separately.
3. **Paywall and access.** ISO and BSI standards are mostly paywalled (BSI subscription typical in NHS Trusts but not at GP level). The taxonomy's references catalogue convention assumes citations resolve to live URLs + Wayback snapshots; ISO/BSI references resolve to the BSI Knowledge / ISO Browse Platform pages, which require purchase to read. The catalogue can still cite them (handle + landing page), but we should be honest about the access cost in the prose.
4. **NHS-only adopting variant.** Some standards have UK variants (BS EN 62304 for IEC 62304; BS ISO/IEC 42001) — usually identical text under a UK number. Convention question: cite the UK variant (consistent with other NHS-context citations) or the international original (more durable across jurisdictions)?
5. **Maintenance cost vs reader value.** Adding 5–10 ISO/BSI mappings is a substantial maintenance commitment. Worth doing only if the reader value is clear — e.g. NHS procurement teams *are* asking about ISO/IEC 42001 conformance and the taxonomy could help them understand which AVT metrics constitute evidence.

**Starting points.**

- **Start with [AIDRS-NHS] (the AI and Digital Regulations Service hub, `digitalregulations.innovation.nhs.uk`).** AIDRS is NHS England's multi-regulator hub bringing together MHRA, NICE, ICO, CQC, and HRA guidance for digital-health AI; its explicit job is to surface where each regulatory frame applies and to point at the international standards each NHS framework rests on. It is the natural first stop for any ISO/BSI mapping exercise: AIDRS already does some of the lineage work (which NHS framework cites which ISO/BSI standard) and a pre-existing catalogue entry exists. Starting here means we don't redo work AIDRS has already done; we use AIDRS's surfacing as the spine for the mapping decisions below.
- Sketch a "ISO / BSI standards lineage" section in `_standards-mapping.md` that *cites* (not maps) the 8–9 candidates above, with one paragraph each explaining how the standard relates to existing NHS frameworks the taxonomy already maps. Lighter touch than full mapping; tests whether readers find this useful before committing to the heavier work.
- Specifically prototype **BS 30440** mapping (it's the closest peer to this taxonomy's purpose): how many of the taxonomy's metrics naturally serve as evidence for its requirements? If the answer is "most of them, with light annotation", BS 30440 deserves promotion to a full 14th-framework mapping. If the answer is "BS 30440 covers different ground", a citation-only treatment is the right shape.
- Cross-check existing NHS framework prose. DCB0129 explicitly references ISO 14971; MHRA SaMD references BS EN 62304 / IEC 82304-1. The lineage exists but the taxonomy doesn't surface it. A first cheap win is making the *existing* implicit references explicit.
- Decide whether ISO/IEC 42001 should be a 14th framework section or a sub-mapping under DTAC + MHRA + NHS T.E.S.T. (since it cuts across all three at the AI-management level rather than being a peer to any one of them).

**Promote to a release plan when:** (i) the scope decision is settled (map vs cite), AND (ii) BS 30440 has been read in full and confirmed in/out of scope. ISO/IEC 42001 + BS 30440 + ISO 14971 lineage surfacing are the minimum-viable shape; the rest can be incremental.

---

## 11. Standards-mapping tables — link metric ref-IDs back to per-metric pages

**Status:** queued.

**Context:** [`taxonomy/_standards-mapping.md`](taxonomy/_standards-mapping.md) cross-references metrics by ref-ID and metric name in the per-framework requirement tables (e.g. "GV.CR-6 Clinical Safety Case Completeness", "GV.SC-12 Cyber Essentials Plus"), but the ref-IDs render as plain text rather than as links to the metric definitions on the site. Readers scanning the tables to see what a framework maps to have to manually navigate to find the metric body — a friction the rest of the v3.9 citation grammar already removed elsewhere via handle-resolution and cross-page anchor rewriting.

This is a build-side mechanical fix in the same family as the v3.8.1 cross-page anchor rewriter and the v3.9 inline-handle resolution: take a known reference shape (`TP.AC-1` etc.) and emit an anchor link to the canonical metric page on the rendered site. The monolith and the per-page nav already use these anchors; the standards-mapping table just doesn't.

**Starting points:**
- The link target shape is already known: `parse.ref_id_to_anchor("TP.AC-1")` → `tp-ac-1`, with the per-metric page at `site/clusters/<cluster>/<group-file>.html#<anchor>`.
- `taxonomy/build_site.py` already has anchor-rewriting helpers (`rewrite_anchors`, `add_metric_anchors`, `link_tier1_quickref`). The standards-mapping pass is a parallel transformation on the same shape.
- Audit-side: an audit check verifying every ref-ID mentioned in `_standards-mapping.md` resolves to a real metric (analogous to the existing handle-resolution audit) would catch drift at build time.
- Edge cases: ref-IDs in prose (not just tables) — e.g. "Multiple metrics, see [TP.SN family](...)" — should also be linked. Ref-IDs that are intentionally retired or reserved should not be linked (cross-check `_retired-ids.md`).
- Reader experience: the AVT Registry table now carries a Tier column (per v4.1); the per-metric link addition would complete the table's usability — frame + tier + click-through-to-definition.

**Promote to a release plan when:** ready to execute. Mechanical scope, no design dependencies. Could fold into a future site-fixes patch (alongside any v4.x.y site work) or run as its own minor release.

---

## How to use this file

- **Adding items:** follow the format above. Lead with status, then *why*, then *starting points*. Don't write the implementation here — that goes in a release plan when the item is promoted.
- **Promoting to a release:** when an item is ready to execute, lift it into the relevant `plan-vX.Y.md` and either remove it from this file or mark its status as "in flight in vX.Y".
- **Removing items:** if an item turns out to be obsolete, redundant, or already done, delete it with a brief commit message explaining why. Keep this file focused on actual deferred work, not historical record (that's what `archive/` is for).
