# Glossary

Quick reference for terms, abbreviations, and standards referenced throughout the taxonomy. Each entry gives a one-line gloss and - where applicable - a link to the authoritative source and the metric(s) or standards that reference it.

## Pipeline and technical terms

- **AVT** - Ambient Voice Technology. Generic term for AI systems that listen to a consultation and produce clinical documentation, typically comprising audio capture → ASR → diarisation → summarisation → clinical coding → downstream write-back. (v4.0 reframed "EPR write-back" as "Downstream Write-back" to reflect that targets include GP clinical systems, e-prescribing, FHIR endpoints, and patient portals.)
- **ASR** - Automatic Speech Recognition. The pipeline stage that converts speech audio to text (transcript).
- **Diarisation** - Speaker attribution. Determining who spoke which segment of the transcript (clinician, patient, bystander).
- **EPR** - Electronic Patient Record. Used synonymously with EHR (Electronic Health Record) in this taxonomy.
- **LLM** - Large Language Model. Statistical model used for summarisation and coding in most current AVT products.
- **SaMD** - Software as a Medical Device. MHRA regulatory classification.
- **AIaMD** - AI as a Medical Device. Subclass of SaMD covering adaptive and learning systems.
- **SNR** - Signal-to-Noise Ratio. See `TP.AC-1`.
- **VAD** - Voice Activity Detection. See `TP.AC-2`.
- **WER** - Word Error Rate. ASR accuracy metric. See `TP.ASR-1`.
- **M-WER** - Medical WER. Clinical-vocabulary-weighted WER. See `TP.ASR-2`.
- **CK-ER** - Clinical Keyword Error Rate. See `TP.ASR-3`.
- **CER** - Character Error Rate. See `TP.ASR-8`.
- **OOV** - Out-of-Vocabulary. See `TP.ASR-9`.
- **RTF** - Real-Time Factor. Processing speed metric. See `TP.ASR-7`.
- **DER** - Diarisation Error Rate. See `TP.DI-1`.
- **HEWER** - Holistic Error-Weighted Error Rate. Diarisation-aware variant. See `TP.DI-8`.
- **cpHEWER** - Clinical-Perspective HEWER.
- **ROUGE** - Recall-Oriented Understudy for Gisting Evaluation. Summarisation text-similarity metric. See `TP.SN-1`.
- **BERTScore** - Neural-embedding-based text similarity metric. See `TP.SN-2`.
- **PDSQI-9** - Physician Documentation Quality Instrument, 9 items. See `TP.SN-3`.
- **CREOLA** - Clinical Record Error Ontology and Labelling Architecture. See `TP.SN-4`.

## Standards and regulatory

- **DTAC** - Digital Technology Assessment Criteria (NHS England). The pre-procurement digital assurance framework.
- **DSPT** - Data Security and Protection Toolkit (NHS Digital). Annual data-security self-assessment.
- **DCB0129** - Clinical Risk Management: Manufacturer. Mandatory for health IT system manufacturers.
- **DCB0160** - Clinical Risk Management: Healthcare Organisation. Deployer-side counterpart to DCB0129.
- **NHS LLM Eval Framework** - NHS England's Large Language Model Evaluation and Monitoring Framework.
- **MHRA** - Medicines and Healthcare products Regulatory Agency.
- **NICE ESF** - National Institute for Health and Care Excellence, Evidence Standards Framework for Digital Health Technologies (ECD7).
- **FHIR UK Core** - HL7 Fast Healthcare Interoperability Resources, UK Core profile (INTEROPen / NHS Digital).
- **CQC** - Care Quality Commission. The primary healthcare regulator in England.
- **PSIRF** - Patient Safety Incident Response Framework (NHS England, 2022→).
- **PRSB** - Professional Record Standards Body.
- **Caldicott Principles** - Eight principles governing the use of confidential patient information (NDG, 2020 revision).
- **UK GDPR** - UK General Data Protection Regulation.
- **DPIA** - Data Protection Impact Assessment.
- **DSPA** - Data Sharing and Processing Agreement.
- **DCB** - Data Coordination Board (NHS Digital).
- **NDG** - National Data Guardian.
- **ICO** - Information Commissioner's Office.
- **SAR** - Subject Access Request (UK GDPR Article 15).

