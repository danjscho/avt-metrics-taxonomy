# AVT Metrics Taxonomy - v1 → v2 Integration Plan

This is a plan for Claude Code to execute the integration of v2 additions into the existing v1 AVT Metrics Taxonomy. The work was drafted in a prior chat session and exists as eight markdown artefact files. This plan explains the structure, the sequence, and the decisions already made so that integration can happen efficiently with clear review gates.

## Context

The AVT Metrics Taxonomy is a reference document for assuring Ambient Voice Technology (ambient scribes, clinical AI documentation tools) in NHS and comparable healthcare settings. It is organised across layers of the AVT pipeline (audio capture, ASR, diarisation, summarisation, coding, EPR write-back) and cross-cutting axes (pipeline layer, assurance question, measurement method, lifecycle phase, responsible actor, maturity, priority tier).

**v1** contains 151 metrics across 18 groups. **v2** adds 63 new metrics, 2 new top-level groups, 4 sub-clusters within existing groups, 4 named metric families with parent-construct framings, 15 underspecification warnings on existing metrics, and a range of cross-cutting updates (resource gap callout, Summary updates, Tier 1 Quick Reference expansion, Contents updates).

The v2 content was drafted in response to research findings about the 2025–2026 evaluation literature (SCRIBE, CREOLA, VeriFact, MedHELM, CHECK frameworks), the January–March 2026 NHS guidance suite (NHSE IG guidance, AVT Supplier Registry, CIO/CCIO guidance v2), and regulatory developments (FDA PCCP, EU AI Act high-risk provisions).

Post-integration target: **214 metrics across 20 groups**, with named families and sub-clusters visible at the Contents level, 15 underspecification warnings flagged in the Summary, 42 Tier 1 metrics in the Quick Reference.

## Input files

Expected to be present in the working directory:

1. **`v1-taxonomy.md`** - the current taxonomy file (~5,000 lines, single monolithic markdown document). The base to split and integrate into.
2. **`avt-metrics-taxonomy-change-plan.md`** - high-level plan mapping v2 additions to sections. Use as reference; do not treat as authoritative where it conflicts with the batch files, which are more current.
3. **`avt-new-metrics-batch-1.md`** - 21 new metric entries covering ASR (2), Diarisation/Conversation Analysis (5), Summarisation (4), Clinical Coding (8), EPR Write-back (2).
4. **`avt-new-metrics-batch-2.md`** - 12 new metric entries covering End-to-End (1), Human Factors/Sociotechnical (4), Patient Experience/Clinical Outcomes (4), Fairness & Equity (3).
5. **`avt-new-metrics-batch-3.md`** - 16 new metric entries covering Longitudinal Drift sub-cluster (4), NHS Compliance & Regulatory new group (10), Security (2).
6. **`avt-new-metrics-batch-4.md`** - 14 new metric entries covering Privacy (5), Operational (3), Environmental & Sustainability new group (3), Vendor Transparency (1), Meta-evaluation (2).
7. **`avt-underspecification-warnings.md`** - 15 warnings to add to existing metrics, with three severity tiers (A/B/C). Includes placement instructions and format convention.
8. **`avt-consolidation-framings.md`** - 4 metric family framings (Clinical Content Fidelity, Post-Generation Correction, Clinical Transcription Accuracy, Reference-Based Text Similarity) plus 14 cross-reference footers.
9. **`avt-cross-cutting-additions.md`** - Summary updates, Tier 1 Quick Reference additions, new-group intros, Contents updates, Adapting to Local Context worked example, header metric count update, resource gap callout.

All artefact files use the existing taxonomy house style: dimensions table, Why this tier, Formal Definition block, Limitations, Novel Thinking / Implications, with selective code snippets where they clarify.

## Target file structure

Split v1 into this layout. File names should be lowercase with hyphens; underscore-prefixed files sort to the top of directory listings which helps the build script ordering and makes the cross-cutting pieces visually distinct from the group files.

```
/taxonomy
  _header.md                    # Title, metric count line, short preamble
  _how-to-use.md                # How to Use This Taxonomy, Priority Tiers,
                                # Cadence, Actors, Adapting to Local Context,
                                # Resource Gap Callout (v2 addition)
  _summary.md                   # By Priority Tier, By Maturity, By Family,
                                # By Underspecification Warning
  _tier-1-quick-reference.md    # Tier 1 Quick Reference block
  _contents.md                  # Table of contents and family convention note
  part-a/
    audio-capture.md
    asr-transcription.md
    diarisation.md
    summarisation-nlp.md
    clinical-coding.md
    epr-write-back.md
  part-b/
    partial-pipeline.md
    end-to-end-pipeline.md
  part-c/
    human-factors-workflow.md
  part-d/
    patient-experience.md
    fairness-equity.md
  part-e/
    safety-governance.md
    nhs-compliance-regulatory.md       # new in v2
    security-adversarial-robustness.md
    privacy-data-governance.md
    operational.md
    environmental-sustainability.md    # new in v2
    training-competency.md
    vendor-transparency-contractual.md
  part-f/
    meta-evaluation.md
  build.py                      # assembles master document
  README.md                     # how to build, how to contribute, versioning policy
```

