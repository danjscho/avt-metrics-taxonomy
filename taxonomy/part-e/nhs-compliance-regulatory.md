# Part E — System Governance

## NHS Compliance & Regulatory

*Process compliance metrics against defined external requirements, distinct from the safety performance metrics in the Safety & Governance group. Most entries here are binary or near-binary — the deployer is compliant or they are not — and most Tier 1 assignments reflect legal or guidance requirements that cannot be responsibly skipped regardless of clinical performance.*

*The group was added to the taxonomy in response to the January–March 2026 NHS guidance suite: NHSE IG guidance on ambient scribing (March 2026), the NHSE AVT Supplier Registry (launched January 2026), and CIO/CCIO guidance v2 (January 2026). Taken together these documents defined a discrete compliance surface that is operationally distinct from clinical safety governance and that deserves its own cluster rather than being scattered across Safety & Governance and Privacy & Data Governance.*

*The group also contains two international regulatory metrics (FDA PCCP-Equivalent Pre-Defined Acceptance Criteria, EU AI Act Event Logging Compliance) because vendor compliance cascades across jurisdictions — an AVT vendor with EU market exposure will typically apply EU AI Act requirements uniformly across their product rather than maintaining jurisdiction-specific variants, which means UK deployments inherit EU requirements through vendor compliance regardless of whether they would otherwise apply.*

*Legal and statutory privacy metrics that pre-date the 2026 NHS guidance (Subject Access Request Fulfilment, Right to Erasure, Cross-Border Data Transfer Compliance, Sub-Processor Transparency) remain in the Privacy & Data Governance group to preserve the legal-basis cluster there. The split between "privacy legal requirements" and "NHS compliance process requirements" is analytical rather than hierarchical — a deployer is obliged to meet both, and neither group has precedence over the other.*

**Tier breakdown**: 🟢 7 Tier 1 · 🟡 3 Tier 2 · 🔵 0 Tier 3

---

### 🟢 Patient Dissent Recording Rate

Per-encounter rate at which patient objections or dissent to AVT use are recorded and respected. Distinct from the existing Patient Opt-Out Rate, which is aggregate and applies at the registration or consent level. Patient Dissent Recording is the per-encounter process compliance metric: when a patient objects at the point of care, is that objection documented, is AVT actually paused for that encounter, and is the objection respected in subsequent encounters without re-litigation.

|Dimension              |Value                                                  |
|-----------------------|--------------------------------------------------------|
|**Priority Tier**      |🟢 Tier 1 — Minimum Viable                              |
|**Measurement Cadence**|Continuous                                              |
|**Pipeline Layer**     |Cross-cutting                                           |
|**Assurance Question** |Patient Experience                                      |
|**Measurement Method** |Passive Observational                                   |
|**Lifecycle Phases**   |Continuous                                              |
|**Responsible Actors** |Deployer                                                |
|**Maturity**           |Established                                             |
|**Outcome Type**       |Proximal                                                |
|**Source**             |NHSE IG guidance on ambient scribing (March 2026)       |

**Why this tier?**

> Direct compliance requirement under NHSE IG guidance. Deployer-measurable from workflow records. Binary compliance — a patient dissent not recorded and respected is a regulatory and ethical failure.

**Formal Definition**

```
Recording Rate = |dissent_events_with_recorded_and_respected_objection| / |total_dissent_events|. Target: 100%. Sub-metrics: (a) dissent documentation rate (was it recorded?); (b) dissent respect rate (was AVT paused?); (c) dissent persistence rate (was it respected in subsequent encounters?). Any sub-metric below 100% indicates compliance failure.
```

**Limitations**

> Detection of dissent events requires clinician reporting or structured capture in the EPR workflow. Silent non-compliance (clinician uses AVT despite patient objection) is invisible to passive observation.

**Novel Thinking / Implications**

> 💡 This is the per-encounter teeth behind the aggregate opt-out metric. Opt-out gives the patient a blanket choice; dissent recording ensures the choice is honoured at each specific consultation where it matters. The two metrics measure different things: opt-out measures consent model acceptance; dissent recording measures procedural integrity at the point of care. Both are necessary for a coherent consent architecture.

