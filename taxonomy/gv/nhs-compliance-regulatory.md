### GV.CR-1 🟢 Patient Dissent Recording Rate

Per-encounter rate at which patient objections or dissent to AVT use are recorded and respected. Distinct from the existing Patient Opt-Out Rate, which is aggregate and applies at the registration or consent level. Patient Dissent Recording is the per-encounter process compliance metric: when a patient objects at the point of care, is that objection documented, is AVT actually paused for that encounter, and is the objection respected in subsequent encounters without re-litigation.

|Dimension              |Value                                                  |
|-----------------------|--------------------------------------------------------|
| **Reference** | GV.CR-1 |
|**Priority Tier**      |🟢 Tier 1 - Minimum Viable                              |
|**Measurement Cadence**|Continuous                                              |
|**Pipeline Layer**     |Cross-cutting                                           |
|**Assurance Question** |Patient Experience                                      |
|**Measurement Method** |Passive Observational                                   |
|**Lifecycle Phases**   |Continuous                                              |
|**Responsible Actors** |Deployer                                                |
|**Maturity**           |Established                                             |
|**Outcome Type**       |Proximal                                                |
|**Applicability**      |General Healthcare AI                                   |
|**Source**             |[NHSE-IG-Guidance-2026-03]                              |

**Why this tier?**

> Direct compliance requirement under NHSE IG guidance. Deployer-measurable from workflow records. Binary compliance - a patient dissent not recorded and respected is a regulatory and ethical failure.

**Formal Definition**

```
Recording Rate = |dissent_events_with_recorded_and_respected_objection| / |total_dissent_events|. Target: 100%. Sub-metrics: (a) dissent documentation rate (was it recorded?); (b) dissent respect rate (was AVT paused?); (c) dissent persistence rate (was it respected in subsequent encounters?). Any sub-metric below 100% indicates compliance failure.
```

**Reference Standard**

