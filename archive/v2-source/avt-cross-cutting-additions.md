# AVT Metrics Taxonomy - Cross-Cutting Additions (Pass 3)

Final pass before the v2 taxonomy is complete. These are the taxonomy-level changes that sit outside individual metric entries - updates to the introductory sections, Summary, Tier 1 Quick Reference, Contents, and new-group introductions for the two groups added during the drafting batches.

## Contents of this pass

1. **Field-wide resource gap callout** - added to the How to Use This Taxonomy section
2. **Summary section updates** - updated counts, new breakdown categories, family structure visibility
3. **Tier 1 Quick Reference updates** - 9 new Tier 1 entries (8 from NHS Compliance + 1 from Clinical Coding) with the Hallucination Rate underspecification flag
4. **New-group introductory paragraphs** - for NHS Compliance & Regulatory and Environmental & Sustainability
5. **Contents / Table of Contents updates** - new groups, sub-clusters, family convention note, updated metric counts
6. **"Adapting to Local Context" addition** - new worked example reflecting NHS Compliance variability
7. **Header metric count update** - top of document

## Final taxonomy figures

Before v1 → After v2 totals:
- **Metrics:** 151 → 214
- **Groups:** 18 → 20
- **Sub-clusters within groups:** 0 explicit → 4 named (Conversation Analysis, Sociotechnical & Resilience, Patient Clinical Outcomes, Longitudinal Drift & Model Contamination)
- **Metric families:** 0 explicit → 4 named (Clinical Content Fidelity, Post-Generation Correction, Clinical Transcription Accuracy, Reference-Based Text Similarity)
- **Tier 1 metrics:** 33 → 42
- **Tier 2 metrics:** 59 → 87
- **Tier 3 metrics:** 59 → 85

---

# 1. Field-wide resource gap callout

**Target location:** How to Use This Taxonomy section. Insert immediately after the "Adapting to Local Context" subsection, as a new subsection before the Summary.

---

### ⚠️ Field-wide resource constraint

> **Only two public benchmark datasets exist for ambient scribe evaluation: ACI Bench and PriMock.** This is not a minor inconvenience. It is the single biggest structural limitation on the operationalisation of nearly every metric in this taxonomy.
>
> Inter-rater reliability is rarely reported in published AVT evaluation studies, and where it is reported, clinical experts show significant disagreement - which means the notion of a stable "gold standard" against which to measure automated metrics is itself empirically fragile. A metric that claims high correlation with expert judgment can only be as reliable as the experts themselves are with each other, and current evidence suggests that ceiling is lower than published figures imply.
>
> The practical consequences for readers of this taxonomy are three-fold:
>
> **First, cross-vendor comparisons are usually not what they appear to be.** When two vendors both claim "95% M-WER" or "97% confabulation detection", they have almost certainly used different reference datasets, different significance ontologies, different inter-rater reliability thresholds, and different evaluation protocols. Direct comparison is not meaningful. The honest position is that procurement decisions based on vendor-reported performance metrics are currently closer to vibes-based assessment than to scientific comparison - and making that visible is part of what this taxonomy is for.
>
> **Second, the field-wide cost of every unvalidated metric is high.** Because there is no shared infrastructure for validation, every deployer or researcher who wants to use a metric meaningfully must rebuild the validation locally at their own cost. This creates enormous duplication and prevents any given metric from accumulating the cross-study evidence base that would make it trustworthy. ROUGE is the canonical example - it is used almost universally in clinical NLG evaluation despite published evidence that it correlates essentially not at all with clinical judgment, because the alternative would require locally-validated replacement metrics that nobody has resources to build.
>
> **Third, this is the single highest-leverage infrastructure intervention the NHS could make.** A national investment in shared clinical encounter datasets - with multi-annotator ground truth across specialties, accents, consultation types, and clinical complexity levels - would transform operationally what nearly every metric in this taxonomy can deliver. It would make vendor-reported metrics comparable for the first time. It would make validation studies tractable for small research groups. It would make the underspecification warnings throughout this taxonomy progressively less necessary as empirical evidence replaces informed speculation. There is no individual deployer, no individual vendor, and no individual academic group that can solve this at the scale required; it is a national body responsibility.
>
> **What deployers should do in the interim.** Until shared infrastructure exists, three working practices help make the limitation manageable rather than invisible: (1) always document the reference dataset, protocol, and inter-rater reliability conditions used when reporting any metric from this taxonomy; (2) treat cross-vendor comparison of self-reported metrics with explicit scepticism in procurement documentation; (3) prefer metrics in the taxonomy that are computable against the deployer's own data (Edit Rate, Time-to-Sign Distribution, the NHS Compliance metrics, Concept Extraction Concordance) over those that require reference datasets the deployer does not have, because the former are at least internally consistent even where cross-site comparison is difficult.

