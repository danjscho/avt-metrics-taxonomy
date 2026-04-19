"""Populate docs/ from the taxonomy source for MkDocs Material.

Pattern: each source file copied to the right docs path, with small
header tweaks so MkDocs page titles read well. The monolithic MD and
CSV/JSON downloads are still produced by build.py; this script only
lays out the site content.
"""

from __future__ import annotations

import pathlib
import re
import shutil

import parse as parse_src

ROOT = pathlib.Path(__file__).parent
REPO = ROOT.parent
DOCS = REPO / "docs"

# source file -> docs path
MAPPING: dict[str, str] = {
    "_header.md": "index.md",
    "_how-to-use.md": "how-to-use.md",
    "_tier-1-quick-reference.md": "tier-1-quick-reference.md",
    "_contents.md": "contents.md",
    "_applicability.md": "applicability.md",
    "_standards-mapping.md": "standards-mapping.md",
    "_responsible-ai-lens.md": "responsible-ai-lens.md",
    "_gaps.md": "gaps.md",
    "_glossary.md": "glossary.md",
    "part-a/audio-capture.md": "groups/audio-capture.md",
    "part-a/asr-transcription.md": "groups/asr-transcription.md",
    "part-a/diarisation.md": "groups/diarisation.md",
    "part-a/summarisation-nlp.md": "groups/summarisation-nlp.md",
    "part-a/clinical-coding.md": "groups/clinical-coding.md",
    "part-a/epr-write-back.md": "groups/epr-write-back.md",
    "part-b/partial-pipeline.md": "groups/partial-pipeline.md",
    "part-b/end-to-end-pipeline.md": "groups/end-to-end-pipeline.md",
    "part-c/human-factors-workflow.md": "groups/human-factors-workflow.md",
    "part-d/patient-experience.md": "groups/patient-experience.md",
    "part-d/fairness-equity.md": "groups/fairness-equity.md",
    "part-e/safety-governance.md": "groups/safety-governance.md",
    "part-e/nhs-compliance-regulatory.md": "groups/nhs-compliance-regulatory.md",
    "part-e/security-adversarial-robustness.md": "groups/security-adversarial-robustness.md",
    "part-e/privacy-data-governance.md": "groups/privacy-data-governance.md",
    "part-e/operational.md": "groups/operational.md",
    "part-e/environmental-sustainability.md": "groups/environmental-sustainability.md",
    "part-e/training-competency.md": "groups/training-competency.md",
    "part-e/vendor-transparency-contractual.md": "groups/vendor-transparency-contractual.md",
    "part-f/meta-evaluation.md": "groups/meta-evaluation.md",
}


# Intra-monolith anchors that used to resolve inside the single file now
# need to redirect to the relevant page. Keys are the anchor slugs as they
# appear in the source; values are the target URL (relative to docs root).
ANCHOR_REWRITES: dict[str, str] = {
    # Group anchors - these were h2s inside the monolith; now they're pages.
    "audio-capture-environment": "groups/audio-capture.md",
    "asr-transcription": "groups/asr-transcription.md",
    "diarisation": "groups/diarisation.md",
    "summarisation-nlp": "groups/summarisation-nlp.md",
    "clinical-coding": "groups/clinical-coding.md",
    "epr-write-back": "groups/epr-write-back.md",
    "partial-pipeline": "groups/partial-pipeline.md",
    "end-to-end-pipeline": "groups/end-to-end-pipeline.md",
    "human-factors-workflow": "groups/human-factors-workflow.md",
    "patient-experience": "groups/patient-experience.md",
    "fairness-equity": "groups/fairness-equity.md",
    "safety-governance": "groups/safety-governance.md",
    "nhs-compliance-regulatory": "groups/nhs-compliance-regulatory.md",
    "security-adversarial-robustness": "groups/security-adversarial-robustness.md",
    "privacy-data-governance": "groups/privacy-data-governance.md",
    "operational": "groups/operational.md",
    "environmental-sustainability": "groups/environmental-sustainability.md",
    "training-competency": "groups/training-competency.md",
    "vendor-transparency-contractual": "groups/vendor-transparency-contractual.md",
    "meta-evaluation": "groups/meta-evaluation.md",
    # Cross-cutting sections - each now its own page.
    "applicability-classification": "applicability.md",
    "standards-mapping": "standards-mapping.md",
    "responsible-ai-lens": "responsible-ai-lens.md",
    "gaps-proposed-metrics-roadmap": "gaps.md",
}

_MD_LINK = re.compile(r"(?<!!)\[([^\]]+?)\]\(#([a-z0-9][a-z0-9_-]*)\)")

# Metric headings look like:  ### TP.AC-1 🟡 Signal-to-Noise Ratio (SNR) Monitoring
# We want stable anchors like #tp-ac-1 so reference IDs can be cited forever.
# MkDocs' default slugifier drops the '.' and produces "tpac-1-...", which is
# unstable if the metric name changes. Inject an explicit {#tp-ac-1} via the
# attr_list extension (enabled in mkdocs.yml).
_METRIC_HEADING = re.compile(
    r"^(###\s+)([A-Z]{2,3}\.[A-Z0-9]{2,3}-\d+)(\s+[🟢🟡🔵]\s+.+?)\s*$",
    re.MULTILINE,
)


# Link every bolded metric name on the Tier-1 Quick Reference page to its
# source page. The source file (`_tier-1-quick-reference.md`) is authored
# prose - we don't edit it at source, we transform it on the way into the
# site. Each bullet is of the form:
#   - 🚪 **Metric Name** - rationale...
# We match `**Metric Name**` tokens (optionally followed by `⚠️`), look the
# name up in the parsed catalogue, and rewrite to a link.
_BOLD_METRIC_TOKEN = re.compile(r"\*\*([^*]+?)\*\*")


