# Changelog

## v3.1 (unreleased)

### Extended Standards Mapping

Added assertion-level or higher-level mapping for seven additional NHS/UK standards. Mapping only — no new metrics added to taxonomy; gaps flagged for future consideration.

**Assertion-level (formal standards):**
- **MHRA SaMD / AIaMD** — Change Programme workstreams (WP1–WP11), SI 2024 No. 1368 Post-Market Surveillance (in force June 2025), Transparency Guiding Principles (June 2024), GMLP 10 principles (Oct 2021)
- **NICE Evidence Standards Framework for DHTs (ECD7)** — all 21 numbered standards across 5 lifecycle areas, Tier A/B/C classification, AI-specific provisions (Standards 4, 5, 6, 15, 16)
- **FHIR UK Core / INTEROPen** — STU1/STU2/STU3 release status, per-profile conformance, UK-specific extensions (NHS Number verification, Ethnic Category, etc.), refinement of TP.WB-6 to mean UK Core not generic FHIR R4

**Higher-level summary:**
- **CQC Assessment for AI** — GP Mythbuster 109 baseline assertions, Five Key Questions (Safe/Effective/Caring/Responsive/Well-led), CSO expectations (flagged as emerging 2025–26)
- **Patient Safety Incident Response Framework (PSIRF)** — four PSIRF principles, response types (AAR, PSII, SEIPS), engagement and board oversight requirements
- **PRSB Clinical Documentation Standards** — Core Information Standard, Outpatient Letter, Discharge, etc.; common header set; narrative vs structured trade-off; relationship to FHIR UK Core
- **Caldicott Principles (2020 revision)** — all 8 principles with direct metric mapping (Principle 8 maps directly to existing GV.CR-1/2/3), Caldicott Guardian role, NDG statutory context

### Proposed New Metrics (Not Yet Implemented)

28 candidate metrics flagged across the 7 new standards to close identified gaps:
- 5 from MHRA (classification, PCCP, PMS reports, transparency, training data)
- 5 from NICE ESF (tier classification, silent mode, subgroup drift, cost-effectiveness, budget impact)
- 3 from FHIR UK Core (per-resource conformance, UK extensions, STU version targeting)
- 4 from CQC (board governance, CSO capacity, AI complaints, Reg 17 record quality)
- 4 from PSIRF (SEIPS analysis, compassionate engagement, Just Culture, learning tracking)
- 4 from PRSB (semantic completeness, narrative preservation, AIS capture, legal status)
- 3 from Caldicott (DPIA justification, consultation appropriateness, per-item necessity)

Distribution: 6 × Tier 1, 19 × Tier 2, 3 × Tier 3. Highest-leverage addition: **TP.WB-11 PRSB Semantic Completeness** (appears as gap across multiple standards).

### New Responsible AI Lens Document

New cross-cutting file `taxonomy/_responsible-ai-lens.md` providing a policy-intent view of the taxonomy complementary to standards mapping and applicability classification.

**Part A: DSIT AI Playbook for the UK Government (Feb 2025) — 10 principles:**
- P1 (Know AI and its limitations), P2 (Lawful/ethical), P3 (Security), P4 (Meaningful human control), P5 (Lifecycle management), P6 (Right tool for the job), P7 (Open and collaborative), P8 (Commercial colleagues), P9 (Skills and expertise), P10 (Organisation policies and assurance)
- Each principle has narrative + metric table + gap notes

**Part B: Six Responsible AI Ethical Themes** (AI Regulation White Paper five + Playbook-added sixth):
- T1 (Safety, Security and Robustness), T2 (Transparency and Explainability), T3 (Fairness), T4 (Accountability and Governance), T5 (Contestability and Redress), T6 (Societal Wellbeing and Public Good)
- Each theme has narrative + metric table + trade-off notes

**Part C: Coverage Matrix** — 25 policy-lever metrics that cross-cut 3+ principles/themes simultaneously. Five "megas" cross 5–6 axes: GV.SG-11 (Adverse Event/LFPSE), GV.VT-4 (Audit Trail), GV.CR-3 (AI Content Labelling), HL.HF-1 (Edit Rate), IO.PX-1 (Patient Opt-Out).

**Part D: Gaps** — 20 principle-level + 18 theme-level gaps identified; cross-referenced to Proposed New Metrics. Societal Wellbeing (T6) has highest gap concentration; P6 (Right tool) and P7 (Openness) weakest principles.

### Build

