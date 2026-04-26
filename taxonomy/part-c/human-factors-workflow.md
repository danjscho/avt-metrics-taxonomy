### HL.HF-1 🟢 Edit Rate (% Notes Edited)

Percentage of AI notes edited before approval. At Day Zero: quality signal. Declining trajectory: primary complacency indicator.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-1 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Day Zero Baseline, Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Abridge; NAS; Stanford framework |

**Why this tier?**

> Primary continuous complacency indicator. Deployer-measurable from EPR workflow data. NAS Day Zero SPI. The single most important human factors metric - trajectory reveals automation bias before incidents occur.

**Formal Definition**

```
ER(t) = |N_edited(t)| / |N_total(t)|. Complacency signal: dER/dt < 0 sustained ≥4 weeks without AI accuracy improvement. Alert: ER drops >15pp from baseline within 3 months.
```

**Reference Standard**

> EPR or AVT-product telemetry capturing the post-generation, pre-signature note-state diff. An "edit" is any change to the AI-generated text between AI output and clinician signature. Out of scope: changes after signature (correction workflows are tracked under [GV.SG-15 Time-to-Correct](#gv-sg-15), not Edit Rate). Edit detection MUST distinguish:
>
> - **Substantive edits** - additions, deletions, or modifications that alter clinical meaning (default count for ER)
> - **Stylistic edits** - formatting, punctuation, casing, whitespace (reported separately, not counted in headline ER)
>
> Where the diff cannot reliably classify substantive vs stylistic, count as substantive. The classification rule MUST be documented and held constant across the deployment; vendors changing the rule must declare a baseline reset (see Operational Specification).

**Operational Specification**

> - **Window:** weekly aggregate per clinician and per deployment site. Continuous monitoring (the Cadence above); weekly granularity is the floor for trajectory analysis.
> - **Population:** all AI-generated notes signed by the clinician during the window. Exclude notes where the clinician aborted the AI workflow before signature (these belong under [HL.HF-9 Re-record / Abandonment Rate](#hl-hf-9)).
> - **Baseline establishment MANDATORY:** the deployment baseline is the mean weekly ER across the first 4 weeks of clinician live use, computed per clinician (not pooled). All complacency-alert calculations are referenced to this per-clinician baseline.
> - **Severity stratification MANDATORY:** edits classified as **safety-critical** (allergy, medication, dose, red-flag, diagnosis, plan), **clinically meaningful** (history, exam findings, risk-factor wording), or **stylistic**. Headline ER is over substantive (safety-critical + clinically-meaningful) edits; safety-critical edit rate reported separately as a leading indicator.
> - **Per-clinician disaggregation MANDATORY:** site-level ER hides individual complacency. Reporting must include per-clinician trajectories alongside aggregate.

**Threshold Guidance**

> ⚠️ **Provenance:** the > 15-percentage-point drop sustained ≥ 4 weeks comes from the existing Formal Definition complacency signal (carried from prior versions of the metric); the 30–80 % baseline range, the < 50 %-of-baseline pause trigger, and the zero-safety-critical-edits-with-continued-stylistic-editing trigger are **proposed in v3.3 as starting points**, not externally validated. Edit Rate is **interpretable only as a trajectory** (per Limitations and Novel Thinking); absolute thresholds below are deployment-context-dependent and require local calibration before contractual use.
>
> - **Pre-deployment / Day Zero baseline expectation:** substantive ER between 30 % and 80 % during the first 4 weeks. ER below 30 % in week 1 is a flag for inadequate review, not for excellent AI.
> - **Continuous monitoring alert:** substantive ER drops > 15 percentage points from the per-clinician baseline within any 12-week rolling window, sustained ≥ 4 weeks (the existing complacency signal in the Code block).
> - **Pause / review trigger:** substantive ER < 50 % of per-clinician baseline for 4 consecutive weeks, OR safety-critical edit rate drops to zero for ≥ 4 weeks while substantive edit rate remains > 10 % (suggests clinicians are stopping their safety review while continuing minor editing). Triggers trust-calibration review and pairing with HL.HF-6 Automation Bias Detection.

**Code: Edit rate complacency detection**

```python
import pandas as pd
from scipy.stats import linregress

def detect_complacency(weekly_rates, baseline_weeks=4):
    df = pd.DataFrame(weekly_rates, columns=["week","rate"])
    baseline = df[df.week <= baseline_weeks]["rate"].mean()
    alerts = []
    for i in range(baseline_weeks, len(df)-3):
        window = df.iloc[i:i+4]
        slope, _, _, p, _ = linregress(window["week"], window["rate"])
        current = window["rate"].iloc[-1]
        if slope < -0.02 and p < 0.1 and baseline - current > 0.15:
            alerts.append({
                "week": int(window["week"].iloc[-1]),
                "current": round(current, 3),
                "action": "COMPLACENCY_REVIEW"})
    return {"baseline": round(baseline,3), "alerts": alerts}
```

**References**

- **Abridge**: Abridge edit-pattern methodology
- **NAS**: NAS Day Zero SPI

**Limitations**

> Ambiguous alone: low rate = good AI or poor review. Requires triangulation.

**Novel Thinking / Implications**

> 💡 Trajectory matters more than absolute value. 60% → 15% in 3 months should trigger review regardless of AI accuracy.

*See also: Edit Type Classification, Edit Location Distribution, Edit-Pattern Monitoring at Scale - all members of the Post-Generation Correction family. Edit Rate is the binary entry point; the other metrics add diagnostic depth. Interpret alongside Review-Before-Signing Rate and Time-to-Sign Distribution to distinguish improving AI from increasing complacency.*

---

### HL.HF-2 🟡 Edit Type Classification

Categorising edits: additions (omission fix), deletions (hallucination fix), modifications, structural. Distribution diagnoses failure mode.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-2 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Abridge; DeepScore |

**Why this tier?**

> More granular than edit rate - diagnoses failure mode (additions = omission problem, deletions = hallucination problem). Requires NLP classification but adds substantial diagnostic value.

**Formal Definition**

```
Type(e) ∈ {Addition, Deletion, Modification, Structural}. P_add >> P_del → omission-dominant; P_del >> P_add → hallucination-dominant. Track over time to assess model updates.
```

**References**

- **Abridge**: 1M+ encounters/week
- **DeepScore**: 135,900 notes

**Limitations**

> Automated classification requires NLP.

**Novel Thinking / Implications**

> 💡 Mostly additions = omission problem; mostly deletions = hallucination problem.

*See also: Edit Rate, Edit Location Distribution, Edit-Pattern Monitoring at Scale - all members of the Post-Generation Correction family. Type classification is where the family becomes diagnostic rather than just descriptive: predominantly additions indicate an omission-dominant failure mode; predominantly deletions indicate a hallucination-dominant mode.*

---

### HL.HF-3 🟢 Review-Before-Signing Rate

Notes demonstrably reviewed before sign-off. NAS: ≥95% threshold, <85% pause trigger.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-3 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | NAS Day Zero SPI; Stanford |

**Why this tier?**

> NAS Day Zero SPI with ≥95% threshold and <85% pause trigger. Deployer-measurable from EPR workflow telemetry. Directly monitors whether human oversight is functioning.

**Formal Definition**

```
RBS = |N_reviewed| / |N_total|. N_reviewed = notes with edit events, scroll events, or dwell > T_min. T_min = max(15s, 3s × word_count/100).
```

**References**

- **NAS**: ≥95% threshold, <85% pause trigger

**Limitations**

> Scrolling ≠ meaningful review.

**Novel Thinking / Implications**

> 💡 EPR should enforce architecturally: minimum dwell-time before approve activates.

---

### HL.HF-4 🟢 Time-to-Sign Distribution

Duration between generation and approval. Model as distribution - tail of very-fast approvals is safety-critical.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-4 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | EPR workflow data; Stanford principles |

**Why this tier?**

> Deployer-measurable from EPR data. The tail of very-fast approvals (<5 seconds for complex notes) is the safety-critical population. Distribution analysis detects rubber-stamping patterns.

**Formal Definition**

```
TTS = t_approve - t_generated. Report: median, P5, P10, P90. Normalise: TTS_norm = TTS / word_count. Flag: TTS_norm < 0.5s/word suggests rubber-stamping.
```

**Reference Standard**

> EPR + AVT product telemetry. `t_generated` = the timestamp at which the AVT-generated note becomes visible to the clinician for review. `t_approve` = the clinician signature event on the note. The window between these two timestamps captures total review-and-edit duration; TTS does NOT include time before AVT note availability or time after signature. Where the clinician opens, leaves, and returns to the note, TTS counts only the foreground review time within the EPR session if the EPR can distinguish; otherwise the full elapsed time is used and the limitation declared.

**Operational Specification**

> - **Window:** continuous; weekly distribution analysis per clinician.
> - **Population:** all AVT-generated notes signed during the window. Notes signed by a clinician other than the one to whom AVT was active (delegated workflows) excluded; flagged as a separate audit item.
> - **Distribution reporting MANDATORY:** P5, P10, median, P90 of TTS per clinician AND of TTS_norm (TTS / word_count). Single-number reporting (mean or median alone) is not Tier 1 sufficient - the safety signal lives in the lower tail.
> - **Per-clinician baseline MANDATORY:** baseline TTS_norm distribution computed across the first 4 weeks of clinician live use; subsequent reporting referenced to per-clinician baseline (parallel to [HL.HF-1 Edit Rate](#hl-hf-1)).
> - **Pairing with Edit Rate MANDATORY:** TTS distribution reported alongside HL.HF-1 substantive edit rate for the same clinician-window. Low TTS + low substantive edit rate is the rubber-stamping signal; either alone is ambiguous.
> - **Note-complexity stratification:** report TTS_norm distribution stratified by note word count quartile (short / medium / long / very-long); rubber-stamping risk is most visible on long/complex notes signed at short-note speed.

**Threshold Guidance**

> ⚠️ **Provenance:** the TTS_norm < 0.5 s/word rubber-stamping flag and the lower-tail focus carry over from the existing Formal Definition and Stanford principles cited in Source. Specific numbers (P5 < 0.3 s/word pause trigger, 4-week baseline window, 10 % below-baseline rate alert) are **proposed in v3.4 as starting points**, not externally validated. TTS is interpretable only as a distribution paired with edit rate; absolute thresholds below are deployment-context-dependent.
>
> - **Pre-deployment / Day Zero baseline:** establish per-clinician TTS_norm distribution across the first 4 weeks of live use; record P5, P10, median, P90.
> - **Continuous monitoring alert:** weekly P5 of TTS_norm < 0.3 s/word for any clinician (the rubber-stamping floor); OR the proportion of notes with TTS_norm < 0.5 s/word rises > 10 percentage points from per-clinician baseline.
> - **Pause / review trigger:** weekly P10 of TTS_norm < 0.3 s/word AND HL.HF-1 substantive edit rate < 25 % for the same clinician-window (rubber-stamping confirmed in distribution and in editing behaviour). Triggers trust-calibration review and pairing with HL.HF-6 Automation Bias Detection.

**Code: Time-to-sign analysis**

```python
import numpy as np

def analyse_tts(data):  # list of {seconds, word_count}
    tts = np.array([d["seconds"] for d in data])
    wc = np.array([d["word_count"] for d in data])
    tts_norm = tts / np.maximum(wc, 1)
    return {
        "median_s": float(np.median(tts)),
        "p5_s": float(np.percentile(tts, 5)),
        "rubber_stamp_pct": float(np.mean(tts_norm < 0.5) * 100),
        "alert": bool(np.percentile(tts_norm, 5) < 0.3)}
```

**Limitations**

> Context-dependent. Must normalise by length/complexity.

**Novel Thinking / Implications**

> 💡 The tail of very-fast approvals is the safety-critical population.

---

### HL.HF-5 🔵 Edit-Pattern Monitoring at Scale

Cross-system edit analysis (1M+/week, 150+ systems). Most scalable quality signal - locked inside one vendor.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-5 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Vendor-Proprietary |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Abridge whitepaper |

**Why this tier?**

> Vendor-proprietary (Abridge). Scale advantage creates a data moat. Informs what a national standard should require all vendors to provide.

**Formal Definition**

```
Aggregate across N systems: system-level distribution, edit type by specialty/template, temporal trends, outlier detection (>2σ from fleet mean). Uses anytime-valid sequential testing.
```

**References**

- **Abridge**: Oberst, Liang, Lipton (2024/2025)

**Limitations**

> Proprietary. Scale creates data moat.

**Novel Thinking / Implications**

> 💡 National standard should require standardised edit-pattern reporting from all vendors.

*See also: Edit Rate, Edit Type Classification, Edit Location Distribution - all members of the Post-Generation Correction family. Pattern monitoring operates at the fleet level to detect shifts invisible to any single deployer; informs what a national standard should require all vendors to provide.*

---

### HL.HF-6 🟡 Automation Bias Detection (Error Injection)

Deliberately seeded errors to test clinician catch rate. The only metric directly measuring human oversight. All others are proxies.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-6 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Regional (ICB) |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | Proposed in NAS framework |

**Why this tier?**

> The only metric that directly tests human oversight. Quarterly error injection audit. Ethically complex but feasible with appropriate safeguards. Should be Tier 1 aspiration for mature deployers.

**Formal Definition**

```
Inject known errors at rate r (e.g. 1 in 50) with defined severity. Detection Rate DR = |E_caught| / |E_injected| per severity. Oversight Effectiveness OE = Σ(severity_weight × DR) / Σ(weight). Must intercept before EPR write-back.
```

**References**

- **Analogy**: Laboratory EQA proficiency testing (NEQAS)

**Limitations**

> Ethical complexity. Must ensure errors intercepted before permanent record.

**⚠️ Underspecification Warning (Tier B - strong concept, ad hoc protocols)**

> Automation bias is well-defined conceptually (Parasuraman & Manzey, *Human Factors* 2010) but measurement protocols in clinical AI remain ad hoc. Most published studies use vignette-based designs comparing diagnostic accuracy with and without AI assistance; there is no standardised measurement protocol for production AVT systems operating under real clinical time pressure. No consensus exists on acceptable automation bias rate thresholds - one computational pathology study reported a 7% rate without specifying whether that was concerning or within expected bounds for the task. An active RCT (NCT07328815) is testing nudge interventions but results are not yet available. Until standardised production protocols emerge, document explicitly: (a) the injection methodology (how errors are generated), (b) the injection rate, (c) the severity distribution of injected errors, (d) the detection criteria (what counts as "caught"), (e) the timing of assessment. Changes to any of these make values incomparable across audits.

**Novel Thinking / Implications**

> 💡 Only metric directly measuring oversight function. Quarterly error injection with known difficulty thresholds.

---

### HL.HF-7 🟡 Edit Location Distribution

Where in the note do clinicians make edits? Concentration in specific sections (history, examination, plan) reveals which sections the AI handles poorly. A diagnostic that complements edit type classification.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-7 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Extends edit-pattern monitoring with structural awareness |

**Why this tier?**

> Diagnostic enhancement to edit rate monitoring. Identifies which sections need more reviewer attention.

**Formal Definition**

```
For each note section s: Edit Density(s) = |edits_in_s| / |words_in_s|. Compare across sections. Sections with edit density >> average have systematic AI quality issues. Track over time to assess model improvement.
```

**Limitations**

> Requires consistent note structure for meaningful comparison.

**Novel Thinking / Implications**

> 💡 Reveals systematic quality patterns invisible to aggregate edit rate. If clinicians always edit the 'plan' section but rarely edit 'history', the AI is good at extracting facts but poor at synthesising clinical reasoning. This guides where vendor improvement should focus and where clinicians should pay particular attention during review.

*See also: Edit Rate, Edit Type Classification, Edit-Pattern Monitoring at Scale - all members of the Post-Generation Correction family. Locus analysis complements type classification: what kind of edit combined with where in the note identifies specific failure modes that either dimension alone would miss.*

---

### HL.HF-8 🟡 Trust Calibration Survey

Clinician confidence vs actual accuracy. Overconfidence = automation bias risk. Gap between stated and behavioural trust is itself a metric.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-8 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Day Zero Baseline, Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | Human factors literature; NAS framework |

**Why this tier?**

> Survey-based. Useful triangulation with behavioural metrics. Annual measurement tracks trust-behaviour gap evolution.

**Formal Definition**

```
Trust Calibration Gap TCG(c) = Stated_Trust(c) - Actual_Accuracy(c). TCG > 0 = overconfidence (dangerous). TCG < 0 = underconfidence (adoption barrier).
```

**References**

- **Trust in automation**: Lee & See (2004)

**Limitations**

> Self-report bias. Must triangulate with behavioural metrics.

**⚠️ Underspecification Warning (Tier B - concept defined, no AVT-validated instrument)**

> Multiple candidate instruments exist for trust calibration in clinical AI (TIAS, HATAS, AITI-H), but **none are validated specifically for ambient scribe contexts**. A 2024 Dokkyo Medical University review concluded that there are currently no accurate and objective measures available for evaluating trust calibration in clinical AI deployments. No thresholds exist for defining "appropriately calibrated" trust, and no empirical integration has been established between subjective trust measures and behavioural proxies (edit rate, review time, error detection) that would allow triangulation. Adapt TIAS or HATAS for AVT context as an interim measure, document the adaptation explicitly, and flag the absence of formal validation when reporting results. Pair with the existing behavioural complacency indicators (Edit Rate, Time-to-Sign, Review-Before-Signing) rather than relying on the survey instrument alone.

**Novel Thinking / Implications**

> 💡 'I always check carefully' + 5-second approval = trust calibration gap requiring architectural intervention.

---

### HL.HF-9 🟡 Re-record / Abandonment Rate

Frequency of clinicians abandoning AVT mid-consultation and starting again, or abandoning the AVT-generated note entirely and writing manually. Strong dissatisfaction signal indicating either technical failure or fundamental quality issues.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-9 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Identified as strong dissatisfaction signal |

**Why this tier?**

> Strong leading indicator of system problems. Should trigger immediate investigation when rates rise.

**Formal Definition**

```
Re-record Rate = |consultations_with_restart| / |total_consultations|. Abandonment Rate = |notes_discarded_and_rewritten| / |total_notes|. Both should be near zero in steady state. Sudden increases indicate system regression.
```

**Limitations**

> Requires EPR workflow telemetry to detect restarts and abandonments. Some legitimate restart cases (technical issues) need to be distinguished from quality-driven restarts.

**Novel Thinking / Implications**

> 💡 Re-record rate is the canary in the coal mine. When clinicians start restarting consultations or abandoning notes, something has gone fundamentally wrong - either the system has degraded or the workflow is broken. This is a leading indicator that should trigger immediate investigation, not routine review.

---

### HL.HF-10 🔵 Cognitive Load Assessment

Mental effort for review. Target: 'effortful but efficient' - enough to catch errors, not so much that time savings disappear.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-10 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | NASA-TLX adapted for clinical documentation review |

**Why this tier?**

> Research metric. NASA-TLX adaptation is established but adds burden. Physiological measures are research-only.

**Formal Definition**

```
Adapted NASA-TLX: Mental Demand, Temporal Demand, Effort, Frustration, Trust Burden. Each 0-100. Target CL: 30-60 (below = disengagement, above = no benefit).
```

**References**

- **NASA-TLX**: [NASA Task Load Index](https://humansystems.arc.nasa.gov/groups/TLX/)

**Limitations**

> Self-report. Adds burden.

**⚠️ Underspecification Warning (Tier B - generic validation, no AVT-specific calibration)**

> NASA-TLX is validated generically with acceptable individual-setting ICC of 0.71–0.81 (lower for group settings). However, for AVT specifically: no subscale selection protocol exists, no consensus on measurement timing (during encounter / immediately after charting / end of day / end of week), no documentation-specific adaptation of the instrument, and no established thresholds for "acceptable" cognitive load in AVT review tasks. The 60.7% reduction in composite cognitive load reported in a 2024 Abridge study is a point estimate with no reference scale for clinical interpretation - "60% less" of an undefined baseline is not directly actionable. Use NASA-TLX as an interim measure, specify the timing and subscale selection used, and avoid comparing raw scores across studies that use different protocols. The proposed **Verification Burden** metric (Human Factors & Workflow) is intended to capture a more specific construct that may ultimately prove more actionable than global cognitive load.

**Novel Thinking / Implications**

> 💡 Optimal load is non-obvious: too low = disengagement, too high = no benefit.

---

### HL.HF-11 🔵 Inter-Clinician Edit Variance

Do different clinicians edit the same AI output similarly? High variance suggests either ambiguous AI output (different clinicians read it differently) or inconsistent quality standards across clinicians. Both are governance issues.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-11 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Contextualised |
| **Source** | Extends inter-rater reliability concepts to AVT review |

**Why this tier?**

> Research-grade metric requiring controlled study. Important for understanding review reliability but not routine measurement.

**Formal Definition**

```
For sample of identical AI outputs reviewed by multiple clinicians: variance in edit count, edit type distribution, and edit content. Inter-rater reliability metrics on edit decisions.
```

**Limitations**

> Requires controlled study with multiple clinicians reviewing same outputs. Difficult to operationalise in routine practice.

**Novel Thinking / Implications**

> 💡 If Clinician A always edits the AI output extensively and Clinician B never edits it, the issue might be either clinician (one is too critical, the other is too lax) or the AI (the output is ambiguous). Inter-clinician variance reveals whether the review function is consistent - a prerequisite for meaningful aggregate metrics.

---

### HL.HF-12 🔵 Clinical Documentation Skill Attenuation

Longitudinal ability to document without AI. Sleeper risk - if a generation trains with AVT, baseline capability degrades.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-12 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | Aviation skill degradation literature |

**Why this tier?**

> Long-term longitudinal study. Effects take years to manifest. Important for workforce planning but not actionable at individual deployer level.

**Formal Definition**

```
Annual: clinicians document N simulated encounters without AI, scored via PDSQI-9. SA(t) = PDSQI9_noAI(t) - PDSQI9_noAI(t-1). Negative SA = attenuation. Compare trainees against pre-AVT cohort norms.
```

**References**

- **Aviation analogy**: Casner & Schooler (2014) - pilot skill degradation

**Limitations**

> Long-term study. Hard to isolate AVT as cause.

**Novel Thinking / Implications**

> 💡 Medical education bodies should be tracking this now.

---

### HL.HF-13 🔵 Cognitive Offloading Rate

Proportion of clinicians who report relying on AI for content recall ('I don't need to remember, the AI will catch it'). Different from automation bias - this is active delegation rather than passive trust. Predicts skill attenuation.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-13 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | Cognitive offloading literature; distinct from automation bias |

**Why this tier?**

> Research metric. Important for understanding workforce impact but not routine measurement.

**Formal Definition**

```
Survey-based: 'I rely on the AVT system to capture details I might otherwise need to remember during consultations' (5-point Likert). Offloading Rate = proportion answering 'agree' or 'strongly agree'. Track over time to detect increasing dependence.
```

**Limitations**

> Self-report bias. Clinicians may not be aware of their own cognitive offloading.

**Novel Thinking / Implications**

> 💡 Offloading is the precursor to skill attenuation. When clinicians actively delegate cognitive functions to the AI, they stop practicing those functions, which then atrophy. This is the mechanism by which AVT could degrade clinical workforce capability over time. Tracking offloading provides an early signal before measurable skill loss occurs.

---

### HL.HF-14 🔵 Trust Halo Decay Rate

Whether initial high trust persists after errors. Absent decay = dangerous over-trust. Trust halo drives off-label scope creep.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-14 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | Trust halo effect analysis |

**Why this tier?**

> Research metric requiring longitudinal measurement. Conceptually important for understanding off-label use drivers but not operationally measurable at scale.

**Formal Definition**

```
Longitudinal T(t). After error at t_e, decay rate λ = -dT/dt for t > t_e. Healthy: λ > 0 (appropriate recalibration). Dangerous: λ ≈ 0 (trust unchanged despite evidence).
```

**Limitations**

> Longitudinal measurement required.

**⚠️ Underspecification Warning (Tier A - no validated measurement in clinical AI)**

> The trust halo effect is well-established in cognitive psychology but has **not been operationalised for clinical AI or AVT specifically**. The concept substantially overlaps with automation bias, and the empirical boundary between the two constructs is not established - it is unclear whether they should be measured as distinct phenomena or as facets of a common over-reliance construct. No validation studies exist. No measurement instruments have been adapted from cognitive psychology to the clinical AI context. Two viable paths forward: (a) define a specific experimental paradigm (e.g. testing whether positive experience with transcription accuracy transfers uncritically to trust in clinical summarisation accuracy, which is a different capability) and build validation evidence from there, or (b) fold the construct into the broader automation bias / over-reliance family until the measurement science matures enough to distinguish it meaningfully. Until one of these is done, any reported values should carry explicit acknowledgement of the definitional uncertainty.

**Novel Thinking / Implications**

> 💡 Trust halo → off-label use: over-trust drives scope creep. The halo is the mechanism; off-label use is the consequence.

---

### HL.HF-15 🔵 Note Review Fatigue Trajectory

Review quality degradation over a clinical session. The 9am note review may be different from the 5pm note review, and AVT may amplify end-of-session fatigue effects by adding documentation review burden to existing clinical fatigue.

| Dimension | Value |
|-----------|-------|
| **Reference** | HL.HF-15 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | AVT-Contextualised |
| **Source** | Clinical fatigue research applied to AVT review |

**Why this tier?**

> Research metric. Important workforce safety question but not routinely measurable.

**Formal Definition**

```
Track review quality metrics (time-to-sign, edit rate, error detection in injection audits) by time-of-day and session position. Fatigue Slope = degradation rate per hour into session. Significant negative slope indicates fatigue effects.
```

**Limitations**

> Confounded with case mix variation (afternoon clinics may have different complexity). Requires careful statistical controls.

**⚠️ Underspecification Warning (Tier A - underlying concept unoperationalised)**

> The broader concept of attention drift across a clinician's reviewing session has **no operationalised definition in AVT literature**. The Cognitive Drift Index (Frontiers in Neuroscience 2025) measures information consumers' judgment shifts in unrelated domains, not clinician review vigilance. A 2026 KevinMD essay described "the slow erosion of clinical humility" qualitatively but offered no measurement approach. No published study has established a detection methodology, thresholds, or relationship to patient safety outcomes. Proposed interim operationalisation for this taxonomy - to be treated as a working definition pending empirical validation - is a composite of (a) declining review time per note over a session, (b) reduced edit rate trajectory within sessions, and (c) reduced error detection rate in periodic injection testing stratified by time-of-session. This proposal has not been validated; deployers using it should document the operational definition applied and treat results as exploratory rather than diagnostic.

**Novel Thinking / Implications**

> 💡 If review quality degrades through the session, the safety implications are significant: the last patients of the day get the least rigorous oversight. AVT systems designed assuming consistent reviewer attention are operating outside that assumption for a meaningful fraction of consultations. This argues for fatigue-aware workflow design - perhaps requiring more thorough review for end-of-session notes, or rotating review responsibility.

---

---

### Sociotechnical & Resilience sub-cluster

*Systems-level constructs drawn from FRAM, Safety-II, and resilience engineering. These metrics assess the clinician-AVT joint cognitive system rather than AVT alone, and capture dimensions that standard human factors metrics miss - the gap between intended and actual practice, the hidden cost of verification, and the capacity to handle unexpected situations.*

---

### HL.HF-16 🔵 Work-as-Imagined vs Work-as-Done Gap

The gap between how AVT is intended to be used (per procedures, training, and governance documentation) and how it is actually used in clinical practice. A construct from Hollnagel's FRAM methodology and the Safety-II tradition. Subsumes and generalises the existing Off-Label Use Detection metric - not every WAI/WAD gap is off-label, and not every adaptation is a safety problem, but the gap itself is diagnostically valuable.

|Dimension              |Value                                                                  |
|-----------------------|-----------------------------------------------------------------------|
| **Reference** | HL.HF-16 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research                                         |
|**Measurement Cadence**|Periodic audit                                                         |
|**Pipeline Layer**     |Cross-cutting                                                          |
|**Assurance Question** |Safety                                                                 |
|**Measurement Method** |Hybrid                                                                 |
|**Lifecycle Phases**   |Periodic Audit                                                         |
|**Responsible Actors** |Deployer, Academic                                                     |
|**Maturity**           |Proposed / Novel                                                       |
|**Outcome Type**       |Distal                                                                 |
|**Applicability**      |General Healthcare AI                                                  |
|**Source**             |Hollnagel FRAM methodology; JMIR 2026 SEIPS-based AVT evaluations      |

**Why this tier?**

> Research-grade metric requiring ethnographic observation and structured interview methodology. Not routinely measurable at deployer level. Academic or national evaluation programme responsibility.

**Formal Definition**

```
Three-step methodology: (1) Document WAI from training materials, SOPs, vendor guidance, and governance policies; (2) Observe WAD through shadowing, workflow analysis, and semi-structured clinician interviews; (3) Gap analysis - categorise deviations as {beneficial adaptation, neutral workaround, latent risk, active hazard}. Report gap count per category and exemplar descriptions rather than a single scalar - the qualitative detail is what supports intervention.
```

**Limitations**

> Ethnographic methods are resource-intensive and subjective. WAI is itself often poorly documented. Observer effects shape observed behaviour. Generalisation across practices is limited.

**Novel Thinking / Implications**

> 💡 Every complex sociotechnical system has a WAI/WAD gap - procedures can never fully specify practice. The Safety-II insight is that adaptations are not automatically failures; they are often what makes the system work at all. The diagnostic question is not "is there a gap?" (there always is) but "which gaps indicate genuine risk vs which indicate necessary adaptation that should be formalised back into WAI?" This metric surfaces the question; human judgment answers it.

---

### HL.HF-17 🟡 Verification Burden

The additional workload created by the need to verify AI-generated content against clinical reality - reading the note, cross-checking against the conversation, identifying errors, making corrections. Distinct from the existing Cognitive Load Assessment metric, which measures total effort. Verification burden is specifically the checking overhead that exists only because the output needs checking. A well-calibrated AVT system minimises this burden; a poorly-calibrated one shifts documentation time into verification time and may eliminate the apparent efficiency gain.

|Dimension              |Value                                                               |
|-----------------------|--------------------------------------------------------------------|
| **Reference** | HL.HF-17 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                              |
|**Measurement Cadence**|Periodic audit                                                      |
|**Pipeline Layer**     |Cross-cutting                                                       |
|**Assurance Question** |Human Factors                                                       |
|**Measurement Method** |Hybrid                                                              |
|**Lifecycle Phases**   |Day Zero Baseline, Periodic Audit                                   |
|**Responsible Actors** |Deployer, Academic                                                  |
|**Maturity**           |Emerging                                                            |
|**Outcome Type**       |Proximal                                                            |
|**Applicability**      |AVT-Contextualised                                                  |
|**Source**             |JMIR 2026 e86166 SEIPS-based evaluation; GOSH Phase 4 TimeCat data  |

**Why this tier?**

> Conceptually important - distinguishes apparent efficiency gain from actual efficiency gain - but requires time-motion observation methodology (TimeCat or equivalent). Day Zero baseline plus periodic re-measurement supports trajectory analysis.

**Formal Definition**

```
VB = t_review + t_correction + t_cross_reference, measured per consultation. Baseline pre-AVT: equivalent activities (proofreading own notes, referencing structured fields). Net Verification Cost = VB_AVT - VB_pre-AVT. Efficiency gain = (t_documentation_pre - t_documentation_AVT) - Net Verification Cost. A genuinely efficient system has positive net gain after accounting for verification burden.
```

**Limitations**

> TimeCat or equivalent time-motion methodology is labour-intensive. Verification activities are often interleaved with other work and hard to isolate. Self-report on verification time is unreliable because the activity is partly automatic.

**Novel Thinking / Implications**

> 💡 The marketing claim "AVT saves 3 minutes of documentation time per consultation" is meaningless without verification burden accounting. A system that saves 3 minutes of typing but adds 4 minutes of verification has negative net efficiency - and research suggests this scenario is common early in deployment before clinicians develop efficient review patterns. Verification burden should be reported alongside every documentation time saving claim, or the claim should not be reported at all.

---

### HL.HF-18 🔵 Resilience Capacities Assessment

Structured assessment of the clinician-AVT joint cognitive system against the four Safety-II resilience capacities: **responding** to unexpected events, **monitoring** for signs of degradation, **learning** from experience, and **anticipating** future challenges. From Hollnagel's resilience engineering framework. Applied not to AVT alone but to the combined human-machine system as it operates in context.

|Dimension              |Value                                                             |
|-----------------------|------------------------------------------------------------------|
| **Reference** | HL.HF-18 |
|**Priority Tier**      |🔵 Tier 3 - Advanced / Research                                    |
|**Measurement Cadence**|Periodic audit                                                    |
|**Pipeline Layer**     |Cross-cutting                                                     |
|**Assurance Question** |Safety                                                            |
|**Measurement Method** |Hybrid                                                            |
|**Lifecycle Phases**   |Periodic Audit                                                    |
|**Responsible Actors** |Deployer, National Body, Academic                                 |
|**Maturity**           |Proposed / Novel                                                  |
|**Outcome Type**       |Distal                                                            |
|**Applicability**      |General Healthcare AI                                             |
|**Source**             |Hollnagel Safety-II; FRAM methodology; resilience engineering literature|

**Why this tier?**

> Research framework applied at system level. Not a routine metric. National or academic responsibility for maturing the methodology into deployable assessment.

**Formal Definition**

```
Four capacity dimensions scored via structured scenario-based assessment and qualitative evaluation:
(1) Responding - when an AVT failure occurs mid-consultation (crash, silent degradation, wrong-patient data), how does the clinician-system respond? Recovery time, recovery completeness, downstream impact.
(2) Monitoring - what signals does the system provide that allow the clinician to detect degradation? Are those signals attended to in practice?
(3) Learning - when errors are discovered, how is that learning captured and integrated into future work? (Links to Hazard Log Completeness and Training Material Currency)
(4) Anticipating - does the deployer identify and prepare for foreseeable challenges (model updates, regulatory changes, novel failure modes)?
Score each capacity 1–5 with narrative justification. Composite is a profile, not a single number.
```

**Limitations**

> Assessment is qualitative and requires trained evaluators. Framework originally developed for complex sociotechnical systems (healthcare, aviation); application to AVT specifically is novel. Scoring inter-rater reliability has not been established for this application.

**Novel Thinking / Implications**

> 💡 Traditional safety metrics are Safety-I: counting failures and aiming for zero. Resilience metrics are Safety-II: assessing the capacity to handle failures that will inevitably occur. An AVT deployment with zero recorded incidents but weak resilience capacities is brittle - the first real test will reveal the gap. This metric family complements rather than replaces the incident-based metrics in Safety & Governance.

---

### HL.HF-19 🟡 AI-Off Performance Test

Scheduled exercises where clinicians document a clinical encounter without AVT assistance, and the resulting documentation is assessed for quality against baseline standards. Provides an operational implementation of the existing Clinical Documentation Skill Attenuation concept - instead of inferring skill degradation longitudinally, directly measure current unassisted capability. Also doubles as business continuity assurance: can the clinical team function if AVT is unavailable?

|Dimension              |Value                                                                                                 |
|-----------------------|------------------------------------------------------------------------------------------------------|
| **Reference** | HL.HF-19 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                                                                |
|**Measurement Cadence**|Periodic audit                                                                                        |
|**Pipeline Layer**     |Cross-cutting                                                                                         |
|**Assurance Question** |Human Factors                                                                                         |
|**Measurement Method** |Hybrid                                                                                                |
|**Lifecycle Phases**   |Day Zero Baseline, Periodic Audit                                                                     |
|**Responsible Actors** |Deployer                                                                                              |
|**Maturity**           |Proposed / Novel                                                                                      |
|**Outcome Type**       |Distal                                                                                                |
|**Applicability**      |General Healthcare AI                                                                                 |
|**Source**             |Operationalisation of existing Clinical Documentation Skill Attenuation metric; Lancet Gastroenterology 2025 endoscopist AI-off study (ADR fell 28.4%→22.4% when AI removed)|

**Why this tier?**

> Operationally feasible for any deployer willing to commit protected time. More actionable than longitudinal skill attenuation measurement because it provides current state data. Should be scheduled at Day Zero baseline and repeated annually.

**Formal Definition**

```
Protocol: (1) Schedule defined exercises where clinicians document simulated or real consultations without AVT; (2) Documentation is scored using PDSQI-9 or equivalent validated instrument; (3) Score is compared against the clinician's pre-AVT baseline (if available) and against peer benchmarks. Trajectory Metric = score_current - score_baseline. Cohort Analysis: compare clinicians trained with AVT from day one against those who learned without it.
```

**Limitations**

> Protected time is expensive. Simulated consultations differ from real consultations. Clinicians who know they are being assessed may perform differently. Pre-AVT baseline is often not available for individual clinicians.

**Novel Thinking / Implications**

> 💡 The endoscopy AI-off finding (adenoma detection rate falling from 28.4% to 22.4% when AI was removed after a period of AI use) is the first robust real-world evidence of clinical deskilling from AI dependency. For ambient scribes, the equivalent question is whether clinicians lose the ability to write a clinically complete note unassisted after a period of AVT use. This is testable today. The business continuity case - can the practice function during a vendor outage? - is almost sufficient reason to run the test regardless of the deskilling question.