def _metric_name_index() -> dict[str, "parse_src.Metric"]:
    metrics = parse_src.parse_all_metrics()
    idx: dict[str, parse_src.Metric] = {}
    for m in metrics:
        idx[m.name] = m
        stripped = re.sub(r"\s*\([^)]*\)\s*", "", m.name).strip()
        if stripped and stripped not in idx:
            idx[stripped] = m
    return idx


def link_tier1_quickref(text: str) -> str:
    """Convert `**Name**` → `[Name](../groups/<group>.md#ref-id)` when the
    bolded text matches a known Tier-1 metric. Non-metric bold phrases (e.g.
    **Deployer** actor subsection headings) are left untouched because they
    don't match the name index.
    """
    idx = _metric_name_index()

    def sub(m: re.Match) -> str:
        raw = m.group(1).strip()
        candidate = raw.rstrip(" ⚠️").strip()
        hit = idx.get(candidate)
        if hit is None:
            # Try base name (strip parenthetical)
            base = re.sub(r"\s*\([^)]*\)\s*", "", candidate).strip()
            hit = idx.get(base)
        if hit is None or hit.tier != 1:
            return m.group(0)  # not a Tier-1 metric, leave as-is
        slug = hit.ref_id.lower().replace(".", "-")
        page = SRC_GROUP_FILE_TO_PAGE.get(hit.group_file, "")
        if not page:
            return m.group(0)
        # Keep the warning suffix outside the link if present.
        suffix = " ⚠️" if raw.endswith("⚠️") else ""
        return f"[**{candidate}**]({page}#{slug}){suffix}"

    return _BOLD_METRIC_TOKEN.sub(sub, text)


def add_metric_anchors(text: str) -> str:
    def sub(m: re.Match) -> str:
        prefix, ref_id, tail = m.group(1), m.group(2), m.group(3)
        slug = ref_id.lower().replace(".", "-")
        # Keep the reference-ID visible in the heading; attach a stable id.
        return f"{prefix}{ref_id}{tail} {{ #{slug} }}"

    return _METRIC_HEADING.sub(sub, text)


def rewrite_anchors(text: str, current_page: str) -> str:
    """Rewrite `[text](#slug)` links where `#slug` targets a section that
    has moved to another page in the site. Same-page anchors are left
    untouched.
    """

    def sub(m: re.Match) -> str:
        label, slug = m.group(1), m.group(2)
        target = ANCHOR_REWRITES.get(slug)
        if target is None:
            return m.group(0)  # unchanged - assumed same-page
        # Don't self-redirect if the current page is the target.
        if target.split("#", 1)[0] == current_page:
            return m.group(0)
        return f"[{label}]({target})"

    return _MD_LINK.sub(sub, text)


def promote_h2_to_h1(text: str) -> str:
    """Reshape a source file so MkDocs gets exactly one h1 at the top.

    Group-file pattern:
        # Part A - The Technical Pipeline
        ## Audio Capture & Environment

    We want the *group name* to be the h1 (so the sidebar, tab title, and
    page heading all match the user's mental model of "I'm on the Audio
    Capture page"), with the Part shown as a small italic kicker above it
    so readers don't lose the parent-section context.

    Non-group files (underscore-prefixed) start with a single `## Heading`
    and just need that promoted to `# Heading`.
    """
    lines = text.splitlines()
    # Find first non-empty line
    first_idx = None
    for i, line in enumerate(lines):
        if line.strip():
            first_idx = i
            break
    if first_idx is None:
        return text

    first = lines[first_idx].strip()
    # Case A: group file - `# Part …` then later `## <Group>`
    if first.startswith("# Part ") and " - " in first:
        part_title = first[2:].strip()  # "Part A - The Technical Pipeline"
        # Find the next `## ` heading
        for j in range(first_idx + 1, len(lines)):
            s = lines[j].strip()
            if s.startswith("## ") and not s.startswith("### "):
                group_title = s[3:].strip()
                # Replace lines from first_idx..j (inclusive) with a kicker + h1
                kicker = f"*{part_title}*"
                new_head = [f"# {group_title}", "", kicker, ""]
                lines = lines[:first_idx] + new_head + lines[j + 1 :]
                break
        return "\n".join(lines) + ("\n" if not text.endswith("\n") else "")

    # Case B: cross-cutting file starting with `## Heading` - promote to `# Heading`.
    if first.startswith("## "):
        lines[first_idx] = "# " + first[3:]
    return "\n".join(lines) + ("\n" if not text.endswith("\n") else "")


