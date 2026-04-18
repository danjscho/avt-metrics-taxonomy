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
    "_header.md":                                  "index.md",
    "_how-to-use.md":                              "how-to-use.md",
    "_tier-1-quick-reference.md":                  "tier-1-quick-reference.md",
    "_contents.md":                                "contents.md",
    "_applicability.md":                           "applicability.md",
    "_standards-mapping.md":                       "standards-mapping.md",
    "_responsible-ai-lens.md":                     "responsible-ai-lens.md",
    "_gaps.md":                                    "gaps.md",
    "part-a/audio-capture.md":                     "groups/audio-capture.md",
    "part-a/asr-transcription.md":                 "groups/asr-transcription.md",
    "part-a/diarisation.md":                       "groups/diarisation.md",
    "part-a/summarisation-nlp.md":                 "groups/summarisation-nlp.md",
    "part-a/clinical-coding.md":                   "groups/clinical-coding.md",
    "part-a/epr-write-back.md":                    "groups/epr-write-back.md",
    "part-b/partial-pipeline.md":                  "groups/partial-pipeline.md",
    "part-b/end-to-end-pipeline.md":               "groups/end-to-end-pipeline.md",
    "part-c/human-factors-workflow.md":            "groups/human-factors-workflow.md",
    "part-d/patient-experience.md":                "groups/patient-experience.md",
    "part-d/fairness-equity.md":                   "groups/fairness-equity.md",
    "part-e/safety-governance.md":                 "groups/safety-governance.md",
    "part-e/nhs-compliance-regulatory.md":         "groups/nhs-compliance-regulatory.md",
    "part-e/security-adversarial-robustness.md":   "groups/security-adversarial-robustness.md",
    "part-e/privacy-data-governance.md":           "groups/privacy-data-governance.md",
    "part-e/operational.md":                       "groups/operational.md",
    "part-e/environmental-sustainability.md":      "groups/environmental-sustainability.md",
    "part-e/training-competency.md":               "groups/training-competency.md",
    "part-e/vendor-transparency-contractual.md":   "groups/vendor-transparency-contractual.md",
    "part-f/meta-evaluation.md":                   "groups/meta-evaluation.md",
}


