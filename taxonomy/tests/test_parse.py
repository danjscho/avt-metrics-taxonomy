"""Unit tests for taxonomy/parse.py.

Tests focus on the parsing surface (find_inline_handles, ref_id_to_anchor,
populate_cited_by) and the catalogue parser. Where a function reads files
from disk via the module-level `ROOT` constant, we either use small
inline-string fixtures fed through helpers or monkeypatch ROOT to point at
a tmp_path.
"""
from __future__ import annotations

import pathlib
import sys
from textwrap import dedent

# Make `taxonomy/` importable so tests can `import parse`.
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import parse  # noqa: E402


# ---------------------------------------------------------------------------
# ref_id_to_anchor
# ---------------------------------------------------------------------------


class TestRefIdToAnchor:
    def test_simple(self):
        assert parse.ref_id_to_anchor("TP.SN-5") == "tp-sn-5"

    def test_subpart(self):
        assert parse.ref_id_to_anchor("HL.HF-3a") == "hl-hf-3a"

    def test_two_digit(self):
        assert parse.ref_id_to_anchor("GV.PD-10") == "gv-pd-10"

    def test_already_lower(self):
        # Idempotent on lower-case input
        assert parse.ref_id_to_anchor("tp.sn-5") == "tp-sn-5"


# ---------------------------------------------------------------------------
# find_inline_handles — purely text-based, no fixtures needed
# ---------------------------------------------------------------------------


class TestFindInlineHandles:
    def test_simple_inline_handle(self):
        text = "See [DCB0129] for the safety case."
        assert parse.find_inline_handles(text) == ["DCB0129"]

    def test_multiple_handles(self):
        text = "Refs: [UK-GDPR] Article 5 and [NHSE-IG-Guidance-2026-03]."
        assert parse.find_inline_handles(text) == ["UK-GDPR", "NHSE-IG-Guidance-2026-03"]

    def test_excludes_image_link(self):
        text = "Image: ![alt](#anchor) and prose [DCB0129]."
        assert parse.find_inline_handles(text) == ["DCB0129"]

    def test_excludes_inline_link(self):
        text = "[label](url) and bare [DCB0129]"
        assert parse.find_inline_handles(text) == ["DCB0129"]

    def test_excludes_headings(self):
        text = "# [DCB0129] in heading\n\nbut [UK-GDPR] in prose"
        assert parse.find_inline_handles(text) == ["UK-GDPR"]

    def test_excludes_fenced_code_block(self):
        text = dedent(
            """\
            outside [DCB0129]
            ```
            inside [UK-GDPR]
            ```
            after [ICO]
            """
        )
        result = parse.find_inline_handles(text)
        assert "DCB0129" in result
        assert "ICO" in result
        assert "UK-GDPR" not in result

    def test_excludes_tilde_fenced_code_block(self):
        text = dedent(
            """\
            outside [DCB0129]
            ~~~
            inside [UK-GDPR]
            ~~~
            after [ICO]
            """
        )
        result = parse.find_inline_handles(text)
        assert "DCB0129" in result
        assert "ICO" in result
        assert "UK-GDPR" not in result

    def test_excludes_inline_code_span(self):
        text = "Source: `[UK-GDPR]` is shown as code; [DCB0129] is real."
        assert parse.find_inline_handles(text) == ["DCB0129"]

    def test_counts_repetitions(self):
        # The function returns a list, not a set — same handle cited twice
        # should appear twice (used for cited-by frequency in a future iteration).
        text = "First [DCB0129], then [DCB0129] again."
        assert parse.find_inline_handles(text) == ["DCB0129", "DCB0129"]

    def test_empty_text(self):
        assert parse.find_inline_handles("") == []

    def test_no_handles(self):
        assert parse.find_inline_handles("Plain prose with no handles.") == []


# ---------------------------------------------------------------------------
# parse_references — uses ROOT/_references.md; monkeypatch via tmp_path
# ---------------------------------------------------------------------------


CATALOGUE_FIXTURE = dedent(
    """\
    ## References

    ### DCB0129

    - **Title:** Clinical Risk Management
    - **Publisher:** NHS England
    - **Source-Type:** framework
    - **URL:** https://example.com/dcb0129
    - **Archive:** https://web.archive.org/web/2026/example.com/dcb0129
    - **Retrieved:** 2026-04-15
    - **Local-Mirror:** _(reserved)_
    - **Cited-by:** _(auto-generated)_

    Description prose for DCB0129.
    Continues across lines.

    ### UK-GDPR

    - **Title:** UK General Data Protection Regulation
    - **Publisher:** UK Statute
    - **Source-Type:** framework
    - **URL:** https://example.com/uk-gdpr
    - **Archive:** _(Phase 1 — pending snapshot.py)_
    - **Retrieved:** 2026-04-15
    - **Local-Mirror:** _(reserved)_
    - **Cited-by:** _(auto-generated)_

    Description for UK-GDPR.
    """
)


def _setup_catalogue(tmp_path, monkeypatch, catalogue_text=CATALOGUE_FIXTURE):
    """Set parse.ROOT to tmp_path with a fixture _references.md."""
    (tmp_path / "_references.md").write_text(catalogue_text)
    monkeypatch.setattr(parse, "ROOT", tmp_path)