> Authoritative source: the EPR consultation record + AVT activation telemetry. A "dissent event" is any patient communication declining AVT use at the point of care, captured by one of:
>
> - **Explicit verbal objection** logged by the clinician in the consultation record (free-text or structured field; structured preferred)
> - **Structured opt-out indicator** set in the patient record at or before the encounter (must propagate to AVT activation - see [IO.PX-1 Patient Opt-Out Rate](#io-px-1))
> - **Patient-initiated AVT termination mid-consultation** signalled to the clinician
>
> Implicit / inferred dissent (patient appears uncomfortable, clinician guesses) is out of scope for this metric and belongs under separate human-factors observation. "Respected" means AVT was not active at any point after the dissent event during that encounter or in subsequent encounters until the patient affirmatively reverses the dissent. Reversal MUST be documented separately; absence of new dissent ≠ reversal.

**Operational Specification**

> - **Window:** continuous, monthly compliance reporting per practice / per clinician.
> - **Population:** all AVT-eligible consultations during the window. Denominator includes encounters where the patient *could* have dissented (i.e. AVT was offered or activated), not just encounters where dissent occurred.
> - **Sub-metric breakdown MANDATORY:** the three sub-metrics (documentation, respect, persistence) reported separately; aggregate-only reporting is not Tier 1 sufficient.
> - **Per-clinician disaggregation MANDATORY:** dissent compliance hides at clinician level. A practice 95 % aggregate may hide one clinician at 50 %.
> - **Dissent-detection coverage check:** if recorded dissent rate is < 0.5 % of AVT-eligible consultations, the deployer must run a sampling check (clinician self-report or patient survey) to verify the low rate reflects actual patient acceptance rather than under-detection.

**Trigger Conditions**

> ⚠️ **Provenance:** the IG-incident reportability framing follows from [NHSE-IG-Guidance-2026-03] and the single-instance dissent-not-respected escalation reflects the binary-compliance logic in the Why-this-tier section. Specific numbers (≥ 99 % monthly sub-metric compliance, < 95 % escalation trigger, < 0.5 % coverage-check threshold) are **proposed in v3.3 as starting points**, not externally validated. Indicative; require local calibration before contractual use.
>
> - **Pre-deployment gate:** EPR / AVT integration capable of recording dissent in a structured form and propagating it to subsequent encounters; consultation workflow includes a documented step at which the clinician offers AVT and records the response.
> - **Continuous monitoring:** documentation, respect, and persistence sub-metrics each ≥ 99 % monthly; alert on any single dissent-not-respected event.
> - **Pause / escalation trigger:** any dissent-not-respected event confirmed (single instance), OR sub-metric < 95 % in any month. Both reportable as IG incidents.
>
> Specific numerical starting points are deployment-context-dependent and live in [Threshold Reference: GV.CR-1](../thresholds.md#gv-cr-1). Treat them as starting points to calibrate locally — not as contractual gates.



**Limitations**

> Detection of dissent events requires clinician reporting or structured capture in the EPR workflow. Silent non-compliance (clinician uses AVT despite patient objection) is invisible to passive observation. The dissent-detection coverage check in the Operational Specification provides a partial counter to this by requiring sampling-based verification when recorded dissent is implausibly low.

**Novel Thinking / Implications**

> 💡 This is the per-encounter teeth behind the aggregate opt-out metric. Opt-out gives the patient a blanket choice; dissent recording ensures the choice is honoured at each specific consultation where it matters. The two metrics measure different things: opt-out measures consent model acceptance; dissent recording measures procedural integrity at the point of care. Both are necessary for a coherent consent architecture.

---

### GV.CR-2 🟢 Verbal Notification Compliance

Proportion of AVT-using consultations where verbal notification was delivered to the patient at session start, as required by NHSE IG guidance (March 2026). Consent model in NHS primary care relies on informing patients before AVT activation, but the "informing" step is often poorly observed in busy practice. This metric measures the actual delivery of notification, not just the existence of a notification policy.

|Dimension              |Value                                                    |
|-----------------------|----------------------------------------------------------|
| **Reference** | GV.CR-2 |
|**Priority Tier**      |🟢 Tier 1 - Minimum Viable                                |
|**Measurement Cadence**|Periodic audit                                            |
|**Pipeline Layer**     |Cross-cutting                                             |
|**Assurance Question** |Patient Experience                                        |
|**Measurement Method** |Hybrid                                                    |
|**Lifecycle Phases**   |Day Zero Baseline, Periodic Audit                         |
|**Responsible Actors** |Deployer                                                  |
|**Maturity**           |Established                                               |
|**Outcome Type**       |Proximal                                                  |
|**Applicability**      |General Healthcare AI                                     |
|**Source**             |[NHSE-IG-Guidance-2026-03]; [CQC-Mythbuster-109] context|

**Why this tier?**

> Direct compliance requirement. Measurable via patient survey sampling, consultation audit, or (with appropriate consent) recording sampling. Binary compliance - notification either happened or it didn't.

**Formal Definition**

```
Compliance Rate = |consultations_with_verbal_notification_delivered| / |total_AVT_consultations|. Measurement methods in order of increasing rigour: (a) clinician self-report at end of session; (b) patient survey sampling asking whether notification was delivered; (c) audit of audio recordings (where retention allows) for notification language. Target: 100%. Values below 95% indicate systematic compliance failure requiring intervention.
```

**Reference Standard**

> The deployer-approved patient notification script (drawn from [NHSE-IG-Guidance-2026-03] + local DPIA). A consultation counts as "notified" only if the script's required content elements were delivered to the patient before AVT activation:
>
> - **What** the technology is (ambient scribe / AI-assisted documentation) and what it does
> - **What** is captured (audio + transcript) and where it goes
> - **Who** has access (clinician, vendor, sub-processors)
> - **How** to decline (without service consequence)
>
> A notification missing any of the four content elements counts as non-compliant even if some notification language was used. The most rigorous measurement method available at the deployment site is the gold standard; methods (a)-(c) are ranked by reliability and the headline rate must be reported with the method declared.

**Operational Specification**

> - **Window:** monthly, with quarterly periodic audit using the highest-rigour method available.
> - **Population:** all AVT consultations during the window (denominator excludes consultations where AVT was not used, including patient-opt-out cases).
> - **Method declaration MANDATORY:** the headline compliance rate carries the measurement method (self-report / patient survey / audio audit). Reporting "Compliance: 98 %" without method is not Tier 1 sufficient.
> - **Sample size for survey or audit MANDATORY:** ≥ 30 patients per clinician per quarter for survey method; ≥ 30 audio recordings per clinician per quarter where audio audit is used. Sub-30 samples are uninformative and do not satisfy the metric.
> - **Content-element breakdown MANDATORY:** report compliance per content element (what / what / who / how). A clinician who consistently omits "how to decline" is failing differently from one who omits "where it goes"; aggregate-only reporting hides the failure pattern.

**Trigger Conditions**

> ⚠️ **Provenance:** the four content-element framing (what / what / who / how) follows from [NHSE-IG-Guidance-2026-03]. Specific numerical thresholds (≥ 95 % self-report, ≥ 90 % audited, ≥ 85 % per-element, < 75 % escalation, ≥ 30 sample-size floor) are **proposed in v3.3 as starting points**, not externally validated. Indicative; require local calibration before contractual use.
>
> - **Pre-deployment gate:** notification script drafted and reviewed against [NHSE-IG-Guidance-2026-03] content elements; clinician training complete; one mock-consultation audit per clinician confirms script delivery.
> - **Continuous monitoring:** monthly self-report compliance ≥ 95 %; quarterly survey-based or audio-based compliance ≥ 90 % overall and ≥ 85 % on every content element.
> - **Pause / escalation trigger:** any content element < 75 % compliance in any audit cycle; or self-report > 95 % paired with audited rate < 75 % (this is a self-report integrity failure, separately serious).
>
> Specific numerical starting points are deployment-context-dependent and live in [Threshold Reference: GV.CR-2](../thresholds.md#gv-cr-2). Treat them as starting points to calibrate locally — not as contractual gates.



**Limitations**

> Self-report over-estimates compliance. Patient recall is imperfect. Audio audit is resource-intensive and depends on retention policies that may conflict with data minimisation. The Operational Specification's method-declaration requirement makes the self-report bias visible by forcing the audited cross-check.

**Novel Thinking / Implications**

> 💡 The gap between policy and practice on patient notification is the compliance equivalent of the consent understanding gap. A practice can have a 100% notification policy and a 60% actual notification rate - and the 40% gap is where the consent model breaks down. Periodic audit is the only way to know which side of the gap a deployer is on. A practice that refuses to audit is implicitly choosing not to know.

---

### GV.CR-3 🟢 AI-Generated Content Labelling Compliance

Automated verification that AI-generated clinical record entries carry the mandatory SNOMED suffix identifying them as AVT output (e.g. "Audio Dictation 24771000000105" per NHSE guidance). Required for downstream systems to distinguish AI-generated content from clinician-authored content - essential for audit, safety investigation, and future training data curation.

|Dimension              |Value                                                     |
|-----------------------|-----------------------------------------------------------|
| **Reference** | GV.CR-3 |
|**Priority Tier**      |🟢 Tier 1 - Minimum Viable                                 |
|**Measurement Cadence**|Continuous                                                 |
|**Pipeline Layer**     |Downstream Write-back |
|**Assurance Question** |Meta-evaluation                                            |
|**Measurement Method** |Computational                                              |
|**Lifecycle Phases**   |Pre-deployment, Continuous                                 |
|**Responsible Actors** |Vendor, Deployer                                           |
|**Maturity**           |Established                                                |
|**Outcome Type**       |Proximal                                                   |
|**Applicability**      |General Healthcare AI                                      |
|**Source**             |[NHSE-IG-Guidance-2026-03]                                 |

**Why this tier?**

> Automated compliance check with trivial implementation cost. Should be a pre-deployment gate and continuous monitoring metric. Non-compliance is both a governance failure and a downstream data quality problem.

**Formal Definition**

```
Labelling Rate = |AI_generated_entries_with_correct_suffix| / |total_AI_generated_entries|. Target: 100%. Zero-tolerance - every AI-generated entry must be labelled. Automated verification is feasible because the suffix is a fixed SNOMED concept that either appears or doesn't. Report non-compliance instances for immediate remediation.
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

> Assumes the vendor's write-back system supports the suffix - some EPR integrations strip metadata fields that don't map to native EPR structures. The suffix location (free-text vs metadata) affects automated detection methodology.

**Novel Thinking / Implications**

> 💡 Without reliable labelling, every downstream system that consumes clinical records is operating without knowing which content is AI-generated. This matters for: safety investigation (was the error in a human-written or AI-generated entry?); training data curation (if AI-generated records are fed back into training, the labelling is necessary to detect and exclude them); audit trails (which clinicians rely on AI assistance and how frequently). Non-labelling is an infrastructure failure with cascading consequences.

---

### GV.CR-4 🟢 AVT Supplier Registry Listing Verification

Procurement and ongoing verification that the deployed AVT system is listed on the NHS England AVT Supplier Registry and remains listed throughout the deployment lifecycle. The Registry (launched January 2026) is the NHS-level mechanism for self-certified minimum standards, and registry status is expected to become a procurement precondition.

|Dimension              |Value                                                 |
|-----------------------|------------------------------------------------------|
| **Reference** | GV.CR-4 |
|**Priority Tier**      |🟢 Tier 1 - Minimum Viable                             |
|**Measurement Cadence**|Continuous                                            |
|**Pipeline Layer**     |Cross-cutting                                         |
|**Assurance Question** |Safety                                                |
|**Measurement Method** |Human Review                                          |
|**Lifecycle Phases**   |Pre-deployment, Continuous                            |
|**Responsible Actors** |Deployer, Vendor                                      |
|**Maturity**           |Established                                           |
|**Outcome Type**       |Proximal                                              |
|**Applicability**      |AVT-Specific                                          |
|**Source**             |[NHSE-AVT-Registry] (live since January 2026)         |

**Why this tier?**

> Procurement gate with trivial verification cost. Should be confirmed at procurement and re-verified at contract renewal and on notification of vendor compliance events.

**Formal Definition**

```
Listing Verification: at procurement, confirm vendor is on the live Registry. Quarterly re-verification during deployment. Binary: listed or not listed. Where not listed, deployment should not proceed (pre-deployment) or should trigger formal risk review (during deployment). Also track: date of most recent vendor compliance attestation, scope of attested compliance (which AVT products are covered).
```

**Reference Standard**

> [NHSE-AVT-Registry] is the authoritative source — operational location at digital.nhs.uk/services/ambient-scribing (long-read context also hosted on the NHS Transformation Directorate site). **Listing is binary** (listed / not listed) at the registry-status level. **Scope** is read from the vendor's registry submission (which AVT products are covered, which use cases, which deployment contexts) and compared against the deployer's contracted scope. **Attestation date** is read from the vendor's signed declaration on the Hub. See also the cross-cutting [NHS England AVT Self-Certified Supplier Registry](#nhs-england-avt-self-certified-supplier-registry) standards-mapping section for the framework-level treatment, and the registry-driven companion metrics [GV.SC-12 Cyber Essentials Plus Certification Status](#gv-sc-12), [GV.VT-13 Evidence Pack Freshness](#gv-vt-13), and [GV.VT-14 Indicative Pricing Transparency](#gv-vt-14).

**Operational Specification**

> - **Window:** at procurement decision; quarterly re-verification during deployment; ad-hoc re-verification on any vendor change-event per [GV.SG-1 Model Version Tracking](#gv-sg-1).
> - **Three sub-metrics MANDATORY:** (a) listing status (binary); (b) scope alignment with deployer's contracted use cases (vendor's registry-submission scope is a superset of deployer's contracted scope); (c) attestation currency (vendor's signed declaration ≤ 12 months old). Aggregate-only reporting hides the failure pattern.
> - **Self-certification disclosure MANDATORY:** every quarterly verification record carries an explicit reminder that the registry is self-certified (NHSE preliminary checks only; no endorsement). Pair with [GV.VT-13 Evidence Pack Freshness](#gv-vt-13) for the substantive evidence-pack-quality assessment.
> - **Multi-product handling:** for vendors with multiple AVT products, the verification records the specific product covered. A vendor's overall registry listing does not transfer to a sibling product without explicit registry-submission scope coverage.
> - **Delisting watch:** the deployer's IG file records the registry status at each verification; any change from listed to not-listed (or vice versa) triggers an explicit governance review.

**Trigger Conditions**

> ⚠️ **Provenance:** the binary registry status, the 12-month attestation currency window, and the quarterly re-verification cadence are cited from the NHS England registry mechanics. The "12-month signed declaration" threshold and the multi-product scope-alignment requirement are **proposed in v3.8 as starting points**, not externally validated by NHSE — registry's specific re-listing rules are still pending publication. Per the [Calibration & Context principle](#calibration-context), require local calibration against the deployer's procurement risk appetite before contractual use.
>
> - **Pre-deployment gate:** vendor listed on live Registry; vendor's registry-submission scope covers deployer's contracted use cases; vendor's signed declaration ≤ 12 months old; companion metrics ([GV.VT-13](#gv-vt-13), [GV.VT-14](#gv-vt-14), [GV.SC-12](#gv-sc-12)) all pass their pre-deployment gates.
> - **Continuous monitoring:** quarterly verification of all three sub-metrics; alert on attestation > 9 months old (60-day grace); alert on any scope-coverage gap discovered post-procurement.
> - **Pause / escalation trigger:** vendor delisted (single instance — registry status loss is governance-event-grade); OR contracted use case discovered outside vendor's registry-submission scope; OR attestation > 12 months and not renewed.
>
> Specific numerical starting points are deployment-context-dependent and live in [Threshold Reference: GV.CR-4](../thresholds.md#gv-cr-4). Treat them as starting points to calibrate locally — not as contractual gates.



**Limitations**

> Registry is self-certified - listing indicates vendor attestation rather than independent verification. Listing scope may not cover all deployed AVT modules from a vendor with multiple products. The Operational Specification's self-certification disclosure makes this explicit at every verification, but does not eliminate the structural asymmetry. Substantive evidence-quality assessment lives in [GV.VT-13 Evidence Pack Freshness](#gv-vt-13); this metric verifies the listing fact, not the underlying evidence pack.

**Novel Thinking / Implications**

> 💡 The Registry's value depends on NHS bodies treating listing as a procurement precondition. If deployments proceed with non-listed vendors, the Registry becomes advisory rather than normative and loses its governance function. Making Registry verification a Tier 1 metric supports the norm that listing is expected - and creates visible data on deployment-to-listing alignment that can inform Registry policy over time.

---

### GV.CR-5 🟢 ICB Engagement Documentation

Documented evidence that the deployer engaged with their ICB digital team (or equivalent regional body) before AVT deployment, as required by the CIO/CCIO guidance (v2, January 2026). The ICB engagement requirement exists to prevent uncoordinated deployment across an integrated care system and to ensure regional intelligence about AVT risks and mitigations is applied consistently.

|Dimension              |Value                                                       |
|-----------------------|-------------------------------------------------------------|
| **Reference** | GV.CR-5 |
|**Priority Tier**      |🟢 Tier 1 - Minimum Viable                                   |
|**Measurement Cadence**|One-off gate                                                 |
|**Pipeline Layer**     |Cross-cutting                                                |
|**Assurance Question** |Meta-evaluation                                              |
|**Measurement Method** |Human Review                                                 |
|**Lifecycle Phases**   |Pre-deployment                                               |
|**Responsible Actors** |Deployer, Regional (ICB)                                     |
|**Maturity**           |Established                                                  |
|**Outcome Type**       |Proximal                                                     |
|**Applicability**      |General Healthcare AI                                        |
|**Source**             |[CIO-CCIO-Guidance-2026]; NHS CIO priority notification|

**Why this tier?**

> Pre-deployment compliance requirement. Should be a documented gate before go-live. Failure indicates a governance process breakdown that deserves immediate correction.

**Formal Definition**

```
Engagement documentation includes: (1) formal notification to ICB digital team dated before go-live; (2) ICB response acknowledging notification; (3) any conditions or recommendations from ICB on file. Binary compliance: all three present = compliant. Missing ICB response is a flag for follow-up, not automatic non-compliance, because ICB capacity constraints may prevent timely response.
```

**Reference Standard**

> Authoritative source: the deployer's governance file plus ICB digital team's correspondence record. "Formal notification" = a written communication to the named ICB digital lead (not generic inbox) containing at minimum: vendor identity, product scope, deployment site list, intended go-live date, DPIA reference, and Clinical Safety Case reference. "ICB response" = any written acknowledgement, including auto-receipts where the ICB has explicitly designated them as acknowledgements; substantive review responses are tracked separately as "ICB conditions". A response received after go-live counts but is recorded with the latency.

**Operational Specification**

> - **Window:** one-off pre-deployment gate; quarterly re-verification when material scope changes (new sites, new vendor product, new use case).
> - **Population:** every AVT deployment by the practice / Trust / federation. The denominator is deployments, not consultations.
> - **Three sub-metrics MANDATORY:** notification-sent rate, ICB-acknowledged rate, ICB-conditions-on-file rate. Aggregate-only reporting is not Tier 1 sufficient — the three failure modes (deployer didn't notify / ICB didn't acknowledge / conditions exist but not actioned) require separate visibility.
> - **Latency reporting MANDATORY:** time-to-notification (deployment-decision to ICB notification) and time-to-acknowledgement (notification to ICB response). Latency reveals process health independently of binary compliance.
> - **Carve-out logging MANDATORY:** any deployment proceeding without ICB acknowledgement (under the capacity-constraint allowance) MUST be logged with reason and review date. Repeated unanswered notifications to the same ICB within 12 months trigger escalation to the regional CCIO, not silent acceptance.

**Trigger Conditions**

> ⚠️ **Provenance:** the three-sub-metric framing follows from [CIO-CCIO-Guidance-2026] and the carve-out logic in the existing Formal Definition. Specific numerical thresholds (≥ 14-day notification lead time, escalation after two unanswered notifications in 12 months, quarterly re-verification cadence) are **proposed in v3.5 as starting points**, not externally validated. Indicative; require local calibration before contractual use.
>
> - **Pre-deployment gate:** notification sent to named ICB digital lead ≥ 14 days before planned go-live; DPIA + Clinical Safety Case referenced; deployment-site list complete.
> - **Continuous monitoring:** quarterly review of acknowledgement rate and conditions-on-file rate; alert when any ICB has > 1 unanswered notification on the deployer's books.
> - **Pause / escalation trigger:** any deployment going live without notification sent (process failure, not capacity issue); OR same ICB unanswered for ≥ 2 separate notifications within 12 months (escalate to regional CCIO).
>
> Specific numerical starting points are deployment-context-dependent and live in [Threshold Reference: GV.CR-5](../thresholds.md#gv-cr-5). Treat them as starting points to calibrate locally — not as contractual gates.



**Limitations**

> ICB engagement quality varies - some ICBs have mature digital teams providing substantive review; others acknowledge notifications without meaningful engagement. Documentation presence does not guarantee engagement quality. The Operational Specification's separate sub-metric for ICB-conditions-on-file makes substantive engagement visible (it surfaces only when the ICB has actually reviewed), but the metric still cannot distinguish deep review from cursory acknowledgement.
>
> The escalation-to-regional-CCIO trigger in the Threshold Guidance assumes regional CCIO capacity exists to receive and act on escalations. [CIO-CCIO-Guidance-2026] does not mandate or fund that capacity, so in regions where it is absent the metric's escalation pathway is non-operational — failed acknowledgements pile up at the next layer rather than being resolved. Where this is the case, deployers should document the gap in their governance file and surface it via routes other than this metric (e.g. ICS digital risk register).

**Novel Thinking / Implications**

> 💡 ICB engagement is the mechanism that prevents NHS AVT deployment from being a series of disconnected practice-level decisions with no regional coordination. It only works if it is actually happening - and practices deploying AVT without ICB engagement are a visible symptom of governance friction, ICB capacity constraints, or deployment urgency overriding process. Tracking the metric is a diagnostic tool for that friction as much as it is a compliance check.

---

### GV.CR-6 🟢 Clinical Safety Case Completeness

Existence, currency, and coverage of a formal DCB0129/0160 clinical safety case for the AVT deployment. Distinct from the existing Hazard Log Completeness metric, which covers log currency. Safety Case Completeness is the broader document: hazard identification, risk analysis, mitigations, residual risk acceptance, and governance arrangements. A 2025 FOI-based study (PubMed 41172285) found widespread non-compliance with DCB0129 requirements among NHS digital health deployments.

|Dimension              |Value                                                                                            |
|-----------------------|-------------------------------------------------------------------------------------------------|
| **Reference** | GV.CR-6 |
|**Priority Tier**      |🟢 Tier 1 - Minimum Viable                                                                        |
|**Measurement Cadence**|Periodic audit                                                                                   |
|**Pipeline Layer**     |Cross-cutting                                                                                    |
|**Assurance Question** |Safety                                                                                           |
|**Measurement Method** |Human Review                                                                                     |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                                                   |
|**Responsible Actors** |Deployer                                                                                         |
|**Maturity**           |Established                                                                                      |
|**Outcome Type**       |Proximal                                                                                         |
|**Applicability**      |General Healthcare AI                                                                            |
|**Source**             |[DCB0129] / [DCB0160]; [PubMed-41172285-FOI-Study]|

**Why this tier?**

> Direct regulatory requirement. Non-compliance is both a legal and a safety issue. The 2025 FOI study found widespread non-compliance, making this a known high-risk area requiring active monitoring.

**Formal Definition**

```
Completeness assessed against DCB0129 standard sections: (1) safety management system; (2) hazard identification; (3) hazard analysis and evaluation; (4) hazard control; (5) hazard log; (6) safety case report; (7) safety incident management; (8) issue resolution. Each section binary (present and current / missing or out-of-date). Full compliance requires all sections. Currency: major update triggered by significant system change, model version change, or new hazard identification.
```

**Reference Standard**

> [DCB0129] (Clinical Risk Management for Health IT Systems) is the authoritative section schema for vendors / manufacturers. The deployer-side equivalent [DCB0160] governs the safety case for the implementing institution and is the cross-reference for sites operating their own safety case (see also [Clinical Safety Officer reviewer requirement under DCB0129/0160]). "Present" requires a section heading plus content authored by a named Clinical Safety Officer (CSO); template-only sections (heading present, body empty or "TBC") count as missing. "Current" requires last-update date within the metric's currency window per the Operational Specification below.

**Operational Specification**

> - **Window:** annual periodic audit; mandatory re-review on any of the four trigger events (significant system change, model version change in any component per [GV.SG-1 Model Version Tracking](#gv-sg-1), new hazard identification, scope expansion).
> - **Population:** every deployment site holding a safety case (typically Trust-level for hospitals, federation-level for primary-care networks).
> - **Per-section reporting MANDATORY:** the eight sub-metrics (one per DCB0129 section) reported separately. Aggregate-only reporting is not sufficient — the failure pattern matters: a site missing section 5 (hazard log) has a different compliance failure from one missing section 7 (incident management).
> - **Currency window MANDATORY:** sections (2) hazard identification, (3) analysis, (4) control, and (5) log MUST be updated within 30 days of any trigger event (the 30-day figure is proposed in v3.5 as a starting point; DCB0129 itself does not specify a numeric window — see Threshold Guidance Provenance). Section (1) safety management system, (6) safety case report, and (8) issue resolution MUST be reviewed at least annually. Section (7) safety incident management MUST be live-current (updated on each new incident per the existing process).
> - **Trigger-event log MANDATORY:** every trigger event recorded with date, type, sections requiring update, and target completion date. Time-to-update reported per trigger.
> - **External review:** independent CSO review of the safety case at intervals not exceeding 24 months OR on any major version change of the AVT product. Internal-only review is not Tier 1 sufficient.

**Trigger Conditions**

> ⚠️ **Provenance:** the eight-section schema and currency triggers carry from [DCB0129] itself. Specific numerical thresholds (30-day post-trigger window, 24-month external review cadence, 100 % per-section currency gate) are **proposed in v3.5 as starting points**, not externally validated. The 2025 PubMed FOI study (cited in Source) found widespread non-compliance; these thresholds reflect a procurement-grade interpretation of "current" rather than a regulator-published standard. Indicative; require local calibration against the deployer's clinical risk management framework before contractual use.
>
> - **Pre-deployment gate:** all eight [DCB0129] sections present with named CSO author; safety case report explicitly references the AVT product version, EPR target, and deployment scope.
> - **Continuous monitoring:** annual per-section review; alert when any of sections 2-5 falls outside the 30-day post-trigger window; alert when external review is overdue.
> - **Pause / escalation trigger:** any section in "missing" state (heading present, content empty or stub); OR sections 2-5 unupdated > 90 days after a trigger event; OR any model-version change deployed without corresponding safety-case update (cross-link [SI-2024-1368] MHRA PMS substantial-change framework).
>
> Specific numerical starting points are deployment-context-dependent and live in [Threshold Reference: GV.CR-6](../thresholds.md#gv-cr-6). Treat them as starting points to calibrate locally — not as contractual gates.



**Limitations**

> Compliance with structure does not guarantee quality of content. Safety cases are often written to satisfy the standard rather than to genuinely analyse system safety - the "compliance theatre" problem. External independent review is the only reliable check; the Operational Specification's 24-month external-review cadence makes this requirement explicit but does not eliminate the gap between structural compliance and genuine safety analysis.

**Novel Thinking / Implications**

> 💡 The 2025 FOI finding that many NHS digital health deployments lack DCB0129 compliance is a structural warning about regulatory enforcement gaps. AVT deployment is happening faster than safety case development in many places. Making Safety Case Completeness a Tier 1 metric both highlights the compliance obligation and creates visible data on how widespread the gap is - which is itself a governance intervention.

---

### GV.CR-7 🟢 DPIA Template Completion Rate

Proportion of AVT deployments using the NHS-provided March 2026 DPIA template with all mandatory sections completed. Data Protection Impact Assessment is required under UK GDPR Article 35 for high-risk processing, and AVT meets the high-risk threshold. The NHSE template provides standardised structure - but the template only helps if it's actually used and completed.

|Dimension              |Value                                                 |
|-----------------------|------------------------------------------------------|
| **Reference** | GV.CR-7 |
|**Priority Tier**      |🟢 Tier 1 - Minimum Viable                             |
|**Measurement Cadence**|Periodic audit                                        |
|**Pipeline Layer**     |Cross-cutting                                         |
|**Assurance Question** |Safety                                                |
|**Measurement Method** |Human Review                                          |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                        |
|**Responsible Actors** |Deployer                                              |
|**Maturity**           |Established                                           |
|**Outcome Type**       |Proximal                                              |
|**Applicability**      |General Healthcare AI                                 |
|**Source**             |[UK-GDPR] Article 35; [NHSE-IG-Guidance-2026-03] template|

**Why this tier?**

> Legal requirement. Pre-deployment gate. Template completion is measurable and binary.

**Formal Definition**

```
Completion Rate = |deployments_with_complete_DPIA_using_template| / |total_AVT_deployments|. Template mandatory sections: processing description, lawful basis, data flows, risks identified, mitigations, residual risk acceptance, DPO sign-off, review schedule. Each section binary; complete DPIA requires all sections. Review cadence: minimum annually or on significant processing change.
```

**Reference Standard**

> The [NHSE-IG-Guidance-2026-03] DPIA template is the authoritative section schema for AVT deployments; [UK-GDPR] Article 35 is the legal floor. "Complete" requires every mandatory section populated with substantive content, signed off by the named Data Protection Officer (DPO). Template-only sections (heading present, body empty, "TBC", or boilerplate copied from the template's example text) count as incomplete. Cross-link to [GV.CR-6 Clinical Safety Case Completeness](#gv-cr-6) — DPIA risks identified MUST be reconcilable with hazards in the safety case; gaps between the two are themselves a quality signal.

**Operational Specification**

> - **Window:** annual periodic audit; mandatory re-review on significant processing change (defined: new vendor, new data flow, new sub-processor, new use case, model component change per [GV.SG-1](#gv-sg-1), site expansion).
> - **Population:** every AVT deployment (denominator: deployments, not consultations).
> - **Per-section reporting MANDATORY:** the eight mandatory sections (processing description, lawful basis, data flows, risks identified, mitigations, residual-risk acceptance, DPO sign-off, review schedule) reported separately. Aggregate-only reporting hides sectional failure patterns.
> - **Significant-change definition MANDATORY:** the deployer's local definition of "significant processing change" must be documented; ambiguity here is a common failure mode for the metric. Default rule: any change requiring sub-processor disclosure update under [GV.VT-7](#gv-vt-7) is significant by definition.
> - **DPO sign-off MANDATORY (binary):** unsigned DPIAs do not count as complete regardless of section content. Sign-off date recorded; sign-offs preceding the most recent significant change are stale.
> - **Cross-reconciliation with safety case:** DPIA-identified risks MUST be cross-mapped to safety-case hazards; risks named in DPIA but absent from safety case (or vice versa) are flagged in the audit output.

**Trigger Conditions**

> ⚠️ **Provenance:** the eight-section schema and DPO sign-off requirement carry from [UK-GDPR] Article 35 and the [NHSE-IG-Guidance-2026-03] template. Specific numerical thresholds (annual audit cadence, 30-day post-significant-change re-review window, 100 % per-section gate) are **proposed in v3.5 as starting points**, not externally validated. Indicative; require local calibration against the deployer's IG framework before contractual use.
>
> - **Pre-deployment gate:** all eight template sections complete with substantive content; DPO sign-off dated within the 30 days preceding go-live; DPIA-safety-case reconciliation documented.
> - **Continuous monitoring:** annual completion-rate review; alert on any DPIA where sign-off precedes the most recent significant change; alert when DPIA-safety-case reconciliation reveals unaligned risk/hazard list.
> - **Pause / escalation trigger:** any deployment going live without a DPO-signed DPIA (legal failure, not process); OR any DPIA stale > 12 months past a significant change without re-review (regulatory exposure).
>
> Specific numerical starting points are deployment-context-dependent and live in [Threshold Reference: GV.CR-7](../thresholds.md#gv-cr-7). Treat them as starting points to calibrate locally — not as contractual gates.



**Limitations**

> Template compliance doesn't guarantee substantive risk analysis. "Completed" DPIAs that list "no residual risks identified" for a novel AVT deployment are likely inadequate regardless of template adherence. The Operational Specification's reconciliation-with-safety-case requirement creates a partial check on substantive quality (a DPIA that names no risks while the safety case names hazards is automatically flagged), but the gap between section-completion compliance and genuine analysis remains.

**Novel Thinking / Implications**

> 💡 The NHSE template provides common structure across deployments, which has three benefits: (1) makes comparison possible across sites, (2) ensures mandatory considerations aren't missed, (3) creates an evidence base for national-level risk analysis. Template non-use isn't necessarily non-compliance with UK GDPR (bespoke DPIAs can be legitimate) but it loses the aggregation benefit. Tracking template use rate is a proxy for how consistently the governance infrastructure is being built.

---

### GV.CR-8 🟡 DSPA Status

Existence and currency of Data Sharing/Processing Agreements with all data processors involved in AVT operation. UK GDPR Article 28 requires written agreements with processors, and cloud-hosted AVT typically involves multiple processors (primary vendor, cloud provider, model provider, annotation services). Related to the existing Sub-Processor Transparency metric but specifically focuses on the contractual agreements rather than the disclosure of sub-processors.

|Dimension              |Value                                         |
|-----------------------|----------------------------------------------|
| **Reference** | GV.CR-8 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                        |
|**Measurement Cadence**|Periodic audit                                |
|**Pipeline Layer**     |Cross-cutting                                 |
|**Assurance Question** |Safety                                        |
|**Measurement Method** |Human Review                                  |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                |
|**Responsible Actors** |Deployer, Vendor                              |
|**Maturity**           |Established                                   |
|**Outcome Type**       |Proximal                                      |
|**Applicability**      |General Healthcare AI                         |
|**Source**             |[UK-GDPR] Article 28; NHS data protection guidance|

**Why this tier?**

> Legal compliance requirement. Annual audit recommended. Slightly lower tier than DPIA because absence of DSPA is more commonly an oversight than a structural governance failure - but still a legal requirement.

**Formal Definition**

```
DSPA Status per processor: (a) agreement in place (binary); (b) agreement currency (signed within last 2 years or since last significant change); (c) agreement covers all processing activities actually performed by that processor; (d) UK GDPR Article 28 mandatory clauses present. Full compliance requires all four per processor. Aggregate metric: |processors_fully_compliant| / |total_processors|.
```

**Limitations**

> Agreement existence doesn't guarantee processor compliance with the agreement. Cross-border processors may have limited enforceability. Complex sub-processor chains make coverage verification difficult.

**Novel Thinking / Implications**

> 💡 DSPAs are where the legal rubber meets the road. A deployer with a DPIA but no DSPAs has documented the risks without contractually binding the processors to manage them. This is a common gap because DPIAs are visible in NHS audit processes while DSPAs are often handled by legal departments outside the IG team's line of sight.

---

### GV.CR-9 🟡 FDA PCCP-Equivalent Pre-Defined Acceptance Criteria

Whether the vendor has pre-specified quantitative acceptance criteria that any model update must meet before being deployed to production. FDA Predetermined Change Control Plans (finalised December 2024) require this for US-market medical device AI. Even in UK-only deployments, it matters because: (1) EU-market vendors cascade similar requirements through the EU AI Act, and (2) the existence of pre-defined acceptance criteria is a proxy for mature change control regardless of regulatory jurisdiction.

|Dimension              |Value                                                   |
|-----------------------|---------------------------------------------------------|
| **Reference** | GV.CR-9 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                                   |
|**Measurement Cadence**|One-off gate                                             |
|**Pipeline Layer**     |Cross-cutting                                            |
|**Assurance Question** |Safety                                                   |
|**Measurement Method** |Human Review                                             |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                           |
|**Responsible Actors** |Vendor                                                   |
|**Maturity**           |Emerging                                                 |
|**Outcome Type**       |Proximal                                                 |
|**Applicability**      |General Healthcare AI                                    |
|**Source**             |[FDA-PCCP-Guidance-2024]; [EU-AI-Act] Article 15; [NICE-ESF] 2022 AI updates|

**Why this tier?**

> Procurement assessment. Should be standard due diligence for any AVT acquisition. Vendors without PCCP-equivalent frameworks are a higher governance risk.

**Formal Definition**

```
Assessment against criteria: (1) Performance acceptance thresholds pre-specified and quantitative; (2) Regression test suite defined and maintained; (3) Fairness/equity criteria included in acceptance testing; (4) Rollback procedure specified if update fails acceptance post-deployment; (5) Documentation of acceptance decisions available for audit. Binary per criterion; full compliance = all five.
```

**Limitations**

> Vendors may claim PCCP equivalence without independent verification. The substantive quality of acceptance criteria matters more than their existence - a criterion like "WER not more than 20% worse" technically exists but provides no meaningful safety floor.

**Novel Thinking / Implications**

> 💡 PCCP is a structural shift in how AI medical devices are regulated - from approving specific models to approving the change control process. For AVT specifically, this is essential because continuous model improvement is expected, and ad-hoc change control makes every update a regulatory event. NHS procurement should treat PCCP-equivalent frameworks as the baseline expectation, not a differentiator, even though the formal PCCP framework applies to US-market devices.

---

### GV.CR-10 🟡 EU AI Act Event Logging Compliance

Compliance with EU AI Act Article 12 automatic event logging requirements for high-risk AI systems. High-risk provisions became effective August 2026. Applies to any AVT vendor with EU market exposure, and cascades into UK deployment because vendors typically apply the strictest applicable regulatory regime uniformly across their product rather than maintaining jurisdiction-specific variants.

|Dimension              |Value                                              |
|-----------------------|----------------------------------------------------|
| **Reference** | GV.CR-10 |
|**Priority Tier**      |🟡 Tier 2 - Recommended                              |
|**Measurement Cadence**|Continuous                                          |
|**Pipeline Layer**     |Cross-cutting                                       |
|**Assurance Question** |Safety                                              |
|**Measurement Method** |Computational                                       |
|**Lifecycle Phases**   |Pre-deployment, Continuous                          |
|**Responsible Actors** |Vendor                                              |
|**Maturity**           |Emerging                                            |
|**Outcome Type**       |Proximal                                            |
|**Applicability**      |General Healthcare AI                               |
|**Source**             |[EU-AI-Act] Article 12 (high-risk provisions effective August 2026)|

**Why this tier?**

> Vendor-side regulatory requirement. Deployer should verify event logging infrastructure exists and receive logs for foreseeable-misuse investigation. Important for incident investigation capability.

**Formal Definition**

```
Event logging must capture: (1) period of use (start, duration, stop per session); (2) reference database used; (3) input data that led to output; (4) natural persons involved in verification of output. Logging must be automatic, not opt-in. Retention period specified in vendor policy and aligned with EU AI Act minimums. Deployer verification: can the vendor provide a complete event log for any given encounter on request within a reasonable timeframe?
```

**Limitations**

> Full logging creates large data volumes and storage costs. Logging of input data conflicts with data minimisation principles - resolving this requires careful policy design. Deployer verification is manual and sample-based.

**Novel Thinking / Implications**

> 💡 Event logging is the infrastructure that supports retrospective incident investigation. Without it, when an AVT error causes harm six months after the fact, the investigation has nothing to work with - the clinician may not remember the encounter, the patient certainly won't remember the AI's behaviour, and the vendor has no logs to reconstruct what happened. The EU AI Act requirement is essentially mandating the infrastructure for forensic investigation of AI clinical systems, which is a governance improvement regardless of jurisdiction.