---

### 🟢 Verbal Notification Compliance

Proportion of AVT-using consultations where verbal notification was delivered to the patient at session start, as required by NHSE IG guidance (March 2026). Consent model in NHS primary care relies on informing patients before AVT activation, but the "informing" step is often poorly observed in busy practice. This metric measures the actual delivery of notification, not just the existence of a notification policy.

|Dimension              |Value                                                    |
|-----------------------|----------------------------------------------------------|
|**Priority Tier**      |🟢 Tier 1 — Minimum Viable                                |
|**Measurement Cadence**|Periodic audit                                            |
|**Pipeline Layer**     |Cross-cutting                                             |
|**Assurance Question** |Patient Experience                                        |
|**Measurement Method** |Hybrid                                                    |
|**Lifecycle Phases**   |Day Zero Baseline, Periodic Audit                         |
|**Responsible Actors** |Deployer                                                  |
|**Maturity**           |Established                                               |
|**Outcome Type**       |Proximal                                                  |
|**Source**             |NHSE IG guidance on ambient scribing (March 2026); CQC Mythbuster 109 context|

**Why this tier?**

> Direct compliance requirement. Measurable via patient survey sampling, consultation audit, or (with appropriate consent) recording sampling. Binary compliance — notification either happened or it didn't.

**Formal Definition**

```
Compliance Rate = |consultations_with_verbal_notification_delivered| / |total_AVT_consultations|. Measurement methods in order of increasing rigour: (a) clinician self-report at end of session; (b) patient survey sampling asking whether notification was delivered; (c) audit of audio recordings (where retention allows) for notification language. Target: 100%. Values below 95% indicate systematic compliance failure requiring intervention.
```

**Limitations**

> Self-report over-estimates compliance. Patient recall is imperfect. Audio audit is resource-intensive and depends on retention policies that may conflict with data minimisation.

**Novel Thinking / Implications**

> 💡 The gap between policy and practice on patient notification is the compliance equivalent of the consent understanding gap. A practice can have a 100% notification policy and a 60% actual notification rate — and the 40% gap is where the consent model breaks down. Periodic audit is the only way to know which side of the gap a deployer is on. A practice that refuses to audit is implicitly choosing not to know.

---

### 🟢 AI-Generated Content Labelling Compliance

Automated verification that AI-generated clinical record entries carry the mandatory SNOMED suffix identifying them as AVT output (e.g. "Audio Dictation 24771000000105" per NHSE guidance). Required for downstream systems to distinguish AI-generated content from clinician-authored content — essential for audit, safety investigation, and future training data curation.

|Dimension              |Value                                                     |
|-----------------------|-----------------------------------------------------------|
|**Priority Tier**      |🟢 Tier 1 — Minimum Viable                                 |
|**Measurement Cadence**|Continuous                                                 |
|**Pipeline Layer**     |EPR Write-back                                             |
|**Assurance Question** |Meta-evaluation                                            |
|**Measurement Method** |Computational                                              |
|**Lifecycle Phases**   |Pre-deployment, Continuous                                 |
|**Responsible Actors** |Vendor, Deployer                                           |
|**Maturity**           |Established                                                |
|**Outcome Type**       |Proximal                                                   |
|**Source**             |NHSE IG guidance on ambient scribing (March 2026)          |

**Why this tier?**

> Automated compliance check with trivial implementation cost. Should be a pre-deployment gate and continuous monitoring metric. Non-compliance is both a governance failure and a downstream data quality problem.

**Formal Definition**

```
Labelling Rate = |AI_generated_entries_with_correct_suffix| / |total_AI_generated_entries|. Target: 100%. Zero-tolerance — every AI-generated entry must be labelled. Automated verification is feasible because the suffix is a fixed SNOMED concept that either appears or doesn't. Report non-compliance instances for immediate remediation.
```

**Code: Labelling compliance check**

