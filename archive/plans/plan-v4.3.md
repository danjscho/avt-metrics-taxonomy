# Plan v4.3 — Formal Definition + code snippet verification (remaining clusters)

**Branch:** `v4-3-remaining-clusters-verification`
**Status:** in flight, started 2026-05-03.
**Source item:** plan-future #5 (originally), continuing v4.2's verification methodology to the remaining clusters.
**Decision recap:** Option A (full extension) with code-snippet verification included.

## Why this release

v4.2 verified Formal Definitions + code snippets across the **TP cluster + IO.FE + ES.ME** subset (92 metrics) against cited sources. 18 metrics surfaced as 🔴 (confabulated source attributions). This release extends the same Pass A / Pass B methodology to the remaining clusters — **GV, HL, PI, IO.PX** — so every metric in the taxonomy has been source-verified at least once.

## Subset (Option A — full extension)

**~134 metrics across:**

- **GV cluster (~81 metrics across 8 group files):**
  - GV.SG Safety & Governance (~17 metrics)
  - GV.CR NHS Compliance & Regulatory (~10)
  - GV.SC Security & Adversarial Robustness (~12)
  - GV.PD Privacy & Data Governance (~12)
  - GV.OP Operational (~10)
  - GV.EN Environmental & Sustainability (~3)
  - GV.TC Training & Competency (~5)
  - GV.VT Vendor Transparency & Contractual (~11)
- **HL cluster (~21 metrics):**
  - HL.HF Human Factors & Workflow (~21)
- **PI cluster (~21 metrics across 2 files):**
  - PI.PP Partial-Pipeline (~9)
  - PI.E2E End-to-End Pipeline (~12)
- **IO.PX (~11 metrics):**
  - Patient Experience (~11)

**Code snippets in scope:** 12 (9 PI, 2 HL, 1 GV) — picked up from v4.2 Phase 4 triage out-of-scope list.

## Triage categories (unchanged from v4.2)

| Symbol | Meaning | Action |
|--------|---------|--------|
| ✓ | Match | No action. |
| ~ | Rewording | Substance right; prose loose. Opportunistic. |
| ⚠ | Softening needed | Definition overclaims. Mandatory fix. |
| 🔴 | Actual problem | Definition contradicts source / wrong citation. Mandatory fix. |

## Phases (mirroring v4.2)

### Phase 1 — Pass A: Formal Definition triage (internal coherence)

Read each metric in the subset; check Formal Definition ↔ Reference Standard ↔ Threshold Guidance ↔ Source row consistency. No external fetches. Output: `v4.3-fd-triage.md`.

**Sequencing inside Phase 1:**

1. **HL.HF (21 metrics)** — paper-grounded constructs, expected highest 🔴 yield-per-hour outside TP cluster.
2. **IO.PX (11 metrics)** — patient experience, paper citations.
3. **PI.E2E + PI.PP (21 metrics)** — composite end-to-end metrics; downstream-paper citations.
4. **GV.SC (12 metrics)** — security & adversarial robustness; paper-cited research framework.
5. **GV.SG (17 metrics)** — safety & governance.
6. **GV.PD (12 metrics)** — privacy & data governance.
7. **GV.CR (10 metrics)** — NHS compliance & regulatory.
8. **GV.OP (10 metrics)** — operational.
9. **GV.VT (11 metrics)** — vendor transparency.
10. **GV.TC (5 metrics)** — training & competency.
11. **GV.EN (3 metrics)** — environmental & sustainability.

Order is roughly *highest-likelihood-of-confabulation first* so any pattern surfaces early enough to inform Pass B prioritisation.

### Phase 2 — Pass B: External source verification

For each metric flagged ⚠ or 🔴 in Pass A, fetch the cited source and verify the specific claim. Cache excerpts at `reference-docs/v4.3-pass-b/` (gitignored, same convention as v4.2).

Bundles to expect (the cluster shape predicts the pattern):