def main() -> None:
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir()
    (DOCS / "groups").mkdir()

    for src_rel, dst_rel in MAPPING.items():
        src = ROOT / src_rel
        dst = DOCS / dst_rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        text = src.read_text()
        text = rewrite_anchors(text, dst_rel)
        text = add_metric_anchors(text)
        if dst_rel == "tier-1-quick-reference.md":
            text = link_tier1_quickref(text)
        if dst_rel == "gaps.md":
            text = _inject_roadmap_prelude(text)
        if dst_rel == "contents.md":
            text = _inject_contents_applicability_row(text)
        if dst_rel.startswith("groups/"):
            text = _add_applicability_badges(text, dst_rel)
            text = _add_related_metrics_footers(text, dst_rel)
        if dst_rel == "index.md":
            # Root index page - replace the source h1 and the repeated
            # summary prose with a concise landing block; keep the source's
            # "Acknowledgements / Sources / Structure" content below the
            # new jumping-off section.
            promoted = promote_h2_to_h1(text)
            promoted_lines = promoted.splitlines()
            if promoted_lines and promoted_lines[0].startswith("# "):
                promoted_lines = promoted_lines[1:]
            while promoted_lines and not promoted_lines[0].strip():
                promoted_lines = promoted_lines[1:]
            promoted = "\n".join(promoted_lines)
            text = _landing_page(promoted)
        else:
            text = promote_h2_to_h1(text)
            # Icon legend collapsible — lives on pages where tier + cadence
            # emoji appear densely; injected after promote_h2_to_h1 so the
            # h1 and Part kicker are already in place on group pages.
            text = inject_legend(text, dst_rel)
        dst.write_text(text)

    # Changelog at repo root is already Markdown - copy as-is.
    cl_src = REPO / "CHANGELOG.md"
    if cl_src.exists():
        (DOCS / "changelog.md").write_text(cl_src.read_text())

    # Downloads landing page - links resolve in CI where dist/* is copied
    # into docs/downloads/ before mkdocs build (see .github/workflows/site.yml).
    # For local preview, also mirror dist/* into docs/downloads/ here so
    # `mkdocs serve` shows the downloads as working links.
    (DOCS / "downloads.md").write_text(_downloads_page())
    _mirror_downloads()
    _copy_stylesheets()

    # Cross-cut auto-generated pages (applicability / principle / theme).
    crosscut_count = build_crosscuts()

    print(
        f"Populated {DOCS.relative_to(REPO)} with {len(MAPPING) + 2 + crosscut_count} pages."
    )


def _copy_stylesheets() -> None:
    """Copy taxonomy/stylesheets/*.css into docs/stylesheets/.
    docs/ is gitignored, so this has to run every build."""
    src = ROOT / "stylesheets"
    if not src.exists():
        return
    dest = DOCS / "stylesheets"
    dest.mkdir(exist_ok=True)
    for css in src.glob("*.css"):
        shutil.copy2(css, dest / css.name)


def _mirror_downloads() -> None:
    dist = REPO / "dist"
    if not dist.exists():
        return  # build.py hasn't been run; skip
    target = DOCS / "downloads"
    target.mkdir(exist_ok=True)
    for name in ("metrics.csv", "metrics.json", "gaps.json", "summary.json"):
        src = dist / name
        if src.exists():
            shutil.copy2(src, target / name)
    # Copy the monolithic MD for local preview parity with CI - but with
    # a `.txt` extension so MkDocs doesn't treat it as a page source.
    # The Downloads page link carries `download="avt-metrics-taxonomy.md"`
    # so browsers save it with the expected filename.
    md_src = REPO / "avt-metrics-taxonomy.md"
    if md_src.exists():
        shutil.copy2(md_src, target / "avt-metrics-taxonomy.txt")


# ---------------------------------------------------------------------------
# Cross-cut auto-generated pages
#
# Generates pages under docs/crosscuts/ from parsed source:
#   - by-applicability/avt-specific.md, avt-contextualised.md, general.md
#   - by-principle/p1.md … p10.md
#   - by-theme/t1.md … t6.md
# Per-standard cross-cut pages are deferred - standards-mapping tables have
# heterogeneous shapes per standard; needs a dedicated extractor round.
# ---------------------------------------------------------------------------

CROSSCUT_DIR = "crosscuts"

# Short labels that match the left-nav hand-written names in mkdocs.yml,
# used wherever we link to a principle/theme page (index, landing, per-metric
# references). Kept in one place so a nav rename stays in sync.
PRINCIPLE_SHORT = {
    "P1": "P1 - Limitations",
    "P2": "P2 - Lawful/ethical",
    "P3": "P3 - Security",
    "P4": "P4 - Human control",
    "P5": "P5 - Lifecycle",
    "P6": "P6 - Right tool",
    "P7": "P7 - Openness",
    "P8": "P8 - Commercial",
    "P9": "P9 - Skills",
    "P10": "P10 - Org assurance",
}

THEME_SHORT = {
    "T1": "T1 - Safety, Security, Robustness",
    "T2": "T2 - Transparency & Explainability",
    "T3": "T3 - Fairness",
    "T4": "T4 - Accountability & Governance",
    "T5": "T5 - Contestability & Redress",
    "T6": "T6 - Societal Wellbeing",
}

SRC_GROUP_FILE_TO_PAGE = {
    "part-a/audio-capture.md": "groups/audio-capture.md",
    "part-a/asr-transcription.md": "groups/asr-transcription.md",
    "part-a/diarisation.md": "groups/diarisation.md",
    "part-a/summarisation-nlp.md": "groups/summarisation-nlp.md",
    "part-a/clinical-coding.md": "groups/clinical-coding.md",
    "part-a/epr-write-back.md": "groups/epr-write-back.md",
    "part-b/partial-pipeline.md": "groups/partial-pipeline.md",
    "part-b/end-to-end-pipeline.md": "groups/end-to-end-pipeline.md",
    "part-c/human-factors-workflow.md": "groups/human-factors-workflow.md",
    "part-d/patient-experience.md": "groups/patient-experience.md",
    "part-d/fairness-equity.md": "groups/fairness-equity.md",
    "part-e/safety-governance.md": "groups/safety-governance.md",
    "part-e/nhs-compliance-regulatory.md": "groups/nhs-compliance-regulatory.md",
    "part-e/security-adversarial-robustness.md": "groups/security-adversarial-robustness.md",
    "part-e/privacy-data-governance.md": "groups/privacy-data-governance.md",
    "part-e/operational.md": "groups/operational.md",
    "part-e/environmental-sustainability.md": "groups/environmental-sustainability.md",
    "part-e/training-competency.md": "groups/training-competency.md",
    "part-e/vendor-transparency-contractual.md": "groups/vendor-transparency-contractual.md",
    "part-f/meta-evaluation.md": "groups/meta-evaluation.md",
}