```python
AVT_LABEL_SUFFIX = "24771000000105"  # Audio Dictation SNOMED concept

def check_labelling_compliance(epr_entries):
    """
    Verify every AI-generated entry carries the mandatory suffix.
    """
    ai_entries = [e for e in epr_entries if e.get("source") == "AVT"]
    compliant = [e for e in ai_entries
                 if AVT_LABEL_SUFFIX in e.get("content", "")
                 or e.get("label_code") == AVT_LABEL_SUFFIX]
    non_compliant = [e for e in ai_entries if e not in compliant]
    return {
        "rate": len(compliant) / len(ai_entries) if ai_entries else 1.0,
        "non_compliant_count": len(non_compliant),
        "non_compliant_entries": non_compliant,
        "alert": len(non_compliant) > 0,
        "severity": "CRITICAL" if non_compliant else "OK"
    }
```

**Limitations**

> Assumes the vendor's write-back system supports the suffix — some EPR integrations strip metadata fields that don't map to native EPR structures. The suffix location (free-text vs metadata) affects automated detection methodology.

**Novel Thinking / Implications**

> 💡 Without reliable labelling, every downstream system that consumes clinical records is operating without knowing which content is AI-generated. This matters for: safety investigation (was the error in a human-written or AI-generated entry?); training data curation (if AI-generated records are fed back into training, the labelling is necessary to detect and exclude them); audit trails (which clinicians rely on AI assistance and how frequently). Non-labelling is an infrastructure failure with cascading consequences.

---

### 🟢 AVT Supplier Registry Listing Verification

Procurement and ongoing verification that the deployed AVT system is listed on the NHS England AVT Supplier Registry and remains listed throughout the deployment lifecycle. The Registry (launched January 2026) is the NHS-level mechanism for self-certified minimum standards, and registry status is expected to become a procurement precondition.

|Dimension              |Value                                                 |
|-----------------------|------------------------------------------------------|
|**Priority Tier**      |🟢 Tier 1 — Minimum Viable                             |
|**Measurement Cadence**|Continuous                                            |
|**Pipeline Layer**     |Cross-cutting                                         |
|**Assurance Question** |Safety                                                |
|**Measurement Method** |Human Review                                          |
|**Lifecycle Phases**   |Pre-deployment, Continuous                            |
|**Responsible Actors** |Deployer, Vendor                                      |
|**Maturity**           |Established                                           |
|**Outcome Type**       |Proximal                                              |
|**Source**             |NHSE AVT Supplier Registry (January 2026)             |

**Why this tier?**

> Procurement gate with trivial verification cost. Should be confirmed at procurement and re-verified at contract renewal and on notification of vendor compliance events.

**Formal Definition**

```
Listing Verification: at procurement, confirm vendor is on the live Registry. Quarterly re-verification during deployment. Binary: listed or not listed. Where not listed, deployment should not proceed (pre-deployment) or should trigger formal risk review (during deployment). Also track: date of most recent vendor compliance attestation, scope of attested compliance (which AVT products are covered).
```

**Limitations**

> Registry is self-certified — listing indicates vendor attestation rather than independent verification. Listing scope may not cover all deployed AVT modules from a vendor with multiple products.

**Novel Thinking / Implications**

> 💡 The Registry's value depends on NHS bodies treating listing as a procurement precondition. If deployments proceed with non-listed vendors, the Registry becomes advisory rather than normative and loses its governance function. Making Registry verification a Tier 1 metric supports the norm that listing is expected — and creates visible data on deployment-to-listing alignment that can inform Registry policy over time.

---

### 🟢 ICB Engagement Documentation

Documented evidence that the deployer engaged with their ICB digital team (or equivalent regional body) before AVT deployment, as required by the CIO/CCIO guidance (v2, January 2026). The ICB engagement requirement exists to prevent uncoordinated deployment across an integrated care system and to ensure regional intelligence about AVT risks and mitigations is applied consistently.

|Dimension              |Value                                                       |
|-----------------------|-------------------------------------------------------------|
|**Priority Tier**      |🟢 Tier 1 — Minimum Viable                                   |
|**Measurement Cadence**|One-off gate                                                 |
|**Pipeline Layer**     |Cross-cutting                                                |
|**Assurance Question** |Meta-evaluation                                              |
|**Measurement Method** |Human Review                                                 |
|**Lifecycle Phases**   |Pre-deployment                                               |
|**Responsible Actors** |Deployer, Regional (ICB)                                     |
|**Maturity**           |Established                                                  |
|**Outcome Type**       |Proximal                                                     |
|**Source**             |CIO/CCIO guidance v2 (January 2026); NHS CIO priority notification|

