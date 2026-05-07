## Gaps & Proposed Metrics (Roadmap)

Consolidated register of metrics not yet in the taxonomy but flagged during mapping, coverage audit, or policy-lens analysis. Nothing here has been added to the 214-metric catalogue - each entry is a *candidate*, tracked so future rounds can draw from one place instead of re-discovering gaps.

**Entry states:**
- `proposed` - identified, not yet reviewed for inclusion
- `accepted` - approved for a future metric round (awaiting full entry drafting)
- `deferred` - considered and set aside with reasoning; may revisit
- `rejected` - considered and dismissed; reasoning preserved so it's not re-raised

**Totals across origins:** 74 outstanding candidates (9 external-review accepted, 4 external-review deferred, 0 NHSE IG, 13 standards-mapping, 6 NHS T.E.S.T., 38 Responsible AI lens) plus 17 promoted-in-earlier-releases rows preserved at the bottom of this file (§7) for historical record. The build's `gap_count` ignores §7.

---

## 1. External Review (RSET + NHSE IG)

Derived from two external-source coverage audits (see `archive/rset-coverage-audit.md` and `archive/nhse-ig-alignment-audit.md`).

### 1a. Accepted - RSET taxonomy (9 candidates)

Gaps identified against the Nuffield Trust RSET AVT taxonomy (Feb 2026) - a product-capability checklist that complements our measurement taxonomy.

| Gap ID | Title | Suggested Tier | Rationale | Source |
|--------|-------|----------------|-----------|--------|
| Gap-RSET-E | AI-mediated editing modality integrity | 🟡 2 | Voice/chat-based editing introduces a second hallucination surface on top of the original summarisation. Distinct failure mode not covered by summary-edit metrics (HL.HF-1/2/7). | RSET #16 |
| Gap-RSET-F | Letter / referral generation quality | 🟡 2 | Patient-facing and clinician-facing letters are a discrete output class from summaries written to the EPR. Own failure modes (audience calibration, tone, clinical accuracy). Matches scoping-review "document turnaround" evidence gap. | RSET #21–22, Phase 1 slide deck |
| Gap-RSET-G | Contextual data fusion accuracy | 🟡 2 | When AVT pulls prior EHR content into the note, fidelity of that pull is distinct from within-consultation summarisation fidelity. Untested territory. | RSET #23, #37 |
| Gap-RSET-H | Task / action-item extraction accuracy | 🟡 2 | Separate construct from consultation summary: can misattribute, fabricate, or miss tasks. Downstream workflow impact. | RSET #25 |
| Gap-RSET-I | Disability-specific speech performance | 🟡 2 | Dysarthria, aphasia, hearing-impaired speech as explicit sub-populations. Current IO.FE-* covers general demographics but not disability-specific speech. Health-equity salience. | RSET #31 |
| Gap-RSET-J | Interpreter-mediated consultation performance | 🟢 1 | Explicitly flagged by NHSE IG guidance ("enhanced verification for translated consultations") - cross-validated by both external audits. Translation introduces distortion of speaker turns, content, and consent flow. Tier 1 because the IG guidance makes it a compliance expectation. | RSET #32, NHSE IG Mar-2026 |
| Gap-RSET-K | Offline-mode integrity | 🟡 2 | Everyday safety concern when connectivity drops mid-consultation: does the product fail safely, buffer with integrity, or silently degrade? Current GV.OP-5 covers uptime but not offline-mode semantics. | RSET #38 |
| Gap-RSET-L | Validated wellbeing-instrument metric | 🔵 3 | Named validated instruments (Maslach Burnout Inventory, Copenhagen Burnout) rather than ad-hoc surveys. Scoping review confirms the field is still using non-standardised self-reports. | Phase 1 slide deck p. 14 |
| Gap-RSET-M | Consultation duration / overrun impact | 🟡 2 | Time per encounter, overrun rate - genuinely missing operational metric. Scoping review called this out as an inconsistent measure across studies. | Phase 1 slide deck p. 14 |

### 1b. Deferred - RSET taxonomy (4 candidates)

Considered and set aside. Preserved so the reasoning is durable if the same gaps are re-raised in future rounds.