## Build script requirements

`build.py` should:

- Walk the file tree in defined order: `_header`, `_contents`, `_how-to-use`, `_summary`, `_tier-1-quick-reference`, then `part-a` through `part-f` in alphabetical filename order within each part directory
- Concatenate with appropriate blank-line separators between files
- Produce a single output file `avt-metrics-taxonomy.md` at the repo root
- Be idempotent - running it twice produces identical output
- After v1 split, produce output that matches v1 semantically (whitespace normalisation acceptable; section ordering and content must match)
- After v2 integration, produce the final v2 document

Keep the script simple. Python with `pathlib` is fine. No templating engines, no external dependencies beyond the standard library.

## Execution sequence

Three phases, with review gates between them.

### Phase 1 - Split v1 (main branch)

One commit on `main`.

**Commit 1: Split v1 into file structure**
- Read `v1-taxonomy.md`
- Create the directory structure above
- Distribute v1 content into files according to the section structure
- Write `build.py` to assemble files back into a master document
- Write `README.md` with: how to build (`python build.py`), how the file structure maps to the taxonomy, versioning policy (v-tags on the main branch for stable releases), contribution guidance (one metric = one edit to one file)
- Run `build.py` and diff the output against `v1-taxonomy.md`. Differences should be whitespace-only. If content differs, fix the split before committing.
- Tag this commit as `v1.0`

**Review gate 1 - Pause here.** Summarise what was split into which file, report the diff status between the reassembled build and the original v1, and wait for user confirmation before proceeding to Phase 2.

### Phase 2 - v2 integration (v2-integration branch)

Create branch `v2-integration` off `v1.0`. All Phase 2 work happens on this branch.

The commits are ordered so that content additions land before cross-cutting updates that depend on final counts.

**Commit 2: Batch 1 - Technical pipeline additions (21 metrics)**
- Source: `avt-new-metrics-batch-1.md`
- Target files: `asr-transcription.md` (+2), `diarisation.md` (+5, new Conversation Analysis sub-cluster), `summarisation-nlp.md` (+4), `clinical-coding.md` (+8), `epr-write-back.md` (+2)
- Placement: append new entries in tier order within each section (Tier 1 before Tier 2 before Tier 3), matching the existing placement convention in v1
- For Diarisation: the 5 new metrics form a sub-cluster labelled "Conversation Analysis". Add a sub-cluster intro paragraph (in italics, 1–2 sentences) before the first new metric. The sub-cluster intro text is in the batch 1 file.

**Commit 3: Batch 2 - Human layer, outcomes, fairness (12 metrics)**
- Source: `avt-new-metrics-batch-2.md`
- Target files: `end-to-end-pipeline.md` (+1), `human-factors-workflow.md` (+4, new Sociotechnical & Resilience sub-cluster), `patient-experience.md` (+4, new Patient Clinical Outcomes sub-cluster), `fairness-equity.md` (+3)
- Two new sub-clusters, each needing an italic intro paragraph before the first metric in the sub-cluster

**Commit 4: Batch 3a - Longitudinal Drift sub-cluster (4 metrics)**
- Source: `avt-new-metrics-batch-3.md` (partial - the Longitudinal Drift section only)
- Target file: `safety-governance.md`
- New sub-cluster "Longitudinal Drift & Model Contamination" with italic intro paragraph

**Commit 5: Batch 3b - NHS Compliance & Regulatory new group (10 metrics)**
- Source: `avt-new-metrics-batch-3.md` (the NHS Compliance section) + `avt-cross-cutting-additions.md` (the new-group introductory paragraph, section 4.1)
- Create new file: `part-e/nhs-compliance-regulatory.md`
- Contains: group header, group intro paragraph, all 10 metrics in tier order
- Update `build.py` to include the new file in the Part E ordering - specifically between `safety-governance.md` and `security-adversarial-robustness.md`

**Commit 6: Batch 3c - Security additions (2 metrics)**
- Source: `avt-new-metrics-batch-3.md` (the Security section)
- Target file: `security-adversarial-robustness.md`