def _metric_page_link(ref_id: str, name: str, group_file: str) -> str:
    """Return a Markdown link like [name](../groups/<group>.md#tp-ac-1)."""
    slug = ref_id.lower().replace(".", "-")
    page = SRC_GROUP_FILE_TO_PAGE.get(group_file, "")
    if not page:
        return name
    # From crosscuts/by-X/page.md, the group pages are at ../../groups/*.md.
    # Use Markdown-style .md#slug path so MkDocs validates and rewrites it.
    return f"[{name}](../../{page}#{slug})"


def _tier_icon(t: int) -> str:
    return {1: "🟢", 2: "🟡", 3: "🔵"}[t]


def _crosscut_index_page(
    applicability_counts: dict[str, int],
    principle_counts: dict[str, int],
    theme_counts: dict[str, int],
    standards: dict[str, dict] | None = None,
) -> str:
    lines = [
        "# Cross-cut views",
        "",
        "Auto-generated views that slice the 214-metric catalogue along three additional axes. "
        "Each view links back to individual metric pages - nothing here is authoritative, "
        "just a different way to read the same source.",
        "",
        "## By applicability",
        "",
        "Which metrics are AVT-specific vs transferable to any healthcare AI.",
        "",
    ]
    for label, path in (
        ("AVT-Specific", "by-applicability/avt-specific.md"),
        ("AVT-Contextualised", "by-applicability/avt-contextualised.md"),
        ("General Healthcare AI", "by-applicability/general.md"),
    ):
        count = applicability_counts.get(label, 0)
        lines.append(f"- [{label}]({path}) - {count} metrics")
    lines += [
        "",
        "## By DSIT AI Playbook principle",
        "",
        "The 10 Playbook principles that the taxonomy supports. Counts below include only "
        "metrics that genuinely operationalise the principle (not metrics that merely touch on it).",
        "",
    ]
    for code in sorted(principle_counts, key=lambda c: int(c[1:])):
        count = principle_counts[code]
        label = PRINCIPLE_SHORT.get(code, f"{code} - principle membership")
        lines.append(f"- [{label}](by-principle/{code.lower()}.md) - {count} metrics")
    lines += [
        "",
        "## By standard",
        "",
        "Auto-generated assertion-level pages for standards whose source "
        "tables map directly to metric IDs. Four additional standards "
        "(CQC, PSIRF, PRSB, Caldicott) use narrative prose rather than "
        "structured tables; they are summarised on the main "
        "[Standards Mapping](../standards-mapping.md) page.",
        "",
    ]
    if standards:
        for std, info in standards.items():
            total = sum(len(s.rows) for s in info["sections"])
            resolved = sum(len(r.metric_refs) for s in info["sections"] for r in s.rows)
            lines.append(
                f"- [{std}](by-standard/{info['code']}.md) - {total} assertions, {resolved} metric mappings"
            )
    lines += [
        "",
        "## By Responsible AI ethical theme",
        "",
        "Six cross-cutting themes from the Responsible AI literature, mapped to the metric catalogue.",
        "",
    ]
    for code in sorted(theme_counts, key=lambda c: int(c[1:])):
        count = theme_counts[code]
        label = THEME_SHORT.get(code, f"{code} - theme membership")
        lines.append(f"- [{label}](by-theme/{code.lower()}.md) - {count} metrics")
    lines.append("")
    return "\n".join(lines)


def _applicability_page(label: str, metrics: list) -> str:
    lines = [
        f"# Applicability: {label}",
        "",
        f"{len(metrics)} metrics classified as **{label}**.",
        "",
        "| Ref | Metric | Group | Tier |",
        "|-----|--------|-------|------|",
    ]
    for m in sorted(metrics, key=lambda x: (x.part, x.group, x.ref_id)):
        link = _metric_page_link(m.ref_id, m.name, m.group_file)
        lines.append(
            f"| {m.ref_id} | {link} | {m.group} | {_tier_icon(m.tier)} {m.tier} |"
        )
    lines.append("")
    return "\n".join(lines)


def _principle_or_theme_page(kind: str, code: str, label: str, entries: list) -> str:
    header = "Playbook principle" if kind == "principle" else "Ethical theme"
    lines = [
        f"# {header} {code}: {label}",
        "",
        f"{len(entries)} metrics operationalise this {kind}. Each entry links to the metric's full definition on its group page.",
        "",
        "| Ref | Metric | Group | Tier | Aspect |",
        "|-----|--------|-------|------|--------|",
    ]
    # Resolve ref_id -> group_file via a quick lookup through parsed metrics.
    all_metrics = parse_src.parse_all_metrics()
    ref_to_group_file = {m.ref_id: m.group_file for m in all_metrics}
    for e in entries:
        gf = ref_to_group_file.get(e.ref_id, "")
        link = _metric_page_link(e.ref_id, e.name, gf) if gf else e.name
        lines.append(
            f"| {e.ref_id} | {link} | {e.group} | {e.tier_icon} | {e.aspect} |"
        )
    lines.append("")
    return "\n".join(lines)


def _standard_page(standard: str, sections: list) -> str:
    lines = [f"# Coverage: {standard}", ""]
    lines.append(
        f"Assertion-level mapping of this standard to the metric catalogue. "
        f"Each metric link jumps to the full definition on its group page. "
        f"See the full [Standards Mapping](../../standards-mapping.md) for "
        f"overview, publisher, and scope of this standard."
    )
    lines.append("")
    ref_to_group_file = {m.ref_id: m.group_file for m in parse_src.parse_all_metrics()}
    for section in sections:
        if section.subsection:
            lines.append(f"## {section.subsection}")
            lines.append("")
        lines.append("| Criterion | Description | Metrics | Tier |")
        lines.append("|-----------|-------------|---------|------|")
        for row in section.rows:
            metric_md = _render_metric_refs(
                row.metric_refs, row.metric_names, ref_to_group_file
            )
            lines.append(
                f"| {row.criterion} | {row.description} | {metric_md} | {row.tier_cell or '-'} |"
            )
        lines.append("")
    return "\n".join(lines)


