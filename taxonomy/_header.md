# AVT Metrics Taxonomy

> **Draft - {{TAXONOMY_VERSION}}, {{TAXONOMY_DATE}}.** This taxonomy is under active review and has not yet been stakeholder-approved. Content, tier assignments, gap analysis, and cross-references may change before public release. It is shared openly so that early feedback can shape the content, but it should not yet be cited as a settled standard.

Comprehensive metrics for NHS ambient voice technology assurance - covering the full pipeline from audio capture to clinical record, with formal definitions, code snippets, responsible actors, tiered priority guidance, and novel proposals.

**218 metrics** across **20 groups**, organised in six parts. Includes 4 named metric families, 4 sub-clusters, and 15 metrics carrying explicit underspecification warnings that flag specific measurement-science gaps in the published literature. The taxonomy maps to **13 NHS / regulatory / procurement frameworks** in [Standards Mapping](#standards-mapping). Two cross-cutting principles govern application:

- The [**Outcomes Boundary**](#outcomes-boundary) (v3.3) names what is *out of scope* — clinical-outcome validation belongs to national research bodies, not deployers — and is operationalised by two ES.ME meta-metrics (ES.ME-8/-9) measuring vendor commitment to outcome evidence.
- The [**Calibration & Context principle**](#calibration-context) (v3.7) names what is *in scope but context-dependent* — tier assignments and threshold numbers are deployer-calibrated starting points against six named deployment-setting axes (specialty mix, patient population, platform maturity, governance capacity, risk appetite, volume), not universal gates.

Tier 1 metrics increasingly carry a structured Reference Standard / Operational Specification / Threshold Guidance pattern with ⚠️ Provenance preludes that distinguish cited thresholds from proposed-as-starting-points. As of v3.8, **32 of 42 Tier 1 constructs** carry this pattern (33 of 43 individual entries when sub-parts are counted separately). v3.7 introduced parent-with-sub-parts structure for redundancy resolution; v3.8 added the NHS England AVT Self-Certified Supplier Registry as the 13th mapped framework, three registry-driven metrics (Cyber Essentials Plus certification, evidence-pack freshness, indicative pricing transparency), and two new audit checks (Maturity-value enum; Source presence). See `taxonomy/audit.py` output for the live tightening-status manifest. The full release history is in [CHANGELOG.md](CHANGELOG.md).

