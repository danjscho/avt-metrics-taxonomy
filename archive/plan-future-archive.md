# Future work — completed items archive

Completed plan-future items that delivered substantive work. Preserved here as a historical record of how each item evolved from problem statement through to landed implementation. The active backlog is in [`plan-future.md`](plan-future.md).

Per-item original numbering preserved (so cross-references in old commits / CHANGELOG entries still resolve).

---

## 3. Versioning strategy across the project (metrics, tier selections, site, repo)

**Status:** complete (v4.5). Conventions written down at `taxonomy/_versioning.md` (renders as `versioning.md` on the site under About). Audit slice `check_version_bump_consistency` flags release over/under-bumps at INFO. Per-metric provenance handled by auto-built `metric-history.md` (git-derived, file-level) plus opt-in `**Change history:**` stanzas on metrics with substantive fixes (audit-checked via `check_change_history_versions`).

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
- Read the v3.8.x release sub-numbering convention in the [v3.8.1 / v3.8.2 / v3.8.3 / v3.8.4 CHANGELOG entries](CHANGELOG.md) — those four point releases are the clearest evidence that the current single-version scheme is being stretched.
- Look at how comparable taxonomies / standards bodies handle this. SNOMED CT has separate version lines for the international edition vs national extensions; HL7 FHIR has a release version + a profile version + an implementation guide version. ICD-11 has annual minor revisions distinct from major editions. Worth picking 2–3 reference models and seeing which fits the AVT taxonomy's downstream-use patterns.
- Look at the v3.7 deprecate-don't-renumber pattern (see the [v3.7 CHANGELOG entry](CHANGELOG.md) and the relevant TP.CC-7/8 → parent + sub-parts refactor) — that's the closest existing precedent for per-metric lineage.
- Lighter-weight alternatives to consider before committing to a full scheme: a "Last-tightened" date field in each Dimensions table; a Changes section per metric; a release-by-release diff table at the catalogue level; a "Tier set as-of" timestamp in `_tier-1-quick-reference.md`.
- Trade-off to think about: every additional version axis is overhead at every edit. The right answer might be no more than one or two extra axes, not five.

**Decision needed before implementation:** which scheme. This shouldn't be a Claude call — it's a project-direction decision. Surface as an explicit design question to the user when this item is promoted to a release.

---

---

## 4. Full Tier 1 gap review and minimum-set construction (post-agreement)

**Status: closed in v5.5.5.** Substantively actioned through the v5.0.1 → v5.5.0 Phase 5 work — the FTS notice 069369-2025 provided the external trigger for "what counts as minimum viable" (the AVT Self-Certified Supplier Registry surface), the v5.1.4 action list framed the criteria, and v5.3.0 / v5.4.0 actioned the gap-fill (7 promotions T2 → T1, 13 pull-throughs, 2 mints). The catalogue moved 218 metrics / 43 Tier 1 → 236 / 58.

**v5.5.5 closure work:**
- `_tier-1-quick-reference.md` refreshed with the 13 v5.3/v5.4 promoted/minted Tier 1 metrics and the 2 v4.1 promotions that had been missed (Decommissioning Data Handling, Retirement Notification Compliance). Per-actor headline counts corrected to reflect multi-actor responsibilities.
- Counts in this plan-future entry corrected from the v3.x-era 218/43 baseline to the current 236/58.
- Original "agreement criteria" question (every assurance question? every layer? every actor?) was settled implicitly by the FTS-derived approach: the Registry surface is the criteria, FTS Step 1.a–j defines the substantive obligations, the catalogue maps each substantive obligation to a Tier 1 metric.

**What's still open:** ongoing maintenance — when new Tier 1 obligations surface (regulatory updates, new NHSE guidance, new Registry requirements), the same gap-then-fill loop runs again rather than as a one-off review.

**Starting points** (now historical):
- The existing Tier 1 set is summarised in `taxonomy/_tier-1-quick-reference.md` (organised by responsible actor).
- Gaps file at [taxonomy/_gaps.md](taxonomy/_gaps.md) lists outstanding candidates organised by source standard.
- Promoted candidates are now lifted to `_gaps.md §7` historical record for clean separation.

---

---

## 5. Verify code snippets *and* Formal Definitions against sources

**Status:** complete. v4.2 covered TP / IO.FE / ES.ME (92 metrics); v4.3 covered GV / HL / PI / IO.PX (131 metrics); v4.4 ran Pass B externally over the 138-metric ✓ set (137/138 verified clean, 1 fix on GV.SG-5); v5.5.2 verified the 23 code snippets + the 15 v5.3/v5.4 Formal Definitions added since v4.4. Two-pass methodology (Pass A internal coherence + Pass B external source verification) plus per-snippet API check is the established pattern.

**v5.5.5 reconfirms closure.** No FD edits between v4.4 and v5.5.2 bypassed verification — the v4.5 / v5.0 / v5.1 / v5.2 commits did not modify Formal Definitions (they ran citation-grammar polish, threshold-block structural split, cadence-dimension cleanup, and research-output additions respectively). The verification arc is end-to-end across all 236 metrics.

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

---

## 7. Citation grammar review — should inline links carry a human-readable name?

**Status:** complete (v4.5). Build-time expansion: catalogue entries declare an optional `**Short:**` field; `build_site.rewrite_reference_handles()` uses that as the link label, falling back to the bare handle. Source-side `[Handle]` unchanged so audit and grep continue to work. Top 20 most-cited handles seeded with Short forms in v4.5; further entries can opt in incrementally.

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