def _render_metric_refs(
    ref_ids: list[str], names: list[str], ref_to_group_file: dict
) -> str:
    if not ref_ids and not names:
        return "*Process criterion - no metric equivalent*"
    parts: list[str] = []
    # Walk ref_ids in order, falling back to names that didn't resolve.
    seen = set()
    for rid in ref_ids:
        if rid in seen:
            continue
        seen.add(rid)
        gf = ref_to_group_file.get(rid, "")
        if gf:
            slug = rid.lower().replace(".", "-")
            page = SRC_GROUP_FILE_TO_PAGE.get(gf, "")
            # Find the metric's display name
            display = None
            for name, hit in parse_src._name_to_metric_idx().items():
                if hit.ref_id == rid and name == hit.name:
                    display = name
                    break
            display = display or rid
            if page:
                parts.append(f"[{rid} {display}](../../{page}#{slug})")
            else:
                parts.append(f"{rid} {display}")
        else:
            parts.append(rid)
    # Any unresolved textual names
    for name in names:
        if name in seen:
            continue
        # Skip names we already resolved by ref
        already = any(name in p for p in parts)
        if already:
            continue
        parts.append(f"*{name}*")
    return "<br>".join(parts)  # <br> keeps cells readable inside Markdown tables


def build_crosscuts() -> int:
    """Emit applicability / principle / theme cross-cut pages. Returns page count."""
    metrics = parse_src.annotate_applicability(parse_src.parse_all_metrics())
    apps = parse_src.group_metrics_by_applicability(metrics)
    principles = parse_src.parse_rai_principle_membership()
    themes = parse_src.parse_rai_theme_membership()

    base = DOCS / CROSSCUT_DIR
    (base / "by-applicability").mkdir(parents=True, exist_ok=True)
    (base / "by-principle").mkdir(parents=True, exist_ok=True)
    (base / "by-theme").mkdir(parents=True, exist_ok=True)
    (base / "by-standard").mkdir(parents=True, exist_ok=True)

    # Per-standard pages (only those with table-based assertion mappings).
    standards = parse_src.parse_standards_grouped()
    for standard, info in standards.items():
        (base / "by-standard" / f"{info['code']}.md").write_text(
            _standard_page(standard, info["sections"])
        )

    # Index page for the section
    (base / "index.md").write_text(
        _crosscut_index_page(
            applicability_counts={k: len(v) for k, v in apps.items()},
            principle_counts={k: len(v) for k, (_, v) in principles.items()},
            theme_counts={k: len(v) for k, (_, v) in themes.items()},
            standards=standards,
        )
    )

    # Applicability pages
    applicability_slugs = {
        "AVT-Specific": "avt-specific.md",
        "AVT-Contextualised": "avt-contextualised.md",
        "General Healthcare AI": "general.md",
    }
    for label, slug in applicability_slugs.items():
        if label in apps:
            (base / "by-applicability" / slug).write_text(
                _applicability_page(label, apps[label])
            )

    # Principle pages
    for code, (name, entries) in principles.items():
        (base / "by-principle" / f"{code.lower()}.md").write_text(
            _principle_or_theme_page("principle", code, name, entries)
        )

    # Theme pages
    for code, (name, entries) in themes.items():
        (base / "by-theme" / f"{code.lower()}.md").write_text(
            _principle_or_theme_page("theme", code, name, entries)
        )

    total = (
        1 + len(applicability_slugs) + len(principles) + len(themes) + len(standards)
    )
    print(f"Generated {total} crosscut pages under docs/{CROSSCUT_DIR}/.")
    return total


_APPLICABILITY_BADGES = {
    "AVT-Specific": ("🎯", "avt-specific.md"),
    "AVT-Contextualised": ("🔀", "avt-contextualised.md"),
    "General Healthcare AI": ("🌐", "general.md"),
}


def _legend_block(how_to_use_link: str) -> str:
    return (
        "\n"
        "??? note \"Legend: tier and cadence icons\"\n"
        "    **Priority tier** (leading dot in each metric heading):\n\n"
        "    - 🟢 **Tier 1** - Minimum viable assurance (measurable today with existing tools)\n"
        "    - 🟡 **Tier 2** - Recommended for any AVT deployment\n"
        "    - 🔵 **Tier 3** - Advanced / research-grade\n\n"
        "    **Measurement cadence** (used in the Tier 1 quick-reference bullets):\n\n"
        "    - 🚪 **One-off gate** - measured once pre-deployment as an acceptance criterion\n"
        "    - 📡 **Continuous** - automated, ongoing measurement during operational use\n"
        "    - 🔄 **Periodic audit** - scheduled assessment (quarterly / annual)\n\n"
        "    **Other flags:**\n\n"
        "    - ⚠️ Metric carries an underspecification warning - see the full entry for measurement-science caveats\n\n"
        f"    See [How to use]({how_to_use_link}) for the full definitions.\n"
        "\n"
    )


def _insert_after_h1(text: str, block: str) -> str:
    """Insert a block immediately after the page's h1 + its blank line, and
    after any immediately following italic kicker paragraph (for group pages
    where `promote_h2_to_h1` puts a Part kicker under the h1)."""
    lines = text.splitlines()
    # Find h1
    i = 0
    while i < len(lines) and not lines[i].startswith("# "):
        i += 1
    if i == len(lines):
        return text  # no h1 found; leave alone
    # Skip the h1 line and any blank
    i += 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    # Skip a single kicker line of the form `*...*` plus following blanks
    if i < len(lines) and lines[i].startswith("*") and lines[i].rstrip().endswith("*"):
        i += 1
        while i < len(lines) and not lines[i].strip():
            i += 1
    return "\n".join(lines[:i]) + "\n" + block + "\n".join(lines[i:]) + (
        "\n" if not text.endswith("\n") else ""
    )


