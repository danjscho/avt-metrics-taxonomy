"""Unit tests for taxonomy/audit.py.

One pair of tests per check function: one fixture that should pass cleanly
(zero findings of the relevant category), one fixture that should trip the
check (returns the expected finding category).

Catches the silent-regression case where a check accidentally stops
detecting its target invariant — integration tests can't see this because
the real catalogue currently passes every check.
"""
from __future__ import annotations

import pathlib
import sys
from textwrap import dedent

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import audit  # noqa: E402
import parse  # noqa: E402


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_metric(
    ref_id: str = "TP.AC-1",
    name: str = "Test Metric",
    tier: int = 1,
    file: str = "tp/audio-capture.md",
    line: int = 1,
    dimensions: dict | None = None,
    body: str = "",
) -> audit.Metric:
    return audit.Metric(
        ref_id=ref_id,
        name=name,
        tier=tier,
        file=file,
        line=line,
        dimensions=dimensions or {},
        body=body,
    )


def _categories(findings: list[audit.Finding]) -> set[str]:
    return {f.category for f in findings}


# ---------------------------------------------------------------------------
# check_prefixes
# ---------------------------------------------------------------------------


class TestCheckPrefixes:
    def test_pass(self, monkeypatch):
        monkeypatch.setattr(
            audit,
            "GROUP_FILES",
            {"tp/audio-capture.md": {"prefix": "TP.AC", "label": "Audio"}},
        )
        m = _make_metric(ref_id="TP.AC-1", file="tp/audio-capture.md")
        findings = audit.check_prefixes({"tp/audio-capture.md": [m]})
        assert findings == []

    def test_fail(self, monkeypatch):
        monkeypatch.setattr(
            audit,
            "GROUP_FILES",
            {"tp/audio-capture.md": {"prefix": "TP.AC", "label": "Audio"}},
        )
        m = _make_metric(ref_id="GV.PD-1", file="tp/audio-capture.md")
        findings = audit.check_prefixes({"tp/audio-capture.md": [m]})
        assert len(findings) == 1
        assert findings[0].category == "prefix-mismatch"
        assert findings[0].severity == "ERROR"


# ---------------------------------------------------------------------------
# check_numbering
# ---------------------------------------------------------------------------


class TestCheckNumbering:
    def test_pass_consecutive(self, monkeypatch, tmp_path):
        # Empty retired-ids file (no skips) + consecutive numbering.
        monkeypatch.setattr(audit, "ROOT", tmp_path)
        monkeypatch.setattr(
            audit,
            "GROUP_FILES",
            {"tp/audio-capture.md": {"prefix": "TP.AC", "label": "Audio"}},
        )
        ms = [
            _make_metric(ref_id="TP.AC-1", file="tp/audio-capture.md"),
            _make_metric(ref_id="TP.AC-2", file="tp/audio-capture.md"),
            _make_metric(ref_id="TP.AC-3", file="tp/audio-capture.md"),
        ]
        findings = audit.check_numbering({"tp/audio-capture.md": ms})
        assert "numbering-gap" not in _categories(findings)

    def test_fail_with_gap(self, monkeypatch, tmp_path):
        monkeypatch.setattr(audit, "ROOT", tmp_path)
        monkeypatch.setattr(
            audit,
            "GROUP_FILES",
            {"tp/audio-capture.md": {"prefix": "TP.AC", "label": "Audio"}},
        )
        # 1, 2, 4 — gap at 3 with no retired-ids file present
        ms = [
            _make_metric(ref_id="TP.AC-1", file="tp/audio-capture.md"),
            _make_metric(ref_id="TP.AC-2", file="tp/audio-capture.md"),
            _make_metric(ref_id="TP.AC-4", file="tp/audio-capture.md"),
        ]
        findings = audit.check_numbering({"tp/audio-capture.md": ms})
        assert "numbering-gap" in _categories(findings)


# ---------------------------------------------------------------------------
# check_tier_totals
# ---------------------------------------------------------------------------


class TestCheckTierTotals:
    def test_pass(self):
        # check_tier_totals enforces specific tier counts; we feed exactly the
        # shape it expects (58 / 99 / 79 as of v5.4.0 mints).
        ms = (
            [_make_metric(ref_id=f"TP.AC-{i}", tier=1) for i in range(1, 59)]
            + [_make_metric(ref_id=f"TP.AC-{i}", tier=2) for i in range(59, 158)]
            + [_make_metric(ref_id=f"TP.AC-{i}", tier=3) for i in range(158, 237)]
        )
        findings = audit.check_tier_totals(ms)
        assert findings == []

    def test_fail(self):
        # Wrong tier-1 count → finding
        ms = [_make_metric(tier=1)] * 5
        findings = audit.check_tier_totals(ms)
        assert len(findings) >= 1
        assert findings[0].severity == "ERROR"


