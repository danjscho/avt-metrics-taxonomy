# v3.9.1 plan — code test suite (pytest)

**Goal.** Add a focused pytest suite under `taxonomy/tests/` covering the load-bearing build-pipeline code (parse / build / build_site / audit / tools/snapshot). Land before v4.0 starts so the test suite is a safety net for the v4.0 cluster rename — not a follow-on cleanup.

**Non-goals.** No taxonomy content changes. No new metrics. No tier shifts. No site changes. No coverage-percentage targets. No generative testing. The deliverable is a small, targeted suite that locks in the structural invariants the existing audit + build + strict-mkdocs integration tests don't catch.

**Why now.** Promoted from `plan-future.md` item #10. The repo has grown from ~v3.7 thin assembly to ~1,500 lines across `parse.py` / `build.py` / `build_site.py` / `audit.py` / `tools/snapshot.py` with 13 audit checks and the v3.9 references catalogue parser, cited-by walker, handle resolver, and slug helper. v4.0's cluster rename will touch ~270 cross-references plus all four Python files; without unit tests the only safety net is the same integration check (does the build produce a clean site?), which catches *whether something broke* but not *what*. The v3.9 FILLED-review fold-in is the recent reminder of why per-function tests pay off: wrong DOIs, phantom catalogue entries, and unresolved handles that per-function tests on `parse.parse_references` / `find_inline_handles` / `build_cited_by` would have caught immediately.

---

## Scope

### `taxonomy/tests/test_parse.py`

Lowest-level dependency; benefits most from unit tests.

- `parse_all_metrics()` — fixture catalogue with 5–10 metrics across 2–3 group files; assertions on metric count, ref-ID parsing, dimension-table parsing, applicability annotation
- `parse_references()` — fixture `_references.md` with 3–5 entries; assertions on Title / Publisher / URL / Archive / Retrieved field parsing, description capture, `is_archived` property
- `find_inline_handles()` — fixture text with handles in: heading line (excluded), fenced code block (excluded), backtick-wrapped (excluded), image link (`![alt](#anchor)` — excluded), inline `[Handle]` in prose (included), inline link `[label](url)` (excluded). Assertions on returned list (with multiplicity, since back-reference frequency may matter for a future iteration)
- `build_cited_by()` — small two-file fixture catalogue; assertions on the returned `{handle: [files]}` map
- `populate_cited_by()` — fixture `_references.md` with the `Cited-by: _(auto-generated)_` placeholder; assertions on substituted output with realistic catalogue
- `ref_id_to_anchor()` — quick assertion: `TP.SN-5 → tp-sn-5`, `HL.HF-3a → hl-hf-3a`, `GV.PD-10 → gv-pd-10`

### `taxonomy/tests/test_audit.py`

Each of the 13 check functions tested with *both* a passing and a failing fixture. Catches regressions where a check accidentally stops detecting its target invariant — the silent-regression case unit tests are the only way to catch.

Functions to test:
- `check_prefixes`
- `check_numbering`
- `check_tier_totals`
- `check_see_also_resolves`
- `check_applicability_presence`
- `check_applicability_totals`
- `check_maturity_values`
- `check_source_presence`
- `check_tier1_quickref`
- `check_tightening_pattern`
- `check_threshold_provenance`
- `check_metric_cross_references`
- `check_reference_handles_resolve`
- `check_archive_present`
- `check_retrieved_date_format`

Each test: pass a tiny in-memory `metrics_by_file` (or `_references.md` fixture) shaped to either pass cleanly or trip exactly one finding; assert the returned `Finding` list (length + category + severity).

### `taxonomy/tests/test_build.py`

- `build_monolithic_md()` — small assembly fixture (3–4 source files); assertions on file ordering, `{{TAXONOMY_VERSION}}` / `{{TAXONOMY_DATE}}` substitution, `Cited-by:` placeholder substitution
- CSV / JSON download shape — assertions on column presence (against `CSV_COLUMNS`), row count match, `part_name` field present, `version` field carries `parse.TAXONOMY_VERSION`

### `taxonomy/tests/test_build_site.py`

- `rewrite_anchors()` — fixture text with same-page anchors (left bare), cross-page metric anchors (rewritten to `<page>.md#slug`), section-level anchors (rewritten via `ANCHOR_REWRITES`)
- `rewrite_external_links()` — `CHANGELOG.md` → `changelog.md`, `README.md` → GitHub blob URL, archive paths → GitHub blob URLs
- `link_tier1_quickref()` — fixture with bold metric names + non-metric bold phrases; assertion that metric names become `[`REF-ID` **Name**](page#slug)` and non-metric bolds are untouched
- `add_metric_anchors()` — fixture `### TP.SN-5 🟢 Hallucination Rate` heading; assertion of `{ #tp-sn-5 }` injection
- `_metric_name_index()` and `_metric_slug_to_page()` cache correctness — assert second call returns same dict object (cache hit)

