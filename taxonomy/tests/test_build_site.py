"""Unit tests for taxonomy/build_site.py.

Tests focus on the per-page text transformations that don't depend on the
full catalogue being parsed: rewrite_anchors, rewrite_external_links,
add_metric_anchors, _inject_changelog_dates_frontmatter,
_substitute_template_tokens.

The transformations that DO depend on a parsed catalogue
(link_tier1_quickref, rewrite_reference_handles) get fixture-backed tests
that monkeypatch the underlying _metric_name_index / _reference_handles
caches.
"""
from __future__ import annotations

import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import build_site  # noqa: E402
import parse  # noqa: E402


# ---------------------------------------------------------------------------
# rewrite_external_links
# ---------------------------------------------------------------------------


class TestRewriteExternalLinks:
    def test_changelog_rewrite(self):
        text = "See [CHANGELOG](CHANGELOG.md) for history."
        result = build_site.rewrite_external_links(text)
        assert result == "See [CHANGELOG](changelog.md) for history."

    def test_changelog_with_fragment(self):
        text = "See [v3.9](CHANGELOG.md#v39) entry."
        result = build_site.rewrite_external_links(text)
        assert result == "See [v3.9](changelog.md#v39) entry."

    def test_readme_rewrite_to_github_blob(self):
        text = "See [README](README.md)."
        result = build_site.rewrite_external_links(text)
        assert "github.com/danjscho/avt-metrics-taxonomy" in result
        assert "README.md" in result

    def test_archive_path_rewrite(self):
        text = "See [plan](archive/plans/plan-v3.7.md)."
        result = build_site.rewrite_external_links(text)
        assert "github.com" in result
        assert "archive/plans/plan-v3.7.md" in result

    def test_internal_md_link_left_alone(self):
        text = "See [other page](how-to-use.md)."
        # Not in EXTERNAL_LINK_REWRITES and not under archive/ — should be untouched
        assert build_site.rewrite_external_links(text) == text

    def test_image_link_not_matched(self):
        text = "Image: ![alt](some.png)"
        # PNG isn't a .md link; regex shouldn't match
        assert build_site.rewrite_external_links(text) == text


# ---------------------------------------------------------------------------
# add_metric_anchors
# ---------------------------------------------------------------------------


class TestAddMetricAnchors:
    def test_injects_anchor_for_tier1(self):
        text = "### TP.AC-1 🟢 Microphone Validation\n\nProse here."
        result = build_site.add_metric_anchors(text)
        assert "{ #tp-ac-1 }" in result
        assert "TP.AC-1" in result  # ref-id still visible

    def test_injects_anchor_for_tier2(self):
        text = "### HL.HF-3a 🟡 Edit Rate sub-part\n"
        result = build_site.add_metric_anchors(text)
        assert "{ #hl-hf-3a }" in result

    def test_no_match_for_h2(self):
        text = "## TP.AC-1 🟢 Wrong heading level"
        # Should not match — _METRIC_HEADING requires `### `
        result = build_site.add_metric_anchors(text)
        assert "{ #" not in result

    def test_no_match_for_non_metric_h3(self):
        text = "### Just a heading without ref-id"
        result = build_site.add_metric_anchors(text)
        assert "{ #" not in result


# ---------------------------------------------------------------------------
# _substitute_template_tokens
# ---------------------------------------------------------------------------


class TestSubstituteTemplateTokens:
    def test_substitutes_version(self):
        text = "Version is {{TAXONOMY_VERSION}}."
        result = build_site._substitute_template_tokens(text)
        assert "{{TAXONOMY_VERSION}}" not in result
        assert parse.TAXONOMY_VERSION in result

    def test_substitutes_date(self):
        text = "Date is {{TAXONOMY_DATE}}."
        result = build_site._substitute_template_tokens(text)
        assert "{{TAXONOMY_DATE}}" not in result
        assert parse.TAXONOMY_DATE in result

    def test_no_tokens_unchanged(self):
        text = "Plain prose."
        assert build_site._substitute_template_tokens(text) == text


# ---------------------------------------------------------------------------
# _inject_changelog_dates_frontmatter
# ---------------------------------------------------------------------------


class TestInjectChangelogDates:
    def test_injects_frontmatter_when_git_dates_available(self, monkeypatch):
        # Stub out _git_dates_for to return a known pair
        monkeypatch.setattr(
            build_site,
            "_git_dates_for",
            lambda _: ("2026-01-01T00:00:00+00:00", "2026-05-02T12:00:00+01:00"),
        )
        text = "# Changelog\n\nentries here.\n"
        result = build_site._inject_changelog_dates_frontmatter(text)
        assert result.startswith("---\n")
        assert "date:" in result
        assert "created: 2026-01-01T00:00:00+00:00" in result
        assert "updated: 2026-05-02T12:00:00+01:00" in result
        # Original content preserved after front-matter
        assert "# Changelog" in result
        assert "entries here." in result

    def test_returns_text_unchanged_when_git_unavailable(self, monkeypatch):
        monkeypatch.setattr(build_site, "_git_dates_for", lambda _: None)
        text = "# Changelog\n\nentries here.\n"
        assert build_site._inject_changelog_dates_frontmatter(text) == text