def inject_legend(text: str, current_page: str) -> str:
    """Add a collapsible legend explaining tier and cadence icons to pages
    where those icons appear densely (group pages + the Tier-1 quickref).
    Uses a `???` collapsible admonition so it stays out of the way until a
    reader needs it."""
    if current_page.startswith("groups/"):
        return _insert_after_h1(text, _legend_block("../how-to-use.md"))
    if current_page == "tier-1-quick-reference.md":
        return _insert_after_h1(text, _legend_block("how-to-use.md"))
    return text


def _add_applicability_badges(text: str, current_page: str) -> str:
    """Inject a compact applicability badge after each metric's dimensions
    table on a group page. The badge is a single line:
        **Applicability:** 🎯 [AVT-Specific](../crosscuts/by-applicability/avt-specific.md)
    Inserted immediately after the closing row of the dimensions table (the
    line before the next blank-line-separated section).
    """
    if not current_page.startswith("groups/"):
        return text
    applicability_idx = parse_src.parse_applicability()

    # Split the doc into metric segments by ### Ref-ID heading (same regex
    # as add_metric_anchors, after anchor injection).
    heading_re = re.compile(
        r"^(###\s+([A-Z]{2,3}\.[A-Z0-9]{2,3}-\d+)\s+[🟢🟡🔵]\s+.+?)\s+\{\s*#[a-z0-9-]+\s*\}\s*$"
    )
    lines = text.splitlines()

    # Identify metric heading line numbers.
    metric_bounds: list[tuple[int, int, str]] = []
    indices = [i for i, line in enumerate(lines) if heading_re.match(line)]
    for k, start in enumerate(indices):
        end = indices[k + 1] if k + 1 < len(indices) else len(lines)
        ref_id = heading_re.match(lines[start]).group(2)
        metric_bounds.append((start, end, ref_id))

    if not metric_bounds:
        return text

    # For each metric, find the end of its dimensions table (last `|` row
    # before a non-`|` line), and insert the badge immediately below.
    inserts: dict[int, str] = {}
    for start, end, ref_id in metric_bounds:
        label = applicability_idx.get(ref_id)
        if label is None:
            continue
        badge = _APPLICABILITY_BADGES.get(label)
        if badge is None:
            continue
        emoji, target = badge
        # Walk from start+1 forward to find the dimensions table end.
        table_end = None
        in_table = False
        for i in range(start + 1, end):
            if lines[i].startswith("|"):
                in_table = True
                table_end = i
            elif in_table and not lines[i].startswith("|"):
                break
        if table_end is None:
            continue
        # Build the badge line. From groups/<this>.md, crosscuts/by-applicability/<target>
        # is reachable at ../crosscuts/by-applicability/<target>.
        badge_md = f"\n**Applicability:** {emoji} [{label}](../crosscuts/by-applicability/{target})\n"
        inserts[table_end + 1] = badge_md

    if not inserts:
        return text

    out: list[str] = []
    for i, line in enumerate(lines):
        if i in inserts:
            out.append(inserts[i])
        out.append(line)
    if len(lines) in inserts:
        out.append(inserts[len(lines)])
    return "\n".join(out)


_RAI_MEMBERSHIP_CACHE: dict[str, list[tuple[str, str]]] | None = None


def _rai_membership_by_ref_id() -> dict[str, list[tuple[str, str]]]:
    """Return {ref_id: [(axis, code), ...]} where axis is 'Principle' or 'Theme'."""
    global _RAI_MEMBERSHIP_CACHE
    if _RAI_MEMBERSHIP_CACHE is not None:
        return _RAI_MEMBERSHIP_CACHE
    out: dict[str, list[tuple[str, str]]] = {}
    for code, (_name, entries) in parse_src.parse_rai_principle_membership().items():
        for e in entries:
            out.setdefault(e.ref_id, []).append(("Principle", code))
    for code, (_name, entries) in parse_src.parse_rai_theme_membership().items():
        for e in entries:
            out.setdefault(e.ref_id, []).append(("Theme", code))
    _RAI_MEMBERSHIP_CACHE = out
    return out


