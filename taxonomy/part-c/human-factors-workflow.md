# Part C — The Human Layer

## Human Factors & Workflow

*The human in the loop. Whether oversight actually functions or erodes over time.*

**Tier breakdown**: 🟢 3 Tier 1 · 🟡 5 Tier 2 · 🔵 7 Tier 3

### 🟢 Edit Rate (% Notes Edited)

Percentage of AI notes edited before approval. At Day Zero: quality signal. Declining trajectory: primary complacency indicator.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Day Zero Baseline, Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Abridge; NAS; Stanford framework |

**Why this tier?**

> Primary continuous complacency indicator. Deployer-measurable from EPR workflow data. NAS Day Zero SPI. The single most important human factors metric — trajectory reveals automation bias before incidents occur.

**Formal Definition**

```
ER(t) = |N_edited(t)| / |N_total(t)|. Complacency signal: dER/dt < 0 sustained ≥4 weeks without AI accuracy improvement. Alert: ER drops >15pp from baseline within 3 months.
```

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

---

### 🟡 Edit Type Classification

Categorising edits: additions (omission fix), deletions (hallucination fix), modifications, structural. Distribution diagnoses failure mode.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Abridge; DeepScore |

**Why this tier?**

> More granular than edit rate — diagnoses failure mode (additions = omission problem, deletions = hallucination problem). Requires NLP classification but adds substantial diagnostic value.

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

---

### 🟢 Review-Before-Signing Rate

Notes demonstrably reviewed before sign-off. NAS: ≥95% threshold, <85% pause trigger.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
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

### 🟢 Time-to-Sign Distribution

Duration between generation and approval. Model as distribution — tail of very-fast approvals is safety-critical.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | EPR workflow data; Stanford principles |

**Why this tier?**

> Deployer-measurable from EPR data. The tail of very-fast approvals (<5 seconds for complex notes) is the safety-critical population. Distribution analysis detects rubber-stamping patterns.

**Formal Definition**

```
TTS = t_approve - t_generated. Report: median, P5, P10, P90. Normalise: TTS_norm = TTS / word_count. Flag: TTS_norm < 0.5s/word suggests rubber-stamping.
```

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

### 🔵 Edit-Pattern Monitoring at Scale

Cross-system edit analysis (1M+/week, 150+ systems). Most scalable quality signal — locked inside one vendor.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Vendor-Proprietary |
| **Outcome Type** | Proximal |
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

---

### 🟡 Automation Bias Detection (Error Injection)

Deliberately seeded errors to test clinician catch rate. The only metric directly measuring human oversight. All others are proxies.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Regional (ICB) |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
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

**Novel Thinking / Implications**

> 💡 Only metric directly measuring oversight function. Quarterly error injection with known difficulty thresholds.

---

### 🟡 Edit Location Distribution

Where in the note do clinicians make edits? Concentration in specific sections (history, examination, plan) reveals which sections the AI handles poorly. A diagnostic that complements edit type classification.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
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

---

### 🟡 Trust Calibration Survey

Clinician confidence vs actual accuracy. Overconfidence = automation bias risk. Gap between stated and behavioural trust is itself a metric.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Day Zero Baseline, Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
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

**Novel Thinking / Implications**

> 💡 'I always check carefully' + 5-second approval = trust calibration gap requiring architectural intervention.

---

### 🟡 Re-record / Abandonment Rate

Frequency of clinicians abandoning AVT mid-consultation and starting again, or abandoning the AVT-generated note entirely and writing manually. Strong dissatisfaction signal indicating either technical failure or fundamental quality issues.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
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

> 💡 Re-record rate is the canary in the coal mine. When clinicians start restarting consultations or abandoning notes, something has gone fundamentally wrong — either the system has degraded or the workflow is broken. This is a leading indicator that should trigger immediate investigation, not routine review.

---

### 🔵 Cognitive Load Assessment

Mental effort for review. Target: 'effortful but efficient' — enough to catch errors, not so much that time savings disappear.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
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

**Novel Thinking / Implications**

> 💡 Optimal load is non-obvious: too low = disengagement, too high = no benefit.

---

### 🔵 Inter-Clinician Edit Variance

Do different clinicians edit the same AI output similarly? High variance suggests either ambiguous AI output (different clinicians read it differently) or inconsistent quality standards across clinicians. Both are governance issues.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
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

> 💡 If Clinician A always edits the AI output extensively and Clinician B never edits it, the issue might be either clinician (one is too critical, the other is too lax) or the AI (the output is ambiguous). Inter-clinician variance reveals whether the review function is consistent — a prerequisite for meaningful aggregate metrics.

---

### 🔵 Clinical Documentation Skill Attenuation

Longitudinal ability to document without AI. Sleeper risk — if a generation trains with AVT, baseline capability degrades.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Aviation skill degradation literature |

**Why this tier?**

> Long-term longitudinal study. Effects take years to manifest. Important for workforce planning but not actionable at individual deployer level.

**Formal Definition**

```
Annual: clinicians document N simulated encounters without AI, scored via PDSQI-9. SA(t) = PDSQI9_noAI(t) - PDSQI9_noAI(t-1). Negative SA = attenuation. Compare trainees against pre-AVT cohort norms.
```

**References**

- **Aviation analogy**: Casner & Schooler (2014) — pilot skill degradation

**Limitations**

> Long-term study. Hard to isolate AVT as cause.

**Novel Thinking / Implications**

> 💡 Medical education bodies should be tracking this now.

---

### 🔵 Cognitive Offloading Rate

Proportion of clinicians who report relying on AI for content recall ('I don't need to remember, the AI will catch it'). Different from automation bias — this is active delegation rather than passive trust. Predicts skill attenuation.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
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

### 🔵 Trust Halo Decay Rate

Whether initial high trust persists after errors. Absent decay = dangerous over-trust. Trust halo drives off-label scope creep.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Survey |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Trust halo effect analysis |

**Why this tier?**

> Research metric requiring longitudinal measurement. Conceptually important for understanding off-label use drivers but not operationally measurable at scale.

**Formal Definition**

```
Longitudinal T(t). After error at t_e, decay rate λ = -dT/dt for t > t_e. Healthy: λ > 0 (appropriate recalibration). Dangerous: λ ≈ 0 (trust unchanged despite evidence).
```

**Limitations**

> Longitudinal measurement required.

**Novel Thinking / Implications**

> 💡 Trust halo → off-label use: over-trust drives scope creep. The halo is the mechanism; off-label use is the consequence.

---

### 🔵 Note Review Fatigue Trajectory

Review quality degradation over a clinical session. The 9am note review may be different from the 5pm note review, and AVT may amplify end-of-session fatigue effects by adding documentation review burden to existing clinical fatigue.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Passive Observational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Deployer, Academic |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Clinical fatigue research applied to AVT review |

**Why this tier?**

> Research metric. Important workforce safety question but not routinely measurable.

**Formal Definition**

```
Track review quality metrics (time-to-sign, edit rate, error detection in injection audits) by time-of-day and session position. Fatigue Slope = degradation rate per hour into session. Significant negative slope indicates fatigue effects.
```

**Limitations**

> Confounded with case mix variation (afternoon clinics may have different complexity). Requires careful statistical controls.

**Novel Thinking / Implications**

> 💡 If review quality degrades through the session, the safety implications are significant: the last patients of the day get the least rigorous oversight. AVT systems designed assuming consistent reviewer attention are operating outside that assumption for a meaningful fraction of consultations. This argues for fatigue-aware workflow design — perhaps requiring more thorough review for end-of-session notes, or rotating review responsibility.

---

