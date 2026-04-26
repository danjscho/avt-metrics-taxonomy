# v3.7 — Pipeline Tightening + Duplication Action + Bespoke Deferred-Pool Scoping

## Context

This plan is **sketched, not detailed.** Two of its three phases depend on outputs from v3.6 (the duplication review artefact, the cross-reference audit results, and possibly small applicability reclassifications surfaced during Phase A). Detailed planning for Phase B and Phase C should happen at v3.7 kick-off, after v3.6 ships. Phase A is detailed enough to execute against today.

After v3.5 the tightening status is 25/43 Tier 1 metrics tightened, with the v3.4 classification artefact identifying three remaining buckets:

- **6 pipeline narrow candidates** (TP.ASR-12, TP.ASR-13, TP.WB-2, TP.WB-3, TP.WB-4, TP.SN-20) — pattern fits but applied narrowly; these are mostly TIGHT-ish with specific underspecified facets rather than wholesale loose
- **5 pattern-may-not-fit deferred** (GV.OP-6, GV.SG-9, GV.SG-11, GV.SG-13, HL.HF-3) — bespoke per-metric work; the standard pattern is the wrong shape for at least some
- **8 TIGHT** — explicitly not planned for tightening (would be structural cleanup, not substance)

v3.6 will add: a duplication-review artefact (research, not action), the v3.5 follow-up fixes, applicability-on-metric alignment.

**Why now:** v3.6 closes the architectural / honesty / known-issues backlog and produces the duplication-review input. v3.7 is the first release where we can act on duplication findings, complete the pipeline tightening, and start work on the awkward 5 deferred metrics — each of which needs bespoke shape.

**Intended outcome:** Tier 1 tightening passes the 30/43 mark via pipeline narrow tightening; duplication-review findings actioned (merges or explicit-stay decisions) with user sign-off; at least 1–2 of the 5 deferred metrics scoped and progressed.

---

## Phase A — Pipeline narrow tightening (6 metrics)

These are the v3.4-classified pipeline candidates: TP.ASR-12 Hallucination-Under-Noise Rate, TP.ASR-13 Numeric Accuracy, TP.WB-2 Integration Error Rate, TP.WB-3 Field Mapping Accuracy, TP.WB-4 Update vs Append Behaviour, TP.SN-20 Uncertainty Marker Preservation.

Different shape from compliance/governance (v3.5) — these are technical-pipeline metrics with narrow underspecified facets rather than wholesale loose definitions. The pattern (Reference Standard / Operational Specification / Threshold Guidance with ⚠️ Provenance prelude) still applies, but the substance per metric is targeted:

