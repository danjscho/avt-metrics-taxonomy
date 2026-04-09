## Training & Competency

*Clinician readiness: training completion, failure mode awareness, and ongoing competency maintenance.*

**Tier breakdown**: 🟢 1 Tier 1 · 🟡 3 Tier 2 · 🔵 1 Tier 3

### 🟢 Clinician Training Completion Rate

Percentage of AVT-using clinicians who have completed required training modules: vendor product training, local induction (review-before-signing, known failure modes, error reporting, opt-out processes), and periodic refresher training.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟢 Tier 1 — Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Day Zero Baseline, Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Source** | NAS Day Zero requirements; standard clinical governance |

**Why this tier?**

> Governance requirement. No clinician should use AVT without completing required training. Binary compliance metric — 100% is the only acceptable target.

**Formal Definition**

```
TCR = |clinicians_fully_trained| / |clinicians_using_AVT|. Fully trained = completed all required modules within validity period. Track by module: vendor training, local induction, failure mode awareness, refresher. TCR < 100% = governance non-compliance.
```

**Limitations**

> Completion ≠ competence. A clinician who completed e-learning in 5 minutes has 'completed' training but may not have learned anything.

**Novel Thinking / Implications**

> 💡 Training should include AVT-specific failure modes that differ from general AI awareness: hallucination vs omission asymmetry, speaker misattribution patterns, accent-related accuracy variation, the complacency trajectory, and what to do when the system is unavailable. Generic 'AI awareness' training is insufficient.

---

### 🟡 Failure Mode Awareness Score

Clinician knowledge of AVT-specific failure modes: can they identify hallucination, omission, speaker misattribution, and coding errors? Tested via scenario-based assessment, not self-report.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Day Zero Baseline, Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Proposed — extends error injection concept to training assessment |

**Why this tier?**

> Scenario-based competency assessment. More meaningful than training completion (which measures attendance, not learning). Annual assessment recommended.

**Formal Definition**

```
FMAS = |failure_modes_correctly_identified| / |failure_modes_presented|. Tested via annotated note scenarios containing seeded errors of each type. Threshold: FMAS ≥ 80% for all clinicians. Re-test at 6-month intervals to track knowledge decay.
```

**Limitations**

> Scenario-based testing in a training context differs from real-world detection under time pressure. Clinicians who can identify errors in a test may still miss them in practice.

**Novel Thinking / Implications**

> 💡 This connects to the automation bias error injection metric: failure mode awareness is the training prerequisite, error injection is the operational test. A clinician who cannot identify a hallucination in a training scenario will not catch one in practice. FMAS < 80% should delay that clinician's AVT deployment, not just trigger more training.

---

### 🟡 Refresher Training & CPD Compliance

Ongoing competency maintenance: are clinicians completing periodic refresher training that incorporates new failure modes discovered through operational monitoring and incident reports?

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Standard clinical governance CPD requirements; applied to AVT |

**Why this tier?**

> Ongoing competency maintenance. Content should be data-driven from operational monitoring. Annual minimum, triggered by model updates.

**Formal Definition**

```
Compliance = |clinicians_current_on_refresher| / |clinicians_using_AVT|. Refresher content must be updated to include: (a) locally discovered failure modes, (b) national safety alerts, (c) model update implications, (d) new attack vectors. Frequency: minimum annually, triggered by model updates.
```

**Limitations**

> Refresher fatigue — clinicians already have substantial CPD requirements. AVT-specific refresher competes for limited time. Must be efficient and clinically relevant.

**Novel Thinking / Implications**

> 💡 Refresher content should be data-driven: if edit-pattern monitoring reveals a new failure mode (e.g. systematic omission of safety-netting advice), the refresher should include examples of that specific failure. Generic refresher training is less effective than targeted, evidence-based updates.

---

### 🔵 Trainee Impact Assessment

Does AVT use during training affect junior clinician skill development? GMC educational standards consideration. If trainees learn to consult with AVT from day one, they may not develop documentation skills the profession traditionally relied on.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Academic, National Body |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Source** | Medical education literature; GMC standards consideration |

**Why this tier?**

> Long-term workforce question. National research priority but not deployer-actionable.

**Formal Definition**

```
Compare documentation skills of: (1) trainees who learned with AVT from start; (2) trainees who learned without AVT then transitioned. Measure: independent documentation quality (PDSQI-9), clinical reasoning evident in notes, ability to function when AVT unavailable.
```

**Limitations**

> Long-term study required. Effects take years to manifest. Difficult to control for cohort differences.

**Novel Thinking / Implications**

> 💡 This is the medical education question that should be answered before AVT becomes ubiquitous in training environments. If trainees lose documentation skills, the workforce loses resilience — what happens when AVT is unavailable, malfunctioning, or contraindicated? Medical Royal Colleges should be tracking this.

---

### 🟡 Training Material Currency

Is training content updated to reflect newly discovered failure modes from operational monitoring? Static training that doesn't incorporate lessons from incidents misses opportunities to prevent recurrence.

| Dimension | Value |
|-----------|-------|
| **Priority Tier** | 🟡 Tier 2 — Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Source** | Standard training governance |

**Why this tier?**

> Operational governance metric. Should be tracked as part of incident-to-training feedback loop.

**Formal Definition**

```
Training Currency = days since last update of training materials. Coverage of recent failure modes: |recent_failure_modes_covered_in_training| / |recent_failure_modes_identified|. Target: training updated within 90 days of any new failure mode discovery.
```

**Limitations**

> Requires connection between operational monitoring and training update process — often disconnected.

**Novel Thinking / Implications**

> 💡 Training that doesn't evolve with operational experience is a missed opportunity. When a new failure mode is discovered (e.g. systematic omission of safety-netting in a particular context), the training should be updated within weeks, not years.

---

