## Tier 1 - Minimum Viable Assurance (Quick Reference)

The smallest set of metrics that a deployer cannot responsibly skip. All are measurable today with existing tools, data, and governance capacity.

> ⚠️ **This list is a calibrated starting point, not a fixed checklist.** Local deployment context — specialty mix, patient population, platform maturity, governance capacity, risk appetite, and volume — shifts both tier assignments and threshold numbers. A deployment with elevated risk on any of these axes should promote relevant Tier 2 or Tier 3 metrics to Tier 1; a deployment with low risk on a given axis may treat a Tier 1 metric as Tier 2 with explicit justification. See the [Calibration & Context principle](#calibration-context) for the structural commitment, the six axes, and the local-calibration documentation expectation.

The current Tier 1 set comprises **58 countable metrics**. Tier 1 expanded substantially with the January–March 2026 NHS guidance suite and again in v5.3.0 / v5.4.0 following the FTS notice 069369-2025; entries promoted or minted in those waves are marked **(new in v5.3/v5.4)** or **(promoted v5.3)** below. For NHS deployers, the shape of Day Zero minimum assurance has changed materially since early-2025 vendor procurement; re-assess existing deployments against the expanded set.

Multi-actor responsibilities are counted once per actor, so per-actor totals below sum to more than 58.

**Cadence icons:**

- 🚪 = pre-deployment gate (Prevention layer)
- 📡 = continuous in-service signal (Detection or Limitation layer)
- 🔄 = periodic content audit (Detection layer)

### Tier 1 by Responsible Actor

#### Deployer

| Metric | Cadence | Why this tier |
|---|---|---|
| **Microphone & Hardware Validation** | 🚪 | Basic pre-deployment hardware check. No AVT should go live without confirming capture hardware meets minimum specifications. |
| **Hallucination Rate** ⚠️ | 🔄 | Core safety metric. NAS Day Zero SPI with <2% review and ≥5% pause thresholds. *See underspecification warning — reported rates span 1–67% across the literature.* |
| **Omission Rate** | 🔄 | Arguably more dangerous than hallucination because omissions are invisible to the reviewer. Must be included in periodic clinical note audit. |
| **Negation Handling Accuracy** | 🔄 | Safety-critical and well-documented LLM failure mode. Negation errors directly cause clinical harm. |
| **Uncertainty Marker Preservation** | 🔄 | Safety-critical: certainty inflation creates false diagnostic confidence in the record. |
| **Write-back Fidelity** | 🚪 | Highest-priority pre-deployment gate. A hallucinated allergy written to the EPR allergy field is a system-level safety failure that propagates to every future clinical decision. |
| **Integration Error Rate** | 📡 | Standard integration monitoring. Automated, low-burden, catches data pipeline failures that directly affect patient records. |
| **Field Mapping Accuracy** | 🚪 | Safety-critical pre-deployment test. Wrong-field placement of safety-critical content (allergies, medications) bypasses downstream safety mechanisms entirely. |
| **Update vs Append Behaviour** | 🚪 | Safety-critical pre-deployment test. Overwriting existing safety-critical data is a patient safety event. |
| **Edit Rate (% Notes Edited)** | 📡 | Primary continuous complacency indicator. NAS Day Zero SPI. The single most important human factors metric — trajectory reveals automation bias before incidents occur. |
| **Review-Before-Signing Rate** | 📡 | NAS Day Zero SPI with ≥95% threshold and <85% pause trigger. Directly monitors whether human oversight is functioning. |
| **Time-to-Sign Distribution** | 📡 | The tail of very-fast approvals (<5 seconds for complex notes) is the safety-critical population. Distribution analysis detects rubber-stamping patterns. |
| **Safety Performance Indicators with Thresholds (DSCMS)** | 📡 | The governance mechanism that converts metrics into action. Without pre-defined thresholds and escalation paths, metrics are information without teeth. |
| **Adverse Event / Incident Rate (LFPSE)** | 📡 | Established national reporting. The ultimate lagging indicator — by the time this metric moves, harm has occurred. |
| **Assurance Debt Accumulation Rate** | 📡 | The honest governance metric. Every deployer will accumulate it; making it visible prevents governance theatre. |
| **Patient Opt-Out Rate** | 📡 | Low-burden continuous monitoring. Rising rates signal trust issues. Demographic disaggregation reveals consent model equity. |
| **Documentation Time per Consultation** | 📡 | Most widely measured benefit metric. Tells you nothing about safety but essential for demonstrating value proposition. |
| **Adoption Rate & Selective Use Patterns** | 📡 | Selective adoption patterns (avoiding AVT for complex cases) reveal practical system boundaries and are diagnostically valuable. |
| **Near-Miss Reporting Rate** | 📡 | Essential leading indicator — the early warning system that LFPSE is the lagging indicator of. |
| **Hazard Log Completeness** | 📡 | Regulatory requirement under DCB0129. Compliance obligation, not a recommendation. |
| **Audio Retention Compliance** | 📡 | UK GDPR storage limitation requirement. Non-compliance is a regulatory breach. |
| **Consent Verification Accuracy** | 📡 | CQC Mythbuster 109 requires patients to be informed. Process compliance is measurable today. |
| **Cross-Border Data Transfer Compliance** | 🚪 | Legal compliance requirement. Must be assessed at procurement. Non-compliance is a regulatory breach. |
| **Subject Access Request Fulfilment** | 🚪 | Legal compliance requirement. Must be tested before go-live to confirm vendor supports SAR fulfilment workflow. |
| **Right to Erasure Compliance** | 🚪 | Legal compliance requirement. Must be tested before go-live to understand erasure scope and limitations. |
| **Clinician Training Completion Rate** | 📡 | Governance requirement. No clinician should use AVT without completing required training — binary compliance, 100% target. |
| **Sub-Processor Transparency** | 📡 | Legal compliance requirement under UK GDPR Article 28. Must be assessed at procurement and monitored for changes. |
| **AVT Supplier Registry Listing Verification** | 🚪 | Procurement gate with trivial verification cost. Non-listed vendors should not be deployed. |
| **ICB Engagement Documentation** | 🚪 | Pre-deployment compliance gate under CIO/CCIO guidance v2. Absence indicates governance process breakdown. |
| **Clinical Safety Case Completeness** | 🔄 | DCB0129/0160 regulatory requirement. The 2025 FOI finding that many NHS digital health deployments lack compliant safety cases makes active monitoring essential. |
| **DPIA Template Completion Rate** | 🚪 | UK GDPR Article 35 legal requirement. Use of the NHSE March 2026 template enables cross-deployment comparison. |
| **Patient Dissent Recording Rate** | 📡 | Per-encounter compliance with the requirement to document and respect objections. Distinct from aggregate opt-out: dissent recording is procedural integrity at the point of care. |
| **Verbal Notification Compliance** | 🔄 | Proportion of AVT consultations where verbal notification was delivered at session start. The compliance metric behind the consent model. |
| **AI-Generated Content Labelling Compliance** | 📡 | Every AI-generated entry must carry the mandatory SNOMED suffix. Non-compliance breaks downstream audit and safety investigation. |
| **Audio Time-to-Deletion** | 📡 | NHSE IG guidance March 2026 requires deletion after summary sign-off. Must verify deletion in primary storage, caches, and backups. |
| **Transcript Retention Compliance** | 📡 | Higher-risk than audio (structured, searchable, readily consumable). Explicit retention policy required; compliance measurable continuously. |
| **Decommissioning Data Handling Compliance** *(new in v4.1)* | 🚪 | End-of-life data handling per the deployer-vendor contract. Limitation-layer infrastructure that bounds damage at retirement. |
| **Privacy Notice Currency & Completeness** *(new in v5.3)* | 🚪 | Each public-facing privacy notice must include an AVT-specific section with lawful basis, controller/processor relationship, retention, and any model-training-use disclosure. NHSE IG Attestation family. |
| **Information Asset Register Completeness** *(new in v5.4)* | 🚪 | AVT system listed in the IAR with named Information Asset Owner, lawful basis, retention, sub-processor list, and risk classification. |
| **Consultation-Type Appropriateness Assessment** *(new in v5.3)* | 🚪 | Documented assessment of which consultation types (safeguarding, mental health, paediatrics, intimate exams, end-of-life) AVT is appropriate for vs requires carve-outs. Caldicott Guardian sign-off. |
| **Board-Level AI Governance Mechanism** *(new in v5.3)* | 📡 | Named board committee or executive director with AI oversight in formal remit, quarterly minimum cadence, escalation path. CQC well-led inspection point. |
| **Deployment Equity Index** *(promoted v5.3)* | 📡 | Deployment equity disaggregated by site, setting, and demographic axes. Complements cluster-level disaggregated metrics. |
| **PRSB Semantic Completeness** *(new in v5.3)* | 📡 | Proportion of PRSB-mandatory information elements present in AVT-generated output, stratified by applicable PRSB standard (CIS, Outpatient Letter, Discharge, etc.). |

#### Vendor

| Metric | Cadence | Why this tier |
|---|---|---|
| **Hallucination-Under-Noise Rate** | 🚪 | Critical pre-deployment test. Whisper-based systems are documented to hallucinate from silence. |
| **Numeric Accuracy** | 🚪 | Safety-critical and underspecified by current vendor reporting. Should be a Day Zero acceptance criterion. |
| **Hallucination Rate** ⚠️ | 🔄 | Core safety metric. NAS Day Zero SPI with <2% review and ≥5% pause thresholds. *See underspecification warning.* |
| **Omission Rate** | 🔄 | Arguably more dangerous than hallucination because omissions are invisible to the reviewer. |
| **Negation Handling Accuracy** | 🔄 | Safety-critical and well-documented LLM failure mode. |
| **Uncertainty Marker Preservation** | 🔄 | Certainty inflation creates false diagnostic confidence in the record. |
| **Code Hallucination Rate** | 📡 | Zero-tolerance metric. Any non-zero rate indicates architectural failure in generation constraints. |
| **Write-back Fidelity** | 🚪 | Highest-priority pre-deployment gate. Per-EPR test before go-live. |
| **Integration Error Rate** | 📡 | Standard integration monitoring. Automated, low-burden. |
| **Field Mapping Accuracy** | 🚪 | Wrong-field placement of safety-critical content bypasses downstream safety mechanisms. |
| **Update vs Append Behaviour** | 🚪 | Overwriting existing safety-critical data is a patient safety event. |
| **Model Version Tracking** | 📡 | Foundation for all continuous assurance. Without knowing which model version produced which output, no performance change is interpretable. |
| **System Availability / Uptime** | 📡 | Standard SLA monitoring. NAS Day Zero SPI (≥99.5%). |
| **Audio Retention Compliance** | 📡 | UK GDPR storage limitation. Vendor retention practices must align with DPIA. |
| **Cross-Border Data Transfer Compliance** | 🚪 | Legal compliance requirement assessed at procurement. |
| **Subject Access Request Fulfilment** | 🚪 | Vendor must support SAR fulfilment workflow before go-live. |
| **Right to Erasure Compliance** | 🚪 | Vendor must demonstrate erasure scope before go-live. |
| **Model Change Notification Compliance** | 📡 | Should be a contractual requirement. The Keyes monitoring framework depends on it. |
| **Incident Disclosure Compliance** | 📡 | Without timely incident disclosure, deployers cannot respond to vendor-side security issues. |
| **Sub-Processor Transparency** | 📡 | UK GDPR Article 28 compliance. Assessed at procurement and monitored for changes. |
| **Telemetry Provision Completeness** *(promoted v5.3)* | 📡 | Per-inference logging, confidence scores, model version per output, intermediate outputs, demographic performance data. The substrate for FTS Performance & Monitoring Response. |
| **Evidence Pack Freshness** *(promoted v5.3)* | 📡 | All collateral kept up to date. Vendor's responsibility to keep the Hub current. |
| **Indicative Pricing Transparency** *(promoted v5.3)* | 🚪 | FTS Step 1.a direct submission requirement. Pricing structure transparency for procurement. |
| **Retirement Notification Compliance** *(new in v4.1)* | 📡 | Notice period before product retirement, feature withdrawal, integration withdrawal. |
| **Medical Device Classification Documentation** *(new in v5.3)* | 🚪 | MHRA SaMD classification (Class I / IIa / IIb / III) documented with justification. FTS Step 1.h direct submission. |

#### Vendor + Deployer + National Body

| Metric | Cadence | Why this tier |
|---|---|---|
| **Outcome Evidence Commitment Status** *(promoted v5.3)* | 🚪 | FTS Step 1.f "Evidence of impact and benefit in the NHS" required submission. |

#### Vendor + National Body

| Metric | Cadence | Why this tier |
|---|---|---|
| **Demographic-Disaggregated WER** *(promoted v5.3)* | 📡 | WER by accent, language, age, speech characteristics. NAS proposes max 5pp gap. MHRA GMLP-3 + Performance & Monitoring "boundaries and bias". |

#### Regional (ICB) + National Body

| Metric | Cadence | Why this tier |
|---|---|---|
| **Safety Performance Indicators with Thresholds (DSCMS)** | 📡 | The governance mechanism that converts metrics into action. |
| **Assurance Debt Accumulation Rate** | 📡 | The honest governance metric, surfaced at regional level. |
| **Adverse Event / Incident Rate (LFPSE)** | 📡 | Established national reporting. Needs dedicated LFPSE category for AI/AVT incidents. |
| **Performance Degradation Detection Latency** *(promoted v5.3)* | 📡 | Time from drift signal to detection. MHRA post-market surveillance (FTS Step 1.i). Limitation-layer detection sitting at regional / national level. |

---

> **Disagree, want to propose a metric, or think a tier should shift?** This Tier 1 list is a [prototype-for-discussion](#prototype-status), not a settled checklist. Open an issue at [github.com/danjscho/avt-metrics-taxonomy/issues](https://github.com/danjscho/avt-metrics-taxonomy/issues) — the roadmap is shaped by reader pushback as much as by the author's pre-baked plan.
