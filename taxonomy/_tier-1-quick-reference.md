## Tier 1 - Minimum Viable Assurance (Quick Reference)

The smallest set of metrics that a deployer cannot responsibly skip. All are measurable today with existing tools, data, and governance capacity.

> ⚠️ **This list is a calibrated starting point, not a fixed checklist.** Local deployment context — specialty mix, patient population, platform maturity, governance capacity, risk appetite, and volume — shifts both tier assignments and threshold numbers. A deployment with elevated risk on any of these axes should promote relevant Tier 2 or Tier 3 metrics to Tier 1; a deployment with low risk on a given axis may treat a Tier 1 metric as Tier 2 with explicit justification. See the [Calibration & Context principle](#calibration-context) for the structural commitment, the six axes, and the local-calibration documentation expectation.

**Tier 1 expanded substantially with the January–March 2026 NHS guidance suite.** Nine metrics moved into Tier 1 or were added as new Tier 1 entries reflecting compliance requirements that did not exist when the taxonomy was first drafted: the NHS Compliance & Regulatory cluster (Patient Dissent Recording, Verbal Notification, AI-Generated Content Labelling, AVT Supplier Registry, ICB Engagement, Clinical Safety Case, DPIA Template, Audio Time-to-Deletion, Transcript Retention) plus Code Hallucination Rate. For NHS deployers, the shape of Day Zero minimum assurance has changed materially since early-2025 vendor procurement; re-assess existing deployments against the expanded Tier 1 set.

**Tier 1 expanded again in v5.3.0 / v5.4.0** following the FTS notice 069369-2025 anchoring the AVT Self-Certified Supplier Registry surface. 13 metrics moved into Tier 1: 7 promotions T2 → T1 (Telemetry Provision Completeness, Evidence Pack Freshness, Indicative Pricing Transparency, Outcome Evidence Commitment Status, Deployment Equity Index, Demographic-Disaggregated WER, Performance Degradation Detection Latency) and 6 new T1 mints (Medical Device Classification Documentation, Board-Level AI Governance Mechanism, Consultation-Type Appropriateness Assessment, Privacy Notice Currency & Completeness, Information Asset Register Completeness, PRSB Semantic Completeness). The current Tier 1 set comprises **58 countable metrics** (236 total / 58 / 99 / 79).

Multi-actor responsibilities are counted once per actor, so per-actor totals below sum to more than 58.

### Tier 1 by Responsible Actor

**Deployer** (47 metrics)

- 🚪 **Microphone & Hardware Validation** - Basic pre-deployment hardware check. No AVT should go live without confirming capture hardware meets minimum specifications. Measurable today by any deployer.
- 🔄 **Hallucination Rate** ⚠️ - Core safety metric. NAS Day Zero SPI with <2% review and ≥5% pause thresholds. Every deployer must measure this through periodic clinical audit even if methodology is manual. *See underspecification warning in full entry - the term has no universally accepted definition and reported rates across the literature span 1–67% due largely to methodological differences. Document the specific subtype taxonomy and reference dataset used.*
- 🔄 **Omission Rate** - Arguably more dangerous than hallucination because omissions are invisible to the reviewer. Must be included in periodic clinical note audit alongside hallucination rate.
- 🔄 **Negation Handling Accuracy** - Safety-critical and well-documented LLM failure mode. Should be tested pre-deployment and periodically re-audited. Negation errors directly cause clinical harm.
- 🔄 **Uncertainty Marker Preservation** - Safety-critical: certainty inflation creates false diagnostic confidence in the record. Should be tested with adversarial cases as part of pre-deployment and periodic audit.
- 🚪 **Write-back Fidelity** - Highest-priority pre-deployment gate. A hallucinated allergy written to the EPR allergy field is a system-level safety failure that propagates to every future clinical decision. Must test per EPR system before go-live.
- 📡 **Integration Error Rate** - Standard integration monitoring. Automated, low-burden, and catches data pipeline failures that directly affect patient records.
- 🚪 **Field Mapping Accuracy** - Safety-critical pre-deployment test. Wrong-field placement of safety-critical content (allergies, medications) bypasses downstream safety mechanisms entirely.
- 🚪 **Update vs Append Behaviour** - Safety-critical pre-deployment test. Must be tested per EPR system before go-live. Overwriting existing safety-critical data is a patient safety event.
- 📡 **Edit Rate (% Notes Edited)** - Primary continuous complacency indicator. Deployer-measurable from EPR workflow data. NAS Day Zero SPI. The single most important human factors metric - trajectory reveals automation bias before incidents occur.
- 📡 **Review-Before-Signing Rate** - NAS Day Zero SPI with ≥95% threshold and <85% pause trigger. Deployer-measurable from EPR workflow telemetry. Directly monitors whether human oversight is functioning.
- 📡 **Time-to-Sign Distribution** - Deployer-measurable from EPR data. The tail of very-fast approvals (<5 seconds for complex notes) is the safety-critical population. Distribution analysis detects rubber-stamping patterns.
- 📡 **Safety Performance Indicators with Thresholds (DSCMS)** - The governance mechanism that converts metrics into action. Without pre-defined thresholds and escalation paths, metrics are information without teeth. Every Tier 1 metric needs an SPI wrapper.
- 📡 **Adverse Event / Incident Rate (LFPSE)** - Established national reporting. The ultimate lagging indicator - by the time this metric moves, harm has occurred. Needs dedicated LFPSE category for AI/AVT incidents.
- 📡 **Assurance Debt Accumulation Rate** - The honest governance metric. Every deployer will accumulate it. Making it visible, tracked, and managed prevents governance theatre.
- 📡 **Patient Opt-Out Rate** - Deployer-measurable from practice records. Low-burden continuous monitoring. Rising rates signal trust issues. Demographic disaggregation reveals consent model equity.
- 📡 **Documentation Time per Consultation** - Most widely measured benefit metric. Tells you nothing about safety but essential for demonstrating value proposition. Must be reported alongside quality metrics.
- 📡 **Adoption Rate & Selective Use Patterns** - Basic deployment tracking. Selective adoption patterns (avoiding AVT for complex cases) reveal practical system boundaries and are diagnostically valuable.
- 📡 **Near-Miss Reporting Rate** - Essential leading indicator. Should be Tier 1 because it's the early warning system that LFPSE is the lagging indicator of. Requires lightweight reporting infrastructure.
- 📡 **Hazard Log Completeness** - Regulatory requirement under DCB0129. Tier 1 because it's a compliance obligation, not a recommendation. Should be linked to operational monitoring.
- 📡 **Audio Retention Compliance** - UK GDPR storage limitation requirement. Non-compliance is a regulatory breach. Deployer must verify vendor retention practices align with DPIA.
- 📡 **Consent Verification Accuracy** - CQC Mythbuster 109 requires patients to be informed. Process compliance is measurable today. Understanding gap is harder but periodic survey is feasible.
- 🚪 **Cross-Border Data Transfer Compliance** - Legal compliance requirement. Must be assessed at procurement. Non-compliance is a regulatory breach.
- 🚪 **Subject Access Request Fulfilment** - Legal compliance requirement. Must be tested before go-live to confirm vendor supports SAR fulfilment workflow.
- 🚪 **Right to Erasure Compliance** - Legal compliance requirement. Must be tested before go-live to understand erasure scope and limitations.
- 📡 **Clinician Training Completion Rate** - Governance requirement. No clinician should use AVT without completing required training. Binary compliance metric - 100% is the only acceptable target.
- 📡 **Sub-Processor Transparency** - Legal compliance requirement under UK GDPR Article 28. Must be assessed at procurement and monitored for changes.
- 🚪 **AVT Supplier Registry Listing Verification** - Procurement gate with trivial verification cost. Must be confirmed before deployment and re-verified at contract renewal. Non-listed vendors should not be deployed.
- 🚪 **ICB Engagement Documentation** - Pre-deployment compliance gate under CIO/CCIO guidance v2. Documented evidence of regional engagement required before go-live. Absence indicates governance process breakdown.
- 🔄 **Clinical Safety Case Completeness** - DCB0129/0160 regulatory requirement. The 2025 FOI finding that many NHS digital health deployments lack compliant safety cases makes active monitoring essential, not optional.
- 🚪 **DPIA Template Completion Rate** - UK GDPR Article 35 legal requirement. Use of the NHSE March 2026 template enables cross-deployment comparison and ensures mandatory considerations aren't missed.
- 📡 **Patient Dissent Recording Rate** - Per-encounter compliance with the requirement to document and respect objections. Distinct from aggregate opt-out: opt-out is a blanket choice; dissent recording is procedural integrity at the point of care. Target 100%.
- 🔄 **Verbal Notification Compliance** - Proportion of AVT consultations where verbal notification was delivered at session start. The compliance metric behind the consent model. Periodic audit via patient survey or recording sample.
- 📡 **AI-Generated Content Labelling Compliance** - Every AI-generated entry must carry the mandatory SNOMED suffix. Automated verification is trivial; non-compliance breaks downstream audit and safety investigation.
- 📡 **Audio Time-to-Deletion** - NHSE IG guidance March 2026 requires deletion after summary sign-off. Measurement makes the policy operational rather than assertive. Must verify deletion in primary storage, caches, and backups.
- 📡 **Transcript Retention Compliance** - Parallel to audio deletion but often treated as less sensitive despite being higher-risk (structured, searchable, readily consumable). Explicit retention policy required; compliance measurable continuously.

**Vendor** (33 metrics)

- 🚪 **Hallucination-Under-Noise Rate** - Critical pre-deployment test. Whisper-based systems are documented to hallucinate from silence - this must be tested before clinical use. Tier 1 because the failure mode is well-documented and the test is straightforward.
- 🚪 **Numeric Accuracy** - Safety-critical and underspecified by current vendor reporting. Should be a Day Zero acceptance criterion. Numeric errors are disproportionately dangerous and should be reported separately from general WER.
- 🔄 **Hallucination Rate** ⚠️ - Core safety metric. NAS Day Zero SPI with <2% review and ≥5% pause thresholds. Every deployer must measure this through periodic clinical audit even if methodology is manual. *See underspecification warning in full entry - the term has no universally accepted definition and reported rates across the literature span 1–67% due largely to methodological differences. Document the specific subtype taxonomy and reference dataset used.*
- 🔄 **Omission Rate** - Arguably more dangerous than hallucination because omissions are invisible to the reviewer. Must be included in periodic clinical note audit alongside hallucination rate.
- 🔄 **Negation Handling Accuracy** - Safety-critical and well-documented LLM failure mode. Should be tested pre-deployment and periodically re-audited. Negation errors directly cause clinical harm.
- 🔄 **Uncertainty Marker Preservation** - Safety-critical: certainty inflation creates false diagnostic confidence in the record. Should be tested with adversarial cases as part of pre-deployment and periodic audit.
- 📡 **Code Hallucination Rate** - Zero-tolerance metric. Any non-zero rate indicates architectural failure in generation constraints. Vendor must demonstrate 0% pre-deployment and maintain continuous monitoring. A vendor who cannot achieve zero has unconstrained code generation, which is a procurement red flag.
- 🚪 **Write-back Fidelity** - Highest-priority pre-deployment gate. A hallucinated allergy written to the EPR allergy field is a system-level safety failure that propagates to every future clinical decision. Must test per EPR system before go-live.
- 📡 **Integration Error Rate** - Standard integration monitoring. Automated, low-burden, and catches data pipeline failures that directly affect patient records.
- 🚪 **Field Mapping Accuracy** - Safety-critical pre-deployment test. Wrong-field placement of safety-critical content (allergies, medications) bypasses downstream safety mechanisms entirely.
- 🚪 **Update vs Append Behaviour** - Safety-critical pre-deployment test. Must be tested per EPR system before go-live. Overwriting existing safety-critical data is a patient safety event.
- 📡 **Model Version Tracking** - Foundation for all continuous assurance. Without knowing which model version produced which output, no performance change is interpretable. Must be contractually required.
- 📡 **System Availability / Uptime** - Standard SLA monitoring. NAS Day Zero SPI (≥99.5%). Automated, zero-burden continuous metric.
- 📡 **Audio Retention Compliance** - UK GDPR storage limitation requirement. Non-compliance is a regulatory breach. Deployer must verify vendor retention practices align with DPIA.
- 🚪 **Cross-Border Data Transfer Compliance** - Legal compliance requirement. Must be assessed at procurement. Non-compliance is a regulatory breach.
- 🚪 **Subject Access Request Fulfilment** - Legal compliance requirement. Must be tested before go-live to confirm vendor supports SAR fulfilment workflow.
- 🚪 **Right to Erasure Compliance** - Legal compliance requirement. Must be tested before go-live to understand erasure scope and limitations.
- 📡 **Model Change Notification Compliance** - Should be a contractual requirement in NHS procurement. The Keyes et al. monitoring framework (system integrity / performance / impact) depends on it. Without vendor notification, governance is reactive.
- 📡 **Incident Disclosure Compliance** - Should be a contractual requirement. Without timely incident disclosure, deployers cannot respond to vendor-side security issues.
- 📡 **Sub-Processor Transparency** - Legal compliance requirement under UK GDPR Article 28. Must be assessed at procurement and monitored for changes.

**Regional (ICB)** (5 metrics)

- 📡 **Safety Performance Indicators with Thresholds (DSCMS)** - The governance mechanism that converts metrics into action. Without pre-defined thresholds and escalation paths, metrics are information without teeth. Every Tier 1 metric needs an SPI wrapper.
- 📡 **Assurance Debt Accumulation Rate** - The honest governance metric. Every deployer will accumulate it. Making it visible, tracked, and managed prevents governance theatre.

**National Body** (5 metrics)

- 📡 **Adverse Event / Incident Rate (LFPSE)** - Established national reporting. The ultimate lagging indicator - by the time this metric moves, harm has occurred. Needs dedicated LFPSE category for AI/AVT incidents.

---

### v4.1 / v5.3 / v5.4 additions to Tier 1

The following Tier 1 metrics were promoted or minted in releases since the original quick-reference content above. They are listed here separately to preserve the original prose without disturbing it; the catalogue's per-metric pages are the canonical source for each.

**Deployer**

- 🚪 **Decommissioning Data Handling Compliance** *(GV.PD-16, v4.1)* — End-of-life data handling per the deployer-vendor contract. Limitation-layer infrastructure that bounds damage at retirement. Procurement gate for new contracts; activation triggers at retirement notification.
- 🚪 **Privacy Notice Currency & Completeness** *(GV.PD-13, v5.3)* — Each public-facing privacy notice (organisation-level + service-level) must include an AVT-specific section with lawful basis, controller/processor relationship, retention periods, and any model-training-use disclosure. Annual currency check; any material processing change re-triggers. NHSE IG Attestation family.
- 🚪 **Information Asset Register Completeness** *(GV.PD-18, v5.4)* — AVT system listed in the IAR with named Information Asset Owner, lawful basis, retention period, sub-processor list, and risk classification. Annual review tied to broader IG cadence.
- 🚪 **Consultation-Type Appropriateness Assessment** *(GV.CR-14, v5.3)* — Documented assessment of which consultation types (safeguarding, mental health, paediatrics, intimate exams, end-of-life) AVT is appropriate for vs requires carve-outs. Caldicott Guardian sign-off; annual review.
- 📡 **Board-Level AI Governance Mechanism** *(GV.CR-12, v5.3)* — Named board committee or executive director with AI oversight in formal remit, quarterly minimum cadence, and escalation path. CQC well-led inspection point; cross-framework leverage (DTAC C3.1, RAI Theme 4, Principle 10).
- 📡 **Deployment Equity Index** *(IO.FE-1, v5.3)* — Deployment equity disaggregated by site, setting, and demographic axes. Continuous monitoring; complements the cluster-level disaggregated metrics (Demographic Equity Disaggregation family).
- 📡 **PRSB Semantic Completeness** *(TP.WB-8, v5.3)* — Proportion of PRSB-mandatory information elements present in AVT-generated output, stratified by applicable PRSB standard (CIS, Outpatient Letter, Discharge, etc.). Cross-framework heavyweight (DTAC C4 + FHIR UK Core + CQC Reg 17 + PRSB).

**Vendor**

- 📡 **Telemetry Provision Completeness** *(GV.VT-2, promoted v5.3)* — Per-inference logging, confidence scores, model version per output, intermediate outputs, demographic performance data. The substrate for FTS Performance & Monitoring Response.
- 📡 **Evidence Pack Freshness** *(GV.VT-13, promoted v5.3)* — All collateral kept up to date and current; vendor's responsibility to keep the Hub up to date. Periodic audit cadence.
- 🚪 **Indicative Pricing Transparency** *(GV.VT-14, promoted v5.3)* — FTS Step 1.a direct submission requirement. Pricing structure transparency for procurement.
- 📡 **Retirement Notification Compliance** *(GV.VT-15, v4.1)* — Notice period before product retirement, feature withdrawal, integration withdrawal. End-of-life infrastructure that activates on retirement event.
- 🚪 **Medical Device Classification Documentation** *(GV.CR-11, v5.3)* — MHRA SaMD classification (Class I / IIa / IIb / III) documented with justification. FTS Step 1.h direct submission requirement.

**Vendor + Deployer + National Body**

- 🚪 **Outcome Evidence Commitment Status** *(ES.ME-8, promoted v5.3)* — FTS Step 1.f "Evidence of impact and benefit in the NHS" required submission.

**Vendor + National Body**

- 📡 **Demographic-Disaggregated WER** *(TP.ASR-4, promoted v5.3)* — WER by accent, language, age, speech characteristics. NAS proposes max 5pp gap. MHRA GMLP-3 + Performance & Monitoring "boundaries and bias".

**Regional (ICB) + National Body**

- 📡 **Performance Degradation Detection Latency** *(GV.SG-3, promoted v5.3)* — Time from drift signal to detection. MHRA post-market surveillance (FTS Step 1.i). Limitation-layer detection sitting at regional / national level.

---

The two icons below align with the existing entries above:

- 🚪 = pre-deployment gate (Prevention layer)
- 📡 = continuous in-service signal (Detection or Limitation layer)
- 🔄 = periodic content audit (Detection layer)

---

> **Disagree, want to propose a metric, or think a tier should shift?** This Tier 1 list is a [prototype-for-discussion](#prototype-status), not a settled checklist. Open an issue at [github.com/danjscho/avt-metrics-taxonomy/issues](https://github.com/danjscho/avt-metrics-taxonomy/issues) — the roadmap is shaped by reader pushback as much as by the author's pre-baked plan.