class TestParseReferences:
    def test_parses_two_entries(self, tmp_path, monkeypatch):
        _setup_catalogue(tmp_path, monkeypatch)
        refs = parse.parse_references()
        assert set(refs.keys()) == {"DCB0129", "UK-GDPR"}

    def test_field_extraction(self, tmp_path, monkeypatch):
        _setup_catalogue(tmp_path, monkeypatch)
        refs = parse.parse_references()
        dcb = refs["DCB0129"]
        assert dcb.title == "Clinical Risk Management"
        assert dcb.publisher == "NHS England"
        assert dcb.source_type == "framework"
        assert dcb.url == "https://example.com/dcb0129"
        assert dcb.archive == "https://web.archive.org/web/2026/example.com/dcb0129"
        assert dcb.retrieved == "2026-04-15"

    def test_is_archived_property_true(self, tmp_path, monkeypatch):
        _setup_catalogue(tmp_path, monkeypatch)
        refs = parse.parse_references()
        # DCB0129 has a real http archive URL
        assert refs["DCB0129"].is_archived is True

    def test_is_archived_property_false_when_placeholder(self, tmp_path, monkeypatch):
        # UK-GDPR's archive field is the placeholder "(Phase 1 — pending snapshot.py)"
        _setup_catalogue(tmp_path, monkeypatch)
        refs = parse.parse_references()
        assert refs["UK-GDPR"].is_archived is False

    def test_description_capture(self, tmp_path, monkeypatch):
        _setup_catalogue(tmp_path, monkeypatch)
        refs = parse.parse_references()
        # The description prose between an entry's bullets and the next ###
        # heading should be captured (collapsed into ref.description).
        assert "Description prose for DCB0129" in refs["DCB0129"].description

    def test_empty_catalogue(self, tmp_path, monkeypatch):
        _setup_catalogue(tmp_path, monkeypatch, catalogue_text="## References\n\n")
        assert parse.parse_references() == {}

    def test_missing_catalogue_file(self, tmp_path, monkeypatch):
        # No _references.md exists at ROOT
        monkeypatch.setattr(parse, "ROOT", tmp_path)
        assert parse.parse_references() == {}


# ---------------------------------------------------------------------------
# populate_cited_by — text substitution; uses build_cited_by which walks files
# ---------------------------------------------------------------------------


class TestPopulateCitedBy:
    def test_substitution_replaces_placeholder(self, tmp_path, monkeypatch):
        # Set up a tiny ROOT with a _references.md and one metric file
        # that cites a handle. build_cited_by() will walk the metric file
        # and find the citation; populate_cited_by then substitutes.
        (tmp_path / "_references.md").write_text(
            "### DCB0129\n\n- **Title:** X\n- **Cited-by:** _(auto-generated)_\n"
        )
        # GROUP_FILES uses keys like "tp/audio-capture.md"; we need at least
        # one file in that shape that contains a [DCB0129] citation.
        # Build a minimal GROUP_FILES override.
        (tmp_path / "tp").mkdir()
        (tmp_path / "tp" / "audio-capture.md").write_text(
            "## Audio capture\n\nUses [DCB0129] for the safety case."
        )
        monkeypatch.setattr(parse, "ROOT", tmp_path)
        monkeypatch.setattr(
            parse,
            "GROUP_FILES",
            {"tp/audio-capture.md": {"cluster": "TP", "group": "Audio capture"}},
        )

        text = "### DCB0129\n\n- **Title:** X\n- **Cited-by:** _(auto-generated)_\n"
        result = parse.populate_cited_by(text)
        assert "_(auto-generated)_" not in result
        assert "tp/audio-capture.md" in result

    def test_no_citations_emits_explicit_marker(self, tmp_path, monkeypatch):
        (tmp_path / "_references.md").write_text(
            "### Unused-Handle\n\n- **Title:** X\n- **Cited-by:** _(auto-generated)_\n"
        )
        monkeypatch.setattr(parse, "ROOT", tmp_path)
        monkeypatch.setattr(parse, "GROUP_FILES", {})

        text = "### Unused-Handle\n\n- **Title:** X\n- **Cited-by:** _(auto-generated)_\n"
        result = parse.populate_cited_by(text)
        assert "_(no citations found in source)_" in result


# ---------------------------------------------------------------------------
# build_cited_by — walks ROOT for inline handles
# ---------------------------------------------------------------------------


class TestBuildCitedBy:
    def test_walks_group_files_and_cross_cutting(self, tmp_path, monkeypatch):
        (tmp_path / "tp").mkdir()
        (tmp_path / "tp" / "audio-capture.md").write_text(
            "Uses [DCB0129] and [UK-GDPR]."
        )
        (tmp_path / "_standards-mapping.md").write_text("Refs [UK-GDPR].")
        monkeypatch.setattr(parse, "ROOT", tmp_path)
        monkeypatch.setattr(
            parse,
            "GROUP_FILES",
            {"tp/audio-capture.md": {"cluster": "TP", "group": "Audio capture"}},
        )

        cited = parse.build_cited_by()
        assert set(cited.keys()) == {"DCB0129", "UK-GDPR"}
        assert cited["DCB0129"] == ["tp/audio-capture.md"]
        assert cited["UK-GDPR"] == ["_standards-mapping.md", "tp/audio-capture.md"]

    def test_excludes_references_md_self_citations(self, tmp_path, monkeypatch):
        # _references.md is the catalogue itself; its intra-catalogue cross-refs
        # are not citations in the bibliographic sense.
        (tmp_path / "_references.md").write_text("Self-mentions [DCB0129].")
        monkeypatch.setattr(parse, "ROOT", tmp_path)
        monkeypatch.setattr(parse, "GROUP_FILES", {})

        cited = parse.build_cited_by()
        # _references.md should not be in any citing-files list
        for files in cited.values():
            assert "_references.md" not in files