def _add_related_metrics_footers(text: str, current_page: str) -> str:
    """Append a compact "Related metrics" list after each metric entry on a
    group page. Related = other metrics sharing at least one Playbook
    principle or ethical theme from the Responsible AI lens.

    Works by matching each `### REF ICON Name` heading, computing the set
    of co-memberships, and injecting the block before the next metric
    heading or before the final `---` / EOF.
    """
    if not current_page.startswith("groups/"):
        return text
    membership = _rai_membership_by_ref_id()
    ref_to_metric = {m.ref_id: m for m in parse_src.parse_all_metrics()}

    # Build a reverse lookup: axis-code -> list of ref_ids
    by_axis: dict[tuple[str, str], list[str]] = {}
    for rid, axes in membership.items():
        for ax in axes:
            by_axis.setdefault(ax, []).append(rid)

    # Walk the page: find metric heading lines, collect their co-members.
    lines = text.splitlines()
    out_lines: list[str] = []
    i = 0
    # Pattern: our headings include the explicit {#slug} suffix added earlier.
    heading_re = re.compile(
        r"^###\s+([A-Z]{2,3}\.[A-Z0-9]{2,3}-\d+)\s+[🟢🟡🔵]\s+.+?\s+\{\s*#[a-z0-9-]+\s*\}\s*$"
    )
    # For each metric, find the range ending before the next `###` or `---` at col 1.
    metric_heading_line_nums: list[tuple[int, str]] = []
    for idx, line in enumerate(lines):
        m = heading_re.match(line)
        if m:
            metric_heading_line_nums.append((idx, m.group(1)))

    if not metric_heading_line_nums:
        return text

    # Compute bounds for each metric: ends at next metric heading or a standalone '---'.
    bounds: list[tuple[int, int, str]] = []
    for i, (line_num, rid) in enumerate(metric_heading_line_nums):
        end = (
            metric_heading_line_nums[i + 1][0]
            if i + 1 < len(metric_heading_line_nums)
            else len(lines)
        )
        bounds.append((line_num, end, rid))

    # Build an insert map: index -> block text
    inserts: dict[int, str] = {}
    for start, end, rid in bounds:
        axes = membership.get(rid, [])
        if not axes:
            continue
        related_ids: set[str] = set()
        for ax in axes:
            related_ids.update(by_axis.get(ax, []))
        related_ids.discard(rid)
        if not related_ids:
            continue

        # Cap at 6 most-shared first (sort by co-axis count).
        def co_count(r: str) -> int:
            other = set(membership.get(r, []))
            return len(set(axes) & other)

        ranked = sorted(related_ids, key=lambda r: (-co_count(r), r))[:6]
        items = []
        for r in ranked:
            target = ref_to_metric.get(r)
            if target is None:
                continue
            page = SRC_GROUP_FILE_TO_PAGE.get(target.group_file, "")
            same_page = page == current_page
            slug = r.lower().replace(".", "-")
            # Markdown-style link so mkdocs validates and rewrites.
            # From groups/<this>.md, sibling group pages are at ./<name>.md.
            href = f"#{slug}" if same_page else f"{pathlib.Path(page).name}#{slug}"
            items.append(f"[{r} {target.name}]({href})")
        if not items:
            continue
        # Find the last content line before the next metric heading - place
        # before any trailing `---` separator.
        insert_at = end
        while insert_at > start and lines[insert_at - 1].strip() in ("", "---"):
            insert_at -= 1
        block = (
            "\n\n**Related metrics** *(shared Playbook principles / ethical themes):* "
            + " · ".join(items)
            + "\n"
        )
        inserts[insert_at] = block

    # Assemble output with inserts.
    for idx, line in enumerate(lines):
        if idx in inserts:
            out_lines.append(inserts[idx])
        out_lines.append(line)
    # Any inserts at EOF
    if len(lines) in inserts:
        out_lines.append(inserts[len(lines)])
    return "\n".join(out_lines)


def _inject_contents_applicability_row(text: str) -> str:
    """Inject a prominent applicability-filter row near the top of the
    contents page so a reader can jump to AVT-Specific / AVT-Contextualised
    / General Healthcare AI in one click."""
    block = (
        "\n"
        '!!! tip "Browse by applicability"\n'
        "    Jump straight to the metrics that match your scope:\n\n"
        "    [:material-target: 48 AVT-Specific](crosscuts/by-applicability/avt-specific.md){ .md-button }\n"
        "    [:material-shuffle-variant: 77 AVT-Contextualised](crosscuts/by-applicability/avt-contextualised.md){ .md-button }\n"
        "    [:material-earth: 89 General Healthcare AI](crosscuts/by-applicability/general.md){ .md-button }\n"
        "\n"
    )
    # Insert after the h1 (first `# ` line) and any immediately following blank lines.
    lines = text.splitlines()
    insert_at = 0
    for i, line in enumerate(lines):
        if line.startswith("# "):
            insert_at = i + 1
            while insert_at < len(lines) and not lines[insert_at].strip():
                insert_at += 1
            break
    return (
        "\n".join(lines[:insert_at])
        + "\n"
        + block
        + "\n".join(lines[insert_at:])
        + ("\n" if not text.endswith("\n") else "")
    )


def _inject_roadmap_prelude(text: str) -> str:
    """Insert a 'Near-term priorities' panel at the top of the gaps page,
    driven by parsed gap data (Tier 1 candidates + High-severity RAI gaps).
    The source file stays editorial; this is a derived view.
    """
    gaps = parse_src.parse_gaps()
    tier_1 = [g for g in gaps if g.tier == 1]
    rai_high = [g for g in gaps if g.severity == "High"]

    # Build a compact table of the Tier 1 candidates - the accepted/proposed
    # set a deployer or standards body would want to tackle first.
    lines = [
        '!!! tip "Near-term priorities"',
        "    These candidates combine **Tier 1 classification** (where assigned) "
        "and **High severity** (Responsible AI lens). They are the highest-leverage "
        "adds for any future metric round.",
        "",
        "### Tier 1 candidates",
        "",
    ]
    if tier_1:
        lines.append("| ID | Title | Origin |")
        lines.append("|----|-------|--------|")
        for g in sorted(tier_1, key=lambda x: (x.origin, x.gap_id or "")):
            gid = g.gap_id or "-"
            lines.append(f"| {gid} | {g.title} | {g.origin} |")
    else:
        lines.append(
            "_(no Tier 1 candidates currently - earlier rounds promoted all available.)_"
        )
    lines.append("")

    lines += [
        "### High-severity policy gaps (RAI lens)",
        "",
    ]
    if rai_high:
        lines.append("| Origin | Title | Cross-reference |")
        lines.append("|--------|-------|-----------------|")
        for g in rai_high:
            lines.append(f"| {g.origin} | {g.title} | {g.notes} |")
    else:
        lines.append("_(no High-severity gaps recorded.)_")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Insert the prelude immediately after the first "## Gaps..." heading + intro
    # paragraph, which ends at the "---" separator on line 13 in the source.
    # The post-promotion text starts with "# Gaps & Proposed Metrics (Roadmap)".
    # Place the prelude right after the first "---" line.
    pieces = text.split("\n---\n", 1)
    if len(pieces) == 2:
        return pieces[0] + "\n\n" + "\n".join(lines) + "\n" + pieces[1]
    return text + "\n\n" + "\n".join(lines) + "\n"