- **TP.ASR-12** — test-corpus sample sizes per non-speech category; severity weighting on spurious clinical content
- **TP.ASR-13** — sub-metric reference standards (date-format canonicalisation, unit normalisation); critical-numeric pause threshold
- **TP.WB-2** — partial-vs-degraded boundary; per-EPR stratification (parallel to TP.WB-1's v3.3 tightening); error-type taxonomy
- **TP.WB-3** — explicit field-map per-EPR reference; safety-critical categorisation cross-link to TP.WB-1
- **TP.WB-4** — correct-behaviour decision rule per context; duplicate-detection windowing; safety-critical override
- **TP.SN-20** — certainty-direction asymmetric weighting (inflation more dangerous than deflation, per existing Limitations)

After v3.7 Phase A: tightening status reaches **31/43 Tier 1** (from 25/43).

**Effort:** ~3–4 days, comparable to v3.5 Wave 1.

---

## Phase B — Act on duplication-review findings (input: v3.6 Phase B artefact)

**Sketch only — detailed planning at v3.7 kick-off.**

The v3.6 duplication review will produce a frozen artefact at `archive/v3.6-duplication-review.md` classifying every metric pair as `distinct` / `overlapping` / `redundant`. v3.7 acts on the findings:

- **`overlapping` pairs** — document the relationship explicitly in metric prose (e.g. cross-references, family or sub-cluster framing where genuinely warranted). Most likely outcome: 5–10 metrics get a See-also or family-framing addition; no structural changes.
- **`redundant` pairs** — review with user before any merges. Likely 0–5 candidates surfaced. Decision options per pair:
  - Merge (one metric absorbs the other, retired metric's content folded in, ID retired with redirect note)
  - Explicit-distinct call (clarify in prose why they are not redundant despite appearing so)
  - Cut (one metric removed entirely; rare, requires explicit user sign-off because metric IDs are stable)

**Locked decision (now):** any redundancy merges or cuts in v3.7 require explicit user sign-off per pair. Plan-mode pause before action.

**Effort:** highly variable, 0–5 days depending on count of redundancy candidates.

---

## Phase C — Bespoke deferred-pool scoping (input: v3.4 classification + v3.6 duplication review)

**Sketch only — detailed planning at v3.7 kick-off.**

The 5 pattern-may-not-fit metrics each need bespoke shape:

- **GV.OP-6 Adoption Rate & Selective Use Patterns** — the SUI threshold question is more about consultation-type taxonomy than tightening; needs a SUI-specific framing
- **GV.SG-9 Safety Performance Indicators with Thresholds (DSCMS)** — the metric *is* the threshold framework; tightening sub-blocks would be redundant, but the SPI taxonomy itself could be operationalised
- **GV.SG-11 Adverse Event / Incident Rate (LFPSE)** — LFPSE taxonomy gap acknowledged but not bridged; needs an LFPSE-AVT taxonomy proposal, not standard tightening
- **GV.SG-13 Assurance Debt Accumulation Rate** — surrogate-without-bounded-proxy-gap; needs the proxy gap bounded explicitly
- **HL.HF-3 Review-Before-Signing Rate** — the T_min thresholds are concrete but unvalidated; surrogate for review *quality*; needs a quality-bound or pairing rule

**Likely v3.7 scope:** scope and progress 1–2 of these (probably GV.SG-11 LFPSE-AVT taxonomy and HL.HF-3 quality-bound), defer the rest to v3.8+. Each is a research-grade proposal in its own right, not a mechanical tightening.

**Decision deferred to v3.7 kick-off:** which of the 5 to address first, based on (a) external feedback if any v3.5/v3.6 release attracts user comment, (b) whether the v3.6 duplication review reframes any of them.

**Effort:** ~5–10 days for 2 metrics, depending on substance.

---

## Phase D — Release wrap

CHANGELOG v3.7 entry covers all three phases. Header bump. Tightened-count narrative in `_how-to-use.md` updated.

Counts may change if Phase B includes any merges (decreases total from 216) or cuts. Tier split likely unchanged.

### Branching

- Branch `v3-7-pipeline-tightening-and-duplication-action` off `main@v3.6`
- Phase A as 1–2 commits
- Phase B as N commits depending on findings (one per merge/decision)
- Phase C as 1 commit per addressed deferred metric
- Phase D as final commit
- `--no-ff` merge, tag `v3.7`

---

## Critical files (sketch)

**Phase A:**
- `taxonomy/part-a/asr-transcription.md` (TP.ASR-12, TP.ASR-13)
- `taxonomy/part-a/epr-write-back.md` (TP.WB-2, TP.WB-3, TP.WB-4)
- `taxonomy/part-a/summarisation-nlp.md` (TP.SN-20)

**Phase B:**
- TBD per duplication-review findings

**Phase C:**
- TBD per metric chosen

**Phase D:**
- `CHANGELOG.md`, `taxonomy/_header.md`, `taxonomy/_how-to-use.md`

---

## Verification (end-to-end, sketch)

1. Build + audit clean
2. Tightening status manifest reaches **31/43** after Phase A
3. Duplication-review actions traceable to the v3.6 artefact (every redundancy decision references the pair from the artefact)
4. v3.5 / v3.6 follow-ups status — confirm none reopened by v3.7 changes
5. CHANGELOG v3.7 entry names the deferred metrics not addressed (so v3.8+ scope is auto-tracked)

---

## Out of scope (defer to v3.8+)

- Tier 2 / Tier 3 tightening — Tier 1 hasn't even completed yet; the pattern hasn't been validated against non-Tier-1 metrics
- Outcomes layer extension beyond ES.ME-8/9
- Roadmap (`_gaps.md`) candidate promotion — 89 candidates remain queued
- Stakeholder review process / public release — that's a separate workstream not yet scoped here
- Site-side improvements (procurement wizard, filter-by-context, etc. — flagged in earlier critique as missing but not on the tightening pipeline)

---

## Open questions for v3.7 kick-off

1. **Has v3.5 / v3.6 attracted external feedback?** If yes, that may reframe Phase B or C priorities.
2. **Is the user comfortable with merge / cut authority for redundant pairs?** The locked decision here is to require explicit per-pair sign-off; reaffirm at kick-off.
3. **Which of the 5 deferred metrics to address first?** GV.SG-11 (LFPSE-AVT taxonomy) is the most externally-relevant; HL.HF-3 (review-quality bound) is the most internally-coherent given v3.5's HL.HF-1 / HL.HF-4 pairing. Pick one or both.