**Why this tier?**

> Pre-deployment compliance requirement. Should be a documented gate before go-live. Failure indicates a governance process breakdown that deserves immediate correction.

**Formal Definition**

```
Engagement documentation includes: (1) formal notification to ICB digital team dated before go-live; (2) ICB response acknowledging notification; (3) any conditions or recommendations from ICB on file. Binary compliance: all three present = compliant. Missing ICB response is a flag for follow-up, not automatic non-compliance, because ICB capacity constraints may prevent timely response.
```

**Limitations**

> ICB engagement quality varies — some ICBs have mature digital teams providing substantive review; others acknowledge notifications without meaningful engagement. Documentation presence does not guarantee engagement quality.

**Novel Thinking / Implications**

> 💡 ICB engagement is the mechanism that prevents NHS AVT deployment from being a series of disconnected practice-level decisions with no regional coordination. It only works if it is actually happening — and practices deploying AVT without ICB engagement are a visible symptom of governance friction, ICB capacity constraints, or deployment urgency overriding process. Tracking the metric is a diagnostic tool for that friction as much as it is a compliance check.

---

### 🟢 Clinical Safety Case Completeness

Existence, currency, and coverage of a formal DCB0129/0160 clinical safety case for the AVT deployment. Distinct from the existing Hazard Log Completeness metric, which covers log currency. Safety Case Completeness is the broader document: hazard identification, risk analysis, mitigations, residual risk acceptance, and governance arrangements. A 2025 FOI-based study (PubMed 41172285) found widespread non-compliance with DCB0129 requirements among NHS digital health deployments.

|Dimension              |Value                                                                                            |
|-----------------------|-------------------------------------------------------------------------------------------------|
|**Priority Tier**      |🟢 Tier 1 — Minimum Viable                                                                        |
|**Measurement Cadence**|Periodic audit                                                                                   |
|**Pipeline Layer**     |Cross-cutting                                                                                    |
|**Assurance Question** |Safety                                                                                           |
|**Measurement Method** |Human Review                                                                                     |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                                                   |
|**Responsible Actors** |Deployer                                                                                         |
|**Maturity**           |Established                                                                                      |
|**Outcome Type**       |Proximal                                                                                         |
|**Source**             |DCB0129/0160 regulatory requirement; PubMed 41172285 FOI study of NHS digital safety standard compliance|

**Why this tier?**

> Direct regulatory requirement. Non-compliance is both a legal and a safety issue. The 2025 FOI study found widespread non-compliance, making this a known high-risk area requiring active monitoring.

**Formal Definition**

```
Completeness assessed against DCB0129 standard sections: (1) safety management system; (2) hazard identification; (3) hazard analysis and evaluation; (4) hazard control; (5) hazard log; (6) safety case report; (7) safety incident management; (8) issue resolution. Each section binary (present and current / missing or out-of-date). Full compliance requires all sections. Currency: major update triggered by significant system change, model version change, or new hazard identification.
```

**Limitations**

> Compliance with structure does not guarantee quality of content. Safety cases are often written to satisfy the standard rather than to genuinely analyse system safety — the "compliance theatre" problem. External independent review is the only reliable check.

**Novel Thinking / Implications**

> 💡 The 2025 FOI finding that many NHS digital health deployments lack DCB0129 compliance is a structural warning about regulatory enforcement gaps. AVT deployment is happening faster than safety case development in many places. Making Safety Case Completeness a Tier 1 metric both highlights the compliance obligation and creates visible data on how widespread the gap is — which is itself a governance intervention.

---

### 🟢 DPIA Template Completion Rate

Proportion of AVT deployments using the NHS-provided March 2026 DPIA template with all mandatory sections completed. Data Protection Impact Assessment is required under UK GDPR Article 35 for high-risk processing, and AVT meets the high-risk threshold. The NHSE template provides standardised structure — but the template only helps if it's actually used and completed.

