# avt-metrics-ref

**Reference implementations of metrics from the [AVT Metrics Taxonomy](https://danjscho.github.io/avt-metrics-taxonomy/).** Pilot scope: TP.ASR cluster only.

> ⚠️ **Prototype-for-discussion.** This library is a runnable companion to a prototype taxonomy. The functions implement the catalogue's Formal Definitions but cannot guarantee that any given input/output behaviour matches every reasonable reading. **Verify before relying on the numbers in contractual or academic contexts.** See the catalogue's [prototype-status framing](https://danjscho.github.io/avt-metrics-taxonomy/prototype-status/) for the broader context.

## What this is

The AVT Metrics Taxonomy is documentation. Each metric has a Formal Definition that describes how to compute it, but two readers of the same definition can produce subtly different operationalisations — especially around tokenisation, edge cases, and per-class weighting.

This library is **one reference operationalisation** of that documentation, made runnable so that:

- Two deployers measuring the same metric apply the same kernel (assuming they choose the same domain models — see "What this is not").
- Operationalisation ambiguities surface as test failures rather than silent disagreements.
- The catalogue's "AI-coauthored prototype for discussion" framing applies to the code as well as the documentation — disagreement is welcome and tracked.

The library version (currently `0.1.0`) is independent of the catalogue version (currently `v5.5.5`). The package follows SemVer; the catalogue follows the convention documented in [`taxonomy/_versioning.md`](https://github.com/danjscho/avt-metrics-taxonomy/blob/main/taxonomy/_versioning.md). The package's `__catalogue_version__` attribute records which catalogue release it was authored against.

## What this is not

- **Not a clinical decision support system.** Nothing here makes patient-level decisions or replaces clinician judgement.
- **Not a benchmarking dataset.** No reference transcripts, no demographic-labelled corpora, no pre-trained models. The library expects the caller to supply data.
- **Not a clinical NER.** Several metrics (M-WER, CK-ER) require a domain-specific tokeniser/extractor; the library's signature exposes that dependency rather than embedding a specific model. MedCAT, scispaCy, custom regex — all are reasonable choices the caller makes.
- **Not validated for procurement contracts or regulatory submission.** Cite at your own risk; pair with the catalogue's prototype-status disclaimer if you do.
- **Not a replacement for the catalogue itself.** When the documentation and the code disagree, the documentation is the *intent*; the code is one operationalisation that may need fixing.

## Pilot scope: TP.ASR

| Catalogue ref | Function | Wraps | Notes |
|---|---|---|---|
| TP.ASR-1 | `wer(reference, hypothesis)` | `jiwer.wer` | Identical to jiwer's WER; convenience wrapper with optional breakdown |
| TP.ASR-8 | `cer(reference, hypothesis)` | `jiwer.cer` | Character-level error rate; useful for near-miss clinical terms |
| TP.ASR-2 | `medical_wer(ref, hyp, classifier=...)` | `jiwer.process_words` + per-token weights | Composes alignment with user-supplied classifier; default weight matrix matches the catalogue snippet |
| TP.ASR-3 | `clinical_keyword_error_rate(ref, hyp, extractor=...)` | own Levenshtein matcher | User-supplied keyword extractor; library does the similarity matching |
| TP.ASR-4 | `disaggregated_wer(samples, ...)` | composes `wer` | Per-group WER + equity gap; NAS 5pp threshold default |
| TP.ASR-10 | `asr_confidence_calibration(confs, correctness)` | own ECE/MCE | Expected and Maximum Calibration Error via fixed-width binning |

**Out of pilot scope** (see `tp/asr/__init__.py` docstring): TP.ASR-5 Speaker-Stratified WER (needs diarisation), TP.ASR-6 Error Transmission Rate (cross-stage pipeline-level), TP.ASR-7 RTF (operational not transcription-quality), TP.ASR-9 OOV Rate, TP.ASR-11 Confidence Exposure, TP.ASR-12 Hallucination-Under-Noise, TP.ASR-13 Numeric Accuracy, TP.ASR-14 Punctuation & Capitalisation.

## Install

```bash
pip install avt-metrics-ref
```

Or from source while the package is on the `reference-library-pilot` branch:

```bash
git clone https://github.com/danjscho/avt-metrics-taxonomy
cd avt-metrics-taxonomy
git checkout reference-library-pilot
pip install -e pkg/avt_metrics_ref
```

## Quickstart

```python
from avt_metrics_ref import wer, cer, disaggregated_wer

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
```

For metrics requiring user-supplied classifiers (M-WER, CK-ER), see the per-function docstring for the expected signature.

## Disclaimer

The library exposes `disclaimer()` as a runtime-callable string. Recommended: include in any publication, dashboard, or contract that cites the package output:

```python
from avt_metrics_ref import disclaimer
print(disclaimer())
# → "avt-metrics-ref v0.1.0 — prototype-for-discussion companion to AVT Metrics
#    Taxonomy v5.5.5. Not validated for production decisions, clinical decision
#    support, or contractual thresholds. See https://danjscho.github.io/avt-metrics-taxonomy/
#    for the canonical catalogue and the prototype-status framing."
```

## Versioning

- **Package version (`__version__`)** follows SemVer. `0.x.0` is alpha — the major stays 0 while the package is itself prototype-shaped.
- **Catalogue version (`__catalogue_version__`)** records the AVT Metrics Taxonomy release this package was authored against. Bumped when a catalogue release modifies a TP.ASR Formal Definition or adds a new in-scope metric.
- **Independent release cadences** — catalogue releases that don't touch TP.ASR don't bump the package version; package patches that don't change behaviour don't bump the catalogue version.

## Contributing

The pilot is a single-cluster proof of shape. Two reasonable next steps:

1. **Expand cluster coverage** — TP.WB write-back metrics (FHIR conformance, PRSB completeness) are the natural next pilot since they have well-defined external standards. TP.SN summarisation metrics need NLI/semantic-similarity infrastructure that the pilot deliberately avoided.
2. **Tighten the pilot** — the M-WER and CK-ER signatures push the domain-NER choice onto the caller, which is honest but creates an integration tax. A reference NER bundle (clinical-keyword-list-only, no models) would lower that tax for the common case.

PRs welcome on either axis. The maintenance commitment is honest about itself: this is a prototype companion to a prototype catalogue, and the library will only be expanded when there is genuine pull from people actually running it on real data.

## License

MIT — see [LICENSE](LICENSE).
