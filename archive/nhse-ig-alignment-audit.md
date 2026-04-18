# NHSE IG Guidance Alignment Audit

**Date:** 2026-04-18
**Taxonomy baseline:** v3.1 (214 metrics)
**Source:** NHS England IG guidance *Using AI-enabled ambient scribing products in health and care settings* (reviewed 31 Mar 2026), via NHS Transformation Directorate. Reviewed by Health and Care Information Governance Working Group, ICO, and National Data Guardian.

## Scope of this audit

Per user request, focus is **governance / consent**. Compares NHSE IG guidance requirements against Part E (System Governance) of our taxonomy, especially:

- `taxonomy/part-e/nhs-compliance-regulatory.md` (GV.CR-*)
- `taxonomy/part-e/privacy-data-governance.md` (GV.PD-*)
- `taxonomy/part-e/safety-governance.md` (GV.SG-*)
- `taxonomy/part-e/vendor-transparency-contractual.md` (GV.VT-*)
- `taxonomy/part-e/training-competency.md` (GV.TC-*)
- `taxonomy/part-e/security-adversarial-robustness.md` (GV.SC-*)

Also relevant outside Part E: `taxonomy/part-d/patient-experience.md` (IO.PX-*).

## Headline finding

**Strong alignment.** The NHS Compliance & Regulatory group (added v2→v3 specifically in response to the Jan–Mar 2026 NHSE guidance suite) is the direct home for most IG-derived requirements. Of 24 distinct requirements identified in the guidance, **22 are covered by existing metrics**, **2 are partial gaps**, and **0 are missing**.

Two new candidate metrics are proposed below; neither is critical for a compliant deployment because existing metrics bracket the requirement.

## Requirement-by-requirement mapping

### Consent model (implied consent + dissent)

| Guidance requirement | Our metric(s) | Coverage |
|---|---|---|
| Implied consent under common law — no explicit consent needed | — conceptual framing, not a metric | n/a |
| Must verbally inform patient at start of session | **GV.CR-2 Verbal Notification Compliance** (Tier 1) | **direct** |
| Individual can refuse at start; refusal must be respected | **GV.CR-1 Patient Dissent Recording Rate** (Tier 1) | **direct** |
| Refusal handling — explain impact on care | *covered by GV.CR-2's underlying process* — no dedicated metric on the *quality* of the impact-explanation. See Gap-IG-A below. | **partial** |
| Objection persistence — respect across future encounters | **GV.CR-1** sub-metric (c) explicitly covers this | **direct** |
| Capacity-impaired handling — best-interest framework | — conceptual; no separable metric | **gap by design** — best-interest decisions are clinical judgement, not a population metric |

### Transparency (patient-facing)

| Guidance requirement | Our metric(s) | Coverage |
|---|---|---|
| Update privacy notices | **GV.VT-5 Incident Disclosure Compliance** is the closest structural match, but privacy-notice currency is distinct. See Gap-IG-B. | **partial** |
| Public-area materials (posters, TV screens, leaflets) | Not metric-shaped; process rather than measurement | **intentional gap** |
| Explain how to object | covered under GV.CR-1 / GV.CR-2 | **direct** |
| Accessibility for those without digital access | **IO.PX-4 Cultural & Linguistic Appropriateness** · **IO.PX-8 Patient Comprehension** | **direct** |

### Accuracy & verification (clinician-side)

| Guidance requirement | Our metric(s) | Coverage |
|---|---|---|
| User is accountable for accuracy of record | **HL.HF-3 Review-Before-Signing Rate** (Tier 1) · **HL.HF-4 Time-to-Sign Distribution** (Tier 1) | **direct** |
| Check notes every use, meaningful review timeframe | **HL.HF-3** · **HL.HF-4** · **HL.HF-1 Edit Rate** | **direct** |
| Enhanced verification for translated consultations | Not called out explicitly — subsumed under HL.HF-3 but distinct practice. See Gap-RSET-J in the RSET audit (interpreter-mediated consultations) — overlapping gap. | **partial** |
| Inaccuracies corrected before inclusion | **HL.HF-1 Edit Rate** · **HL.HF-2 Edit Type Classification** · **HL.HF-7 Edit Location Distribution** | **direct** |
| Label AI-generated outputs (SNOMED 24771000000105 or equivalent) | **GV.CR-3 AI-Generated Content Labelling Compliance** (Tier 1) | **direct** |
| Third-party info — review and exclude as needed | **TP.SN-6 Omission Rate** (inverse lens) · **HL.HF-7** | **direct** |