| Gap ID | Title | Proposed Tier | Why deferred |
|--------|-------|---------------|--------------|
| Gap-RSET-A | Transcript / code review-ergonomics | (would have been 🟡 2) | HL.HF-3a Review-Before-Signing Rate and HL.HF-3b Time-to-Sign Distribution (sub-parts of HL.HF-3 Inadequate-Review Detection post-v3.7) already capture whether review happens and how long it takes. "Ergonomics" as a distinct construct is hard to operationalise without subjective instruments; not a pure measurement gap. Revisit only if HL.HF-3 sub-parts prove insufficient in practice. |
| Gap-RSET-B | Transcript relevance / signal-preservation | (would have been 🔵 3) | Most AVT products don't expose the raw transcript to the clinician; measurement would apply to a minority of deployments. Signal-preservation is also already bracketed by TP.SN-6 Omission Rate (summary level) and TP.SN-11 MEDIC Cross-Examination. Narrow additional value. |
| Gap-RSET-C | Transcript edit metrics (parallel to summary) | (would have been 🔵 3) | Only meaningful where the transcript is user-editable - a minority feature. HL.HF-* metrics can be applied to transcript edits by analogy if the product supports it; no new metric needed. |
| Gap-RSET-D | Configurability surface integrity | (would have been 🔵 3) | Meta-property of product configuration surfaces (whether safety-critical features can be toggled off). Unusual measurement shape - closer to a design review than a continuous metric. Out of scope for an assurance metrics taxonomy; belongs to vendor-transparency reporting. Revisit only if configuration-related incidents surface. |

### 1c. Accepted - NHSE IG alignment — **all 4 candidates promoted in v5.3.0**

