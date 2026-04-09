# Part E — System Governance

## Safety & Governance

*Cross-cutting safety monitoring, model tracking, incident reporting, and governance infrastructure.*

**Tier breakdown**: 🟢 6 Tier 1 · 🟡 5 Tier 2 · 🔵 2 Tier 3

### 🟢 Model Version Tracking

Logging which model version produces each output. Foundation for all continuous metrics — without it, performance changes are uninterpretable.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | Keyes et al., Stanford, Dec 2025 |

**Why this tier?**

> Foundation for all continuous assurance. Without knowing which model version produced which output, no performance change is interpretable. Must be contractually required.

**Formal Definition**

```
Per inference: log model_id, model_version, timestamp, config_hash. On change (v_old → v_new), monitoring window W with duration Δt calibrated for statistical power ≥0.8.
```

**References**

- **Stanford**: [Keyes et al. (2025)](https://arxiv.org/abs/2512.09048)

**Limitations**

> Not contractually mandated in most NHS procurement.

**Novel Thinking / Implications**

> 💡 Three-layer surveillance: detected nationally (contractual), evaluated regionally (benchmark), monitored locally (edit-pattern shift).

---

### 🟡 Model Update Impact Score

Standardised before/after on update. Governance: vendor notifies → regional benchmark → local monitoring.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Regional (ICB) |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | NAS + Stanford frameworks |

**Why this tier?**

> Triggered by model version changes. Requires vendor notification and deployer/regional benchmark suite. The three-layer surveillance model depends on this.

**Formal Definition**

```
Impact IS = Σ w_m × (metric_new - metric_old) / metric_old. Mandatory re-evaluation if IS < -0.05 on any safety metric.
```

**References**

- **NAS**: Three-layer surveillance
- **Stanford**: [Keyes et al. (2025)](https://arxiv.org/abs/2512.09048)

**Limitations**

> Requires vendor notification + deployer benchmark capacity.

**Novel Thinking / Implications**

> 💡 Benchmark suite should be nationally standardised for cross-site comparison.

---

### 🔵 Probabilistic Risk Quantification (P₁/P₂)

Medical device safety paradigm for LLMs. First quantitative risk analysis: P₁ from 2.0×10⁻⁸ to 2.6×10⁻⁴.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Vendor, Academic |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Source** | medRxiv, Nov 2025 |

**Why this tier?**

> Research methodology. First published PRA for LLM-SaMD. Important for DCB0129 maturity but requires clinical harm pathway modelling that doesn't yet exist for AVT.

**Formal Definition**

```
P₁ = P(hazardous output | normal use). P₂ = P(harm | hazardous output). Risk R = P₁ × P₂ × Severity. P₂ requires clinical harm pathway modelling with probability attenuation at each stage.
```

**References**

- **Preprint**: medRxiv, Nov 2025 — 14 open-source LLMs

**Limitations**

> Validated on open-source only. Commercial AVT = black box.

**Novel Thinking / Implications**

> 💡 For DCB0129: translating error rates into P₁/P₂ makes safety cases quantitative, not just qualitative.

---

### 🔵 DeepScore (Defect-Free Rate)

Two-tier: Major Defect-Free Rate + Critical Defect-Free Rate. 135,900 notes. Sound approach but proprietary definitions.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Summarisation |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Vendor-Proprietary |
| **Outcome Type** | Proximal |
| **Source** | DeepScribe |

**Why this tier?**

> Vendor-proprietary (DeepScribe). Sound two-tier severity approach but proprietary definitions prevent cross-vendor comparison.

**Formal Definition**

```
MDFR = |N_no_major| / |N_total|. CDFR = |N_no_critical| / |N_total|. Vendor-specific severity definitions — not aligned to external standard.
```

**References**

- **DeepScore**: DeepScribe, arXiv Sept 2024

**Limitations**

> Proprietary severity definitions. Human QA in enterprise tier conflates AI + human performance.

**Novel Thinking / Implications**

> 💡 CREOLA taxonomy is best candidate for common severity framework.

---

### 🟢 Safety Performance Indicators with Thresholds (DSCMS)

Metrics + thresholds + escalation = governance. A metric without a threshold is information; with a threshold and action it becomes governance.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer, Regional (ICB) |
| **Maturity** | Emerging |
| **Outcome Type** | Proximal |
| **Source** | DSCMS methodology in NAS framework |

**Why this tier?**

> The governance mechanism that converts metrics into action. Without pre-defined thresholds and escalation paths, metrics are information without teeth. Every Tier 1 metric needs an SPI wrapper.

**Formal Definition**

```
For SPI s: measurement M(s), threshold T(s), action A(s). If M(s) > T(s) for duration d → trigger A(s). Tiered: Review / Pause / Suspend.
```

**References**

- **DSCMS**: Dynamic Safety Case Management System

**Limitations**

> Threshold-setting is judgemental.

**Novel Thinking / Implications**

> 💡 Every metric here should be assessable for SPI candidacy.

---

### 🟡 Off-Label Use Detection Rate

AVT use outside validated contexts. Well-intentioned scope creep — each boundary crossing compounds risk.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Compound boundary risk model; NHSE LLM framework |

**Why this tier?**

> Deployer monitoring. Technically feasible if the validated use envelope is machine-readable. Detects well-intentioned scope creep that compounds boundary risk.

**Formal Definition**

```
Validated envelope V = set of (domain, type, population, setting) tuples. Boundary distance BD(e) = dimensions where encounter e falls outside V. OLR = |{e: BD>0}| / |E_total|. BD > 2 → immediate CSO review.
```

**References**

- **Compound risk**: Compound boundary risk model

**Limitations**

> Requires clear validated envelope definition.

**Novel Thinking / Implications**

> 💡 Automated detection feasible if validated envelope is machine-readable.

---

### 🟢 Adverse Event / Incident Rate (LFPSE)

National patient safety reporting. Ultimate lagging indicator. No specific LFPSE category for AI/AVT incidents exists.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer, National Body |
| **Maturity** | Established |
| **Outcome Type** | Distal |
| **Source** | LFPSE national reporting |

**Why this tier?**

> Established national reporting. The ultimate lagging indicator — by the time this metric moves, harm has occurred. Needs dedicated LFPSE category for AI/AVT incidents.

**Formal Definition**

```
IR = N_incidents / N_encounters. Stratify by severity. Currently no LFPSE taxonomy code for AI/AVT — coded under general documentation errors.
```

**References**

- **LFPSE**: NHS Learn From Patient Safety Events

**Limitations**

> Massive under-reporting. No specific AI/AVT category. Unknown denominator.

**Novel Thinking / Implications**

> 💡 Dedicated LFPSE reporting category needed for this to function as national signal.

---

### 🟡 Cross-Practice Variance Coefficient

Performance variation across practices within ICB. High variance = context-dependent performance. Justifies regional assurance tier.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Regional (ICB) |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Multi-level assurance framework |

**Why this tier?**

> Regional (ICB) metric. Justifies the regional assurance tier. Requires standardised metrics collection across practices.

**Formal Definition**

```
CV_m = σ(m across practices) / μ(m). High CV (>0.3) = context-dependent. ANOVA to identify drivers: practice size, demographics, template, clinician experience.
```

**Limitations**

> Requires standardised collection across practices.

**Novel Thinking / Implications**

> 💡 Same AVT, different quality = contextual difference. That's deployer responsibility, not vendor's.

---

### 🟢 Assurance Debt Accumulation Rate

Gap between required and completed assurance. The honest metric — better visible and managed than hidden until incident.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Meta-evaluation |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer, Regional (ICB) |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Multi-level assurance framework |

**Why this tier?**

> The honest governance metric. Every deployer will accumulate it. Making it visible, tracked, and managed prevents governance theatre.

**Formal Definition**

```
AD(t) = |A_due(t)| - |A_completed(t)|. Decompose: clinical audit, SPI review, training refresh, patient feedback, model update check.
```

**Limitations**

> Requires defined schedule. Risk of checkbox compliance.

**Novel Thinking / Implications**

> 💡 '3 overdue audits and 2 unresolved SPI breaches' is more useful than 'everything is fine.'

---

### 🟢 Near-Miss Reporting Rate

Incidents caught by clinician review before reaching the EPR. The leading indicator that LFPSE rate is the lagging indicator of. A high near-miss rate with low LFPSE rate suggests the human review layer is functioning; a low near-miss rate may indicate either an excellent system or inadequate review.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Patient safety leading vs lagging indicator literature |

**Why this tier?**

> Essential leading indicator. Should be Tier 1 because it's the early warning system that LFPSE is the lagging indicator of. Requires lightweight reporting infrastructure.

**Formal Definition**

```
Near-Miss Rate = |errors_caught_in_review| / |total_AI_outputs|. Track separately from LFPSE incidents (errors that reached the record). Healthy ratio: high near-miss rate, low LFPSE rate. Concerning ratio: low near-miss rate, any LFPSE incidents.
```

**Limitations**

> Requires clinicians to actively report near-misses, which is often under-reported in busy clinical practice.

**Novel Thinking / Implications**

> 💡 The leading indicator: by the time LFPSE moves, harm has occurred. Near-miss reporting catches errors before they cause harm — but only if there's a low-friction reporting mechanism and a no-blame culture. The ratio of near-miss to actual incidents is itself diagnostic of safety culture.

---

### 🟡 Time-to-Correct

When an AVT error is detected, how quickly is it corrected and the lessons disseminated? Measures the responsiveness of the governance loop from detection to action.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Standard incident response metric applied to AVT |

**Why this tier?**

> Important operational governance metric. Requires structured incident tracking.

**Formal Definition**

```
Time-to-Correct = t_correction_implemented - t_error_detected. Track per error severity. Critical errors: target < 24 hours. Major errors: target < 1 week. Includes: error correction in record, communication to other clinicians, model/template adjustment if applicable.
```

**Limitations**

> Requires structured incident tracking. 'Correction' may have multiple stages with different completion times.

**Novel Thinking / Implications**

> 💡 A long time-to-correct means errors persist in the system and may affect multiple patients before resolution. This is operationally important — a single error is bad, but a single error that took 3 weeks to correct is a governance failure.

---

### 🟡 SPI Escalation Response Time

When an SPI threshold is breached, how quickly does the governance response actually occur? Measures whether the SPI framework is operationally functional or just a paper exercise.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer, Regional (ICB) |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Operational extension of DSCMS SPI framework |

**Why this tier?**

> Important governance functionality test. Requires SPI monitoring infrastructure to be in place.

**Formal Definition**

```
Escalation Response Time = t_governance_action - t_SPI_breach. Track per escalation level (review trigger, pause trigger). Target: review actions within 48 hours, pause actions within 4 hours. Note: pause should be automatic, not requiring human action.
```

**Limitations**

> Requires automated SPI monitoring and structured escalation tracking. Most current implementations are manual.

**Novel Thinking / Implications**

> 💡 An SPI framework that takes a week to respond to a breach is not protecting anyone. The whole point of pre-defined thresholds with escalation paths is to enable rapid response. Measuring response time reveals whether the framework is operationally functional or governance theatre.

---

### 🟢 Hazard Log Completeness

DCB0129 requires a hazard log. Is it actually maintained and updated as new failure modes are discovered operationally? A static hazard log written at deployment and never updated is a compliance failure with safety implications.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Safety |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | DCB0129 compliance requirement |

**Why this tier?**

> Regulatory requirement under DCB0129. Tier 1 because it's a compliance obligation, not a recommendation. Should be linked to operational monitoring.

**Formal Definition**

```
Hazard Log Currency = (date_of_last_update - today) in days. Hazard Coverage = |operationally_observed_failure_modes_in_log| / |total_observed_failure_modes|. Currency target: updated within 30 days of any new failure mode discovery.
```

**References**

- **DCB0129**: DCB0129 hazard log requirement

**Limitations**

> Requires connecting operational monitoring to hazard log update process — often disconnected in current practice.

**Novel Thinking / Implications**

> 💡 DCB0129 hazard logs are often written once at deployment and forgotten. As operational monitoring discovers new failure modes (through edit pattern analysis, near-miss reporting, incident investigation), these should be added to the hazard log with mitigations. A hazard log that hasn't been updated in 6 months is either a perfect system or a compliance failure — and almost certainly the latter.

---

