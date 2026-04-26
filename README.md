# AVT Metrics Taxonomy

A healthcare metrics taxonomy for assuring Ambient Voice Technology (AVT) systems from an NHS perpective.

**216 metrics across 20 groups**, covering the full AVT pipeline from audio capture to EPR write-back, plus governance, human factors, equity, and meta-evaluation. **Draft v3.6, 2026-04-26** — under active review, not yet stakeholder-approved.

> ⚠️ This is a draft. Content, tier assignments, gap analysis, and cross-references may change before public release. It is shared openly so early feedback can shape the content. Do not yet cite as a settled standard.

## Quick links

- **Published site:** <https://danjscho.github.io/avt-metrics-taxonomy/> — readable navigation, search, per-standard cross-cut pages
- **Monolithic markdown:** [avt-metrics-taxonomy.md](avt-metrics-taxonomy.md) — single-file assembled output
- **Structured data:** [`dist/metrics.csv`](dist/metrics.csv) (flat 216-row export), [`dist/metrics.json`](dist/metrics.json) (full structured catalogue), [`dist/gaps.json`](dist/gaps.json) (89 roadmap candidates)
- **Release history:** [CHANGELOG.md](CHANGELOG.md)
- **What's in scope vs out of scope:** [Outcomes Boundary](taxonomy/_outcomes-boundary.md) — this taxonomy assures deployment safety; clinical-outcome validation is national-research-body work

## What this is for

The taxonomy organises measurable indicators that NHS deployers, vendors, and assurance teams can use to evaluate AVT systems. Metrics are tiered:

- **🟢 Tier 1 (43 metrics) — Minimum Viable Assurance.** What every deployer must measure to operate safely.
- **🟡 Tier 2 (94 metrics) — Recommended Assurance.** Add with reasonable governance capacity.
- **🔵 Tier 3 (79 metrics) — Advanced / Research.** Requires infrastructure that often doesn't yet exist.

As of v3.6, **25 of 43 Tier 1 metrics** carry a structured **Reference Standard / Operational Specification / Threshold Guidance** sub-block pattern with explicit ⚠️ Provenance preludes that distinguish cited thresholds from proposed-as-starting-points.

## Per-audience entry points

### Procurement officer / Clinical Safety Officer

Start with the **Tier 1 Quick Reference** in the rendered site or [taxonomy/_tier-1-quick-reference.md](taxonomy/_tier-1-quick-reference.md). The 43 Tier 1 metrics are organised by responsible actor (Vendor, Deployer, Regional, National Body).

For the 25 tightened metrics, the **Operational Specification** sub-block tells you what your vendor must comply with at procurement; the **Threshold Guidance** sub-block tells you what triggers escalation post-deployment. Read the ⚠️ Provenance line in each Threshold Guidance block — it distinguishes thresholds derived from cited sources (e.g. NAS Day Zero SPI, UK GDPR, NHSE IG guidance March 2026) from numbers proposed in this taxonomy as starting points that require local calibration.

For NHS T.E.S.T. assurance, see the [NHS T.E.S.T. Framework section in standards-mapping](taxonomy/_standards-mapping.md) — the framework's 22 Section A platform-assurance requirements and 12 Section B benefit domains are mapped to specific metrics in this taxonomy.

### Vendor

The standards-mapping section ([taxonomy/_standards-mapping.md](taxonomy/_standards-mapping.md)) maps every metric against twelve NHS / regulatory frameworks: DTAC, DSPT, DCB0129/0160, NHS England LLM Evaluation Framework, NHS T.E.S.T., MHRA SaMD/AIaMD, NICE ESF, FHIR UK Core, CQC, PSIRF, PRSB, Caldicott. Use it to identify which metrics satisfy which compliance obligation.

The [Outcomes Boundary](taxonomy/_outcomes-boundary.md) is worth reading first — it sets the explicit limit of what this taxonomy assures (deployment safety) versus what national research bodies must validate (clinical outcomes). Vendors making outcome claims should also see [ES.ME-8 Outcome Evidence Commitment Status](taxonomy/part-f/meta-evaluation.md) and [ES.ME-9 Causal Model Operationalisation](taxonomy/part-f/meta-evaluation.md), which operationalise vendor-side commitment to outcome evaluation.