- `build.py` now assembles from 28 files (was 27) — added `_responsible-ai-lens.md`
- All 214 metric reference IDs preserved; no existing metrics changed
- Tier counts unchanged: 43 Tier 1 / 92 Tier 2 / 79 Tier 3
- All metric references in new sections validated against assembled taxonomy

---

## v3.0 (unreleased)

### Reference IDs
- Every metric now carries a unique reference ID in the format `{Part}.{Group}-{Number}` (e.g. `TP.AC-1`, `GV.CR-7`)
- IDs appear in both the metric heading and the dimensions table
- Part abbreviations: TP (Technical Pipeline), PI (Pipeline Interactions), HL (Human Layer), IO (Impact & Outcomes), GV (System Governance), ES (Evaluation Science)
- 20 group abbreviations documented in the Reference IDs section of How to Use
- Reference key legend added to How to Use section

### Applicability Classification
- New cross-cutting section classifying all 214 metrics by applicability:
  - **AVT-Specific** (48 metrics, 22%) — meaningful only with the audio pipeline
  - **AVT-Contextualised** (77 metrics, 36%) — general concept, AVT-tuned definition
  - **General Healthcare AI** (89 metrics, 42%) — applicable to any clinical AI system
- Summary and per-part breakdown tables included
- Full per-metric classification table with reference IDs

### New Metric Families
- **Medication Safety Thread** (4 metrics: TP.SN-19, TP.SN-21, TP.CC-5, IO.PX-10) — cross-cutting family tracking medication accuracy from summarisation through coding to patient outcomes
- **Demographic Equity Disaggregation** (7 metrics: TP.ASR-4, TP.ASR-5, TP.CC-9, PI.E2E-5, IO.FE-2, IO.FE-4, IO.FE-5) — cross-cutting family applying demographic disaggregation across pipeline layers

### New Sub-clusters
- **Write-back Safety** (4 metrics: TP.WB-1 through TP.WB-4) — the four Tier 1 pre-deployment gates at the EPR integration boundary
- **Coding Fidelity** (7 metrics: TP.CC-1 through TP.CC-6 plus TP.CC-11) — accuracy of individual code assignment across NHS terminology systems

### Standards Mapping
- New cross-cutting section with assertion-level mapping to four NHS/regulatory frameworks:
  - **DTAC v2.0** — all 5 sections (C1 Clinical Safety, C2 Data Protection, C3 Technical Security, C4 Interoperability, D1 Usability)
  - **DSPT v8** — all 10 National Data Guardian standards with individual assertion mapping
  - **DCB0129/DCB0160** — all 7 clinical safety lifecycle stages
  - **NHS England LLM Evaluation & Monitoring Framework v0.2.2** — all 30 dimensions across 3 groups (flagged as draft)
- Gap summary identifying 9 areas where standards require coverage the taxonomy doesn't provide
- Coverage summary identifying 8 areas where the taxonomy extends beyond all standards

### Count Corrections
- Tier breakdown corrected from 42/87/85 to **43/92/79** (Tier 1/Tier 2/Tier 3) in Summary and How to Use
- Human Factors & Workflow metric count corrected from 20 to **19** in Contents
- EPR Write-back tier breakdown corrected from "4 Tier 1 · 1 Tier 2" to **4 Tier 1 · 2 Tier 2 · 1 Tier 3**
- Clinical Coding tier breakdown corrected from "2 Tier 2 · 2 Tier 3" to **1 Tier 1 · 8 Tier 2 · 3 Tier 3**

### Build
- `build.py` now assembles from 27 files (was 25) — added `_applicability.md` and `_standards-mapping.md`
- Family count: 6 (was 4)
- Sub-cluster count: 6 (was 4)
- Unaffiliated metrics: 189 (was 200)

---

## v2.0

- 214 metrics across 20 groups (was 151 metrics across 18 groups in v1)
- 63 new metrics added in batches 1-4
- 2 new groups: NHS Compliance & Regulatory, Environmental & Sustainability
- 4 named metric families: Clinical Content Fidelity, Post-Generation Correction, Clinical Transcription Accuracy, Reference-Based Text Similarity
- 4 sub-clusters: Conversation Analysis, Sociotechnical & Resilience, Patient Clinical Outcomes, Longitudinal Drift & Model Contamination
- 15 underspecification warnings across Tiers A/B/C
- Tier 1 Quick Reference section organised by responsible actor

## v1.0

- Initial release: 151 metrics across 18 groups
- Modular file structure with `build.py` assembler
- Monolithic source split into `taxonomy/` directory
