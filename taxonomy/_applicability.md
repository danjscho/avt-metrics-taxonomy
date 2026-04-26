## Applicability Classification

This section classifies each metric by whether it is specific to Ambient Voice Technology (AVT) or applicable to healthcare AI systems more broadly. The classification helps readers identify which parts of the taxonomy are transferable to other clinical AI contexts (diagnostic imaging AI, predictive analytics, clinical decision support) and which are meaningful only in the context of an audio-to-clinical-record pipeline.

### Classification Values

- **AVT-Specific** - the metric is meaningful only in the context of an audio capture, speech recognition, or speaker attribution pipeline. Removing the audio layer removes the need for the metric entirely. *Example: Signal-to-Noise Ratio Monitoring measures audio input quality - irrelevant to a text-based clinical AI system.*

- **General Healthcare AI** - the metric applies to any clinical AI system regardless of input modality. The definition, measurement method, and assurance question are independent of whether the system processes audio, text, images, or structured data. *Example: Consent Verification Accuracy applies equally to an ambient scribe, a diagnostic imaging AI, or an EHR predictive model.*

- **AVT-Contextualised** - the underlying concept is general (applicable to any clinical AI) but the specific definition, threshold, or measurement method in this taxonomy is tuned for AVT. Adapting the metric to another modality would require redefining the formal definition while preserving the assurance question. *Example: Hallucination Rate measures fabricated content in AI output - a general concern - but the formal definition here references transcript-to-note fidelity, speaker attribution errors, and audio-derived confabulation, which are AVT-specific failure modes.*

### Summary

| Classification | Count | Percentage |
|----------------|-------|------------|
| AVT-Specific | 50 | 23% |
| AVT-Contextualised | 77 | 35% |
| General Healthcare AI | 91 | 42% |
| **Total** | **218** | **100%** |

### By Part

| Part | AVT-Specific | AVT-Contextualised | General Healthcare AI | Total |
|------|-------------|--------------------|--------------------|-------|
| A - Technical Pipeline | 33 | 41 | 0 | 74 |
| B - Pipeline Interactions | 8 | 13 | 0 | 21 |
| C - The Human Layer | 0 | 16 | 3 | 19 |
| D - Impact & Outcomes | 1 | 6 | 11 | 18 |
| E - System Governance | 8 | 1 | 68 | 77 |
| F - Evaluation Science | 0 | 0 | 9 | 9 |
| **Total** | **50** | **77** | **91** | **218** |


### Full Classification

#### Part A - The Technical Pipeline

