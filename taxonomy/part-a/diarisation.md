## Diarisation

*Who said what. Attribution errors cascade into summarisation.*

**Tier breakdown**: 🟡 3 Tier 2 · 🔵 1 Tier 3

### 🟡 Diarisation Error Rate (DER)

Proportion of audio time with incorrect speaker labels. Combines missed speech, false alarm, and speaker confusion.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Diarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | SCRIBE framework; standard diarisation literature |

**Why this tier?**

> Vendor pre-deployment metric. Deployer should request results, especially for multi-party scenarios relevant to their clinical context.

**Formal Definition**

```
DER = (FA + MISS + SPKR_ERR) / TOTAL. FA = false alarm time, MISS = missed speech, SPKR_ERR = speaker confusion. Optionally with 0.25s collar tolerance. NIST md-eval is the standard scorer.
```

**Code: DER via pyannote**

```python
from pyannote.metrics.diarization import DiarizationErrorRate

metric = DiarizationErrorRate(collar=0.25)
der = metric(reference_annotation, hypothesis_annotation)
# Returns: {'diarization error rate': 0.12,
#            'false alarm': 0.03,
#            'missed detection': 0.04,
#            'confusion': 0.05}
```

**References**

- **Scoring tool**: [dscore — Python NIST md-eval](https://github.com/nryant/dscore)
- **SCRIBE**: [Wang et al. (2025) — npj Digital Medicine](https://doi.org/10.1038/s41746-025-01449-w)

**Limitations**

> Challenging in multi-party consultations. Most benchmarks assume two speakers.

---

### 🟡 Speaker Attribution Accuracy

Percentage of utterances assigned to correct speaker. Misattributed medication instructions directly cause prescribing errors.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Diarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | SCRIBE framework |

**Why this tier?**

> Vendor pre-deployment. Safety-critical for medication attribution but deployer cannot independently measure.

**Formal Definition**

```
SAA = |U_correct| / |U_total|. Unlike DER (time-based), SAA is utterance-based. Compute separately for medication-related utterances: SAA_med.
```

**References**

- **SCRIBE**: [Wang et al. (2025)](https://doi.org/10.1038/s41746-025-01449-w)

**Limitations**

> Multi-party scenarios poorly benchmarked.

**Novel Thinking / Implications**

> 💡 Medication instruction misattribution (patient reports vs clinician prescribes) deserves separate measurement as a safety-critical sub-class.

---

### 🟡 Speaker Count Accuracy

Does the system correctly identify how many speakers are present? Particularly important for distinguishing 2-speaker (validated) from 3+-speaker (out-of-envelope) consultations. Over-counting fragments single speakers; under-counting merges distinct speakers.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Diarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard diarisation evaluation |

**Why this tier?**

> Vendor pre-deployment metric. Important for any deployer routinely operating with multi-party consultations.

**Formal Definition**

```
Speaker Count Accuracy = |encounters_with_correct_count| / |total_encounters|. Detailed: |estimated_speakers - actual_speakers|. Mean Absolute Error preferred over binary accuracy.
```

**Limitations**

> Speaker count is often unknown in advance and itself estimated. Multiple ground truth annotators may disagree on speaker count for marginal cases.

**Novel Thinking / Implications**

> 💡 Speaker count is the gateway to multi-party robustness. If the system thinks there are 2 speakers when there are actually 3 (interpreter, family member), the third speaker's content is misattributed to one of the others — silently changing the clinical meaning of utterances.

---

### 🔵 Speaker Boundary Precision

Temporal accuracy of where one speaker stops and another starts. Affects attribution at turn boundaries — words at the edge of a turn may be attributed to the wrong speaker.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Diarisation |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | Standard diarisation literature |

**Why this tier?**

> Vendor research metric. Important for understanding diarisation quality but not directly actionable by deployers.

**Formal Definition**

```
Boundary Precision = mean temporal error (ms) between predicted and actual speaker change points. Report as distribution. NIST scoring uses 250ms collar; tighter collars expose boundary precision better.
```

**Limitations**

> Precise boundary annotation is labour-intensive. Inter-annotator agreement on exact boundaries is itself imperfect.

**Novel Thinking / Implications**

> 💡 Boundary errors are the most common cause of speaker attribution errors at turn boundaries. The first or last word of a turn is the most likely to be misattributed — and often these are the words that carry clinical meaning ('yes' to a question about symptoms, 'no' to a question about allergies).

---

