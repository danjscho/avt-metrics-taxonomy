## Tier 1 — Minimum Viable Assurance (Quick Reference)

The smallest set of metrics that a deployer cannot responsibly skip. All are measurable today with existing tools, data, and governance capacity.

### Tier 1 by Responsible Actor

**Deployer** (27 metrics)

- 🚪 **Microphone & Hardware Validation** — Basic pre-deployment hardware check. No AVT should go live without confirming capture hardware meets minimum specifications. Measurable today by any deployer.
- 🔄 **Hallucination Rate** — Core safety metric. NAS Day Zero SPI with <2% review and ≥5% pause thresholds. Every deployer must measure this through periodic clinical audit even if methodology is manual.
- 🔄 **Omission Rate** — Arguably more dangerous than hallucination because omissions are invisible to the reviewer. Must be included in periodic clinical note audit alongside hallucination rate.
- 🔄 **Negation Handling Accuracy** — Safety-critical and well-documented LLM failure mode. Should be tested pre-deployment and periodically re-audited. Negation errors directly cause clinical harm.
- 🔄 **Uncertainty Marker Preservation** — Safety-critical: certainty inflation creates false diagnostic confidence in the record. Should be tested with adversarial cases as part of pre-deployment and periodic audit.
- 🚪 **Write-back Fidelity** — Highest-priority pre-deployment gate. A hallucinated allergy written to the EPR allergy field is a system-level safety failure that propagates to every future clinical decision. Must test per EPR system before go-live.
- 📡 **Integration Error Rate** — Standard integration monitoring. Automated, low-burden, and catches data pipeline failures that directly affect patient records.
- 🚪 **Field Mapping Accuracy** — Safety-critical pre-deployment test. Wrong-field placement of safety-critical content (allergies, medications) bypasses downstream safety mechanisms entirely.
- 🚪 **Update vs Append Behaviour** — Safety-critical pre-deployment test. Must be tested per EPR system before go-live. Overwriting existing safety-critical data is a patient safety event.
- 📡 **Edit Rate (% Notes Edited)** — Primary continuous complacency indicator. Deployer-measurable from EPR workflow data. NAS Day Zero SPI. The single most important human factors metric — trajectory reveals automation bias before incidents occur.
- 📡 **Review-Before-Signing Rate** — NAS Day Zero SPI with ≥95% threshold and <85% pause trigger. Deployer-measurable from EPR workflow telemetry. Directly monitors whether human oversight is functioning.
- 📡 **Time-to-Sign Distribution** — Deployer-measurable from EPR data. The tail of very-fast approvals (<5 seconds for complex notes) is the safety-critical population. Distribution analysis detects rubber-stamping patterns.
- 📡 **Safety Performance Indicators with Thresholds (DSCMS)** — The governance mechanism that converts metrics into action. Without pre-defined thresholds and escalation paths, metrics are information without teeth. Every Tier 1 metric needs an SPI wrapper.
- 📡 **Adverse Event / Incident Rate (LFPSE)** — Established national reporting. The ultimate lagging indicator — by the time this metric moves, harm has occurred. Needs dedicated LFPSE category for AI/AVT incidents.
- 📡 **Assurance Debt Accumulation Rate** — The honest governance metric. Every deployer will accumulate it. Making it visible, tracked, and managed prevents governance theatre.
- 📡 **Patient Opt-Out Rate** — Deployer-measurable from practice records. Low-burden continuous monitoring. Rising rates signal trust issues. Demographic disaggregation reveals consent model equity.
- 📡 **Documentation Time per Consultation** — Most widely measured benefit metric. Tells you nothing about safety but essential for demonstrating value proposition. Must be reported alongside quality metrics.
- 📡 **Adoption Rate & Selective Use Patterns** — Basic deployment tracking. Selective adoption patterns (avoiding AVT for complex cases) reveal practical system boundaries and are diagnostically valuable.
- 📡 **Near-Miss Reporting Rate** — Essential leading indicator. Should be Tier 1 because it's the early warning system that LFPSE is the lagging indicator of. Requires lightweight reporting infrastructure.
- 📡 **Hazard Log Completeness** — Regulatory requirement under DCB0129. Tier 1 because it's a compliance obligation, not a recommendation. Should be linked to operational monitoring.
- 📡 **Audio Retention Compliance** — UK GDPR storage limitation requirement. Non-compliance is a regulatory breach. Deployer must verify vendor retention practices align with DPIA.
- 📡 **Consent Verification Accuracy** — CQC Mythbuster 109 requires patients to be informed. Process compliance is measurable today. Understanding gap is harder but periodic survey is feasible.
- 🚪 **Cross-Border Data Transfer Compliance** — Legal compliance requirement. Must be assessed at procurement. Non-compliance is a regulatory breach.
- 🚪 **Subject Access Request Fulfilment** — Legal compliance requirement. Must be tested before go-live to confirm vendor supports SAR fulfilment workflow.
- 🚪 **Right to Erasure Compliance** — Legal compliance requirement. Must be tested before go-live to understand erasure scope and limitations.
- 📡 **Clinician Training Completion Rate** — Governance requirement. No clinician should use AVT without completing required training. Binary compliance metric — 100% is the only acceptable target.
- 📡 **Sub-Processor Transparency** — Legal compliance requirement under UK GDPR Article 28. Must be assessed at procurement and monitored for changes.