# ---------------------------------------------------------------------------
# check_applicability_presence
# ---------------------------------------------------------------------------


class TestCheckApplicabilityPresence:
    def test_pass(self):
        m = _make_metric(dimensions={"Applicability": "AVT-Specific"})
        assert audit.check_applicability_presence([m]) == []

    def test_fail_missing(self):
        m = _make_metric(dimensions={})
        findings = audit.check_applicability_presence([m])
        assert "missing-applicability" in _categories(findings)

    def test_fail_invalid_value(self):
        m = _make_metric(dimensions={"Applicability": "Made-Up-Category"})
        findings = audit.check_applicability_presence([m])
        # Either applicability-missing or applicability-invalid — both
        # indicate the check did its job
        assert findings  # at least one finding


# ---------------------------------------------------------------------------
# check_maturity_values
# ---------------------------------------------------------------------------


class TestCheckMaturityValues:
    def test_pass(self):
        m = _make_metric(dimensions={"Maturity": "Established"})
        assert audit.check_maturity_values([m]) == []

    def test_fail_invalid_value(self):
        m = _make_metric(dimensions={"Maturity": "Vintage"})
        findings = audit.check_maturity_values([m])
        assert findings
        assert findings[0].severity == "ERROR"


# ---------------------------------------------------------------------------
# check_source_presence
# ---------------------------------------------------------------------------


class TestCheckSourcePresence:
    def test_pass(self):
        m = _make_metric(dimensions={"Source": "[DCB0129]"})
        assert audit.check_source_presence([m]) == []

    def test_fail_missing(self):
        m = _make_metric(dimensions={})
        findings = audit.check_source_presence([m])
        assert findings


# ---------------------------------------------------------------------------
# check_reference_handles_resolve
# ---------------------------------------------------------------------------


class TestCheckReferenceHandlesResolve:
    def test_pass(self, tmp_path, monkeypatch):
        # Catalogue has DCB0129; metric file cites [DCB0129] → resolves.
        (tmp_path / "_references.md").write_text(
            "### DCB0129\n\n- **Title:** X\n- **URL:** https://example.com\n"
        )
        (tmp_path / "part-a").mkdir()
        (tmp_path / "part-a" / "audio-capture.md").write_text("Refs [DCB0129].")
        monkeypatch.setattr(parse, "ROOT", tmp_path)
        monkeypatch.setattr(audit, "ROOT", tmp_path)

        findings = audit.check_reference_handles_resolve()
        assert all(f.category != "unresolved-reference-handle" for f in findings)

    def test_fail_unresolved(self, tmp_path, monkeypatch):
        # Catalogue is empty, but metric file cites [DCB0129] in pilot scope
        # (standards-mapping is a pilot-scope file → ERROR not INFO).
        (tmp_path / "_references.md").write_text(
            "### Other-Handle\n\n- **Title:** X\n- **URL:** https://example.com\n"
        )
        (tmp_path / "_standards-mapping.md").write_text("Refs [DCB0129].")
        monkeypatch.setattr(parse, "ROOT", tmp_path)
        monkeypatch.setattr(audit, "ROOT", tmp_path)

        findings = audit.check_reference_handles_resolve()
        assert any(f.category == "unresolved-reference-handle" for f in findings)


# ---------------------------------------------------------------------------
# check_archive_present
# ---------------------------------------------------------------------------


class TestCheckArchivePresent:
    def test_pass_with_real_archive(self, tmp_path, monkeypatch):
        (tmp_path / "_references.md").write_text(
            "### DCB0129\n\n"
            "- **URL:** https://example.com/dcb0129\n"
            "- **Archive:** https://web.archive.org/web/2026/example.com/dcb0129\n"
            "- **Retrieved:** 2026-04-15\n"
        )
        monkeypatch.setattr(parse, "ROOT", tmp_path)
        findings = audit.check_archive_present()
        assert all(f.category != "reference-archive-pending" for f in findings)
        assert all(f.category != "reference-url-pending" for f in findings)

    def test_fail_url_pending(self, tmp_path, monkeypatch):
        (tmp_path / "_references.md").write_text(
            "### DCB0129\n\n- **URL:** _(pending v3.9 Phase 2 follow-up)_\n"
        )
        monkeypatch.setattr(parse, "ROOT", tmp_path)
        findings = audit.check_archive_present()
        assert any(f.category == "reference-url-pending" for f in findings)

    def test_fail_archive_pending(self, tmp_path, monkeypatch):
        # URL real but Archive: still placeholder
        (tmp_path / "_references.md").write_text(
            "### DCB0129\n\n"
            "- **URL:** https://example.com/dcb0129\n"
            "- **Archive:** _(Phase 1 — pending snapshot.py)_\n"
        )
        monkeypatch.setattr(parse, "ROOT", tmp_path)
        findings = audit.check_archive_present()
        assert any(f.category == "reference-archive-pending" for f in findings)