---

# 2. Summary section updates

**Target location:** Existing Summary section at the top of the taxonomy.

## 2.1 Replace the existing "By Priority Tier" block

**Old:**
```
- **🟢 Tier 1 - Minimum Viable Assurance**: 33 metrics - what every deployer must measure to operate safely
- **🟡 Tier 2 - Recommended Assurance**: 59 metrics - recommended with reasonable governance capacity
- **🔵 Tier 3 - Advanced / Research**: 59 metrics - advanced, research, or requires infrastructure that doesn't yet exist
```

**New:**
```
- **🟢 Tier 1 - Minimum Viable Assurance**: 42 metrics - what every deployer must measure to operate safely
- **🟡 Tier 2 - Recommended Assurance**: 87 metrics - recommended with reasonable governance capacity
- **🔵 Tier 3 - Advanced / Research**: 85 metrics - advanced, research, or requires infrastructure that doesn't yet exist
```

## 2.2 Replace the existing "By Maturity" block

**Old:**
```
- **Established**: 39 metrics
- **Emerging**: 32 metrics
- **Vendor-Proprietary**: 4 metrics
- **Proposed / Novel**: 76 metrics
```

**New:**
```
- **Established**: 54 metrics
- **Emerging**: 48 metrics
- **Vendor-Proprietary**: 4 metrics
- **Proposed / Novel**: 108 metrics
```

*Note: maturity assignments for the 63 new metrics use the same criteria as the original taxonomy - Established for metrics with validated methodology in related fields (e.g. FHIR conformance, medication attribute extraction), Emerging for metrics with recent but not yet consolidated clinical validation (e.g. M-WER, DER variants, cpHEWER), and Proposed / Novel for metrics introduced by the taxonomy itself or drawn from 2025–2026 regulatory frameworks that have not yet accumulated deployment evidence.*

## 2.3 Add a new "By Metric Family" breakdown

Insert after the "By Maturity" block, before "By Underspecification Warning" (see 2.4):

```
### By Metric Family

Some groups contain named metric families - clusters of related metrics that measure facets of a shared construct. Family framings appear before the first metric of each family.

- **Clinical Content Fidelity** (Summarisation / NLP): 5 metrics - hallucination, omission, confabulation, negation, uncertainty
- **Post-Generation Correction** (Human Factors & Workflow): 4 metrics - edit rate, type, location, pattern
- **Clinical Transcription Accuracy** (ASR / Transcription): 3 metrics - WER, M-WER, CK-ER
- **Reference-Based Text Similarity** (Summarisation / NLP): 2 metrics - ROUGE, BERTScore
- **Unaffiliated**: 200 metrics - the remainder, not currently grouped into a named family
```

## 2.4 Add a new "By Underspecification Warning" breakdown

Insert after the new "By Metric Family" block:

```
### By Underspecification Warning

15 existing metrics in the taxonomy carry explicit flags indicating specific measurement-science gaps. Readers should treat these as calls for caution rather than for avoidance.

- **⚠️ Tier A - No established methodology**: 3 metrics
  - Off-Label Use Detection Rate (Safety & Governance)
  - Trust Halo Decay Rate (Human Factors & Workflow)
  - Note Review Fatigue Trajectory (Human Factors & Workflow)
- **⚠️ Tier B - Concept defined, no AVT-specific validation**: 7 metrics
  - Hallucination Rate (Summarisation / NLP)
  - Medical WER (ASR / Transcription)
  - Clinical Keyword Error Rate (ASR / Transcription)
  - Cognitive Load Assessment (Human Factors & Workflow)
  - Trust Calibration Survey (Human Factors & Workflow)
  - Automation Bias Detection (Human Factors & Workflow)
  - Clinical Decision Equivalence (End-to-End Pipeline)
- **⚠️ Tier C - Technically defined, clinical validity unproven or disproven**: 5 metrics
  - ROUGE Scores (Summarisation / NLP)
  - BERTScore (Summarisation / NLP)
  - LLM-as-a-Judge (PDSQI-9 Proxy) (Summarisation / NLP)
  - Diarisation Error Rate (Diarisation)
  - Demographic-Disaggregated WER (ASR / Transcription)
```

## 2.5 Update the header sentence

**Old header sentence of the Summary section (top of document):**
```
**151 metrics** across **18 groups**, organised in six parts.
```

**New:**
```
**214 metrics** across **20 groups**, organised in six parts. Includes 4 named metric families and 4 sub-clusters within existing groups. 15 metrics carry explicit underspecification warnings reflecting specific measurement-science gaps in the published literature.
```

---

# 3. Tier 1 Quick Reference updates

**Target location:** Tier 1 - Minimum Viable Assurance (Quick Reference) section.

The Tier 1 count moves from 33 to 42 with the additions from Pass batches 1 and 3. Nine new entries need to be added, and one existing entry (Hallucination Rate) needs an underspecification flag.

## 3.1 New entries to add under "Deployer" subsection

Add these to the existing Deployer list in the Tier 1 Quick Reference:

- 🚪 **AVT Supplier Registry Listing Verification** - Procurement gate with trivial verification cost. Must be confirmed before deployment and re-verified at contract renewal. Non-listed vendors should not be deployed.
- 🚪 **ICB Engagement Documentation** - Pre-deployment compliance gate under CIO/CCIO guidance v2. Documented evidence of regional engagement required before go-live. Absence indicates governance process breakdown.
- 🔄 **Clinical Safety Case Completeness** - DCB0129/0160 regulatory requirement. The 2025 FOI finding that many NHS digital health deployments lack compliant safety cases makes active monitoring essential, not optional.
- 🚪 **DPIA Template Completion Rate** - UK GDPR Article 35 legal requirement. Use of the NHSE March 2026 template enables cross-deployment comparison and ensures mandatory considerations aren't missed.
- 📡 **Patient Dissent Recording Rate** - Per-encounter compliance with the requirement to document and respect objections. Distinct from aggregate opt-out: opt-out is a blanket choice; dissent recording is procedural integrity at the point of care. Target 100%.
- 🔄 **Verbal Notification Compliance** - Proportion of AVT consultations where verbal notification was delivered at session start. The compliance metric behind the consent model. Periodic audit via patient survey or recording sample.
- 📡 **AI-Generated Content Labelling Compliance** - Every AI-generated entry must carry the mandatory SNOMED suffix. Automated verification is trivial; non-compliance breaks downstream audit and safety investigation.
- 📡 **Audio Time-to-Deletion** - NHSE IG guidance March 2026 requires deletion after summary sign-off. Measurement makes the policy operational rather than assertive. Must verify deletion in primary storage, caches, and backups.
- 📡 **Transcript Retention Compliance** - Parallel to audio deletion but often treated as less sensitive despite being higher-risk (structured, searchable, readily consumable). Explicit retention policy required; compliance measurable continuously.

## 3.2 New entry to add under "Vendor" subsection

- 📡 **Code Hallucination Rate** - Zero-tolerance metric. Any non-zero rate indicates architectural failure in generation constraints. Vendor must demonstrate 0% pre-deployment and maintain continuous monitoring. A vendor who cannot achieve zero has unconstrained code generation, which is a procurement red flag.

## 3.3 Existing entry to annotate

The existing **Hallucination Rate** entry in the Tier 1 Quick Reference (under both Deployer and Vendor subsections) should carry an underspecification flag so readers don't miss the definitional instability when scanning the summary. Modify the existing entry:

**Old:**
> 🔄 **Hallucination Rate** - Core safety metric. NAS Day Zero SPI with <2% review and ≥5% pause thresholds. Every deployer must measure this through periodic clinical audit even if methodology is manual.

**New:**
> 🔄 **Hallucination Rate** ⚠️ - Core safety metric. NAS Day Zero SPI with <2% review and ≥5% pause thresholds. Every deployer must measure this through periodic clinical audit even if methodology is manual. *See underspecification warning in full entry - the term has no universally accepted definition and reported rates across the literature span 1–67% due largely to methodological differences. Document the specific subtype taxonomy and reference dataset used.*

## 3.4 Update Tier 1 actor counts

The existing Tier 1 Quick Reference has subsection counts at the top of each actor group. Update:

- **Deployer**: (27 metrics) → (35 metrics)
- **Vendor**: (19 metrics) → (20 metrics)
- **Regional (ICB)**: (2 metrics) → unchanged
- **National Body**: (1 metric) → unchanged

Note the Deployer count rises by 8 (the 9 NHS Compliance Tier 1s minus the AVT Supplier Registry entry which has joint Deployer/Vendor responsibility). Count accurately during integration - some new entries have joint actors.

## 3.5 Add a note to the Tier 1 section opening

The existing Tier 1 Quick Reference section opens with:
> The smallest set of metrics that a deployer cannot responsibly skip. All are measurable today with existing tools, data, and governance capacity.

Add a second paragraph after this:
> **Tier 1 expanded substantially with the January–March 2026 NHS guidance suite.** Nine metrics moved into Tier 1 or were added as new Tier 1 entries reflecting compliance requirements that did not exist when the taxonomy was first drafted: the NHS Compliance & Regulatory cluster (Patient Dissent Recording, Verbal Notification, AI-Generated Content Labelling, AVT Supplier Registry, ICB Engagement, Clinical Safety Case, DPIA Template, Audio Time-to-Deletion, Transcript Retention) plus Code Hallucination Rate. For NHS deployers, the shape of Day Zero minimum assurance has changed materially since early-2025 vendor procurement; re-assess existing deployments against the expanded Tier 1 set.

---

# 4. New-group introductory paragraphs

**Target location:** Start of each new group section, before the first metric entry. Format matches existing group intros (italic, 2–4 paragraphs).

## 4.1 NHS Compliance & Regulatory

Insert at the start of the NHS Compliance & Regulatory section, before the first metric (Patient Dissent Recording Rate).

---

### NHS Compliance & Regulatory

*Process compliance metrics against defined external requirements, distinct from the safety performance metrics in the Safety & Governance group. Most entries here are binary or near-binary - the deployer is compliant or they are not - and most Tier 1 assignments reflect legal or guidance requirements that cannot be responsibly skipped regardless of clinical performance.*

*The group was added to the taxonomy in response to the January–March 2026 NHS guidance suite: NHSE IG guidance on ambient scribing (March 2026), the NHSE AVT Supplier Registry (launched January 2026), and CIO/CCIO guidance v2 (January 2026). Taken together these documents defined a discrete compliance surface that is operationally distinct from clinical safety governance and that deserves its own cluster rather than being scattered across Safety & Governance and Privacy & Data Governance.*

*The group also contains two international regulatory metrics (FDA PCCP-Equivalent Pre-Defined Acceptance Criteria, EU AI Act Event Logging Compliance) because vendor compliance cascades across jurisdictions - an AVT vendor with EU market exposure will typically apply EU AI Act requirements uniformly across their product rather than maintaining jurisdiction-specific variants, which means UK deployments inherit EU requirements through vendor compliance regardless of whether they would otherwise apply.*

*Legal and statutory privacy metrics that pre-date the 2026 NHS guidance (Subject Access Request Fulfilment, Right to Erasure, Cross-Border Data Transfer Compliance, Sub-Processor Transparency) remain in the Privacy & Data Governance group to preserve the legal-basis cluster there. The split between "privacy legal requirements" and "NHS compliance process requirements" is analytical rather than hierarchical - a deployer is obliged to meet both, and neither group has precedence over the other.*