# ---------------------------------------------------------------------------
# rewrite_anchors — uses ANCHOR_REWRITES + metric slug index
# ---------------------------------------------------------------------------


class TestRewriteAnchors:
    def test_anchor_rewrite_to_other_page(self):
        # `applicability-classification` is in ANCHOR_REWRITES → applicability.md
        text = "See [applicability section](#applicability-classification)."
        result = build_site.rewrite_anchors(text, current_page="how-to-use.md")
        assert "applicability.md" in result

    def test_anchor_rewrite_skipped_on_target_page(self):
        # If we're already on applicability.md, the link to #applicability-classification
        # should stay bare (in-page anchor)
        text = "See [self](#applicability-classification)."
        result = build_site.rewrite_anchors(text, current_page="applicability.md")
        # rewrite_anchors should not redirect to the same page
        assert result == text

    def test_unknown_anchor_left_alone(self):
        text = "See [random](#random-anchor-not-in-rewrites)."
        result = build_site.rewrite_anchors(text, current_page="how-to-use.md")
        assert result == text


# ---------------------------------------------------------------------------
# link_tier1_quickref — needs catalogue; use stubbed metric index
# ---------------------------------------------------------------------------


class TestLinkTier1Quickref:
    def test_links_tier1_metric(self, monkeypatch):
        # Build a tiny stubbed index with one Tier-1 metric.
        stub_metric = parse.Metric(
            ref_id="TP.SN-5",
            name="Hallucination Rate",
            tier=1,
            part="A",
            group="Summarisation",
            group_file="part-a/summarisation-nlp.md",
            heading_line=1,
        )
        monkeypatch.setattr(
            build_site,
            "_metric_name_index",
            lambda: {"Hallucination Rate": stub_metric},
        )
        # SRC_GROUP_FILE_TO_PAGE needs to know where summarisation-nlp lives
        monkeypatch.setitem(
            build_site.SRC_GROUP_FILE_TO_PAGE,
            "part-a/summarisation-nlp.md",
            "groups/summarisation-nlp.md",
        )

        text = "- 🔄 **Hallucination Rate** - core safety metric"
        result = build_site.link_tier1_quickref(text)
        # Both ref-ID prefix and metric name end up in a link
        assert "`TP.SN-5`" in result
        assert "**Hallucination Rate**" in result
        assert "groups/summarisation-nlp.md#tp-sn-5" in result

    def test_skips_non_tier1_metric(self, monkeypatch):
        stub_metric = parse.Metric(
            ref_id="TP.SN-15",
            name="Some Tier 2",
            tier=2,
            part="A",
            group="Summarisation",
            group_file="part-a/summarisation-nlp.md",
            heading_line=1,
        )
        monkeypatch.setattr(
            build_site, "_metric_name_index", lambda: {"Some Tier 2": stub_metric}
        )
        text = "- **Some Tier 2** - prose"
        # Tier 2 is not Tier 1 — the bold phrase should be left untouched
        assert build_site.link_tier1_quickref(text) == text

    def test_skips_unknown_bold(self, monkeypatch):
        monkeypatch.setattr(build_site, "_metric_name_index", lambda: {})
        text = "- **Deployer** - actor subsection heading"
        assert build_site.link_tier1_quickref(text) == text

    def test_preserves_warning_suffix_outside_link(self, monkeypatch):
        stub_metric = parse.Metric(
            ref_id="TP.SN-5",
            name="Hallucination Rate",
            tier=1,
            part="A",
            group="Summarisation",
            group_file="part-a/summarisation-nlp.md",
            heading_line=1,
        )
        monkeypatch.setattr(
            build_site,
            "_metric_name_index",
            lambda: {"Hallucination Rate": stub_metric},
        )
        monkeypatch.setitem(
            build_site.SRC_GROUP_FILE_TO_PAGE,
            "part-a/summarisation-nlp.md",
            "groups/summarisation-nlp.md",
        )
        text = "- 🔄 **Hallucination Rate** ⚠️ - underspecified"
        result = build_site.link_tier1_quickref(text)
        # The ⚠️ should appear after the closing `)` of the link, not inside
        assert "**](groups/summarisation-nlp.md#tp-sn-5) ⚠️" in result
