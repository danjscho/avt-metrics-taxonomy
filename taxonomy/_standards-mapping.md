## Standards Mapping

This section maps the taxonomy's 214 metrics against four NHS/regulatory frameworks to help deployers, vendors, and assurance teams identify which metrics satisfy which compliance obligations. For each framework, individual criteria or assertions are mapped to specific taxonomy metrics.

Where a standard criterion has no corresponding taxonomy metric, this is flagged as a **gap**. Where the taxonomy provides coverage beyond the standard's scope, this is noted as **taxonomy extends**.

---

### DTAC (Digital Technology Assessment Criteria) v2.0

DTAC is the NHS assessment framework for digital health technologies. It has four assessed sections (C1–C4) and one comparative section (D1). DTAC v2.0 (February 2026) explicitly names Ambient Voice Technologies as potentially requiring additional assurance beyond DTAC.

#### C1 — Clinical Safety

| DTAC Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| C1.1.1 | Software / AI as Medical Device classification | *Process criterion — no metric equivalent; informs scope* | — |
| C1.2.2 | DCB0129 Clinical Risk Management compliance | Clinical Safety Case Completeness | 🟢 1 |
| C1.2.3 | Clinical risk management system detail | Hazard Log Completeness | 🟢 1 |
| C1.2.4 | Clinical Safety Case Report and Hazard Log | Clinical Safety Case Completeness, Hazard Log Completeness | 🟢 1 |
| C1.2.5 | Named Clinical Safety Officer | *Process criterion — no metric equivalent* | — |

**Taxonomy extends:** Safety Performance Indicators with Thresholds (DSCMS), Adverse Event / Incident Rate (LFPSE), Near-Miss Reporting Rate, Probabilistic Risk Quantification (P₁/P₂) — the taxonomy provides ongoing safety monitoring metrics that DTAC does not assess.

#### C2 — Data Protection

| DTAC Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| C2.1 | DSPT compliance | DSPA Status | 🟡 2 |
| C2.2.1 | ICO registration | *Process criterion — no metric equivalent* | — |
| C2.2.2 | Data Protection Impact Assessment | DPIA Template Completion Rate | 🟢 1 |
| C2.2.3 | Transparency information / privacy notice | Patient Dissent Recording Rate, Verbal Notification Compliance | 🟢 1 |
| C2.2.4 | Terms and conditions | *Process criterion — no metric equivalent* | — |
| C2.2.5 | Data storage and processing location | Cross-Border Data Transfer Compliance | 🟢 1 |
| C2.2.6 | Cross-border legislative compliance | Cross-Border Data Transfer Compliance | 🟢 1 |

**Taxonomy extends:** Audio Retention Compliance, Audio Time-to-Deletion, Transcript Retention Compliance, Data Minimisation Score, Right to Erasure Compliance, Subject Access Request Fulfilment, Consent Verification Accuracy — extensive AVT-specific privacy metrics beyond DTAC's data protection scope.

#### C3 — Technical Security

| DTAC Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| C3.1 | Cyber Essentials certification | *Certification criterion — no metric equivalent* | — |
| C3.3 | Penetration testing (OWASP top 10) | Prompt Injection Resistance Rate, Jailbreak Resistance Score, Template Injection Vulnerability Assessment | 🟡 2 |
| C3.4 | Software Security Code of Practice | Output Safety Classifier Coverage | 🟡 2 |
| C3.5 | Multi-factor authentication | Clinician Identity Authentication | 🟡 2 |
| C3.6 | Logging and reporting | Audit Trail Completeness, EU AI Act Event Logging Compliance | 🟡 2 |

**Taxonomy extends:** Adversarial Audio Detection Rate, Data Poisoning Resilience, Voice Cloning / Deepfake Detection, Side-Channel Data Leakage, Cross-Patient Information Leakage Rate, Membership Inference Attack AUC — AVT-specific adversarial robustness metrics beyond DTAC's general security scope.

#### C4 — Interoperability

| DTAC Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| C4.1.1 | API interoperability standards | FHIR R4 Resource Conformance Rate, openEHR Archetype Conformance | 🟡 2 / 🔵 3 |
| C4.1.2 | Open API documentation | *Process criterion — no metric equivalent* | — |
| C4.2.1 | NHS number for patient identification | Field Mapping Accuracy (EPR integration) | 🟢 1 |
| C4.2.2 | PDS / local record integration | Integration Error Rate | 🟢 1 |

**Taxonomy extends:** Write-back Fidelity, Update vs Append Behaviour, Write-back Rollback Capability, Structured/Free-Text Consistency — the taxonomy has extensive EPR write-back safety metrics that go far beyond DTAC's interoperability questions.

#### D1 — Usability and Accessibility

| DTAC Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| D1.1 | User journey / care pathway fit | Work-as-Imagined vs Work-as-Done Gap | 🔵 3 |
| D1.2 | User testing | Trust Calibration Survey, Full Attentiveness Rate | 🟡 2 |
| D1.3 | Accessible Information Standard | *Gap — no accessibility metric in taxonomy* | — |
| D1.4.1 | WCAG 2.2 AA compliance | *Gap — no accessibility metric in taxonomy* | — |
| D1.5 | Service availability | System Availability / Uptime | 🟢 1 |

**Gaps:** The taxonomy has no web accessibility (WCAG) or Accessible Information Standard metrics. These are relevant for AVT user interfaces but not for the clinical AI pipeline itself.

---

### DSPT (Data Security and Protection Toolkit) — NDG Standards

DSPT v8 uses 10 National Data Guardian Data Security Standards with assertions and evidence items. This mapping covers the Category 2 (IT Supplier) variant, which is most relevant to AVT vendors. Only assertions with AI/AVT-relevant content are mapped.

#### Standard 1 — Personal Confidential Data

| DSPT Assertion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| 1.1.1 | ICO registration | *Process criterion — no metric equivalent* | — |
| 1.1.2 | Documented personal data holdings | Data Minimisation Score, Training Data Inclusion Status | 🟡 2 |
| 1.1.3 | Privacy information published | Verbal Notification Compliance, Patient Dissent Recording Rate | 🟢 1 |
| 1.1.6 | Consent to share reviewed | Consent Verification Accuracy | 🟢 1 |
| 1.2.2 | Handling objection to processing | Patient Opt-Out Rate, Patient Dissent Recording Rate | 🟢 1 |
| 1.2.3 | Subject access request process | Subject Access Request Fulfilment | 🟢 1 |
| 1.2.4 | National data opt-out compliance | Patient Opt-Out Rate | 🟢 1 |
| 1.3.5 | Data security risk register | Assurance Debt Accumulation Rate | 🟢 1 |
| 1.3.7 | Data protection by design | Data Minimisation Score, PII Extraction Attack Success Rate | 🟡 2 |
| 1.3.8 | DPIA process linked to risk management | DPIA Template Completion Rate | 🟢 1 |
| 1.4.1 | Records management including retention | Audio Retention Compliance, Transcript Retention Compliance, Audio Time-to-Deletion | 🟢 1 |

#### Standard 2 — Staff Responsibilities

| DSPT Assertion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| 2.2.1 | Contracts contain data security requirements | *Process criterion — no metric equivalent* | — |

#### Standard 3 — Training

| DSPT Assertion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| 3.1.1 | Training needs analysis | Training Material Currency | 🟡 2 |
| 3.1.2 | Training activities implemented | Clinician Training Completion Rate | 🟢 1 |
| 3.1.3 | Evaluation of training | Failure Mode Awareness Score | 🟡 2 |
| 3.2.1 | IG/cyber prioritised by board | *Process criterion — no metric equivalent* | — |

#### Standard 4 — Managing Access

| DSPT Assertion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| 4.2.3 | Logs retained and searchable | Audit Trail Completeness | 🟡 2 |
| 4.3.2 | Users/systems authenticated before access | Clinician Identity Authentication | 🟡 2 |
| 4.4.1 | Privileged account logs tamper-proof | Audit Trail Completeness | 🟡 2 |
| 4.5.3 | MFA enforced on remote/privileged access | Clinician Identity Authentication | 🟡 2 |

#### Standard 5 — Process Reviews

| DSPT Assertion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| 5.1.1 | Root cause analysis after incidents | Time-to-Correct, Adverse Event / Incident Rate (LFPSE) | 🟡 2 / 🟢 1 |

#### Standard 6 — Responding to Incidents

