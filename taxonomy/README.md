# AVT Metrics Taxonomy - Repository Guide

## Local development — build and serve the site

A fresh clone needs three steps to reproduce what `https://danjscho.github.io/avt-metrics-taxonomy/` shows. The project uses [uv](https://docs.astral.sh/uv/) for Python environment management; install it via `curl -LsSf https://astral.sh/uv/install.sh | sh` (or `brew install uv`) if you don't already have it. All commands run from the repo root.

### 1. Install dependencies

```
uv sync
```

`uv sync` reads `pyproject.toml` + `uv.lock` and creates a `.venv/` with the exact package set CI uses (`mkdocs-material`, `mike`, `mkdocs-rss-plugin` plus their transitive deps). The lockfile is committed so local builds match CI bit-for-bit. uv also handles the Python toolchain — no separate `pyenv` / `python -m venv` step needed.

### 2. Build the artefacts

```
uv run python taxonomy/build.py        # → avt-metrics-taxonomy.md + dist/{metrics.csv,metrics.json,gaps.json,summary.json}
uv run python taxonomy/build_site.py   # → populates docs/ and mirrors dist/* into docs/downloads/
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

- `dist/metrics.csv` — flat 218-row spreadsheet (17 columns)
- `dist/metrics.json` — same metrics with full structured dimension data preserved per entry
- `dist/gaps.json` — 89 roadmap candidates partitioned by origin
- `dist/summary.json` — headline counts (metric / tier / group / gap)
- `avt-metrics-taxonomy.md` (repo root) — monolithic concatenated Markdown

`taxonomy/build_site.py`'s `_mirror_downloads()` then copies these into `docs/downloads/` so `mkdocs serve` can serve them locally; CI does the equivalent copy via the workflow file.

### Audit

```
uv run python taxonomy/audit.py
```

Source of truth for current state — emits parsed counts, the Tier 1 tightening manifest, retired/reserved IDs, and any structural findings. The CI workflow runs this first and fails the build on any finding. Run it before pushing if you've touched metric files.

## Building the document (legacy short form)

```
uv run python taxonomy/build.py
```

Produces `avt-metrics-taxonomy.md` at the repo root by concatenating the modular source files in the order defined in `build.py`. The script is idempotent.

## File structure

```
taxonomy/
  _header.md                    # Title, metric count, preamble
  _how-to-use.md                # Priority tiers, cadence, responsible actors,
                                # adapting to local context
  _summary.md                   # By priority tier, by maturity
  _tier-1-quick-reference.md    # All Tier 1 metrics organised by responsible actor
  _contents.md                  # Table of contents
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
    safety-governance.md
    nhs-compliance-regulatory.md
    security-adversarial-robustness.md
    privacy-data-governance.md
    operational.md
    environmental-sustainability.md
    training-competency.md
    vendor-transparency-contractual.md
  es/                           # Evaluation Science
    meta-evaluation.md
  build.py
  README.md
```

Underscore-prefixed files contain cross-cutting content (not tied to a single metric group). Group files within each part directory are assembled alphabetically.

## Versioning

Stable releases are tagged on `main`:

- `v1.0` - 151 metrics across 18 groups (initial modular split)
- `v2.0` - 214 metrics across 20 groups (first major extension)

## Contributing

One metric = one edit to one file. Add new metrics to the appropriate group file in the correct tier order (Tier 1 before Tier 2 before Tier 3). After editing, run `build.py` and verify the output looks correct before committing.

New metric groups require a new file in the appropriate part directory and an update to the file order in `build.py` if the alphabetical default is not correct.