All four NHSE-IG-derived gap candidates were promoted to active metrics in v5.3.0 (Refusal Impact-Explanation Quality, Privacy Notice Currency & Completeness, SAR Deletion-Pause Interaction, Right-to-Restrict Tooling Support). Original rows preserved for historical record at [§7](#7-promoted-in-earlier-releases-historical-record).

---

## 2. Standards Mapping (28 candidates)

Identified during assertion-level mapping to extended standards (`_standards-mapping.md`). Gap candidates are slot-less per the v5.3.0 ID-allocation convention (see `_versioning.md` § Gap-candidate ID allocation); the actual ref-ID is allocated to the next-available slot in the natural cluster at the moment of promotion.

### 2a. MHRA SaMD / AIaMD — **all 5 candidates promoted in v5.3.0**

All five MHRA-derived candidates were promoted to active metrics in v5.3.0 (Medical Device Classification Documentation, PCCP Documentation Completeness, PMS Report Currency, MHRA Transparency Content Completeness, Training Data Representativeness Documentation). Original rows preserved for historical record at [§7](#7-promoted-in-earlier-releases-historical-record).

### 2b. NICE Evidence Standards Framework (5)

**Earlier promotions:** Tier Classification Documentation and Silent Mode Evaluation Coverage promoted to ES.ME-8 / ES.ME-9 at v3.3; rows preserved at [§7](#7-promoted-in-earlier-releases-historical-record).

| Title | Tier | What it measures |
|---|---|---|
| Subgroup Drift Monitoring Plan | 🟡 2 | Documented plan for monitoring performance drift across demographic subgroups post-deployment. |
| Cost-Effectiveness Analysis Availability | 🔵 3 | For Tier C AVT: CEA with QALY or cost-consequences. Research-grade for most deployments. |
| Budget Impact Analysis Completeness | 🟡 2 | Direct and indirect costs; NHS reference costs; sensitivity analysis. Extends GV.OP-7. |

### 2c. FHIR UK Core (3) — **deferred from v5.3.0; pickup-ready outline at `reference-docs/v5.3-deferred-fhir-uk-core.md`**

These three were originally in scope for v5.3.0 but held back by reviewer 2026-05-07 pending UK Core STU landscape stabilisation. Pre-flight checklist in the deferred-outline file.

| Title | Tier | What it measures |
|---|---|---|
| Per-Resource UK Core Conformance | 🟡 2 | Stratified conformance by resource type (Composition, Condition, AllergyIntolerance, etc.). |
| UK Core Extension Conformance | 🟡 2 | NHS Number verification status, Ethnic Category, Birth Sex, Death Notification extensions. |
| STU Version Targeting Declaration | 🟢 1 | Vendor declaration of which UK Core STU version(s) supported. Procurement requirement. |

### 2d. CQC Assessment — **1 of 4 candidates promoted in v5.3.0**

Board-Level AI Governance Mechanism promoted to **GV.CR-12** in v5.3.0; row preserved at [§7](#7-promoted-in-earlier-releases-historical-record).

| Title | Tier | What it measures |
|---|---|---|
| CSO AI Oversight Capacity | 🟡 2 | Protected time / budget for CSO to oversee AI safety (not just sign-off). Operational capacity. |
| AI-Specific Complaint Handling Rate | 🟡 2 | Rate of complaints about AI-generated records and their resolution time. Also flagged under RAI Theme 5 (Contestability). |
| Record Quality Composite (Reg 17) | 🟡 2 | Composite of content accuracy, completeness, and timeliness against Reg 17 good-governance standard. |

### 2e. PSIRF (4)

| Title | Tier | What it measures |
|---|---|---|
| Systems-Based Incident Analysis Rate | 🟡 2 | Proportion of AI-related safety incidents receiving SEIPS-informed systems analysis. Also flagged under RAI Theme 1 (Safety). |
| Compassionate Engagement with Affected Patients | 🟡 2 | Rate at which patients/families affected by AI-related harm received early contact, named liaison, and draft report review. |
| Staff Just Culture Protection | 🔵 3 | Staff survey on whether they feel supported vs blamed after AI-related incidents. Organisational culture. |
| Learning Implementation Tracking | 🟡 2 | Did identified learning actually change practice? Closure rate on systemic actions. |

### 2f. PRSB — **1 of 4 candidates promoted in v5.3.0**

PRSB Semantic Completeness promoted to **TP.WB-8** in v5.3.0; row preserved at [§7](#7-promoted-in-earlier-releases-historical-record).

| Title | Tier | What it measures |
|---|---|---|
| Professional Narrative Preservation | 🟡 2 | Ratio of free-text narrative vs structured extraction; flags over-structurisation and loss of clinical nuance. |
| Communication Needs (AIS) Capture | 🟡 2 | Whether Accessible Information Standard flags (interpreter, BSL, etc.) are captured and preserved. Accessibility-critical. |
| Legal Status Information Capture | 🟡 2 | Whether MHA status, DoLS, LPA, advance decisions are preserved when present. Clinical-legal critical. |

### 2g. Caldicott Principles — **2 of 3 candidates promoted in v5.3.0**

DPIA Justification Quality promoted to **GV.PD-17** and Consultation-Type Appropriateness Assessment promoted to **GV.CR-14** in v5.3.0; rows preserved at [§7](#7-promoted-in-earlier-releases-historical-record).

| Title | Tier | What it measures |
|---|---|---|
| Per-Data-Item Necessity Documentation | 🔵 3 | DPIA-level documentation of why each data element processed is necessary. Granular and burdensome but thorough. |

### 2h. Standards summary (outstanding only)

Promoted candidates moved to [§7](#7-promoted-in-earlier-releases-historical-record); counts below reflect outstanding gaps.

| Source Standard | Outstanding | Tier Distribution | Promoted (cumulative) |
|-----------------|-------------|-------------------|-----------------------|
| MHRA SaMD / AIaMD | 0 | — | 5 (all in v5.3.0) |
| NICE ESF | 3 | 2 × Tier 2, 1 × Tier 3 | 2 (ES.ME-8/-9 at v3.3) |
| FHIR UK Core | 3 | 1 × Tier 1, 2 × Tier 2 | 0 (held back; see §2c) |
| CQC Assessment | 3 | 3 × Tier 2 | 1 (GV.CR-12 at v5.3.0) |
| PSIRF | 4 | 3 × Tier 2, 1 × Tier 3 | 0 (Registry-deferrable) |
| PRSB | 3 | 3 × Tier 2 | 1 (TP.WB-8 at v5.3.0) |
| Caldicott | 1 | 1 × Tier 3 | 2 (GV.CR-14 + GV.PD-17 at v5.3.0) |
| **Total outstanding** | **17** | **1 × Tier 1, 13 × Tier 2, 3 × Tier 3** | **11 cumulative** |

---

## 3. NHS T.E.S.T. Framework (6 candidates)

Derived from the NHS T.E.S.T. Framework mapping (see `_standards-mapping.md` § NHS T.E.S.T.). T.E.S.T. is AVT-specific, so alignment is already strong - these 6 gaps are genuinely novel surfaces rather than re-statements of existing standards.

| Title | Tier | T.E.S.T. Source | What it measures |
|---|---|---|---|
| AI Translation Accuracy & Liability Attribution | 🟡 2 | Section A req 13 | Accuracy of AI-generated language translation in AVT output, with explicit documentation that liability for translation errors rests with the vendor, not the clinician. T.E.S.T. names translation as a distinctive clinical safety surface; no existing metric. |
| Training Data Anonymisation Provenance | 🟡 2 | Section A req 4 | Documented provenance of anonymisation technique applied to AI training data (ICO-aligned). Extends GV.PD-7 Training Data Inclusion Status, which covers inclusion declaration but not anonymisation quality. |
| Total Cost of Ownership / Formal Economic Evaluation | 🟡 2 | Section B domain 2 (25 pts) | Formal multi-dimensional economic evaluation including ROI, operational savings, and full TCO. Extends GV.OP-7 (per-consultation cost) and GV.OP-8 (governance burden) with a top-down economic view that T.E.S.T. weights at 25 of 420 points. Distinct from NICE-derived Cost-Effectiveness and Budget Impact candidates (§2b) — this is an NHS-procurement-framed TCO view. |
| Multi-Specialty Validation Coverage | 🔵 3 | Section B domain 3 | Count and breadth of clinical specialties in which the AVT has been formally validated (medical, surgical, allied health). T.E.S.T. awards 10 pts for multi-specialty validation; no existing metric captures breadth of validation scope. |
| Virtual-Care Modality Stratified Performance | 🔵 3 | Section B domain 9 | Performance stratified by consultation modality (in-person, video, telephone, ambulance triage). Existing IO.FE-1 covers deployment equity by site/setting but not by modality. T.E.S.T. singles out ambulance telephone triage as a distinct high-weight case (10 pts). |
| Sovereign AI / UK Supply Chain Disclosure | 🔵 3 | Section B domain 12 | Disclosure of whether the vendor and underlying model stack are UK-based (contributing to UK PLC per T.E.S.T. domain 12). Procurement transparency surface. Complements GV.VT-7 Sub-Processor Transparency with sovereignty-specific attribute. |

### 3a. T.E.S.T. summary

| Source | Gaps | Tier Distribution |
|--------|------|-------------------|
| NHS T.E.S.T. Section A | 2 | 2 × Tier 2 |
| NHS T.E.S.T. Section B | 4 | 1 × Tier 2, 3 × Tier 3 |
| **Total** | **6** | **3 × Tier 2, 3 × Tier 3** |

Note: 18 of 22 Section A requirements already have direct or strong metric coverage. 3 Section A items are pure process/product-feature criteria (CSO embedding, VR/dictation product offering, DCB 0160 local risk control) and are not metric-shaped. The 4th un-mapped item (req 13, translation) becomes Gap TP.SN-26 above. Section B's 12 domains all have at least partial coverage; the 4 gaps captured above are where weighting is heavy or coverage is thin.

---

## 4. Responsible AI Lens (38 candidates)

Derived from the DSIT AI Playbook principle mapping and the six ethical theme mapping in `_responsible-ai-lens.md`. Some overlap the standards-mapping gaps - cross-references noted inline.

### 4a. By Playbook principle (20)

| Principle | Gap | Severity | Cross-reference |
|-----------|-----|----------|-----------------|
| P1 - Limitations | Patient-facing disclosure of AVT limitations (not just clinician-facing) | Medium | - |
| P1 - Limitations | Running tally of encountered failure modes over deployment time | Medium | Partial via GV.SG-11 / GV.SG-14 |
| P2 - Lawful/ethical | IP status of training data (copyright, consent) | Medium | - |
| P2 - Lawful/ethical | Proportionality review (is AVT the right intervention?) | Medium | See P6; partial via ES.ME-1 |
| P3 - Security | Supply-chain security for model weights and dependencies | Medium | - |
| P3 - Security | AI-specific red-teaming cadence | Medium | - |
| P4 - Human control | Formal escalation paths when AI output is rejected | Medium | - |
| P4 - Human control | Board-level visibility of aggregate override patterns | Medium | Partial via GV.SG-13 |
| P5 - Lifecycle | Decommissioning plan | — | Promoted in v4.1: GV.PD-16 (data handling), GV.OP-14 (output continuity), GV.VT-15 (retirement notification) |
| P5 - Lifecycle | Model retirement criteria | — | Promoted in v4.1 alongside decommissioning plan (GV.VT-15 covers vendor-side retirement triggers/notification) |
| P6 - Right tool | Formal comparison against non-AI alternatives at procurement | High | No existing metric |
| P6 - Right tool | Procurement-stage tool-fit assessment | High | No existing metric |
| P7 - Openness | ATRS publication completeness (where applicable) | Low | ATRS referenced but not mapped |
| P7 - Openness | Patient-facing plain-language AVT documentation | Medium | - |
| P8 - Commercial | Contractual SLA enforcement (actual enforcement, not just clauses) | Medium | - |
| P8 - Commercial | Exit-clause testing | Medium | GV.VT-6 is about provisions; gap is on testing |
| P9 - Skills | SRO / board-level AI literacy assessment | Medium | - |
| P9 - Skills | Deployer-side data science / engineering skills | Low | - |
| P10 - Org assurance | AI review board effectiveness metric | Medium | - |
| P10 - Org assurance | Enterprise risk register alignment for AI risks | Medium | Partial via GV.SG-13 |

### 4b. By ethical theme (18)

| Theme | Gap | Severity | Cross-reference |
|-------|-----|----------|-----------------|
| T1 - Safety/Security/Robustness | Systems-based root cause analysis (SEIPS) for AI incidents | High | GV.SG-19 proposed (Standards §2e) |
| T1 - Safety | Catastrophic failure mode planning | Medium | - |
| T2 - Transparency | Patient-facing explanation of AI decision-making in the record | High | TP.WB-11 proposed (Standards §2f) |
| T2 - Transparency | Model card / system card publication | Medium | Partial via GV.VT-2 |
| T2 - Transparency | Audience-proportionate explanation | Medium | - |
| T3 - Fairness | Fairness during deployment ramp | Medium | Partial via IO.FE-1 |
| T3 - Fairness | Intersectional fairness at small-group level | High | IO.FE-4/5 partial; small-group power unresolved |
| T4 - Accountability | Board-level AI governance mechanism | High | GV.CR-12 proposed (Standards §2d) |
| T4 - Accountability | Named accountable director for AI | High | Covered under GV.CR-12 |
| T4 - Accountability | Clear role distinction: CSO, DPO, SIRO, Caldicott Guardian in AI context | Medium | - |
| T5 - Contestability | Patient route to challenge AI-generated note content (beyond SAR) | High | Related to IO.PX-11 (Standards §2d) |
| T5 - Contestability | Affected-third-party contestability | Medium | - |
| T5 - Contestability | Redress mechanism for population-level AVT harm | Medium | - |
| T6 - Societal Wellbeing | Workforce displacement / role change assessment | High | HL.HF-12 partial |
| T6 - Societal Wellbeing | Equity of benefit distribution across practices | High | IO.FE-1 partial |
| T6 - Societal Wellbeing | Patient trust at population level | High | IO.PX-5, IO.PX-6 partial |
| T6 - Societal Wellbeing | Long-term sustainability of AVT adoption | Medium | - |
| T6 - Societal Wellbeing | Job security / workforce anxiety assessment | Medium | Flagged low severity in Standards Mapping |

### 4c. Highest-severity cross-cutting gaps

Gaps that surface under multiple lens axes - highest-leverage targets for future metric rounds.

1. **Patient-facing explanation / contestability of AVT output** - P7, T2, T5. The taxonomy assumes clinicians mediate AI output to patients; patient-facing AI requires direct channels.
2. **Board-level AI governance** - P10, T4, CQC Well-led. Captured in proposed GV.CR-12. Arguably the single highest-leverage missing metric for NHS deployment.
3. **Tool-fit / proportionality assessment** - P2, P6, NICE ESF Tier classification. Procurement-stage gap.
4. **Systems-based incident learning (SEIPS)** - T1, PSIRF mandatory requirements. Captured in proposed GV.SG-19.
5. **Societal Wellbeing measurement generally** - Theme 6 has the highest concentration of gaps because second-order effects on workforce, patient relationships, and healthcare sustainability are intrinsically hard to measure.

---

## 5. Roll-up (outstanding only)

**Totals across origins (outstanding only — promoted candidates moved to §7):**

| Origin | Outstanding | Deferred | Rejected | Total outstanding |
|--------|-------------|----------|----------|-------------------|
| RSET external review | 9 | 4 | 0 | 13 |
| NHSE IG external review | 0 | 0 | 0 | 0 (all 4 promoted in v5.3.0) |
| Standards mapping | 17 | 0 | 0 | 17 (11 promoted cumulatively) |
| NHS T.E.S.T. | 6 | 0 | 0 | 6 |
| Responsible AI lens | 38 | 0 | 0 | 38 |
| **Total outstanding** | **70** | **4** | **0** | **74** |

**Tier distribution of the 70 outstanding accepted/proposed candidates:**

| Tier | Count |
|------|-------|
| 🟢 1 | 2 (Gap-RSET-J + 1 FHIR UK Core deferred) |
| 🟡 2 | 47 |
| 🔵 3 | 5 |
| Unassigned (RAI severity only) | 16 |

**If all 70 outstanding candidates were adopted as metrics,** the taxonomy would grow from 234 to ~304 metrics. In practice, cross-cutting gaps will collapse to single metrics, so the true additive count is likely ~50–55.

**Highest-leverage outstanding single additions** (gap appears in multiple origins simultaneously):
- **Systems-Based Incident Analysis Rate** — Standards §2e (PSIRF), RAI Theme 1 Safety
- **AI-Specific Complaint Handling Rate** — Standards §2d (CQC), RAI Theme 5 Contestability

## 6. How this file is maintained

- New gaps identified in any source document are added here with `status: proposed`.
- Gaps promoted to metrics: original row moves to [§7](#7-promoted-in-earlier-releases-historical-record) with the landed ref-ID; section-level breadcrumb left in place. The CHANGELOG records the promotion.
- Reference IDs are slot-less in §1–§4 per the [v5.3.0 ID-allocation convention](versioning.md#gap-candidate-id-allocation-v530-convention); actual ref-IDs are recorded only in §7 once the metric lands.
- Deferred gaps stay in §1b-style "Deferred" subsections with explicit reasoning so the rejection is durable.
- Cross-cutting gaps (single concept across multiple origins) are listed once in their primary origin with cross-references, not duplicated.
- This file is the **single source of truth for roadmap content**. The prose gap sections in `_standards-mapping.md` and `_responsible-ai-lens.md` are summaries that point here. The build's `gap_count` is `len(§1–§4 entries)`; §7 is excluded.

---

## 7. Promoted in earlier releases (historical record)

Rows here have already been promoted to active metrics in earlier releases. They are preserved with their original tier, rationale, and source for historical record — these were the entries that drove the metric's design at promotion time. The build's `gap_count` does **not** include these rows.

### 7a. NHSE IG (4 → all promoted in v5.3.0)

| Original Gap ID | Title | Tier at promotion | Rationale | Source | Landed at |
|---|---|---|---|---|---|
| Gap-IG-A | Refusal impact-explanation quality | 🟡 2 | NHSE IG explicitly requires clinicians to explain *how* refusal affects care. We measure recording/respecting dissent (GV.CR-1) but not the quality of the explanation. Periodic audit. | NHSE IG Mar-2026 | **GV.CR-13** (v5.3.0; Maturity: Proposed/Novel pending piloted rubric) |
| Gap-IG-B | Privacy notice currency & completeness | 🟢 1 | Organisational privacy notices must be updated to include ambient-scribe processing specifics. Binary compliance, trivial measurement cost, named requirement in the guidance. | NHSE IG Mar-2026 | **GV.PD-13** (v5.3.0) |
| Gap-IG-C | SAR deletion-pause interaction | 🟡 2 | Guidance explicitly requires deletion paused during active SAR handling. GV.PD-2 Audio Time-to-Deletion doesn't test the SAR interaction — the two processes are measured separately today. | NHSE IG Mar-2026 | **GV.PD-14** (v5.3.0) |
| Gap-IG-D | Right-to-restrict tooling support | 🟡 2 | Restriction is distinct from erasure — data held, marked, not processed. Current GV.PD-11 covers erasure only. IG guidance explicitly requires tool functionality for restriction. | NHSE IG Mar-2026 | **GV.PD-15** (v5.3.0) |

### 7b. MHRA SaMD / AIaMD (5 → all promoted in v5.3.0)

| Title | Tier at promotion | What it measured | Landed at |
|---|---|---|---|
| Medical Device Classification Documentation | 🟢 1 | Whether the AVT system's SaMD classification (Class I/IIa/IIb/III) is documented with justification. Deployer must know regulatory status before go-live. | **GV.CR-11** (v5.3.0) |
| PCCP Documentation Completeness | 🟡 2 | Whether Predetermined Change Control Plans cover model updates, thresholds, and rollback. Required for adaptive/retrained models. | **GV.SG-18** (v5.3.0) |
| Post-Market Surveillance Report Currency | 🟡 2 | PMSR (Class I/IIa) availability on demand; PSUR (Class IIb/III) annual currency. Regulatory reporting cadence. | **GV.VT-9** (v5.3.0) |
| MHRA Transparency Content Completeness | 🟡 2 | Composite check of WHAT content items (device characterisation, performance, limitations, lifecycle). | **GV.VT-10** (v5.3.0; Maturity: Proposed/Novel pending WP-2 final outputs) |
| Training Data Representativeness Documentation | 🟡 2 | Evidence that training data covers intended patient population (age, ethnicity, accent, comorbidity). Foundational for bias mitigation. | **GV.PD-12** (v5.3.0) |

### 7c. NICE ESF (2 → both promoted at v3.3)

| Title | Tier at promotion | What it measured | Landed at |
|---|---|---|---|
| NICE ESF Tier Classification Documentation | 🟢 1 | Whether the AVT deployment is classified as Tier A / B / C with justification. Required before evidence assembly. | **ES.ME-8** (v3.3) |
| Silent Mode Evaluation Coverage | 🟡 2 | Evidence that AVT was run in silent mode on local data before go-live. | **ES.ME-9** (v3.3) |

### 7d. CQC Assessment (1 of 4 → promoted in v5.3.0)

| Title | Tier at promotion | What it measured | Landed at |
|---|---|---|---|
| Board-Level AI Governance Mechanism | 🟢 1 | Named board committee or director with AI oversight responsibility. CQC inspection point. Also flagged under RAI Theme 4 (Accountability) and Principle 10 (Org assurance). | **GV.CR-12** (v5.3.0) |

### 7e. PRSB (1 of 4 → promoted in v5.3.0)

| Title | Tier at promotion | What it measured | Landed at |
|---|---|---|---|
| PRSB Semantic Completeness | 🟢 1 | Proportion of PRSB-mandatory information elements present in AVT-generated output, per applicable PRSB standard (CIS, Outpatient Letter, Discharge, etc.). Highest-leverage single addition — appears as a gap across PRSB, FHIR UK Core, and CQC record quality. | **TP.WB-8** (v5.3.0) |

### 7f. Caldicott Principles (2 of 3 → promoted in v5.3.0)

| Title | Tier at promotion | What it measured | Landed at |
|---|---|---|---|
| DPIA Justification Quality | 🟡 2 | Independent review (e.g. by Caldicott Guardian) of DPIA purpose justification, not just completion. Extends GV.CR-7 completion metric. | **GV.PD-17** (v5.3.0) |
| Consultation-Type Appropriateness Assessment | 🟢 1 | Documented assessment of whether AVT is appropriate for sensitive consultation types (safeguarding, MH, children, intimate exams). High-risk carve-outs. | **GV.CR-14** (v5.3.0) |

### 7g. NHSE IG additional mints (2 → both minted directly in v5.4.0)

These two were not enumerated in §1c at v5.3.0 time — they surfaced as additional NHSE IG-driven gaps during the v5.1.1 Phase 1b batch 1 framework audit and were tracked as v5.4.0 mints in `v5.2-registry-action-list.md §C`. They are minted directly without an intermediate `_gaps.md` row.

| Title | Tier at promotion | What it measured | Landed at |
|---|---|---|---|
| Information Asset Register Completeness | 🟢 1 | NHSE IG section 8 IAR registration with named owner, lawful basis, retention period, sub-processor list, risk classification. | **GV.PD-18** (v5.4.0) |
| Joint-Controller Status Assessment | 🟡 2 | UK GDPR Article 26 + NHSE IG section 5 binary determination distinct from sub-processor disclosure. | **GV.VT-11** (v5.4.0) |

### 7h. Cumulative roll-up

- **17 candidates promoted** across all releases to date (2 at v3.3, 13 at v5.3.0, 2 at v5.4.0)
- 4 origin sections fully closed (NHSE IG, MHRA SaMD)
- 4 origin sections partially closed (NICE ESF, CQC, PRSB, Caldicott)
- The build's `gap_count` reports outstanding gaps only (74 as of v5.4.0)