**Commit 7: Batch 4a - Privacy additions (5 metrics)**
- Source: `avt-new-metrics-batch-4.md` (the Privacy section)
- Target file: `privacy-data-governance.md`

**Commit 8: Batch 4b - Operational additions (3 metrics)**
- Source: `avt-new-metrics-batch-4.md` (the Operational section)
- Target file: `operational.md`

**Commit 9: Batch 4c - Environmental & Sustainability new group (3 metrics)**
- Source: `avt-new-metrics-batch-4.md` (the Environmental section) + `avt-cross-cutting-additions.md` (the new-group introductory paragraph, section 4.2)
- Create new file: `part-e/environmental-sustainability.md`
- Update `build.py` to include the new file in Part E ordering - between `operational.md` and `training-competency.md`

**Commit 10: Batch 4d - Vendor Transparency and Meta-evaluation (3 metrics)**
- Source: `avt-new-metrics-batch-4.md` (the Vendor Transparency and Meta-evaluation sections)
- Target files: `vendor-transparency-contractual.md` (+1), `meta-evaluation.md` (+2)

**Review gate 2 - Pause here.** Confirm all 63 new metrics have landed in the correct files. Report the count per file. Wait for user confirmation before proceeding to the passes.

**Commit 11: Pass 1 - Consolidation framings (4 families, 14 cross-references)**
- Source: `avt-consolidation-framings.md`
- Target files: `summarisation-nlp.md` (Clinical Content Fidelity and Reference-Based Text Similarity families), `human-factors-workflow.md` (Post-Generation Correction family), `asr-transcription.md` (Clinical Transcription Accuracy family)
- Each family framing is a structured block quote inserted immediately before the first metric of the family
- Each member metric gets a "See also" cross-reference footer at the end of the entry

**Commit 12: Pass 2 - Underspecification warnings (15 warnings)**
- Source: `avt-underspecification-warnings.md`
- Target: 15 existing metric entries across `asr-transcription.md`, `diarisation.md`, `summarisation-nlp.md`, `human-factors-workflow.md`, `safety-governance.md`, `end-to-end-pipeline.md`
- Placement: after the existing Limitations block, before Novel Thinking / Implications (or at end of entry if Novel Thinking is absent)
- **Important overlap with Pass 1:** 4 warnings (ROUGE, BERTScore, M-WER, CK-ER) overlap with family framings from Pass 1. Use the trimmed versions specified in the Pass 3 artefact file (`avt-cross-cutting-additions.md`, "One small interaction to resolve during integration" section). Trimmed warnings reference the family framing for the detailed evidence rather than repeating it.

**Commit 13: Pass 3a - Cross-cutting content additions**
- Source: `avt-cross-cutting-additions.md` sections 1, 4, 6
- Target files: `_how-to-use.md` (resource gap callout, Adapting to Local Context worked example), `part-e/nhs-compliance-regulatory.md` (group intro, if not already added in commit 5), `part-e/environmental-sustainability.md` (group intro, if not already added in commit 9)
- If the new-group intros were already added in commits 5 and 9, this commit only handles the How to Use additions

**Commit 14: Pass 3b - Summary, Tier 1 Quick Reference, Contents, header updates**
- Source: `avt-cross-cutting-additions.md` sections 2, 3, 5, 7
- Target files: `_summary.md`, `_tier-1-quick-reference.md`, `_contents.md`, `_header.md`
- All counts, breakdowns, and Tier 1 Quick Reference entries. This commit lands last because everything in it depends on the final state of Phase 2.
- Verify the counts in the Summary match the actual counts in the assembled file - specifically the Tier 1 / Tier 2 / Tier 3 distribution, the family counts, the underspecification warning counts, and the per-group metric counts in Contents

**Review gate 3 - Pause here.** Run `build.py`, produce the assembled v2 document, report the final metric count by group and by tier, and flag any counts that disagree with the expected values (214 total, 42 Tier 1, 87 Tier 2, 85 Tier 3). Wait for user review before merging.

### Phase 3 - Merge to main

**Merge commit: v2-integration → main**
- Once the user has reviewed the assembled v2 document and confirmed it's correct
- Fast-forward or merge commit is fine - a merge commit with a descriptive message is preferred because it preserves the branch history visibly
- Tag the merge commit as `v2.0`
- Delete the `v2-integration` branch or keep it for historical reference (user preference)

## Decisions already made

The user has made the following decisions during the drafting phase. Do not revisit these without explicit instruction.

