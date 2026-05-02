# AVT Metrics Taxonomy

A healthcare metrics taxonomy for assuring Ambient Voice Technology (AVT) systems from an NHS perpective.

**218 metrics across 20 groups**, covering the full AVT pipeline from audio capture to downstream write-back, plus governance, human factors, equity, and meta-evaluation. **AI-coauthored prototype for discussion — v4.0.1, 2026-05-02.** Shared to provoke conversation; not a settled standard.

> ⚠️ This is an **AI-coauthored prototype for discussion**, not a finished taxonomy. Substantial portions were drafted with AI assistance and human-reviewed; **specific claims, citations, and threshold numbers may still contain confabulations or factual errors** despite review. Keep this front of mind, verify before use, and please flag anything that looks wrong — feedback on errors is genuinely welcome. It is shared openly to provoke conversation about what an AVT assurance frame should look like — *not* as an NHS-endorsed standard, regulatory document, or procurement gate. Tier assignments, threshold numbers, and metric framings will change in response to feedback. **You are invited to disagree, propose changes, point at gaps, flag errors, and share with colleagues. You should not paste threshold numbers into contracts, cite metrics as authoritative without flagging the prototype status, or treat any specific metric as policy.** See [docs site → Prototype status](https://danjscho.github.io/avt-metrics-taxonomy/prototype-status/) for the full framing.

## Quick links

- **Published site:** <https://danjscho.github.io/avt-metrics-taxonomy/> — readable navigation, search, per-standard cross-cut pages
- **Monolithic markdown:** [avt-metrics-taxonomy.md](avt-metrics-taxonomy.md) — single-file assembled output
- **Structured data:** [`dist/metrics.csv`](dist/metrics.csv) (flat 218-row export), [`dist/metrics.json`](dist/metrics.json) (full structured catalogue), [`dist/gaps.json`](dist/gaps.json) (89 roadmap candidates)
- **Release history:** [CHANGELOG.md](CHANGELOG.md)
- **What's in scope vs out of scope:** [Outcomes Boundary](taxonomy/_outcomes-boundary.md) — this taxonomy assures deployment safety; clinical-outcome validation is national-research-body work
- **How to apply the metrics to your deployment:** [Calibration & Context principle](taxonomy/_calibration-and-context.md) — tier assignments and threshold numbers are calibration starting points; six deployment-setting axes (specialty mix, patient population, platform maturity, governance capacity, risk appetite, volume) drive local calibration

## What this is for

The taxonomy organises measurable indicators that NHS deployers, vendors, and assurance teams can use to evaluate AVT systems. Metrics are tiered:

- **🟢 Tier 1 (43 metrics) — Minimum Viable Assurance.** What every deployer must measure to operate safely.
- **🟡 Tier 2 (96 metrics) — Recommended Assurance.** Add with reasonable governance capacity.
- **🔵 Tier 3 (79 metrics) — Advanced / Research.** Requires infrastructure that often doesn't yet exist.

As of v3.8, **32 of 42 Tier 1 constructs** (33 of 43 individual entries when sub-parts are counted separately) carry a structured **Reference Standard / Operational Specification / Threshold Guidance** sub-block pattern with explicit ⚠️ Provenance preludes that distinguish cited thresholds from proposed-as-starting-points.

The taxonomy commits to two parallel principles that govern how it should be applied: the [Outcomes Boundary](taxonomy/_outcomes-boundary.md) names what's *out of scope* (clinical-outcome validation belongs elsewhere); the [Calibration & Context principle](taxonomy/_calibration-and-context.md) names what's *in scope but context-dependent* (tier assignments and threshold numbers are deployer-calibrated starting points). Read both before applying any metric in procurement or operational governance.

## Per-audience entry points

### Procurement officer / Clinical Safety Officer

Start with the **Tier 1 Quick Reference** in the rendered site or [taxonomy/_tier-1-quick-reference.md](taxonomy/_tier-1-quick-reference.md). The 43 Tier 1 metrics are organised by responsible actor (Vendor, Deployer, Regional, National Body). **The Tier 1 list is a calibrated starting point, not a fixed checklist** — your specialty mix, patient population, platform maturity, governance capacity, risk appetite, and volume all shift which metrics belong in your Tier 1 set; see the [Calibration & Context principle](taxonomy/_calibration-and-context.md) for the structural commitment and the documentation expectation.

For the 25 tightened metrics, the **Operational Specification** sub-block tells you what your vendor must comply with at procurement; the **Threshold Guidance** sub-block tells you what triggers escalation post-deployment. Read the ⚠️ Provenance line in each Threshold Guidance block — it distinguishes thresholds derived from cited sources (e.g. NAS Day Zero SPI, UK GDPR, NHSE IG guidance March 2026) from numbers proposed in this taxonomy as starting points that require local calibration before contractual use.

For NHS T.E.S.T. assurance, see the [NHS T.E.S.T. Framework section in standards-mapping](taxonomy/_standards-mapping.md) — the framework's 22 Section A platform-assurance requirements and 12 Section B benefit domains are mapped to specific metrics in this taxonomy.

### Vendor

The standards-mapping section ([taxonomy/_standards-mapping.md](taxonomy/_standards-mapping.md)) maps every metric against twelve NHS / regulatory frameworks: DTAC, DSPT, DCB0129/0160, NHS England LLM Evaluation Framework, NHS T.E.S.T., MHRA SaMD/AIaMD, NICE ESF, FHIR UK Core, CQC, PSIRF, PRSB, Caldicott. Use it to identify which metrics satisfy which compliance obligation.

The [Outcomes Boundary](taxonomy/_outcomes-boundary.md) is worth reading first — it sets the explicit limit of what this taxonomy assures (deployment safety) versus what national research bodies must validate (clinical outcomes). Vendors making outcome claims should also see [ES.ME-8 Outcome Evidence Commitment Status](taxonomy/part-f/meta-evaluation.md) and [ES.ME-9 Causal Model Operationalisation](taxonomy/part-f/meta-evaluation.md), which operationalise vendor-side commitment to outcome evaluation.

When pricing or scoping AVT contracts against this taxonomy, note that the [Calibration & Context principle](taxonomy/_calibration-and-context.md) means the contractual gate is the *deployer's local calibration*, not the taxonomy's published starting-point thresholds. Vendors should expect deployer calibration documents that name the local tier assignments and threshold values; once a deployer has calibrated, the calibrated number is the contract.

### Developer / contributor

[taxonomy/README.md](taxonomy/README.md) covers the full local-build recipe (uv-based) and the file layout. Quick version:

```
uv sync --extra dev                    # one-off: install deps + pytest from uv.lock
uv run python taxonomy/build.py        # → avt-metrics-taxonomy.md + dist/* CSV/JSON
uv run python taxonomy/build_site.py   # → populates docs/ and mirrors dist/* into docs/downloads/
uv run mkdocs serve                    # → http://127.0.0.1:8000/avt-metrics-taxonomy/
uv run python taxonomy/audit.py        # → structural + Tier 1 tightening + cross-reference audits
uv run pytest                          # → 88 unit tests (parse / build / build_site / audit / snapshot)
```

The project uses [uv](https://docs.astral.sh/uv/) for environment management; `uv.lock` is committed so local and CI builds match. `audit.py` is the source of truth for current tightening status — it emits a manifest after the tier counts showing which Tier 1 metrics carry the tightening pattern and which are still pending. Future work scope is derived from this output rather than from CHANGELOG prose.

[`taxonomy/parse.py`](taxonomy/parse.py) extracts every metric from its dimension table; [`taxonomy/build_site.py`](taxonomy/build_site.py) renders the MkDocs site; [`taxonomy/_gaps.md`](taxonomy/_gaps.md) is the consolidated roadmap of 89 proposed candidates across five origins (RSET external review, NHSE IG, standards mapping, NHS T.E.S.T., Responsible AI Lens).

The [`archive/`](archive/) directory holds prior plans and research artefacts: the v3.4 [Tier 1 LOOSE/TIGHT/SURROGATE classification](archive/v3.3-tier1-classification.md), the v3.6 [duplication review](archive/v3.6-duplication-review.md), and per-release plans (`plan-v2`, `plan-v3.1`, etc.).

### Researcher

Four cross-cutting documents frame the policy, ethics, and application surface:

- [taxonomy/_responsible-ai-lens.md](taxonomy/_responsible-ai-lens.md) — DSIT AI Playbook (Feb 2025) ten principles and the six Responsible AI ethical themes (Safety/Security/Robustness; Transparency/Explainability; Fairness; Accountability/Governance; Contestability/Redress; Societal Wellbeing). Covers 38 cross-cutting policy gaps.
- [taxonomy/_outcomes-boundary.md](taxonomy/_outcomes-boundary.md) — explicit out-of-scope statement (this taxonomy does not assure clinical outcomes; that work belongs elsewhere) plus pointers to [ES.ME-1](taxonomy/part-f/meta-evaluation.md), [ES.ME-8](taxonomy/part-f/meta-evaluation.md), [ES.ME-9](taxonomy/part-f/meta-evaluation.md) for the proximal/distal causal-logic framework.
- [taxonomy/_calibration-and-context.md](taxonomy/_calibration-and-context.md) — parallel principle to the Outcomes Boundary: tier assignments and threshold numbers are calibration starting points, not universal gates. Six deployment-setting axes drive local calibration. Research-side relevance: studies citing the taxonomy should specify both the version and the calibration applied to the deployment under study.
- [taxonomy/_gaps.md](taxonomy/_gaps.md) — 89 proposed metric candidates with classification (proposed / accepted / deferred / rejected). Single source of truth across five origins.

## Citation grammar (v3.9 onwards)

External citations in metric files use a two-layer grammar settled at v3.9:

1. **Inline reference** in metric prose — a short stable handle in square brackets, e.g. `[DCB0129]`, `[NHSE-IG-Guidance-2026-03]`, `[UK-GDPR]`, `[Keyes-Stanford-Monitoring-2025]`.
2. **Catalogue entry** in [taxonomy/_references.md](taxonomy/_references.md) — full bibliographic record per handle (Title / Publisher / Source-Type / URL / Archive / Retrieved date / `Local-Mirror` field reserved for a future v3.x option-(c) local-mirror release).

Source rows in metric Dimensions tables, Reference Standard / Threshold Guidance prose blocks, and the `_standards-mapping.md` framework sections all follow this convention. The grammar separates *what* is cited from *where* the bibliographic detail lives, so a citation update touches one catalogue entry rather than every metric that references it. The `Local-Mirror` field is present-but-empty in v3.9; when a future release brings authoritative documents into the repo as local mirrors, the catalogue grows the field, but no metric file needs to change.

`audit.py` enforces handle resolution: every `[Handle]` in a metric file must exist in `_references.md`, or the audit fails.

## Status / version

**Current prototype version:** v4.0.1, released 2026-05-02.

Tag history: `v1.0` → `v2.0` → `v3.1` → `v3.2` (modular restructure + MkDocs site + 12-framework standards mapping) → `v3.3` (Outcomes Boundary + ES.ME-8/9 + first 9 Tier 1 tightenings) → `v3.4` (audit-side enforcement + Phase 3 + classification artefact) → `v3.5` (Wave 1 compliance/governance + Wave 2 privacy-chain tightenings) → `v3.6` (applicability-on-metric alignment + duplication review + v3.5 follow-ups + this README) → `v3.7` (Calibration & Context principle + 6 pipeline narrow tightenings + 3 redundancy pairs as parent-with-sub-parts + US-flavour reframe of TP.CC family) → `v3.8` (NHSE AVT Self-Certified Supplier Registry as 13th mapped framework + 3 registry-driven metrics + Maturity-value and Source-presence audit checks + HL.HF-3a tightening) → `v3.9` (citation grammar + References catalogue: ~100 entries, every external authority resolves through `_references.md` with handles + URLs + Wayback snapshots + retrieval dates; audit-enforced handle resolution; cited-by back-references at build time) → `v3.9.1` (88-test pytest suite under `taxonomy/tests/` covering parse / build / build_site / audit / tools/snapshot; CI runs on every push) → `v4.0.0` (cluster-code naming throughout: folders renamed `part-a/` → `tp/`, `part-b/` → `pi/`, etc.; Pipeline Layer "EPR Write-back" → "Downstream Write-back"; CSV/JSON breaking change `part`/`part_name` → `cluster`/`cluster_name`; mkdocs-redirects added so old URLs still resolve) → **v4.0.1** (drop the v4.0 backwards-compat `Metric.part` / `Metric.part_name` aliases; one in-repo reader fixed; clean break for v4.x consumers).

See [CHANGELOG.md](CHANGELOG.md) for full release notes.

## Citation

Until the prototype reaches a settled state, please cite as:

> Schofield, D. (2026). *AVT Metrics Taxonomy v4.0.1* [prototype-for-discussion]. Retrieved from https://danjscho.github.io/avt-metrics-taxonomy/

Note: prototype status means content / tier assignments / cross-references may change in response to feedback. Cite the specific version (e.g. v3.9) so subsequent readers can reproduce what you read, and please flag the prototype status when citing in academic work — pasting numbers into contracts or treating any specific metric as policy is out of scope until the artefact is settled.

## Contributing

The current contribution path is **GitHub issues** for proposed gaps, corrections, or framework alignments: <https://github.com/danjscho/avt-metrics-taxonomy/issues>.

Substantive proposals (new metrics, sub-cluster framings, cross-references) are tracked through [`taxonomy/_gaps.md`](taxonomy/_gaps.md). The roadmap convention is: `proposed` → reviewed → `accepted` (drafted) or `deferred` (with reasoning preserved) or `rejected` (with reasoning preserved).

A formal CONTRIBUTING file does not yet exist. Issues are the right entry point until one does.

## Licence

Licence TBD. Until a licence is declared in this repository, treat the taxonomy as **prototype work shared for discussion**, not as a settled standard or a freely re-licensable artefact.

---

*Last updated: v4.0.1 / 2026-05-02.*
