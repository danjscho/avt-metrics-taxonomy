# Plan v4.2 — Formal Definition + Code Snippet verification (high-yield subset)

**Branch:** `v4-2-formal-definition-audit`
**Status:** in flight, started 2026-05-02.
**Source item:** plan-future #5 ("Verify code snippets *and* Formal Definitions against sources").

## Why this release

Every metric carries a **Formal Definition** block. Many were authored or edited by Claude during integration passes and have not been independently verified against the cited source. The v3.9 Phase 2 URL review surfaced multiple cases where Source-row *claims* didn't match the cited paper; the same drift is plausible in Formal Definitions and has not yet been checked. The Formal Definition is the load-bearing part of each metric — if it doesn't match what the source defines, downstream implementers measure something different from what the catalogue claims to standardise.

Code snippets sit alongside (~27 across 9 files). They should *implement* the Formal Definition; if they drift, the catalogue contradicts itself silently.

This release pairs the two as a single review per metric, on the assumption that snippet ↔ definition ↔ source must all agree.

## Subset (high-yield first)

v4.2 covers ~100 of 221 metrics. The remainder is queued for v4.3 (governance/compliance prose-heavy clusters where the yield-per-hour is lower).

In scope:

- **TP cluster (~80 metrics)** — Technical Pipeline. Highest density of mathematical / operational definitions and the most code snippets. The metrics most likely to drift from cited papers and the ones where drift causes the most downstream harm.
- **IO.FE (~10 metrics)** — Fairness & Equity. Paper-derived formulas (demographic parity, equal opportunity, equalised odds, intersectional metrics). Definitions are formula-precise and source-traceable; high yield.
- **ES.ME (~9 metrics)** — Meta-evaluation. Citation-heavy, references published evaluation methodology; benefits from source verification.

Out of scope (v4.3 candidates):

- GV cluster — mostly compliance prose where Source rows already point at regulations/standards, and Formal Definitions are operational rather than mathematical. Lower yield-per-hour.
- HL cluster — workflow / human-factors metrics. Definitions are constructs, not formulas; source verification is a different shape (qualitative-research literature).
- IO.PX (Patient Experience) and PI (Pipeline Interactions) — mixed; queue for v4.3 with GV.

## Triage categories

Applied per metric during Pass A:

| Symbol | Meaning | Action |
|--------|---------|--------|
| ✓ | Match | Definition aligns with source. No action. |
| ~ | Rewording | Substance is right; prose is loose / informal / unclear. Fix opportunistically; doesn't block release. |
| ⚠ | Softening needed | Definition overclaims (cites validation that's preliminary; threshold quoted as if from source when it's our extrapolation). Rewrite to match what the source actually supports. **Mandatory fix.** |
| 🔴 | Actual problem | Definition contradicts the source, cites wrong paper, or describes a metric different from what the source defines. **Mandatory fix.** |

The ~ vs ⚠ distinction matters: ~ is "we said it well-enough but could say it better"; ⚠ is "we said something the source doesn't actually support". Most of the value of this release is separating these two cleanly.

## Phases

### Phase 1 — Formal Definition triage (Pass A, internal coherence)

For each metric in the subset, check internal consistency:

- Does the Formal Definition match the Reference Standard / Threshold Guidance prose?
- Does the Source-row handle resolve to a citation that plausibly defines what the Formal Definition claims?
- Are units, ranges, and operational rules self-consistent?

Output: `v4.2-fd-triage.md` at repo root. One row per metric:

```
| Ref ID | Metric | Category | Note |
|--------|--------|----------|------|
| TP.AC-1 | Signal-to-Noise Ratio Monitoring | ✓ | — |
| TP.ASR-1 | Word Error Rate | ~ | "lower is better" prose; could state range explicitly |
| TP.SN-7a | Confabulation Detection | ⚠ | Source-row cites Croxford-2025 but FD describes a different operational rule |
```

