# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A healthcare metrics taxonomy for assuring Ambient Voice Technology (AVT) systems — ambient scribes and clinical AI documentation tools — in NHS and comparable healthcare settings.

The repo contains both **catalogue content** (Markdown source under `taxonomy/`) and **Python tooling** (parser, builder, audit, site-build, tests) that keeps the catalogue reproducible. Since v0.1.0 of `avt-metrics-ref` (currently on the `reference-library-pilot` branch only), the repo also hosts a **separately-versioned reference implementation library** at `pkg/avt_metrics_ref/`. The catalogue and the package release at independent cadences and are licensed separately.

The taxonomy organises metrics across pipeline layers (audio capture, ASR, diarisation, summarisation, clinical coding, downstream write-back) and per-metric structural dimensions: Priority Tier, Applicability, Family, Layer of Defence (Prevention / Detection / Limitation), Pipeline Layer, Assurance Question, Measurement Method, Lifecycle Phases, Measurement Cadence (multi-valued), Responsible Actors, Maturity, Outcome Type, and Source.

**Current state:** v5.5.7 — 236 metrics across 20 groups. Tier counts 58 / 99 / 79. Eight named metric families. All metrics carry an explicit `Layer` field. Catalogue is licensed CC BY 4.0; package on the pilot branch is MIT-licensed.

## Build

```
uv sync                                     # install deps + lockfile
uv run python taxonomy/build.py             # → avt-metrics-taxonomy.md + dist/* CSV/JSON
uv run python taxonomy/build_site.py        # → populates docs/ + crosscut pages
uv run mkdocs serve                         # → http://127.0.0.1:8000/avt-metrics-taxonomy/
uv run python taxonomy/audit.py             # → 15 structural + count + enum checks
uv run pytest                               # → 99 unit tests across parse/build/build_site/audit/snapshot
uv run mkdocs build --strict                # → fails on broken links or missing pages
```

The build is idempotent — running it twice produces identical output. The CI workflow (`.github/workflows/build-deploy.yml`) runs audit + pytest first and fails the build on any finding.

**Build file order** is defined explicitly in `taxonomy/build.py:FILES`. The order matters because the assembled `avt-metrics-taxonomy.md` is concatenated in that sequence. Underscore-prefixed cross-cutting files come first, then per-cluster directories `tp/` / `pi/` / `hl/` / `io/` / `gv/` / `es/` with explicit per-cluster filename ordering.

## File structure

```
taxonomy/
  _header.md                    # Title, metric count, prototype-status framing
  _prototype-status.md          # Detailed prototype framing
  _how-to-use.md                # Priority tiers, cadence, actors, deployment guidance
  _summary.md                   # By tier, maturity, family, underspecification warning
  _tier-1-quick-reference.md    # All Tier 1 metrics organised by responsible actor
  _contents.md                  # Table of contents with family / sub-cluster convention
  _applicability.md             # Per-metric applicability matrix
  _families.md                  # 8 named metric families (canonical home; v5.4.0+)
  _layers-of-defence.md         # Prevention/Detection/Limitation principle (v5.4.0+)
  _failure-pathways.md          # 3 archetypes + worked timeline (v5.5.1)
  _ai-substrate.md              # 5-class derived cut (v5.5.0; structurally derived v5.5.3)
  _dimensions-overview.md       # Reader-orientation page for the 13 per-metric dimensions
  _outcomes-boundary.md         # Out-of-scope statement (v3.3 first-class principle)
  _calibration-and-context.md   # Calibration principle (v3.7 first-class principle)
  _standards-mapping.md         # 13-framework mapping
  _responsible-ai-lens.md       # DSIT Playbook + ethical themes
  _gaps.md                      # 74 outstanding candidates + §7 promoted historical record
  _references.md                # Catalogue handles (~110 entries); audit-enforced resolution
  _retired-ids.md               # Retired-not-reused ref-IDs
  _versioning.md                # Versioning conventions (release / per-metric / gap-allocation)
  _glossary.md                  # Terms, abbreviations, standards
  _thresholds.md                # Threshold Reference (structural split landed v5.0.0)
  tp/                           # Technical Pipeline (audio → downstream write-back)
  pi/                           # Pipeline Interactions (partial + end-to-end)
  hl/                           # Human Layer (human factors and workflow)
  io/                           # Impact & Outcomes (patient experience + fairness/equity)
  gv/                           # System Governance (compliance, safety, security, privacy,
                                #   operations, sustainability, training, vendor transparency,
                                #   environmental)
  es/                           # Evaluation Science (meta-evaluation)
  build.py                      # Concatenate sources → avt-metrics-taxonomy.md + CSV/JSON
  build_site.py                 # Populate docs/ for mkdocs; render crosscuts; rewrite handles
  parse.py                      # Parse metric files → Metric objects; canonical data model
  audit.py                      # Structural + count + enum + ordering audit checks
  tests/                        # pytest suite covering parse/build/build_site/audit/snapshot
  tools/                        # Snapshot / archive helpers
```

Underscore-prefixed files sort to the top and contain cross-cutting content (not group content). Group files within each cluster directory are one file per metric group, ordered explicitly in `build.FILES` (not alphabetically).

The two-letter cluster code (TP / PI / HL / IO / GV / ES) is the canonical naming surface throughout. v4.0 retired the v3.x Part-letter scheme (A–F); pre-v4.0 documents in `archive/` retain the old wording.

## Metric entry format

Every metric entry follows this structure (in order):