*Tier breakdown: 🟢 7 Tier 1 · 🟡 3 Tier 2 · 🔵 0 Tier 3*

---

## 4.2 Environmental & Sustainability

Insert at the start of the Environmental & Sustainability section, before the first metric (Energy Consumption per Clinical Note).

---

### Environmental & Sustainability

*Energy, carbon, and water footprint of AVT operation. All three current metrics in this group are Tier 3 - not Day Zero priority for clinical safety assurance, but increasingly required for NHS procurement under Net Zero commitments and cascading through EU-market vendor compliance under forthcoming corporate sustainability reporting requirements.*

*The group exists more as placeholder for an expected future than as a cluster of actionable metrics today. The measurement infrastructure is immature: vendors rarely expose per-inference telemetry; cloud providers are not consistent in sustainability reporting; methodology for attributing training emissions to individual inferences is contested; water consumption data is especially limited. None of the current metrics are deployer-measurable - they are vendor-reported, and deployers currently have no independent verification path.*

*All three metrics may move to Tier 2 as the NHS Net Zero procurement framework matures and as vendor sustainability reporting becomes routine. At the scale of potential NHS AVT deployment (millions of consultations per year), even small per-note environmental differences compound into substantial total footprint, and procurement conversations are starting to ask the question even where answers are uneven.*

*Tier breakdown: 🔵 3 Tier 3*

---

# 5. Contents / Table of Contents updates

**Target location:** The existing Contents section (between "By Maturity" and the "Tier 1 - Minimum Viable Assurance (Quick Reference)" section).

## 5.1 Replace the existing Contents block with updated metric counts and new entries

**Old structure (abbreviated):**
```
**Part E - System Governance**
- [Safety & Governance] (13 metrics - 6 Tier 1)
- [Security & Adversarial Robustness] (9 metrics)
- [Privacy & Data Governance] (6 metrics - 5 Tier 1)
- [Operational] (6 metrics - 3 Tier 1)
- [Training & Competency] (5 metrics - 1 Tier 1)
- [Vendor Transparency & Contractual] (7 metrics - 3 Tier 1)
```

**New structure with all groups and updated counts:**

```
**Part A - The Technical Pipeline**

- [Audio Capture & Environment](#audio-capture-environment) (9 metrics - 1 Tier 1)
- [ASR / Transcription](#asr-transcription) (14 metrics - 2 Tier 1) *contains Clinical Transcription Accuracy family*
- [Diarisation](#diarisation) (9 metrics) *contains Conversation Analysis sub-cluster*
- [Summarisation / NLP](#summarisation-nlp) (24 metrics - 4 Tier 1) *contains Clinical Content Fidelity and Reference-Based Text Similarity families*
- [Clinical Coding](#clinical-coding) (12 metrics - 1 Tier 1)
- [EPR Write-back](#epr-write-back) (7 metrics - 4 Tier 1)

**Part B - Pipeline Interactions**

- [Partial-Pipeline](#partial-pipeline) (9 metrics)
- [End-to-End Pipeline](#end-to-end-pipeline) (12 metrics)

**Part C - The Human Layer**

- [Human Factors & Workflow](#human-factors-workflow) (20 metrics - 3 Tier 1) *contains Post-Generation Correction family and Sociotechnical & Resilience sub-cluster*

**Part D - Impact & Outcomes**

- [Patient Experience](#patient-experience) (10 metrics - 1 Tier 1) *contains Patient Clinical Outcomes sub-cluster*
- [Fairness & Equity](#fairness-equity) (8 metrics)

**Part E - System Governance**

- [Safety & Governance](#safety-governance) (17 metrics - 6 Tier 1) *contains Longitudinal Drift & Model Contamination sub-cluster*
- [NHS Compliance & Regulatory](#nhs-compliance-regulatory) (10 metrics - 7 Tier 1) *NEW GROUP*
- [Security & Adversarial Robustness](#security-adversarial-robustness) (11 metrics)
- [Privacy & Data Governance](#privacy-data-governance) (11 metrics - 7 Tier 1)
- [Operational](#operational) (9 metrics - 3 Tier 1)
- [Environmental & Sustainability](#environmental-sustainability) (3 metrics) *NEW GROUP*
- [Training & Competency](#training-competency) (5 metrics - 1 Tier 1)
- [Vendor Transparency & Contractual](#vendor-transparency-contractual) (8 metrics - 3 Tier 1)

**Part F - Evaluation Science**

- [Meta-evaluation](#meta-evaluation) (7 metrics)
```