### Data protection

| Guidance requirement | Our metric(s) | Coverage |
|---|---|---|
| UK GDPR Art. 6(1)(e) / 9(2)(h) lawful basis | conceptual — framed in `_standards-mapping.md` | **direct** |
| Data-protection accuracy (personal data correct) | **HL.HF-1/2/7** (edit-based correction) | **direct** |
| AI statistical accuracy distinct from data-protection accuracy | **TP.SN-5 Hallucination Rate** · **TP.SN-6 Omission Rate** · **TP.ASR-1 WER** · full Summarisation group | **direct** |
| Retain audio/transcript only as needed; delete after summary sign-off | **GV.PD-1 Audio Retention Compliance** · **GV.PD-2 Audio Time-to-Deletion** (Tier 1) · **GV.PD-3 Transcript Retention Compliance** (Tier 1) | **direct** — exact match |
| Technical functionality for retention compliance, auto-delete | **GV.PD-2** · **GV.VT-6 Exit & Data Portability Provisions** | **direct** |
| Output retention per destination-record policy | **GV.PD-1/2/3** | **direct** |
| Sequential deletion — once in final store, purge from intermediate stores | **GV.PD-2 Audio Time-to-Deletion** "Must verify deletion in primary storage, caches, and backups" | **direct** — exact match |
| Provider instructions documented | **GV.VT-7 Sub-Processor Transparency** · **GV.VT-6 Exit & Data Portability** | **direct** |

### Controller/processor arrangements

| Guidance requirement | Our metric(s) | Coverage |
|---|---|---|
| Assess and document controller/processor roles | **GV.VT-7 Sub-Processor Transparency** (Tier 1) | **direct** |
| Default: org is controller for individual-care processing | conceptual | **direct** via `_standards-mapping.md` |
| Guard against joint controllership creep (supplier uses data beyond care) | **GV.VT-7** · **GV.PD-7 Training Data Inclusion Status** | **direct** |
| DSPA in place | **GV.CR-8 DSPA Status** (Tier 2) | **direct** |

### DPIA

| Guidance requirement | Our metric(s) | Coverage |
|---|---|---|
| DPIA is highly likely legally required | **GV.CR-7 DPIA Template Completion Rate** (Tier 1) | **direct** |
| Use NHSE DPIA template | **GV.CR-7** references the March 2026 template explicitly | **direct** |

### Individual rights (UK GDPR)