## Policy and governance

- **DSIT AI Playbook** - Department for Science, Innovation and Technology, *AI Playbook for the UK Government* (Feb 2025). Source of the 10 Playbook principles mapped in the Responsible AI lens.
- **ICB** - Integrated Care Board.
- **LFPSE** - Learn from Patient Safety Events (NHS England national reporting system).
- **NAS** - National Assurance Service (NHS England Chief Safety Officer; publishes AVT Day Zero SPIs).
- **SPI** - Safety Performance Indicator.
- **DSCMS** - Digital Safety Clinical Monitoring Scheme (NHS England).
- **CSO** - Clinical Safety Officer (DCB0129/0160 role).
- **SIRO** - Senior Information Risk Officer.
- **CIO / CCIO** - Chief Information Officer / Chief Clinical Information Officer.
- **DPO** - Data Protection Officer.
- **AIS** - Accessible Information Standard (NHS).
- **ATRS** - Algorithmic Transparency Recording Standard (UK government).
- **AVT Self-Certified Supplier Registry** - NHS England registry of AVT suppliers self-certifying compliance with the Day Zero requirements; the FTS notice 069369-2025 anchored its publicly-visible procurement surface, and v5.3.0 / v5.4.0 mapped it as the 13th framework in the standards-mapping. Registry-direct obligations drove the v5.x Phase 5 minimum-set extension.
- **FTS** - Find a Tender Service (UK government). Public-tender publication mechanism; FTS notice 069369-2025 is the AVT Self-Certified Supplier Registry tender. (Cited because it provides the publicly-readable ceiling on what the Registry actually requires — the granular Atamis application pack remains inaccessible without supplier credentials.)
- **NHSE IG Guidance March 2026** - NHS England Information Governance guidance on ambient scribing. The March 2026 update introduced new transparency, dissent-handling, privacy-notice, SAR-handling, and right-to-restrict requirements that drove several v5.3.0 / v5.4.0 metric promotions and mints. Cited via the `[NHSE-IG-Guidance-2026-03]` catalogue handle. Per the v5.5.0 topic-cited convention, source rows reference the substantive obligation rather than fabricating section numbers, since the parent guidance hub doesn't currently expose stable per-section URL anchors.

## Taxonomy-specific