| DSPT Assertion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| 6.1.1 | Incidents reported by staff | Near-Miss Reporting Rate, Adverse Event / Incident Rate (LFPSE) | 🟢 1 |
| 6.1.2 | Board informed of reportable breaches | SPI Escalation Response Time | 🟡 2 |
| 6.1.3 | Affected individuals informed | Incident Disclosure Compliance | 🟢 1 |
| 6.3.3 | Proportionate monitoring for security events | Performance Degradation Detection Latency, Output Safety Classifier Coverage | 🟡 2 |

#### Standard 7 — Continuity Planning

| DSPT Assertion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| 7.1.2 | Service continuity during incidents | Pipeline Failure Recovery, System Availability / Uptime | 🟡 2 / 🟢 1 |
| 7.3.4 | Backups of essential service data | Write-back Rollback Capability | 🟡 2 |

#### Standard 8 — Unsupported Systems

| DSPT Assertion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| 8.1.1 | Software asset tracking | Model Version Tracking | 🟢 1 |
| 8.3.1 | System update frequency | Model Update Impact Score, Model Change Notification Compliance | 🟡 2 / 🟢 1 |

#### Standard 9 — IT Protection

| DSPT Assertion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| 9.2.1 | Annual penetration test | Prompt Injection Resistance Rate, Jailbreak Resistance Score | 🟡 2 |
| 9.3.1 | Web applications protected (OWASP) | Template Injection Vulnerability Assessment | 🟡 2 |
| 9.3.6 | Data in transit protected | Cross-Border Data Transfer Compliance | 🟢 1 |
| 9.5.11 | Software per Security Code of Practice | Output Safety Classifier Coverage | 🟡 2 |

#### Standard 10 — Accountable Suppliers

| DSPT Assertion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| 10.1.1 | Supplier list with risk identification | Sub-Processor Transparency, AVT Supplier Registry Listing Verification | 🟢 1 |
| 10.2.1 | Supplier certification | AVT Supplier Registry Listing Verification | 🟢 1 |
| 10.2.4 | Outsourced service security | Sub-Processor Transparency | 🟢 1 |

---

### DCB0129 / DCB0160 — Clinical Risk Management Standards

DCB0129 applies to manufacturers of health IT systems; DCB0160 applies to deploying organisations. Both follow the same clinical safety lifecycle. This mapping shows which taxonomy metrics provide evidence for each lifecycle stage.

#### Stage 1: Clinical Risk Management System

| Requirement | Actor | Taxonomy Metrics | Tier |
|-------------|-------|-----------------|------|
| Appoint Clinical Safety Officer | Manufacturer / Deployer | Clinical Safety Case Completeness (evidences CSO sign-off) | 🟢 1 |
| Document Clinical Risk Management Plan | Manufacturer / Deployer | *Process artefact — no metric equivalent* | — |
| Define risk management scope | Manufacturer / Deployer | Coverage Gap Analysis (identifies where measurement is absent) | 🔵 3 |

#### Stage 2: Hazard Identification

| Requirement | Actor | Taxonomy Metrics | Tier |
|-------------|-------|-----------------|------|
| Systematic hazard identification | Both | Hazard Log Completeness | 🟢 1 |
| Consider intended use and foreseeable misuse | Both | Off-Label Use Detection Rate | 🟡 2 |
| Document hazards in Hazard Log | Both | Hazard Log Completeness | 🟢 1 |
| Consider failure modes | Both | Error Propagation / Cascade Analysis, Pipeline Failure Recovery | 🔵 3 / 🟡 2 |
| Consider interactions with other systems | Both | Integration Error Rate, Structured/Free-Text Consistency | 🟢 1 / 🟡 2 |
| Consider user interface issues | Both | Automation Bias Detection (Error Injection), Trust Calibration Survey | 🟡 2 |

**Taxonomy extends for AVT-specific hazards:**
- Hallucination Rate, Omission Rate (content fabrication/loss)
- Speaker Attribution Accuracy (misattribution)
- Write-back Fidelity, Field Mapping Accuracy (EPR integration failures)
- Code Hallucination Rate (non-existent code generation)
- Bystander Voice Detection Rate (consent/privacy failures)

#### Stage 3: Risk Assessment

| Requirement | Actor | Taxonomy Metrics | Tier |
|-------------|-------|-----------------|------|
| Severity × likelihood risk estimation | Both | Probabilistic Risk Quantification (P₁/P₂), Safety Performance Indicators with Thresholds (DSCMS) | 🔵 3 / 🟢 1 |
| Risk classification (acceptable → unacceptable) | Both | Assurance Debt Accumulation Rate (tracks tolerable risk accumulation) | 🟢 1 |
| Record initial and residual risk | Both | Hazard Log Completeness | 🟢 1 |

#### Stage 4: Risk Control

| Requirement | Actor | Taxonomy Metrics | Tier |
|-------------|-------|-----------------|------|
| Inherent safety by design | Manufacturer | Code Hallucination Rate (constrained generation = inherent safety) | 🟢 1 |
| Protective measures within system | Manufacturer | Output Safety Classifier Coverage, Prompt Injection Resistance Rate | 🟡 2 |
| Information for safety (warnings, guidance) | Manufacturer | Uncertainty Marker Preservation, ASR Confidence Exposure | 🟢 1 / 🟡 2 |
| Verify risk control effectiveness | Both | All Tier 1 metrics collectively evidence risk control effectiveness | 🟢 1 |
| Ensure no new hazards from controls | Both | Metric Interaction Analysis | 🔵 3 |

#### Stage 5: Clinical Safety Case

| Requirement | Actor | Taxonomy Metrics | Tier |
|-------------|-------|-----------------|------|
| Clinical Safety Case Report | Both | Clinical Safety Case Completeness | 🟢 1 |
| Residual risk summary | Both | Assurance Debt Accumulation Rate | 🟢 1 |
| Release decision sign-off | Both | *Process criterion — no metric equivalent* | — |

#### Stage 6: Monitoring and Review

| Requirement | Actor | Taxonomy Metrics | Tier |
|-------------|-------|-----------------|------|
| Post-market surveillance | Manufacturer | Performance Degradation Detection Latency, Cross-Practice Variance Coefficient | 🟡 2 |
| Monitor safety through incident analysis | Both | Adverse Event / Incident Rate (LFPSE), Near-Miss Reporting Rate | 🟢 1 |
| Review Hazard Log on modification | Both | Model Update Impact Score, Retraining Trigger Threshold Specification | 🟡 2 |
| Periodic safety reviews | Both | Safety Performance Indicators with Thresholds (DSCMS) | 🟢 1 |
| Manage safety through change | Manufacturer | Model Change Notification Compliance, FDA PCCP-Equivalent Pre-Defined Acceptance Criteria | 🟢 1 / 🟡 2 |
| Monitor for unexpected clinical impacts | Deployer | Downstream Diagnostic Accuracy, Medication Error Rate Differential | 🔵 3 |

#### Stage 7: Incident Management

| Requirement | Actor | Taxonomy Metrics | Tier |
|-------------|-------|-----------------|------|
| Incident management procedures | Both | Adverse Event / Incident Rate (LFPSE), SPI Escalation Response Time | 🟢 1 / 🟡 2 |
| Root cause investigation | Both | Error Attribution Analysis, Time-to-Correct | 🔵 3 / 🟡 2 |
| Corrective actions | Both | Time-to-Correct | 🟡 2 |
| Safety notices / field corrective actions | Manufacturer | Incident Disclosure Compliance, Model Change Notification Compliance | 🟢 1 |
| Report to MHRA if medical device | Manufacturer | *Process criterion — no metric equivalent* | — |
| Report through LFPSE | Deployer | Adverse Event / Incident Rate (LFPSE) | 🟢 1 |

---

### NHS England LLM Evaluation and Monitoring Framework (v0.2.2)

> **⚠️ Draft framework.** This mapping is against v0.2.2 (August 2025), which is experimental and subject to change. Dimensions marked with 🔄 appear provisional — their scope or measurement approach may evolve significantly before v1.0. This mapping should be reviewed when the framework reaches v1.0.

The framework has 30 evaluation dimensions across three groups. All dimensions in Suitability in Context and Wider Impact use manual monitoring; Quantifiable Changes dimensions use automatic continuous monitoring with manual review.

#### Group 1: Suitability in Context (11 dimensions)

