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