- **HL.HF** — likely paper bundles around: PDSQI/PDQI sub-citations distinct from the Croxford catalogue handles; automation-bias literature (Mosier et al., Parasuraman); review-before-signing rate work.
- **IO.PX** — patient-experience research literature; medication error rate pre/post-AVT studies.
- **PI** — end-to-end evaluation papers; partial-pipeline composition methodologies.
- **GV.SC** — adversarial-ML literature already partly catalogued (Carlini, Biggio); prompt-injection research; data-poisoning papers.
- **GV.SG, GV.CR, GV.PD, GV.OP, GV.VT, GV.TC, GV.EN** — mostly regulation citations (DCB0129/0160, UK GDPR, NHSE IG Guidance, MHRA SaMD, NICE ESF, CQC, PSIRF, NHS T.E.S.T., NHS BSA dm+d, NHS Digital OPCS-4, NHSE AVT Registry). Verification shape here is "does the cited regulation say what we claim it says?" — different from paper verification.

### Phase 3 — Apply fixes

- **🔴 Actual problems:** mandatory.
- **⚠ Softenings:** mandatory.
- **~ Rewordings:** opportunistic, bundled per file.
- **Catalogue work:** new handles where citations need promotion; renames / removals where verification surfaces wrong attribution; author corrections where v4.2-style mismatches exist.

### Phase 4 — Code snippet verification (12 snippets)

Same triage as v4.2 Phase 4. Snippets to verify (from v4.2-phase4-snippet-triage.md):

- **gv/nhs-compliance-regulatory.md:163** (GV.CR snippet)
- **hl/human-factors-workflow.md:57** (HL snippet 1)
- **hl/human-factors-workflow.md:300** (HL snippet 2)
- **pi/end-to-end-pipeline.md:32, 153, 226, 346, 422** (5 PI E2E snippets)
- **pi/partial-pipeline.md:32, 143, 249, 361** (4 PI PP snippets)

### Phase 5 — Release wrap

- CHANGELOG entry summarising counts: total reviewed (~134), ✓/~/⚠/🔴 split, list of metrics with substantive fixes.
- Update plan-future to remove #5 if the v4.2 partial-removal needs finalising (or note that v4.2 + v4.3 together close it).
- Audit + pytest + build + build_site + mkdocs strict clean.
- TAXONOMY_VERSION → v4.3.0; pyproject.toml → 4.3.0.
- Tag v4.3.0; merge to main; push.

## Out-of-scope decisions (locked)

- **Threshold-numbers review (plan-future #8)** — separate design item. v4.3 only adds ⚠ Provenance preludes where v4.2's pattern requires; full review remains deferred.
- **Tier 1 gap review (plan-future #4)** — separate substantive release. Better-foundationed after v4.3 but not part of it.
- **ISO/BSI standards (plan-future #9)** — separate new-framework release. Out of scope.
- **Audit-side ratchets** (Option C from scoping) — interesting but out of v4.3 scope. Capture in plan-future after v4.3 ships.

## Success criteria

- Triage table covers all ~134 in-scope metrics with one of ✓ / ~ / ⚠ / 🔴.
- All 🔴 and ⚠ rows have landed fixes with verified attributions.
- All 12 code snippets verified, with any pseudocode-vs-real-API issues clarified.
- CHANGELOG describes the substantive fixes (not just "reviewed everything").
- plan-future #5 fully closed.
- No regressions: audit clean, pytest 99/99 (or higher if new tests), build clean, mkdocs strict clean.

## Working files

- `plan-v4.3.md` (this file) — release plan
- `v4.3-fd-triage.md` (to be created in Phase 1) — Pass A/B triage table
- `v4.3-fd-triage-review.md` (to be created if 🔴/⚠ count is large enough to warrant) — reviewer verdicts
- `v4.3-phase3-sweeps-review.md` (to be created if a sweep-shape pattern surfaces, e.g. broader Provenance prelude additions)
- `v4.3-phase4-snippet-triage.md` (to be created in Phase 4) — code snippet triage
- `v4.3-catalogue-promotion-candidates.md` (to be created if new candidates surface)
- `reference-docs/v4.3-pass-b/` (gitignored) — local source caches
