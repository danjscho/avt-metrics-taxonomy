# Future work — taxonomy backlog

A running list of cross-release improvements that don't fit the current release plan. Items here are deferred work, not blocked work — promote to a release plan when ready to execute.

Format per item: short title, status, context (the *why*), and starting points (where to look in the codebase / what to consider first).

Items that landed in earlier releases are preserved in [`archive/plan-future-archive.md`](archive/plan-future-archive.md) as a historical record (items 3, 4, 5, 7, 8 — versioning conventions, Tier 1 minimum-set construction, snippet/FD verification, citation grammar, threshold-numbers review). Per-item original numbering is preserved across both files so cross-references in CHANGELOG / commits continue to resolve.

---

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

---

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

---

---

## 11. Reference implementation library — extract code snippets as a runnable package

**Status:** open question, candidate for v5.5+ or later. Surfaced 2026-05-08 during v5.4.0 work.

Roughly a dozen metrics in the catalogue carry **code snippets** in their bodies — currently embedded as illustrative pseudocode or runnable-but-not-actually-run blocks (the `pyannote` DER snippet at TP.DI-1, scikit-learn calibration code at the calibration metrics, the stigmatising-language detection lexicon at TP.SN-24, the medication-attribute extraction sketch at TP.SN-19, etc.). Plan-future #5 already surfaced that these snippets need verification against cited sources.

The next step beyond verification is **extraction into a runnable companion library**:

- **What it would be.** A `pip install avt-metrics` (or similar) Python package providing reference implementations of every metric whose definition reduces to a computational operation. Each metric becomes a function with the same name as the metric (e.g. `avt_metrics.tp.asr.wer(reference, hypothesis)`, `avt_metrics.tp.di.der(reference_diar, hypothesis_diar)`). The catalogue body's code snippet is replaced by `from avt_metrics import ...` and the canonical implementation lives in the package.

- **What it would buy.**
  - **Consistency** — two deployers measuring "Hallucination Rate" today might apply different operationalisations of TP.SN-5; a reference implementation makes the operationalisation auditable.
  - **Runnability** — readers can actually compute the metric on their own data without re-implementing from prose definitions.
  - **Versioning** — the package version tracks alongside the taxonomy version, so "I measured this against avt-metrics v5.4.0" is a citable claim. The CHANGELOG already names per-metric Change history; the library would mirror that.
  - **Test coverage** — every metric function gets unit tests, which surfaces operationalisation ambiguities the prose can paper over.
  - **Community contribution path** — vendors and deployers who disagree with a reference implementation can PR an alternative, with the discussion happening at function-level rather than at prose-level.

- **What it would cost.**
  - **Maintenance burden** — every catalogue change that touches an operationalisable metric needs a code change too. The package and the catalogue have to stay in sync; drift becomes a real risk.
  - **Scope creep** — once a reference implementation exists, readers will ask for plotting helpers, dataset loaders, evaluation harnesses, NHS-context-specific connectors. Easy to balloon.
  - **Authoritative-but-prototype tension** — the library would be code that *runs* on real data; the taxonomy is explicitly a *prototype for discussion*. The library would need its own prototype-status framing or it would silently elevate the taxonomy's authority.
  - **Not all metrics fit** — process-attestation metrics (DPIA completion, board oversight, PCCP documentation) have no computational kernel. The library would only cover the ~30-40% of metrics that reduce to a function; the prose taxonomy stays canonical for the rest.

- **Suggested incremental path.**
  1. **v5.5+ scoping pass** — enumerate which metrics have computational kernels worth packaging. Plan-future #5's Formal Definition + code snippet verification work has to land first; the library can't extract from snippets that haven't been verified.
  2. **Single-cluster pilot** — extract TP.ASR (WER, M-WER, CK-ER, demographic-disaggregated WER, calibration) as a sub-package. ASR metrics have well-established external implementations (NIST SCTK, jiwer), so wrapping is mostly composition rather than re-implementation. Roughly 8-10 metric functions.
  3. **CI integration** — add a workflow that runs the library's test suite on every catalogue change to that cluster's metrics; if tests fail, the catalogue prose has drifted from the operationalisation and one or the other needs fixing.
  4. **Decision point** — after the TP.ASR pilot, evaluate whether the maintenance cost is worth it. If yes, expand cluster-by-cluster. If no, document the conclusion and keep code in metric bodies as illustrative.

- **Open questions to settle before this lands.**
  1. **Package name and ownership** — is this `avt-metrics`, `nhs-avt-metrics`, something else? Who maintains it? The catalogue is already AI-coauthored prototype; the library would inherit that framing or claim a different one.
  2. **Licensing** — the catalogue is a documentation artefact; the library is software. License compatibility matters (MIT / Apache 2.0 are common; the catalogue itself doesn't yet declare a license).
  3. **Versioning** — does the library track the taxonomy version exactly, or have its own SemVer? Tracking exactly is simpler but couples release cadences; independent SemVer is more flexible but harder to cross-reference.
  4. **Out-of-scope shape** — the package should explicitly say what it does NOT do (no clinical-decision support, no ground-truth datasets, no pre-trained models). The Outcomes Boundary principle from the taxonomy gives a natural framing.

**Promote to a release plan when:** (i) Plan-future #5 (Formal Definition + code snippet verification) has landed for the candidate pilot cluster, AND (ii) at least one external reader has expressed interest in using the library on real data (a deployer, a vendor's evaluation team, or a researcher). Without external pull, the maintenance cost outruns the reader value.

---

---

---

## 12. Outstanding follow-ups from v5.3 pre-mint triage

**Status:** carried forward from `archive/v5.4/v5.3-pre-mint-triage.md`. Not blockers; tracked for future minor releases.

- **Gap-IG-A rubric piloting** — the metric currently uses the placeholder "structured per local IG officer review" with Maturity: Proposed/Novel. Once a piloted rubric exists, Maturity can move Proposed/Novel → Emerging.
- **GV.VT-10 Option-2 source verification** — the MHRA Roadmap WP-2 transparency outputs need to be cited in the metric's References block once WP-2 outputs are publicly available. Currently held as Proposed/Novel pending citation.

Both items are low-cost to action when the upstream artefacts (piloted rubric / published WP-2 output) become available; neither needs proactive chasing.

---

---

---

## How to use this file

- **Adding items:** follow the format above. Lead with status, then *why*, then *starting points*. Don't write the implementation here — that goes in a release plan when the item is promoted.
- **Promoting to a release:** when an item is ready to execute, lift it into the relevant `plan-vX.Y.md` and either remove it from this file or mark its status as "in flight in vX.Y".
- **Removing items:** if an item turns out to be obsolete, redundant, or already done, delete it with a brief commit message explaining why. Keep this file focused on actual deferred work, not historical record (that's what `archive/` is for).