def _landing_page(header_body: str) -> str:
    """Generate the site landing page with live counts and jump links."""
    summary = parse_src.summary()
    metric_count = summary["metric_count"]
    group_count = summary["group_count"]
    t1 = summary["tier_counts"].get("1", 0)
    t2 = summary["tier_counts"].get("2", 0)
    t3 = summary["tier_counts"].get("3", 0)
    gap_count = summary["gap_count"]
    return f"""# AVT Metrics Taxonomy

!!! warning "Draft - not yet stakeholder-approved"
    Shared openly for early feedback. Tier assignments, gap analysis, and
    cross-references may change before public release. Treat as a working
    document, not a settled standard.

!!! info "v3.1 - {metric_count} metrics across {group_count} groups"
    A healthcare-AI assurance metrics taxonomy for Ambient Voice Technology
    in NHS and comparable settings. Each metric carries a formal definition,
    priority tier, responsible actors, and mappings to 11 healthcare and
    AI standards.

## At a glance

<div class="grid cards" markdown>

-   :material-scale:{{ .lg .middle }} **Three priority tiers**

    ---

    🟢 **{t1}** Tier 1 - minimum viable assurance, measurable today
    🟡 **{t2}** Tier 2 - recommended for any AVT deployment
    🔵 **{t3}** Tier 3 - advanced / research-grade

    [Jump to Tier 1 quick reference](tier-1-quick-reference.md)

-   :material-clipboard-check-outline:{{ .lg .middle }} **Standards coverage**

    ---

    Mapped to DTAC, DSPT, DCB0129/0160, NHS LLM Framework, MHRA SaMD,
    NICE ESF, FHIR UK Core, CQC, PSIRF, PRSB, and Caldicott Principles.

    [Full standards mapping](standards-mapping.md)

-   :material-eye-outline:{{ .lg .middle }} **Policy lens**

    ---

    Mapped to the DSIT AI Playbook's 10 principles and the six
    Responsible AI ethical themes. Includes a coverage matrix of
    high-leverage "policy-lever" metrics.

    [Responsible AI lens](responsible-ai-lens.md)

-   :material-map-marker-path:{{ .lg .middle }} **Roadmap**

    ---

    {gap_count} gap candidates pending review, drawn from external
    coverage audits (RSET, NHSE IG), standards mapping, and the
    policy lens.

    [Browse roadmap](gaps.md)

-   :material-filter-variant:{{ .lg .middle }} **Browse by applicability**

    ---

    Quickly filter the catalogue by whether the metric is specific to
    ambient voice, applies to any healthcare AI, or sits in between.

    🎯 [48 AVT-Specific](crosscuts/by-applicability/avt-specific.md) ·
    🔀 [77 AVT-Contextualised](crosscuts/by-applicability/avt-contextualised.md) ·
    🌐 [89 General Healthcare AI](crosscuts/by-applicability/general.md)

</div>

## Ways in

- **First time here?** Read [How to use the taxonomy](how-to-use.md) to understand tiers, cadence, and responsible actors.
- **Deploying AVT?** Start with the [Tier 1 Quick Reference](tier-1-quick-reference.md) - the Day Zero set.
- **Evaluating products?** Jump to the [Applicability classification](applicability.md) and the [AVT-Specific cross-cut](crosscuts/by-applicability/avt-specific.md).
- **Setting procurement criteria?** Work through [Standards Mapping](standards-mapping.md) and the [per-principle cross-cuts](crosscuts/index.md).
- **Building a metric?** Every metric has a stable reference ID. Cite as `TP.AC-1` → `/groups/audio-capture/#tp-ac-1`.
- **Want raw data?** See [Downloads](downloads.md) for CSV, JSON, and the monolithic Markdown archival copy.

---

{header_body}
"""


def _downloads_page() -> str:
    return """# Downloads

Machine-readable and archival exports of the taxonomy, regenerated on every release.

## Structured data

- [metrics.csv](downloads/metrics.csv) - all 214 metrics as a flat spreadsheet (17 columns: reference ID, name, tier, part, group, applicability, 8 dimension fields, source, pointer to source file).
- [metrics.json](downloads/metrics.json) - same metrics with full dimension dictionary preserved per entry. Stable for programmatic consumption.
- [gaps.json](downloads/gaps.json) - 83 roadmap candidates (accepted + deferred), partitioned by origin (RSET, NHSE IG, standards mapping, Responsible AI lens).
- [summary.json](downloads/summary.json) - headline counts (metric count, tier distribution, group count, gap count).

## Archival Markdown

- <a href="downloads/avt-metrics-taxonomy.txt" download="avt-metrics-taxonomy.md">avt-metrics-taxonomy.md</a> - the full monolithic document. Same content as the site, assembled into a single file for offline reading, PDF printing, or citation. Served with a `.txt` extension so MkDocs treats it as a static download; the link triggers a `.md` save filename in the browser.

## Citing

Cite the taxonomy as:

> AVT Metrics Taxonomy v3.1 (2026). Schofield, D. Healthcare metrics taxonomy for assuring Ambient Voice Technology. https://danjscho.github.io/avt-metrics-taxonomy/

For a specific metric, use its reference ID (e.g. `TP.AC-1`) - these are stable across versions. Individual metric pages carry anchor links of the form `/groups/<group>/#tp-ac-1` suitable for deep citation.

## Earlier versions

Versioned historical builds will appear here once the `mike` plugin is wired up. For now, this page shows the current tagged release.
"""


if __name__ == "__main__":
    main()
