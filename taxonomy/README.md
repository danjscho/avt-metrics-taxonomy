# Prototype AVT Metrics Taxonomy — Repository Guide

This is the contributor / developer guide. For the reader-facing description of what the taxonomy *is*, see [`../README.md`](../README.md). For session-level guidance to Claude Code working in this repo, see [`../CLAUDE.md`](../CLAUDE.md).

## Local development — build and serve the site

A fresh clone needs three steps to reproduce what `https://danjscho.github.io/avt-metrics-taxonomy/` shows. The project uses [uv](https://docs.astral.sh/uv/) for Python environment management; install it via `curl -LsSf https://astral.sh/uv/install.sh | sh` (or `brew install uv`) if you don't already have it. All commands run from the repo root.

### 1. Install dependencies

```
uv sync --extra dev
```

`uv sync` reads `pyproject.toml` + `uv.lock` and creates a `.venv/` with the exact package set CI uses (`mkdocs-material`, `mike`, `mkdocs-rss-plugin`, `mkdocs-redirects`, plus `pytest` from the dev extras). The lockfile is committed so local builds match CI bit-for-bit. uv also handles the Python toolchain — no separate `pyenv` / `python -m venv` step needed.

### 2. Build the artefacts

```
uv run python taxonomy/build.py        # → avt-metrics-taxonomy.md + dist/{metrics.csv,metrics.json,gaps.json,summary.json}
uv run python taxonomy/build_site.py   # → populates docs/, mirrors dist/* into docs/downloads/, generates 45 crosscut pages
```

Order matters: `build_site.py` reads `dist/` to populate the Downloads page, so `build.py` must run first. Both scripts are idempotent; rerun freely.

### 3. Serve locally

```
uv run mkdocs serve
```

Serves on `http://127.0.0.1:8000/avt-metrics-taxonomy/` (the path prefix comes from `site_url` in `mkdocs.yml`). Live-reloads when files change in `docs/`, but **does not re-run `build_site.py`** — if you edit `taxonomy/*.md` source files you need to re-run `uv run python taxonomy/build_site.py` to repopulate `docs/` and trigger reload.

For a one-off static build into `site/` (what gets published) use `uv run mkdocs build` (or `uv run mkdocs build --strict` to catch broken links — strict mode aborts on missing nav targets, missing link destinations, and similar).

### Where `dist/` files come from

The downloadable CSV / JSON / monolithic-Markdown artefacts on the published site are produced by `python taxonomy/build.py`:

- `dist/metrics.csv` — flat **236-row** spreadsheet (21 columns: ref_id, name, tier, tier_label, cluster, cluster_name, group, applicability, family, layer, ai_substrate, cadence, pipeline_layer, assurance_question, measurement_method, lifecycle_phases, responsible_actors, maturity, source, group_file, heading_line)
- `dist/metrics.json` — same metrics with full structured dimension data preserved per entry
- `dist/gaps.json` — 74 outstanding roadmap candidates partitioned by origin (RSET / NHSE IG / standards-mapping / NHS T.E.S.T. / RAI lens). The 17 promoted-historical-record rows in `_gaps.md §7` are excluded from `gap_count`.
- `dist/summary.json` — headline counts (metric / tier / group / gap) plus `version` and `status`
- `avt-metrics-taxonomy.md` (repo root) — monolithic concatenated Markdown

`taxonomy/build_site.py`'s `_mirror_downloads()` then copies these into `docs/downloads/` so `mkdocs serve` can serve them locally; CI does the equivalent copy via the workflow file.

### Audit + tests

```
uv run python taxonomy/audit.py        # → 15 structural / count / enum / ordering checks
uv run pytest                          # → 99 unit tests covering parse / build / build_site / audit / snapshot
```

`audit.py` is the source of truth for current structural correctness — checks include tier totals, applicability totals, maturity values enum, cadence values enum, family resolution, layer enum, within-cluster numerical ordering, summary maturity drift, README headline counts, retired-IDs-not-reused, source presence, see-also resolution, ref-ID handle resolution, threshold-page anchor resolution, and version bump consistency. The CI workflow runs audit + pytest first and fails the build on any finding. Run both before pushing if you've touched metric files.

## File structure

```
taxonomy/
  _header.md                    # Title, metric count, prototype-status framing
  _prototype-status.md          # Detailed prototype framing
  _how-to-use.md                # Priority tiers, cadence, actors, deployment guidance
  _summary.md                   # By tier, maturity, family, underspecification warning
  _tier-1-quick-reference.md    # All Tier 1 metrics organised by responsible actor
  _contents.md                  # Table of contents
  _applicability.md             # Per-metric applicability matrix (legacy; per-metric Family
                                #   / Applicability fields are now the source of truth)
  _families.md                  # Eight named metric families (canonical home; v5.4.0+)
  _layers-of-defence.md         # Prevention/Detection/Limitation principle (v5.4.0+)
  _failure-pathways.md          # Three archetypes + worked timeline (v5.5.1)
  _ai-substrate.md              # Five-class derived cut (v5.5.0; v5.5.3 build-time derived)
  _dimensions-overview.md       # Reader-orientation page for the 13 per-metric dimensions
  _outcomes-boundary.md         # Out-of-scope statement (v3.3 first-class principle)
  _calibration-and-context.md   # Calibration principle (v3.7 first-class principle)
  _standards-mapping.md         # 13-framework mapping
  _responsible-ai-lens.md       # DSIT Playbook + ethical themes
  _gaps.md                      # 74 outstanding + §7 promoted historical record
  _references.md                # Catalogue handles (~110 entries); audit-enforced resolution
  _retired-ids.md               # Retired-not-reused ref-IDs
  _versioning.md                # Versioning conventions
  _glossary.md                  # Terms, abbreviations, standards
  _thresholds.md                # Threshold Reference (split landed v5.0.0)
  tp/                           # Technical Pipeline
    audio-capture.md
    asr-transcription.md
    diarisation.md
    summarisation-nlp.md
    clinical-coding.md
    downstream-write-back.md
  pi/                           # Pipeline Interactions
    partial-pipeline.md
    end-to-end-pipeline.md
  hl/                           # The Human Layer
    human-factors-workflow.md
  io/                           # Impact & Outcomes
    patient-experience.md
    fairness-equity.md
  gv/                           # System Governance
    nhs-compliance-regulatory.md
    safety-governance.md
    security-adversarial-robustness.md
    privacy-data-governance.md
    operational.md
    environmental-sustainability.md
    training-competency.md
    vendor-transparency-contractual.md
  es/                           # Evaluation Science
    meta-evaluation.md
  build.py                      # Concatenate sources → avt-metrics-taxonomy.md + CSV/JSON
  build_site.py                 # Populate docs/, render crosscuts, rewrite handles
  parse.py                      # Parse metric files → Metric objects; canonical data model
  audit.py                      # Structural + count + enum + ordering audit checks
  tests/                        # pytest suite covering parse/build/build_site/audit/snapshot
  tools/                        # Snapshot / archive helpers
  README.md                     # This file
```

Underscore-prefixed files contain cross-cutting content (not tied to a single metric group). **Group files within each cluster directory are assembled in an explicit order from `build.FILES`, not alphabetically.** When adding a new group file, edit `build.FILES` to slot it into the correct position; the build will fail loudly if the file isn't listed.

`reference-docs/` (gitignored) holds locally-cached source excerpts used during Pass-B verification. `dist/`, `docs/`, and `site/` (gitignored) hold build artefacts reproduced from source on every CI run.

## Conventions

- **Cluster codes** (TP / PI / HL / IO / GV / ES) are canonical. v4.0 retired the v3.x Part-letter scheme (A–F); pre-v4.0 documents in `archive/` retain the old wording.
- **Reference IDs** are stable identifiers. Retired IDs are recorded in `_retired-ids.md` and never reused.
- **Within-cluster ordering** (v5.4.0+): metric blocks within each cluster file appear in ascending numeric ref-ID order. Audit-enforced via `check_within_cluster_order` (WARN-level).
- **Gap-candidate ID allocation** (v5.3.0+): gap candidates in `_gaps.md` are slot-less; ref-IDs are allocated to the next-available slot in the natural cluster at promotion time. See `_versioning.md § Gap-candidate ID allocation`.
- **Topic-cited convention for NHSE IG** (v5.5.0+): the NHSE IG hub doesn't expose a stable per-section URL anchor; Source rows derived from that guidance use topic-cited references rather than fabricated section numbers.
- **Per-metric dimensions** are the source of truth for Family, Applicability, Layer, and other structural fields; cross-cutting `_*.md` files are derived views.

## Versioning

Stable releases are tagged on `main`. See [`../CHANGELOG.md`](../CHANGELOG.md) for the full release history. Notable historical milestones:

- `v1.0` — 151 metrics, initial modular split from monolithic v0.
- `v2.0` — 214 metrics, first major extension; sub-clusters and named families introduced.
- `v3.x` — multiple tier 1 tightening waves, calibration & context principle, NHSE Registry mapped as 13th framework, References catalogue with audit-enforced handle resolution.
- `v4.0.0` — cluster-code naming throughout (`part-a/` → `tp/` etc.); CSV/JSON breaking change.
- `v4.2 / v4.3 / v4.4` — three-pass Formal Definition + code snippet verification, end-to-end across all 221 metrics.
- `v5.0.0` — structural split: thresholds move to dedicated Threshold Reference page; **Trigger Conditions** sub-block replaces **Threshold Guidance**; per-metric pointers; "starting points" framing structurally repeated.
- `v5.3.0 / v5.4.0` — Phase 5 minimum-set extension against the FTS-direct surface: 7 promotions T2 → T1 + 13 pull-throughs + 2 mints; named-metric families consolidated to `_families.md` with audit-enforced `Family` dimension; Layer of Defence principle named.
- `v5.5.0` → `v5.5.7` — `_ai-substrate.md`, `_failure-pathways.md`, `_dimensions-overview.md` cross-cutting pages; explicit per-metric `Layer` dimension on all 236 metrics; AI-substrate Option 2 derivation; CC BY 4.0 catalogue licence; consistency sweeps.

The release-cadence convention is documented in [`_versioning.md`](_versioning.md) — content-aware semantics for what counts as MAJOR (structural breaking change), MINOR (new metrics or new principles), or PATCH (fixes / refresh / housekeeping). Audit slice `check_version_bump_consistency` flags over- and under-bumps.

## Contributing

One metric = one edit to one file. Add new metrics to the appropriate group file in **ascending numeric ref-ID order** (the within-cluster numerical-ordering convention from v5.4.0). Each new metric needs the full dimensions table (see `_dimensions-overview.md` for the 13 dimensions), Why-this-tier rationale, Formal Definition, and Limitations. Optional: Reference Standard / Operational Specification / Trigger Conditions sub-blocks for tightened metrics; Code snippet only where the source already includes one.

After editing:

1. `uv run python taxonomy/build.py` — assemble the catalogue
2. `uv run python taxonomy/audit.py` — fail-loudly checks (the audit is the gate; CI fails on any finding)
3. `uv run pytest` — unit tests
4. `uv run mkdocs build --strict` — site-build broken-link check

A new metric group requires a new file in the appropriate cluster directory and an explicit entry in `build.FILES`. Update `_contents.md` per-group counts in the same commit.

## See also

- [`../README.md`](../README.md) — reader-facing description of what the taxonomy is for
- [`../CLAUDE.md`](../CLAUDE.md) — session-level guidance for Claude Code working in this repo
- [`../CHANGELOG.md`](../CHANGELOG.md) — full release history
- [`../plan-future.md`](../plan-future.md) — open backlog items
- [`../LICENSE`](../LICENSE) — CC BY 4.0 catalogue licence + per-artefact split