---

## 8. Threshold-numbers review — remove or reword "proposed as starting points" thresholds

**Status:** complete (v5.0). The structural split landed: threshold numbers moved out of metric bodies into a dedicated [Threshold Reference](thresholds.md) page; the **Threshold Guidance** sub-block was renamed **Trigger Conditions** with qualitative-only content; per-metric pointers link to per-anchor sections; "starting points" framing is structurally repeated; the compound-errors caveat is made explicit. Phase 2a tightenings applied (TP.ASR-12 drift, TP.WB-2 IER provenance, GV.TC-1 minute-floors). Four cross-metric conventions named (severity-weighting, test-corpus floor, severity-band ladders, aggregate-rate-vs-zero-tolerance). The earlier text below is preserved for historical context.

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

## 10. AI-substrate classification — separate cut from Applicability

**Status:** complete (v5.5.3). Option 2 landed — five-class derived classification (`Pre-AI` / `AI-Substrate` / `Post-AI` / `AI-Mediated Workflow` / `AI-Agnostic Governance`) computed at build time from cluster + per-metric overrides. Surfaced as `ai_substrate` column in CSV/JSON, five `by-ai-substrate/` cross-cut pages on the site, and audit-enforced via `check_ai_substrate_resolves`. The earlier text below is preserved for historical context.


The existing **Applicability** dimension answers *"is this AVT-specific?"* (AVT-Specific / AVT-Contextualised / General Healthcare AI). It does NOT answer *"is this metric about the AI itself, the infrastructure around the AI, or the governance of the AI?"* — those are different cuts. A user asking "which metrics test the LLM?" can't currently get a clean answer.

**Why this matters.** Different audiences want different cuts:

- A vendor team building model-evaluation infrastructure wants the AI-substrate metrics (hallucination, calibration, WER) — they're the test surface.
- A deployer's IG officer wants the AI-agnostic governance metrics (DPIA completeness, board oversight, privacy notice currency) — they're the same regardless of vendor.
- A clinical safety officer wants the human-AI-workflow metrics (edit rate, automation bias, time-to-sign) — they're where AI shapes practice.
- A procurement officer wants the pre-AI infrastructure metrics (microphone validation, audio capture) — they're vendor-agnostic hardware concerns.

**Three approaches considered:**

1. **Add a new dimension `AI Substrate`** with values like `Pre-AI`, `AI-Substrate` (the model itself), `Post-AI` (write-back, EPR integration), `AI-Mediated Workflow` (clinician edits, automation bias), `AI-Agnostic Governance` (DPIA, board oversight). Honest but adds authoring cost to all 234 metric bodies.

2. **Derive from existing fields rather than add a new one.** Pipeline Layer already encodes most of this: TP.AC = pre-AI signal capture, TP.ASR/TP.SN/TP.CC = AI core, TP.WB = post-AI integration, HL.HF = human-AI workflow, IO/GV = mostly governance-of-AI. Add a derived classification at build time via cluster → AI-substrate-class lookup, with a small `disputed` category for honest edge cases (e.g. GV.PD-12 Training Data Representativeness sits between AI-substrate and AI-agnostic governance). Less precise but zero authoring cost on existing metrics.

3. **Documentation-only:** add an "AI relevance" framing in `_applicability.md` explaining that the cleanest answer is "look at Pipeline Layer" and walk through examples. Lowest cost, no structural change.

**Status update (v5.5.0):** Option 3 (documentation-only framing page) landed at `_ai-substrate.md`. The page names the five substrate classes, explains why this cut is documentation-only rather than per-metric structural, and walks through derivation rules + worked examples. Promotion to Option 2 (derived classification at build time) remains open; the page documents the criteria for that promotion.

**Default plan if this gets picked up:** Option 2 — derived classification at build time. Avoids editing 234 metric bodies. The classification is genuinely cluster-level for ~90% of metrics; the `disputed` category lets the catalogue be honest about edge cases.

**Open questions to settle before this lands:**

1. **Where does the classification surface?** A new column in CSV/JSON downloads? A new cross-cut page on the site (`docs/ai-substrate.md`)? Both? Audit dependency from `_applicability.md`?
2. **What happens to metrics that span classes?** GV.PD-12 (training data representativeness) is both AI-substrate (about the model) AND AI-agnostic governance (a documentation attestation). Force a single classification? Allow multi-valued like Cadence is now? Keep `disputed` as a real value rather than a fudge?
3. **Does this replace or supplement Applicability?** Best read: it's a different cut; both stay. AVT-Specific × AI-Substrate gives a 4-way intersection (e.g. "AVT-Specific AI-Substrate = ASR/diarisation/voice-summarisation models"; "General Healthcare AI AI-Agnostic Governance = the governance attestations").
4. **Does the taxonomy gain or lose by foregrounding this?** The Applicability dimension already gets occasional pushback for being a confusing cut; adding a second cross-cut may compound the noise rather than clarify. Worth piloting with a small group of readers before committing.

**Promote to a release plan when:** (i) Option 2 derivation has been prototyped against ~30 metrics to see how often `disputed` shows up, AND (ii) at least one reader who's not the author has reviewed the cut and confirmed it carries weight. If `disputed` covers >20% of metrics, the cut is too fuzzy to be useful and Option 3 (documentation-only) becomes the better answer.

---

---