|Dimension              |Value                                                 |
|-----------------------|------------------------------------------------------|
|**Priority Tier**      |🟢 Tier 1 — Minimum Viable                             |
|**Measurement Cadence**|Periodic audit                                        |
|**Pipeline Layer**     |Cross-cutting                                         |
|**Assurance Question** |Safety                                                |
|**Measurement Method** |Human Review                                          |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                        |
|**Responsible Actors** |Deployer                                              |
|**Maturity**           |Established                                           |
|**Outcome Type**       |Proximal                                              |
|**Source**             |UK GDPR Article 35; NHSE IG guidance template (March 2026)|

**Why this tier?**

> Legal requirement. Pre-deployment gate. Template completion is measurable and binary.

**Formal Definition**

```
Completion Rate = |deployments_with_complete_DPIA_using_template| / |total_AVT_deployments|. Template mandatory sections: processing description, lawful basis, data flows, risks identified, mitigations, residual risk acceptance, DPO sign-off, review schedule. Each section binary; complete DPIA requires all sections. Review cadence: minimum annually or on significant processing change.
```

**Limitations**

> Template compliance doesn't guarantee substantive risk analysis. "Completed" DPIAs that list "no residual risks identified" for a novel AVT deployment are likely inadequate regardless of template adherence.

**Novel Thinking / Implications**

> 💡 The NHSE template provides common structure across deployments, which has three benefits: (1) makes comparison possible across sites, (2) ensures mandatory considerations aren't missed, (3) creates an evidence base for national-level risk analysis. Template non-use isn't necessarily non-compliance with UK GDPR (bespoke DPIAs can be legitimate) but it loses the aggregation benefit. Tracking template use rate is a proxy for how consistently the governance infrastructure is being built.

---

### 🟡 DSPA Status

Existence and currency of Data Sharing/Processing Agreements with all data processors involved in AVT operation. UK GDPR Article 28 requires written agreements with processors, and cloud-hosted AVT typically involves multiple processors (primary vendor, cloud provider, model provider, annotation services). Related to the existing Sub-Processor Transparency metric but specifically focuses on the contractual agreements rather than the disclosure of sub-processors.

|Dimension              |Value                                         |
|-----------------------|----------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                        |
|**Measurement Cadence**|Periodic audit                                |
|**Pipeline Layer**     |Cross-cutting                                 |
|**Assurance Question** |Safety                                        |
|**Measurement Method** |Human Review                                  |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                |
|**Responsible Actors** |Deployer, Vendor                              |
|**Maturity**           |Established                                   |
|**Outcome Type**       |Proximal                                      |
|**Source**             |UK GDPR Article 28; NHS data protection guidance|

**Why this tier?**

> Legal compliance requirement. Annual audit recommended. Slightly lower tier than DPIA because absence of DSPA is more commonly an oversight than a structural governance failure — but still a legal requirement.

**Formal Definition**

```
DSPA Status per processor: (a) agreement in place (binary); (b) agreement currency (signed within last 2 years or since last significant change); (c) agreement covers all processing activities actually performed by that processor; (d) UK GDPR Article 28 mandatory clauses present. Full compliance requires all four per processor. Aggregate metric: |processors_fully_compliant| / |total_processors|.
```

**Limitations**

> Agreement existence doesn't guarantee processor compliance with the agreement. Cross-border processors may have limited enforceability. Complex sub-processor chains make coverage verification difficult.

**Novel Thinking / Implications**

> 💡 DSPAs are where the legal rubber meets the road. A deployer with a DPIA but no DSPAs has documented the risks without contractually binding the processors to manage them. This is a common gap because DPIAs are visible in NHS audit processes while DSPAs are often handled by legal departments outside the IG team's line of sight.

---

### 🟡 FDA PCCP-Equivalent Pre-Defined Acceptance Criteria

Whether the vendor has pre-specified quantitative acceptance criteria that any model update must meet before being deployed to production. FDA Predetermined Change Control Plans (finalised December 2024) require this for US-market medical device AI. Even in UK-only deployments, it matters because: (1) EU-market vendors cascade similar requirements through the EU AI Act, and (2) the existence of pre-defined acceptance criteria is a proxy for mature change control regardless of regulatory jurisdiction.