| LLM Framework Dimension | Taxonomy Metrics | Tier | Notes |
|--------------------------|-----------------|------|-------|
| **Accountability** | Clinical Safety Case Completeness, ICB Engagement Documentation, Incident Disclosure Compliance | 🟢 1 | Taxonomy provides specific metrics for the accountability chain |
| **Concept drift** | Concept Drift in Clinical Notes, Performance Degradation Detection Latency, AI-Generated Data Contamination Rate | 🔵 3 / 🟡 2 | Taxonomy's Longitudinal Drift & Model Contamination sub-cluster maps directly |
| **Cost** 🔄 | Cost per Consultation, Governance & Maintenance Burden | 🟡 2 / 🔵 3 | **Partial gap** — taxonomy lacks total cost of ownership or cost-effectiveness metric |
| **Data governance** | DPIA Template Completion Rate, Audio Retention Compliance, Transcript Retention Compliance, Data Minimisation Score, Training Data Inclusion Status | 🟢 1 / 🟡 2 | Strong coverage through Privacy & Data Governance group |
| **Expected outcomes** | Clinical Decision Equivalence, Downstream Diagnostic Accuracy, Documentation Time per Consultation | 🔵 3 / 🟢 1 | Taxonomy addresses clinical outcomes; framework's "is an LLM the right solution?" question has no metric equivalent |
| **Explainability** 🔄 | Linked Evidence / Provenance Tracing, Intermediate Output Access, ASR Confidence Exposure | 🟡 2 | Taxonomy provides provenance tracing rather than model interpretability |
| **Fairness and edge cases** | Demographic-Disaggregated WER, Intersectional Performance, Rare Presentation Handling, Health Literacy Performance Variation, Coding Equity Index | 🟡 2 / 🔵 3 | Extensive coverage through Demographic Equity Disaggregation family + Fairness & Equity group |
| **Privacy** | PII Extraction Attack Success Rate, Re-identification Risk Assessment, Cross-Patient Information Leakage Rate, Membership Inference Attack AUC | 🟡 2 / 🔵 3 | Strong coverage for model-level privacy; audio/transcript privacy in separate group |
| **Safety assessment** | Safety Performance Indicators with Thresholds (DSCMS), Hazard Log Completeness, Clinical Safety Case Completeness | 🟢 1 | Maps directly to DCB0129/0160 requirements |
| **Subject matter expert involvement** 🔄 | *Gap — no metric for SME participation in evaluation* | — | Taxonomy assigns Responsible Actors but does not measure SME involvement depth |
| **Uncertainty communication** | Uncertainty Marker Preservation, ASR Confidence Exposure, ASR Confidence Calibration | 🟢 1 / 🟡 2 | Strong coverage for output uncertainty; automation bias addresses user response |

#### Group 2: Wider Impact (11 dimensions)

| LLM Framework Dimension | Taxonomy Metrics | Tier | Notes |
|--------------------------|-----------------|------|-------|
| **Accessibility of healthcare** | Deployment Equity Index, Adoption Rate & Selective Use Patterns | 🟡 2 / 🟢 1 | Taxonomy addresses deployment equity; does not address health literacy access |
| **Documentation** | Telemetry Provision Completeness, Benchmark & Evaluation Data Accessibility, Model Change Notification Compliance | 🟡 2 / 🟢 1 | Good coverage through Vendor Transparency group |
| **Ethics** 🔄 | Stigmatising Language Replication Rate, Emotional Content Preservation, Chilling Effect Assessment | 🟡 2 / 🔵 3 | Taxonomy addresses specific ethical dimensions; no general ethics framework metric |
| **Feedback mechanism** | Near-Miss Reporting Rate, Re-record / Abandonment Rate | 🟢 1 / 🟡 2 | Taxonomy covers incident/feedback reporting but not structured staff feedback mechanisms |
| **Human oversight** | Review-Before-Signing Rate, Edit Rate, Automation Bias Detection, Verification Burden | 🟢 1 / 🟡 2 | Strong coverage through Post-Generation Correction family + human factors metrics |
| **Intentional misuse** | Prompt Injection Resistance Rate, Jailbreak Resistance Score, Adversarial Audio Detection Rate, Template Injection Vulnerability Assessment | 🟡 2 / 🔵 3 | Strong coverage through Security & Adversarial Robustness group |
| **Natural environment** | Energy Consumption per Clinical Note, Carbon Emissions per Inference, Water Consumption per Query | 🔵 3 | Direct mapping to Environmental & Sustainability group |
| **Regulations** | Clinical Safety Case Completeness, DPIA Template Completion Rate, EU AI Act Event Logging Compliance, FDA PCCP-Equivalent Pre-Defined Acceptance Criteria | 🟢 1 / 🟡 2 | Strong coverage through NHS Compliance & Regulatory group |
| **Society** 🔄 | Clinical Documentation Skill Attenuation, Cognitive Offloading Rate, Therapeutic Relationship Impact | 🔵 3 | Taxonomy addresses skill/wellbeing impacts; no job security metric |
| **Third-party audit** | Audit Trail Completeness, Benchmark & Evaluation Data Accessibility | 🟡 2 / 🔵 3 | Taxonomy provides audit infrastructure metrics |
| **Unintentional misuse** | Clinician Training Completion Rate, Failure Mode Awareness Score, Off-Label Use Detection Rate | 🟢 1 / 🟡 2 | Good coverage through Training & Competency group |

#### Group 3: Quantifiable Changes (8 dimensions)

| LLM Framework Dimension | Taxonomy Metrics | Tier | Notes |
|--------------------------|-----------------|------|-------|
| **Benchmark relevance** 🔄 | Goodhart's Law Monitoring, Coverage Gap Analysis, Inter-Rater Reliability Baseline | 🟡 2 / 🔵 3 | **Partial gap** — taxonomy lacks explicit benchmark relevance decay metric |
| **Bias — in-context learning** 🔄 | *Gap — no metric for few-shot prompt bias* | — | Not directly applicable to most AVT systems (pipeline-based, not prompt-based) |
| **Bias analysis — error rates** | Demographic-Disaggregated WER, Intersectional Performance, Intersectional Compound Fairness Score, Compound Demographic Performance | 🟡 2 / 🔵 3 | Strong coverage through Demographic Equity Disaggregation family |
| **Changes to the system** | Model Version Tracking, Model Update Impact Score, Model Change Notification Compliance | 🟢 1 / 🟡 2 | Direct mapping — taxonomy has strong change management metrics |
| **Data drift** | Performance Degradation Detection Latency, Concept Drift in Clinical Notes, Retraining Trigger Threshold Specification | 🟡 2 / 🔵 3 | Good coverage; taxonomy distinguishes concept drift from data drift |
| **Evaluation techniques for ongoing monitoring** | PDSQI-9, CREOLA Error Taxonomy, LLM-as-a-Judge, Automated-Human Metric Concordance | 🟡 2 / 🔵 3 | Strong coverage; taxonomy extensively addresses clinical evaluation methodology |
| **Scalability** 🔄 | Full-Pipeline Latency Budget, System Availability / Uptime | 🟡 2 / 🟢 1 | **Partial gap** — taxonomy lacks explicit scalability / concurrency metric |
| **System for monitoring** | Safety Performance Indicators with Thresholds (DSCMS), Goodhart's Law Monitoring | 🟢 1 / 🟡 2 | Taxonomy provides the metrics; framework asks whether monitoring infrastructure exists |

---

### MHRA Software and AI as a Medical Device (SaMD / AIaMD)

The MHRA's regulatory position on software and AI as medical devices is delivered through the **Change Programme** (workstreams WP1–WP11), the **joint FDA/Health Canada Guiding Principles**, and the **Post-Market Surveillance Regulations 2024** (SI 2024 No. 1368, in force 16 June 2025). This mapping covers the assessable criteria most relevant to AVT systems.

**Publisher:** Medicines and Healthcare products Regulatory Agency (MHRA)
**Mandatory status:** Mandatory for systems classified as medical devices under UK MDR 2002; cascades to AVT deployments via vendor compliance obligations
**AVT relevance:** AVT systems with clinical decision-support components may qualify as SaMD/AIaMD. Documentation-only systems may not, but the AI RIG and Transparency principles are widely applied as best practice regardless of classification.

#### Change Programme — Classification (WP1, WP2)

| MHRA Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| WP1-01 | What qualifies as SaMD | *Process criterion — no metric equivalent; informs scope* | — |
| WP1-02 | Crafting intended purpose | *Process criterion — documentation requirement* | — |
| WP1-03 | Manufacturer definition | *Process criterion — legal determination* | — |
| WP2-01 | Classification rules (UK MDR 2002, IMDRF-aligned) | GV.CR-6 Clinical Safety Case Completeness (evidences classification) | 🟢 1 |
| WP2-02 | Regulatory "airlock" sandbox | *Process route — no metric equivalent* | — |
| WP2-03 | Classification rule interpretation | *Process criterion* | — |

#### Change Programme — Premarket (WP3)

