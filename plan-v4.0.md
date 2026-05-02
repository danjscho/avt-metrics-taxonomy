# v4.0 plan — drop Part letters, align folder structure with two-letter cluster codes

## Context

The taxonomy currently carries **two parallel naming schemes** for the same six top-level clusters:

| Cluster | Two-letter prefix (in ref-IDs) | Part letter (in folders + headings) |
|---|---|---|
| Technical Pipeline | `TP` | A |
| Pipeline Interactions | `PI` | B |
| Human Layer | `HL` | C |
| Impact & Outcomes | `IO` | D |
| Governance | `GV` | E |
| Evaluation Science | `ES` | F |

The Part letter is a holdover from when the taxonomy was a monolithic markdown file that needed top-level sequencing. Once ref-IDs were introduced, the Part letter became redundant — the prefix already encodes the cluster, and "Part E" carries less information than "GV" because a reader has to look up which letter is which. The two-scheme overhead surfaces every time someone reads a CSV row, a cross-reference, or the folder tree:

- `dist/metrics.csv` had `part=A` until v3.8.3 added `part_name`. The letter alone is meaningless without the lookup.
- Folder names `part-a/` … `part-f/` vs ref-ID prefixes `TP`/`PI`/`HL`/`IO`/`GV`/`ES` create a needless translation step.
- Cross-references in metric files say "see Part E for governance" when "see GV cluster" would be both shorter and self-explaining.
- The Part letter is **not even ordinal in any meaningful way** — A/B/C/D/E/F is just an artefact of the order they happened to be drafted. Any rationale for the order (pipeline-first → human-second → governance-third → meta-last) is implicit and would survive renaming the scheme.

v4.0 retires the Part-letter scheme entirely and aligns the folder structure, file paths, prose references, and downloads metadata to the two-letter cluster codes. This is a **structural release**, not a content release — no metrics added, no thresholds tightened, no roadmap promotions. The output is a cleaner repo where one naming scheme drives everything.

**Why a v4.0, not a v3.x patch.** The folder rename and the prose sweep affect ~300+ source-file references and produce a backwards-incompatible CSV/JSON shape change (`part: "A"` → `part: "TP"` and `part_name` reframed). External consumers of `dist/metrics.csv` (if any) would need to update. Bumping the major version signals that and gives a clean break. The git history pre-v4.0 still uses Part letters; readers of historic plans / archive artefacts won't be confused because those files name themselves as v3.x.

**Non-goals.** No metric content changes. No tier shifts. No new metrics. No roadmap promotions. No ref-ID renames (TP.AC-1 stays TP.AC-1 — only the cluster-naming layer above ref-IDs changes). No changes to the *order* clusters are presented in (pipeline → interactions → human → outcomes → governance → meta stays).

## Decisions to settle at planning time

**Locked at draft time, can be revisited at the Phase 0 gate:**

- **New cluster code is the existing two-letter prefix.** `TP`, `PI`, `HL`, `IO`, `GV`, `ES`. No renaming. The prefix is already the canonical identifier in every ref-ID; all v4.0 does is surface it everywhere else.
- **Folder rename: `part-a/` → `tp/`, `part-b/` → `pi/`, etc.** Two-letter lowercase. Matches the ref-ID prefix in lowercase form.
- **CSV/JSON breaking change.** `part: "A"` → `part: "TP"`. `part_name: "The Technical Pipeline"` stays. (Or rename to `cluster` / `cluster_code` / `cluster_name` — see open question 1.)
- **Cluster ordering stays current.** TP → PI → HL → IO → GV → ES. The order is meaningful (pipeline → end-to-end → human → outcomes → governance → meta) even though it's not encoded in any letter.
- **Archive content frozen.** Existing `archive/plan-*.md` and `archive/v*-*.md` files are historical artefacts; we do not back-edit them. Their Part-letter references stay as written. New content (CHANGELOG entries, plans from v4.0 onwards) uses cluster codes only.

**Open questions to resolve at the Phase 0 gate (after the pilot lands):**

1. Field naming on CSV/JSON. Options:
   - (a) Keep `part` / `part_name` field names; just change values (`part: "TP"`).
   - (b) Rename to `cluster` / `cluster_name`. Cleaner but a second breaking change.
   - (c) Rename to `cluster_code` / `cluster_name`. Most explicit.
   Default if unanswered: **(b)** for clean break.