Pass A is fast (~5 min/metric × ~100 metrics ≈ 8 hours). No fixes during Pass A — we want the full picture before deciding how to land.

### Phase 2 — Formal Definition verification (Pass B, external sources)

For each metric flagged ⚠ or 🔴 in Pass A, plus a sampled ~10% of ✓s as a sanity check, fetch the cited source and verify the Formal Definition against the actual paper / standard text.

Pass B catches:

- Confabulated formulas (definition that "looks right" but isn't in the source).
- Citation drift (right concept, wrong paper).
- Threshold numbers attributed to a source that doesn't state them.

Output: triage rows updated with Pass B findings, escalating ~→⚠ or ⚠→🔴 where warranted.

### Phase 3 — Apply fixes

- **🔴 Actual problems:** mandatory. Fix definition, source row, or both. May require re-tiering or re-classifying if the drift is large enough that the metric isn't what we said it was.
- **⚠ Softenings:** mandatory. Reword to match what the source actually supports. Add ⚠ Provenance prelude where missing.
- **~ Rewordings:** opportunistic. Bundle into the same commit per file to keep the diff focused.

### Phase 4 — Code snippet verification

~15 of the 27 snippets fall in the TP subset. For each:

- Does the snippet implement the Formal Definition for the metric it sits under?
- Do imports / APIs match the current version of the cited library (pyannote, scikit-learn, dscore, FHIR validators)?
- Is the snippet runnable as-shown, or illustrative-only? (Either is fine; the prose around it should match the choice.)

Most snippets are illustrative. The work is checking that none have bit-rotted past the point of being misleading.

### Phase 5 — Release wrap

- CHANGELOG entry summarising counts: total reviewed, ✓/~/⚠/🔴 split, list of metrics with substantive fixes.
- Update plan-future to remove #5.
- Audit + pytest + build + build_site + mkdocs strict clean.
- TAXONOMY_VERSION → v4.2.0; pyproject.toml → 4.2.0.
- Tag v4.2.0; merge to main.

## Sequencing inside Phase 1

To keep velocity, work through the subset in dependency order:

1. **TP.AC** (audio capture, 9 metrics) — physical signal metrics; sources are signal-processing literature.
2. **TP.ASR** (transcription, 14 metrics) — WER family; sources are speech-recognition literature.
3. **TP.DI** (diarisation, 9 metrics) — DER family; sources are pyannote / dscore.
4. **TP.SN** (summarisation/NLP, ~25 metrics) — largest group, includes named families (Clinical Content Fidelity, Reference-Based Text Similarity, LLM-Judge methodology).
5. **TP.CC** (clinical coding, ~11 metrics) — SNOMED / dm+d / ICD-10 alignment.
6. **TP.WB** (downstream write-back, ~10 metrics) — FHIR / HL7 / EPR integration.
7. **IO.FE** (fairness & equity, ~10 metrics).
8. **ES.ME** (meta-evaluation, ~9 metrics).

## Out-of-scope decisions (locked)

- v4.2 is **content-correctness only** — no new metrics, no tier shifts (unless a 🔴 forces re-classification), no structural changes.
- v4.2 does not re-do the v3.9 reference catalogue work — Source rows already point at handles in `_references.md`. The audit here is whether the *Formal Definition* matches what those handles cite, not whether the handles themselves are correct.
- v4.2 does not pursue snippet runnability — illustrative snippets are fine. The bar is "doesn't actively mislead".

## Success criteria

- Triage table covers all ~100 in-scope metrics with one of ✓ / ~ / ⚠ / 🔴.
- All 🔴 and ⚠ rows have landed fixes.
- No regressions: audit clean, pytest 88/88, build clean, mkdocs strict clean.
- CHANGELOG describes the substantive fixes (not just "reviewed everything").
- Plan-future #5 either removed (if all subset items shipped clean) or rescoped to remaining clusters (GV / HL / IO.PX / PI).
