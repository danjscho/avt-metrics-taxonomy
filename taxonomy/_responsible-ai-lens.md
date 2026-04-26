## Responsible AI Lens

This section provides a **policy-intent view** of the taxonomy. Where the [Standards Mapping](#standards-mapping) section maps metrics against specific regulatory criteria (DTAC, DSPT, MHRA, etc.), this lens tags metrics against two complementary policy frameworks:

- **DSIT AI Playbook for the UK Government (Feb 2025)** - 10 principles for responsible AI use across UK public sector
- **Six Responsible AI Ethical Themes** - the AI Regulation White Paper's five principles (Safety/Security/Robustness; Transparency/Explainability; Fairness; Accountability/Governance; Contestability/Redress) plus the Playbook-added sixth theme (Societal Wellbeing)

### Why a separate lens document?

Standards prescribe *what artefacts and processes must exist*. Principles and themes are *policy lenses* - every metric hits multiple principles and themes, the Playbook itself acknowledges trade-offs between them (e.g. collecting demographic data to assess fairness reduces privacy), and the value is cross-tagging rather than 1:1 mapping.

This lens sits alongside:
- The standards mapping (regulatory-requirement view)
- The [applicability classification](#applicability-classification) (AVT-specific vs general AI view)
- The NHS LLM Evaluation Framework's three groups (operationalisation view - already mapped in standards section)

Think of these as four complementary readings of the same 214-metric substrate: **what's required** (standards), **who it applies to** (applicability), **how to measure** (NHS LLM framework), and **why it matters in policy terms** (this lens).

### On trade-offs

The Playbook is explicit that its principles and themes can be in tension:
- Collecting demographic data for fairness assessment may reduce privacy
- A more explainable or fairer algorithm may consume more energy
- Tighter security may reduce usability
- Stronger human oversight may reduce workflow benefit

Metrics in this lens often serve multiple principles/themes - the [Coverage Matrix](#part-c-coverage-matrix) in Part C highlights cross-cutting "policy-lever" metrics where a single measurement supports several assurance goals simultaneously. Metrics are listed against a principle/theme when they genuinely operationalise that principle, not when they merely touch on it.

---

## Part A - DSIT AI Playbook: 10 Principles

The DSIT AI Playbook (February 2025) sets out ten principles for responsible AI use across UK government. While the Playbook targets central government and arm's length bodies, its principles are referenced in NHS AI governance and many of its requirements (notably ATRS transparency publication) cascade to NHS ALBs. The principles are numbered P1–P10 for reference throughout this document.

### Principle 1: You know what AI is and what its limitations are

> *"AI is a broad field subject to rapid research and innovation, and many claims have been made about both its promise and risks."*

**AVT application:** Understanding AVT's inherent limitations - ASR has error rates proportional to audio quality, accent, and clinical vocabulary; LLM-based summarisation can hallucinate; demographic performance varies; outputs require clinical review. Users must know what the system *can't* do, not just what it can.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | Aspect of P1 |
|-----|--------|-------|------|--------------|
| TP.SN-5 | Hallucination Rate | Summarisation / NLP | 🟢 1 | Knowing fabrication rate |
| TP.SN-6 | Omission Rate | Summarisation / NLP | 🟢 1 | Knowing what gets dropped |
| TP.ASR-1 | Word Error Rate (WER) | ASR / Transcription | 🟡 2 | Baseline accuracy limit |
| TP.ASR-2 | Medical Word Error Rate (M-WER) | ASR / Transcription | 🔵 3 | Clinical vocabulary limits |
| TP.ASR-10 | ASR Confidence Calibration | ASR / Transcription | 🟡 2 | How well confidence reflects accuracy |
| TP.ASR-11 | ASR Confidence Exposure | ASR / Transcription | 🟡 2 | Surfacing uncertainty to users |
| TP.SN-20 | Uncertainty Marker Preservation | Summarisation / NLP | 🟢 1 | Preserving clinician hedging |
| TP.AC-3 | Acoustic Environment Profiling | Audio Capture | 🟡 2 | Environment-limit awareness |
| GV.TC-2 | Failure Mode Awareness Score | Training & Competency | 🟡 2 | Clinician understanding of limits |
| ES.ME-1 | Proximal vs Distal Outcome Distinction | Meta-evaluation | 🔵 3 | Understanding what the metric means |

**Gaps:** Limitations disclosure to patients (not just clinicians) - no direct metric. Running-tally of encountered failure modes over time.

### Principle 2: You use AI lawfully, ethically and responsibly

> *"AI solutions bring specific legal and ethical considerations. Your use of AI tools must be lawful and responsible."*

**AVT application:** UK GDPR lawful basis, DPIA completion, equality assessments, IP considerations for training data, environmental impact, proportionality - is AVT the right intervention for this context? Engages legal, compliance, and DP experts early.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | Aspect of P2 |
|-----|--------|-------|------|--------------|
| GV.CR-7 | DPIA Template Completion Rate | NHS Compliance | 🟢 1 | UK GDPR Art 35 compliance |
| GV.CR-6 | Clinical Safety Case Completeness | NHS Compliance | 🟢 1 | Clinical ethics grounding |
| GV.PD-8 | Consent Verification Accuracy | Privacy & Data Gov | 🟢 1 | Lawful basis foundation |
| GV.CR-1 | Patient Dissent Recording Rate | NHS Compliance | 🟢 1 | Respect for patient rights |
| GV.CR-2 | Verbal Notification Compliance | NHS Compliance | 🟢 1 | Transparency of use |
| GV.PD-9 | Cross-Border Data Transfer Compliance | Privacy & Data Gov | 🟢 1 | International lawfulness |
| GV.PD-10 | Subject Access Request Fulfilment | Privacy & Data Gov | 🟢 1 | UK GDPR Art 15 rights |
| GV.PD-11 | Right to Erasure Compliance | Privacy & Data Gov | 🟢 1 | UK GDPR Art 17 rights |
| GV.PD-4 | Data Minimisation Score | Privacy & Data Gov | 🟡 2 | Proportionality of data use |
| IO.PX-1 | Patient Opt-Out Rate | Patient Experience | 🟢 1 | Respect for dissent |
| GV.EN-1 | Energy Consumption per Clinical Note | Environmental | 🔵 3 | Environmental responsibility |
| GV.EN-2 | Carbon Emissions per Inference | Environmental | 🔵 3 | Environmental responsibility |
| TP.SN-24 | Stigmatising Language Replication Rate | Summarisation / NLP | 🟡 2 | Ethical content generation |

**Gaps:** IP status of training data (not directly measured). Proportionality review (is AVT the right tool for this use case - covered partially by ES.ME-1 but not as a procurement gate).

### Principle 3: You know how to use AI securely

> *"When building and deploying AI services, you must make sure that they are secure to use and resilient to cyber attacks."*

**AVT application:** AI-specific threats - prompt injection via dictated content, data poisoning of fine-tuning sets, audio-channel adversarial attacks, PHI leakage through model outputs, cross-patient information contamination. Secure by Design alignment.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | Aspect of P3 |
|-----|--------|-------|------|--------------|
| GV.SC-1 | Prompt Injection Resistance Rate | Security | 🟡 2 | AI-specific threat |
| GV.SC-2 | Jailbreak Resistance Score | Security | 🟡 2 | Bypass resistance |
| GV.SC-3 | Adversarial Audio Detection Rate | Security | 🔵 3 | AVT-specific threat |
| GV.SC-4 | Data Poisoning Resilience | Security | 🔵 3 | Training-time threat |
| GV.SC-5 | Output Safety Classifier Coverage | Security | 🟡 2 | Output safeguards |
| GV.SC-6 | Template Injection Vulnerability Assessment | Security | 🟡 2 | Template-layer threats |
| GV.SC-7 | Voice Cloning / Deepfake Detection | Security | 🔵 3 | Audio authenticity |
| GV.SC-8 | Side-Channel Data Leakage | Security | 🟡 2 | Information leakage |
| GV.SC-9 | Cross-Patient Information Leakage Rate | Security | 🟡 2 | Cross-contamination |
| GV.SC-10 | Clinician Identity Authentication | Security | 🟡 2 | Access control |
| GV.SC-11 | Membership Inference Attack AUC | Security | 🔵 3 | Privacy attack resistance |
| GV.PD-5 | PII Extraction Attack Success Rate | Privacy & Data Gov | 🟡 2 | PII threat resistance |

**Gaps:** Supply-chain security for model weights and dependencies. AI-specific red-teaming cadence (how often is security re-tested?).

### Principle 4: You have meaningful human control at the right stages

> *"You need to monitor the AI's behaviour and have plans in place to prevent any harmful effects on users."*

**AVT application:** Clinician-in-the-loop review before signing off AI-generated notes into the EPR; ability to edit freely; ability to reject; live monitoring of edit patterns as a signal of AI drift; fallback to manual documentation if AVT fails.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | Aspect of P4 |
|-----|--------|-------|------|--------------|
| HL.HF-3a | Review-Before-Signing Rate | Human Factors | 🟢 1 | Core human control |
| HL.HF-1 | Edit Rate (% Notes Edited) | Human Factors | 🟢 1 | Evidence of meaningful review |
| HL.HF-3b | Time-to-Sign Distribution | Human Factors | 🟢 1 | Review time sufficiency |
| HL.HF-2 | Edit Type Classification | Human Factors | 🟡 2 | Depth of review |
| HL.HF-6 | Automation Bias Detection (Error Injection) | Human Factors | 🟡 2 | Detecting over-reliance |
| HL.HF-7 | Edit Location Distribution | Human Factors | 🟡 2 | Where humans intervene most |
| HL.HF-8 | Trust Calibration Survey | Human Factors | 🟡 2 | Appropriate trust level |
| HL.HF-17 | Verification Burden | Human Factors | 🟡 2 | Cognitive cost of oversight |
| HL.HF-19 | AI-Off Performance Test | Human Factors | 🟡 2 | Graceful degradation |
| HL.HF-9 | Re-record / Abandonment Rate | Human Factors | 🟡 2 | User-initiated override |
| TP.WB-5 | Write-back Rollback Capability | EPR Write-back | 🟡 2 | Reversibility after error |

**Gaps:** Formal escalation paths when AI output is rejected. Board-level visibility of aggregate override patterns.

### Principle 5: You understand how to manage the full AI life cycle

> *"AI solutions, like other technology deployments, have a full product life cycle that you need to understand."*

**AVT application:** Pre-deployment validation, go-live gates, continuous monitoring for drift and bias, model version tracking, update impact assessment, retraining protocols, decommissioning. Aligned with Technology Code of Practice.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | Aspect of P5 |
|-----|--------|-------|------|--------------|
| GV.SG-1 | Model Version Tracking | Safety & Governance | 🟢 1 | Lifecycle foundation |
| GV.SG-2 | Model Update Impact Score | Safety & Governance | 🟡 2 | Change impact |
| GV.SG-3 | Performance Degradation Detection Latency | Safety & Governance | 🟡 2 | Drift detection speed |
| GV.SG-4 | Retraining Trigger Threshold Specification | Safety & Governance | 🟡 2 | When to retrain |
| GV.SG-5 | AI-Generated Data Contamination Rate | Safety & Governance | 🔵 3 | Training data integrity |
| GV.SG-6 | Concept Drift in Clinical Notes | Safety & Governance | 🔵 3 | Semantic drift |
| GV.SG-7 | Probabilistic Risk Quantification (P₁/P₂) | Safety & Governance | 🔵 3 | Risk quantification |
| GV.SG-9 | Safety Performance Indicators with Thresholds (DSCMS) | Safety & Governance | 🟢 1 | Ongoing safety |
| GV.VT-1 | Model Change Notification Compliance | Vendor Transparency | 🟢 1 | Vendor lifecycle cooperation |
| GV.CR-9 | FDA PCCP-Equivalent Pre-Defined Acceptance Criteria | NHS Compliance | 🟡 2 | Pre-defined change control |
| GV.CR-10 | EU AI Act Event Logging Compliance | NHS Compliance | 🟡 2 | Lifecycle event tracking |

**Gaps:** Decommissioning plan (no metric). Model retirement criteria.

### Principle 6: You use the right tool for the job

> *"You should select the most appropriate technology to meet your needs. AI is good at many tasks, but there are a wide range of models and products."*

**AVT application:** Is AVT the right tool? For which consultation types - not all? Should it be template-driven structured notes or full LLM summarisation? Small model or frontier? Procurement should compare AVT against non-AI alternatives (dictation, typing, templated notes).

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | Aspect of P6 |
|-----|--------|-------|------|--------------|
| ES.ME-1 | Proximal vs Distal Outcome Distinction | Meta-evaluation | 🔵 3 | Is AVT solving the right problem? |
| ES.ME-3 | Metric Interaction Analysis | Meta-evaluation | 🔵 3 | Are metrics telling a coherent story? |
| GV.OP-6 | Adoption Rate & Selective Use Patterns | Operational | 🟢 1 | Where clinicians choose to use AVT |
| GV.OP-1 | Documentation Time per Consultation | Operational | 🟢 1 | Comparison vs manual |
| GV.OP-7 | Cost per Consultation | Operational | 🟡 2 | Cost-benefit signal |
| GV.TC-2 | Failure Mode Awareness Score | Training & Competency | 🟡 2 | When not to use |
| HL.HF-9 | Re-record / Abandonment Rate | Human Factors | 🟡 2 | Signal of inappropriate fit |

**Gaps:** Formal comparison against non-AI alternatives (no metric). Procurement-stage tool-fit assessment.

### Principle 7: You are open and collaborative

> *"There are many teams across government and the wider public sector using or exploring AI tools in their work."*

**AVT application:** Publishing AVT use in the Algorithmic Transparency Recording Standard (ATRS) where applicable; patient-facing disclosure of AVT use; benchmark data shared; engaging with civil society, patient groups, and academic community.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | Aspect of P7 |
|-----|--------|-------|------|--------------|
| GV.CR-3 | AI-Generated Content Labelling Compliance | NHS Compliance | 🟢 1 | Output disclosure (parallel to ATRS for records) |
| GV.CR-2 | Verbal Notification Compliance | NHS Compliance | 🟢 1 | Patient-facing transparency |
| GV.CR-4 | AVT Supplier Registry Listing Verification | NHS Compliance | 🟢 1 | Registry transparency |
| GV.CR-5 | ICB Engagement Documentation | NHS Compliance | 🟢 1 | Cross-organisational transparency |
| GV.VT-1 | Model Change Notification Compliance | Vendor Transparency | 🟢 1 | Vendor-to-deployer openness |
| GV.VT-2 | Telemetry Provision Completeness | Vendor Transparency | 🟡 2 | Observability |
| GV.VT-3 | Benchmark & Evaluation Data Accessibility | Vendor Transparency | 🔵 3 | Reproducibility |
| GV.VT-7 | Sub-Processor Transparency | Vendor Transparency | 🟢 1 | Supply chain openness |
| GV.VT-8 | Intermediate Output Access | Vendor Transparency | 🟡 2 | Observability of internal state |

**Gaps:** ATRS publication completeness (no direct metric - ATRS may not apply to all NHS deployments). Patient-facing plain-language documentation.

### Principle 8: You work with commercial colleagues from the start

> *"AI is a rapidly developing market, and you should get specific advice from commercial colleagues on the implications for your project."*

**AVT application:** Vendor contracts should require the same ethical standards as in-house systems; contract clauses for transparency, auditability, incident disclosure; procurement via DTAC-compliant routes; supplier-registry verification.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | Aspect of P8 |
|-----|--------|-------|------|--------------|
| GV.VT-1 | Model Change Notification Compliance | Vendor Transparency | 🟢 1 | Contractual cooperation |
| GV.VT-4 | Audit Trail Completeness | Vendor Transparency | 🟡 2 | Contractual auditability |
| GV.VT-5 | Incident Disclosure Compliance | Vendor Transparency | 🟢 1 | Contractual disclosure |
| GV.VT-6 | Exit & Data Portability Provisions | Vendor Transparency | 🟡 2 | Exit strategy |
| GV.VT-7 | Sub-Processor Transparency | Vendor Transparency | 🟢 1 | Supply chain management |
| GV.VT-8 | Intermediate Output Access | Vendor Transparency | 🟡 2 | Contractual observability |
| GV.CR-4 | AVT Supplier Registry Listing Verification | NHS Compliance | 🟢 1 | Procurement eligibility |
| GV.CR-9 | FDA PCCP-Equivalent Pre-Defined Acceptance Criteria | NHS Compliance | 🟡 2 | Change control clauses |
| GV.OP-7 | Cost per Consultation | Operational | 🟡 2 | Commercial performance |

**Gaps:** Contractual SLA enforcement (no metric for whether SLAs are actually enforced). Exit-clause testing.

### Principle 9: You have the skills and expertise needed to implement and use AI

> *"You should understand the technical and ethical requirements for using AI tools and have them in place within your team."*

**AVT application:** Clinician training on AVT capabilities and limitations; failure-mode awareness; refresher training as models update; SRO/board understanding of AI-specific risks; prompt-craft literacy where applicable.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | Aspect of P9 |
|-----|--------|-------|------|--------------|
| GV.TC-1 | Clinician Training Completion Rate | Training & Competency | 🟢 1 | Foundational skill coverage |
| GV.TC-2 | Failure Mode Awareness Score | Training & Competency | 🟡 2 | Deep understanding |
| GV.TC-3 | Refresher Training & CPD Compliance | Training & Competency | 🟡 2 | Maintained currency |
| GV.TC-4 | Trainee Impact Assessment | Training & Competency | 🔵 3 | Training downstream users |
| GV.TC-5 | Training Material Currency | Training & Competency | 🟡 2 | Material kept current |
| GV.OP-9 | Training Time per Clinician | Operational | 🟡 2 | Training investment |
| HL.HF-8 | Trust Calibration Survey | Human Factors | 🟡 2 | Appropriately calibrated trust |

**Gaps:** SRO / board-level AI literacy assessment. Data scientist / engineering skills on the deployer side.

### Principle 10: You use these principles alongside your organisation's policies and have the right assurance in place

> *"These principles and this playbook set out a consistent approach... While you should use these principles when working with AI, many government organisations have their own governance structures and policies in place."*

**AVT application:** Alignment with trust-level AI safety committee, clinical safety case sign-off, DCB0129/0160 compliance, early engagement with assurance teams, documented review and escalation.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | Aspect of P10 |
|-----|--------|-------|------|---------------|
| GV.CR-6 | Clinical Safety Case Completeness | NHS Compliance | 🟢 1 | Org-specific safety assurance |
| GV.SG-17 | Hazard Log Completeness | Safety & Governance | 🟢 1 | DCB0129/0160 alignment |
| GV.CR-5 | ICB Engagement Documentation | NHS Compliance | 🟢 1 | Regional governance alignment |
| GV.SG-13 | Assurance Debt Accumulation Rate | Safety & Governance | 🟢 1 | Assurance-gap tracking |
| GV.SG-14 | Near-Miss Reporting Rate | Safety & Governance | 🟢 1 | Learning system |
| GV.SG-15 | Time-to-Correct | Safety & Governance | 🟡 2 | Responsive assurance |
| GV.SG-16 | SPI Escalation Response Time | Safety & Governance | 🟡 2 | Escalation mechanism |
| GV.VT-4 | Audit Trail Completeness | Vendor Transparency | 🟡 2 | Assurance evidence base |

**Gaps:** AI review board effectiveness metric. Integration with existing risk management (enterprise risk register alignment).

---

## Part B - Six Responsible AI Ethical Themes

The AI Regulation White Paper (March 2023) articulated five cross-sectoral principles for responsible AI; the DSIT AI Playbook (Feb 2025) ethics chapter extends this with a sixth theme (Societal Wellbeing and Public Good). These six themes are the **policy-intent axes** that the more operational NHS LLM Evaluation Framework's three groups (Suitability in Context, Wider Impact, Quantifiable Changes) help measure. The themes are labelled T1–T6 for reference.

### Theme 1: Safety, Security and Robustness

> *"AI systems should function in a robust, secure and safe way throughout the AI life cycle, and risks should be continually identified, assessed and managed."*

**Source:** AI Regulation White Paper Principle 1
**AVT application:** Clinical safety cases (DCB0129/0160), adversarial robustness to prompt injection, audio-capture reliability, end-to-end hallucination rate, model drift, degraded-mode behaviour.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | How the metric serves T1 |
|-----|--------|-------|------|--------------------------|
| TP.SN-5 | Hallucination Rate | Summarisation / NLP | 🟢 1 | Content safety |
| TP.SN-6 | Omission Rate | Summarisation / NLP | 🟢 1 | Content safety |
| TP.ASR-12 | Hallucination-Under-Noise Rate | ASR / Transcription | 🟢 1 | Robustness under degraded input |
| TP.WB-1 | Write-back Fidelity | EPR Write-back | 🟢 1 | Safety at integration boundary |
| TP.WB-3 | Field Mapping Accuracy | EPR Write-back | 🟢 1 | Safety-critical field routing |
| TP.WB-4 | Update vs Append Behaviour | EPR Write-back | 🟢 1 | Data integrity safety |
| GV.SG-9 | Safety Performance Indicators with Thresholds (DSCMS) | Safety & Governance | 🟢 1 | Ongoing safety threshold monitoring |
| GV.SG-11 | Adverse Event / Incident Rate (LFPSE) | Safety & Governance | 🟢 1 | Incident tracking |
| GV.SG-14 | Near-Miss Reporting Rate | Safety & Governance | 🟢 1 | Precursor signal |
| GV.SG-17 | Hazard Log Completeness | Safety & Governance | 🟢 1 | Risk identification completeness |
| GV.SG-3 | Performance Degradation Detection Latency | Safety & Governance | 🟡 2 | Drift robustness |
| GV.SC-1 | Prompt Injection Resistance Rate | Security | 🟡 2 | Security |
| GV.SC-2 | Jailbreak Resistance Score | Security | 🟡 2 | Security |
| GV.SC-3 | Adversarial Audio Detection Rate | Security | 🔵 3 | Audio-channel security |
| GV.CR-6 | Clinical Safety Case Completeness | NHS Compliance | 🟢 1 | Foundational safety assurance |
| PI.E2E-3 | Error Propagation / Cascade Analysis | End-to-End Pipeline | 🔵 3 | Systemic robustness |
| HL.HF-19 | AI-Off Performance Test | Human Factors | 🟡 2 | Graceful degradation |

**Relationship to other themes:** Overlaps with T4 (Accountability - who is responsible for safety?) and T5 (Contestability - what recourse when safety fails?). Trade-off with T3 (Fairness): safety monitoring may require demographic data collection.

### Theme 2: Appropriate Transparency and Explainability

> *"AI systems should be appropriately transparent and explainable."*

**Source:** AI Regulation White Paper Principle 2
**AVT application:** ATRS publication where applicable, patient-facing disclosure of AVT use, clinician-facing confidence exposure, uncertainty marker preservation, model cards, system cards, audit trails. Proportionate to risk - different audiences need different explanation types.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | How the metric serves T2 |
|-----|--------|-------|------|--------------------------|
| TP.ASR-11 | ASR Confidence Exposure | ASR / Transcription | 🟡 2 | Transparency to clinician |
| TP.SN-20 | Uncertainty Marker Preservation | Summarisation / NLP | 🟢 1 | Clinical uncertainty transparency |
| TP.SN-12 | Linked Evidence / Provenance Tracing | Summarisation / NLP | 🟡 2 | Explainability of output |
| GV.CR-2 | Verbal Notification Compliance | NHS Compliance | 🟢 1 | Patient-facing transparency |
| GV.CR-3 | AI-Generated Content Labelling Compliance | NHS Compliance | 🟢 1 | Record-level transparency |
| GV.VT-1 | Model Change Notification Compliance | Vendor Transparency | 🟢 1 | Model lifecycle transparency |
| GV.VT-2 | Telemetry Provision Completeness | Vendor Transparency | 🟡 2 | Observability |
| GV.VT-3 | Benchmark & Evaluation Data Accessibility | Vendor Transparency | 🔵 3 | Evidence transparency |
| GV.VT-4 | Audit Trail Completeness | Vendor Transparency | 🟡 2 | Auditability |
| GV.VT-7 | Sub-Processor Transparency | Vendor Transparency | 🟢 1 | Supply chain transparency |
| GV.VT-8 | Intermediate Output Access | Vendor Transparency | 🟡 2 | Internal-state transparency |
| PI.PP-5 | Epistemic Status Preservation | Partial-Pipeline | 🔵 3 | Preserving epistemic transparency |

**Relationship to other themes:** Overlaps with T4 (Accountability - transparency enables accountability). Trade-off with T1 (Security): too much transparency may expose attack surfaces. Trade-off with data minimisation (Caldicott Principle 3): audit trails vs minimisation.

### Theme 3: Fairness

> *"AI systems should not undermine the legal rights of individuals or organisations, discriminate unfairly against individuals or create unfair market outcomes."*

**Source:** AI Regulation White Paper Principle 3
**AVT application:** WER parity across accent/dialect/age/gender; summarisation fidelity parity; equity of access; demographic subgroup monitoring; non-discrimination in high-impact decisions. Equality Act 2010 and UK GDPR compliance.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | How the metric serves T3 |
|-----|--------|-------|------|--------------------------|
| TP.ASR-4 | Demographic-Disaggregated WER | ASR / Transcription | 🟡 2 | Fairness at transcription layer |
| TP.ASR-5 | Speaker-Stratified WER | ASR / Transcription | 🔵 3 | Role-based fairness |
| TP.CC-9 | Coding Equity Index | Clinical Coding | 🟡 2 | Fairness at coding layer |
| PI.E2E-5 | Compound Demographic Performance | End-to-End Pipeline | 🔵 3 | Pipeline-level fairness |
| IO.FE-1 | Deployment Equity Index | Fairness & Equity | 🟡 2 | Access-equity |
| IO.FE-2 | Accent Taxonomy Standardisation | Fairness & Equity | 🟡 2 | Equity measurement foundation |
| IO.FE-3 | Clinical Domain Performance Variance | Fairness & Equity | 🟡 2 | Domain-level fairness |
| IO.FE-4 | Intersectional Performance | Fairness & Equity | 🔵 3 | Intersectional fairness |
| IO.FE-5 | Intersectional Compound Fairness Score | Fairness & Equity | 🔵 3 | Composite intersectional |
| IO.FE-6 | Rare Presentation Handling | Fairness & Equity | 🔵 3 | Edge-case equity |
| IO.FE-7 | Health Literacy Performance Variation | Fairness & Equity | 🔵 3 | Literacy equity |
| IO.FE-8 | Cross-Platform Fairness Consistency | Fairness & Equity | 🔵 3 | Platform equity |
| IO.PX-4 | Cultural & Linguistic Appropriateness | Patient Experience | 🔵 3 | Cultural fit |
| TP.SN-24 | Stigmatising Language Replication Rate | Summarisation / NLP | 🟡 2 | Non-discrimination in output |

**Relationship to other themes:** Trade-off with T2 (Transparency around demographic-data collection): fairness assessment requires demographic data, which reduces privacy. Trade-off with T1 (Safety): safety floors may be set based on fairness gaps. Overlaps with T6 (Societal Wellbeing): fairness is part of societal benefit.

### Theme 4: Accountability and Governance

> *"Governance measures should be in place to ensure effective oversight of the supply and use of AI systems, with clear lines of accountability established across the AI life cycle."*

**Source:** AI Regulation White Paper Principle 4
**AVT application:** Clinical Safety Officer sign-off, SRO designation, vendor contract accountability, DTAC assurance, audit trails, AI review board, PSIRF organisation-level oversight.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | How the metric serves T4 |
|-----|--------|-------|------|--------------------------|
| GV.CR-5 | ICB Engagement Documentation | NHS Compliance | 🟢 1 | Regional governance |
| GV.CR-6 | Clinical Safety Case Completeness | NHS Compliance | 🟢 1 | Safety accountability |
| GV.CR-7 | DPIA Template Completion Rate | NHS Compliance | 🟢 1 | Data protection accountability |
| GV.SG-1 | Model Version Tracking | Safety & Governance | 🟢 1 | Traceability |
| GV.SG-13 | Assurance Debt Accumulation Rate | Safety & Governance | 🟢 1 | Governance-gap tracking |
| GV.SG-17 | Hazard Log Completeness | Safety & Governance | 🟢 1 | Safety accountability |
| GV.VT-1 | Model Change Notification Compliance | Vendor Transparency | 🟢 1 | Vendor accountability |
| GV.VT-4 | Audit Trail Completeness | Vendor Transparency | 🟡 2 | Auditability for accountability |
| GV.VT-5 | Incident Disclosure Compliance | Vendor Transparency | 🟢 1 | Vendor disclosure |
| GV.VT-7 | Sub-Processor Transparency | Vendor Transparency | 🟢 1 | Supply-chain accountability |
| GV.CR-10 | EU AI Act Event Logging Compliance | NHS Compliance | 🟡 2 | Regulatory accountability |
| GV.CR-4 | AVT Supplier Registry Listing Verification | NHS Compliance | 🟢 1 | Procurement accountability |

**Relationship to other themes:** Overlaps with T5 (Contestability: accountability enables contestation). Overlaps with T2 (Transparency enables accountability). Distinct from T1 (Safety is what is governed; accountability is how governance is structured).

### Theme 5: Contestability and Redress

> *"Where appropriate, users, impacted third parties and actors in the AI life cycle should be able to contest an AI decision or outcome that is harmful or creates material risk of harm."*

**Source:** AI Regulation White Paper Principle 5
**AVT application:** Patient route to challenge note content; clinician override capability; incident reporting workflow; complaint pipeline; redress for documentation errors; rollback capability.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | How the metric serves T5 |
|-----|--------|-------|------|--------------------------|
| IO.PX-1 | Patient Opt-Out Rate | Patient Experience | 🟢 1 | Patient-level contestability |
| GV.CR-1 | Patient Dissent Recording Rate | NHS Compliance | 🟢 1 | Documented dissent |
| GV.PD-10 | Subject Access Request Fulfilment | Privacy & Data Gov | 🟢 1 | Right to see the record |
| GV.PD-11 | Right to Erasure Compliance | Privacy & Data Gov | 🟢 1 | Right to delete |
| HL.HF-9 | Re-record / Abandonment Rate | Human Factors | 🟡 2 | Clinician override evidence |
| HL.HF-1 | Edit Rate (% Notes Edited) | Human Factors | 🟢 1 | Clinician contestability |
| GV.SG-15 | Time-to-Correct | Safety & Governance | 🟡 2 | Redress speed |
| GV.VT-5 | Incident Disclosure Compliance | Vendor Transparency | 🟢 1 | Incident-level redress signal |
| GV.VT-6 | Exit & Data Portability Provisions | Vendor Transparency | 🟡 2 | Organisation-level redress |
| TP.WB-5 | Write-back Rollback Capability | EPR Write-back | 🟡 2 | Technical redress |
| HL.HF-17 | Verification Burden | Human Factors | 🟡 2 | Cost of contestability |

**Relationship to other themes:** Overlaps with T4 (Accountability - contestability requires clear accountability). Overlaps with T2 (Transparency - you must see to contest). Trade-off with T1 (Safety - too-easy reversal may allow errors to propagate before correction).

### Theme 6: Societal Wellbeing and Public Good

> *"AI should deliver positive broader societal impact, use resources proportionately, and avoid deployment where harm outweighs benefit."*

**Source:** DSIT AI Playbook ethics chapter (Playbook-added sixth theme; not in original White Paper five)
**AVT application:** Environmental/compute footprint, equity of benefit distribution across practices, workforce impact (burnout relief vs deskilling), patient trust at population level, sustainability of adoption at scale, therapeutic relationship impact. This is the theme most distinct from operational performance - it asks whether AVT's deployment makes NHS healthcare better overall, including second-order effects.

**Relevant taxonomy metrics:**

| Ref | Metric | Group | Tier | How the metric serves T6 |
|-----|--------|-------|------|--------------------------|
| GV.EN-1 | Energy Consumption per Clinical Note | Environmental | 🔵 3 | Environmental sustainability |
| GV.EN-2 | Carbon Emissions per Inference | Environmental | 🔵 3 | Environmental sustainability |
| GV.EN-3 | Water Consumption per Query | Environmental | 🔵 3 | Environmental sustainability |
| IO.FE-1 | Deployment Equity Index | Fairness & Equity | 🟡 2 | Access equity (societal) |
| IO.PX-6 | Therapeutic Relationship Impact | Patient Experience | 🔵 3 | Doctor-patient relationship |
| IO.PX-5 | Chilling Effect Assessment | Patient Experience | 🔵 3 | Patient willingness to disclose |
| HL.HF-12 | Clinical Documentation Skill Attenuation | Human Factors | 🔵 3 | Workforce deskilling |
| HL.HF-13 | Cognitive Offloading Rate | Human Factors | 🔵 3 | Workforce dependence |
| HL.HF-10 | Cognitive Load Assessment | Human Factors | 🔵 3 | Workforce wellbeing (reducing burnout) |
| GV.OP-1 | Documentation Time per Consultation | Operational | 🟢 1 | Workforce time impact |
| GV.OP-2 | Pyjama Time / After-Hours EHR Use | Operational | 🟡 2 | Workforce wellbeing |
| GV.TC-4 | Trainee Impact Assessment | Training & Competency | 🔵 3 | Future workforce development |

**Relationship to other themes:** Overlaps with T3 (Fairness - equity is part of societal wellbeing). Partial overlap with T1 (Safety - population-level safety is societal). Distinct from T2/T4/T5 (process-focused themes). **This is the theme with the highest concentration of Tier 3 metrics**, reflecting that societal effects are intrinsically harder to measure than operational performance.

---

## Part C - Coverage Matrix

Some metrics serve multiple Playbook principles *and* multiple ethical themes simultaneously. These are **policy-lever metrics** - a single measurement supports several assurance goals at once, making them high-leverage procurement and governance signals. Implementing or monitoring these metrics gives the broadest coverage for the least measurement burden.

The matrix below lists metrics that genuinely operationalise **3 or more principles** *or* **3 or more themes**. Metrics serving only 1–2 principles/themes are listed in the per-principle and per-theme tables in Parts A and B but not repeated here.

### High cross-cutting metrics (policy-lever)

| Ref | Metric | Tier | Playbook Principles | Ethical Themes | Why cross-cutting |
|-----|--------|------|--------------------|-----------------|--------------------|
| TP.SN-5 | Hallucination Rate | 🟢 1 | P1, P4, P5 | T1, T2 | Core content integrity - limits-awareness, human-control trigger, lifecycle drift signal, safety, transparency of fabrication |
| TP.SN-6 | Omission Rate | 🟢 1 | P1, P4, P5 | T1, T2 | Parallel to hallucination - what the system loses is as important as what it fabricates |
| TP.SN-20 | Uncertainty Marker Preservation | 🟢 1 | P1, P4 | T1, T2 | Preserves clinical uncertainty for human decision-making; transparency about confidence |
| HL.HF-1 | Edit Rate (% Notes Edited) | 🟢 1 | P1, P4, P5 | T2, T5 | Evidence of meaningful human review, running signal of model fit, contestability evidence |
| HL.HF-3 | Review-Before-Signing Rate | 🟢 1 | P4, P10 | T4, T5 | Core human control + accountability trail + contestability foundation |
| HL.HF-6 | Automation Bias Detection (Error Injection) | 🟡 2 | P1, P4, P9 | T1, T2 | Reveals user over-reliance, triggers training updates, safety and transparency interplay |
| HL.HF-8 | Trust Calibration Survey | 🟡 2 | P1, P4, P9 | T2, T5 | Calibrated trust is necessary for meaningful control, skills-check, and contestability |
| GV.CR-1 | Patient Dissent Recording Rate | 🟢 1 | P2, P7 | T4, T5 | Lawfulness, transparency, accountability, contestability all converge here |
| GV.CR-2 | Verbal Notification Compliance | 🟢 1 | P2, P7 | T2, T4 | Patient-facing transparency, lawfulness, accountability |
| GV.CR-3 | AI-Generated Content Labelling Compliance | 🟢 1 | P2, P7 | T2, T4, T5 | Record-level transparency enabling audit, contestation, and regulatory compliance |
| GV.CR-6 | Clinical Safety Case Completeness | 🟢 1 | P2, P5, P10 | T1, T4 | Lawfulness, lifecycle, organisational assurance, safety, accountability |
| GV.CR-7 | DPIA Template Completion Rate | 🟢 1 | P2, P10 | T4 | Lawfulness + organisational assurance + accountability |
| GV.SG-1 | Model Version Tracking | 🟢 1 | P5, P10 | T4 | Lifecycle foundation enabling accountability |
| GV.SG-9 | Safety Performance Indicators with Thresholds (DSCMS) | 🟢 1 | P5, P10 | T1, T4 | Lifecycle monitoring + organisational assurance + safety + accountability |
| GV.SG-11 | Adverse Event / Incident Rate (LFPSE) | 🟢 1 | P4, P5, P10 | T1, T4, T5 | Very high cross-cutting - incidents feed every theme |
| GV.SG-14 | Near-Miss Reporting Rate | 🟢 1 | P4, P5, P10 | T1, T4 | Precursor signal across multiple concerns |
| GV.SG-17 | Hazard Log Completeness | 🟢 1 | P2, P5, P10 | T1, T4 | DCB0129/0160 foundation, ethical grounding, organisational assurance |
| GV.VT-1 | Model Change Notification Compliance | 🟢 1 | P5, P7, P8 | T2, T4 | Lifecycle + openness + commercial + transparency + accountability |
| GV.VT-4 | Audit Trail Completeness | 🟡 2 | P3, P8, P10 | T2, T4, T5 | Foundational auditability serving multiple downstream goals |
| GV.VT-5 | Incident Disclosure Compliance | 🟢 1 | P7, P8 | T4, T5 | Openness + commercial + accountability + contestability |
| GV.VT-7 | Sub-Processor Transparency | 🟢 1 | P7, P8 | T2, T4 | Supply-chain openness + commercial accountability |
| GV.PD-8 | Consent Verification Accuracy | 🟢 1 | P2, P7 | T2, T4 | Lawful basis + transparency + accountability |
| IO.PX-1 | Patient Opt-Out Rate | 🟢 1 | P2, P4, P7 | T3, T5 | Lawful basis, human control at patient level, openness, fairness of access, contestability |
| GV.TC-2 | Failure Mode Awareness Score | 🟡 2 | P1, P6, P9 | T1, T2 | Understanding limits + right-tool assessment + skills + safety + transparency |
| TP.WB-1 | Write-back Fidelity | 🟢 1 | P3, P4, P5 | T1, T4 | Safety-critical integration point across multiple axes |

### Patterns in the matrix

**Highest cross-cutting metrics (5 principles/themes or more):**
- GV.SG-11 Adverse Event / Incident Rate (LFPSE) - 6 axes
- GV.VT-4 Audit Trail Completeness - 6 axes
- GV.CR-3 AI-Generated Content Labelling Compliance - 5 axes
- HL.HF-1 Edit Rate - 5 axes
- IO.PX-1 Patient Opt-Out Rate - 5 axes

These five metrics are the "policy-lever megas" - implementing and monitoring them captures a disproportionate share of the responsible-AI requirement space. They should be the backbone of any AVT assurance programme.

**Concentration by group:**
- Safety & Governance, NHS Compliance & Regulatory, and Vendor Transparency groups dominate the cross-cutting list
- Content fidelity metrics (TP.SN-5, TP.SN-6, TP.SN-20) are the only Part A metrics that reach 4+ axes - reflecting how clinical content integrity sits at the intersection of safety, transparency, limits-awareness, and human control
- Human Factors metrics (HL.HF-1, HL.HF-3, HL.HF-6, HL.HF-8) are heavily cross-cutting because human-AI interaction intersects every principle

**Tier distribution:** Nearly all cross-cutting metrics are Tier 1 or Tier 2. This is expected - the most load-bearing assurance metrics are the ones that multiple principles converge on.

---

## Part D - Gaps

Gap analysis has been consolidated into the single roadmap at [Gaps & Proposed Metrics](#gaps-proposed-metrics-roadmap) § 3 (Responsible AI Lens). 38 candidates are tracked there: 20 organised by Playbook principle, 18 organised by ethical theme. Cross-references to standards-mapping gaps (e.g. PSIRF → GV.SG-19, CQC → GV.CR-12) are preserved in the roadmap. Highest-severity cross-cutting findings are summarised below.

### Summary

**Highest-severity cross-cutting gaps (appear in multiple lens axes):**

1. **Patient-facing explanation / contestability of AVT output** - appears as gap under P7 (Openness), T2 (Transparency), T5 (Contestability). The taxonomy assumes clinicians mediate AI output to patients; increasingly, patient-facing AI requires direct patient channels.
2. **Board-level AI governance** - appears under P10 (Org assurance), T4 (Accountability), and CQC Well-led. Captured in proposed GV.CR-12; arguably the single highest-leverage missing metric for NHS deployment.
3. **Tool-fit / proportionality assessment** - appears under P2 (ethical), P6 (Right tool), and NICE ESF Tier classification. Procurement-stage gap.
4. **Systems-based incident learning (SEIPS)** - appears under T1 (Safety), PSIRF mandatory requirements. Captured in proposed GV.SG-19.
5. **Societal Wellbeing measurement generally** - Theme 6 has the highest concentration of gaps because second-order effects on workforce, patient relationships, and healthcare sustainability are intrinsically hard to measure.

**Gap concentration by theme:** Theme 6 (Societal Wellbeing) has the most gaps, followed by Theme 5 (Contestability). Theme 1 (Safety) and Theme 4 (Accountability) have the fewest gaps - reflecting that the taxonomy was built from a safety-first, governance-aware starting point.

**Gap concentration by principle:** P6 (Right tool) and P7 (Openness) have the largest number of gaps - reflecting that the taxonomy is weaker on *decision-to-deploy* and *outward transparency* than on *in-deployment performance*. This is a structural gap that several of the proposed new metrics in the standards mapping would begin to close.