## 5.2 Add a family and sub-cluster convention note

Insert as a short italic paragraph immediately after the Contents block, before the Part A heading:

> *Several groups contain named metric families or sub-clusters. A **metric family** is a group of related metrics measuring facets of a shared construct (e.g. Clinical Content Fidelity groups Hallucination Rate, Omission Rate, Confabulation Detection, Negation Handling Accuracy, and Uncertainty Marker Preservation). Family framings appear before the first metric of each family and provide parent-construct context. A **sub-cluster** is a thematic grouping within a larger group (e.g. Conversation Analysis within Diarisation covers role identification, code-switching, turn-taking, and addressee recognition). Sub-clusters have italic introductory text before the first metric in the sub-cluster. Neither families nor sub-clusters require separate navigation - they are additive context within the existing group structure.*

---

# 6. "Adapting to Local Context" section addition

**Target location:** The existing "Adapting to Local Context" subsection within How to Use This Taxonomy. Add after the existing worked examples.

The current section has four worked examples of promoting metrics to higher tiers based on local context (EAL populations → demographic WER; multi-party consultations → multi-party robustness; template customisation → underspecification; varying digital maturity → cross-practice variance). Add a fifth:

---

> **A trust with multiple AVT platforms deployed across different services should prioritise Cross-Platform Fairness Consistency as Tier 1 rather than Tier 3** - the fairness concern of different patients receiving different documentation quality depending on which service happens to use which vendor is elevated for multi-platform deployments even where each platform individually performs acceptably on single-axis fairness metrics. For an integrated care system with genuinely uniform platform deployment this metric is Tier 3; for one with a mixed AVT portfolio it is Tier 1.

---

# 7. Header metric count update

**Target location:** Top of document, immediately under the title.

**Old:**
```
**151 metrics** across **18 groups**, organised in six parts.
```

**New:**
```
**214 metrics** across **20 groups**, organised in six parts. Includes 4 named metric families, 4 sub-clusters within existing groups, and 15 metrics carrying explicit underspecification warnings that flag specific measurement-science gaps in the published literature. Version 2 incorporates metrics responding to the January–March 2026 NHS guidance suite, the 2025–2026 evaluation science literature (SCRIBE, CREOLA, VeriFact, MedHELM, CHECK), and regulatory developments (FDA PCCP, EU AI Act high-risk provisions).
```

---

# Integration order

All three passes (plus the four drafting batches) need to be applied in a specific order to avoid broken cross-references and duplicated content:

1. **Drafting batches 1–4** (63 new metric entries)
2. **Pass 1 - Consolidation framings** (4 family framings + 14 cross-reference footers; references the new metrics)
3. **Pass 2 - Underspecification warnings** (15 warnings on existing metrics; references the new metrics and new family structure)
4. **Pass 3 - Cross-cutting additions** (this document; updates counts and sections to reflect everything above)

Applying them in any other order will create cross-reference dangling pointers (Pass 1 references new metrics, Pass 2 references the new families from Pass 1), count mismatches (Pass 3 counts depend on all previous passes being complete), and content duplication (Pass 1's family framings and Pass 2's warnings on ROUGE and BERTScore overlap substantially, and Pass 1 should land first to carry the broader framing while Pass 2 can be shortened to avoid repetition - see the Pass 2 integration note on this).

## One small interaction to resolve during integration

The Pass 2 warnings on ROUGE, BERTScore, M-WER, and CK-ER overlap with the Pass 1 family framings (Reference-Based Text Similarity and Clinical Transcription Accuracy). Both passes are drafted independently and both carry the specific literature citations (Kendall-Tau 0.080, Spearman ρ −0.66 to −0.77, Pearson 0.62 with omission rate, etc.). If both are applied verbatim, readers will encounter the same citations twice within a few hundred words.