2. Heading shape in metric files. Currently group files start with `## Group Name` (no Part heading on most; first file per part has `# Part X - …`). Options:
   - (a) Strip the `# Part X` heading from the one-per-part file that carries it (5 of 32 files affected) and let each group stand alone. Build-site infers the cluster from path.
   - (b) Replace `# Part X - Name` with `# TP - Technical Pipeline` cluster headings.
   Default if unanswered: **(a)** — folder name carries the cluster; no need for a redundant heading.

3. URL slug stability. Currently group pages render at `/groups/audio-capture/`. The folder rename doesn't touch this — `MAPPING` in `build_site.py` already maps `part-a/audio-capture.md` → `groups/audio-capture.md`. After v4.0 the source path becomes `tp/audio-capture.md` but the rendered URL stays the same. **No reader-facing URL changes.** This is a non-issue but worth flagging because we explicitly want it.

## Surface area (measured 2026-04-26 against main @ v3.8.3)

| Reference type | Count | Disposition in v4.0 |
|---|---|---|
| `Part [A-F]` literal in `taxonomy/` source | 32 | Sweep: replace with cluster code or remove |
| `Part [A-F]` in `README.md` + repo-root docs | 32 | Sweep: replace with cluster code |
| `Part [A-F]` in `CHANGELOG.md` | 5 | **Leave** — historical entries describe past work; new entries use cluster codes |
| `Part [A-F]` in `archive/*` | 51 | **Leave** — frozen historical artefacts |
| `part-[a-f]/` path-strings in `taxonomy/` | 208 | Sweep: rewrite to `<cluster>/` |
| `part-[a-f]/` path-strings in Python build code | (subset of 208) | Sweep: rewrite |
| `part_a` / `part-a` slugs in test fixtures or CSS | check | Likely zero; verify in Phase 0 |

**Headline:** ~270 source-side references to sweep, 56 deliberately left alone in historical files. One major folder rename (6 directories). Three Python files updated (`parse.py`, `build.py`, `build_site.py`).

## Phasing

### Phase 0 — pilot the cluster-code rename on TP only (1 commit)

Apply the new naming to the one cluster (`TP` = current Part A) so we can react to the shape before sweeping all six. Pilot covers:

- `git mv taxonomy/part-a/ taxonomy/tp/`
- Update `parse.GROUP_FILES` keys for the 6 TP files: `part-a/audio-capture.md` → `tp/audio-capture.md` etc.
- Update `parse.PART_NAMES` → `parse.CLUSTER_NAMES`, keyed by `TP`/`PI`/`HL`/`IO`/`GV`/`ES`. Add `CLUSTER_ORDER` list to preserve presentation order.
- Update `build.py` `FILES` list path strings for the TP files.
- Update `build_site.MAPPING` and `SRC_GROUP_FILE_TO_PAGE` keys for the TP files.
- Update the one `# Part A - The Technical Pipeline` heading in the source file that carries it (decision 2 default — strip).
- Update `_standards-mapping.md` and `_responsible-ai-lens.md` and `_gaps.md` for any TP-prefixed cross-references.
- CSV / JSON: keep field name `part` for now (defer field-rename decision to Phase 0 gate per open question 1); change values: `part: "A"` → `part: "TP"` for the 6 TP-cluster metrics. Other metrics still emit `part: "B"`/`"C"` etc. — site will be in mixed state during pilot, that's acceptable for the gate.
- Audit: extend `audit.py` to check the new naming is consistent within the TP cluster.

**Deliverables at gate:**
- Pilot branch with all TP changes committed
- Mixed-state CSV/JSON to look at (TP rows have new shape; other rows old)
- Brief writeup `archive/v4.0-pilot-notes.md` recording what worked, what was awkward, recommendations for the full sweep
- Open questions 1 and 2 answered explicitly before Phase 1

**Gate:** stop, review with user, settle the field-naming and heading-shape questions before continuing.

### Phase 1 — sweep the remaining 5 clusters (2 commits)

After Phase 0 settles the grammar:

- Commit 1: rename and sweep `PI`, `HL`, `IO` (clusters B, C, D — smaller groups: 2 + 1 + 2 = 5 group files)
- Commit 2: rename and sweep `GV`, `ES` (clusters E, F — larger and meta: 8 + 1 = 9 group files)

Each commit:
- `git mv` the directory
- Update `parse.GROUP_FILES`, `build.FILES`, `build_site.MAPPING` + `SRC_GROUP_FILE_TO_PAGE`
- Strip any `# Part X - …` headings
- Update cross-cut files (`_standards-mapping.md`, `_responsible-ai-lens.md`, `_gaps.md`, `_applicability.md`) for the cluster's metrics

`audit.py` enforces no `part-[a-f]/` path strings remain in any non-archive source file.

