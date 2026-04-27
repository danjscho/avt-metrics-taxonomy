# Plan: Extend Standards Mapping + Add Responsible AI Lens

## Context

The existing [taxonomy/_standards-mapping.md](taxonomy/_standards-mapping.md) covers four NHS/regulatory frameworks: DTAC v2.0, DSPT v8, DCB0129/0160, and the NHS LLM Evaluation & Monitoring Framework v0.2.2. This plan extends the taxonomy's assurance coverage in two complementary ways:

**Part 1 - Seven additional NHS/UK standards** mapped into the existing standards-mapping document (mixed granularity)

**Part 2 - A new cross-cutting Responsible AI lens document** (`_responsible-ai-lens.md`) that tags metrics against:
- The **10 principles** from the DSIT AI Playbook for the UK Government (Feb 2025)
- The **6 ethical themes** of responsible AI (the AI Regulation White Paper's five principles + Societal Wellbeing as the sixth, as articulated in the Playbook ethics chapter)

**Why the two-part approach:**
Standards and principles are categorically different. The 7 standards (Part 1) prescribe *what artefacts/processes/criteria must exist* - they fit the existing assertion-level tables. The Playbook principles and ethical themes (Part 2) are *policy lenses* - every metric hits multiple principles/themes, the Playbook itself acknowledges trade-offs between them, and the value is cross-tagging not 1:1 mapping. A separate lens document mirrors the existing `_applicability.md` pattern and keeps the standards-mapping doc coherent.

**Why Part 1 additions:** Deployers, vendors, and assurance teams need coverage of the full NHS regulatory landscape. The selected additions close genuine gaps:
- **MHRA SaMD/AIaMD** adds the regulatory classification pathway (distinct from DCB0129 clinical risk management)
- **NICE ESF** adds the evidence-gathering dimension required for commissioning decisions
- **CQC Assessment** adds the deployer-side inspection perspective (DTAC is vendor-side)
- **PSIRF** adds systems-learning from incidents (beyond DCB0129 Stage 7)
- **PRSB** adds the semantic layer of clinical records (FHIR/openEHR are technical)
- **Caldicott Principles** adds the strategic governance layer that DSPT operationalises
- **FHIR UK Core** refines existing FHIR mapping with UK-specific constraints

**Why Part 2 additions:** UK Government AI assurance is increasingly framed through the Playbook principles and six themes. ICB boards, assurance teams, and ethicists coming from the policy side need a view of the taxonomy through that lens. The NHS LLM Evaluation Framework's three groups (already mapped) are an operationalisation layer - the Playbook themes give the policy-intent axes, and the NHS framework gives the measurement-method axes. Both are needed.

**Decisions locked in** (from user clarification):
- **Scope**: 7 selected NHS standards + DSIT Playbook 10 principles + 6 ethical themes
- **Part 1 granularity**: assertion-level for formal standards (MHRA, NICE ESF, FHIR UK Core), higher-level summary for less formal ones (CQC, PSIRF, PRSB, Caldicott)
- **Part 1 scope**: mapping + flagged gaps - map existing metrics against new standards, include a "Proposed new metrics" section listing what would close identified gaps, but **do not add new metrics in this round**
- **Part 2 shape**: new document `_responsible-ai-lens.md` (Option B from design discussion) - separate from standards mapping, consistent with `_applicability.md` pattern
- **Sequencing**: all in one extended plan (Option a), but broken into subtasks for separate commits
- **EU AI Act**: not re-extended (already covered via GV.CR-10 at current depth)

---

## Scope

### Part 1: Standards to add to `_standards-mapping.md`

| # | Standard | Granularity | Publisher | Status |
|---|----------|-------------|-----------|--------|
| 1 | **MHRA SaMD / AIaMD** - Change Programme WPs + SI 2024 No. 1368 PMS + Transparency Guiding Principles (June 2024) + GMLP (Oct 2021) | Assertion-level | MHRA | Mandatory for devices; cascading via vendors |
| 2 | **NICE Evidence Standards Framework for DHTs (ECD7)** - 21 standards × A/B/C tiers × min/best; AI provisions in Standards 4, 5, 6, 15, 16 | Assertion-level | NICE | De facto mandatory for commissioning |
| 3 | **FHIR UK Core / INTEROPen** - STU1/STU2/STU3 profiles + UK extensions | Assertion-level (refines TP.WB-6/7) | NHS England Digital / INTEROPen | De facto interop standard |
| 4 | **CQC Assessment for AI** - GP Mythbuster 109 + Single Assessment Framework quality statements under 5 key questions | Higher-level summary | CQC | Mandatory inspection |
| 5 | **Patient Safety Incident Response Framework (PSIRF)** - 4 principles + response types (AAR/PSII/SEIPS) + engagement/oversight | Higher-level summary | NHS England | Mandatory for most NHS providers (full rollout by end 2023; primary care 2025–26) |
| 6 | **PRSB Clinical Documentation Standards** - Core Information Standard + Outpatient Letter + Discharge + others; relationship to UK Core | Higher-level summary | PRSB | Emerging de facto |
| 7 | **Caldicott Principles** (8 principles, 2020 revision) | Higher-level summary | National Data Guardian | Foundational (CLDC + CQC Reg 17) |

### Part 2: Responsible AI lens document

New file `taxonomy/_responsible-ai-lens.md` tags existing metrics against:

**A. DSIT AI Playbook for the UK Government - 10 Principles** (Feb 2025):
1. You know what AI is and what its limitations are
2. You use AI lawfully, ethically and responsibly
3. You know how to use AI securely
4. You have meaningful human control at the right stages
5. You understand how to manage the full AI life cycle
6. You use the right tool for the job
7. You are open and collaborative (includes mandatory ATRS for central gov + ALBs)
8. You work with commercial colleagues from the start
9. You have the skills and expertise needed to implement and use AI
10. You use these principles alongside your organisation's policies and have the right assurance in place

**B. Six Responsible AI Ethical Themes** (White Paper five + Playbook-added sixth):
1. Safety, Security and Robustness
2. Appropriate Transparency and Explainability
3. Fairness
4. Accountability and Governance
5. Contestability and Redress
6. Societal Wellbeing and Public Good *(Playbook-added sixth theme)*

### Out of scope for this round

- **No new metrics** - gaps flagged in both Part 1 and Part 2 but not filled
- **No existing metric changes** - all 214 metrics stay as-is
- **EU AI Act** not extended beyond existing GV.CR-10
- Royal College guidance, ORCHA, CCS RM6200, HRA AI ethics, DAPB 3051 - not selected
- AI Regulation White Paper not mapped separately (subsumed by Playbook's six themes)
- Data Ethics Framework, ATRS mentioned but not separately mapped

---

## Approach

### Files to modify / create

- **Modify:** `taxonomy/_standards-mapping.md` - extend with 7 new standards (Part 1)
- **Create:** `taxonomy/_responsible-ai-lens.md` - new cross-cutting lens document (Part 2)
- **Modify:** `taxonomy/build.py` - add `_responsible-ai-lens.md` to build order (after `_standards-mapping.md`)
- **Modify:** `taxonomy/_contents.md` - add entry for the new lens document
- **Modify:** `CHANGELOG.md` - add v3.1 entry at the end

### Part 1 section structure per standard

**For assertion-level standards (MHRA, NICE ESF, FHIR UK Core):**

```markdown
### {Standard Name} {version}

{Brief introduction: publisher, scope, mandatory status, AVT relevance}

#### {Sub-section / criterion group}

| {Standard} Criterion | Description | Taxonomy Metrics | Tier |
|---------------------|-------------|-----------------|------|
| {Ref} | {Description} | {Ref ID} {Metric Name} | 🟢 1 / 🟡 2 / 🔵 3 |

**Gaps:** {List what the taxonomy doesn't cover}
**Taxonomy extends:** {List what the taxonomy covers beyond this standard}
```

**For higher-level summary standards (CQC, PSIRF, PRSB, Caldicott):**

```markdown
### {Standard Name}

{Brief introduction: publisher, scope, mandatory status, AVT relevance}

**Key dimensions and taxonomy coverage:**

- **{Dimension 1}**: Covered by {TP.AC-1, GV.SG-3, ...}. {One-line commentary}
- **{Dimension 2}**: Partial - {coverage notes + gap}
- **{Dimension 3}**: Not covered - {what would be needed}

**Overall position:** {One paragraph on how the taxonomy relates to this standard overall}
```

### Part 2 lens document structure

`taxonomy/_responsible-ai-lens.md` sections:

```markdown
## Responsible AI Lens

{Intro: explains the lens approach, why it sits alongside standards mapping,
relationship to NHS LLM Evaluation Framework three groups, Playbook
trade-offs acknowledgement - principles and themes overlap intentionally}

### Part A - DSIT AI Playbook: 10 Principles

For each of the 10 principles:

#### Principle {N}: {Principle title}

{One-paragraph narrative on what the principle asks and how it applies to AVT}

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | Aspect of the principle |
|-----|--------|-------|------|------------------------|
| TP.AC-1 | Signal-to-Noise Ratio Monitoring | Audio Capture | 🟡 2 | Understanding limitations (P1) |
| ... |

**Gaps / areas not addressed:** {narrative}

### Part B - Six Ethical Themes

For each of the 6 themes (same structure as Part A):

#### Theme {N}: {Theme title}

{Narrative}

| Ref | Metric | Group | Tier | How the metric serves this theme |
|-----|--------|-------|------|----------------------------------|
| ... |

**Relationship to other themes:** {where this theme overlaps/trades off with others}

### Part C - Coverage Matrix

Summary table showing which metrics address multiple principles/themes
(highlights cross-cutting metrics - the ones that serve as policy-lever
metrics for multiple principles simultaneously).

### Part D - Gaps

Areas where neither the taxonomy nor existing metrics clearly address a
principle/theme, cross-referenced to the Proposed New Metrics section
in _standards-mapping.md where relevant.
```

**Metric-to-principle tagging approach:**
- Most metrics will tag to 2–4 principles and 1–3 themes (Playbook explicitly acknowledges trade-offs)
- Playbook principles 7–10 (openness, commercial, skills, org assurance) concentrate in Part E of the taxonomy
- Ethical theme 6 (Societal Wellbeing) concentrates in Part D (Patient Experience, Fairness) and Environmental & Sustainability
- Don't try to tag every metric against every principle - only meaningful tags (i.e., where the metric genuinely operationalises that principle)

### Proposed new metrics section (Part 1)

Add a new top-level section at the end of `_standards-mapping.md` (after the existing Gap Summary) titled **"Proposed New Metrics (Not Yet Implemented)"**. This lists candidate metrics that would close gaps identified during the mapping, organised by source standard. Each entry gives:
- Proposed reference ID slot (e.g. "GV.CR-11" - next available in the relevant group)
- Proposed metric name
- Short description of what it would measure
- Source standard and criterion it would satisfy
- Priority tier rationale

Gaps identified in Part 2 (Responsible AI lens) that warrant new metrics are also added here, cross-referenced.

This section is **informational only** - no metrics are added to the taxonomy in this round.

### Reference IDs in mapping tables

All existing standards-mapping entries already use reference IDs (e.g. `TP.WB-1`, `GV.CR-7`). New sections use the same convention - this was locked in by the recent reference-ID commit.

### Draft status flagging

- **NHS LLM Framework** is already flagged as v0.2.2 draft - no change
- **CQC emerging quality statements** - flag as "emerging (2025–26)" where referenced, since formal criteria not yet published
- **FHIR UK Core STU2/STU3** - flag STU2 as current (released May 2024), STU3 as "in development (sequence build)"
- **DSIT AI Playbook** - flag as "published Feb 2025; may be superseded by future iterations"

---

## Content details per standard / lens

### Part 1: Standards

#### 1. MHRA SaMD / AIaMD (assertion-level)

**Sub-sections to map:**
- **Classification (WP1, WP2)** - what qualifies as SaMD, intended purpose, manufacturer definition, UK MDR 2002 classification rules (most SaMD now Class IIa; higher-risk clinical decision tools IIb/III)
- **Premarket (WP3)** - best-practice SaMD development, data-driven SaMD (joint with HRA), human-centred SaMD
- **Post-Market Surveillance (WP4 + SI 2024 No. 1368, in force 16 June 2025)** - PMS Plan, PMSR (Class I/IIa on demand), PSUR (Class IIb/III annually), trend reporting, FSCA, Field Safety Notices, reporting timelines (2/10/15 working days), indirect harm reporting
- **Cybersecurity (WP5)** - legislation, guidance, vulnerability reporting
- **AI RIG (WP9)** - GMLP principles, bias across populations, bias identification/mitigation standards
- **Glass Box / Interpretability (WP10)** - human-centred AIaMD, trustworthy AIaMD standards
- **Ship of Theseus / Adaptivity (WP11)** - static/batch-trained/individualised/continuous learning categories, PCCPs for AIaMD
- **Transparency Guiding Principles (June 2024)** - WHO/WHY/WHAT/WHERE/WHEN/HOW framework with specific content items under WHAT (device characterisation, workflow integration, performance/safety, model logic, limitations, lifecycle)
- **GMLP 10 principles (Oct 2021)** - the full 10 including multi-disciplinary expertise, representative datasets, training/test independence, human-AI team focus, clinically relevant testing, deployment monitoring

**Expected taxonomy extends:** Strong coverage through Safety & Governance, NHS Compliance, Security, and Privacy & Data Governance groups.

**Expected gaps flagged:**
- Medical device classification documentation
- PCCP documentation for adaptive algorithms
- PMSR / PSUR report completeness
- Transparency documentation covering all WHAT content items
- GMLP 3 (representative training data) documentation

#### 2. NICE Evidence Standards Framework for DHTs (assertion-level)

**Sub-sections to map (21 numbered standards across 5 lifecycle areas):**

- **Design Factors (Standards 1–9):** Safety & Quality Compliance; User Acceptability; Environmental Sustainability; Inequalities & Bias Mitigation (AI-specific: algorithmic bias); Data Practices (AI-specific: GMLP alignment); Professional Oversight; Health Information Reliability; UK Professional Credibility; Safeguarding
- **Describing Value (Standards 10–13):** Intended Purpose & Target Population; Current Pathway; Proposed Pathway; Expected Impacts
- **Demonstrating Performance (Standards 14–16):** Effectiveness Evidence (Tier C only); Real-World Evidence (AI-specific: silent mode evaluation); Performance Monitoring Plan (AI-specific: post-deployment reporting, retraining schedules, subgroup drift monitoring)
- **Delivering Value (Standards 17–18):** Budget Impact Analysis; Cost-Effectiveness Analysis
- **Deployment (Standards 19–21):** Deployment Transparency; Communication/Consent/Training; Scalability

Each standard has **minimum** and **best practice** levels across **Tier A/B/C** functional classification. AVT typically sits in Tier B1 (communicating) or Tier C1/C2 (clinical management) depending on write-back configuration.

**Expected gaps flagged:**
- Tier classification documentation for the specific AVT deployment
- Silent mode evaluation evidence (Standard 15 best practice)
- Subgroup drift monitoring in deployment (Standard 16)
- Cost-effectiveness analysis (Standard 18) - no existing metric
- Budget impact analysis (Standard 17) - no existing metric

#### 3. FHIR UK Core / INTEROPen (assertion-level refinement)

**Sub-sections to map:**
- **Governance** - NHS England Digital + HL7 UK; INTEROPen community contribution; successor to CareConnect
- **STU1 (1.0.0, current)** - 12 foundational profiles (Patient, Practitioner, PractitionerRole, Organization, Location, AllergyIntolerance, Immunization, Medication, MedicationRequest, MedicationStatement, MedicationDispense, MedicationAdministration) + ~21 extensions
- **STU2 (2.0.2, released May 2024)** - 33 profiles adding clinical resources critical for AVT: Composition, Condition, Encounter, Observation, Procedure, ServiceRequest, DiagnosticReport
- **STU3 (in development sequence)** - ~52 profiles adding specialised Observation profiles (vital signs, NEWS2, blood glucose, alcohol, tobacco, etc.)
- **UK-specific constraints** - NHS Number + NHSNumberVerificationStatus extension; EthnicCategory; BirthSex; DeathNotificationStatus; ResidentialStatus; SNOMED CT primary terminology; dm+d for medicinal products

**Refinement of existing metrics:**
- `TP.WB-6` (FHIR R4 Resource Conformance Rate) - clarify "FHIR conformance" means UK Core profiles for NHS deployment, not generic FHIR R4
- `TP.WB-7` (openEHR Archetype Conformance) - similar clarification

**Expected gaps flagged:**
- Per-resource UK Core conformance (Composition, Encounter, Condition, AllergyIntolerance, MedicationStatement, Observation)
- UK-specific extension conformance (NHS Number verification, Ethnic Category binding)
- STU version targeting (STU1 cannot write back Composition/Condition/Observation)
- PRSB-to-UK Core mapping (overlaps with PRSB section)

#### 4. CQC Assessment for AI (higher-level summary)

**Key dimensions to cover:**
- **Mythbuster 109 assertions:** CQC regulates providers not tools; clinical responsibility non-delegable; record-keeping (Reg 17); AVT consent (display signage, privacy notices, opt-out); medical device classification; DCB0129/0160; DTAC pre-procurement; monitoring/audit; staff training
- **Five key questions (Single Assessment Framework):**
  - **Safe** - hazard log, risk management, clinician oversight, rollback, CSO sign-off, fallback, near-miss reporting, bias audits
  - **Effective** - clinical accuracy benchmarking, outcome monitoring vs pre-AI baseline, clinician review/sign-off, NICE alignment
  - **Caring** - patient awareness/consent, opt-out uptake, dignity during recording
  - **Responsive** - accessibility (accent, speech impairments), language coverage, equity audit, complaint routes
  - **Well-led** - board-level AI oversight, named accountable director, CSO role, audit trail, vendor management, risk register
- **CSO expectations** - registered clinician, DCB0129/0160 trained, maintains Clinical Safety Case and Hazard Log, signs off DCB0160 before go-live

**Prominent note:** Full CQC quality statements for AI are emerging (2025–26); mapping will need review when formal criteria published.

**Expected gaps flagged:**
- Board-level AI governance mechanism
- CSO capacity for AI oversight (separate from CSO sign-off)
- Patient complaint handling specific to AI outputs
- Equity of access auditing (language/accessibility)

#### 5. PSIRF (higher-level summary)

**Key dimensions to cover:**
- **Four PSIRF principles:** Compassionate engagement; Systems-based learning; Proportionate response; Supportive oversight
- **Key components:** Patient Safety Incident Response Policy; PSIRP (12–18 month forward plan); PSIRS; PSII (deepest response type)
- **Learning response types:** AAR, MDT Review, PSII, SEIPS-informed analysis, Swarm huddle, Thematic review, Horizon scanning
- **Engagement requirements:** Patients/families (early contact, named liaison, updates, draft review); Staff (psychological support, Just Culture); Community (thematic issues)
- **Board oversight:** Named executive lead, quarterly reports, PSIRP board sign-off, LFPSE integration
- **How PSIRF differs from old SI Framework:** systems thinking not individual RCA; proportionate not mandatory deep-dive; supportive oversight not transactional sign-off

**Overall position:** PSIRF complements DCB0129 Stage 7. Taxonomy captures incident occurrence (GV.SG-11 LFPSE, GV.SG-13 Near-Miss) but not the systems-learning response.

**Expected gaps flagged:**
- Systems-based root cause analysis readiness
- Compassionate engagement with affected patients/families
- Learning implementation tracking
- Board-level patient safety reporting on AI incidents

#### 6. PRSB Clinical Documentation Standards (higher-level summary)

**Key dimensions to cover:**
- **Main standards:** Core Information Standard (CIS); GP Connect Access Record; Outpatient Letter Standard; Discharge Summary Standard; Mental Health Inpatient Discharge; Emergency Care Discharge; Transfer of Care Around Medicines (ToCAM); About Me; End of Life Care; Maternity Record Standard; Palliative and End of Life Care
- **Common header set:** patient demographics + NHS Number; next of kin/carer; GP/care team; allergies/adverse reactions; medications; problems/diagnoses (SNOMED); procedures; investigations/results; observations/vital signs; social context; communication needs; consent/preferences; legal status; clinical narrative; safety netting
- **Narrative vs structured** - PRSB preserves narrative text as valuable; does not mandate full structurisation
- **Cardinality** - Mandatory / Required-if-known / Optional per data item
- **Royal College endorsement** - AoMRC, RCGP, RCP, etc.
- **Relationship to FHIR UK Core** - PRSB defines what, UK Core defines how

**Overall position:** The taxonomy has technical integration metrics (TP.WB-1 Write-back Fidelity, TP.WB-3 Field Mapping Accuracy) but no semantic-completeness metric for "does the AVT output include all PRSB-mandatory information elements." This is the clearest gap across all the new standards.

**Expected gaps flagged:**
- PRSB semantic completeness (mandatory information elements)
- Consultation record structure conformance (per PRSB profile)
- Professional narrative preservation (narrative vs over-structurisation trade-off)

#### 7. Caldicott Principles (higher-level summary)

**Key dimensions to cover:**
- Full wording of all 8 principles (2020 revision):
  1. Justify the purpose(s) for using confidential information
  2. Use confidential information only when it is necessary
  3. Use the minimum necessary confidential information
  4. Access on a strict need-to-know basis
  5. Everyone aware of their responsibilities
  6. Comply with the law
  7. The duty to share for individual care is as important as the duty to protect
  8. Inform patients and service users about how their information is used *(added 2020)*
- **Caldicott Guardian role** - senior person in every NHS org, UKCGC-trained, advises on IG decisions, represents confidentiality at board
- **Relationship to UK GDPR + Common Law Duty of Confidentiality** - three overlapping regimes; lawful basis doesn't automatically satisfy CLDC
- **National Data Guardian role** - statutory (HSC Act 2018); publishes guidance with "have regard to" obligation

**Overall position:** Caldicott is operationalised by DSPT (already mapped). This section makes the strategic governance layer explicit. Principle 8 (inform patients) maps directly to Verbal Notification Compliance (GV.CR-2) and Patient Dissent Recording (GV.CR-1).

**Expected gaps flagged:**
- Caldicott Guardian AI-specific engagement
- DPIA justification quality under Principle 1
- Minimum necessary data use documentation under Principle 3

### Part 2: Responsible AI Lens

#### A. DSIT AI Playbook - 10 Principles (content sketch)

For each principle, lens document will include:
- One-paragraph narrative explaining the principle and its AVT application
- Table of 5–15 metrics that operationalise aspects of the principle
- Note on which other principles the same metrics also serve (cross-tag)
- Gap note where coverage is thin

**Expected metric concentration:**
- P1 (limitations) - Summarisation/NLP hallucination/confabulation metrics, ASR error rates
- P2 (lawful/ethical) - Privacy & Data Governance, NHS Compliance groups
- P3 (security) - Security & Adversarial Robustness group
- P4 (human control) - Human Factors & Workflow (edit rate, review before signing, AI-off performance test)
- P5 (lifecycle) - Safety & Governance (drift detection, model version tracking)
- P6 (right tool) - Meta-evaluation (proximal/distal distinction), operational metrics
- P7 (openness) - Vendor Transparency, Sub-Processor Transparency, Model Change Notification
- P8 (commercial) - Vendor Transparency & Contractual group
- P9 (skills) - Training & Competency group
- P10 (org assurance) - Safety & Governance (Clinical Safety Case), NHS Compliance

#### B. Six Ethical Themes (content sketch)

For each theme, lens document will include:
- Canonical wording + scope
- Connection to White Paper (themes 1–5) or Playbook addition (theme 6)
- Table of metrics serving this theme
- Note on trade-offs with other themes (Playbook acknowledges tension)

**Expected metric concentration:**
- T1 (Safety, Security and Robustness) - Part A content fidelity + Part E Safety & Security groups
- T2 (Transparency and Explainability) - ASR Confidence Exposure, Uncertainty Marker Preservation, Linked Evidence/Provenance Tracing, Vendor Transparency metrics
- T3 (Fairness) - Demographic Equity Disaggregation family, Fairness & Equity group
- T4 (Accountability and Governance) - NHS Compliance & Regulatory, Safety & Governance groups
- T5 (Contestability and Redress) - Patient Opt-Out Rate, Time-to-Correct, Incident Disclosure, Verification Burden
- T6 (Societal Wellbeing) - Environmental & Sustainability, Clinical Documentation Skill Attenuation, Chilling Effect Assessment, Therapeutic Relationship Impact, Deployment Equity Index

#### C. Coverage Matrix

A table highlighting metrics that cross-cut multiple principles/themes (the "policy-lever" metrics that a single measurement supports multiple assurance goals). Example format:

| Metric | Playbook Principles | Ethical Themes | Why cross-cutting |
|--------|--------------------|-----------------|--------------------|
| TP.SN-5 Hallucination Rate | P1, P4, P5 | T1, T2 | Fundamental content integrity + transparency of limitations |

#### D. Gaps

Areas where neither taxonomy metrics nor standards coverage clearly addresses a principle/theme. Cross-reference to Part 1 "Proposed New Metrics" where the same gap surfaces from multiple angles.

---

## Critical files

- **Modify:** [taxonomy/_standards-mapping.md](taxonomy/_standards-mapping.md) - 7 new standards + Proposed New Metrics section + Gap Summary update
- **Create:** `taxonomy/_responsible-ai-lens.md` - new cross-cutting lens document
- **Modify:** [taxonomy/build.py](taxonomy/build.py) - add new file to build order
- **Modify:** [taxonomy/_contents.md](taxonomy/_contents.md) - add lens document to cross-cutting list
- **Modify:** [CHANGELOG.md](CHANGELOG.md) - v3.1 entry

---

## Execution order (subtasks for separate commits)

Each subtask is a logical commit unit. The 7 standards can be grouped where they naturally share content (e.g., FHIR UK Core + PRSB have overlap; Caldicott is small).

### Subtask 1: Three assertion-level standards (MHRA + NICE ESF + FHIR UK Core)

- [ ] **MHRA SaMD/AIaMD section**
  - [ ] Intro: publisher, scope, mandatory status, AVT relevance
  - [ ] Classification (WP1, WP2) sub-section
  - [ ] Premarket (WP3) sub-section
  - [ ] Post-Market Surveillance (WP4 + SI 2024 No. 1368) sub-section
  - [ ] Cybersecurity (WP5) sub-section
  - [ ] AI RIG (WP9) sub-section
  - [ ] Glass Box / Interpretability (WP10) sub-section
  - [ ] Ship of Theseus / Adaptivity (WP11) sub-section
  - [ ] Transparency Guiding Principles (June 2024) - WHO/WHY/WHAT/WHERE/WHEN/HOW
  - [ ] GMLP 10 principles (Oct 2021)
  - [ ] Gaps + Taxonomy extends blocks
- [ ] **NICE Evidence Standards Framework section**
  - [ ] Intro + Tier A/B/C classification explanation
  - [ ] Standards 1–9 Design Factors table
  - [ ] Standards 10–13 Describing Value table
  - [ ] Standards 14–16 Demonstrating Performance (including AI-specific provisions)
  - [ ] Standards 17–18 Delivering Value
  - [ ] Standards 19–21 Deployment
  - [ ] Gaps + Taxonomy extends blocks
- [ ] **FHIR UK Core / INTEROPen section**
  - [ ] Intro: governance, relationship to CareConnect
  - [ ] STU1 / STU2 / STU3 release status table
  - [ ] Per-profile conformance table (assertion-level)
  - [ ] UK-specific extensions table
  - [ ] Refinement note for TP.WB-6 and TP.WB-7
  - [ ] Gaps block
- [ ] **Verification**
  - [ ] `python taxonomy/build.py` runs cleanly
  - [ ] Metric count unchanged (214)
  - [ ] No garbled characters
  - [ ] All referenced metric names exist in assembled taxonomy
- [ ] Commit: `🦞 add MHRA, NICE ESF, and FHIR UK Core to standards mapping`

### Subtask 2: Four higher-level summary standards (CQC + PSIRF + PRSB + Caldicott)

- [ ] **CQC Assessment for AI section**
  - [ ] Intro + "emerging (2025–26)" status flag
  - [ ] GP Mythbuster 109 assertions summary
  - [ ] Five Key Questions coverage (Safe / Effective / Caring / Responsive / Well-led)
  - [ ] CSO expectations
  - [ ] Overall position + gaps flagged
- [ ] **PSIRF section**
  - [ ] Intro: mandatory status, AVT relevance
  - [ ] Four PSIRF principles
  - [ ] Key components (PSIRP, PSIRS, PSII)
  - [ ] Learning response types (AAR, PSII, SEIPS, etc.)
  - [ ] Engagement + board oversight requirements
  - [ ] How PSIRF differs from SI Framework
  - [ ] Overall position + gaps flagged
- [ ] **PRSB Clinical Documentation Standards section**
  - [ ] Intro + Royal College endorsement context
  - [ ] Main PRSB standards list
  - [ ] Common header set
  - [ ] Narrative vs structured trade-off
  - [ ] Cardinality (Mandatory / Required-if-known / Optional)
  - [ ] Relationship to FHIR UK Core
  - [ ] Overall position + gaps flagged
- [ ] **Caldicott Principles section**
  - [ ] Intro: 2020 revision context
  - [ ] Full wording of all 8 principles
  - [ ] Caldicott Guardian role
  - [ ] Relationship to UK GDPR + Common Law Duty of Confidentiality
  - [ ] National Data Guardian role
  - [ ] Overall position + gaps flagged
- [ ] **Verification**
  - [ ] `python taxonomy/build.py` runs cleanly
  - [ ] All referenced metric names exist in assembled taxonomy
- [ ] Commit: `🦞 add CQC, PSIRF, PRSB, and Caldicott Principles to standards mapping`

### Subtask 3: Consolidate gap analysis in `_standards-mapping.md`

- [ ] Update existing Gap Summary table with rows for the 7 new standards
- [ ] Add "Proposed New Metrics (Not Yet Implemented)" top-level section after Gap Summary
- [ ] For each proposed metric: reference ID slot, name, description, source standard, tier rationale
  - [ ] MHRA gap candidates (~5 proposed metrics)
  - [ ] NICE ESF gap candidates (~5 proposed metrics: cost-effectiveness, budget impact, silent mode, tier classification, subgroup drift)
  - [ ] FHIR UK Core gap candidates (~3 proposed metrics)
  - [ ] CQC gap candidates (~4 proposed metrics)
  - [ ] PSIRF gap candidates (~4 proposed metrics: systems RCA, compassionate engagement, learning tracking, board reporting)
  - [ ] PRSB gap candidates (~3 proposed metrics: semantic completeness, profile conformance, narrative preservation)
  - [ ] Caldicott gap candidates (~3 proposed metrics)
- [ ] Aim for ~25–30 total candidates across all 7 standards
- [ ] Commit: `🦞 consolidate standards mapping gaps and propose new metrics`

### Subtask 4: Create Responsible AI Lens document

- [ ] Create `taxonomy/_responsible-ai-lens.md` with top-level intro
  - [ ] Explain lens approach vs standards mapping
  - [ ] Relationship to NHS LLM Evaluation Framework three groups
  - [ ] Playbook trade-offs acknowledgement
- [ ] **Part A: DSIT AI Playbook 10 Principles**
  - [ ] Principle 1 (limitations) - narrative + metrics table
  - [ ] Principle 2 (lawful/ethical) - narrative + metrics table
  - [ ] Principle 3 (security) - narrative + metrics table
  - [ ] Principle 4 (human control) - narrative + metrics table
  - [ ] Principle 5 (lifecycle) - narrative + metrics table
  - [ ] Principle 6 (right tool) - narrative + metrics table
  - [ ] Principle 7 (openness / ATRS) - narrative + metrics table
  - [ ] Principle 8 (commercial) - narrative + metrics table
  - [ ] Principle 9 (skills) - narrative + metrics table
  - [ ] Principle 10 (org assurance) - narrative + metrics table
- [ ] **Part B: Six Ethical Themes**
  - [ ] Theme 1 (Safety, Security and Robustness) - narrative + metrics table + trade-offs note
  - [ ] Theme 2 (Transparency and Explainability) - narrative + metrics table + trade-offs note
  - [ ] Theme 3 (Fairness) - narrative + metrics table + trade-offs note
  - [ ] Theme 4 (Accountability and Governance) - narrative + metrics table + trade-offs note
  - [ ] Theme 5 (Contestability and Redress) - narrative + metrics table + trade-offs note
  - [ ] Theme 6 (Societal Wellbeing) - narrative + metrics table + trade-offs note
- [ ] Add `_responsible-ai-lens.md` to `build.py` FILES list (after `_standards-mapping.md`)
- [ ] Add entry to `_contents.md` cross-cutting section
- [ ] **Verification**
  - [ ] `python taxonomy/build.py` runs cleanly from 28 files
  - [ ] All referenced metric names exist in assembled taxonomy
  - [ ] No garbled characters
- [ ] Commit: `🦞 add Responsible AI lens (DSIT Playbook principles + 6 ethical themes)`

### Subtask 5: Cross-cutting coverage matrix + gaps in lens document

- [ ] **Part C: Coverage Matrix**
  - [ ] Identify ~15–25 cross-cutting "policy-lever" metrics
  - [ ] Table: Metric | Playbook Principles | Ethical Themes | Why cross-cutting
  - [ ] Narrative explaining the cross-cutting pattern
- [ ] **Part D: Gaps**
  - [ ] List gaps where neither taxonomy nor standards coverage addresses a principle/theme
  - [ ] Cross-reference to Proposed New Metrics in `_standards-mapping.md`
  - [ ] Flag Societal Wellbeing-specific gaps (likely highest concentration)
- [ ] **Verification**
  - [ ] Build runs cleanly
  - [ ] Cross-references between lens doc and standards mapping are valid
- [ ] Commit: `🦞 add coverage matrix and gap analysis to Responsible AI lens`

### Subtask 6: Verify and update CHANGELOG

- [ ] **Final verification pass**
  - [ ] `python taxonomy/build.py` runs cleanly from 28 files
  - [ ] Metric count unchanged at 214 (`grep -c '^### [A-Z][A-Z]\.' avt-metrics-taxonomy.md`)
  - [ ] Tier counts unchanged: 43 Tier 1 / 92 Tier 2 / 79 Tier 3
  - [ ] No broken metric references (all referenced names match assembled taxonomy)
  - [ ] No garbled characters (`grep -c '�' avt-metrics-taxonomy.md` → 0)
  - [ ] Existing four mappings unchanged (DTAC, DSPT, DCB0129/0160, NHS LLM Framework)
  - [ ] Existing `_applicability.md` unchanged
- [ ] **Update CHANGELOG.md**
  - [ ] Add v3.1 section at top (above v3.0)
  - [ ] List 7 new standards mapped
  - [ ] List Responsible AI lens document addition
  - [ ] Note ~25–30 proposed new metrics flagged (not implemented)
  - [ ] Note no changes to existing 214 metrics
- [ ] Commit: `🦞 add CHANGELOG v3.1 entry for extended standards mapping and responsible AI lens`

---

## Verification

- `python taxonomy/build.py` runs cleanly from 28 files (was 27)
- Metric count unchanged at 214 (grep `^### [A-Z][A-Z]\.` → 214)
- Tier counts unchanged (43/92/79)
- No metric reference IDs changed (spot check: TP.AC-1, GV.CR-1, ES.ME-1 unchanged)
- All 7 new standards have their own section in `_standards-mapping.md`
- `_responsible-ai-lens.md` covers all 10 Playbook principles + all 6 ethical themes
- Every metric referenced in new mapping tables matches a metric in the assembled taxonomy
- No garbled characters (`grep -c '�' avt-metrics-taxonomy.md` → 0)
- CHANGELOG updated with v3.1 entry covering both parts
- Existing four mappings unchanged (DTAC, DSPT, DCB0129/0160, NHS LLM Framework)
- Existing `_applicability.md` unchanged

---

## Expected scope

- Lines added to `_standards-mapping.md`: ~400–500 (current file ~330 lines)
- Lines in new `_responsible-ai-lens.md`: ~350–450
- New sections in `_standards-mapping.md`: 7 standards + 1 "Proposed New Metrics" section + Gap Summary update
- Sections in `_responsible-ai-lens.md`: 10 principles + 6 themes + coverage matrix + gaps (Parts A–D)
- Proposed new metrics flagged: ~25–30 candidates (in `_standards-mapping.md`)
- Commits: 6 (one per subtask)
- Build time: unchanged (Python string concatenation scales linearly)