Recommendation: when integrating, **keep the family framing full** (it provides structural context for all family members) and **trim the individual underspecification warnings** on ROUGE, BERTScore, M-WER, and CK-ER to reference the family framing rather than repeating it. Example for ROUGE:

**Pass 2 original warning (trimmed):**
> **⚠️ Underspecification Warning (Tier C - technically rigorous, clinically invalid)**
>
> See the Reference-Based Text Similarity family framing at the start of this section for the detailed evidence on ROUGE's poor correlation with clinical judgment (Croxford et al. 2025 Kendall-Tau 0.080; catastrophic Spearman ρ between −0.66 and −0.77 in some medical contexts). **ROUGE must not be used as a standalone clinical quality indicator.** Retain only for technical benchmarking and always report alongside a validated clinical instrument.

This is about 40% the length of the original Pass 2 warning for ROUGE and carries the same assurance weight because the citations are in the family framing immediately above. The same trimming applies to BERTScore, M-WER, and CK-ER. The other 11 underspecification warnings are not affected and should be integrated as drafted.

---

# Pass 3 complete

All three passes are now drafted. The v2 taxonomy is ready for assembly.

## What the v2 taxonomy will contain

- **214 metrics** across **20 groups** (up from 151 across 18)
- **4 named metric families** with explicit parent-construct framings and cross-references
- **4 sub-clusters** within existing groups (Conversation Analysis, Sociotechnical & Resilience, Patient Clinical Outcomes, Longitudinal Drift & Model Contamination)
- **2 new top-level groups** (NHS Compliance & Regulatory, Environmental & Sustainability)
- **15 underspecification warnings** on existing metrics with three severity tiers (A/B/C)
- **1 field-wide resource gap callout** on the ACI Bench / PriMock constraint
- **Updated Tier 1 Quick Reference** reflecting 9 new Tier 1 entries and the Hallucination Rate definitional flag
- **Updated Summary** with new breakdowns by Metric Family and Underspecification Warning
- **Updated Contents** with family and sub-cluster visibility

## What the v2 taxonomy does NOT contain

To preserve integration integrity and avoid scope creep, none of the three passes:

- Renames any existing metrics
- Deletes or deprecates any existing metrics (including the three Tier A metrics with no established methodology - Off-Label Use Detection, Trust Halo Decay Rate, Note Review Fatigue Trajectory - which remain in the operational taxonomy with explicit warnings)
- Restructures any section ordering beyond adding the two new groups
- Changes the five-axis cross-cutting structure of individual metric entries
- Changes the three-tier priority model or the cadence / actor / maturity assignments

All changes are additive. The v2 taxonomy is a superset of v1, with new content slotted in and existing content enhanced with warnings, framings, and cross-references. Consumers of v1 who reference the taxonomy externally will not find their references broken.

## Remaining work beyond the three passes

Two things are out of scope for these passes but may be worth a future iteration:

1. **Validation of the proposed metrics against real deployment data.** Many of the new metrics are drafter proposals with literature backing but without empirical validation in NHS AVT deployments. The taxonomy acknowledges this in the Maturity field (most new metrics are "Proposed / Novel") but validation would materially strengthen the taxonomy's status as an operational reference rather than a theoretical framework.

2. **Companion deliverables.** The taxonomy is a reference document. Three companion pieces would make it more immediately actionable: a **deployer one-pager** listing the Tier 1 metrics with their formal definitions and measurement cadence only; a **procurement checklist** drawn from the Vendor and Vendor-joint-responsibility entries; and a **national body infrastructure-gap briefing** drawn from the Tier 3 metrics and the field-wide resource gap callout, aimed at NHS England and equivalent commissioners as the argument for national investment in shared benchmark datasets.

Neither of these is part of the v2 taxonomy itself, but both are natural extensions once the taxonomy is stable.

---

**v2 taxonomy is now fully specified across four drafting batches and three structural passes. Ready for assembly into the master document.**
