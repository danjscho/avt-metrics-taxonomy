#!/usr/bin/env python3
"""Assemble the AVT Metrics Taxonomy from modular source files.

Outputs:
- <repo-root>/avt-metrics-taxonomy.md   monolithic Markdown
- <repo-root>/dist/metrics.csv           flat spreadsheet (214 rows + header)
- <repo-root>/dist/metrics.json          structured metric catalogue
- <repo-root>/dist/gaps.json             roadmap candidates
- <repo-root>/dist/summary.json          headline counts
"""

import csv
import json
import pathlib
from dataclasses import asdict

import parse as p

ROOT = pathlib.Path(__file__).parent
OUTPUT_MD = ROOT.parent / "avt-metrics-taxonomy.md"
DIST = ROOT.parent / "dist"

# Explicit file order - pipeline order within parts, not alphabetical.
# Cross-cutting files first, matching the original document structure.
FILES = [
    "_header.md",
    "_how-to-use.md",
    "_summary.md",
    "_tier-1-quick-reference.md",
    "_contents.md",
    "_applicability.md",
    "_standards-mapping.md",
    "_responsible-ai-lens.md",
    "_outcomes-boundary.md",
    "_gaps.md",
    "_glossary.md",
    "part-a/audio-capture.md",
    "part-a/asr-transcription.md",
    "part-a/diarisation.md",
    "part-a/summarisation-nlp.md",
    "part-a/clinical-coding.md",
    "part-a/epr-write-back.md",
    "part-b/partial-pipeline.md",
    "part-b/end-to-end-pipeline.md",
    "part-c/human-factors-workflow.md",
    "part-d/patient-experience.md",
    "part-d/fairness-equity.md",
    "part-e/safety-governance.md",
    "part-e/nhs-compliance-regulatory.md",
    "part-e/security-adversarial-robustness.md",
    "part-e/privacy-data-governance.md",
    "part-e/operational.md",
    "part-e/environmental-sustainability.md",
    "part-e/training-competency.md",
    "part-e/vendor-transparency-contractual.md",
    "part-f/meta-evaluation.md",
]


def build_monolithic_md() -> None:
    sections = []
    for name in FILES:
        path = ROOT / name
        sections.append(path.read_text().rstrip("\n"))
    output = "\n\n".join(sections) + "\n"
    OUTPUT_MD.write_text(output)
    print(f"Built {OUTPUT_MD.relative_to(ROOT.parent)} from {len(FILES)} files.")


CSV_COLUMNS = [
    "ref_id",
    "name",
    "tier",
    "tier_label",
    "part",
    "group",
    "applicability",
    "cadence",
    "pipeline_layer",
    "assurance_question",
    "measurement_method",
    "lifecycle_phases",
    "responsible_actors",
    "maturity",
    "source",
    "group_file",
    "heading_line",
]


def build_metric_outputs() -> int:
    metrics = p.annotate_applicability(p.parse_all_metrics())

    DIST.mkdir(exist_ok=True)

    # CSV - flat, spreadsheet-friendly
    csv_path = DIST / "metrics.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        for m in metrics:
            writer.writerow(
                {
                    "ref_id": m.ref_id,
                    "name": m.name,
                    "tier": m.tier,
                    "tier_label": m.tier_label,
                    "part": m.part,
                    "group": m.group,
                    "applicability": m.applicability or "",
                    "cadence": m.cadence,
                    "pipeline_layer": m.pipeline_layer,
                    "assurance_question": m.assurance_question,
                    "measurement_method": m.measurement_method,
                    "lifecycle_phases": m.lifecycle_phases,
                    "responsible_actors": m.responsible_actors,
                    "maturity": m.maturity,
                    "source": m.source,
                    "group_file": m.group_file,
                    "heading_line": m.heading_line,
                }
            )
    print(f"Built {csv_path.relative_to(ROOT.parent)} ({len(metrics)} rows).")

    # JSON - preserves full dimensions dict
    json_path = DIST / "metrics.json"
    payload = {
        "version": "v3.2-dev",
        "metric_count": len(metrics),
        "metrics": [
            {
                "ref_id": m.ref_id,
                "name": m.name,
                "tier": m.tier,
                "tier_label": m.tier_label,
                "tier_icon": m.tier_icon,
                "part": m.part,
                "group": m.group,
                "applicability": m.applicability,
                "dimensions": m.dimensions,
                "group_file": m.group_file,
                "heading_line": m.heading_line,
            }
            for m in metrics
        ],
    }
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"Built {json_path.relative_to(ROOT.parent)} ({len(metrics)} metrics).")

    return len(metrics)


def build_gap_output() -> int:
    gaps = p.parse_gaps()
    DIST.mkdir(exist_ok=True)
    path = DIST / "gaps.json"
    payload = {
        "gap_count": len(gaps),
        "by_origin": {},
        "gaps": [asdict(g) for g in gaps],
    }
    # Count by origin for a cheap sanity-checkable header.
    for g in gaps:
        payload["by_origin"][g.origin] = payload["by_origin"].get(g.origin, 0) + 1
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    print(f"Built {path.relative_to(ROOT.parent)} ({len(gaps)} gaps).")
    return len(gaps)


def build_summary() -> None:
    summary = p.summary()
    path = DIST / "summary.json"
    path.write_text(json.dumps(summary, indent=2) + "\n")
    print(f"Built {path.relative_to(ROOT.parent)} ({summary}).")


def build() -> None:
    build_monolithic_md()
    build_metric_outputs()
    build_gap_output()
    build_summary()


if __name__ == "__main__":
    build()
