#!/usr/bin/env python3
"""Assemble the AVT Metrics Taxonomy from modular source files."""

import pathlib

ROOT = pathlib.Path(__file__).parent
OUTPUT = ROOT.parent / "avt-metrics-taxonomy.md"

# Explicit file order — pipeline order within parts, not alphabetical.
# Cross-cutting files first, matching the original document structure.
FILES = [
    "_header.md",
    "_how-to-use.md",
    "_summary.md",
    "_tier-1-quick-reference.md",
    "_contents.md",
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
    "part-e/security-adversarial-robustness.md",
    "part-e/privacy-data-governance.md",
    "part-e/operational.md",
    "part-e/training-competency.md",
    "part-e/vendor-transparency-contractual.md",
    "part-f/meta-evaluation.md",
]


def build():
    sections = []
    for name in FILES:
        path = ROOT / name
        sections.append(path.read_text().rstrip("\n"))

    output = "\n\n".join(sections) + "\n"
    OUTPUT.write_text(output)
    print(f"Built {OUTPUT} from {len(FILES)} files.")


if __name__ == "__main__":
    build()
