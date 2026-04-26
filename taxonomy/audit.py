#!/usr/bin/env python3
"""Audit the AVT Metrics Taxonomy source for consistency violations.

Run: python taxonomy/audit.py
Exit 0 if clean, 1 if violations found.
"""

from __future__ import annotations

import pathlib
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field

ROOT = pathlib.Path(__file__).parent

# Part directory -> expected reference-ID prefix(es) used by metrics in that dir.
# Prefixes are observed from actual source; any mismatch is a violation.
GROUP_FILES = {
    "part-a/audio-capture.md": {
        "prefix": "TP.AC",
        "label": "Audio Capture & Environment",
    },
    "part-a/asr-transcription.md": {"prefix": "TP.ASR", "label": "ASR / Transcription"},
    "part-a/diarisation.md": {"prefix": "TP.DI", "label": "Diarisation"},
    "part-a/summarisation-nlp.md": {"prefix": "TP.SN", "label": "Summarisation & NLP"},
    "part-a/clinical-coding.md": {"prefix": "TP.CC", "label": "Clinical Coding"},
    "part-a/epr-write-back.md": {"prefix": "TP.WB", "label": "EPR Write-back"},
    "part-b/partial-pipeline.md": {"prefix": "PI.PP", "label": "Partial Pipeline"},
    "part-b/end-to-end-pipeline.md": {
        "prefix": "PI.E2E",
        "label": "End-to-End Pipeline",
    },
    "part-c/human-factors-workflow.md": {
        "prefix": "HL.HF",
        "label": "Human Factors & Workflow",
    },
    "part-d/patient-experience.md": {"prefix": "IO.PX", "label": "Patient Experience"},
    "part-d/fairness-equity.md": {"prefix": "IO.FE", "label": "Fairness & Equity"},
    "part-e/safety-governance.md": {"prefix": "GV.SG", "label": "Safety & Governance"},
    "part-e/nhs-compliance-regulatory.md": {
        "prefix": "GV.CR",
        "label": "NHS Compliance & Regulatory",
    },
    "part-e/security-adversarial-robustness.md": {
        "prefix": "GV.SC",
        "label": "Security & Adversarial Robustness",
    },
    "part-e/privacy-data-governance.md": {
        "prefix": "GV.PD",
        "label": "Privacy & Data Governance",
    },
    "part-e/operational.md": {"prefix": "GV.OP", "label": "Operational"},
    "part-e/environmental-sustainability.md": {
        "prefix": "GV.EN",
        "label": "Environmental & Sustainability",
    },
    "part-e/training-competency.md": {
        "prefix": "GV.TC",
        "label": "Training & Competency",
    },
    "part-e/vendor-transparency-contractual.md": {
        "prefix": "GV.VT",
        "label": "Vendor Transparency & Contractual",
    },
    "part-f/meta-evaluation.md": {"prefix": "ES.ME", "label": "Meta-Evaluation"},
}

TIER_ICON_TO_NUM = {"🟢": 1, "🟡": 2, "🔵": 3}
EXPECTED_TIER_TOTALS = {1: 43, 2: 94, 3: 79}
EXPECTED_APPLICABILITY = {
    "AVT-Specific": 48,
    "AVT-Contextualised": 77,
    "General Healthcare AI": 91,
}
EXPECTED_TOTAL = 216

# Heading form:  ### TP.AC-1 🟡 Signal-to-Noise Ratio (SNR) Monitoring
# Sub-parts (v3.7+) carry a single lowercase letter suffix: ### TP.SN-7a ...
METRIC_HEADING = re.compile(
    r"^###\s+([A-Z]{2,3}\.[A-Z0-9]{2,3}-\d+[a-z]?)\s+([🟢🟡🔵])\s+(.+?)\s*$"
)
REF_ROW = re.compile(
    r"^\|\s*\*\*Reference\*\*\s*\|\s*([A-Z]{2,3}\.[A-Z0-9]{2,3}-\d+[a-z]?)\s*\|"
)
SUBPART_REF_ID_RE = re.compile(r"^([A-Z]{2,3}\.[A-Z0-9]{2,3}-\d+)([a-z])$")
TIER_ROW = re.compile(r"^\|\s*\*\*Priority Tier\*\*\s*\|\s*([🟢🟡🔵])\s*Tier\s*(\d)")

