# Changelog

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