| MHRA Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| WP3-02 | Best-practice SaMD development | GV.VT-2 Telemetry Provision Completeness, GV.VT-3 Benchmark & Evaluation Data Accessibility | 🟡 2 / 🔵 3 |
| WP3-04 | Data-driven SaMD (joint with HRA) | GV.PD-7 Training Data Inclusion Status, TP.ASR-4 Demographic-Disaggregated WER | 🟡 2 |
| WP3-05 | Human-centred SaMD | HL.HF-1 Edit Rate, HL.HF-3 Review-Before-Signing Rate, HL.HF-6 Automation Bias Detection | 🟢 1 / 🟡 2 |

#### Change Programme — Post-Market Surveillance (WP4 + SI 2024 No. 1368)

| MHRA Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| PMS Plan | Signal detection, complaints handling, literature review, field experience | GV.SG-3 Performance Degradation Detection Latency, GV.SG-12 Cross-Practice Variance Coefficient | 🟡 2 |
| PMSR (Class I/IIa, on demand) | Periodic non-implantable reporting | *No metric equivalent — reporting artefact* | — |
| PSUR (Class IIb/III, annually) | Periodic Safety Update Report | *No metric equivalent — reporting artefact* | — |
| WP4-02 Reportable incidents (including indirect harm) | Documentation errors causing downstream clinical harm | GV.SG-11 Adverse Event / Incident Rate (LFPSE), GV.SG-14 Near-Miss Reporting Rate | 🟢 1 |
| Trend reporting | Statistically significant increases in non-serious incidents | GV.SG-12 Cross-Practice Variance Coefficient | 🟡 2 |
| WP4-03 Change management | Post-deployment changes and their re-evaluation | GV.SG-2 Model Update Impact Score, GV.VT-1 Model Change Notification Compliance | 🟡 2 / 🟢 1 |
| WP4-04 Predetermined Change Control Plans | PCCPs for AIaMD | GV.CR-9 FDA PCCP-Equivalent Pre-Defined Acceptance Criteria | 🟡 2 |
| Field Safety Corrective Action (FSCA) | Corrective action execution | GV.SG-15 Time-to-Correct, GV.VT-5 Incident Disclosure Compliance | 🟡 2 / 🟢 1 |
| Field Safety Notices (FSN) | Targeted notifications | GV.VT-5 Incident Disclosure Compliance | 🟢 1 |
| Reporting timelines (2/10/15 working days) | Serious threat / death / other serious incidents | GV.SG-16 SPI Escalation Response Time | 🟡 2 |

#### Change Programme — Cybersecurity (WP5)

| MHRA Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| WP5-01 / 02 | Cybersecurity legislation and guidance | GV.SC-1 Prompt Injection Resistance Rate, GV.SC-2 Jailbreak Resistance Score | 🟡 2 |
| WP5-03 | Unsupported software | GV.SG-1 Model Version Tracking | 🟢 1 |
| WP5-04 | Vulnerability reporting | GV.VT-5 Incident Disclosure Compliance | 🟢 1 |

#### Change Programme — AI Rigour (WP9)

| MHRA Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| WP9-01 | GMLP guiding principles (Oct 2021) | *Cross-references 10 GMLP principles below* | — |
| WP9-05 | "AIaMD for all" — bias across populations | TP.ASR-4 Demographic-Disaggregated WER, IO.FE-4 Intersectional Performance, TP.CC-9 Coding Equity Index | 🟡 2 / 🔵 3 |
| WP9-06 | Bias identification standards | IO.FE-3 Clinical Domain Performance Variance, IO.FE-5 Intersectional Compound Fairness Score | 🟡 2 / 🔵 3 |
| WP9-07 | Experimental bias detection / mitigation | IO.FE-2 Accent Taxonomy Standardisation, TP.ASR-5 Speaker-Stratified WER | 🟡 2 / 🔵 3 |

#### Change Programme — Glass Box / Interpretability (WP10)

| MHRA Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| WP10-01 | Human-centred AIaMD | TP.ASR-11 ASR Confidence Exposure, TP.SN-20 Uncertainty Marker Preservation, TP.SN-12 Linked Evidence / Provenance Tracing | 🟡 2 / 🟢 1 |
| WP10-02 | Trustworthy AIaMD standards | HL.HF-8 Trust Calibration Survey, HL.HF-6 Automation Bias Detection | 🟡 2 |

#### Change Programme — Ship of Theseus / Adaptivity (WP11)

| MHRA Criterion | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| WP11-01 | Adaptivity guiding principles (static/batch/individualised/continuous) | GV.SG-1 Model Version Tracking, GV.SG-2 Model Update Impact Score | 🟢 1 / 🟡 2 |
| WP11-02 | Concept drift and significant-change detection | GV.SG-6 Concept Drift in Clinical Notes, GV.SG-3 Performance Degradation Detection Latency | 🔵 3 / 🟡 2 |
| WP11-03 | PCCPs for AIaMD | GV.CR-9 FDA PCCP-Equivalent Pre-Defined Acceptance Criteria | 🟡 2 |

#### Transparency Guiding Principles (June 2024, joint MHRA/FDA/Health Canada)

Six-dimension framework (WHO/WHY/WHAT/WHERE/WHEN/HOW). The WHAT dimension contains the most assessable content items:

| Transparency Dimension | Content Items | Taxonomy Metrics | Tier |
|------------------------|---------------|-----------------|------|
| **WHAT — Device characterisation** | Medical purpose, disease/condition, intended users, use environments, target populations | *Partial gap — no specific "device characterisation completeness" metric* | — |
| **WHAT — Workflow integration** | How device fits workflow, intended inputs/outputs | HL.HF-1 Edit Rate, HL.HF-3 Review-Before-Signing Rate | 🟢 1 |
| **WHAT — Performance & safety** | Performance details, benefits/risks, bias-management, clinical study summaries | TP.ASR-1 WER, TP.SN-5 Hallucination Rate, GV.SG-9 Safety Performance Indicators | 🟡 2 / 🟢 1 |
| **WHAT — Model logic & development** | Output logic, ML approach, training/testing data characterisation | GV.PD-7 Training Data Inclusion Status, GV.VT-3 Benchmark & Evaluation Data Accessibility | 🟡 2 / 🔵 3 |
| **WHAT — Limitations** | Known biases, failure modes, confidence intervals, data gaps, validation envelope | TP.SN-5 Hallucination Rate, TP.SN-6 Omission Rate, TP.ASR-10 ASR Confidence Calibration, TP.AC-3 Acoustic Environment Profiling | 🟢 1 / 🟡 2 |
| **WHAT — Lifecycle** | Local acceptance testing, ongoing monitoring, change-management, vulnerability mitigation | GV.SG-3 Performance Degradation Detection Latency, GV.SG-1 Model Version Tracking | 🟡 2 / 🟢 1 |

#### Good Machine Learning Practice (GMLP) — 10 Principles (Oct 2021)

| GMLP Principle | Description | Taxonomy Metrics | Tier |
|----------------|-------------|-----------------|------|
| GMLP-1 | Multi-Disciplinary Expertise | *Organisational requirement — no direct metric* | — |
| GMLP-2 | Good Software and Engineering Practices | GV.SC-1/2 security metrics, GV.VT-4 Audit Trail Completeness | 🟡 2 |
| GMLP-3 | Representative Datasets | TP.ASR-4 Demographic-Disaggregated WER, GV.PD-7 Training Data Inclusion Status | 🟡 2 |
| GMLP-4 | Training Data Independent from Test Data | *No metric equivalent — methodology check* | — |
| GMLP-5 | Best Available Reference Datasets | GV.VT-3 Benchmark & Evaluation Data Accessibility | 🔵 3 |
| GMLP-6 | Model Design Tailored to Data and Intended Use | ES.ME-1 Proximal vs Distal Outcome Distinction | 🔵 3 |
| GMLP-7 | Focus on Human-AI Team Performance | HL.HF-1 Edit Rate, HL.HF-6 Automation Bias Detection, HL.HF-8 Trust Calibration Survey | 🟢 1 / 🟡 2 |
| GMLP-8 | Testing in Clinically Relevant Conditions | TP.AC-3 Acoustic Environment Profiling, PI.E2E-9 Clinical Decision Equivalence | 🟡 2 / 🔵 3 |
| GMLP-9 | Users Provided Clear Essential Information | TP.ASR-11 ASR Confidence Exposure, TP.SN-20 Uncertainty Marker Preservation | 🟡 2 / 🟢 1 |
| GMLP-10 | Deployed Models Monitored, Retraining Risks Managed | GV.SG-3 Performance Degradation Detection Latency, GV.SG-4 Retraining Trigger Threshold Specification, GV.SG-5 AI-Generated Data Contamination Rate | 🟡 2 / 🔵 3 |

