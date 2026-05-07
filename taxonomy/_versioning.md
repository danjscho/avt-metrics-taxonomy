# Versioning conventions

How releases of this taxonomy are numbered, what each digit means, and how per-metric provenance is surfaced. Written down so contributors and downstream consumers can predict what changes between versions without reverse-engineering the git log.

## Release-level versioning — semantic but content-aware

Versions are `vMAJOR.MINOR.PATCH` (e.g. `v4.4.0`). Mapping to change kind:

| Bump | Trigger |
|---|---|
| **MAJOR** | Breaking changes to the metric set or downstream consumer contract — metrics renamed / renumbered / removed; CSV / JSON column rename; reference-ID scheme reshape; cluster-code overhaul. v4.0 (Part-letter retirement → cluster codes) is the canonical example. |
| **MINOR** | Substantive content addition or a verification wave that touches metric content — new metrics promoted from `_gaps.md`, new tightening pattern applied across a Tier 1 cohort, Pass A/B verification waves correcting confabulated source attributions, new catalogue handles promoted, new mapped framework. v4.1 (3 new metrics + Tier column) and v4.2 / v4.3 / v4.4 (verification waves) are MINOR. |
| **PATCH** | Site, tooling, build, or audit changes that don't touch metric content — site-build patches (e.g. v4.2.1 ref-ID linkification), test-suite additions, dependency or CI changes, README / glossary copy-edits, audit-rule additions that don't change the metrics themselves. v3.8.1 / v3.8.2 / v3.8.3 / v3.8.4 / v3.9.1 / v4.2.1 are all PATCH. |

The split that matters: **MINOR = the rendered content actually changed**, PATCH = the rendering pipeline or surrounding tooling changed. A reader who only cares about content can skip PATCH releases without missing anything substantive.

## Content vs site separation

Site and content releases share the same version stream (one `vX.Y.Z` per release) but are conceptually separable:

- **Content release** = at least one metric body / catalogue entry / cross-cutting principle changed → MINOR or MAJOR
- **Site / tooling release** = no metric content changed → PATCH

The shared-stream choice keeps the version simple — readers don't have to track two numbers — but the convention above lets them filter to "content-meaningful" releases by ignoring PATCH.

A small audit check (added in v4.5) warns when:

- a release bumps MINOR/MAJOR but `git diff` against the previous tag shows no metric or catalogue file changed (suggests an over-bump)
- a release bumps PATCH but metric files did change (suggests an under-bump)

The check is informational, not blocking — there are legitimate exceptions (e.g. shipping a metric content fix as part of a wider tooling PATCH).

## Per-metric provenance

Two mechanisms, mirroring the release-level split:

### Site-level metric history

Auto-generated from git history at build time. Lists, per release, which metrics had a substantive content change. Lives at [Metric History](metric-history.md) on the site. Mechanical, exhaustive, but coarse — it knows that the file changed, not what changed semantically.

### Metric-level Change history stanzas

A small `**Change history:**` stanza appears on the subset of metrics that had a *substantive* fix or framing change worth flagging to the reader. Examples: v3.3 Tier-1 tightenings, v4.2 confabulation corrections, v4.3 metric content fixes (HL.HF-8 trust instruments etc.), v4.4 GV.SG-5 medRxiv re-attribution.

Stanzas list `vX.Y.Z` (one-line summary of what changed). Manual to maintain at release time; audit checks the cited versions exist.

Most metrics have only whitespace / cross-reference / grammar churn since their introduction and carry no stanza — adding "Last updated: vX.Y" universally would be noise without signal. The stanza is opt-in for changes the reader should know about.

## Tagging and merge mechanics

- All releases tag on `main` after a `--no-ff` merge from the release branch
- Tag format: `vX.Y.Z` (no leading zero, no `v0.x` prerelease numbering — the prototype is at v4.x already)
- `parse.py:TAXONOMY_VERSION` and `pyproject.toml:version` bumped together in the release commit; the `{{TAXONOMY_VERSION}}` / `{{TAXONOMY_DATE}}` template tokens propagate to every header, banner, and citation block at build time

## Deprecation policy

Reference IDs (TP.AC-1 etc.) are stable identifiers. When a metric is removed (e.g. v3.7 redundancy resolution promoting two related metrics into a parent + sub-parts), the original ID is **retired, not reused**:

- `_retired-ids.md` records the retired ID and the reason
- `audit.py:check_retired_ids_not_reused` enforces non-reuse
- Documentation may continue to reference retired IDs in historical narration; the cross-cut linkifier tolerates them

This applies symmetrically to catalogue handles: a handle that resolves today should resolve in every future version, even if the entry's content changes (e.g. v4.4 corrected the `Chung-NEJM-AI-2025` entry to describe the right paper without renaming the handle).

## Gap-candidate ID allocation (v5.3.0 convention)

Gap candidates in `_gaps.md` no longer reserve specific reference IDs. Earlier versions of `_gaps.md` listed proposed ref-IDs (e.g. `GV.OP-10` for a NICE ESF cost-effectiveness candidate) under the assumption that each gap would land at its proposed slot when promoted. In practice this caused:

- **Numbering gaps inside active clusters** (e.g. GV.OP missing -10/-11/-12/-13 because those were reserved for deferred candidates).
- **Slot conflicts at promotion time** when two gap candidates competed for the same proposed slot, or when v5.3.0's pull-through plan diverged from the original `_gaps.md` allocation.
- **Stale cross-references** in archived plans pointing to slots whose meaning changed before promotion.

From v5.3.0 onwards, gap candidates are slot-less. `_gaps.md` rows show `Proposed (slot at promotion)` or similar; the actual ref-ID is allocated to the next-available slot in the natural cluster at the moment the candidate is promoted to an active metric. Deprecated IDs (HL.HF-4, TP.CC-8, TP.SN-8/-10) remain retired under the existing deprecation policy and are *not* reused as fill.