|Dimension              |Value                                                   |
|-----------------------|---------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                   |
|**Measurement Cadence**|One-off gate                                             |
|**Pipeline Layer**     |Cross-cutting                                            |
|**Assurance Question** |Safety                                                   |
|**Measurement Method** |Human Review                                             |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                           |
|**Responsible Actors** |Vendor                                                   |
|**Maturity**           |Emerging                                                 |
|**Outcome Type**       |Proximal                                                 |
|**Source**             |FDA PCCP guidance (December 2024); EU AI Act Article 15; NICE ESF 2022 AI updates|

**Why this tier?**

> Procurement assessment. Should be standard due diligence for any AVT acquisition. Vendors without PCCP-equivalent frameworks are a higher governance risk.

**Formal Definition**

```
Assessment against criteria: (1) Performance acceptance thresholds pre-specified and quantitative; (2) Regression test suite defined and maintained; (3) Fairness/equity criteria included in acceptance testing; (4) Rollback procedure specified if update fails acceptance post-deployment; (5) Documentation of acceptance decisions available for audit. Binary per criterion; full compliance = all five.
```

**Limitations**

> Vendors may claim PCCP equivalence without independent verification. The substantive quality of acceptance criteria matters more than their existence — a criterion like "WER not more than 20% worse" technically exists but provides no meaningful safety floor.

**Novel Thinking / Implications**

> 💡 PCCP is a structural shift in how AI medical devices are regulated — from approving specific models to approving the change control process. For AVT specifically, this is essential because continuous model improvement is expected, and ad-hoc change control makes every update a regulatory event. NHS procurement should treat PCCP-equivalent frameworks as the baseline expectation, not a differentiator, even though the formal PCCP framework applies to US-market devices.

---

### 🟡 EU AI Act Event Logging Compliance

Compliance with EU AI Act Article 12 automatic event logging requirements for high-risk AI systems. High-risk provisions became effective August 2026. Applies to any AVT vendor with EU market exposure, and cascades into UK deployment because vendors typically apply the strictest applicable regulatory regime uniformly across their product rather than maintaining jurisdiction-specific variants.

|Dimension              |Value                                              |
|-----------------------|----------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                              |
|**Measurement Cadence**|Continuous                                          |
|**Pipeline Layer**     |Cross-cutting                                       |
|**Assurance Question** |Safety                                              |
|**Measurement Method** |Computational                                       |
|**Lifecycle Phases**   |Pre-deployment, Continuous                          |
|**Responsible Actors** |Vendor                                              |
|**Maturity**           |Emerging                                            |
|**Outcome Type**       |Proximal                                            |
|**Source**             |EU AI Act Article 12 (high-risk provisions effective August 2026)|

**Why this tier?**

> Vendor-side regulatory requirement. Deployer should verify event logging infrastructure exists and receive logs for foreseeable-misuse investigation. Important for incident investigation capability.

**Formal Definition**

```
Event logging must capture: (1) period of use (start, duration, stop per session); (2) reference database used; (3) input data that led to output; (4) natural persons involved in verification of output. Logging must be automatic, not opt-in. Retention period specified in vendor policy and aligned with EU AI Act minimums. Deployer verification: can the vendor provide a complete event log for any given encounter on request within a reasonable timeframe?
```

**Limitations**

> Full logging creates large data volumes and storage costs. Logging of input data conflicts with data minimisation principles — resolving this requires careful policy design. Deployer verification is manual and sample-based.

**Novel Thinking / Implications**

> 💡 Event logging is the infrastructure that supports retrospective incident investigation. Without it, when an AVT error causes harm six months after the fact, the investigation has nothing to work with — the clinician may not remember the encounter, the patient certainly won't remember the AI's behaviour, and the vendor has no logs to reconstruct what happened. The EU AI Act requirement is essentially mandating the infrastructure for forensic investigation of AI clinical systems, which is a governance improvement regardless of jurisdiction.
