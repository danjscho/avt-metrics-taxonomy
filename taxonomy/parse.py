"""Shared parser for the AVT Metrics Taxonomy source files.

Used by `build.py` (to emit CSV/JSON alongside the monolithic Markdown),
by `audit.py` (single invariant surface), and later by `build_site.py`
(to generate per-standard, per-principle, per-applicability pages).

Do not author structured data outside the source files — this parser
is the single route by which in-prose tables become structured data.
"""

from __future__ import annotations

import pathlib
import re
from collections import Counter
from dataclasses import dataclass, field

ROOT = pathlib.Path(__file__).parent

# Canonical group file list: path -> {prefix, part, group name}.
# Matches the build.py order within each part.
GROUP_FILES: dict[str, dict[str, str]] = {
    "part-a/audio-capture.md":                 {"prefix": "TP.AC",  "part": "A", "group": "Audio Capture & Environment"},
    "part-a/asr-transcription.md":             {"prefix": "TP.ASR", "part": "A", "group": "ASR / Transcription"},
    "part-a/diarisation.md":                   {"prefix": "TP.DI",  "part": "A", "group": "Diarisation"},
    "part-a/summarisation-nlp.md":             {"prefix": "TP.SN",  "part": "A", "group": "Summarisation / NLP"},
    "part-a/clinical-coding.md":               {"prefix": "TP.CC",  "part": "A", "group": "Clinical Coding"},
    "part-a/epr-write-back.md":                {"prefix": "TP.WB",  "part": "A", "group": "EPR Write-back"},
    "part-b/partial-pipeline.md":              {"prefix": "PI.PP",  "part": "B", "group": "Partial-Pipeline"},
    "part-b/end-to-end-pipeline.md":           {"prefix": "PI.E2E", "part": "B", "group": "End-to-End Pipeline"},
    "part-c/human-factors-workflow.md":        {"prefix": "HL.HF",  "part": "C", "group": "Human Factors & Workflow"},
    "part-d/patient-experience.md":            {"prefix": "IO.PX",  "part": "D", "group": "Patient Experience"},
    "part-d/fairness-equity.md":               {"prefix": "IO.FE",  "part": "D", "group": "Fairness & Equity"},
    "part-e/safety-governance.md":             {"prefix": "GV.SG",  "part": "E", "group": "Safety & Governance"},
    "part-e/nhs-compliance-regulatory.md":     {"prefix": "GV.CR",  "part": "E", "group": "NHS Compliance & Regulatory"},
    "part-e/security-adversarial-robustness.md": {"prefix": "GV.SC", "part": "E", "group": "Security & Adversarial Robustness"},
    "part-e/privacy-data-governance.md":       {"prefix": "GV.PD",  "part": "E", "group": "Privacy & Data Governance"},
    "part-e/operational.md":                   {"prefix": "GV.OP",  "part": "E", "group": "Operational"},
    "part-e/environmental-sustainability.md":  {"prefix": "GV.EN",  "part": "E", "group": "Environmental & Sustainability"},
    "part-e/training-competency.md":           {"prefix": "GV.TC",  "part": "E", "group": "Training & Competency"},
    "part-e/vendor-transparency-contractual.md": {"prefix": "GV.VT", "part": "E", "group": "Vendor Transparency & Contractual"},
    "part-f/meta-evaluation.md":               {"prefix": "ES.ME",  "part": "F", "group": "Meta-Evaluation"},
}

TIER_ICON_TO_NUM = {"🟢": 1, "🟡": 2, "🔵": 3}
TIER_NUM_TO_LABEL = {1: "Minimum Viable", 2: "Recommended", 3: "Advanced / Research"}