**Gaps:**
- Medical device classification documentation (no metric)
- PCCP documentation for adaptive algorithms (partial — GV.CR-9 is about acceptance criteria, not the PCCP itself)
- PMSR / PSUR report completeness (reporting artefacts, no metric)
- Transparency documentation for all WHAT content items as a composite
- Device characterisation completeness

**Taxonomy extends:** Strong coverage through Safety & Governance (incident detection and response), Security & Adversarial Robustness, Privacy & Data Governance, and Vendor Transparency groups. MHRA guidance is process-heavy; the taxonomy provides the measurement substrate that MHRA assumes exists.

---

### NICE Evidence Standards Framework for Digital Health Technologies (ECD7)

**Publisher:** National Institute for Health and Care Excellence (NICE)
**Version:** ECD7 published 10 December 2018; last substantive update 9 August 2022 (AI provisions)
**Mandatory status:** Not formally mandatory but de facto required for any DHT claiming NHS clinical benefit; referenced in NICE appraisal, procurement, and ICS commissioning.
**AVT relevance:** AVT systems typically sit in Tier B1 (Communicating) or Tier C1/C2 (Clinical Management) depending on write-back configuration. A pure transcription tool that does not influence clinical decisions is Tier B1; a tool whose output drives structured coding or decision-support is Tier C1/C2.

ECD7 contains **21 numbered standards across 5 lifecycle areas**. Each has **minimum** and **best practice** levels across **Tier A/B/C** functional classification. AI-specific provisions are concentrated in Standards 4, 5, 6, 15, and 16.

#### Standards 1–9: Design Factors

| NICE Standard | Description | Taxonomy Metrics | Tier |
|--------------|-------------|-----------------|------|
| 1 — Safety & Quality Compliance | UKCA/CE, GDPR, CQC (min); ISO 13485, IEC 82304-1, BS EN 62304 (best) | GV.CR-6 Clinical Safety Case Completeness, GV.CR-7 DPIA Template Completion Rate | 🟢 1 |
| 2 — User Acceptability | Users in design/testing (min); IEC 62366-1 usability engineering (best) | HL.HF-8 Trust Calibration Survey, IO.PX-7 Full Attentiveness Rate | 🟡 2 |
| 3 — Environmental Sustainability | Narrative (min); NHS net-zero alignment, quantified GHG (best) | GV.EN-1 Energy Consumption per Clinical Note, GV.EN-2 Carbon Emissions per Inference | 🔵 3 |
| **4 — Inequalities & Bias Mitigation** ⭐ AI-specific | Describe considerations (min); **document algorithmic bias mitigation** (best) | IO.FE-1 Deployment Equity Index, TP.ASR-4 Demographic-Disaggregated WER, TP.CC-9 Coding Equity Index, IO.FE-5 Intersectional Compound Fairness Score | 🟡 2 / 🔵 3 |
| **5 — Data Practices** ⭐ AI-specific | Identify datasets (min); **follow MHRA GMLP, dataset diversity** (best) | GV.PD-7 Training Data Inclusion Status, GV.PD-4 Data Minimisation Score | 🟡 2 |
| **6 — Professional Oversight** ⭐ AI-specific | Articulate oversight level (min); proportionate oversight, override tracking (best) | HL.HF-3 Review-Before-Signing Rate, HL.HF-1 Edit Rate, HL.HF-6 Automation Bias Detection | 🟢 1 / 🟡 2 |
| 7 — Health Information Reliability | Validity processes (min); expert review at intervals (best) | TP.SN-3 PDSQI-9, TP.SN-4 CREOLA Error Taxonomy Scores | 🟡 2 |
| 8 — UK Professional Credibility | Professional involvement (min); expert-group utility evidence (best) | *Process criterion — no metric equivalent* | — |
| 9 — Safeguarding | Access controls, moderation (min); documented agreements, qualified oversight (best) | GV.PD-8 Consent Verification Accuracy, TP.AC-4 Bystander Voice Detection Rate | 🟢 1 / 🔵 3 |

#### Standards 10–13: Describing Value

| NICE Standard | Description | Taxonomy Metrics | Tier |
|--------------|-------------|-----------------|------|
| 10 — Intended Purpose & Target Population | Inclusion/exclusion (min); subgroup variation (best) | IO.FE-3 Clinical Domain Performance Variance, IO.FE-6 Rare Presentation Handling | 🟡 2 / 🔵 3 |
| 11 — Current Pathway | Clinical guidelines + consultation (min) | *Process criterion — no metric equivalent* | — |
| 12 — Proposed Pathway | Differences from current care (min); workforce changes, boundaries crossed (best) | GV.OP-1 Documentation Time per Consultation, GV.OP-6 Adoption Rate & Selective Use Patterns | 🟢 1 |
| 13 — Expected Impacts | Compare benefits/costs (min); confidence intervals, sensitivity analysis (best) | IO.PX-9 Downstream Diagnostic Accuracy, PI.E2E-9 Clinical Decision Equivalence | 🔵 3 |

#### Standards 14–16: Demonstrating Performance

| NICE Standard | Description | Taxonomy Metrics | Tier |
|--------------|-------------|-----------------|------|
| 14 — Effectiveness Evidence *(Tier C only)* | Clinical-mgmt: real-world evaluations; Diagnostic: accuracy vs reference; Treatment: RCTs preferred | PI.E2E-9 Clinical Decision Equivalence, IO.PX-9 Downstream Diagnostic Accuracy, IO.PX-10 Medication Error Rate Differential | 🔵 3 |
| **15 — Real-World Evidence** ⭐ AI-specific | Pilot site statement (min); **"silent mode" evaluation for AI on local data** (best) | GV.SG-12 Cross-Practice Variance Coefficient, GV.OP-6 Adoption Rate & Selective Use Patterns | 🟡 2 / 🟢 1 |
| **16 — Performance Monitoring Plan** ⭐ AI-specific | Usage vs expected (min); **AI/ML: post-deployment reporting, retraining schedules, subgroup drift** (best) | GV.SG-3 Performance Degradation Detection Latency, GV.SG-4 Retraining Trigger Threshold Specification, GV.SG-6 Concept Drift in Clinical Notes | 🟡 2 / 🔵 3 |

#### Standards 17–18: Delivering Value

| NICE Standard | Description | Taxonomy Metrics | Tier |
|--------------|-------------|-----------------|------|
| 17 — Budget Impact Analysis | Direct costs vs comparator (min); indirect costs, NHS reference costs (best) | GV.OP-7 Cost per Consultation | 🟡 2 |
| 18 — Cost-Effectiveness Analysis | Cost-utility or cost-consequences (min); EQ-5D for QALYs, sensitivity/scenario analyses (best) | *Gap — taxonomy lacks cost-effectiveness or QALY metric* | — |

#### Standards 19–21: Deployment

| NICE Standard | Description | Taxonomy Metrics | Tier |
|--------------|-------------|-----------------|------|
| 19 — Deployment Transparency | Data dictionary, input description, infrastructure (min); tolerance for incomplete data, DICOM etc. (best) | GV.VT-2 Telemetry Provision Completeness, TP.WB-6 FHIR R4 Resource Conformance Rate | 🟡 2 |
| 20 — Communication, Consent & Training | Describe outputs (min); model cards, training approaches (best) | GV.TC-1 Clinician Training Completion Rate, GV.TC-2 Failure Mode Awareness Score, GV.CR-3 AI-Generated Content Labelling Compliance | 🟢 1 / 🟡 2 |
| 21 — Scalability | Load testing (min); documented methodology vs projected users (best) | GV.OP-5 System Availability / Uptime, PI.E2E-10 Full-Pipeline Latency Budget | 🟢 1 / 🟡 2 |

**Gaps:**
- Tier A/B/C functional classification documentation for specific AVT deployments
- "Silent mode" evaluation evidence (Standard 15 best practice) — partial coverage via GV.OP-6 but no dedicated metric
- Subgroup drift monitoring as a composite (Standard 16 best practice) — metrics exist but not assembled
- Cost-effectiveness analysis / QALY (Standard 18) — no metric
- Budget impact analysis composite (Standard 17) — GV.OP-7 is partial
- Real-world performance data plan documentation (Standard 15)

**Taxonomy extends:** Standards 14–16 (Performance) are well covered. Part A (Technical Pipeline) and Part B (Pipeline Interactions) provide measurement depth that NICE ESF does not prescribe at the operational level.

---

### FHIR UK Core / INTEROPen

