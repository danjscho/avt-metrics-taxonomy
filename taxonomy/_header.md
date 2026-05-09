# AVT Metrics Taxonomy

> **AI-coauthored prototype for discussion — {{TAXONOMY_VERSION}}, {{TAXONOMY_DATE}}.** Substantial portions of this taxonomy were drafted with AI assistance and human-reviewed; **specific claims, citations, and threshold numbers may still contain confabulations or factual errors** despite review. Keep this front of mind, verify before use, and please flag anything that looks wrong — feedback on errors is genuinely welcome. This is shared openly to provoke conversation, not as a settled standard, NHS-endorsed document, or procurement gate. Tier assignments, threshold numbers, and metric framings will change in response to feedback. See the [prototype status](#prototype-status) page for what you're invited to do, what you shouldn't do, and how the artefact evolves.

Comprehensive metrics for NHS ambient voice technology assurance - covering the full pipeline from audio capture to clinical record, with formal definitions, code snippets, responsible actors, tiered priority guidance, and novel proposals.

**236 metrics** across **20 groups**, organised in six clusters. Includes 4 named metric families, 4 sub-clusters, and 15 metrics carrying explicit underspecification warnings that flag specific measurement-science gaps in the published literature. The taxonomy maps to **13 NHS / regulatory / procurement frameworks** in [Standards Mapping](#standards-mapping). Two cross-cutting principles govern application:

- The [**Outcomes Boundary**](#outcomes-boundary) (v3.3) names what is *out of scope* — clinical-outcome validation belongs to national research bodies, not deployers — and is operationalised by two ES.ME meta-metrics (ES.ME-8/-9) measuring vendor commitment to outcome evidence.
- The [**Calibration & Context principle**](#calibration-context) (v3.7) names what is *in scope but context-dependent* — tier assignments and threshold numbers are deployer-calibrated starting points against six named deployment-setting axes (specialty mix, patient population, platform maturity, governance capacity, risk appetite, volume), not universal gates.

**Structural patterns active in the v5.x catalogue:**

- **Tier 1 tightening pattern** (v3.4+) — Tier 1 metrics carry a structured *Reference Standard* / *Operational Specification* / *Trigger Conditions* sub-block trio with ⚠️ Provenance preludes distinguishing cited thresholds from proposed-as-starting-points. Threshold numbers themselves live on the dedicated [Threshold Reference](thresholds.md) page since v5.0.0.
- **Citation grammar** (v3.9+) — every external authority resolves through a [References catalogue](#references) of ~110 handles with URLs, Wayback snapshots, and retrieval dates. Audit-enforced handle resolution.
- **Per-metric dimensions** (v5.4+) — `Family`, `Layer of Defence`, `AI-Substrate`, and `Applicability` are explicit per-metric fields surfaced in CSV/JSON. Cross-cutting `_*.md` pages (`_families.md`, `_layers-of-defence.md`, `_ai-substrate.md`) are derived views.
- **Honest-prototype framing** — opt-in `**Change history:**` stanzas on metrics with substantive fixes; ⚠️ underspecification warnings on 15 metrics where measurement science is unsettled; auto-built [Metric history](metric-history.md) page from git tag history.
- **Test + audit safety net** (v3.9.1+) — 99-test pytest suite plus a 15-check structural audit gate (CI fails on any error or warning).

**Recent release highlights** (full per-release notes in [CHANGELOG.md](CHANGELOG.md)):

- **v5.5.x** — Failure pathways, AI-substrate cross-cut, dimensions overview, explicit `Layer` extended to all 236 metrics, CC BY 4.0 catalogue licence, repo-wide documentation sweep.
- **v5.4.0** — `_families.md` consolidated home for 8 named metric families with audit-enforced `Family` dimension; `_layers-of-defence.md` and `_dimensions-overview.md` first-class pages; 2 new Tier 1 mints (GV.PD-18, GV.VT-11); within-cluster numerical-order audit check.
- **v5.3.0** — Phase 5 minimum-set extension against the FTS-direct surface: 7 T2→T1 promotions + 13 pull-throughs; counts 221 → 234; Tier 1 45 → 57.
- **v5.1.0** — Multi-valued `Measurement Cadence` with new `Event-triggered` enum value.
- **v5.0.0** — Structural split: thresholds move out of metric bodies into the [Threshold Reference](thresholds.md) page; *Threshold Guidance* renamed to *Trigger Conditions*.
- **v4.0.0** — Cluster-code naming throughout (TP / PI / HL / IO / GV / ES); EPR Write-back → Downstream Write-back.

