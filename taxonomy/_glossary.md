# Glossary

Quick reference for terms, abbreviations, and standards referenced throughout the taxonomy. Each entry gives a one-line gloss and — where applicable — a link to the authoritative source and the metric(s) or standards that reference it.

## Pipeline and technical terms

- **AVT** — Ambient Voice Technology. Generic term for AI systems that listen to a consultation and produce clinical documentation, typically comprising audio capture → ASR → diarisation → summarisation → EPR write-back.
- **ASR** — Automatic Speech Recognition. The pipeline stage that converts speech audio to text (transcript).
- **Diarisation** — Speaker attribution. Determining who spoke which segment of the transcript (clinician, patient, bystander).
- **EPR** — Electronic Patient Record. Used synonymously with EHR (Electronic Health Record) in this taxonomy.
- **LLM** — Large Language Model. Statistical model used for summarisation and coding in most current AVT products.
- **SaMD** — Software as a Medical Device. MHRA regulatory classification.
- **AIaMD** — AI as a Medical Device. Subclass of SaMD covering adaptive and learning systems.
- **SNR** — Signal-to-Noise Ratio. See `TP.AC-1`.
- **VAD** — Voice Activity Detection. See `TP.AC-2`.
- **WER** — Word Error Rate. ASR accuracy metric. See `TP.ASR-1`.
- **M-WER** — Medical WER. Clinical-vocabulary-weighted WER. See `TP.ASR-2`.
- **CK-ER** — Clinical Keyword Error Rate. See `TP.ASR-3`.
- **CER** — Character Error Rate. See `TP.ASR-8`.
- **OOV** — Out-of-Vocabulary. See `TP.ASR-9`.
- **RTF** — Real-Time Factor. Processing speed metric. See `TP.ASR-7`.
- **DER** — Diarisation Error Rate. See `TP.DI-1`.
- **HEWER** — Holistic Error-Weighted Error Rate. Diarisation-aware variant. See `TP.DI-8`.
- **cpHEWER** — Clinical-Perspective HEWER.
- **ROUGE** — Recall-Oriented Understudy for Gisting Evaluation. Summarisation text-similarity metric. See `TP.SN-1`.
- **BERTScore** — Neural-embedding-based text similarity metric. See `TP.SN-2`.
- **PDSQI-9** — Physician Documentation Quality Instrument, 9 items. See `TP.SN-3`.
- **CREOLA** — Clinical Record Error Ontology and Labelling Architecture. See `TP.SN-4`.

## Standards and regulatory

- **DTAC** — Digital Technology Assessment Criteria (NHS England). The pre-procurement digital assurance framework.
- **DSPT** — Data Security and Protection Toolkit (NHS Digital). Annual data-security self-assessment.
- **DCB0129** — Clinical Risk Management: Manufacturer. Mandatory for health IT system manufacturers.
- **DCB0160** — Clinical Risk Management: Healthcare Organisation. Deployer-side counterpart to DCB0129.
- **NHS LLM Eval Framework** — NHS England's Large Language Model Evaluation and Monitoring Framework.
- **MHRA** — Medicines and Healthcare products Regulatory Agency.
- **NICE ESF** — National Institute for Health and Care Excellence, Evidence Standards Framework for Digital Health Technologies (ECD7).
- **FHIR UK Core** — HL7 Fast Healthcare Interoperability Resources, UK Core profile (INTEROPen / NHS Digital).
- **CQC** — Care Quality Commission. The primary healthcare regulator in England.
- **PSIRF** — Patient Safety Incident Response Framework (NHS England, 2022→).
- **PRSB** — Professional Record Standards Body.
- **Caldicott Principles** — Eight principles governing the use of confidential patient information (NDG, 2020 revision).
- **UK GDPR** — UK General Data Protection Regulation.
- **DPIA** — Data Protection Impact Assessment.
- **DSPA** — Data Sharing and Processing Agreement.
- **DCB** — Data Coordination Board (NHS Digital).
- **NDG** — National Data Guardian.
- **ICO** — Information Commissioner's Office.
- **SAR** — Subject Access Request (UK GDPR Article 15).

## Policy and governance

- **DSIT AI Playbook** — Department for Science, Innovation and Technology, *AI Playbook for the UK Government* (Feb 2025). Source of the 10 Playbook principles mapped in the Responsible AI lens.
- **ICB** — Integrated Care Board.
- **LFPSE** — Learn from Patient Safety Events (NHS England national reporting system).
- **NAS** — National Assurance Service (NHS England Chief Safety Officer; publishes AVT Day Zero SPIs).
- **SPI** — Safety Performance Indicator.
- **DSCMS** — Digital Safety Clinical Monitoring Scheme (NHS England).
- **CSO** — Clinical Safety Officer (DCB0129/0160 role).
- **SIRO** — Senior Information Risk Officer.
- **CIO / CCIO** — Chief Information Officer / Chief Clinical Information Officer.
- **DPO** — Data Protection Officer.
- **AIS** — Accessible Information Standard (NHS).
- **ATRS** — Algorithmic Transparency Recording Standard (UK government).

## Taxonomy-specific

- **Metric family** — A named parent-construct grouping of related metrics (e.g. *Clinical Content Fidelity*) that may span multiple groups. The full list: Reference-Based Text Similarity, Clinical Content Fidelity, Clinical Transcription Accuracy, Post-Generation Correction, Medication Safety Thread, Demographic Equity Disaggregation.
- **Sub-cluster** — A thematic grouping of metrics within a single group. Sub-clusters have italic introductory text before the first member.
- **Reference ID** — Format `{Part}.{Group}-{Number}` (e.g. `TP.AC-1`). Stable across versions; cite as `TP.AC-1` → `/groups/audio-capture/#tp-ac-1`.
- **Tier 1 / 2 / 3** — Priority classification: Tier 1 is minimum viable assurance (measurable today, every deployer must do it); Tier 2 is recommended; Tier 3 is advanced/research-grade.
- **Cadence** — One of *Gate* (pre-deployment), *Continuous*, or *Audit* (periodic).
- **Responsible Actor** — Who is accountable for measuring: *Vendor*, *Deployer*, *Regional body* (ICB), *National body* (NHS England), or *Academic*.
- **Applicability** — Three-way classification per metric: *AVT-Specific*, *AVT-Contextualised*, or *General Healthcare AI*.
- **Underspecification warning** — Explicit flag on a metric where the measurement science does not yet have consensus. Readers should treat these as calls for caution.

*This glossary is a convenience only; the authoritative source for any term is the standards document or the metric entry itself.*