**Publisher:** NHS England Digital, with HL7 UK; INTEROPen community contribution
**Scope:** UK-specific FHIR R4 profiles for health and care data exchange. Successor to CareConnect (STU3).
**Mandatory status:** De facto mandatory for NHS system interoperability; referenced in NHS Standard Contract and procurement.
**AVT relevance:** AVT systems writing back to EPRs must conform to UK Core profiles, not generic FHIR R4. Different STU versions expose different resources: STU1 is foundational only (no Composition/Condition/Observation); STU2 adds the clinical content profiles AVT actually needs; STU3 adds specialised observations.

#### Release Status

| Release | Base | Status | Relevance for AVT |
|---------|------|--------|-------------------|
| **STU1 (1.0.0)** | FHIR R4 | Published | 12 foundational profiles (Patient, Practitioner, Medication*, AllergyIntolerance) — insufficient alone for clinical note write-back |
| **STU2 (2.0.2)** | FHIR R4 | Released 28 May 2024 (current) | 33 profiles including Composition, Condition, Encounter, Observation, Procedure — the baseline for AVT write-back |
| **STU3** | FHIR R4 | In development ("Sequence") | ~52 profiles adding specialised vital-sign Observations (NEWS2, blood glucose, alcohol consumption, vital signs) |

#### Assertion-level profile conformance (STU2+ baseline for AVT)

| UK Core Profile | STU | AVT Write-back Relevance | Taxonomy Metrics | Tier |
|-----------------|-----|--------------------------|-----------------|------|
| UKCore-Composition | 2+ | Clinical note container; assembles sections | TP.WB-6 FHIR R4 Resource Conformance Rate *(refined: means UK Core, not generic FHIR R4)* | 🟡 2 |
| UKCore-Encounter | 2+ | Binds note to consultation event | TP.WB-6 FHIR R4 Resource Conformance Rate | 🟡 2 |
| UKCore-Condition | 2+ | Extracted diagnoses / problems | TP.WB-3 Field Mapping Accuracy, TP.CC-2 SNOMED CT Concept Mapping Accuracy | 🟢 1 / 🟡 2 |
| UKCore-AllergyIntolerance | 1+ | Extracted allergies (safety-critical) | TP.WB-1 Write-back Fidelity, TP.WB-4 Update vs Append Behaviour | 🟢 1 |
| UKCore-MedicationStatement | 1+ | Current medications | TP.CC-5 dm+d Medication Coding Accuracy, TP.WB-1 Write-back Fidelity | 🟡 2 / 🟢 1 |
| UKCore-MedicationRequest | 1+ | New prescriptions | TP.SN-19 Medication Attribute Extraction F1, TP.SN-21 Medication Event Classification | 🟡 2 |
| UKCore-Observation | 2+ | Structured vitals from consultation | TP.WB-3 Field Mapping Accuracy | 🟢 1 |
| UKCore-Procedure | 2+ | Procedures performed/planned | TP.CC-4 OPCS-4 Procedure Coding Accuracy | 🟡 2 |
| UKCore-ServiceRequest | 2+ | Referrals, tests ordered | TP.WB-3 Field Mapping Accuracy | 🟢 1 |
| UKCore-Patient | 1+ | Patient demographics | TP.WB-3 Field Mapping Accuracy | 🟢 1 |

#### UK-specific Extensions and Terminology Bindings

| UK Core Extension / Binding | Description | Taxonomy Metrics | Tier |
|------------------------------|-------------|-----------------|------|
| NHS Number + NHSNumberVerificationStatus | Primary patient identifier with verification state | TP.WB-3 Field Mapping Accuracy | 🟢 1 |
| EthnicCategory | UK census code system on Patient | *Gap — no specific ethnic category binding metric* | — |
| BirthSex extension | UK-specific sex at birth | *Process criterion — no metric equivalent* | — |
| DeathNotificationStatus | PDS integration | *Gap — no PDS integration metric* | — |
| ResidentialStatus | UK-specific residential state | *Process criterion* | — |
| SNOMED CT primary terminology binding | With CodingSCTDescDisplay extension | TP.CC-1 SNOMED Code Accuracy, TP.CC-2 SNOMED CT Concept Mapping Accuracy | 🟡 2 |
| dm+d for medicinal products | Medication terminology | TP.CC-5 dm+d Medication Coding Accuracy | 🟡 2 |
| NHS Data Dictionary codes | Administrative data | *Process criterion* | — |

**Refinement of existing metrics (interpretation clarification, not content change):**

| Existing Metric | Refinement |
|-----------------|-----------|
| TP.WB-6 FHIR R4 Resource Conformance Rate | "FHIR conformance" for NHS deployment means **UK Core profiles**, not generic FHIR R4. Vendors claiming STU1 compliance cannot write back Composition / Condition / Observation — that is STU2+ capability. Stratify conformance reporting by STU version. |
| TP.WB-7 openEHR Archetype Conformance | openEHR is the alternative to FHIR in some NHS trusts (particularly mental health). Relevance depends on target EPR. |