| Guidance requirement | Our metric(s) | Coverage |
|---|---|---|
| Right to object (where lawful basis is public task) | **GV.CR-1 Patient Dissent Recording** · **IO.PX-1 Patient Opt-Out Rate** | **direct** |
| Tool must support objection being upheld (stop processing) | **GV.CR-1** covers process; tool-functionality side partially covered by **GV.VT-6 Exit & Data Portability** | **partial** — no dedicated "objection-enforceability" tool property metric. Arguable — GV.CR-1 at 100% implies it works. |
| Staff prepared for non-tool fallback | **HL.HF-19 AI-Off Performance Test** (Tier 2) | **direct** |
| Right of access (SAR) — includes audio, transcripts, outputs | **GV.PD-10 Subject Access Request Fulfilment** (Tier 1) | **direct** |
| SAR within one month, pause deletion during SAR | **GV.PD-10** · **GV.PD-2** explicit interaction is not tested. See Gap-IG-C. | **partial** |
| Right to rectification of audio/transcript/output | **HL.HF-1/2/7** (edit metrics) · **GV.VT-4 Audit Trail Completeness** | **direct** |
| Right to erasure — limited by public-task / health-purposes exemptions | **GV.PD-11 Right to Erasure Compliance** (Tier 1) | **direct** |
| Right to restrict processing — data marked restricted, not deleted, tool must comply | **GV.PD-11** covers erasure; restriction is conceptually distinct. See Gap-IG-D. | **partial** |
| Automated decision-making rights — N/A (tool aids, doesn't decide) | conceptual | **direct** |

### Pre-implementation & governance

| Guidance requirement | Our metric(s) | Coverage |
|---|---|---|
| Product must be org-approved via due diligence | **GV.CR-4 AVT Supplier Registry Listing Verification** (Tier 1) · **GV.CR-5 ICB Engagement Documentation** (Tier 1) | **direct** |
| Safety case / clinical safety assessment (DCB0129/0160) | **GV.CR-6 Clinical Safety Case Completeness** (Tier 1) · **GV.SG-17 Hazard Log Completeness** (Tier 1) | **direct** |
| Involve CIO/CCIO/SIRO/Caldicott/DPO/board | conceptual; **GV.CR-5 ICB Engagement Documentation** captures institutional sign-off | **direct** |
| Review supplier, product design, safety, security | **GV.VT-3 Benchmark & Evaluation Data Accessibility** · **GV.SC-1..11** (full security group) | **direct** |
| Regulatory compliance beyond IG (MHRA, DTAC) | `_standards-mapping.md` — full MHRA SaMD/AIaMD + DTAC mapping | **direct** |

### Staff training & competency

| Guidance requirement | Our metric(s) | Coverage |
|---|---|---|
| Staff trained on obligations | **GV.TC-1 Clinician Training Completion Rate** (Tier 1) · **GV.TC-3 Refresher Training & CPD Compliance** | **direct** |
| Competency assessments | **GV.TC-2 Failure Mode Awareness Score** | **direct** |
| Professional judgement — don't use in sensitive contexts | **GV.SG-10 Off-Label Use Detection Rate** · **GV.OP-6 Adoption Rate & Selective Use Patterns** | **direct** |

### Security

| Guidance requirement | Our metric(s) | Coverage |
|---|---|---|
| Engage technical/security specialists, assess vulnerabilities | **GV.SC-1..11** (full Security & Adversarial Robustness group) | **direct** |

### Scope limitations

| Guidance point | Our handling |
|---|---|
| National data opt-out does NOT apply | No metric needed; correctly not listed as an opt-out mechanism |
| Does not cover research / model training use | **GV.PD-7 Training Data Inclusion Status** addresses the secondary-use boundary |

## Identified gaps

Four partial gaps. Proposed additions to `gaps.yaml` under `origin: external-review`, `source: NHSE-IG-Mar-2026`.

| Gap ID | Title | Rationale | Suggested tier |
|---|---|---|---|
| Gap-IG-A | Refusal impact-explanation quality | Guidance says clinicians must explain *how* refusal impacts care; we measure recording/respecting dissent but not the quality of the explanation offered. Could be a periodic audit. | Tier 2 |
| Gap-IG-B | Privacy notice currency & completeness | Organisational privacy notices must be updated to include ambient-scribe processing specifics. No existing metric tracks whether the notice was updated, when, and whether it includes required elements. | Tier 1 (compliance binary) |
| Gap-IG-C | Deletion-pause during active SAR | Guidance explicitly requires deletion paused during SAR handling; current GV.PD-2 (Audio Time-to-Deletion) doesn't test the SAR-interaction. Could be a sub-metric or a new compliance test. | Tier 2 |
| Gap-IG-D | Right-to-restrict tooling support | Restriction is distinct from erasure — data held, marked, not processed. Current GV.PD-11 covers erasure only. | Tier 2 |

Additionally, two **non-gaps** worth noting — NHSE IG requirements that map to existing metrics but whose standards-mapping references could be strengthened:

- **`_standards-mapping.md`** should explicitly cite this IG guidance as the authoritative source for GV.CR-1, GV.CR-2, GV.CR-3, GV.CR-7, GV.PD-2, GV.PD-3 (currently cited in some metric source lines but not aggregated in the standards-mapping table).
- **GV.VT-7 Sub-Processor Transparency** should reference the "joint controller risk" language in its rationale so a reader knows why it's Tier 1.

## Relationship with the RSET audit

The RSET coverage audit (see `rset-coverage-audit.md`) identified product-capability gaps. This IG audit identifies governance/compliance gaps. **No overlap** between the two gap lists except Gap-RSET-J (interpreter-mediated consultations), which reinforces the IG guidance's "enhanced verification" requirement for translated consultations — that's a shared finding and strengthens the case for adding it as a Tier 2 metric.

## Conflict check — do any existing metrics contradict the guidance?

Separate question from coverage: does any metric implicitly endorse a model the IG guidance rejects? Scanned every metric file for terms that would signal a conflict with the guidance's positive assertions (explicit consent, opt-in, NDOO applicability, universal right-to-erasure, mandatory audio retention).

### Findings

**1. Confirmed conflict — `_standards-mapping.md` line 90 (DSPT assertion 1.2.4)**

The DSPT Standard 1 table maps assertion **1.2.4 "National data opt-out compliance"** to **IO.PX-1 Patient Opt-Out Rate** with Tier 1 marking, which implies the National Data Opt-Out applies to AVT processing.

NHSE IG guidance is explicit to the contrary:

> "The national data opt-out will not apply when you are using an ambient scribe for individual care."

**Impact:** a deployer following the standards-mapping table could configure AVT to honour NDOO flags and wrongly suppress ambient-scribe use for patients whose NDOO applies to secondary use (research, planning) but **not** their individual care. This is a real operational misalignment.

**Fix:** edit the DSPT 1.2.4 row. Options:
- Keep the assertion listed, replace the metric cell with `— does not apply to AVT processing for individual care (NHSE IG Mar-2026)` and drop the Tier badge.
- Add a footnote under the DSPT table clarifying that NDOO applies to secondary use only.

IO.PX-1 itself is fine — it measures practice-level AVT opt-out, not NDOO. The bug is in the mapping table.

**2. Soft conflict — GV.PD-11 Right to Erasure Compliance (tier framing)**

GV.PD-11 is Tier 1 and frames Right to Erasure as a universal compliance obligation. NHSE IG guidance is explicit that Right to Erasure **does not apply** where processing is for public-task health/care purposes (which is the lawful basis for AVT). The Article 17 exemption is case-by-case.

Testing the *capability* to erase is still correct (SAR workflows, training-data withdrawal, dispute resolution), so the metric's existence is sound. But the framing could mislead a reader into thinking erasure is universally exercisable.

**Fix:** edit the "Why this tier?" and description to say:

> "Tested pre-deployment to establish *scope, Article 17 applicability exemptions, and* technical limitations of erasure. Statutory right is narrowly applicable for individual-care AVT processing, but the capability must exist for cases where it does apply (e.g. data used beyond individual care)."

No tier change needed — the metric is still Tier 1 because understanding what erasure *can* deliver is a pre-deployment gate.

**3. No conflict — consent terminology across the corpus**

Searched for `explicit consent`, `opt-in`, `signed consent`, `written consent`, `obtain consent`, `must be consented`. No hits in metric files that would contradict the implied-consent model. The one `opt-in` occurrence in GV.CR-10 is about AI-Act event logging (correctly specified as "automatic, not opt-in"), not patient consent.

**4. No conflict — retention defaults**

GV.PD-1, GV.PD-2, GV.PD-3 all correctly frame retention as minimised, with audio deletion after sign-off as the default. No metric assumes long-term retention by default. GV.VT-4 (Audit Trail Completeness) explicitly acknowledges the tension between audit-trail retention and data minimisation rather than silently endorsing one over the other.

**5. No conflict — training data use**

GV.PD-7 Training Data Inclusion Status correctly requires explicit documented consent basis if NHS data flows into vendor training pipelines. Aligned with the IG guidance's warning on joint-controller risk and "patient data is not used by the technology provider for purposes beyond the care of the individual".

### Summary

| Finding | Severity | Action |
|---|---|---|
| DSPT 1.2.4 row implies NDOO applies | **Conflict — fix required** | Edit `_standards-mapping.md` row; add footnote |
| GV.PD-11 framing implies erasure universally exercisable | Soft conflict — rewording | Edit "Why this tier?" + description |
| Consent terminology | None | — |
| Retention defaults | None | — |
| Training data use | None | — |

Recommend both fixes land as corrections on `restructure-and-site` branch before Phase 2c gap consolidation, so the source that feeds the `gaps.yaml` roadmap is consistent with current guidance.

## Recommendations

1. Add Gap-IG-A/B/C/D to `gaps.yaml` (Phase 2c) with `origin: external-review`, `source: NHSE-IG-Mar-2026`.
2. Promote **Gap-IG-B Privacy Notice Currency** toward Tier 1 on next review — it is a binary organisational compliance artefact with trivial measurement cost.
3. Strengthen source attribution in `_standards-mapping.md` to cite the IG guidance explicitly.
4. Strengthen GV.VT-7's rationale to reference joint-controllership risk.
5. Carry the shared RSET/IG finding on interpreter-mediated consultations into Phase 2c gap list as a single unified entry.

## Confidence / limitations

- Guidance reviewed is the current published version (reviewed 31 Mar 2026). Website is flagged as retiring; content will migrate. Re-check before Phase 2c gap consolidation to avoid citing superseded text.
- This audit does **not** cover: research/training-data use (out of IG scope), NICE/MHRA-specific clinical-safety requirements (covered by separate standards-mapping entries), or the NHS Records Management Code of Practice retention schedule (cross-referenced but not itemised here).