**Vendor** (19 metrics)

- 🚪 **Hallucination-Under-Noise Rate** — Critical pre-deployment test. Whisper-based systems are documented to hallucinate from silence — this must be tested before clinical use. Tier 1 because the failure mode is well-documented and the test is straightforward.
- 🚪 **Numeric Accuracy** — Safety-critical and underspecified by current vendor reporting. Should be a Day Zero acceptance criterion. Numeric errors are disproportionately dangerous and should be reported separately from general WER.
- 🔄 **Hallucination Rate** — Core safety metric. NAS Day Zero SPI with <2% review and ≥5% pause thresholds. Every deployer must measure this through periodic clinical audit even if methodology is manual.
- 🔄 **Omission Rate** — Arguably more dangerous than hallucination because omissions are invisible to the reviewer. Must be included in periodic clinical note audit alongside hallucination rate.
- 🔄 **Negation Handling Accuracy** — Safety-critical and well-documented LLM failure mode. Should be tested pre-deployment and periodically re-audited. Negation errors directly cause clinical harm.
- 🔄 **Uncertainty Marker Preservation** — Safety-critical: certainty inflation creates false diagnostic confidence in the record. Should be tested with adversarial cases as part of pre-deployment and periodic audit.
- 🚪 **Write-back Fidelity** — Highest-priority pre-deployment gate. A hallucinated allergy written to the EPR allergy field is a system-level safety failure that propagates to every future clinical decision. Must test per EPR system before go-live.
- 📡 **Integration Error Rate** — Standard integration monitoring. Automated, low-burden, and catches data pipeline failures that directly affect patient records.
- 🚪 **Field Mapping Accuracy** — Safety-critical pre-deployment test. Wrong-field placement of safety-critical content (allergies, medications) bypasses downstream safety mechanisms entirely.
- 🚪 **Update vs Append Behaviour** — Safety-critical pre-deployment test. Must be tested per EPR system before go-live. Overwriting existing safety-critical data is a patient safety event.
- 📡 **Model Version Tracking** — Foundation for all continuous assurance. Without knowing which model version produced which output, no performance change is interpretable. Must be contractually required.
- 📡 **System Availability / Uptime** — Standard SLA monitoring. NAS Day Zero SPI (≥99.5%). Automated, zero-burden continuous metric.
- 📡 **Audio Retention Compliance** — UK GDPR storage limitation requirement. Non-compliance is a regulatory breach. Deployer must verify vendor retention practices align with DPIA.
- 🚪 **Cross-Border Data Transfer Compliance** — Legal compliance requirement. Must be assessed at procurement. Non-compliance is a regulatory breach.
- 🚪 **Subject Access Request Fulfilment** — Legal compliance requirement. Must be tested before go-live to confirm vendor supports SAR fulfilment workflow.
- 🚪 **Right to Erasure Compliance** — Legal compliance requirement. Must be tested before go-live to understand erasure scope and limitations.
- 📡 **Model Change Notification Compliance** — Should be a contractual requirement in NHS procurement. The three-layer surveillance model depends on it. Without vendor notification, governance is reactive.
- 📡 **Incident Disclosure Compliance** — Should be a contractual requirement. Without timely incident disclosure, deployers cannot respond to vendor-side security issues.
- 📡 **Sub-Processor Transparency** — Legal compliance requirement under UK GDPR Article 28. Must be assessed at procurement and monitored for changes.

**Regional (ICB)** (2 metrics)

- 📡 **Safety Performance Indicators with Thresholds (DSCMS)** — The governance mechanism that converts metrics into action. Without pre-defined thresholds and escalation paths, metrics are information without teeth. Every Tier 1 metric needs an SPI wrapper.
- 📡 **Assurance Debt Accumulation Rate** — The honest governance metric. Every deployer will accumulate it. Making it visible, tracked, and managed prevents governance theatre.

**National Body** (1 metrics)

- 📡 **Adverse Event / Incident Rate (LFPSE)** — Established national reporting. The ultimate lagging indicator — by the time this metric moves, harm has occurred. Needs dedicated LFPSE category for AI/AVT incidents.

---