1. Tier icon + metric name heading (`### REF-ID 🟢/🟡/🔵 Name`)
2. **Optional Change history stanza** — for metrics with substantive fixes since drafting
3. **Dimensions table** — all per-metric structural axes (see `_dimensions-overview.md` for the 13 dimensions)
4. **Why this tier?** — rationale for the priority assignment
5. **Formal Definition** block — mathematical or operational definition
6. **Reference Standard** + **Operational Specification** + **Trigger Conditions** sub-blocks (Tier 1 metrics with the v3.4+ tightening pattern; numerical thresholds live in `docs/thresholds.md` since v5.0.0, not in the body)
7. **References** sub-block (where catalogue handles need explicit framing)
8. **Limitations** section
9. **Novel Thinking / Implications** section (may be absent)
10. Code snippet (only where the source file already includes one — do not add speculatively)

Within-cluster metric ordering: ascending numeric ref-ID (v5.4.0 convention; audit-enforced via `check_within_cluster_order`).

For sub-cluster groupings: an italic 1–2 sentence intro paragraph appears before the first metric in the sub-cluster.

For named metric families: framing prose lives on the canonical `_families.md` page (since v5.5.0). Member metrics carry a `Family: <name>` row in their dimensions table (audit-enforced via `check_family_resolves`) and a `*See also: ... family*` italic at the bottom of their body.

## Locked conventions

Do not revisit these without explicit user instruction:

- **Reference IDs are stable identifiers.** Retired IDs are recorded in `_retired-ids.md` and never reused (`check_retired_ids_not_reused`). The deprecate-don't-renumber pattern applies symmetrically to catalogue handles.
- **Gap-candidate ID allocation (v5.3.0+).** Gap candidates in `_gaps.md` no longer reserve specific reference IDs; the actual ref-ID is allocated to the next-available slot at promotion time. See `_versioning.md § Gap-candidate ID allocation`.
- **Within-cluster numerical ordering (v5.4.0+).** Metric blocks within each cluster file appear in ascending numeric ref-ID order. Audit-enforced as WARN.
- **Topic-cited convention for NHSE IG (v5.5.0+).** The NHSE IG guidance hub does not currently expose a stable per-section URL anchor. Source rows on metrics derived from that guidance use topic-cited references rather than fabricated section numbers.
- **Per-artefact licensing.** Catalogue content under `taxonomy/` and supporting documents at the repo root are CC BY 4.0. The reference implementation library at `pkg/avt_metrics_ref/` (currently on `reference-library-pilot` branch only) is MIT. The Python tooling under `taxonomy/*.py` is supplied to make the catalogue reproducible; treat as MIT for independent re-use. See `LICENSE` for the full per-artefact split.
- **Branch discipline.** Catalogue work happens on per-release branches (`v5-5-X-<topic>`) merged with `--no-ff` to main and tagged. The reference implementation library lives on `reference-library-pilot` and may not merge to main without an explicit decision; rebase pilot on main when main moves.

## File location conventions

- **`archive/` is for finished work only.** Plans, review files, and round-trip artefacts that are still being actively edited or reviewed live at the repo root. Move them into `archive/plans/` (per-release plans), `archive/audits/` (audit research outputs), `archive/v5.X/` (per-release research), or `archive/` (other historical artefacts) only when the associated release ships or the review closes. Premature archiving forces context switches when you need to come back to active work; late archiving keeps history clean.
- **Per-release plan files** (`plan-vX.Y.md`) start at the repo root during the release, then move to `archive/plans/` in the release-wrap commit.
- **Round-trip review files** (`vX.Y-*-review.md`, `vX.Y-pre-mint-triage.md`, `vX.Y-merge-and-family-sweep.md`) start at the repo root during active review, then move to `archive/` once the review closes and changes have landed.
- **`reference-docs/`** (gitignored) — locally-cached source excerpts used during Pass-B verification. Working material, not committed.
- **`.claude/`** (gitignored) — local Claude Code workspace.
- **`dist/` / `docs/` / `site/`** (gitignored) — build artefacts. Reproduced from source on every CI run.

## When to stop and ask the user

Pause and ask rather than making an autonomous call if:

- Final metric counts in the Summary or Contents disagree with actual counts in the assembled file
- A "See also" cross-reference points to a metric that cannot be found
- A new metric needs a tier assignment that conflicts with the placement logic for existing metrics
- A change would break a locked convention from the section above
- A change would touch the prototype-status framing in `_prototype-status.md` or `README.md` (these are deliberately reviewer-gated)

## Commit conventions

- Start all commit messages with 🦞 (`:lobster:`).
- Use the body to explain the *why*; the subject line should be `🦞 vX.Y.Z — short summary` for releases or `🦞 <short summary>` for non-release commits.
- One logical change per commit; rebase the pilot branch on main when main moves rather than merging main into the pilot.
- Co-author trailer: `Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>` for AI-coauthored commits.

## Tag and release conventions

- Tags follow semantic versioning: `vMAJOR.MINOR.PATCH`.
- See `_versioning.md` for the content-aware semantics — what counts as MAJOR (structural breaking change), MINOR (new metrics or new principles), PATCH (fixes / refresh / housekeeping). Audit slice `check_version_bump_consistency` flags over- and under-bumps.
- Release wrap order: bump `taxonomy/parse.py:TAXONOMY_VERSION` → bump `pyproject.toml:version` → update `README.md` version strings → add CHANGELOG entry → run build / audit / pytest / mkdocs strict → commit → merge to main with `--no-ff` → tag → push tag.
