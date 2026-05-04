### GV.TC-1 🟢 Clinician Training Completion Rate

Percentage of AVT-using clinicians who have completed required training modules: vendor product training, local induction (review-before-signing, known failure modes, error reporting, opt-out processes), and periodic refresher training.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.TC-1 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Day Zero Baseline, Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | [NAS-Day-Zero-SPI-internal] requirements; standard clinical governance |

**Why this tier?**

> Governance requirement. No clinician should use AVT without completing required training. Binary compliance metric - 100% is the only acceptable target.

**Formal Definition**

```
TCR = |clinicians_fully_trained| / |clinicians_using_AVT|. Fully trained = completed all required modules within validity period. Track by module: vendor training, local induction, failure mode awareness, refresher. TCR < 100% = governance non-compliance.
```

**Reference Standard**

> Authoritative source: the deployer's clinical governance training record (LMS or equivalent), with module catalogue mapped against the [NAS-Day-Zero-SPI-internal] training requirements and local induction policy. Four mandatory modules MUST be enumerated:
>
> - **M1: Vendor product training** — system mechanics, activation, opt-out, error reporting per the specific AVT product
> - **M2: Local induction** — review-before-signing workflow, opt-out and dissent procedures (cross-link [GV.CR-1 Patient Dissent Recording Rate](#gv-cr-1) and [GV.CR-2 Verbal Notification Compliance](#gv-cr-2)), incident-reporting pathway
> - **M3: Failure-mode awareness** — AVT-specific failure modes (hallucination/omission asymmetry, speaker misattribution, accent-related accuracy variation, complacency trajectory, system-unavailable fallback)
> - **M4: Refresher** — annual re-engagement on M1-M3 with updates reflecting deployed system changes
>
> "Completed" requires evidenced engagement, not just course-record entry. Module-completion timestamps recorded; minimum-engagement-time floors specified per module to prevent "5-minute completion".

**Operational Specification**

> - **Window:** continuous; monthly compliance reporting per practice / per clinician.
> - **Population:** every clinician using AVT (denominator). Clinicians who have stopped using AVT but remain on the practice register are excluded with reason.
> - **Per-module reporting MANDATORY:** four sub-rates (M1/M2/M3/M4 completion). Aggregate TCR alone is insufficient — a clinician missing M3 (failure-mode awareness) is a different risk from one missing M4 (refresher overdue).
> - **Validity periods MANDATORY (per module):** M1 valid for the lifetime of the deployed system version (revoked on major vendor product upgrade per [GV.SG-1 Model Version Tracking](#gv-sg-1)); M2 valid until significant local-policy change; M3 valid 12 months; M4 must be completed within 12 months of the previous engagement (rolling).
> - **Engagement-time floor MANDATORY:** minimum 30 minutes recorded engagement on M3 specifically (the failure-mode-awareness module is the most subject to "click-through" completion); 15 minutes on M1; 20 minutes on M2.
> - **Coverage check:** any clinician active on AVT in the previous 30 days appears in the denominator. Late-onboarders given a 14-day grace window from first AVT use to completion of M1 + M2.

**Trigger Conditions**

> ⚠️ **Provenance:** the four-module structure follows from the existing Formal Definition and the [NAS-Day-Zero-SPI-internal] requirements cited in Source. The AVT-specific failure-mode list in M3 carries from the Novel Thinking section. Specific numerical thresholds (30/20/15-minute engagement floors, 12-month refresher cadence, 14-day onboarding grace, 100 % gate) are **proposed in v3.5 as starting points**, not externally validated. Indicative; require local calibration against the deployer's clinical governance framework before contractual use.
>
> - **Pre-deployment / Day Zero gate:** every clinician scheduled to use AVT has M1 + M2 + M3 complete within validity periods; M4 not yet applicable for new starters.
> - **Continuous monitoring:** monthly per-module TCR ≥ 100 %; alert on any clinician active on AVT with any module out of date by > 14 days.
> - **Pause / escalation trigger:** any clinician using AVT with M3 (failure-mode awareness) missing or stale (this is the safety-critical module — operational use without it is a governance failure regardless of M1/M2/M4 status); OR aggregate TCR < 95 % at the practice level for any module sustained two consecutive months.
>
> Specific numerical starting points are deployment-context-dependent and live in [Threshold Reference: GV.TC-1](../thresholds.md#gv-tc-1). Treat them as starting points to calibrate locally — not as contractual gates.



**Limitations**

> Completion ≠ competence. A clinician who completed e-learning in 5 minutes has 'completed' training but may not have learned anything. The Operational Specification's engagement-time floors prevent the most blatant click-through pattern but cannot test actual understanding; pair with [GV.TC-2 Failure Mode Awareness Score](#gv-tc-2) for an outcome-side check on whether training has produced competence.

**Novel Thinking / Implications**

> 💡 Training should include AVT-specific failure modes that differ from general AI awareness: hallucination vs omission asymmetry, speaker misattribution patterns, accent-related accuracy variation, the complacency trajectory, and what to do when the system is unavailable. Generic 'AI awareness' training is insufficient.

---

### GV.TC-2 🟡 Failure Mode Awareness Score

Clinician knowledge of AVT-specific failure modes: can they identify hallucination, omission, speaker misattribution, and coding errors? Tested via scenario-based assessment, not self-report.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.TC-2 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Day Zero Baseline, Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
| **Source** | Proposed - extends error injection concept to training assessment |

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

### GV.TC-3 🟡 Refresher Training & CPD Compliance

Ongoing competency maintenance: are clinicians completing periodic refresher training that incorporates new failure modes discovered through operational monitoring and incident reports?

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.TC-3 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
| **Source** | Standard clinical governance CPD requirements; applied to AVT |

**Why this tier?**

> Ongoing competency maintenance. Content should be data-driven from operational monitoring. Annual minimum, triggered by model updates.

**Formal Definition**

```
Compliance = |clinicians_current_on_refresher| / |clinicians_using_AVT|. Refresher content must be updated to include: (a) locally discovered failure modes, (b) national safety alerts, (c) model update implications, (d) new attack vectors. Frequency: minimum annually, triggered by model updates.
```

**Limitations**

> Refresher fatigue - clinicians already have substantial CPD requirements. AVT-specific refresher competes for limited time. Must be efficient and clinically relevant.

**Novel Thinking / Implications**

> 💡 Refresher content should be data-driven: if edit-pattern monitoring reveals a new failure mode (e.g. systematic omission of safety-netting advice), the refresher should include examples of that specific failure. Generic refresher training is less effective than targeted, evidence-based updates.

**Relationship to [GV.TC-1 Clinician Training Completion Rate](#gv-tc-1)**

> v3.5 tightening of GV.TC-1 enumerated four mandatory training modules with **M4 Refresher** as one of them, and v3.6 duplication review flagged the apparent overlap with GV.TC-3. v3.8 retains both with explicit framing rather than folding:
>
> - **GV.TC-1 M4** measures *whether* refresher engagement has occurred (per-clinician completion rate against the rolling 12-month validity window); a process-compliance metric for the four-module training framework.
> - **GV.TC-3** (this metric) measures *what* the refresher contains: the four content-currency requirements (locally discovered failure modes, national safety alerts, model-update implications, new attack vectors). The metric exists to prevent generic CPD theatre — a clinician completing M4 against content that hasn't been updated in three years passes GV.TC-1's M4 check but fails GV.TC-3's content-currency check.
>
> Headline reporting at the deployment level should pair the two: GV.TC-1 M4 completion rate alongside GV.TC-3 content-currency compliance. Either alone is incomplete.

---

### GV.TC-4 🔵 Trainee Impact Assessment

Does AVT use during training affect junior clinician skill development? GMC educational standards consideration. If trainees learn to consult with AVT from day one, they may not develop documentation skills the profession traditionally relied on.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.TC-4 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Hybrid |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Academic, National Body |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Distal |
| **Applicability** | General Healthcare AI |
| **Source** | Medical education literature; [GMC] standards consideration |

**Why this tier?**

> Long-term workforce question. National research priority but not deployer-actionable.

**Formal Definition**

```
Compare documentation skills of: (1) trainees who learned with AVT from start; (2) trainees who learned without AVT then transitioned. Measure: independent documentation quality (PDSQI-9), clinical reasoning evident in notes, ability to function when AVT unavailable.
```

**Limitations**

> Long-term study required. Effects take years to manifest. Difficult to control for cohort differences.

**Novel Thinking / Implications**

> 💡 This is the medical education question that should be answered before AVT becomes ubiquitous in training environments. If trainees lose documentation skills, the workforce loses resilience - what happens when AVT is unavailable, malfunctioning, or contraindicated? Medical Royal Colleges should be tracking this.

---

### GV.TC-5 🟡 Training Material Currency

Is training content updated to reflect newly discovered failure modes from operational monitoring? Static training that doesn't incorporate lessons from incidents misses opportunities to prevent recurrence.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.TC-5 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Human Factors |
| **Measurement Method** | Human Review |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | General Healthcare AI |
| **Source** | Standard training governance |

**Why this tier?**

> Operational governance metric. Should be tracked as part of incident-to-training feedback loop.

**Formal Definition**

```
Training Currency = days since last update of training materials. Coverage of recent failure modes: |recent_failure_modes_covered_in_training| / |recent_failure_modes_identified|. Target: training updated within 90 days of any new failure mode discovery.
```

**Limitations**

> Requires connection between operational monitoring and training update process - often disconnected.

**Novel Thinking / Implications**

> 💡 Training that doesn't evolve with operational experience is a missed opportunity. When a new failure mode is discovered (e.g. systematic omission of safety-netting in a particular context), the training should be updated within weeks, not years.

---

