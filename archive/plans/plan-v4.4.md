# v4.4 plan — Pass B sweep over the v4.2/v4.3 ✓ set + catalogue-promotion-candidates formalisation

## Context

v4.2 + v4.3 verified Formal Definitions, References, and code snippets across all 221 metrics — but Pass B (external source fetching + claim-checking) only ran on the 38 source bundles where Pass A flagged ⚠ or 🔴 verdicts. The 138 metrics that cleared Pass A as ✓ have **internally coherent definitions and resolved citations**, but their specific external claims (numbers, thresholds, framework names attributed to real papers) were not independently verified against the cited sources.

The v4.2 finding pattern — "specific numbers attributed to real papers that don't actually contain them" — is exactly the failure mode Pass A doesn't catch, so a full Pass B sweep over the ✓ set is the right closing move on the verification methodology.

## Scope

### Phase 1 — pilot (HL + IO ✓ metrics from v4.3)

18 metrics. Smallest contained slice that exercises the full Pass B shape on previously-unverified metrics.

- HL: HF-1, HF-3, HF-3a, HF-3b, HF-7, HF-9, HF-11, HF-13, HF-14, HF-18 (10)
- IO: PX-1, PX-2, PX-3, PX-4, PX-5, PX-8, PX-9, PX-10 (8)

**Reviewer checkpoint after pilot.** Triage file with per-metric verdicts → user reviews → decide whether to continue full sweep, narrow to risk-weighted subset, or stop.

### Phase 2 — full sweep (post-pilot, pending review)

Remaining 120 ✓ metrics:

- v4.2: TP (41), IO.FE (7), ES.ME (6) — 54 metrics
- v4.3 (post-pilot): GV (57), PI (9) — 66 metrics

### Phase 3 — formalise v4.3 catalogue-promotion-candidates

5 future-promote inline references from `archive/v4.3/v4.3-catalogue-promotion-candidates.md`:

| Inline link | Location | v4.4 action |
|---|---|---|
| SCTK NIST scoring toolkit | TP.ASR-1 References block | Promote as `NIST-SCTK` |
| Woodard & Nelson 1982 NBS Report | TP.ASR-1 References block | Promote if verifiable URL is found; else leave as bare-prose historical credit |
| dscore (https://github.com/nryant/dscore) | TP.DI-1 References block | Promote as `dscore-Ryant` |
| philipchung/verifact | TP.SN-7b References block | Fold into `[Chung-NEJM-AI-2025]` metadata (no separate handle) |
| NEQAS analogy | HL.HF-6 References block | Likely keep inline — analogy/framework reference, not a primary source. Decide based on Pass B findings. |

### Phase 4 — release wrap

CHANGELOG, version bump v4.3.0 → v4.4.0, archive working files, tag, merge to main, push.

## Methodology (mirrors v4.2/v4.3)

For each ✓ metric with an external citation:

1. Identify cited sources (Source row + References block + inline `[Handle]` references)
2. Fetch source if not already cached at `reference-docs/` (gitignored)
3. Verify specific quantitative claims, framework names, threshold numbers, and operational definitions appear in the cited source
4. Record verdict per metric: ✓ verified / ~ minor reword / ⚠ softening needed / 🔴 confabulation needs fix

Triage files: `v4.4-clean-set-pilot-triage.md` (Phase 1) → reviewer checkpoint → `v4.4-clean-set-full-triage.md` (Phase 2 if continued).

## Verification (after each fix wave)

1. `uv run python taxonomy/build.py` — clean build, 221 metrics
2. `uv run python taxonomy/audit.py` — clean
3. `uv run pytest taxonomy/tests/ -q` — 99/99
4. `uv run python taxonomy/build_site.py` — clean
5. `uv run mkdocs build --strict` — clean

## Net effect (estimated)

If the v4.2 confabulation rate (18/92 ≈ 20%) holds on the ✓ set, expect ~25–28 corrections across 138 metrics. If much lower (since these passed Pass A clean), expect ~10–15. Counts unchanged. Catalogue may gain a handful of new handles for sources that turn out to be real and previously inline-only.

## Branch + tag

- Branch: `v4-4-clean-set-pass-b-sweep`
- Tag at release: `v4.4.0`
