# avt-metrics-ref

**Reference implementations of metrics from the [AVT Metrics Taxonomy](https://danjscho.github.io/avt-metrics-taxonomy/).** Coverage spans five clusters; full per-metric table below.

> ⚠️ **Prototype-for-discussion.** This library is a runnable companion to a prototype taxonomy. The functions implement the catalogue's Formal Definitions but cannot guarantee that any given input/output behaviour matches every reasonable reading. **Verify before relying on the numbers in contractual or academic contexts.** See the catalogue's [prototype-status framing](https://danjscho.github.io/avt-metrics-taxonomy/prototype-status/) for the broader context.

## What this is

The AVT Metrics Taxonomy is documentation. Each metric has a Formal Definition that describes how to compute it, but two readers of the same definition can produce subtly different operationalisations — especially around tokenisation, edge cases, and per-class weighting.

This library is **one reference operationalisation** of that documentation, made runnable so that:

- Two deployers measuring the same metric apply the same kernel (assuming they choose the same domain models — see "What this is not").
- Operationalisation ambiguities surface as test failures rather than silent disagreements.
- The catalogue's "AI-coauthored prototype for discussion" framing applies to the code as well as the documentation — disagreement is welcome and tracked.

The library version (currently `0.4.0`) is independent of the catalogue version (currently `v5.5.12`). The package follows SemVer; the catalogue follows the convention documented in [`taxonomy/_versioning.md`](https://github.com/danjscho/avt-metrics-taxonomy/blob/main/taxonomy/_versioning.md). The package's `__catalogue_version__` attribute records which catalogue release it was authored against.

## What this is not

- **Not a clinical decision support system.** Nothing here makes patient-level decisions or replaces clinician judgement.
- **Not a benchmarking dataset.** No reference transcripts, no demographic-labelled corpora, no pre-trained models. The library expects the caller to supply data.
- **Not a clinical NER.** Several metrics (M-WER, CK-ER) require a domain-specific tokeniser/extractor; the library's signature exposes that dependency rather than embedding a specific model. MedCAT, scispaCy, custom regex — all are reasonable choices the caller makes.
- **Not a human-rater workflow.** Metrics that require human review (Hallucination Rate TP.SN-5, Omission Rate TP.SN-6, PDSQI-9 TP.SN-3, CREOLA TP.SN-4, LLM-Judge TP.SN-9) are deliberately out of scope — the library only covers metrics with a direct computational kernel.
- **Not validated for procurement contracts or regulatory submission.** Cite at your own risk; pair with the catalogue's prototype-status disclaimer if you do.
- **Not a replacement for the catalogue itself.** When the documentation and the code disagree, the documentation is the *intent*; the code is one operationalisation that may need fixing.

## Coverage

| Catalogue ref | Function | Cluster · Group | Notes |
|---|---|---|---|
| TP.ASR-1 | `wer(reference, hypothesis)` | TP · ASR | Wraps `jiwer.wer`; optional breakdown into substitutions / deletions / insertions / hits |
| TP.ASR-2 | `medical_wer(ref, hyp, classifier=...)` | TP · ASR | Composes `jiwer.process_words` alignment with a user-supplied per-token classifier |
| TP.ASR-3 | `clinical_keyword_error_rate(ref, hyp, extractor=...)` | TP · ASR | User-supplied keyword extractor; library does Levenshtein-ratio similarity matching |
| TP.ASR-4 | `disaggregated_wer(samples, ...)` | TP · ASR | Per-group WER + equity gap; NAS 5pp threshold default |
| TP.ASR-8 | `cer(reference, hypothesis)` | TP · ASR | Wraps `jiwer.cer` |
| TP.ASR-10 | `asr_confidence_calibration(confs, correctness)` | TP · ASR | Expected + Maximum Calibration Error via fixed-width binning |
| TP.SN-1 | `rouge(reference, hypothesis, ...)` | TP · SN (Reference-Based Text Similarity family) | Wraps Google's `rouge-score`; ROUGE-1 / ROUGE-2 / ROUGE-L precision-recall-F1 |
| TP.SN-2 | `bertscore(references, hypotheses, ...)` | TP · SN (Reference-Based Text Similarity family) | Wraps `bert-score`; **behind the `[bertscore]` extra** so the default install stays light |
| TP.WB-2 | `integration_error_rate(events, ...)` | TP · WB | Per-error-type / per-severity / per-EPR breakdown + NAS-band classification with critical-event escalation |
| HL.HF-1 | `edit_rate(events, baseline_pct=None, ...)` | HL · HF | Aggregate ER + severity stratification + per-clinician breakdown + complacency-alert / pause-trigger classification |
| HL.HF-3a | `review_before_signing_rate(events, ...)` | HL · HF | T_min computed per the catalogue; NAS-band classification (≥95% target / <85% pause) |
| HL.HF-3b | `time_to_sign_distribution(events, ...)` | HL · HF | Distribution percentiles + rubber-stamp count + very-fast-on-long-note count |
| IO.FE-1 | `deployment_equity_index(bucket_to_rate, ...)` | IO · FE (Demographic Equity Disaggregation family) | Pearson r between deployment rate and ordered demographic axis + band classification |
| GV.OP-5 | `system_availability(operational_minutes, down_minutes, ...)` | GV · OP | Raw + degraded-aware availability + NAS-band classification (99.5% target / 99.0% pause) |
| GV.SG-3 | `degradation_detection_latency(onsets, detections, ...)` | GV · SG | Per-event latency + distribution summary + meets-target flag against the catalogue 28-day target |

The coverage table is hand-curated; the public API surface lives in [`avt_metrics_ref/__init__.py:__all__`](avt_metrics_ref/__init__.py) and is the single source of truth — every function listed above must appear there. CI catches drift via the `package.yml` workflow's import-surface sanity check.

### Deliberately out of scope

- **TP.ASR-5 / -7 / -9 / -11 / -12 / -13 / -14** — speaker-stratified WER (needs diarisation), RTF (operational not transcription-quality), OOV rate, confidence exposure, hallucination-under-noise, numeric accuracy, punctuation/capitalisation. Pilot omissions; no architectural reason they couldn't land.
- **TP.SN-3 / -4 / -5 / -6 / -7 / -9 / -11 / -12 / -13 / -14 / -15+** — anything requiring human-rater review, LLM-judge pipelines, or NLI inference. The pilot deliberately avoids the LLM-call abstraction; revisit if external pull is strong.
- **TP.AC, TP.DI, TP.CC** — audio capture, diarisation, clinical coding. No coverage yet.
- **TP.WB-1 / -3 / -4** — write-back fidelity, field mapping accuracy, update vs append. Need a per-EPR adapter pattern this library has not committed to.
- **HL.HF-2 / -4+** — vendor-scale automation-bias and re-record metrics outside the Tier 1 telemetry triplet.
- **GV cluster (most of it)** — the GV cluster is process-attestation-heavy (DPIA completion, board oversight, clinical safety case, etc.) and has no computational kernel. Only the small computational subset is in scope.
- **IO.FE-2+, IO.PX, ES.ME** — most of the impact-and-outcomes and meta-evaluation surface needs human review or qualitative judgement.

## Install

```bash
# Default install (lightweight; covers all metrics except BERTScore)
pip install avt-metrics-ref

# Add the BERTScore extra (loads HuggingFace transformers; ~1.5 GB model)
pip install 'avt-metrics-ref[bertscore]'
```

Or from source while the package is on the `reference-library-pilot` branch:

```bash
git clone https://github.com/danjscho/avt-metrics-taxonomy
cd avt-metrics-taxonomy
git checkout reference-library-pilot
pip install -e pkg/avt_metrics_ref
# or with the bertscore extra:
pip install -e 'pkg/avt_metrics_ref[bertscore]'
```

## Quickstart

```python
from avt_metrics_ref import wer, cer, disaggregated_wer, rouge

# TP.ASR-1: aggregate WER
print(wer("the patient reports chest pain",
          "the patient reports chess pain"))
# → 0.2

# TP.ASR-8: CER for clinical near-misses
print(cer("amoxicillin 500mg",
          "amoxycillin 500mg"))
# → 0.058...

# TP.ASR-4: demographic-disaggregated WER
samples = [
    {"reference": "the patient", "hypothesis": "the patient", "group": "GB"},
    {"reference": "the patient", "hypothesis": "the patient", "group": "GB"},
    {"reference": "she said hello", "hypothesis": "she said yellow", "group": "EAL"},
]
result = disaggregated_wer(samples, threshold=0.05)
print(result["equity_gap"])         # 0.333...
print(result["threshold_met"])      # False
print(result["worst_group"])        # "EAL"

# TP.SN-1: ROUGE
r = rouge("the patient has cough and fever",
          "patient has cough and fever today")
print(round(r.rouge1.f1, 2))
# → 0.86
```

For metrics requiring user-supplied classifiers (M-WER, CK-ER), see the per-function docstring for the expected signature.

## Worked example: assurance dashboard slice

A concrete worked example showing how the library composes across clusters: take a synthetic week of AVT events, compute every applicable metric, surface NAS-band flags. This is the shape of a per-deployment governance report — every line below is data the catalogue says you need to be tracking anyway.

```python
from datetime import datetime, timedelta
from avt_metrics_ref import (
    wer, disaggregated_wer, rouge,
    edit_rate, review_before_signing_rate, time_to_sign_distribution,
    integration_error_rate,
    deployment_equity_index,
    system_availability, degradation_detection_latency,
    disclaimer,
)

# --- Synthetic events for a week of operation -----------------------------

# 1. ASR transcription quality (TP.ASR-1, TP.ASR-4)
asr_samples = [
    {"reference": "the patient has type two diabetes", "hypothesis": "the patient has type two diabetes", "group": "british-rp"},
    {"reference": "blood pressure is one forty over ninety", "hypothesis": "blood pressure is one forty over ninety", "group": "british-rp"},
    {"reference": "she takes metformin five hundred milligrams", "hypothesis": "she takes metformin five hundred milligram", "group": "scottish"},
    {"reference": "no history of cardiovascular disease", "hypothesis": "no history of cardiovascular disease", "group": "scottish"},
]

# 2. Note-level human-factors telemetry (HL.HF-1 / -3a / -3b)
#    Each note is one (clinician, edit_state, review_signals, sign_time) tuple.
g = datetime(2026, 5, 5, 9, 0)
note_events = [
    {"clinician_id": "A", "edited": True,  "edit_severity": "clinically_meaningful",
     "word_count": 220, "edit_events": 4, "scroll_events": 2, "dwell_seconds": 90,
     "generated_at": g, "approved_at": g + timedelta(seconds=120)},
    {"clinician_id": "A", "edited": True,  "edit_severity": "stylistic",
     "word_count": 150, "edit_events": 1, "scroll_events": 1, "dwell_seconds": 60,
     "generated_at": g, "approved_at": g + timedelta(seconds=80)},
    {"clinician_id": "B", "edited": False,
     "word_count": 250, "edit_events": 0, "scroll_events": 0, "dwell_seconds": 4,
     "generated_at": g, "approved_at": g + timedelta(seconds=4)},  # <-- rubber-stamp
]

# 3. Write-back integration events (TP.WB-2)
wb_events = (
    [{"success": True}] * 998
    + [{"success": False, "error_type": "partial", "severity": "moderate"}] * 2
)

# 4. System availability (GV.OP-5)
ops_events = {"operational_minutes": 10080, "down_minutes": 30}  # 99.7% — meets NAS

# 5. Deployment equity (IO.FE-1)
imd_to_coverage = {
    1: 0.20, 2: 0.25, 3: 0.30, 4: 0.40, 5: 0.45,
    6: 0.55, 7: 0.65, 8: 0.70, 9: 0.80, 10: 0.85,
}

# --- Compute --------------------------------------------------------------

agg_wer = wer([s["reference"] for s in asr_samples],
              [s["hypothesis"] for s in asr_samples])
fairness = disaggregated_wer(asr_samples, group_key="group")
er = edit_rate(note_events)
rbs = review_before_signing_rate(note_events)
tts = time_to_sign_distribution(note_events)
ier = integration_error_rate(wb_events)
avail = system_availability(**ops_events)
equity = deployment_equity_index(imd_to_coverage)

# --- Report ---------------------------------------------------------------

print(disclaimer())
print()
print(f"ASR    | aggregate WER:           {agg_wer:.3f}")
print(f"       | demographic gap:         {fairness['equity_gap']:.3f}  ({'meets' if fairness['threshold_met'] else 'fails'} 5pp NAS gate)")
print(f"HL     | edit rate:               {er.edit_rate_pct:.0f}%  ({er.classification})")
print(f"       | review-before-sign:      {rbs.rbs_pct:.0f}%  ({rbs.classification})")
print(f"       | time-to-sign median:     {tts.median_seconds:.0f}s")
print(f"       | rubber-stamp flagged:    {tts.n_rubber_stamp_flag}/{tts.n_notes}  (very-fast on long notes: {tts.n_very_fast_long_note})")
print(f"WB     | integration error rate:  {ier.ier:.4f}  ({ier.classification})")
print(f"OPS    | uptime:                  {avail.availability_pct:.2f}%  ({avail.classification})")
print(f"EQUITY | IMD r:                   {equity.pearson_r:+.3f}  ({equity.direction}, {equity.classification})")
```

Run it on real data; treat any non-`meets-target` band as a calibration discussion, not a failed audit.

## Disclaimer

The library exposes `disclaimer()` as a runtime-callable string. Recommended: include in any publication, dashboard, or contract that cites the package output:

```python
from avt_metrics_ref import disclaimer
print(disclaimer())
# → "avt-metrics-ref v0.4.0 — prototype-for-discussion companion to AVT Metrics
#    Taxonomy v5.5.12. Not validated for production decisions, clinical decision
#    support, or contractual thresholds. See https://danjscho.github.io/avt-metrics-taxonomy/
#    for the canonical catalogue and the prototype-status framing."
```

## Versioning

- **Package version (`__version__`)** follows SemVer. `0.x.0` is alpha — the major stays 0 while the package is itself prototype-shaped.
- **Catalogue version (`__catalogue_version__`)** records the AVT Metrics Taxonomy release this package was authored against. Bumped when a catalogue release modifies a Formal Definition for a metric this library implements, or when a new in-scope metric lands.
- **Independent release cadences** — catalogue releases that don't touch implemented Formal Definitions don't bump the package version; package patches that don't change behaviour don't bump the catalogue version.

Per-package CHANGELOG: [`CHANGELOG.md`](CHANGELOG.md).

## Reporting issues

Bug reports, factual disagreements about the operationalisation, missing metrics — all welcome. Use the catalogue's [GitHub issue templates](https://github.com/danjscho/avt-metrics-taxonomy/issues/new/choose); the **Factual error** template is the right shape for "this function disagrees with the catalogue's Formal Definition".

## Contributing

The pilot is feature-complete for its current scope (TP.ASR + TP.SN Reference-Based Text Similarity + TP.WB-2 + HL Tier 1 telemetry triplet + GV computational subset + IO.FE-1). Reasonable next directions:

1. **Cluster expansion** — TP.AC (audio-quality metrics), TP.DI (diarisation), or further into TP.WB (FHIR conformance, PRSB completeness via per-EPR adapter pattern).
2. **Tighten existing functions** — the M-WER and CK-ER signatures push the domain-NER choice onto the caller, which is honest but creates an integration tax. A reference NER bundle would lower that tax for the common case.
3. **Worked-example notebooks** — the README includes a single composed example. A notebook per cluster, with synthetic data and explicit calibration prompts, would be more useful for a deployer's first read.

PRs welcome on any axis. The maintenance commitment is honest about itself: this is a prototype companion to a prototype catalogue, and the library will only be expanded when there is genuine pull from people actually running it on real data.

## License

MIT — see [LICENSE](LICENSE).