# ---------------------------------------------------------------------------
# check_retrieved_date_format
# ---------------------------------------------------------------------------


class TestCheckRetrievedDateFormat:
    def test_pass_iso(self, tmp_path, monkeypatch):
        (tmp_path / "_references.md").write_text(
            "### DCB0129\n\n"
            "- **URL:** https://example.com\n"
            "- **Retrieved:** 2026-04-15\n"
        )
        monkeypatch.setattr(parse, "ROOT", tmp_path)
        findings = audit.check_retrieved_date_format()
        assert all(f.category != "reference-retrieved-format" for f in findings)

    def test_fail_non_iso(self, tmp_path, monkeypatch):
        # April 15, 2026 — human-readable, not ISO-8601
        (tmp_path / "_references.md").write_text(
            "### DCB0129\n\n"
            "- **URL:** https://example.com\n"
            "- **Retrieved:** April 15, 2026\n"
        )
        monkeypatch.setattr(parse, "ROOT", tmp_path)
        findings = audit.check_retrieved_date_format()
        assert any(f.category == "reference-retrieved-format" for f in findings)

    def test_pass_empty_retrieved_skipped(self, tmp_path, monkeypatch):
        # Empty Retrieved: field — check_archive_present surfaces missing,
        # check_retrieved_date_format skips silently.
        (tmp_path / "_references.md").write_text(
            "### DCB0129\n\n- **URL:** https://example.com\n"
        )
        monkeypatch.setattr(parse, "ROOT", tmp_path)
        findings = audit.check_retrieved_date_format()
        assert all(f.category != "reference-retrieved-format" for f in findings)


class TestCheckCrosscutRefIdsResolve:
    def _write_metric_file(self, tmp_path, metrics):
        for ref_id, name in metrics:
            cluster_dir = tmp_path / ref_id.split(".")[0].lower()
            cluster_dir.mkdir(exist_ok=True)
            (cluster_dir / "stub.md").write_text(
                f"### {ref_id} 🟢 {name}\n\n"
                "| Dimension | Value |\n|---|---|\n"
                "| **Reference** | " + ref_id + " |\n"
                "| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |\n"
            )

    def test_pass_when_all_ref_ids_resolve(self, tmp_path, monkeypatch):
        # Set up tmp ROOT with one valid metric and one cross-cutting
        # file that references it.
        monkeypatch.setattr(audit, "ROOT", tmp_path)
        (tmp_path / "_standards-mapping.md").write_text(
            "| 1 | Some requirement | TP.AC-1 SNR Monitoring | 🟢 1 |\n"
        )
        (tmp_path / "_retired-ids.md").write_text(
            "# Retired\n"
        )
        # Valid metric in the catalogue (passed in directly)
        valid = parse.Metric(
            ref_id="TP.AC-1",
            name="SNR Monitoring",
            tier=2,
            cluster="TP",
            group="Audio Capture",
            group_file="tp/audio-capture.md",
            heading_line=1,
        )
        findings = audit.check_crosscut_ref_ids_resolve([valid])
        assert findings == []

    def test_flags_unresolved_ref_id_as_info(self, tmp_path, monkeypatch):
        monkeypatch.setattr(audit, "ROOT", tmp_path)
        (tmp_path / "_standards-mapping.md").write_text(
            "| 1 | Future requirement | TP.SN-99 Future Metric | 🟢 1 |\n"
        )
        (tmp_path / "_retired-ids.md").write_text("# Retired\n")
        valid = parse.Metric(
            ref_id="TP.AC-1",
            name="SNR Monitoring",
            tier=2,
            cluster="TP",
            group="Audio Capture",
            group_file="tp/audio-capture.md",
            heading_line=1,
        )
        findings = audit.check_crosscut_ref_ids_resolve([valid])
        assert len(findings) == 1
        assert findings[0].severity == "INFO"
        assert findings[0].category == "crosscut-ref-id-unresolved"
        assert "TP.SN-99" in findings[0].message

    def test_tolerates_retired_id(self, tmp_path, monkeypatch):
        monkeypatch.setattr(audit, "ROOT", tmp_path)
        (tmp_path / "_standards-mapping.md").write_text(
            "| 1 | Lineage discussion | retired TP.SN-8 (folded) | — |\n"
        )
        # Retired ID listed in _retired-ids.md
        (tmp_path / "_retired-ids.md").write_text(
            "| Retired ID |\n|---|\n| TP.SN-8 |\n"
        )
        findings = audit.check_crosscut_ref_ids_resolve([])
        assert findings == []