### `taxonomy/tests/test_snapshot.py`

Smoke-test only; the real Wayback API isn't testable in CI.

- Mock `urllib.request.urlopen` to return a canned 200 response with a fake snapshot URL
- Assert `snapshot.py` reads the catalogue, finds entries needing snapshots, calls SPN once per entry, writes the fake snapshot URL back into the catalogue
- One failure-path test: mocked 401 from SPN; assert the entry's `Archive:` field is left untouched and the script reports the error count

---

## Test framework decisions

- **`pytest`** — pip-installable, integrates with `uv`, no fixtures-as-files complexity for a small suite.
- **Fixture style: inline string fixtures inside each test.** Smallest scope, easiest to understand. If fixtures grow to need reuse (likely after 5–10 tests), promote to `taxonomy/tests/fixtures/` directory with hand-curated `.md` files. **Do not** introduce `hypothesis` or generative testing — overkill for a documentation-first repo.
- **Coverage measurement: NOT a percentage target.** Coverage as a metric drives the wrong behaviour in a small focused suite. Aim for: every audit check has both a passing and a failing test; every public function in parse / build / build_site that anyone calls more than once has a test. Audit yourself by reading the test file, not by running coverage.
- **Mocking: stdlib `unittest.mock` only.** Already adequate for the one HTTP-mocking case (`tools/snapshot.py`); no `responses` / `httpretty` / `pytest-mock` needed.

---

## Phasing

Single release. Three commits expected:

1. **Phase 0 — Setup.** Add `pytest` to `pyproject.toml` `[project.optional-dependencies]` as a `dev` extra. Update `uv.lock`. Update CI (`.github/workflows/site.yml`) to run `uv run pytest` after `uv run python taxonomy/audit.py`. Verify CI green with zero tests yet.

2. **Phase 1 — `test_parse.py` + `test_audit.py`.** The bulk of the value: parse.py is the lowest-level dependency, audit.py is where the silent-regression risk lives. ~25–30 tests across the two files.

3. **Phase 2 — `test_build.py` + `test_build_site.py` + `test_snapshot.py` + release wrap.** The page-rendering layer. ~15–20 tests. Plus CHANGELOG entry, version bump (`v3.9.1`), tag.

---

## Critical files

- `pyproject.toml` — pytest dev dependency
- `uv.lock` — regenerated
- `.github/workflows/site.yml` — CI integration
- `taxonomy/tests/__init__.py` — created (empty)
- `taxonomy/tests/test_parse.py` — created
- `taxonomy/tests/test_audit.py` — created
- `taxonomy/tests/test_build.py` — created
- `taxonomy/tests/test_build_site.py` — created
- `taxonomy/tests/test_snapshot.py` — created
- `CHANGELOG.md` — v3.9.1 entry
- `README.md` — version bump (only the banner / current-draft / footer date stamps); developer section gets a "running tests" line
- `taxonomy/parse.py` — `TAXONOMY_VERSION` → `v3.9.1`, `TAXONOMY_DATE` → release date
- `pyproject.toml` (second edit) — version → `3.9.1`

---

## Counts after v3.9.1

No metric content changes. No tier shifts. No new metrics. Counts unchanged at 218 / 43-96-79. New: ~40 tests under `taxonomy/tests/`; CI runs them on every push.

---

## Risks

- **Test-fixture drift.** Inline string fixtures will diverge from the real catalogue shape over time if not maintained. Mitigation: each fixture is small enough that a future change is easy to spot in PR review; if drift becomes a real cost, promote to `fixtures/` directory.
- **CI runtime increase.** ~40 tests in pytest at <1s each adds <1 minute to CI; the existing site build is the dominant cost. Acceptable.
- **Test against v3.9 shape vs v4.0 shape.** Tests written here are against v3.9 (Part-letter scheme). The v4.0 rename will update the tests as part of its sweep — flagged in v4.0 plan as a Phase 1 deliverable. The change is mostly mechanical (rename `part-a/audio-capture.md` → `tp/audio-capture.md` in fixture paths).

---

## Open questions to settle at Phase 0

1. **CI: per-push or per-merge?** Default: per-push since the repo is small and CI is fast.
2. **Mock framework: `unittest.mock` or `pytest-mock`?** Default: `unittest.mock` (stdlib, no extra dep).
3. **Linting: do we add `ruff` / `pyright` while we're at it?** Default: **no** — out of scope. If we add static analysis, it's a separate item.