# Intra-monolith anchors that used to resolve inside the single file now
# need to redirect to the relevant page. Keys are the anchor slugs as they
# appear in the source; values are the target URL (relative to docs root).
ANCHOR_REWRITES: dict[str, str] = {
    # Group anchors — these were h2s inside the monolith; now they're pages.
    "audio-capture-environment":             "groups/audio-capture.md",
    "asr-transcription":                     "groups/asr-transcription.md",
    "diarisation":                           "groups/diarisation.md",
    "summarisation-nlp":                     "groups/summarisation-nlp.md",
    "clinical-coding":                       "groups/clinical-coding.md",
    "epr-write-back":                        "groups/epr-write-back.md",
    "partial-pipeline":                      "groups/partial-pipeline.md",
    "end-to-end-pipeline":                   "groups/end-to-end-pipeline.md",
    "human-factors-workflow":                "groups/human-factors-workflow.md",
    "patient-experience":                    "groups/patient-experience.md",
    "fairness-equity":                       "groups/fairness-equity.md",
    "safety-governance":                     "groups/safety-governance.md",
    "nhs-compliance-regulatory":             "groups/nhs-compliance-regulatory.md",
    "security-adversarial-robustness":       "groups/security-adversarial-robustness.md",
    "privacy-data-governance":               "groups/privacy-data-governance.md",
    "operational":                           "groups/operational.md",
    "environmental-sustainability":          "groups/environmental-sustainability.md",
    "training-competency":                   "groups/training-competency.md",
    "vendor-transparency-contractual":       "groups/vendor-transparency-contractual.md",
    "meta-evaluation":                       "groups/meta-evaluation.md",
    # Cross-cutting sections — each now its own page.
    "applicability-classification":          "applicability.md",
    "standards-mapping":                     "standards-mapping.md",
    "responsible-ai-lens":                   "responsible-ai-lens.md",
    "gaps-proposed-metrics-roadmap":         "gaps.md",
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
            return m.group(0)  # unchanged — assumed same-page
        # Don't self-redirect if the current page is the target.
        if target.split("#", 1)[0] == current_page:
            return m.group(0)
        return f"[{label}]({target})"
    return _MD_LINK.sub(sub, text)


def promote_h2_to_h1(text: str) -> str:
    """If the source starts with `## Title`, promote to `# Title` for the page h1.
    MkDocs expects a single h1 per page; source files avoid h1 because they're
    concatenated into a single monolithic doc."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("## "):
            lines[i] = "# " + stripped[3:]
            break
        # If first non-empty line isn't ## or #, leave alone.
        break
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
        if dst_rel == "index.md":
            # Root index page — replace the source h1 with a landing block
            # that includes a brief lead before the header content.
            promoted = promote_h2_to_h1(text)
            # Strip the original h1 if present; we'll provide our own.
            promoted_lines = promoted.splitlines()
            if promoted_lines and promoted_lines[0].startswith("# "):
                promoted_lines = promoted_lines[1:]
            # Also trim any immediately-following blank line to avoid a double break.
            while promoted_lines and not promoted_lines[0].strip():
                promoted_lines = promoted_lines[1:]
            promoted = "\n".join(promoted_lines)
            text = (
                "# AVT Metrics Taxonomy\n\n"
                "A healthcare-AI assurance metrics taxonomy for Ambient Voice Technology in NHS and comparable settings. "
                "214 metrics across 20 groups, mapped to 11 standards and the DSIT AI Playbook. "
                "v3.1 tagged 2026-04-18.\n\n"
                "Browse metrics by part in the navigation, or jump to the "
                "[Tier 1 Quick Reference](tier-1-quick-reference.md) for a deployer's Day Zero set.\n\n"
                "---\n\n"
                + promoted + "\n"
            )
        else:
            text = promote_h2_to_h1(text)
        dst.write_text(text)

    # Changelog at repo root is already Markdown — copy as-is.
    cl_src = REPO / "CHANGELOG.md"
    if cl_src.exists():
        (DOCS / "changelog.md").write_text(cl_src.read_text())

    # Downloads landing page — links resolve in CI where dist/* is copied
    # into docs/downloads/ before mkdocs build (see .github/workflows/site.yml).
    # For local preview, also mirror dist/* into docs/downloads/ here so
    # `mkdocs serve` shows the downloads as working links.
    (DOCS / "downloads.md").write_text(_downloads_page())
    _mirror_downloads()

    # Cross-cut auto-generated pages (applicability / principle / theme).
    crosscut_count = build_crosscuts()

    print(f"Populated {DOCS.relative_to(REPO)} with {len(MAPPING) + 2 + crosscut_count} pages.")


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
    # Copy the monolithic MD for local preview parity with CI — but with
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
# Per-standard cross-cut pages are deferred — standards-mapping tables have
# heterogeneous shapes per standard; needs a dedicated extractor round.
# ---------------------------------------------------------------------------

CROSSCUT_DIR = "crosscuts"

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


def _crosscut_index_page(applicability_counts: dict[str, int],
                          principle_counts: dict[str, int],
                          theme_counts: dict[str, int]) -> str:
    lines = [
        "# Cross-cut views",
        "",
        "Auto-generated views that slice the 214-metric catalogue along three additional axes. "
        "Each view links back to individual metric pages — nothing here is authoritative, "
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
        lines.append(f"- [{label}]({path}) — {count} metrics")
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
        lines.append(f"- [{code} — principle membership](by-principle/{code.lower()}.md) — {count} metrics")
    lines += [
        "",
        "## By Responsible AI ethical theme",
        "",
        "Six cross-cutting themes from the Responsible AI literature, mapped to the metric catalogue.",
        "",
    ]
    for code in sorted(theme_counts, key=lambda c: int(c[1:])):
        count = theme_counts[code]
        lines.append(f"- [{code} — theme membership](by-theme/{code.lower()}.md) — {count} metrics")
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
        lines.append(f"| {m.ref_id} | {link} | {m.group} | {_tier_icon(m.tier)} {m.tier} |")
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
        lines.append(f"| {e.ref_id} | {link} | {e.group} | {e.tier_icon} | {e.aspect} |")
    lines.append("")
    return "\n".join(lines)


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

    # Index page for the section
    (base / "index.md").write_text(_crosscut_index_page(
        applicability_counts={k: len(v) for k, v in apps.items()},
        principle_counts={k: len(v) for k, (_, v) in principles.items()},
        theme_counts={k: len(v) for k, (_, v) in themes.items()},
    ))

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

    total = 1 + len(applicability_slugs) + len(principles) + len(themes)
    print(f"Generated {total} crosscut pages under docs/{CROSSCUT_DIR}/.")
    return total


def _downloads_page() -> str:
    return """# Downloads

Machine-readable and archival exports of the taxonomy, regenerated on every release.

## Structured data

- [metrics.csv](downloads/metrics.csv) — all 214 metrics as a flat spreadsheet (17 columns: reference ID, name, tier, part, group, applicability, 8 dimension fields, source, pointer to source file).
- [metrics.json](downloads/metrics.json) — same metrics with full dimension dictionary preserved per entry. Stable for programmatic consumption.
- [gaps.json](downloads/gaps.json) — 83 roadmap candidates (accepted + deferred), partitioned by origin (RSET, NHSE IG, standards mapping, Responsible AI lens).
- [summary.json](downloads/summary.json) — headline counts (metric count, tier distribution, group count, gap count).

## Archival Markdown

- <a href="downloads/avt-metrics-taxonomy.txt" download="avt-metrics-taxonomy.md">avt-metrics-taxonomy.md</a> — the full monolithic document. Same content as the site, assembled into a single file for offline reading, PDF printing, or citation. Served with a `.txt` extension so MkDocs treats it as a static download; the link triggers a `.md` save filename in the browser.

## Citing

Cite the taxonomy as:

> AVT Metrics Taxonomy v3.1 (2026). Schofield, D. Healthcare metrics taxonomy for assuring Ambient Voice Technology. https://danjscho.github.io/avt-metrics-taxonomy/

For a specific metric, use its reference ID (e.g. `TP.AC-1`) — these are stable across versions. Individual metric pages carry anchor links of the form `/groups/<group>/#tp-ac-1` suitable for deep citation.

## Earlier versions

Versioned historical builds will appear here once the `mike` plugin is wired up. For now, this page shows the current tagged release.
"""


if __name__ == "__main__":
    main()
