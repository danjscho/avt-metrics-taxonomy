# Changelog — `avt-metrics-ref`

Per-package release history for the reference implementation library.
Independent of the catalogue release history (`/CHANGELOG.md`); this
file tracks only changes to the runnable companion package.

The package follows SemVer. Versioning conventions:

- **MAJOR** — breaking changes to function signatures or return types.
  Stays at 0 while the package is itself prototype-shaped.
- **MINOR** — new public functions or new optional features on existing
  functions.
- **PATCH** — bug fixes, dependency updates, internal refactors that
  preserve public behaviour.
- **`__catalogue_version__`** — bumped when a catalogue release modifies
  a Formal Definition for a metric this library implements, or when a
  new metric this library should cover lands in the catalogue. Decoupled
  from the package SemVer because the catalogue and the package release
  on different cadences.

## 0.3.1 (2026-05-09)

**Phase 6 of plan-reference-library: golden-corpus regression suite + plumbing.**

Added (no public API change):

- `tests/data/golden_corpus.jsonl` — 8-pair synthetic corpus across 4 speaker-group labels, deliberately tiny and synthetic. Job: detect silent metric-output drift when a dependency updates (jiwer averaging convention, rouge-score stemming, etc.). Not statistically meaningful or clinically realistic.
- `tests/test_golden_corpus.py` — 7 regression tests with pinned numerical results (1e-9 tolerance) for `wer` aggregate + per-pair, `cer` aggregate, `disaggregated_wer` per-group / equity-gap / threshold-met flag, `rouge` ROUGE-1 / ROUGE-L F1 on partial-overlap pairs, and `system_availability` band classification at three operating points.
- `pkg/avt_metrics_ref/CHANGELOG.md` — per-package release history (this file).

Other plumbing landed alongside (catalogue-side, not in the package):

- `.github/workflows/package.yml` — runs the package test suite on Python 3.10 / 3.11 / 3.12 on every push to `reference-library-pilot` (and PRs into it). Triggered only when `pkg/avt_metrics_ref/**` or the workflow file itself changes.
- `taxonomy/audit.py:check_reference_implementation_links` — new audit slice validates that every `**Reference implementation:**` cross-link in metric bodies points at a file that actually exists under `pkg/avt_metrics_ref/`. Skips on main where the package isn't checked out; ERROR-level on the pilot branch. Tested by deliberately breaking a link → audit catches it.

Package version 0.3.0 → 0.3.1 (regression-test additions + plumbing; no public API change).

## 0.3.0 (2026-05-09)

**Phase 2 of plan-reference-library: GV computational kernels.**

Added:

- **`system_availability(operational_minutes, down_minutes, ...)` — GV.OP-5.** Raw availability + optional degraded-aware effective availability + NAS-band classification (`meets-target` ≥99.5% / `below-target` 99.0–99.5% / `escalation` <99.0%). Thresholds configurable for local calibration per the Calibration & Context principle.
- **`degradation_detection_latency(onset_timestamps, detection_timestamps, ...)` — GV.SG-3.** Per-event latency in days, distribution summary (median / p90 / max), `meets_target` flag against the catalogue's 28-day target. The library only computes the latency; identifying drift events upstream (CUSUM, Page-Hinkley, sequential testing) is the caller's responsibility.

New module layout: `avt_metrics_ref.gv` is a flat namespace (no per-group sub-package) until multiple computational kernels accumulate within one GV group. Promote to `gv.op/`, `gv.sg/` when that happens.

Tests: 19 new (10 uptime + 9 latency).

`__catalogue_version__` unchanged at v5.5.12 (no FD edits required).

## 0.2.0 (2026-05-09)

**Phase 1 of plan-reference-library: TP.SN Reference-Based Text Similarity.**

Added:

- **`rouge(reference, hypothesis, variants=..., use_stemmer=True)` — TP.SN-1.** Wraps Google's `rouge-score`. Returns `RougeResult` with per-variant `RougeScore(precision, recall, f1)` for ROUGE-1, ROUGE-2, ROUGE-L. Single-pair or corpus-level inputs. Default Porter stemmer matches the standard ROUGE configuration.
- **`bertscore(references, hypotheses, model_type=..., ...)` — TP.SN-2.** Wraps the `bert-score` package. Behind the optional `[bertscore]` extra so the default install stays light (transformer model loading is heavy). Returns per-pair `BertScoreResult` with model + layer metadata recorded so reproducibility is auditable.

`bertscore` is reachable via `from avt_metrics_ref.tp.sn import bertscore` but is **not** exported at the top level so an `import avt_metrics_ref` doesn't force HuggingFace transformer loading. Lazy-import via `__getattr__` on the submodule.

Tests: 11 ROUGE + 4 BERTScore (skipif when extra not installed).

`__catalogue_version__` bumped v5.5.5 → v5.5.12 to reflect the v5.5.x baseline this release covers.

## 0.1.0 (2026-05-08)

**Initial pilot — TP.ASR cluster.**

Six functions covering the operationalisable subset of TP.ASR:

- `wer(reference, hypothesis, return_breakdown=False)` — TP.ASR-1, wraps `jiwer.wer` / `jiwer.process_words`.
- `medical_wer(reference, hypothesis, classifier, ...)` — TP.ASR-2, composes `jiwer.process_words` alignment with a user-supplied per-token classifier.
- `clinical_keyword_error_rate(reference, hypothesis, keyword_extractor, similarity_threshold=0.85)` — TP.ASR-3.
- `disaggregated_wer(group_pairs, threshold=0.05)` — TP.ASR-4. Composes `wer` per-group; returns per-group WER + n, equity gap, threshold-met flag, worst/best group, aggregate.
- `cer(reference, hypothesis)` — TP.ASR-8, wraps `jiwer.cer`.
- `asr_confidence_calibration(token_confidences, token_correctness, n_bins=10)` — TP.ASR-10. ECE + MCE via fixed-width binning; configurable bin count; per-bin breakdown for reliability-diagram rendering.

Tests: 51 unit tests across the six metrics.

`__catalogue_version__`: v5.5.5.