**Audio Capture & Environment** (9 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| TP.AC-1 | Signal-to-Noise Ratio (SNR) Monitoring | 🟡 Tier 2 | AVT-Specific |
| TP.AC-2 | Voice Activity Detection (VAD) Accuracy | 🔵 Tier 3 | AVT-Specific |
| TP.AC-3 | Acoustic Environment Profiling | 🟡 Tier 2 | AVT-Specific |
| TP.AC-4 | Bystander Voice Detection Rate | 🔵 Tier 3 | AVT-Specific |
| TP.AC-5 | Microphone & Hardware Validation | 🟢 Tier 1 | AVT-Specific |
| TP.AC-6 | Speaker Overlap Rate | 🔵 Tier 3 | AVT-Specific |
| TP.AC-7 | Audio Clipping / Saturation Rate | 🟡 Tier 2 | AVT-Specific |
| TP.AC-8 | Codec & Sampling Rate Compliance | 🟡 Tier 2 | AVT-Specific |
| TP.AC-9 | Microphone Drift Detection | 🔵 Tier 3 | AVT-Specific |

**ASR / Transcription** (14 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| TP.ASR-1 | Word Error Rate (WER) | 🟡 Tier 2 | AVT-Specific |
| TP.ASR-2 | Medical Word Error Rate (M-WER) | 🔵 Tier 3 | AVT-Specific |
| TP.ASR-3 | Clinical Keyword Error Rate (CK-ER) | 🔵 Tier 3 | AVT-Specific |
| TP.ASR-4 | Demographic-Disaggregated WER | 🟡 Tier 2 | AVT-Specific |
| TP.ASR-5 | Speaker-Stratified WER | 🔵 Tier 3 | AVT-Specific |
| TP.ASR-6 | Error Transmission Rate | 🟡 Tier 2 | AVT-Specific |
| TP.ASR-7 | Real-Time Factor (RTF) | 🟡 Tier 2 | AVT-Specific |
| TP.ASR-8 | Character Error Rate (CER) | 🟡 Tier 2 | AVT-Specific |
| TP.ASR-9 | Out-of-Vocabulary (OOV) Rate | 🟡 Tier 2 | AVT-Specific |
| TP.ASR-10 | ASR Confidence Calibration | 🟡 Tier 2 | AVT-Specific |
| TP.ASR-11 | ASR Confidence Exposure | 🟡 Tier 2 | AVT-Specific |
| TP.ASR-12 | Hallucination-Under-Noise Rate | 🟢 Tier 1 | AVT-Specific |
| TP.ASR-13 | Numeric Accuracy | 🟢 Tier 1 | AVT-Specific |
| TP.ASR-14 | Punctuation & Capitalisation Accuracy | 🔵 Tier 3 | AVT-Specific |

**Diarisation** (9 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| TP.DI-1 | Diarisation Error Rate (DER) | 🟡 Tier 2 | AVT-Specific |
| TP.DI-2 | Speaker Attribution Accuracy | 🟡 Tier 2 | AVT-Specific |
| TP.DI-3 | Speaker Count Accuracy | 🟡 Tier 2 | AVT-Specific |
| TP.DI-4 | Speaker Boundary Precision | 🔵 Tier 3 | AVT-Specific |
| TP.DI-5 | Speaker Role Identification F1 | 🟡 Tier 2 | AVT-Specific |
| TP.DI-6 | Code-Switching Detection Rate | 🟡 Tier 2 | AVT-Specific |
| TP.DI-7 | Turn-Taking Accuracy in Overlap | 🟡 Tier 2 | AVT-Specific |
| TP.DI-8 | Clinical-Perspective HEWER (cpHEWER) | 🔵 Tier 3 | AVT-Specific |
| TP.DI-9 | Addressee Recognition Accuracy | 🔵 Tier 3 | AVT-Specific |

**Summarisation / NLP** (24 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| TP.SN-1 | ROUGE Scores | 🟡 Tier 2 | AVT-Contextualised |
| TP.SN-2 | BERTScore | 🔵 Tier 3 | AVT-Contextualised |
| TP.SN-3 | PDSQI-9 (Physician Documentation Quality Instrument) | 🟡 Tier 2 | AVT-Contextualised |
| TP.SN-4 | CREOLA Error Taxonomy Scores | 🟡 Tier 2 | AVT-Contextualised |
| TP.SN-5 | Hallucination Rate | 🟢 Tier 1 | AVT-Contextualised |
| TP.SN-6 | Omission Rate | 🟢 Tier 1 | AVT-Contextualised |
| TP.SN-7a | Confabulation Detection (Support × Severity) | 🔵 Tier 3 | AVT-Contextualised |
| TP.SN-7b | VeriFact Factual Verification | 🔵 Tier 3 | AVT-Contextualised |
| TP.SN-9a | LLM-as-a-Judge (PDSQI-9 Proxy) | 🟡 Tier 2 | AVT-Contextualised |
| TP.SN-9b | MedHELM LLM-Jury | 🔵 Tier 3 | AVT-Contextualised |
| TP.SN-11 | MEDIC Cross-Examination | 🔵 Tier 3 | AVT-Contextualised |
| TP.SN-12 | Linked Evidence / Provenance Tracing | 🟡 Tier 2 | AVT-Contextualised |
| TP.SN-13 | SCRIBE Framework Composite | 🔵 Tier 3 | AVT-Specific |
| TP.SN-14 | Template Modification Underspecification Score | 🟡 Tier 2 | AVT-Contextualised |
| TP.SN-15 | Negation Handling Accuracy | 🟢 Tier 1 | AVT-Contextualised |
| TP.SN-16 | Temporal Accuracy | 🟡 Tier 2 | AVT-Contextualised |
| TP.SN-17 | Temporal Event Ordering Accuracy | 🟡 Tier 2 | AVT-Contextualised |
| TP.SN-18 | Quantifier Preservation | 🟡 Tier 2 | AVT-Contextualised |
| TP.SN-19 | Medication Attribute Extraction F1 | 🟡 Tier 2 | AVT-Contextualised |
| TP.SN-20 | Uncertainty Marker Preservation | 🟢 Tier 1 | AVT-Contextualised |
| TP.SN-21 | Medication Event Classification | 🟡 Tier 2 | AVT-Contextualised |
| TP.SN-22 | Style & Format Consistency | 🔵 Tier 3 | AVT-Contextualised |
| TP.SN-23 | Length Appropriateness | 🔵 Tier 3 | AVT-Contextualised |
| TP.SN-24 | Stigmatising Language Replication Rate | 🟡 Tier 2 | AVT-Contextualised |

**Clinical Coding** (11 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| TP.CC-1 | SNOMED Code Accuracy | 🟡 Tier 2 | AVT-Contextualised |
| TP.CC-2 | SNOMED CT Concept Mapping Accuracy | 🟡 Tier 2 | AVT-Contextualised |
| TP.CC-3 | ICD-10 / ICD-11 Full-Specificity Precision | 🟡 Tier 2 | AVT-Contextualised |
| TP.CC-4 | OPCS-4 Procedure Coding Accuracy | 🟡 Tier 2 | AVT-Contextualised |
| TP.CC-5 | dm+d Medication Coding Accuracy | 🟡 Tier 2 | AVT-Contextualised |
| TP.CC-6 | Code Hallucination Rate | 🟢 Tier 1 | AVT-Contextualised |
| TP.CC-7 | Coding Drift Detection | 🟡 Tier 2 | AVT-Contextualised |
| TP.CC-9 | Coding Equity Index | 🟡 Tier 2 | AVT-Contextualised |
| TP.CC-10 | HRG / Tariff Impact Attribution | 🔵 Tier 3 | AVT-Contextualised |
| TP.CC-11 | Code Specificity Index | 🔵 Tier 3 | AVT-Contextualised |
| TP.CC-12 | Code Suggestion Latency | 🔵 Tier 3 | AVT-Contextualised |

**EPR Write-back** (7 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| TP.WB-1 | Write-back Fidelity | 🟢 Tier 1 | AVT-Contextualised |
| TP.WB-2 | Integration Error Rate | 🟢 Tier 1 | AVT-Contextualised |
| TP.WB-3 | Field Mapping Accuracy | 🟢 Tier 1 | AVT-Contextualised |
| TP.WB-4 | Update vs Append Behaviour | 🟢 Tier 1 | AVT-Contextualised |
| TP.WB-5 | Write-back Rollback Capability | 🟡 Tier 2 | AVT-Contextualised |
| TP.WB-6 | FHIR R4 Resource Conformance Rate | 🟡 Tier 2 | AVT-Contextualised |
| TP.WB-7 | openEHR Archetype Conformance | 🔵 Tier 3 | AVT-Contextualised |

#### Part B - Pipeline Interactions

**Partial-Pipeline** (9 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| PI.PP-1 | Speaker-Attributed Transcript Accuracy | 🔵 Tier 3 | AVT-Specific |
| PI.PP-2 | Multi-Party Conversation Robustness | 🟡 Tier 2 | AVT-Specific |
| PI.PP-3 | Information Extraction Yield | 🔵 Tier 3 | AVT-Contextualised |
| PI.PP-4 | Noise-to-Note Resilience | 🔵 Tier 3 | AVT-Specific |
| PI.PP-5 | Epistemic Status Preservation | 🔵 Tier 3 | AVT-Contextualised |
| PI.PP-6 | Diarisation-Stratified WER | 🔵 Tier 3 | AVT-Specific |
| PI.PP-7 | Concept Extraction Concordance | 🟡 Tier 2 | AVT-Contextualised |
| PI.PP-8 | End-of-Utterance Timing Accuracy | 🔵 Tier 3 | AVT-Specific |
| PI.PP-9 | Structured/Free-Text Consistency | 🟡 Tier 2 | AVT-Contextualised |

**End-to-End Pipeline** (12 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| PI.E2E-1 | Source-to-Record Concordance | 🔵 Tier 3 | AVT-Contextualised |
| PI.E2E-2 | Cumulative Information Yield | 🔵 Tier 3 | AVT-Contextualised |
| PI.E2E-3 | Error Propagation / Cascade Analysis | 🔵 Tier 3 | AVT-Specific |
| PI.E2E-4 | Safety-Critical Information Chain of Custody | 🟡 Tier 2 | AVT-Contextualised |
| PI.E2E-5 | Compound Demographic Performance | 🔵 Tier 3 | AVT-Contextualised |
| PI.E2E-6 | Semantic Drift Accumulation | 🔵 Tier 3 | AVT-Specific |
| PI.E2E-7 | Pipeline Non-Determinism / Reproducibility | 🟡 Tier 2 | AVT-Contextualised |
| PI.E2E-8 | Error Attribution Analysis | 🔵 Tier 3 | AVT-Contextualised |
| PI.E2E-9 | Clinical Decision Equivalence | 🔵 Tier 3 | AVT-Contextualised |
| PI.E2E-10 | Full-Pipeline Latency Budget | 🟡 Tier 2 | AVT-Contextualised |
| PI.E2E-11 | Pipeline Failure Recovery | 🟡 Tier 2 | AVT-Contextualised |
| PI.E2E-12 | Round-Trip Information Loss | 🔵 Tier 3 | AVT-Specific |

#### Part C - The Human Layer

**Human Factors & Workflow** (19 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| HL.HF-1 | Edit Rate (% Notes Edited) | 🟢 Tier 1 | AVT-Contextualised |
| HL.HF-2 | Edit Type Classification | 🟡 Tier 2 | AVT-Contextualised |
| HL.HF-3a | Review-Before-Signing Rate | 🟢 Tier 1 | AVT-Contextualised |
| HL.HF-3b | Time-to-Sign Distribution | 🟢 Tier 1 | AVT-Contextualised |
| HL.HF-5 | Edit-Pattern Monitoring at Scale | 🔵 Tier 3 | AVT-Contextualised |
| HL.HF-6 | Automation Bias Detection (Error Injection) | 🟡 Tier 2 | AVT-Contextualised |
| HL.HF-7 | Edit Location Distribution | 🟡 Tier 2 | AVT-Contextualised |
| HL.HF-8 | Trust Calibration Survey | 🟡 Tier 2 | AVT-Contextualised |
| HL.HF-9 | Re-record / Abandonment Rate | 🟡 Tier 2 | AVT-Contextualised |
| HL.HF-10 | Cognitive Load Assessment | 🔵 Tier 3 | AVT-Contextualised |
| HL.HF-11 | Inter-Clinician Edit Variance | 🔵 Tier 3 | AVT-Contextualised |
| HL.HF-12 | Clinical Documentation Skill Attenuation | 🔵 Tier 3 | AVT-Contextualised |
| HL.HF-13 | Cognitive Offloading Rate | 🔵 Tier 3 | AVT-Contextualised |
| HL.HF-14 | Trust Halo Decay Rate | 🔵 Tier 3 | AVT-Contextualised |
| HL.HF-15 | Note Review Fatigue Trajectory | 🔵 Tier 3 | AVT-Contextualised |
| HL.HF-16 | Work-as-Imagined vs Work-as-Done Gap | 🔵 Tier 3 | General Healthcare AI |
| HL.HF-17 | Verification Burden | 🟡 Tier 2 | AVT-Contextualised |
| HL.HF-18 | Resilience Capacities Assessment | 🔵 Tier 3 | General Healthcare AI |
| HL.HF-19 | AI-Off Performance Test | 🟡 Tier 2 | General Healthcare AI |


#### Part D - Impact & Outcomes

**Patient Experience** (10 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| IO.PX-1 | Patient Opt-Out Rate | 🟢 Tier 1 | AVT-Contextualised |
| IO.PX-2 | Patient-Perceived Accuracy | 🔵 Tier 3 | AVT-Contextualised |
| IO.PX-3 | Emotional Content Preservation | 🔵 Tier 3 | AVT-Contextualised |
| IO.PX-4 | Cultural & Linguistic Appropriateness | 🔵 Tier 3 | General Healthcare AI |
| IO.PX-5 | Chilling Effect Assessment | 🔵 Tier 3 | AVT-Contextualised |
| IO.PX-6 | Therapeutic Relationship Impact | 🔵 Tier 3 | AVT-Contextualised |
| IO.PX-7 | Full Attentiveness Rate | 🟡 Tier 2 | AVT-Contextualised |
| IO.PX-8 | Patient Comprehension of AI-Generated Summaries | 🔵 Tier 3 | General Healthcare AI |
| IO.PX-9 | Downstream Diagnostic Accuracy | 🔵 Tier 3 | General Healthcare AI |
| IO.PX-10 | Medication Error Rate Differential | 🔵 Tier 3 | General Healthcare AI |

**Fairness & Equity** (8 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| IO.FE-1 | Deployment Equity Index | 🟡 Tier 2 | General Healthcare AI |
| IO.FE-2 | Accent Taxonomy Standardisation | 🟡 Tier 2 | AVT-Specific |
| IO.FE-3 | Clinical Domain Performance Variance | 🟡 Tier 2 | General Healthcare AI |
| IO.FE-4 | Intersectional Performance | 🔵 Tier 3 | General Healthcare AI |
| IO.FE-5 | Intersectional Compound Fairness Score | 🔵 Tier 3 | General Healthcare AI |
| IO.FE-6 | Rare Presentation Handling | 🔵 Tier 3 | General Healthcare AI |
| IO.FE-7 | Health Literacy Performance Variation | 🔵 Tier 3 | General Healthcare AI |
| IO.FE-8 | Cross-Platform Fairness Consistency | 🔵 Tier 3 | General Healthcare AI |

#### Part E - System Governance

**Safety & Governance** (17 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| GV.SG-1 | Model Version Tracking | 🟢 Tier 1 | General Healthcare AI |
| GV.SG-2 | Model Update Impact Score | 🟡 Tier 2 | General Healthcare AI |
| GV.SG-3 | Performance Degradation Detection Latency | 🟡 Tier 2 | General Healthcare AI |
| GV.SG-4 | Retraining Trigger Threshold Specification | 🟡 Tier 2 | General Healthcare AI |
| GV.SG-5 | AI-Generated Data Contamination Rate | 🔵 Tier 3 | General Healthcare AI |
| GV.SG-6 | Concept Drift in Clinical Notes | 🔵 Tier 3 | General Healthcare AI |
| GV.SG-7 | Probabilistic Risk Quantification (P₁/P₂) | 🔵 Tier 3 | General Healthcare AI |
| GV.SG-8 | DeepScore (Defect-Free Rate) | 🔵 Tier 3 | General Healthcare AI |
| GV.SG-9 | Safety Performance Indicators with Thresholds (DSCMS) | 🟢 Tier 1 | General Healthcare AI |
| GV.SG-10 | Off-Label Use Detection Rate | 🟡 Tier 2 | General Healthcare AI |
| GV.SG-11 | Adverse Event / Incident Rate (LFPSE) | 🟢 Tier 1 | General Healthcare AI |
| GV.SG-12 | Cross-Practice Variance Coefficient | 🟡 Tier 2 | General Healthcare AI |
| GV.SG-13 | Assurance Debt Accumulation Rate | 🟢 Tier 1 | General Healthcare AI |
| GV.SG-14 | Near-Miss Reporting Rate | 🟢 Tier 1 | General Healthcare AI |
| GV.SG-15 | Time-to-Correct | 🟡 Tier 2 | General Healthcare AI |
| GV.SG-16 | SPI Escalation Response Time | 🟡 Tier 2 | General Healthcare AI |
| GV.SG-17 | Hazard Log Completeness | 🟢 Tier 1 | General Healthcare AI |

**NHS Compliance & Regulatory** (10 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| GV.CR-1 | Patient Dissent Recording Rate | 🟢 Tier 1 | General Healthcare AI |
| GV.CR-2 | Verbal Notification Compliance | 🟢 Tier 1 | General Healthcare AI |
| GV.CR-3 | AI-Generated Content Labelling Compliance | 🟢 Tier 1 | General Healthcare AI |
| GV.CR-4 | AVT Supplier Registry Listing Verification | 🟢 Tier 1 | AVT-Specific |
| GV.CR-5 | ICB Engagement Documentation | 🟢 Tier 1 | General Healthcare AI |
| GV.CR-6 | Clinical Safety Case Completeness | 🟢 Tier 1 | General Healthcare AI |
| GV.CR-7 | DPIA Template Completion Rate | 🟢 Tier 1 | General Healthcare AI |
| GV.CR-8 | DSPA Status | 🟡 Tier 2 | General Healthcare AI |
| GV.CR-9 | FDA PCCP-Equivalent Pre-Defined Acceptance Criteria | 🟡 Tier 2 | General Healthcare AI |
| GV.CR-10 | EU AI Act Event Logging Compliance | 🟡 Tier 2 | General Healthcare AI |

**Security & Adversarial Robustness** (12 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| GV.SC-1 | Prompt Injection Resistance Rate | 🟡 Tier 2 | General Healthcare AI |
| GV.SC-2 | Jailbreak Resistance Score | 🟡 Tier 2 | General Healthcare AI |
| GV.SC-3 | Adversarial Audio Detection Rate | 🔵 Tier 3 | AVT-Specific |
| GV.SC-4 | Data Poisoning Resilience | 🔵 Tier 3 | General Healthcare AI |
| GV.SC-5 | Output Safety Classifier Coverage | 🟡 Tier 2 | General Healthcare AI |
| GV.SC-6 | Template Injection Vulnerability Assessment | 🟡 Tier 2 | General Healthcare AI |
| GV.SC-7 | Voice Cloning / Deepfake Detection | 🔵 Tier 3 | AVT-Specific |
| GV.SC-8 | Side-Channel Data Leakage | 🟡 Tier 2 | General Healthcare AI |
| GV.SC-9 | Cross-Patient Information Leakage Rate | 🟡 Tier 2 | General Healthcare AI |
| GV.SC-10 | Clinician Identity Authentication | 🟡 Tier 2 | General Healthcare AI |
| GV.SC-11 | Membership Inference Attack AUC | 🔵 Tier 3 | General Healthcare AI |
| GV.SC-12 | Cyber Essentials Plus Certification Status | 🟡 Tier 2 | AVT-Contextualised |

**Privacy & Data Governance** (11 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| GV.PD-1 | Audio Retention Compliance | 🟢 Tier 1 | AVT-Specific |
| GV.PD-2 | Audio Time-to-Deletion | 🟢 Tier 1 | AVT-Specific |
| GV.PD-3 | Transcript Retention Compliance | 🟢 Tier 1 | AVT-Specific |
| GV.PD-4 | Data Minimisation Score | 🟡 Tier 2 | General Healthcare AI |
| GV.PD-5 | PII Extraction Attack Success Rate | 🟡 Tier 2 | General Healthcare AI |
| GV.PD-6 | Re-identification Risk Assessment | 🟡 Tier 2 | General Healthcare AI |
| GV.PD-7 | Training Data Inclusion Status | 🟡 Tier 2 | General Healthcare AI |
| GV.PD-8 | Consent Verification Accuracy | 🟢 Tier 1 | General Healthcare AI |
| GV.PD-9 | Cross-Border Data Transfer Compliance | 🟢 Tier 1 | General Healthcare AI |
| GV.PD-10 | Subject Access Request Fulfilment | 🟢 Tier 1 | General Healthcare AI |
| GV.PD-11 | Right to Erasure Compliance | 🟢 Tier 1 | General Healthcare AI |

**Operational** (9 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| GV.OP-1 | Documentation Time per Consultation | 🟢 Tier 1 | General Healthcare AI |
| GV.OP-2 | Pyjama Time / After-Hours EHR Use | 🟡 Tier 2 | General Healthcare AI |
| GV.OP-3 | Note Turnaround Time | 🟡 Tier 2 | General Healthcare AI |
| GV.OP-4 | Documentation Workload Composite | 🟡 Tier 2 | General Healthcare AI |
| GV.OP-5 | System Availability / Uptime | 🟢 Tier 1 | General Healthcare AI |
| GV.OP-6 | Adoption Rate & Selective Use Patterns | 🟢 Tier 1 | General Healthcare AI |
| GV.OP-7 | Cost per Consultation | 🟡 Tier 2 | General Healthcare AI |
| GV.OP-8 | Governance & Maintenance Burden | 🔵 Tier 3 | General Healthcare AI |
| GV.OP-9 | Training Time per Clinician | 🟡 Tier 2 | General Healthcare AI |

**Environmental & Sustainability** (3 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| GV.EN-1 | Energy Consumption per Clinical Note | 🔵 Tier 3 | General Healthcare AI |
| GV.EN-2 | Carbon Emissions per Inference | 🔵 Tier 3 | General Healthcare AI |
| GV.EN-3 | Water Consumption per Query | 🔵 Tier 3 | General Healthcare AI |

**Training & Competency** (5 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| GV.TC-1 | Clinician Training Completion Rate | 🟢 Tier 1 | General Healthcare AI |
| GV.TC-2 | Failure Mode Awareness Score | 🟡 Tier 2 | General Healthcare AI |
| GV.TC-3 | Refresher Training & CPD Compliance | 🟡 Tier 2 | General Healthcare AI |
| GV.TC-4 | Trainee Impact Assessment | 🔵 Tier 3 | General Healthcare AI |
| GV.TC-5 | Training Material Currency | 🟡 Tier 2 | General Healthcare AI |

**Vendor Transparency & Contractual** (10 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| GV.VT-1 | Model Change Notification Compliance | 🟢 Tier 1 | General Healthcare AI |
| GV.VT-2 | Telemetry Provision Completeness | 🟡 Tier 2 | General Healthcare AI |
| GV.VT-3 | Benchmark & Evaluation Data Accessibility | 🔵 Tier 3 | General Healthcare AI |
| GV.VT-4 | Audit Trail Completeness | 🟡 Tier 2 | General Healthcare AI |
| GV.VT-5 | Incident Disclosure Compliance | 🟢 Tier 1 | General Healthcare AI |
| GV.VT-6 | Exit & Data Portability Provisions | 🟡 Tier 2 | General Healthcare AI |
| GV.VT-7 | Sub-Processor Transparency | 🟢 Tier 1 | General Healthcare AI |
| GV.VT-8 | Intermediate Output Access | 🟡 Tier 2 | General Healthcare AI |
| GV.VT-13 | Evidence Pack Freshness | 🟡 Tier 2 | AVT-Specific |
| GV.VT-14 | Indicative Pricing Transparency | 🟡 Tier 2 | AVT-Specific |

#### Part F - Evaluation Science

**Meta-evaluation** (9 metrics)

| Ref | Metric | Tier | Applicability |
|-----|--------|------|---------------|
| ES.ME-1 | Proximal vs Distal Outcome Distinction | 🔵 Tier 3 | General Healthcare AI |
| ES.ME-2 | Inter-Rater Reliability Baseline | 🔵 Tier 3 | General Healthcare AI |
| ES.ME-3 | Metric Interaction Analysis | 🔵 Tier 3 | General Healthcare AI |
| ES.ME-4 | Goodhart's Law Monitoring | 🟡 Tier 2 | General Healthcare AI |
| ES.ME-5 | Coverage Gap Analysis | 🔵 Tier 3 | General Healthcare AI |
| ES.ME-6 | LLM-Judge Bias Quantification | 🔵 Tier 3 | General Healthcare AI |
| ES.ME-7 | Automated-Human Metric Concordance | 🔵 Tier 3 | General Healthcare AI |
| ES.ME-8 | Outcome Evidence Commitment Status | 🟡 Tier 2 | General Healthcare AI |
| ES.ME-9 | Causal Model Operationalisation | 🟡 Tier 2 | General Healthcare AI |