### Developer / contributor

[taxonomy/README.md](taxonomy/README.md) covers the build pipeline:

```
python3 taxonomy/build.py    # Assembles avt-metrics-taxonomy.md + dist/ outputs
python3 taxonomy/audit.py    # Structural + Tier 1 tightening + cross-reference audits
```

`audit.py` is the source of truth for current tightening status — it emits a manifest after the tier counts showing which Tier 1 metrics carry the tightening pattern and which are still pending. Future work scope is derived from this output rather than from CHANGELOG prose.

[`taxonomy/parse.py`](taxonomy/parse.py) extracts every metric from its dimension table; [`taxonomy/build_site.py`](taxonomy/build_site.py) renders the MkDocs site; [`taxonomy/_gaps.md`](taxonomy/_gaps.md) is the consolidated roadmap of 89 proposed candidates across five origins (RSET external review, NHSE IG, standards mapping, NHS T.E.S.T., Responsible AI Lens).

The [`archive/`](archive/) directory holds prior plans and research artefacts: the v3.4 [Tier 1 LOOSE/TIGHT/SURROGATE classification](archive/v3.3-tier1-classification.md), the v3.6 [duplication review](archive/v3.6-duplication-review.md), and per-release plans (`plan-v2`, `plan-v3.1`, etc.).

### Researcher

Three cross-cutting documents frame the policy and ethics surface:

- [taxonomy/_responsible-ai-lens.md](taxonomy/_responsible-ai-lens.md) — DSIT AI Playbook (Feb 2025) ten principles and the six Responsible AI ethical themes (Safety/Security/Robustness; Transparency/Explainability; Fairness; Accountability/Governance; Contestability/Redress; Societal Wellbeing). Covers 38 cross-cutting policy gaps.
- [taxonomy/_outcomes-boundary.md](taxonomy/_outcomes-boundary.md) — explicit out-of-scope statement (this taxonomy does not assure clinical outcomes; that work belongs elsewhere) plus pointers to [ES.ME-1](taxonomy/part-f/meta-evaluation.md), [ES.ME-8](taxonomy/part-f/meta-evaluation.md), [ES.ME-9](taxonomy/part-f/meta-evaluation.md) for the proximal/distal causal-logic framework.
- [taxonomy/_gaps.md](taxonomy/_gaps.md) — 89 proposed metric candidates with classification (proposed / accepted / deferred / rejected). Single source of truth across five origins.

## Status / version

**Current draft:** v3.6, released 2026-04-26.

Tag history: `v1.0` → `v2.0` → `v3.1` → `v3.2` (modular restructure + MkDocs site + 12-framework standards mapping) → `v3.3` (Outcomes Boundary + ES.ME-8/9 + first 9 Tier 1 tightenings) → `v3.4` (audit-side enforcement + Phase 3 + classification artefact) → `v3.5` (Wave 1 compliance/governance + Wave 2 privacy-chain tightenings) → **v3.6** (applicability-on-metric alignment + duplication review + v3.5 follow-ups + this README).

See [CHANGELOG.md](CHANGELOG.md) for full release notes.

## Citation

Until the draft reaches a settled state, please cite as:

> Schofield, D. (2026). *AVT Metrics Taxonomy v3.6* [draft]. Retrieved from https://danjscho.github.io/avt-metrics-taxonomy/

Note: draft status means content / tier assignments / cross-references may change. Cite the specific version (e.g. v3.6) so subsequent users can reproduce what you read.

## Contributing

The current contribution path is **GitHub issues** for proposed gaps, corrections, or framework alignments: <https://github.com/danjscho/avt-metrics-taxonomy/issues>.

Substantive proposals (new metrics, sub-cluster framings, cross-references) are tracked through [`taxonomy/_gaps.md`](taxonomy/_gaps.md). The roadmap convention is: `proposed` → reviewed → `accepted` (drafted) or `deferred` (with reasoning preserved) or `rejected` (with reasoning preserved).

A formal CONTRIBUTING file does not yet exist. Issues are the right entry point until one does.

## Licence

Licence TBD. Until a licence is declared in this repository, treat the taxonomy as **draft work shared for early feedback**, not as a settled standard or a freely re-licensable artefact.

---

*Last updated: v3.6 / 2026-04-26.*
