# AVT Metrics Taxonomy — Repository Guide

## Building the document

```
python taxonomy/build.py
```

Produces `avt-metrics-taxonomy.md` at the repo root by concatenating the modular source files in the order defined in `build.py`. The script is idempotent.

## File structure

```
taxonomy/
  _header.md                    # Title, metric count, preamble
  _how-to-use.md                # Priority tiers, cadence, responsible actors,
                                # adapting to local context
  _summary.md                   # By priority tier, by maturity
  _tier-1-quick-reference.md    # All Tier 1 metrics organised by responsible actor
  _contents.md                  # Table of contents
  part-a/                       # The Technical Pipeline
    audio-capture.md
    asr-transcription.md
    diarisation.md
    summarisation-nlp.md
    clinical-coding.md
    epr-write-back.md
  part-b/                       # Pipeline Interactions
    partial-pipeline.md
    end-to-end-pipeline.md
  part-c/                       # The Human Layer
    human-factors-workflow.md
  part-d/                       # Impact & Outcomes
    patient-experience.md
    fairness-equity.md
  part-e/                       # System Governance
    safety-governance.md
    security-adversarial-robustness.md
    privacy-data-governance.md
    operational.md
    training-competency.md
    vendor-transparency-contractual.md
  part-f/                       # Evaluation Science
    meta-evaluation.md
  build.py
  README.md
```

Underscore-prefixed files contain cross-cutting content (not tied to a single metric group). Group files within each part directory are assembled alphabetically.

## Versioning

Stable releases are tagged on `main`:

- `v1.0` — 151 metrics across 18 groups (initial modular split)
- `v2.0` — 214 metrics across 20 groups (first major extension)

## Contributing

One metric = one edit to one file. Add new metrics to the appropriate group file in the correct tier order (Tier 1 before Tier 2 before Tier 3). After editing, run `build.py` and verify the output looks correct before committing.

New metric groups require a new file in the appropriate part directory and an update to the file order in `build.py` if the alphabetical default is not correct.
