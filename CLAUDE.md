# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A healthcare metrics taxonomy for assuring Ambient Voice Technology (AVT) systems — ambient scribes and clinical AI documentation tools — in NHS and comparable healthcare settings. The repo is documentation-only (pure Markdown). There is no application code, no package manager, and no test framework.

The taxonomy organises metrics across pipeline layers (audio capture, ASR, diarisation, summarisation, clinical coding, EPR write-back) and cross-cutting axes (priority tier, measurement cadence, responsible actor, pipeline layer, assurance question, measurement method, maturity).

**Current state:** v1 is a single monolithic file (`avt-metrics-taxonomy.md`, 151 metrics across 18 groups). The active work is a planned migration to a modular directory structure plus a v2 extension to 214 metrics across 20 groups. The execution blueprint is in `plan.md` — read it before starting any work.

## Build

After the Phase 1 split is complete, the modular files live in `taxonomy/` and a build script assembles them:

```
python taxonomy/build.py
```

Output: `avt-metrics-taxonomy.md` at the repo root. The script is idempotent — running it twice produces identical output.

**Build file order** (defined in `build.py`):
1. `_header.md`, `_contents.md`, `_how-to-use.md`, `_summary.md`, `_tier-1-quick-reference.md`
2. `part-a/` through `part-f/` — alphabetical filename order within each part directory

To verify a build: diff the output against the previous version. Phase 1 gate requires whitespace-only differences vs v1.

## File structure (post-split)

```
taxonomy/
  _header.md                    # Title, metric count, preamble
  _how-to-use.md                # Priority tiers, cadence, actors, resource gap callout
  _summary.md                   # By tier, maturity, family, underspecification warning
  _tier-1-quick-reference.md    # All Tier 1 metrics organised by responsible actor
  _contents.md                  # Table of contents with family convention note
  part-a/                       # Technical pipeline (audio → EPR write-back)
  part-b/                       # Partial and end-to-end pipeline assessments
  part-c/                       # Human factors and workflow
  part-d/                       # Patient experience and fairness/equity
  part-e/                       # System governance (safety, compliance, security, privacy,
                                #   operations, sustainability, training, vendor transparency)
  part-f/                       # Meta-evaluation
  build.py
  README.md
```

Underscore-prefixed files sort to the top and contain cross-cutting content (not group content). Group files within each part directory are one file per metric group.

## Metric entry format

Every metric entry follows this structure (in order):

1. Tier icon + metric name heading
2. Dimensions table — all 8 cross-cutting axes (Pipeline Layer, Assurance Question, Measurement Method, Lifecycle Phase, Responsible Actor, Maturity, Priority Tier, Measurement Cadence)
3. **Why this tier?** — rationale for the priority assignment
4. **Formal Definition** block — mathematical or operational definition
5. **Limitations** section
6. **Novel Thinking / Implications** section (may be absent on some entries)
7. Code snippet (only where the batch files include one — do not add speculatively)

For sub-cluster groupings: an italic 1–2 sentence intro paragraph appears before the first metric in the sub-cluster.

For named metric families: a structured block-quote framing appears immediately before the first metric in the family.

## Integration plan

The three-phase execution is detailed in `plan.md`. Key structure:

- **Phase 1** (main branch, one commit): Split v1 into modular files, write `build.py` and `README.md`, verify build output matches v1, tag `v1.0`. **Review gate 1** before proceeding.
- **Phase 2** (`v2-integration` branch, 14 commits): Land 63 new metrics (batches 1–4), then 4 named family framings (Pass 1), 15 underspecification warnings (Pass 2), cross-cutting content updates (Pass 3). **Review gate 2** after metrics land, **review gate 3** after all passes. Pause at each gate and wait for user confirmation.
- **Phase 3**: Merge `v2-integration` → `main` with a merge commit, tag `v2.0`.

Input artefact files in the repo root are the source of truth. Where `avt-metrics-taxonomy-change-plan.md` conflicts with the batch files (`avt-new-metrics-batch-*.md`), the batch files win.

## Locked decisions

Do not revisit these without explicit user instruction:

- All v2 changes are **additive only** — no metric renames, no deletions, no reordering of existing sections
- **NHS Compliance & Regulatory** is a new top-level group in Part E (not a sub-cluster of Safety & Governance)
- **Environmental & Sustainability** is a new top-level group in Part E, all Tier 3, placed between Operational and Training & Competency
- **Sub-clusters** are thematic groupings within an existing group (4 in scope). **Named metric families** are parent-construct groupings that may span sub-clusters (4 in scope). No other groupings should be invented.
- The Pass 1 / Pass 2 overlap on ROUGE, BERTScore, M-WER, and CK-ER is resolved by keeping the family framing full and using trimmed warning versions — see `avt-cross-cutting-additions.md` "One small interaction to resolve during integration"

## When to stop and ask the user

Pause and ask rather than making an autonomous call if:

- A v1 section does not map cleanly to exactly one file in the target structure
- Final metric counts in the Summary or Contents disagree with actual counts in the assembled file
- A "See also" cross-reference points to a metric that cannot be found
- A v2 metric has a tier assignment that conflicts with the placement logic for existing metrics
- Any Pass 1 / Pass 2 overlap is discovered beyond the four flagged cases

## Success criteria for v2.0

- `build.py` produces a file with 214 metrics across 20 groups
- Tier counts: 42 Tier 1, 87 Tier 2, 85 Tier 3
- 4 named metric families with framings, 4 sub-clusters with italic intros, 15 underspecification warnings
- Summary counts match actual assembled counts; Contents per-group counts match file counts
- Header reads "214 metrics across 20 groups"
- Git history: v1 commit (v1.0 tag) → merge commit (v2.0 tag)