### Phase 2 — sweep prose references (1 commit)

The 32 + 32 prose references in `taxonomy/` and root README. Mechanical pass: every `Part E` → `the GV cluster`, `Part A metrics` → `TP metrics`, etc. Phase-0 pilot will surface the natural prose patterns; this commit applies them everywhere.

`audit.py` gains `check_no_part_letter_prose` (no `Part [A-F]\b` matches outside `archive/` and `CHANGELOG.md` historical entries).

### Phase 3 — Python code + downloads (1 commit)

- `parse.GROUP_FILES`: rename inner key from `"part"` to `"cluster"`.
- `Metric.part` → `Metric.cluster`. `Metric.part_name` → `Metric.cluster_name`. (Field rename — settled at Phase 0 gate.)
- `build.py` CSV columns: `part` → `cluster`, `part_name` → `cluster_name`. (Or keep field names and just change values — settled at Phase 0 gate.)
- `build.py` JSON: same field rename.
- `build_site.PART_TITLES` → `build_site.CLUSTER_TITLES` (or remove entirely if unused after the prose sweep).
- `build_site.PART_NAMES` references in CSS / theme overrides — verify and update.

### Phase 4 — site nav restructure (1 commit)

`mkdocs.yml` nav block currently uses Part-letter section headings:

```
- Browse metrics:
    - Contents: contents.md
    - A - Technical Pipeline:
        - Audio Capture & Environment: groups/audio-capture.md
        ...
```

Replace with cluster-code headings:

```
- Browse metrics:
    - Contents: contents.md
    - TP - Technical Pipeline:
        - Audio Capture & Environment: groups/audio-capture.md
        ...
```

This is the most reader-visible change. Test in `mkdocs serve` before commit.

### Phase 5 — release wrap (1 commit + merge)

- CHANGELOG v4.0 entry naming the breaking changes:
  - `dist/metrics.csv` field names changed (specify old → new)
  - `dist/metrics.json` field names changed
  - Folder structure changed (relevant for anyone with local clones with WIP)
  - Reader-facing site nav changed (Part letter → cluster code)
- README updates: every Part-letter reference rewritten
- Version bump to `v4.0.0` (semver — major version because of breaking download-format changes)
- `taxonomy/_header.md` updated for the new top-level naming
- `pyproject.toml` version → `4.0.0`
- Plan archived to `archive/plan-v4.0.md` plus the pilot notes

Tag `v4.0`, merge `--no-ff`, push.

## Forward-compatibility / migration

