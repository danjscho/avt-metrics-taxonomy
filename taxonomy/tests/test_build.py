"""Unit tests for taxonomy/build.py.

The build is mostly an assembly-and-write pipeline reading from disk. We
test the surfaces that are pure logic (template-token substitution, the
JSON payload shape, the CSV column list) and the integration-shaped
build_summary output via tmp-path-redirected DIST.
"""
from __future__ import annotations

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import build as build_mod  # noqa: E402
import parse  # noqa: E402


# ---------------------------------------------------------------------------
# _substitute_template_tokens (mirror of build_site's; tested separately
# because it's a different module-level constant table)
# ---------------------------------------------------------------------------


class TestBuildSubstituteTemplateTokens:
    def test_substitutes_version(self):
        text = "Version is {{TAXONOMY_VERSION}}."
        result = build_mod._substitute_template_tokens(text)
        assert "{{TAXONOMY_VERSION}}" not in result
        assert parse.TAXONOMY_VERSION in result

    def test_substitutes_date(self):
        text = "Date is {{TAXONOMY_DATE}}."
        result = build_mod._substitute_template_tokens(text)
        assert parse.TAXONOMY_DATE in result

    def test_no_tokens_unchanged(self):
        text = "Plain prose."
        assert build_mod._substitute_template_tokens(text) == text

    def test_substitutes_multiple_occurrences(self):
        text = "v{{TAXONOMY_VERSION}} on {{TAXONOMY_VERSION}}."
        result = build_mod._substitute_template_tokens(text)
        assert result.count(parse.TAXONOMY_VERSION) == 2


# ---------------------------------------------------------------------------
# CSV_COLUMNS — schema sanity
# ---------------------------------------------------------------------------


class TestCSVColumns:
    def test_has_expected_columns(self):
        # Schema invariants: ref_id and tier are always present; part_name
        # was added in v3.8.3; status is intentionally NOT a column (status
        # belongs in summary.json metadata, not per-row).
        cols = build_mod.CSV_COLUMNS
        assert "ref_id" in cols
        assert "name" in cols
        assert "tier" in cols
        assert "part" in cols
        assert "part_name" in cols
        assert "group" in cols
        assert "applicability" in cols
        assert "source" in cols

    def test_no_duplicates(self):
        assert len(build_mod.CSV_COLUMNS) == len(set(build_mod.CSV_COLUMNS))


# ---------------------------------------------------------------------------
# FILES — monolith assembly order
# ---------------------------------------------------------------------------


class TestFilesOrder:
    def test_header_first(self):
        # Monolith must start with _header.md so the version banner is at
        # the top of the assembled document.
        assert build_mod.FILES[0] == "_header.md"

    def test_prototype_status_after_header(self):
        # User-decided ordering: prototype status appears second so readers
        # encounter it immediately after the version banner.
        assert build_mod.FILES[1] == "_prototype-status.md"

    def test_references_after_part_f(self):
        # _references.md must come after part-f/* so the catalogue lives
        # at the end of the monolith (after Part F meta-evaluation).
        idx = build_mod.FILES.index("_references.md")
        last_part = max(
            i for i, name in enumerate(build_mod.FILES) if name.startswith("part-")
        )
        assert idx > last_part


# ---------------------------------------------------------------------------
# build_summary — payload shape (uses real parse.summary())
# ---------------------------------------------------------------------------


class TestBuildSummary:
    def test_status_field_present(self, tmp_path, monkeypatch):
        # Redirect DIST to a path under ROOT.parent so the print-line
        # inside build_summary (which calls path.relative_to(ROOT.parent))
        # doesn't blow up on tmp_path. We use a sub-dir of ROOT.parent
        # named after the test so it's deterministic and isolated.
        sandbox = build_mod.ROOT.parent / "_test_dist"
        sandbox.mkdir(exist_ok=True)
        monkeypatch.setattr(build_mod, "DIST", sandbox)
        try:
            build_mod.build_summary()
            payload = json.loads((sandbox / "summary.json").read_text())
            assert payload["status"] == "ai-coauthored-prototype-for-discussion"
            assert payload["version"] == parse.TAXONOMY_VERSION
        finally:
            (sandbox / "summary.json").unlink(missing_ok=True)
            sandbox.rmdir()

    def test_summary_carries_counts(self, tmp_path, monkeypatch):
        sandbox = build_mod.ROOT.parent / "_test_dist"
        sandbox.mkdir(exist_ok=True)
        monkeypatch.setattr(build_mod, "DIST", sandbox)
        try:
            build_mod.build_summary()
            payload = json.loads((sandbox / "summary.json").read_text())
            assert "metric_count" in payload
            assert "tier_counts" in payload
            assert "group_count" in payload
        finally:
            (sandbox / "summary.json").unlink(missing_ok=True)
            sandbox.rmdir()