- **Metric family** - A named parent-construct grouping of related metrics (e.g. *Clinical Content Fidelity*) that may span multiple groups. The eight families as of v5.4.0: Clinical Content Fidelity, Reference-Based Text Similarity, Clinical Transcription Accuracy, Post-Generation Correction, Medication Safety Thread, Demographic Equity Disaggregation, NHSE IG Attestation, and PRSB Semantic Completeness & Write-back Fidelity. Family framings live on the canonical `_families.md` page since v5.5.0; `Family` is an audit-enforced per-metric dimension since v5.4.0.
- **Sub-cluster** - A thematic grouping of metrics within a single group. Sub-clusters have italic introductory text before the first member.
- **Reference ID** - Format `{Cluster}.{Group}-{Number}` (e.g. `TP.AC-1`). Stable across versions; cite as `TP.AC-1` → `/groups/audio-capture/#tp-ac-1`. Retired IDs are recorded in `_retired-ids.md` and never reused (v3.7+ deprecate-don't-renumber convention).
- **Cluster** - Six top-level groupings: TP (Technical Pipeline), PI (Pipeline Interactions), HL (Human Layer), IO (Impact & Outcomes), GV (System Governance), ES (Evaluation Science). The cluster-code naming surface canonical since v4.0.
- **Tier 1 / 2 / 3** - Priority classification: Tier 1 is minimum viable assurance (measurable today, every deployer must do it); Tier 2 is recommended; Tier 3 is advanced/research-grade.
- **Cadence** - Multi-valued since v5.1.0. Each value drawn from a four-element enum: `One-off gate` (pre-deployment), `Periodic audit` (scheduled review), `Continuous` (always-on monitoring), `Event-triggered` (re-measured on a material change event such as a model update, contract renewal, or new failure mode).
- **Responsible Actor** - Who is accountable for measuring: *Vendor*, *Deployer*, *Clinician*, *Regional (ICB)*, or *National Body*. Multi-valued.
- **Applicability** - Three-way classification per metric: *AVT-Specific* (50 metrics), *AVT-Contextualised* (79), or *General Healthcare AI* (107).
- **Layer of Defence** - Per-metric explicit dimension since v5.4.0 (extended to all 236 metrics in v5.5.4). One of *Prevention* (pre-deployment gates), *Detection* (continuous monitoring), or *Limitation* (governance infrastructure that bounds damage when detection fires). Documented in `_layers-of-defence.md`. The catalogue distribution is honestly thin on Limitation (25 metrics, 11%), which surfaces a real architectural gap.
- **AI-Substrate** - Five-class derived classification since v5.5.3: *Pre-AI* (microphone hardware, signal capture), *AI-Substrate* (the model itself), *Post-AI* (write-back, EPR integration), *AI-Mediated Workflow* (clinician edits, automation bias), *AI-Agnostic Governance* (DPIA, board oversight, sub-processor disclosure). Derived at build time from cluster + per-metric overrides; documented in `_ai-substrate.md`.
- **Failure Pathway** - Worked failure-mode archetype showing how an error propagates through the pipeline and which Tier 1 metrics catch it where. Three pathways named (hallucination cascade, silent write-back failure, undisclosed model update) plus a day-by-day worked timeline of one closed governance loop. Documented in `_failure-pathways.md` since v5.5.1.
- **Outcomes Boundary** - First-class principle (v3.3+) naming what is *out of scope* for this taxonomy: clinical-outcome validation belongs to national research bodies, not deployers. Operationalised by ES.ME-8 (Outcome Evidence Commitment Status) and ES.ME-9 (Causal Model Operationalisation).
- **Calibration & Context principle** - First-class principle (v3.7+) naming what is *in scope but context-dependent*: tier assignments and threshold numbers are deployer-calibrated starting points against six named deployment-setting axes (specialty mix, patient population, platform maturity, governance capacity, risk appetite, volume), not universal gates.
- **Maturity** - Four-value enum: *Established*, *Emerging*, *Vendor-Proprietary*, *Proposed / Novel*. Distinct from Tier — a Tier 1 metric can be Proposed/Novel if a regulatory obligation names it but the measurement science isn't yet settled (e.g. GV.CR-13 Refusal Impact-Explanation Quality awaiting a piloted national rubric).
- **Underspecification warning** - Explicit flag on a metric where the measurement science does not yet have consensus. Readers should treat these as calls for caution. Three tiers: A (no established methodology), B (concept defined, no AVT-specific validation), C (technically defined, clinical validity unproven or disproven).
- **Outcome Type** - Two-value enum: *Proximal* (what's happening in the AVT pipeline now) or *Distal* (downstream patient outcome). Bounds Outcomes-Boundary applicability.
- **Tightening pattern** - Tier 1 metric structure introduced in v3.4+ with the **Reference Standard** + **Operational Specification** + **Trigger Conditions** sub-blocks. Numerical thresholds live in `docs/thresholds.md` since v5.0.0 (was: inline in metric bodies). The pattern carries explicit ⚠️ Provenance preludes distinguishing externally-cited thresholds from proposed-as-starting-points.
- **Provenance prelude** - The ⚠️ paragraph at the top of a Trigger Conditions block (or threshold table) naming where each numerical threshold comes from. Honest about author judgement vs cited source; required for Tier 1 metrics with the tightening pattern.

*This glossary is a convenience only; the authoritative source for any term is the standards document or the metric entry itself.*