- **No renaming of existing metrics.** All v2 additions are additive. Existing metric names, section ordering, and the five-axis cross-cutting structure are preserved.
- **No deletion of existing metrics.** Even the three Tier A underspecification metrics with no established methodology (Off-Label Use Detection, Trust Halo Decay Rate, Note Review Fatigue Trajectory) remain in the operational taxonomy with explicit warnings rather than being moved to a research appendix.
- **NHS Compliance & Regulatory is a new top-level group, not a sub-cluster of Safety & Governance.** The rationale is in the group intro paragraph - it's a distinct compliance surface with different responsible actors and different cadences.
- **Environmental & Sustainability is a new top-level group, all Tier 3.** Placed in Part E between Operational and Training & Competency.
- **Sub-clusters are thematic groupings within existing groups. Named metric families are parent-construct groupings that may span sub-clusters.** Four sub-clusters and four families are in scope; no other groupings should be invented during integration.
- **The Pass 1 / Pass 2 overlap on ROUGE, BERTScore, M-WER, and CK-ER is resolved by keeping the family framing full and trimming the individual warnings** - see commit 12 note above.
- **Code snippets are retained where they clarify measurement** (Stigmatising Language Replication, Code Hallucination Rate, etc.) and omitted elsewhere. The batch files are the source of truth for which metrics get code snippets.

## Decisions to flag to the user during integration

If any of the following arise during execution, pause and ask the user before deciding:

- **Split ambiguity** - if a section of v1 does not map cleanly to exactly one file in the new structure (e.g. some cross-cutting content that spans multiple groups), ask where it should land rather than making an arbitrary call.
- **Count mismatches** - if the final counts in the Summary and Contents do not match the actual counts in the assembled file, this is almost certainly a placement error in one of the earlier commits. Stop and report the mismatch rather than editing the Summary to match.
- **Cross-reference dangling pointers** - if a "See also" reference in a family framing or warning points to a metric that cannot be found, stop and report.
- **Conflicting tier assignments** - if any v2 metric has a tier assignment that conflicts with an existing metric's placement logic (e.g. a Tier 1 metric that cannot actually be measured by the assigned responsible actor without vendor cooperation that isn't called out), flag it for user review rather than silently adjusting.
- **Pass 1 / Pass 2 overlap on metrics beyond the four flagged ones** - the four overlaps (ROUGE, BERTScore, M-WER, CK-ER) are known and handled. If any other overlap is discovered during integration, stop and ask how to resolve it.

## Non-goals

Explicitly out of scope for this integration:

- **Content validation against external sources.** The v2 drafts cite specific literature (Croxford et al. 2025, CREOLA framework, CHECK paper, etc.). Do not verify these citations during integration - that's a separate validation pass if the user wants it.
- **Companion deliverables.** A deployer one-pager, procurement checklist, and national body briefing were discussed as future artefacts. These are not part of the v2 integration.
- **Structured data migration.** A future migration from markdown to a structured data store (YAML/JSON per metric) was discussed. This is not part of the v2 integration - it's a potential v3 exercise.
- **Restructuring commits after landing.** Once a commit lands on the v2-integration branch, do not rewrite history to improve it. Fix issues in subsequent commits so the audit trail remains intact.

## Success criteria

v2.0 is complete when:

- `build.py` produces a `avt-metrics-taxonomy.md` file containing 214 metrics across 20 groups
- Tier 1 count is 42, Tier 2 is 87, Tier 3 is 85
- All 4 named metric families appear with framings before their first member
- All 4 sub-clusters appear with italic intros
- All 15 underspecification warnings are present on the correct metrics with the right severity tier labels
- The Summary section counts match the actual counts in the assembled file
- The Contents section metric counts per group match the actual counts in each file
- The Tier 1 Quick Reference contains all 42 Tier 1 metrics organised by responsible actor
- The resource gap callout is present in How to Use This Taxonomy
- The header metric count at the top of the document reads "214 metrics across 20 groups"
- Git history on `main` shows a clean sequence: v1 → split (v1.0) → merge of v2-integration (v2.0)

## Post-integration, out of scope but worth noting

Once v2.0 is stable, the natural next steps are:

1. **Validation of the drafted metrics against the literature cited.** The citations in the v2 drafts should be verified and the bibliography made explicit. Candidates: a `references.md` file in the repo root, or BibTeX-style citation keys in metric entries with a rendered bibliography at the end.
2. **Companion deliverables** drawing from the taxonomy: deployer one-pager, procurement checklist, national body infrastructure-gap briefing.
3. **Consideration of migrating to structured records** if the taxonomy becomes the spine of multiple downstream artefacts - at that point the markdown document becomes a rendered view of a per-metric structured data store rather than the primary editable form.

None of these are blockers for v2.0 release. They are future iterations.