**Gaps:**
- Per-profile UK Core conformance stratification (aggregate TP.WB-6 doesn't distinguish Composition vs Condition vs Observation conformance)
- UK-specific extension conformance (NHS Number verification status, Ethnic Category, Death Notification, Residential Status)
- STU version targeting documentation (vendors must declare which STU version they support)
- INTEROPen-defined extension conformance (beyond UK Core base)
- PDS integration depth

**Taxonomy extends:** Write-back Safety sub-cluster (TP.WB-1 through TP.WB-4) addresses safety semantics that UK Core profile conformance alone doesn't guarantee. A valid-but-wrong FHIR resource passes conformance but fails fidelity.

---

### CQC Assessment for AI

**Publisher:** Care Quality Commission (CQC)
**Scope:** Deployer-side regulatory inspection covering the Five Key Questions (Safe, Effective, Caring, Responsive, Well-led) under the Single Assessment Framework, with AI-specific guidance in GP Mythbuster 109 and emerging quality statements.
**Mandatory status:** CQC inspection is mandatory for all registered providers; CQC ratings are public and directly affect commissioning.
**AVT relevance:** CQC regulates the *provider using the tool*, not the tool itself. Clinical responsibility is non-delegable to the AI. This mapping covers what CQC inspectors are likely to ask about an AVT deployment.

**⚠️ Emerging area (2025–26):** GP Mythbuster 109 is the published baseline. Formal CQC quality statements specific to AI in primary and secondary care are evolving. This mapping will need review when the CQC AI-specific assessment framework is finalised.

**Key dimensions and taxonomy coverage:**

- **GP Mythbuster 109 baseline assertions:**
  - CQC regulates providers not tools — provider remains accountable for AI output
  - Clinical responsibility non-delegable — clinician must review/sign off before the record is final → covered by HL.HF-3 Review-Before-Signing Rate, HL.HF-1 Edit Rate
  - Record-keeping duty (Regulation 17, good governance) applies unchanged → partial (no specific "record quality" composite metric)
  - AVT consent — implied consent acceptable if patients informed and can dissent → covered by GV.CR-1 Patient Dissent Recording Rate, GV.CR-2 Verbal Notification Compliance, IO.PX-1 Patient Opt-Out Rate
  - Medical device classification considerations → cross-reference to MHRA SaMD section
  - DCB0129/DCB0160 clinical safety case → covered by GV.CR-6 Clinical Safety Case Completeness, GV.SG-17 Hazard Log Completeness
  - DTAC compliance pre-procurement → cross-reference to DTAC section
  - Staff training on AI limitations → covered by GV.TC-1 Clinician Training Completion Rate, GV.TC-2 Failure Mode Awareness Score

- **Safe (Five Key Questions)**: Covered extensively by Safety & Governance group — GV.SG-17 Hazard Log Completeness, GV.SG-11 Adverse Event / Incident Rate (LFPSE), GV.SG-14 Near-Miss Reporting Rate, GV.SG-9 Safety Performance Indicators with Thresholds. Bias audits covered by IO.FE-3 Clinical Domain Performance Variance, TP.ASR-4 Demographic-Disaggregated WER. Rollback capability covered by TP.WB-5 Write-back Rollback Capability.

- **Effective**: Partial — clinical accuracy benchmarking covered by TP.ASR-1 WER, TP.SN-5 Hallucination Rate, TP.CC-1 SNOMED Code Accuracy. Outcome monitoring vs pre-AI baseline partially covered by GV.SG-3 Performance Degradation Detection Latency, IO.PX-9 Downstream Diagnostic Accuracy. Clinician review/sign-off covered by HL.HF-3 Review-Before-Signing Rate. NICE alignment cross-references NICE ESF section.

- **Caring**: Covered by IO.PX-1 Patient Opt-Out Rate, IO.PX-2 Patient-Perceived Accuracy, IO.PX-6 Therapeutic Relationship Impact, IO.PX-7 Full Attentiveness Rate, GV.CR-2 Verbal Notification Compliance. Dignity during recording — gap (no specific metric).

- **Responsive**: Partial — accessibility covered by IO.FE-2 Accent Taxonomy Standardisation, IO.FE-7 Health Literacy Performance Variation. Language coverage covered by TP.DI-6 Code-Switching Detection Rate. Equity audit covered by IO.FE-1 Deployment Equity Index, TP.CC-9 Coding Equity Index. Complaint routes specific to AI — gap.

- **Well-led**: Partial — board-level AI governance — gap. Named accountable director — gap. CSO role covered by GV.CR-6 Clinical Safety Case Completeness. Audit trail covered by GV.VT-4 Audit Trail Completeness. Vendor management covered by GV.VT group (transparency, incident disclosure, sub-processor). Risk register — partial via GV.SG-13 Assurance Debt Accumulation Rate.

- **CSO expectations**: Registered clinician, DCB0129/0160 trained, maintains Clinical Safety Case and Hazard Log, signs off DCB0160 before go-live. Covered procedurally by GV.CR-6 Clinical Safety Case Completeness, GV.SG-17 Hazard Log Completeness. CSO capacity for AI oversight is a gap (no metric).

**Overall position:** CQC assessment is structurally broader than any single standard because it covers the whole provider operation. The taxonomy provides strong measurement coverage for the Safe and Caring dimensions, partial coverage for Effective and Responsive, and weakest coverage for Well-led (board-level governance, named accountability, AI-specific complaint handling). The gaps are concentrated in provider-organisation-level governance mechanisms rather than clinical-AI performance.

**Gaps:**
- Board-level AI governance mechanism
- Named accountable director for AI
- CSO capacity for AI oversight (separate from CSO sign-off)
- Patient complaint handling specific to AI outputs
- Dignity during recording
- AI-specific equity of access auditing (language/accessibility composite)
- Record quality composite (Regulation 17 alignment)

---

### Patient Safety Incident Response Framework (PSIRF)

**Publisher:** NHS England
**Scope:** Systems-based, proportionate response to patient safety incidents, replacing the 2015 Serious Incident Framework.
**Mandatory status:** Mandatory for acute, ambulance, mental health, and community NHS providers since autumn 2023; primary care and independent-sector rollout 2024–26.
**AVT relevance:** PSIRF applies when AI-generated documentation contributes to patient harm. The response should be proportionate and system-based, looking at the whole sociotechnical pipeline (audio → ASR → summariser → clinician review → EPR) rather than blaming the clinician who signed off.

**Key dimensions and taxonomy coverage:**

- **Four PSIRF principles:**
  - **Compassionate engagement** — Gap (no metric for engagement with those affected by AI-related harm)
  - **Systems-based learning** — Partial — PI.E2E-3 Error Propagation / Cascade Analysis, PI.E2E-8 Error Attribution Analysis provide pipeline-level analysis but not the organisation-level learning response
  - **Proportionate response** — Partial — GV.SG-16 SPI Escalation Response Time addresses timeliness but not proportionality
  - **Supportive oversight** — Gap (no metric for board/ICB oversight of AI-related safety learning)

- **Key components:**
  - Patient Safety Incident Response Policy — Process artefact, no metric
  - Patient Safety Incident Response Plan (PSIRP, 12–18 month forward plan) — Process artefact, no metric
  - Patient Safety Incident Response Standards — Process artefact, no metric
  - Patient Safety Incident Investigation (PSII) — Partial via GV.SG-11 Adverse Event / Incident Rate (LFPSE), GV.SG-15 Time-to-Correct

- **Learning response types:**
  - After Action Review (AAR) — Gap
  - MDT Review — Gap
  - PSII (deepest response) — Partial via GV.SG-11 Adverse Event / Incident Rate (LFPSE), PI.E2E-8 Error Attribution Analysis
  - SEIPS-informed analysis — Gap (no metric for whole-system analysis of AI incidents)
  - Swarm huddle / thematic review / horizon scanning — Gap

- **Engagement requirements:**
  - Patients/families (early contact, named liaison, updates, draft review, access to final report) — Gap
  - Staff (psychological support, Just Culture, protection from blame) — Gap
  - Community (thematic issues) — Gap

- **Board oversight:**
  - Named executive lead for patient safety — Gap
  - Quarterly reports on safety themes and learning — Gap
  - PSIRP board sign-off — Gap
  - LFPSE integration — Partial via GV.SG-11 Adverse Event / Incident Rate (LFPSE)

- **Differences from old SI Framework:** PSIRF moves from blame-based RCA to systems thinking; from prescribed investigations to proportionate response; from transactional commissioner sign-off to supportive ICB/NHSE oversight. The taxonomy's existing incident metrics (GV.SG-11, GV.SG-14) capture that an incident occurred but not the organisation's systems-learning response.

**Overall position:** PSIRF complements DCB0129 Stage 7 Incident Management (already mapped). DCB0129 is about documenting the technical safety lifecycle; PSIRF is about organisation-level systems learning from live incidents. The taxonomy captures incident occurrence (GV.SG-11 LFPSE, GV.SG-14 Near-Miss Reporting Rate) and technical attribution (PI.E2E-8 Error Attribution Analysis) but not the PSIRF-required engagement, learning, and oversight responses. This is the clearest governance gap in the existing taxonomy.

**Gaps:**
- Systems-based root cause analysis readiness (SEIPS-informed)
- Compassionate engagement with affected patients/families
- Staff support and Just Culture protection
- Learning implementation tracking (did the learning actually change practice?)
- Board-level patient safety reporting on AI incidents
- Proportionate response type selection (when is AAR appropriate vs PSII?)

---

### PRSB Clinical Documentation Standards

**Publisher:** Professional Record Standards Body (community interest company, endorsed by Royal Colleges)
**Scope:** Semantic structure of clinical records — what information must be recorded and how it relates. Distinct from FHIR/openEHR which define technical transport.
**Mandatory status:** Increasingly expected for NHS-commissioned systems; referenced in NHS Standard Contract. Not yet formally mandatory but becoming de facto standard.
**AVT relevance:** AVT systems generating clinical notes must map their outputs to PRSB structures to ensure interoperability and clinical completeness. PRSB defines the "what" (mandatory information elements); FHIR UK Core defines the "how" (wire format).

**Key dimensions and taxonomy coverage:**

- **Main PRSB standards:**
  - Core Information Standard (CIS) — foundational; gap (no semantic-completeness metric)
  - GP Connect Access Record — gap
  - Outpatient Letter Standard — gap
  - Discharge Summary Standard — gap
  - Mental Health Inpatient Discharge Summary — gap
  - Emergency Care Discharge Summary — gap
  - Transfer of Care Around Medicines (ToCAM) — partial via TP.SN-19 Medication Attribute Extraction F1, TP.SN-21 Medication Event Classification
  - About Me — gap
  - End of Life Care — gap
  - Maternity Record Standard — gap
  - Palliative and End of Life Care — gap

- **Common header set (across standards):**
  - Patient demographics + NHS Number — covered by TP.WB-3 Field Mapping Accuracy
  - Allergies and adverse reactions — covered by TP.WB-1 Write-back Fidelity (specifically flagged), TP.WB-4 Update vs Append Behaviour
  - Medications (current, changes, reason) — covered by TP.SN-19 Medication Attribute Extraction F1, TP.SN-21 Medication Event Classification, TP.CC-5 dm+d Medication Coding Accuracy
  - Problems / diagnoses (SNOMED) — covered by TP.CC-1 SNOMED Code Accuracy, TP.CC-2 SNOMED CT Concept Mapping Accuracy
  - Procedures (OPCS) — covered by TP.CC-4 OPCS-4 Procedure Coding Accuracy
  - Observations / vital signs — partial via TP.WB-3 Field Mapping Accuracy
  - Communication needs (AIS flags, interpreter needs) — gap
  - Consent and preferences — partial via GV.PD-8 Consent Verification Accuracy
  - Legal status (MHA, DoLS, LPA, advance decisions) — gap
  - Clinical narrative (history, examination, assessment, plan) — partial via TP.SN-5 Hallucination Rate, TP.SN-6 Omission Rate, TP.SN-20 Uncertainty Marker Preservation
  - Safety netting — gap

- **Narrative vs structured trade-off:** PRSB explicitly preserves narrative text as valuable and does not mandate full structurisation. The taxonomy captures aspects of this — TP.SN-22 Style & Format Consistency, TP.SN-23 Length Appropriateness — but not the narrative-preservation-vs-structurisation trade-off directly. An AVT that over-structures at the expense of narrative fails the PRSB spirit; an AVT that preserves narrative but fails to populate required coded fields also fails.

- **Cardinality (Mandatory / Required-if-known / Optional):** Every data item in a PRSB standard has cardinality. The taxonomy has no metric for "is mandatory information present in the AVT output?"

- **Royal College endorsement:** AoMRC, RCGP, RCP, RCS, RCEM, RCPsych, RCPCH, RCOG, RCR, RCPath, RCA, RCN, RPS, AHP federation, patient groups. Process criterion, no metric.

- **Relationship to FHIR UK Core:** PRSB data items are explicitly mapped to FHIR UK Core resources/elements in published mapping tables. TP.WB-6 FHIR R4 Resource Conformance Rate partially covers this, but conformance to the wire format doesn't guarantee PRSB semantic completeness.

**Overall position:** PRSB is the clearest gap across all seven new standards. The taxonomy has strong technical integration metrics (TP.WB-1 Write-back Fidelity, TP.WB-3 Field Mapping Accuracy, TP.WB-6 FHIR R4 Resource Conformance) and strong content fidelity metrics (TP.SN-5 Hallucination, TP.SN-6 Omission) but no metric for "does the AVT output include all PRSB-mandatory information elements for the applicable standard?" A PRSB-aware AVT should be able to report per-standard compliance (CIS, Outpatient Letter, Discharge Summary, etc.) as a procurement signal.

**Gaps:**
- PRSB semantic completeness per standard (CIS, Outpatient Letter, Discharge, ToCAM)
- Mandatory information element coverage
- Professional narrative preservation (narrative vs over-structurisation trade-off)
- Communication needs (AIS) information capture
- Legal status information capture (MHA, DoLS, advance decisions)
- Safety netting information capture

---

### Caldicott Principles (2020 revision)

**Publisher:** National Data Guardian (originally Caldicott Report 1997; 2020 revision added Principle 8)
**Scope:** Eight principles governing the use of confidential patient information. Foundational to NHS information governance and the legal basis for DSPT operationalisation.
**Mandatory status:** Not statutory but operationalised through Common Law Duty of Confidentiality, UK GDPR, CQC Regulation 17, and DSPT. Every NHS organisation must have a Caldicott Guardian (mandatory since 1999).
**AVT relevance:** Each Caldicott principle has a direct AVT application — purpose justification in DPIA, minimum necessary data processing, Principle 8 inform-patient obligation mapping to verbal notification and dissent recording.

**Key dimensions and taxonomy coverage:**

- **Principle 1 — Justify the purpose(s)**: Partial — GV.CR-7 DPIA Template Completion Rate evidences purpose documentation, but "justify" is judgement-based. Gap: DPIA justification quality metric.

- **Principle 2 — Use confidential information only when it is necessary**: Partial — GV.PD-4 Data Minimisation Score partially addresses this. Gap: "necessity" judgement metric for AVT processing of specific consultation types (e.g. should AVT be used for safeguarding or mental health consultations?).

- **Principle 3 — Use the minimum necessary confidential information**: Partial — GV.PD-4 Data Minimisation Score addresses aggregate minimisation. Gap: per-data-item necessity documentation.

- **Principle 4 — Access on a strict need-to-know basis**: Covered by GV.VT-7 Sub-Processor Transparency, GV.SC-9 Cross-Patient Information Leakage Rate, GV.VT-4 Audit Trail Completeness.

- **Principle 5 — Everyone aware of their responsibilities**: Covered by GV.TC-1 Clinician Training Completion Rate, GV.TC-2 Failure Mode Awareness Score, GV.TC-3 Refresher Training & CPD Compliance.

- **Principle 6 — Comply with the law**: Covered by GV.CR-6 Clinical Safety Case Completeness, GV.CR-7 DPIA Template Completion Rate, GV.PD-9 Cross-Border Data Transfer Compliance, GV.PD-10 Subject Access Request Fulfilment, GV.PD-11 Right to Erasure Compliance.

- **Principle 7 — Duty to share for individual care**: Covered by TP.WB-1 Write-back Fidelity (ensures generated records flow into EPR for continuity of care), TP.WB-2 Integration Error Rate. The principle is that "AI-generated" is not an excuse to withhold information — the taxonomy ensures the information flows correctly.

- **Principle 8 — Inform patients and service users** *(added 2020)*: Directly covered by GV.CR-1 Patient Dissent Recording Rate, GV.CR-2 Verbal Notification Compliance, GV.CR-3 AI-Generated Content Labelling Compliance, IO.PX-1 Patient Opt-Out Rate. This is the clearest direct mapping between a Caldicott principle and existing taxonomy metrics.

- **Caldicott Guardian role:** Senior person in every NHS organisation, UKCGC-trained, advises on complex IG decisions, represents confidentiality at board level. Distinct from DPO (statutory UK GDPR role) and SIRO (risk ownership). Process role, no metric for Guardian's AI-specific engagement.

- **Relationship to UK GDPR and Common Law Duty of Confidentiality**: Three overlapping regimes. UK GDPR lawful basis does not automatically satisfy the Common Law Duty of Confidentiality; both must be met. Caldicott operationalises the CLDC inside health and care. Existing DSPT mapping covers the statutory floor; Caldicott is the ethical/professional framework on top.

- **National Data Guardian role:** Statutory (Health and Social Care (National Data Guardian) Act 2018). Publishes guidance with "have regard to" obligation. Publications directly relevant: 2020 Caldicott Principles, NDG Data Security Standards (underpin DSPT), public benefit test.

**Overall position:** Caldicott is largely operationalised by DSPT (already mapped). This section makes the strategic governance layer explicit for readers who come from an IG/ethics perspective rather than an operational security one. Principle 8 is the strongest direct mapping to existing metrics; Principles 4–7 are well covered; Principles 1–3 have partial coverage because judgement-based "justification" and "necessity" don't reduce to single metrics.

**Gaps:**
- DPIA justification quality under Principle 1
- Consultation-type appropriateness under Principle 2 (e.g. AVT in safeguarding/MH consultations)
- Per-data-item necessity documentation under Principle 3
- Caldicott Guardian AI-specific engagement (review of AVT deployment by the Guardian)

---

### Gap Summary

Gaps where the taxonomy has no coverage against a standard's requirements:

| Gap | Relevant Standard(s) | Severity |
|-----|----------------------|----------|
| **Web accessibility (WCAG 2.2 AA)** | DTAC D1.4.1 | Low — UI concern, not clinical AI pipeline |
| **Accessible Information Standard** | DTAC D1.3 | Low — UI concern, not clinical AI pipeline |
| **Total cost of ownership / cost-effectiveness** | LLM Framework (Cost) | Medium — relevant to deployment decisions |
| **Benchmark relevance decay** | LLM Framework (Benchmark relevance) | Medium — implicit in Meta-evaluation but not explicit |
| **Scalability / concurrency testing** | LLM Framework (Scalability) | Medium — partially covered by latency and uptime |
| **SME involvement depth** | LLM Framework (SME involvement) | Low — taxonomy assigns Responsible Actors but doesn't quantify SME engagement |
| **Few-shot prompt bias** | LLM Framework (Bias — in-context learning) | Low — not applicable to pipeline-based AVT systems |
| **Structured staff feedback mechanism** | LLM Framework (Feedback mechanism) | Low — partially covered by incident reporting |
| **Job security / workforce impact** | LLM Framework (Society) | Low — partially covered by skill attenuation metrics |

Gaps where the taxonomy provides coverage that no standard addresses:

| Taxonomy Coverage | Notes |
|-------------------|-------|
| Audio capture pipeline (9 metrics) | No standard addresses audio quality assurance |
| ASR accuracy and equity (14 metrics) | No standard addresses speech recognition quality |
| Diarisation (9 metrics) | No standard addresses speaker attribution |
| Clinical content fidelity family (5 metrics) | No standard addresses hallucination/omission in clinical AI |
| Post-generation correction family (4 metrics) | No standard addresses human-AI interaction in clinical documentation |
| EPR write-back safety sub-cluster (4 metrics) | DTAC addresses interoperability but not write-back safety semantics |
| Medication Safety Thread family (4 metrics) | No standard addresses medication accuracy across the AI pipeline |
| Meta-evaluation (7 metrics) | No standard addresses measurement science quality |
