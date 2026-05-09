# Plan — `reference-library-pilot` next steps

**Branch:** `reference-library-pilot` (not for merge to main until matured beyond the TP.ASR pilot).
**Package:** `pkg/avt_metrics_ref/`, version `0.1.0`, `__catalogue_version__ = "v5.5.5"`.

Right now the package covers six TP.ASR metrics (WER, M-WER, CK-ER, demographic-disaggregated WER, CER, ASR confidence calibration). Maturity goals before this branch is a serious candidate for merge:

1. Coverage extends beyond a single group so the package shape is exercised by metrics with different operationalisation patterns (text-similarity, generative-output evaluation, structured equity, lexicon-lookup).
2. The catalogue cross-links go in both directions and stay audit-checked.
3. CI runs the package tests so drift between catalogue Formal Definitions and library behaviour surfaces on every commit.
4. There is at least one reader who's not me using the library on real data and confirming the operationalisation carries weight.

Items below are ordered to deliver coverage breadth first (so the package's *shape* is interrogated), then plumbing (CI, audit, cross-links) once the shape is settled.

---

## 1. Extend coverage to TP.SN — text-similarity metrics

**Why first:** TP.ASR is one operationalisation pattern (token-edit-distance via jiwer). Text-similarity metrics are a different pattern — embedding-based or n-gram-based wrappers around external libraries, with no NHS-specific ground-truth assumption. Adding these stresses the package's "thin wrapper around well-established externals" assumption in a different direction.

**Targets:**

- **`TP.SN-1` ROUGE Scores** — wrap `rouge-score` (Google's reference implementation). Functions: `rouge_n(reference, hypothesis, n=2)` (ROUGE-1, -2), `rouge_l(reference, hypothesis)` (longest common subsequence). Returns named tuple of precision / recall / F1.
- **`TP.SN-2` BERTScore** — wrap `bert-score` Python package. Function: `bertscore(references, hypotheses, model="microsoft/deberta-xlarge-mnli", ...)`. Returns precision / recall / F1 per pair plus aggregate. Heavyweight dependency; mark as opt-in via extras (`pip install avt-metrics-ref[bertscore]`).

**Out of scope for this batch:** TP.SN-5 Hallucination Rate, TP.SN-6 Omission Rate (require human-rater workflows or LLM-judge pipelines, not just a function call). TP.SN-9 LLM-Judge family (same — needs a model-call abstraction we don't have yet).

**Acceptance:**

- Two new functions in `pkg/avt_metrics_ref/avt_metrics_ref/tp/sn/` (new sub-package).
- Public surface added to `__init__.py`.
- Tests in `pkg/avt_metrics_ref/tests/test_rouge.py` and `test_bertscore.py`.
- BERTScore behind an extras marker so the default install stays light.
- Catalogue **Reference implementation:** lines added on TP.SN-1 and TP.SN-2 metric bodies.

---

## 2. Extend coverage to GV.OP — operational metrics

**Why next:** Governance metrics are mostly process-attestation (no computational kernel — DPIA completion, board oversight, etc.). But a small subset *do* have computational kernels worth packaging, and they prove the package can grow into the GV cluster without needing every metric to come along. Picking one or two GV computational kernels also forces the question of whether the package's TP-shaped layout (`tp/asr/`) generalises sensibly to GV.

**Targets:**

- **`GV.OP-2` System Availability / Uptime** — function `system_availability(uptime_minutes, total_minutes)` returning the simple ratio + classification (≥99.5% / 99.0–99.5% / <99.0%) per the NAS Day Zero SPI threshold. Trivial in implementation; useful as a structural test of cross-cluster module organisation.
- **`GV.SG-3` Performance Degradation Detection Latency** — function `degradation_detection_latency(drift_signal_timestamps, detection_timestamps)` returning per-event latency + aggregate distribution + threshold-met flag. Computational kernel is small; framing of "drift signal" vs "detection" is the load-bearing part.

**Acceptance:**

- New `pkg/avt_metrics_ref/avt_metrics_ref/gv/` sub-package with `op/` and `sg/` modules.
- Tests in `pkg/avt_metrics_ref/tests/test_uptime.py` and `test_degradation_latency.py`.
- Catalogue cross-links on GV.OP-2 and GV.SG-3.
- Confirm the layout generalises — if `gv/op/uptime.py` feels forced for a one-function module, flatten to `gv/uptime.py`. Document the chosen convention in the package README.

---

## 3. CI: run the package tests on every commit

**Why:** Catalogue / library drift becomes invisible without CI. The package's `__catalogue_version__` is currently a hand-bumped pointer; CI gives us the early-warning signal that something has actually drifted.

**Tasks:**

- Add a `package-tests` job to `.github/workflows/build-deploy.yml` (or a new `.github/workflows/package.yml`) that:
  1. Sets up Python 3.12.
  2. `cd pkg/avt_metrics_ref/ && uv sync --extra test`.
  3. `uv run pytest -q`.
  4. Fails the build on any test failure.
- Triggers: every push to `reference-library-pilot`, plus every push to `main` (so a TP.ASR FD edit on main that breaks the package surfaces immediately when the branch is rebased).
- The job runs *in addition* to the existing catalogue audit + tests, not instead of.

**Acceptance:**

- Workflow file committed; CI passes on green.
- A deliberate test-breaking change confirms the workflow does fail loudly.

---

## 4. Catalogue audit: cross-link resolution

**Why:** The catalogue currently has six "**Reference implementation:**" lines pointing at GitHub blob URLs on the pilot branch. Right now nothing checks that the URL targets exist. If a function rename or file move on the pilot branch breaks the link, the catalogue silently rots.

**Tasks:**

- Add a new audit slice `check_reference_implementation_links` to `taxonomy/audit.py`:
  - Parse every metric body for a `**Reference implementation:**` line containing a `github.com/.../blob/reference-library-pilot/pkg/avt_metrics_ref/...` URL.
  - For each URL, check that the referenced file exists on disk under `pkg/avt_metrics_ref/` (since the pilot branch *is* the working tree when the audit runs from the pilot branch).
  - INFO-level on main (the pilot branch may not be checked out); ERROR-level on the pilot branch via a branch-aware skip.
  - Or simpler: just check existence whenever `pkg/avt_metrics_ref/` exists in the tree.
- Document the new audit slice in `taxonomy/README.md`.

**Acceptance:**

- Audit slice runs cleanly against current six cross-links.
- A deliberate broken link (rename a function in the package) trips the audit ERROR.

---

## 5. Per-package CHANGELOG + release notes

**Why:** `pkg/avt_metrics_ref/` doesn't yet have its own CHANGELOG. Once we add Phase 1 and Phase 2 metrics, the package version will move (0.1.0 → 0.2.0 for new functions; eventually 0.x.y for fixes), and a per-package CHANGELOG keeps the release record local.

**Tasks:**

- Add `pkg/avt_metrics_ref/CHANGELOG.md` with entries for `0.1.0` (the existing TP.ASR pilot) and `0.2.0` (Phase 1 — TP.SN coverage) once it ships.
- Document the package-vs-catalogue versioning convention in the package README (already partially documented; tighten with a short section on "when to bump package version vs `__catalogue_version__`").

**Acceptance:**

- CHANGELOG file exists with at least one entry.
- README has a "Versioning" section that names the bump triggers.

---

## 6. Golden-test corpora

**Why:** Current tests are unit-level (assertions on small synthetic inputs). For a public-facing reference implementation, a small golden-test corpus pinned in the repo provides reproducibility — anyone running the library against `tests/data/golden_corpus.jsonl` should get the same numbers.

**Tasks:**

- Add `pkg/avt_metrics_ref/tests/data/` with 1–2 small JSONL files: synthetic AVT-style transcripts (no real PHI), reference + hypothesis pairs, demographic group labels. Pure synthetic, openly licensed.
- Add a `test_golden_corpus.py` that runs every implemented metric against the corpus and asserts pinned numerical results (with a 1e-6 tolerance for floating-point).
- The corpus is not designed to be statistically meaningful — it's there to catch silent metric-output drift when a dependency updates.

**Acceptance:**

- Corpus committed under `pkg/avt_metrics_ref/tests/data/`.
- Golden test runs as part of `uv run pytest`.
- Updating any metric's behaviour requires updating the pinned numbers (which is a deliberate signal in the diff, not a silent drift).

---

## Sequencing

Phases 1 and 2 deliver coverage breadth; 3 and 4 deliver plumbing; 5 and 6 are nice-to-haves before the eventual "ready for review" milestone.

I'll work them in order: **Phase 1 (TP.SN)** → **Phase 2 (GV)** → **Phase 3 (CI)** → **Phase 4 (audit)** → **Phase 5 (CHANGELOG)** → **Phase 6 (golden corpus)**. Each phase ships as its own commit on the pilot branch with the package version bumped accordingly. None of these merge to main.