# Dimension rows we expect in every metric table (8 core dimensions; "Reference" and optional extras are separate).
REQUIRED_DIMENSIONS = [
    "Priority Tier",
    "Measurement Cadence",
    "Pipeline Layer",
    "Assurance Question",
    "Measurement Method",
    "Lifecycle Phase",  # may appear as "Lifecycle Phase" or "Lifecycle Phases"
    "Responsible Actor",  # may appear as "Responsible Actor" or "Responsible Actors"
    "Maturity",
]


@dataclass
class Metric:
    ref_id: str
    name: str
    tier: int
    file: str
    line: int
    dimensions: dict = field(default_factory=dict)  # dim name -> raw value
    body: str = ""  # Full metric body from heading to next heading (for sub-block detection)


@dataclass
class Finding:
    severity: str  # "ERROR" or "WARN"
    category: str
    message: str
    location: str = ""

    def format(self) -> str:
        loc = f"  @ {self.location}" if self.location else ""
        return f"[{self.severity}] {self.category}: {self.message}{loc}"


def parse_group_file(rel_path: str) -> tuple[list[Metric], list[Finding]]:
    path = ROOT / rel_path
    lines = path.read_text().splitlines()
    metrics: list[Metric] = []
    findings: list[Finding] = []

    i = 0
    while i < len(lines):
        m = METRIC_HEADING.match(lines[i])
        if not m:
            i += 1
            continue
        ref_id, icon, name = m.group(1), m.group(2), m.group(3).strip()
        heading_line = i + 1  # 1-indexed
        tier_from_icon = TIER_ICON_TO_NUM[icon]

        # Scan forward to find the dimension table.
        dims: dict[str, str] = {}
        ref_in_table: str | None = None
        tier_in_table: int | None = None
        j = i + 1
        # Limit search window to the next metric heading.
        while j < len(lines) and not METRIC_HEADING.match(lines[j]):
            row = lines[j]
            rm = REF_ROW.match(row)
            if rm:
                ref_in_table = rm.group(1)
            tm = TIER_ROW.match(row)
            if tm:
                tier_in_table = int(tm.group(2))
            # Pull any `| **Name** | value |` row into dims
            dm = re.match(r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|\s*$", row)
            if dm:
                dims[dm.group(1).strip()] = dm.group(2).strip()
            j += 1

        # Checks
        if ref_in_table is None:
            findings.append(
                Finding(
                    "ERROR",
                    "missing-reference-row",
                    f"metric {ref_id} has no **Reference** row in its dimension table",
                    f"{rel_path}:{heading_line}",
                )
            )
        elif ref_in_table != ref_id:
            findings.append(
                Finding(
                    "ERROR",
                    "reference-mismatch",
                    f"heading says {ref_id} but table says {ref_in_table}",
                    f"{rel_path}:{heading_line}",
                )
            )

        if tier_in_table is None:
            findings.append(
                Finding(
                    "ERROR",
                    "missing-tier-row",
                    f"metric {ref_id} has no **Priority Tier** row",
                    f"{rel_path}:{heading_line}",
                )
            )
        elif tier_in_table != tier_from_icon:
            findings.append(
                Finding(
                    "ERROR",
                    "tier-mismatch",
                    f"heading icon says Tier {tier_from_icon} but table says Tier {tier_in_table}",
                    f"{rel_path}:{heading_line}",
                )
            )

        # Check dimension presence (allow plural variants)
        for dim in REQUIRED_DIMENSIONS:
            variants = [dim, dim + "s"]  # crude plural
            if not any(v in dims for v in variants):
                findings.append(
                    Finding(
                        "WARN",
                        "missing-dimension",
                        f"metric {ref_id} missing dimension '{dim}'",
                        f"{rel_path}:{heading_line}",
                    )
                )

        body = "\n".join(lines[i:j])

        metrics.append(
            Metric(
                ref_id=ref_id,
                name=name,
                tier=tier_from_icon,
                file=rel_path,
                line=heading_line,
                dimensions=dims,
                body=body,
            )
        )
        i = j

    return metrics, findings


def check_prefixes(metrics_by_file: dict[str, list[Metric]]) -> list[Finding]:
    findings: list[Finding] = []
    for rel_path, expected in GROUP_FILES.items():
        prefix = expected["prefix"]
        for m in metrics_by_file.get(rel_path, []):
            if not m.ref_id.startswith(prefix + "-"):
                findings.append(
                    Finding(
                        "ERROR",
                        "prefix-mismatch",
                        f"metric {m.ref_id} in {rel_path} does not start with expected prefix {prefix}-",
                        f"{rel_path}:{m.line}",
                    )
                )
    return findings


def load_retired_ids() -> set[str]:
    """Read taxonomy/_retired-ids.md and return the set of retired ref IDs.

    Format: any markdown table row in the file whose first cell is a valid
    ref ID (e.g. TP.SN-8). Header rows and prose are ignored.
    """
    path = ROOT / "_retired-ids.md"
    if not path.exists():
        return set()
    retired: set[str] = set()
    ref_id_re = re.compile(r"^\|\s*([A-Z]{2,3}\.[A-Z0-9]{2,3}-\d+[a-z]?)\s*\|")
    for line in path.read_text().splitlines():
        m = ref_id_re.match(line)
        if m:
            retired.add(m.group(1))
    return retired


def check_numbering(metrics_by_file: dict[str, list[Metric]]) -> list[Finding]:
    findings: list[Finding] = []
    retired_ids = load_retired_ids()
    for rel_path, metrics in metrics_by_file.items():
        prefix = GROUP_FILES[rel_path]["prefix"]
        # Capture base integer from each ref_id (parents and sub-parts share a base).
        # Sub-parts (TP.SN-7a) contribute their parent integer (7); the parent (TP.SN-7)
        # also contributes 7 — we de-dupe these for gap-checking but flag duplicate
        # *exact* IDs separately.
        nums_seen: list[tuple[int, Metric]] = []
        exact_ids_seen: list[str] = []
        for m in metrics:
            mnum = re.match(
                rf"^{re.escape(prefix)}-(\d+)([a-z]?)$", m.ref_id
            )  # prefix is literal, e.g. PI.E2E
            if not mnum:
                continue
            nums_seen.append((int(mnum.group(1)), m))
            exact_ids_seen.append(m.ref_id)
        # Duplicates: same exact ref_id (including suffix) appearing twice
        exact_counts = Counter(exact_ids_seen)
        for ref_id, count in exact_counts.items():
            if count > 1:
                locs = [f"{mm.file}:{mm.line}" for mm in metrics if mm.ref_id == ref_id]
                findings.append(
                    Finding(
                        "ERROR",
                        "duplicate-id",
                        f"{ref_id} appears {count} times",
                        "; ".join(locs),
                    )
                )
        # Gaps: integer in 1..max not present at all (neither as a flat ID nor as
        # a parent of any sub-part). Retired IDs (per _retired-ids.md) are
        # tolerated; their absence is expected.
        if nums_seen:
            expected = set(range(1, max(n for n, _ in nums_seen) + 1))
            actual = set(n for n, _ in nums_seen)
            for gap in sorted(expected - actual):
                gap_id = f"{prefix}-{gap}"
                # Allow the gap if any retired ID maps to this base integer.
                gap_is_retired = any(
                    r.startswith(f"{gap_id}") and (r == gap_id or r[len(gap_id)].isalpha())
                    for r in retired_ids
                )
                if gap_is_retired:
                    continue
                findings.append(
                    Finding(
                        "WARN",
                        "numbering-gap",
                        f"{gap_id} is missing (numbering not contiguous)",
                        rel_path,
                    )
                )
    return findings


def check_tier_totals(all_metrics: list[Metric]) -> list[Finding]:
    findings: list[Finding] = []
    counts = Counter(m.tier for m in all_metrics)
    for tier, expected in EXPECTED_TIER_TOTALS.items():
        actual = counts.get(tier, 0)
        if actual != expected:
            findings.append(
                Finding(
                    "ERROR",
                    "tier-total",
                    f"Tier {tier}: expected {expected}, found {actual}",
                    "_summary.md declares",
                )
            )
    total = sum(counts.values())
    if total != EXPECTED_TOTAL:
        findings.append(
            Finding(
                "ERROR",
                "metric-total",
                f"expected {EXPECTED_TOTAL} metrics total, found {total}",
            )
        )
    return findings


def check_see_also_resolves(all_metrics: list[Metric]) -> list[Finding]:
    """'See also' in italic sub-cluster intros references metric names, not IDs.
    Build a name index and verify each referenced name exists as a known metric.
    """
    findings: list[Finding] = []
    name_index = {m.name: m for m in all_metrics}
    # Index full name, base name (parens stripped), AND each parenthesised
    # abbreviation mapped back to its metric so "See also: Medical WER (M-WER)"
    # resolves to "Medical Word Error Rate (M-WER)" via the shared M-WER tag.
    normalised = {}
    abbrev_index: dict[str, Metric] = {}
    for m in all_metrics:
        normalised[m.name] = m
        stripped = re.sub(r"\s*\([^)]*\)\s*", "", m.name).strip()
        if stripped and stripped not in normalised:
            normalised[stripped] = m
        for abbr in re.findall(r"\(([^)]+)\)", m.name):
            abbr = abbr.strip()
            if abbr and abbr not in abbrev_index:
                abbrev_index[abbr] = m

    pattern = re.compile(r"\*See also:\s*([^*]+?)\*")
    for rel_path in GROUP_FILES:
        path = ROOT / rel_path
        for lineno, line in enumerate(path.read_text().splitlines(), 1):
            mm = pattern.search(line)
            if not mm:
                continue
            body = mm.group(1)
            # Split on the em-dash boundary - everything before em-dash is the list of metric names.
            head = re.split(r"\s[-–-]\s", body, maxsplit=1)[0]
            # Split metric names by comma.
            candidates = [c.strip() for c in head.split(",") if c.strip()]
            for cand in candidates:
                # Strip trailing "(see ...)" or leading "all members of..."
                cand = cand.rstrip(" .")
                if not cand or cand.lower().startswith("all members"):
                    continue
                if cand in normalised:
                    continue
                # Try matching on base (strip parenthetical)
                base = re.sub(r"\s*\([^)]*\)\s*", "", cand).strip()
                if base in normalised:
                    continue
                # Try matching on abbreviation inside parens: "Medical WER (M-WER)"
                abbrs = re.findall(r"\(([^)]+)\)", cand)
                if any(a.strip() in abbrev_index for a in abbrs):
                    continue
                findings.append(
                    Finding(
                        "WARN",
                        "unresolved-see-also",
                        f"'{cand}' does not match any known metric name",
                        f"{rel_path}:{lineno}",
                    )
                )
    return findings


def check_applicability_presence(all_metrics: list[Metric]) -> list[Finding]:
    """Every metric must carry an Applicability row in its dimension table
    (v3.6+ — Applicability moved on-metric)."""
    findings: list[Finding] = []
    valid = set(EXPECTED_APPLICABILITY.keys())
    for m in all_metrics:
        applic = m.dimensions.get("Applicability")
        if applic is None:
            findings.append(
                Finding(
                    "ERROR",
                    "missing-applicability",
                    f"metric {m.ref_id} has no **Applicability** row in its dimension table",
                    f"{m.file}:{m.line}",
                )
            )
        elif applic not in valid:
            findings.append(
                Finding(
                    "ERROR",
                    "invalid-applicability",
                    (
                        f"metric {m.ref_id} has Applicability='{applic}', "
                        f"expected one of {sorted(valid)}"
                    ),
                    f"{m.file}:{m.line}",
                )
            )
    return findings


def check_applicability_totals(all_metrics: list[Metric]) -> list[Finding]:
    """Reconcile per-metric Applicability values (the v3.6 source of truth)
    against the EXPECTED_APPLICABILITY constants and against the legacy
    _applicability.md declared totals (cross-validation during transition).
    """
    findings: list[Finding] = []

    # Derive totals from per-metric values.
    derived: dict[str, int] = Counter()
    for m in all_metrics:
        applic = m.dimensions.get("Applicability")
        if applic in EXPECTED_APPLICABILITY:
            derived[applic] += 1

    for label, expected in EXPECTED_APPLICABILITY.items():
        actual = derived.get(label, 0)
        if actual != expected:
            findings.append(
                Finding(
                    "ERROR",
                    "applicability-total",
                    (
                        f"{label}: expected {expected} per-metric, "
                        f"derived {actual} from dimension tables"
                    ),
                )
            )

    total = sum(derived.values())
    if total != EXPECTED_TOTAL:
        findings.append(
            Finding(
                "ERROR",
                "applicability-sum",
                f"per-metric applicability counts sum to {total}, expected {EXPECTED_TOTAL}",
            )
        )

    # Cross-validation against legacy _applicability.md declared totals (transition only).
    path = ROOT / "_applicability.md"
    text = path.read_text()
    for label, expected in EXPECTED_APPLICABILITY.items():
        m = re.search(rf"\|\s*{re.escape(label)}\s*\|\s*(\d+)\s*\|", text)
        if not m:
            findings.append(
                Finding(
                    "WARN",
                    "applicability-legacy-missing",
                    f"could not find '{label}' count row in _applicability.md",
                )
            )
            continue
        legacy = int(m.group(1))
        if legacy != expected:
            findings.append(
                Finding(
                    "WARN",
                    "applicability-legacy-mismatch",
                    (
                        f"{label}: per-metric says {derived.get(label, 0)}, "
                        f"_applicability.md declares {legacy}"
                    ),
                )
            )

    return findings


def check_tier1_quickref(all_metrics: list[Metric]) -> list[Finding]:
    findings: list[Finding] = []
    path = ROOT / "_tier-1-quick-reference.md"
    lines = path.read_text().splitlines()

    name_to_metric = {m.name: m for m in all_metrics}
    base_index = {}
    for m in all_metrics:
        base = re.sub(r"\s*\([^)]*\)\s*", "", m.name).strip()
        base_index[base] = m

    # Walk the file: actor subsections are "**Actor Name** (N metrics)".
    # Within each subsection, dedupe bullets. Across subsections, a repeat is fine
    # (one metric may be listed under multiple responsible actors).
    bullet_re = re.compile(r"^-\s+\S+\s+\*\*(.+?)\*\*(.*)$")
    actor_re = re.compile(r"^\*\*([^*]+?)\*\*\s*\(\d+\s+metric")
    current_actor = None
    per_actor_names: dict[str, list[str]] = defaultdict(list)
    all_listed_names: list[str] = []

    for line in lines:
        am = actor_re.match(line)
        if am:
            current_actor = am.group(1).strip()
            continue
        bm = bullet_re.match(line)
        if bm and current_actor:
            raw = bm.group(1).strip()
            clean = re.sub(r"\s*⚠️\s*$", "", raw).strip()
            per_actor_names[current_actor].append(clean)
            all_listed_names.append(clean)

    # Existence / tier check per unique name
    for n in set(all_listed_names):
        m = name_to_metric.get(n) or base_index.get(n)
        if m is None:
            findings.append(
                Finding(
                    "WARN",
                    "tier1-unknown-metric",
                    f"quick-reference lists '{n}' but no source metric has that name",
                    "_tier-1-quick-reference.md",
                )
            )
            continue
        if m.tier != 1:
            findings.append(
                Finding(
                    "ERROR",
                    "tier1-drift",
                    f"'{n}' is listed in Tier 1 quick reference but source has it as Tier {m.tier}",
                    f"{m.file}:{m.line}",
                )
            )

    # Duplicates ONLY within a single actor subsection
    for actor, names in per_actor_names.items():
        dupes = [n for n, c in Counter(names).items() if c > 1]
        for d in dupes:
            findings.append(
                Finding(
                    "WARN",
                    "tier1-duplicate-in-actor",
                    f"'{d}' appears more than once under actor '{actor}'",
                    "_tier-1-quick-reference.md",
                )
            )
    return findings


TIGHTENING_SUB_BLOCKS = (
    "**Reference Standard**",
    "**Operational Specification**",
    "**Threshold Guidance**",
)


def is_subpart_id(ref_id: str) -> bool:
    """True iff ref_id ends in [a-z] (e.g. TP.SN-7a)."""
    return bool(SUBPART_REF_ID_RE.match(ref_id))


def parent_id(ref_id: str) -> str | None:
    """For a sub-part, return parent ref_id; else None."""
    m = SUBPART_REF_ID_RE.match(ref_id)
    return m.group(1) if m else None


def is_parent_metric(metric: Metric, all_metrics: list[Metric]) -> bool:
    """True iff this metric has any sub-parts (i.e. some other metric has
    parent_id == metric.ref_id)."""
    return any(parent_id(m.ref_id) == metric.ref_id for m in all_metrics)


def classify_tightening(metric: Metric) -> str:
    """Return 'tightened' (all 3 sub-blocks present), 'not-tightened' (none),
    or 'partial' (some but not all). Sub-parts are classified individually;
    parents (of sub-parts) are not run through this check — see
    classify_parent_tightening below."""
    present = [b for b in TIGHTENING_SUB_BLOCKS if b in metric.body]
    if len(present) == len(TIGHTENING_SUB_BLOCKS):
        return "tightened"
    if not present:
        return "not-tightened"
    return "partial"


def classify_parent_tightening(parent: Metric, all_metrics: list[Metric]) -> str:
    """For a parent metric, classify as tightened iff every sub-part is
    individually tightened. Otherwise not-tightened. Parents do not carry
    the sub-blocks themselves."""
    subparts = [m for m in all_metrics if parent_id(m.ref_id) == parent.ref_id]
    if not subparts:
        # Defensive: caller should only invoke for actual parents
        return "not-tightened"
    if all(classify_tightening(sp) == "tightened" for sp in subparts):
        return "tightened"
    return "not-tightened"


def check_tightening_pattern(all_metrics: list[Metric]) -> list[Finding]:
    """Tier 1 metrics must carry all three tightening sub-blocks or none of
    them. Mixed (partial) states are an error.

    Parent metrics (those with sub-parts) are not subject to this check —
    they carry construct framing in the body, not the tightening pattern.
    Sub-parts are checked individually."""
    findings: list[Finding] = []
    for m in all_metrics:
        if m.tier != 1:
            continue
        if is_parent_metric(m, all_metrics):
            # Parents don't carry the pattern; sub-parts do
            continue
        state = classify_tightening(m)
        if state == "partial":
            present = [b for b in TIGHTENING_SUB_BLOCKS if b in m.body]
            missing = [b for b in TIGHTENING_SUB_BLOCKS if b not in m.body]
            findings.append(
                Finding(
                    "ERROR",
                    "tightening-partial",
                    (
                        f"Tier 1 metric {m.ref_id} has partial tightening: "
                        f"present={[b.strip('*') for b in present]} "
                        f"missing={[b.strip('*') for b in missing]}"
                    ),
                    f"{m.file}:{m.line}",
                )
            )
    return findings


PROVENANCE_RE = re.compile(r"⚠️\s*\*\*Provenance[:\*]", re.UNICODE)


def check_threshold_provenance(all_metrics: list[Metric]) -> list[Finding]:
    """Every tightened metric's Threshold Guidance block must open with a
    ⚠️ **Provenance** line within the first 400 characters of the block body
    (after the heading itself)."""
    findings: list[Finding] = []
    for m in all_metrics:
        if classify_tightening(m) != "tightened":
            continue
        # Locate the Threshold Guidance block.
        idx = m.body.find("**Threshold Guidance**")
        if idx == -1:
            # Defensive: classify_tightening said it's tightened, so this
            # should not happen, but guard anyway.
            continue
        # Skip past the heading itself.
        block_start = idx + len("**Threshold Guidance**")
        snippet = m.body[block_start : block_start + 400]
        if not PROVENANCE_RE.search(snippet):
            findings.append(
                Finding(
                    "ERROR",
                    "missing-threshold-provenance",
                    (
                        f"tightened metric {m.ref_id} has no ⚠️ **Provenance** "
                        f"prelude in its Threshold Guidance block (must appear "
                        f"in the first 400 chars after the heading)"
                    ),
                    f"{m.file}:{m.line}",
                )
            )
    return findings


# ---------------------------------------------------------------------------
# Cross-reference anchor validation (v3.6 follow-up).
# Metric anchors on the rendered MkDocs site are explicit IDs of the form
# `gv-sg-2`, `tp-sn-5`, etc. - generated by build_site.py's add_metric_anchors
# from the metric reference ID (lower-cased, dot replaced with hyphen).
# Cross-references inside metric bodies that use other shapes (e.g. the
# collapsed `gvsg-2-...` form, or wrong-numbered anchors) will silently
# break on the site. The check below validates every `[...](#...)` link in
# every metric body against the set of valid metric anchors.
# ---------------------------------------------------------------------------


METRIC_LINK_RE = re.compile(r"\]\(#([a-z][a-z0-9-]*)\)")
METRIC_ANCHOR_RE = re.compile(r"^[a-z]{2}-[a-z]{2,3}-\d+$")


def _ref_id_to_anchor(ref_id: str) -> str:
    return ref_id.lower().replace(".", "-")


def check_metric_cross_references(all_metrics: list[Metric]) -> list[Finding]:
    """Validate that every `[...](#anchor)` link in a metric body that *looks*
    like a metric anchor (matches METRIC_ANCHOR_RE) actually resolves to a
    known metric ID. Non-metric anchors (group anchors, section anchors) are
    skipped.
    """
    findings: list[Finding] = []
    valid_anchors = {_ref_id_to_anchor(m.ref_id) for m in all_metrics}

    for m in all_metrics:
        for match in METRIC_LINK_RE.finditer(m.body):
            anchor = match.group(1)
            if not METRIC_ANCHOR_RE.match(anchor):
                # Not metric-shaped; skip (could be #outcomes-boundary etc.)
                continue
            if anchor not in valid_anchors:
                findings.append(
                    Finding(
                        "ERROR",
                        "broken-metric-cross-reference",
                        (
                            f"metric {m.ref_id} body contains `(#{anchor})` "
                            f"but no metric has that anchor"
                        ),
                        f"{m.file}:{m.line}",
                    )
                )
    return findings


def emit_tightening_manifest(all_metrics: list[Metric]) -> None:
    """Print a Tier 1 tightening status manifest. Informational, not gated by
    findings.

    Parent metrics (with sub-parts) are classified by aggregate sub-part
    status — tightened iff all sub-parts tightened, else not-tightened.
    Sub-parts themselves are classified individually. Flat metrics
    (no sub-parts, not a parent) are classified individually.
    """
    tier1 = [m for m in all_metrics if m.tier == 1]
    tightened: list[Metric] = []
    not_tightened: list[Metric] = []
    partial: list[Metric] = []

    for m in tier1:
        if is_parent_metric(m, all_metrics):
            state = classify_parent_tightening(m, all_metrics)
        else:
            state = classify_tightening(m)
        if state == "tightened":
            tightened.append(m)
        elif state == "partial":
            partial.append(m)
        else:
            not_tightened.append(m)

    print(f"Tier 1 tightening status: {len(tightened)}/{len(tier1)} tightened.")
    print(
        f"  Tightened: {', '.join(sorted(m.ref_id for m in tightened)) or '(none)'}"
    )
    print(
        f"  Not tightened: {', '.join(sorted(m.ref_id for m in not_tightened)) or '(none)'}"
    )
    if partial:
        print(
            f"  ⚠️ Partial (audit error): "
            f"{', '.join(sorted(m.ref_id for m in partial))}"
        )
    # Retired IDs status line (v3.7+)
    retired = sorted(load_retired_ids())
    if retired:
        print(f"Retired IDs: {', '.join(retired)}")
    print()


def main() -> int:
    all_metrics: list[Metric] = []
    metrics_by_file: dict[str, list[Metric]] = {}
    findings: list[Finding] = []

    for rel_path in GROUP_FILES:
        ms, fs = parse_group_file(rel_path)
        metrics_by_file[rel_path] = ms
        all_metrics.extend(ms)
        findings.extend(fs)

    findings.extend(check_prefixes(metrics_by_file))
    findings.extend(check_numbering(metrics_by_file))
    findings.extend(check_tier_totals(all_metrics))
    findings.extend(check_applicability_presence(all_metrics))
    findings.extend(check_applicability_totals(all_metrics))
    findings.extend(check_tier1_quickref(all_metrics))
    findings.extend(check_see_also_resolves(all_metrics))
    findings.extend(check_tightening_pattern(all_metrics))
    findings.extend(check_threshold_provenance(all_metrics))
    findings.extend(check_metric_cross_references(all_metrics))

    # Report
    errors = [f for f in findings if f.severity == "ERROR"]
    warns = [f for f in findings if f.severity == "WARN"]

    print(f"Parsed {len(all_metrics)} metrics across {len(GROUP_FILES)} group files.")
    tier_counts = Counter(m.tier for m in all_metrics)
    print(
        f"Tier counts: 🟢 {tier_counts[1]} · 🟡 {tier_counts[2]} · 🔵 {tier_counts[3]}"
    )
    print()
    emit_tightening_manifest(all_metrics)

    if not findings:
        print("✅ AUDIT CLEAN - no findings.")
        return 0

    by_category: dict[str, list[Finding]] = defaultdict(list)
    for f in findings:
        by_category[f.category].append(f)

    print(
        f"Found {len(errors)} errors, {len(warns)} warnings across {len(by_category)} categories.\n"
    )
    for cat, items in sorted(by_category.items()):
        print(f"── {cat} ({len(items)}) ──")
        for f in items[:50]:
            print(" ", f.format())
        if len(items) > 50:
            print(f"  ... and {len(items) - 50} more")
        print()

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