For external consumers of `dist/metrics.csv` (if any exist — currently we don't know of any), v4.0 should ship with a **migration note** in CHANGELOG and on the rendered site Downloads page:

> v3.x CSVs had `part = "A".."F"`. v4.0 CSVs have `cluster = "TP" / "PI" / "HL" / "IO" / "GV" / "ES"`. Mapping: A→TP, B→PI, C→HL, D→IO, E→GV, F→ES. The cluster code matches the prefix on every ref-ID in the same row.

No backwards-compat shim. v4.0 is the breaking change; consumers update once.

## Critical files

- `taxonomy/parse.py` (CLUSTER_NAMES + CLUSTER_ORDER, GROUP_FILES key rewrite, Metric field rename)
- `taxonomy/build.py` (FILES list, CSV columns, JSON shape)
- `taxonomy/build_site.py` (MAPPING, SRC_GROUP_FILE_TO_PAGE, PART_TITLES → CLUSTER_TITLES, kicker prose)
- `taxonomy/audit.py` (new check_no_part_letter_prose, updated path validators)
- `taxonomy/part-{a..f}/` directories — renamed via `git mv`
- `taxonomy/_standards-mapping.md`, `taxonomy/_responsible-ai-lens.md`, `taxonomy/_gaps.md`, `taxonomy/_applicability.md` (cross-references)
- `taxonomy/_header.md`, `taxonomy/_how-to-use.md`, `taxonomy/_contents.md` (reader-facing)
- `mkdocs.yml` (nav block)
- `README.md`, `CHANGELOG.md` (release wrap)

## Verification

End-to-end at every gate and at release:

- `uv run python taxonomy/audit.py` clean (extended with new checks)
- `uv run python taxonomy/build.py` produces 218 metrics with new field shape
- `uv run python taxonomy/build_site.py` populates `docs/` from new folder layout
- `uv run mkdocs build --strict` exits 0 — no broken links from the rename
- `uv run mkdocs serve`: all 20 group pages render correctly under their existing URLs (URLs unchanged); cluster-code labels visible on each group page eyebrow; site nav shows TP/PI/HL/IO/GV/ES headings
- Spot-check 5 random cross-references that previously said "Part E" now say "GV cluster" (or chosen prose pattern)
- `dist/metrics.csv` row 1: `cluster: "TP", cluster_name: "Technical Pipeline"` (or kept `part` field name with new value, per Phase 0 decision)
- Counts unchanged: 218 metrics, 43/96/79 tier split, 32/42 Tier 1 tightened, 13 frameworks

## Risks

- **Git history continuity through the rename.** `git log --follow taxonomy/tp/audio-capture.md` should follow back through the rename, but `git blame` may be noisier. Mitigation: do the rename in isolated commits (one per cluster) so the rename is the only thing in that commit's diff, which makes `--follow` reliable.
- **Cross-reference drift during the sweep.** The 208 path-strings in cross-cut files are easy to miss one-by-one. Mitigation: `audit.py` check fails the build on any `part-[a-f]/` path-string outside `archive/`.
- **Stale ANCHOR_REWRITES in `build_site.py`.** Existing entries reference group anchors via path-derived slugs that won't change (group slug stays `audio-capture`). Verify in Phase 0.
- **Mid-sweep breakage in CI / local serve.** Phase 0 deliberately leaves the system in a mixed state for the gate. Each Phase 1 commit must self-validate (build + strict mkdocs build clean) before moving to the next.
- **External consumer break.** Anyone with v3.x scripts that read `dist/metrics.csv` and key on `part` (letter) will break. Mitigation: clear migration note in CHANGELOG + downloads page; bump major version. Stretch option: ship v3.x final release with both old-and-new fields (deprecation period) — flagged here but **not recommended** unless we discover a real consumer; otherwise it's complexity for a hypothetical user.
- **v3.9 references-sweep ordering.** v3.9 (links + Wayback archives) and v4.0 (cluster rename) both touch cross-references heavily. Doing v4.0 *first* makes v3.9 simpler (cleaner naming surface to add citations to). Doing v3.9 first means v4.0 has more references to update. **Recommendation: v4.0 first**, then v3.9. Sequence captured at the bottom of this plan.

## Sequencing — superseded

This section originally recommended **v4.0 then v3.9**. v3.9 shipped first instead (released 2026-05-02; tag `v3.9` on `main`), so the sequencing question is closed.

**Implications for the v4.0 plan now that v3.9 is in place:**

- v4.0 will carry a cross-reference sweep over the citations v3.9 added (~100 catalogue entries with `[Handle]` references in metric files, plus the cross-cutting prose linking now in `_standards-mapping.md`, `_outcomes-boundary.md`, `_calibration-and-context.md`, `_how-to-use.md`). These need the cluster-rename treatment too. Not a structural blocker; just adds to the surface area count.
- The `_references.md` catalogue entries do **not** need re-issuing — handles are stable, URLs are stable, only the cluster names attached to metrics change. The `Cited-by:` auto-generated lists in the catalogue (populated at build time) will pick up the new cluster names automatically.
- Wayback snapshots (deferred from v3.9 pending IA credentials) should be taken **after v4.0** rather than before, so the snapshot URLs land against the post-rename folder structure. Update the v3.9 deferred-items list accordingly when v4.0 ships.
- The 23-file surface for the EPR → Downstream Write-back rename (next section) overlaps heavily with the v3.9 reference catalogue surface; both passes can be done in the same Phase 1 sweep.

## Counts after v4.0

No metric count changes. No tier shifts. New cluster-code naming throughout. New audit check `check_no_part_letter_prose`. Reader-facing site URLs unchanged (group slugs preserved). Folder structure changed; ref-IDs unchanged.

---

## Companion rename: "EPR Write-back" → "Downstream Write-back"

While we're touching cluster names, the **TP.WB group** ("EPR Write-back") should also be relaxed. The taxonomy currently overpromises specificity — write-back actually targets **EPRs, GP clinical systems (EMIS, SystmOne), e-prescribing systems, order-management, referral systems, FHIR endpoints, openEHR repositories, and patient portals**. Naming the group "EPR Write-back" is technically wrong for a substantial subset of the cited surface and may mislead readers into thinking the metrics only apply to full EPR deployments.

**Decided rename (user-confirmed):** "EPR Write-back" → "**Downstream Write-back**". Captures the full surface area; doesn't overpromise clinical specificity (some downstream targets are admin/operational, not strictly clinical); reads as natural English alongside the other group names.

### What changes

Three flavours of usage to handle:

1. **Group / section / page name** — "EPR Write-back" → "Downstream Write-back" everywhere it appears as a heading, nav label, table-of-contents entry, etc.
2. **Pipeline Layer dimension value** — every metric in TP.WB currently carries `**Pipeline Layer**: EPR Write-back` in its Dimensions table. Rename to `Downstream Write-back`.
3. **Prose softening** — Source rows / Reference Standard / Operational Specification / Threshold Guidance prose mentioning "EPR" specifically should be **kept as "EPR" where the prose is genuinely talking about EPRs** (the metric still applies most commonly to EPRs; relaxing universally would lose the specificity readers actually need); **relaxed to "downstream system"** only where the prose is making a *generic claim* about write-back behaviour. Surgical, not sweeping.

**Ref-IDs stay `TP.WB-*`.** "WB" = "Write-back" already, so the prefix is correct. The rename is purely cosmetic; no ref-ID renumbering, no "deprecate-don't-renumber" pattern needed.

### Decisions to make at the v4.0 Phase 0 gate

1. **Filename — keep `epr-write-back.md` or rename to `downstream-write-back.md`?** The cluster rename already moves this file from `part-a/epr-write-back.md` to `tp/epr-write-back.md`. Renaming the basename in the same commit gives clean naming throughout but breaks any external bookmarks to `/groups/epr-write-back/`. Two options:
   - **(a) Rename basename + add MkDocs redirect** (`mkdocs-redirects` plugin) so old URL `/groups/epr-write-back/` → new URL `/groups/downstream-write-back/`. Cleanest long-term naming. Plugin is one config addition; well-maintained.
   - **(b) Keep basename `epr-write-back.md`** so URLs and content rendering align with the existing reader-facing slug. Group display name on the page heading (`# Downstream Write-back`) and nav label become "Downstream Write-back" but the URL slug stays. Lighter touch; preserves bookmarks. Cost: minor inconsistency between filename and display name.
   - **Default if unanswered: (a)** — clean naming wins; redirect plugin sidesteps the URL-stability concern. Decide at Phase 0 gate.
2. **Pipeline Layer dimension as a controlled vocabulary?** Right now Pipeline Layer is free-text per-metric. Worth confirming the v4.0 sweep treats this as a values-by-rename rather than a values-by-controlled-list — a stretch goal would be `parse.py` enforcing the layer enum. Out of scope for v4.0 by default; flag for a future release.

### Surface area (measured 2026-05-02 against main @ v3.9)

23 files reference "EPR write-back" / "EPR Write-back" / "epr-write-back": `taxonomy/part-a/epr-write-back.md` (the group file itself), `taxonomy/_contents.md`, `taxonomy/_applicability.md`, `taxonomy/_responsible-ai-lens.md`, `taxonomy/_glossary.md`, `taxonomy/_standards-mapping.md`, `taxonomy/_references.md`, `taxonomy/_how-to-use.md`, `taxonomy/build.py`, `taxonomy/build_site.py`, `taxonomy/parse.py`, `taxonomy/audit.py`, `mkdocs.yml`, `README.md`, `taxonomy/README.md`, `CHANGELOG.md`, `CLAUDE.md`, plus several metric files that cross-reference TP.WB-*. Most are mechanical rename; the group file's own prose needs the surgical "EPR" → "downstream system" softening per the prose-softening rule above.

### Phasing

Fold into the v4.0 phasing rather than landing as a separate release:

- **Phase 0 (TP pilot)** — handle the group rename alongside the cluster rename. The TP cluster pilot already touches every TP file; doing the EPR-Write-back rename in the same pass is one walk through the files.
- **Phase 1 (full sweep)** — propagate the rename through cross-cutting files alongside the cluster-folder rename for the remaining clusters.
- **Phase 5 (release wrap)** — CHANGELOG entry covers both the cluster scheme retirement AND the EPR → Downstream rename as a single coherent v4.0 story.

### Why not do this in a v3.9.x patch

Considered. The rename is a heading + dimension-value change that's surgically clean — could ship as a v3.9.x patch. But:

- v4.0 is already touching every group's heading, nav entry, and Pipeline Layer prose. Folding the EPR rename in saves one cross-cutting prose sweep that would otherwise happen twice.
- A v3.9.x release for this single change would be small enough to feel like overhead. v4.0 is the natural home.
- External consumers haven't flagged "EPR Write-back" as a problem; the rename is corrective rather than urgent.

If v4.0 is delayed substantially (>3 months from now), revisit and ship as v3.9.x; otherwise hold for v4.0.
