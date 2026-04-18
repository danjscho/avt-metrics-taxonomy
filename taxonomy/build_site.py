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

    print(f"Populated {DOCS.relative_to(REPO)} with {len(MAPPING) + 1} pages.")


if __name__ == "__main__":
    main()