METRIC_HEADING = re.compile(
    r"^###\s+([A-Z]{2,3}\.[A-Z0-9]{2,3}-\d+)\s+([🟢🟡🔵])\s+(.+?)\s*$"
)
DIM_ROW = re.compile(r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|\s*$")


@dataclass
class Metric:
    ref_id: str
    name: str
    tier: int                          # 1 / 2 / 3
    part: str                          # A–F
    group: str                         # human-readable group name
    group_file: str                    # relative path, e.g. "part-a/audio-capture.md"
    heading_line: int                  # 1-indexed line number of `### ...` heading in group file
    dimensions: dict[str, str] = field(default_factory=dict)
    applicability: str | None = None   # populated by annotate_applicability()

    @property
    def tier_icon(self) -> str:
        return {1: "🟢", 2: "🟡", 3: "🔵"}[self.tier]

    @property
    def tier_label(self) -> str:
        return TIER_NUM_TO_LABEL[self.tier]

    @property
    def cadence(self) -> str:
        return self.dimensions.get("Measurement Cadence", "")

    @property
    def pipeline_layer(self) -> str:
        return self.dimensions.get("Pipeline Layer", "")

    @property
    def assurance_question(self) -> str:
        return self.dimensions.get("Assurance Question", "")

    @property
    def measurement_method(self) -> str:
        return self.dimensions.get("Measurement Method", "")

    @property
    def lifecycle_phases(self) -> str:
        return self.dimensions.get("Lifecycle Phases") or self.dimensions.get("Lifecycle Phase", "")

    @property
    def responsible_actors(self) -> str:
        return self.dimensions.get("Responsible Actors") or self.dimensions.get("Responsible Actor", "")

    @property
    def maturity(self) -> str:
        return self.dimensions.get("Maturity", "")

    @property
    def source(self) -> str:
        return self.dimensions.get("Source", "")


def parse_group_file(rel_path: str) -> list[Metric]:
    info = GROUP_FILES[rel_path]
    lines = (ROOT / rel_path).read_text().splitlines()
    metrics: list[Metric] = []

    i = 0
    while i < len(lines):
        m = METRIC_HEADING.match(lines[i])
        if not m:
            i += 1
            continue
        ref_id, icon, name = m.group(1), m.group(2), m.group(3).strip()
        heading_line = i + 1
        tier = TIER_ICON_TO_NUM[icon]

        # Scan forward to the next metric heading, collecting dimension rows.
        dims: dict[str, str] = {}
        j = i + 1
        while j < len(lines) and not METRIC_HEADING.match(lines[j]):
            dm = DIM_ROW.match(lines[j])
            if dm:
                dims[dm.group(1).strip()] = dm.group(2).strip()
            j += 1

        metrics.append(Metric(
            ref_id=ref_id,
            name=name,
            tier=tier,
            part=info["part"],
            group=info["group"],
            group_file=rel_path,
            heading_line=heading_line,
            dimensions=dims,
        ))
        i = j

    return metrics


def parse_all_metrics() -> list[Metric]:
    out: list[Metric] = []
    for rel_path in GROUP_FILES:
        out.extend(parse_group_file(rel_path))
    return out


# ---------------------------------------------------------------------------
# Applicability — parsed from _applicability.md "Full Classification" tables
# ---------------------------------------------------------------------------

_APPLICABILITY_ROW = re.compile(
    r"^\|\s*([A-Z]{2,3}\.[A-Z0-9]{2,3}-\d+)\s*\|\s*[^|]+\|\s*[^|]+\|\s*([^|]+?)\s*\|"
)


def parse_applicability() -> dict[str, str]:
    """Return a map of ref_id -> applicability label ('AVT-Specific' etc.)."""
    text = (ROOT / "_applicability.md").read_text()
    out: dict[str, str] = {}
    for line in text.splitlines():
        m = _APPLICABILITY_ROW.match(line)
        if m:
            out[m.group(1).strip()] = m.group(2).strip()
    return out


def annotate_applicability(metrics: list[Metric]) -> list[Metric]:
    idx = parse_applicability()
    for metric in metrics:
        metric.applicability = idx.get(metric.ref_id)
    return metrics


# ---------------------------------------------------------------------------
# Gaps — parsed from _gaps.md by origin section
# ---------------------------------------------------------------------------

@dataclass
class Gap:
    gap_id: str | None           # e.g. "Gap-RSET-A", "GV.CR-11", or None for RAI severity rows
    title: str
    origin: str                  # "rset-accepted" / "rset-deferred" / "ig" / "standards-*" / "rai-principle" / "rai-theme"
    tier: int | None             # 1 / 2 / 3 or None (RAI severity rows don't have a tier)
    severity: str | None         # "High" / "Medium" / "Low" or None
    source: str                  # source standard / audit reference
    notes: str                   # free-text rationale or cross-reference


_GAP_SECTIONS: list[tuple[str, str, str]] = [
    # (section anchor start, origin tag, source label)
    ("### 1a. Accepted — RSET", "rset-accepted", "RSET external review"),
    ("### 1b. Deferred — RSET", "rset-deferred", "RSET external review"),
    ("### 1c. Accepted — NHSE IG", "ig", "NHSE IG Mar-2026"),
    ("### 2a. MHRA SaMD", "standards-mhra", "MHRA SaMD / AIaMD"),
    ("### 2b. NICE Evidence Standards", "standards-nice-esf", "NICE ESF"),
    ("### 2c. FHIR UK Core", "standards-fhir-uk-core", "FHIR UK Core"),
    ("### 2d. CQC Assessment", "standards-cqc", "CQC Assessment"),
    ("### 2e. PSIRF", "standards-psirf", "PSIRF"),
    ("### 2f. PRSB", "standards-prsb", "PRSB"),
    ("### 2g. Caldicott", "standards-caldicott", "Caldicott Principles"),
    ("### 3a. By Playbook principle", "rai-principle", "DSIT AI Playbook"),
    ("### 3b. By ethical theme", "rai-theme", "Responsible AI ethical themes"),
]


def _section_slices(text: str) -> list[tuple[str, str, str, str]]:
    """Return [(origin, source, section_header, section_body)] for each tracked section."""
    out = []
    for header, origin, source in _GAP_SECTIONS:
        idx = text.find(header)
        if idx == -1:
            continue
        # Body runs until the next section marker or a higher-level heading.
        rest = text[idx + len(header):]
        # Next `### ` or `## ` heading ends the section.
        m = re.search(r"\n(#{2,3})\s", rest)
        body = rest[:m.start()] if m else rest
        out.append((origin, source, header, body))
    return out


_TIER_RE = re.compile(r"🟢\s*1|🟡\s*2|🔵\s*3")


def _parse_gap_row(cells: list[str], origin: str, source: str) -> Gap | None:
    """Interpret a gap table row. Column layout varies by section."""
    # Strip markdown-table artefacts.
    cells = [c.strip() for c in cells]
    if not cells or not any(cells):
        return None

    # Detect tier icon anywhere in the row.
    tier = None
    for c in cells:
        if "🟢" in c:
            tier = 1; break
        if "🟡" in c:
            tier = 2; break
        if "🔵" in c:
            tier = 3; break

    # Severity (RAI rows use High/Medium/Low).
    severity = None
    for c in cells:
        lc = c.lower()
        if lc in {"high", "medium", "low"}:
            severity = c
            break

    # For standards rows the first cell is a proposed ref ID (e.g. GV.CR-11).
    # For external-review rows the first cell is Gap-RSET-* / Gap-IG-*.
    # For RAI rows there's no gap ID — first cell is the principle/theme label.
    gap_id = None
    if cells and re.match(r"^(Gap-[A-Z]+-[A-Z0-9]+|[A-Z]{2,3}\.[A-Z0-9]{2,3}-\d+)$", cells[0]):
        gap_id = cells[0]

    # Title: for standards/external rows, column index 1. For RAI rows, column 1 is the gap itself.
    title_cell = cells[1] if len(cells) >= 2 else cells[0]

    # Notes: last cell is usually "cross-reference" or rationale.
    notes = cells[-1] if len(cells) >= 3 else ""

    # Filter out header rows masquerading as data (e.g. "Gap ID | Title | ...").
    if title_cell.lower() in {"title", "gap", "description"}:
        return None
    if gap_id is None and title_cell.lower().startswith("principle") or title_cell.lower().startswith("theme"):
        return None

    return Gap(
        gap_id=gap_id,
        title=title_cell,
        origin=origin,
        tier=tier,
        severity=severity,
        source=source,
        notes=notes,
    )


def parse_gaps() -> list[Gap]:
    path = ROOT / "_gaps.md"
    if not path.exists():
        return []
    text = path.read_text()

    gaps: list[Gap] = []
    for origin, source, _header, body in _section_slices(text):
        # Walk rows of any Markdown table inside this section body.
        for line in body.splitlines():
            line = line.strip()
            if not line.startswith("|"):
                continue
            # Skip header separator rows (|---|---|).
            if re.match(r"^\|\s*[:\-]+\s*(\|\s*[:\-]+\s*)+\|\s*$", line):
                continue
            # Split cells; drop empty leading/trailing cell from |..|..|..
            parts = [c for c in line.split("|")]
            # Trim first and last if empty
            if parts and parts[0].strip() == "":
                parts = parts[1:]
            if parts and parts[-1].strip() == "":
                parts = parts[:-1]
            parts = [c.strip() for c in parts]
            # Header row detection: contains "Gap ID" / "Proposed Ref" / "Principle" / "Theme"
            lower = [c.lower() for c in parts]
            if any(h in lower for h in ("gap id", "proposed ref", "principle", "theme")):
                continue
            gap = _parse_gap_row(parts, origin, source)
            if gap is not None:
                gaps.append(gap)

    return gaps


# ---------------------------------------------------------------------------
# Convenience
# ---------------------------------------------------------------------------

def summary() -> dict:
    metrics = annotate_applicability(parse_all_metrics())
    gaps = parse_gaps()
    tiers = Counter(m.tier for m in metrics)
    return {
        "metric_count": len(metrics),
        "tier_counts": {str(k): v for k, v in sorted(tiers.items())},
        "group_count": len(GROUP_FILES),
        "gap_count": len(gaps),
    }


if __name__ == "__main__":
    import json
    print(json.dumps(summary(), indent=2))
