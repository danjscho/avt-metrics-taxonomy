# Changelog

## v3.4 (2026-04-25)

Three deliverables completing the v3.3 tightening work and making the conventions machine-enforced. No new metrics, no new gap-roadmap candidates. Counts unchanged: 216 metrics, tier split 43 / 94 / 79.

### Phase A — Audit-side enforcement

Two new checks in `taxonomy/audit.py` promote the v3.3 conventions from documentation to machine-enforced:

- **`check_tightening_pattern`** — every Tier 1 metric must carry all three tightening sub-blocks (`Reference Standard`, `Operational Specification`, `Threshold Guidance`) or none of them. Mixed (partial) state is an ERROR. Preserves cohort integrity: a metric is either tightened or not, no half-states.
- **`check_threshold_provenance`** — every metric classified as 'tightened' must open its Threshold Guidance block with a `⚠️ **Provenance**` line within the first 400 characters. Closes the honesty gap surfaced by the v3.3 self-review.

`audit.py` also emits a Tier 1 tightening status manifest after the tier counts:

```
Tier 1 tightening status: 13/43 tightened.
  Tightened: GV.CR-1, GV.CR-2, GV.OP-1, GV.PD-1, GV.PD-3, GV.SG-1,
             HL.HF-1, HL.HF-4, IO.PX-1, TP.SN-15, TP.SN-5, TP.SN-6, TP.WB-1
  Not tightened: [30 metric IDs]
```

v3.5+ scope is now derived from this output rather than from CHANGELOG prose. Future contributors see the deferred set in the audit log, not buried in a release note.

The Metric dataclass gained a `body` field (heading-to-next-heading content) so sub-block detection runs on parsed bodies rather than re-reading files.

### Phase B — Phase 3 tightening (4 operational/proxy metrics)

Apply the Reference Standard / Operational Specification / Threshold Guidance pattern (with ⚠️ Provenance prelude written in from the start) to the operational/proxy class — different shape from the safety class (Phase B.1, v3.3) and compliance class (Phase B.2, v3.3):

- **GV.OP-1 Documentation Time per Consultation** — defines doc start/end timestamps; in-consultation vs out-of-consultation breakdown mandatory; pairing with quality companion metric (PDSQI-9 / hallucination rate) mandatory; pause trigger when time-saved positive but quality deteriorates or burden displaces to after-hours.
- **HL.HF-4 Time-to-Sign Distribution** — TTS_norm distribution (P5 / P10 / median / P90) per clinician mandatory; pairing with HL.HF-1 substantive edit rate mandatory (rubber-stamping signal lives in the conjunction); per-clinician baseline; note-complexity stratification.
- **IO.PX-1 Patient Opt-Out Rate** — distinguishes registration-level from per-encounter opt-out (cross-link to GV.CR-1); demographic disaggregation mandatory with χ² + Holm correction; trajectory + disparity-ratio thresholds; the disparities are the metric's value, not the absolute rate.
- **GV.SG-1 Model Version Tracking** — six-component versioning mandatory (ASR / LLM weights / prompt / retrieval / safety classifier / fine-tunes); change-event log structure mandatory; deployer-notification latency monitored; MHRA PMS substantial-change cross-link.

Tightened count: 9/43 → **13/43**.

### Phase C — Full Tier 1 LOOSE classification

`archive/v3.3-tier1-classification.md` (new) classifies every Tier 1 metric not yet tightened as **TIGHT** (8), **LOOSE** (18), or **SURROGATE-and-LOOSE** (3, also LOOSE) with one-sentence per-metric reasoning. The artefact is frozen at v3.4 ship date and is the input to v3.5+ scoping.

Suggested v3.5+ waves identified in the artefact:

- **v3.5 Wave 1 (8 compliance/governance core metrics):** GV.CR-5, GV.CR-6, GV.CR-7, GV.TC-1, GV.VT-1, GV.VT-5, GV.VT-7, GV.SG-14
- **v3.5 Wave 2 (4 privacy-chain completion metrics):** GV.PD-2, GV.PD-8, GV.PD-10, GV.PD-11
- **v3.6+ pipeline narrow tightening (6 metrics):** TP.ASR-12, TP.ASR-13, TP.WB-2, TP.WB-3, TP.WB-4, TP.SN-20
- **Deferred / pattern-may-not-fit (5 metrics):** GV.OP-6, GV.SG-9, GV.SG-11, GV.SG-13, HL.HF-3

The v3.4 release does **not** promote these — it stops at the audit boundary. v3.5 will pick the wave it wants based on stakeholder input.

### Cross-cutting

- `taxonomy/_header.md` bumped to v3.4 / 2026-04-25 with reference to the audit-side enforcement and the published classification
- `taxonomy/_how-to-use.md` updated to list 13 tightened metrics and to point readers at `audit.py` output for current status rather than the prose
- 8 of 30 not-yet-tightened Tier 1 metrics are classified TIGHT and explicitly will not be tightened — the pattern is structural, not substantive, for these

### Counts

Unchanged: 216 metrics, 43 / 94 / 79 tier split, 20 groups. v3.4 is structural, not additive.

`audit.py` baseline updated; build clean; audit clean (both new checks pass on the 13 tightened metrics).

### Deferred to v3.5+

- Tightening of remaining LOOSE metrics per the classification waves above
- Outcomes layer stays at ES.ME-8/9; the [Outcomes Boundary](#outcomes-boundary) position holds
- Roadmap (`_gaps.md`) untouched in v3.4 — 89 candidates still queued

---

## v3.3 (2026-04-25)

Two structural changes addressing critique findings on v3.2: an explicit outcomes boundary and a definitional-tightening pattern applied to nine Tier 1 metrics. No new gap-roadmap candidates are promoted in this release.

### Outcomes Boundary

New cross-cutting file `taxonomy/_outcomes-boundary.md` makes the scope of the taxonomy explicit:

- **What this taxonomy assures:** technical fidelity, documentation quality, clinician oversight, equitable performance, hazard identification, governance compliance, measurement quality. Process, structure, and proximal-outcome measures.
- **What it does not:** clinical-outcome validation - whether AVT changes diagnostic accuracy, patient safety incident rates, downstream care quality, or clinical reasoning. That work belongs to national research bodies (e.g. NIHR RSET), regulators with post-market surveillance powers (MHRA), evidence-standards frameworks (NICE ESF Tier C), and vendors pursuing formal clinical claims.
- **Why drawn explicitly:** to prevent the failure mode where passing every metric in a deployment-assurance taxonomy is read as evidence of clinical benefit.

Two new Tier 2 meta-metrics in Part F operationalise the boundary at procurement:

- **ES.ME-8 Outcome Evidence Commitment Status** - 4-check composite for whether vendor and deployer have committed to outcome evaluation (registered protocol or NHS pilot; PMS plan naming patient-outcome signals distinct from technical-performance signals; baseline data infrastructure; contractual commitment to share results).
- **ES.ME-9 Causal Model Operationalisation** - 4-stage check that each vendor outcome claim is backed by a documented causal chain from proximal performance to distal outcome, with cited mechanisms and named confounders.

ES.ME-1 Proximal vs Distal Outcome Distinction prose updated to point at ES.ME-8/9 as making its "burden of proof on vendors" requirement operational. T.E.S.T. Section B Clinical Effectiveness mapping row updated to reference ES.ME-8 as the closest taxonomy proxy for the 50-point RCT-validation item (commitment, not the evidence itself).

### Tier 1 Definitional Tightening (9 metrics)

Adds three structured sub-blocks to nine Tier 1 metrics where loose definitions previously allowed vendor-selective compliance and non-comparable evidence:

- **Reference Standard** - what counts as ground truth, with inter-rater reliability target where applicable
- **Operational Specification** - measurement window, population, mandatory breakdowns (subtype, severity, category, per-storage-location, per-clinician), aggregation rule
- **Threshold Guidance** - pre-deployment gate, continuous-monitoring alert, pause / escalation trigger

The pattern lifts existing-but-buried content (Tier B underspecification warnings, Limitations, Novel Thinking) into discoverable structured sub-blocks. No new measurement science is invented; existing knowledge is made actionable.

**Phase 1 - five safety-critical metrics:**
- TP.SN-5 Hallucination Rate (CREOLA subtype mandatory; weighted aggregate HR_w; gate ≤ 2 %, pause ≥ 5 % sustained)
- TP.SN-6 Omission Rate (per-CREOLA-category breakdown mandatory; allergies / red-flags / dose / safety-netting critical by default)
- TP.SN-15 Negation Handling Accuracy (negation-type scope explicit; ≥ 200-sentence adversarial test set; allergy-category zero-failure gate)
- HL.HF-1 Edit Rate (substantive vs stylistic distinction; per-clinician baseline mandatory; safety-critical edit rate as separate leading indicator)
- TP.WB-1 Write-back Fidelity (structural / semantic / no-addition decomposition; per-EPR ≥ 200-case test corpus; type-(iii) hallucination into safety-critical fields as binary defect)

**Phase 2 - four compliance/consent metrics:**
- GV.PD-1 Audio Retention Compliance (per-storage-location reporting; cryptographic erasure not logical deletion; independent verification annual minimum)
- GV.PD-3 Transcript Retention Compliance (purpose enumeration mandatory; "quality monitoring" decomposition required; transcript derivatives tracked under same chain)
- GV.CR-1 Patient Dissent Recording Rate (dissent-event scope explicit; coverage-check sampling required when recorded rate implausibly low; per-clinician disaggregation)
- GV.CR-2 Verbal Notification Compliance (four content elements mandatory; method declaration mandatory; ≥ 30 patients/recordings per clinician per quarter)

`taxonomy/_how-to-use.md` adds a paragraph explaining the sub-block structure to readers and lists the nine tightened metrics.

### Counts

- 214 → 216 metrics (+2 from ES.ME-8/9)
- Tier split 43 / 92 / 79 → **43 / 94 / 79**
- 20 groups unchanged
- Meta-evaluation group: 7 → 9 metrics
- Applicability: AVT-Specific 48, AVT-Contextualised 77, General Healthcare AI 89 → 91, total 216

`audit.py` baseline updated; build clean; audit clean.

### Deferred to v3.4

The v3.3 critique work identified ~30 of 43 Tier 1 metrics as LOOSE or SURROGATE (definitional rigour audit, sampled 20 of 43). v3.3 tightens 9 of those; the remainder are deferred:

- **Phase 3 - operational/proxy (4 metrics):** GV.OP-1 Documentation Time per Consultation, HL.HF-4 Time-to-Sign Distribution, IO.PX-1 Patient Opt-Out Rate, GV.SG-1 Model Version Tracking
- **Remaining LOOSE Tier 1 pool (~17 metrics):** scope to be confirmed in v3.4 via a full rather than sampled audit
- **Outcomes layer:** explicitly *not* extended beyond ES.ME-8/9; the [Outcomes Boundary](#outcomes-boundary) position stands
- **Roadmap:** 89 candidates remain in `_gaps.md`; v3.3 promotes none

### Repository hygiene

- `taxonomy/_header.md` updated to v3.3 / 2026-04-25 with reference to the new structural elements
- Plan file `plan-v3.3.md` lives at repo root during the release; will move to `archive/` on completion per the established convention

### Post-release clarification (2026-04-25)

Self-review of v3.3 surfaced an honesty gap in the Threshold Guidance blocks: some numerical thresholds derive from cited sources (e.g. NAS Day Zero SPI, UK GDPR storage limitation, NHSE IG guidance), but others were proposed during v3.3 as starting points without external validation. The original blocks did not consistently distinguish the two, risking over-trust by procurement officers reading the numbers as authoritative.

A ⚠️ **Provenance** prelude was added to each of the nine Threshold Guidance blocks naming which thresholds are cited and which are proposed-as-starting-points, and stating that all numbers require local calibration before contractual use. `_how-to-use.md` updated to explain the distinction. No metric IDs, dimensions, or substantive content changed.

This clarification is a small follow-up to v3.3 rather than a new tag. v3.4 will add an `audit.py` check that flags Threshold Guidance blocks missing the Provenance prelude, so the convention becomes machine-enforced.

---

## v3.2 (2026-04-22)

No new metrics in the taxonomy (still 214 across 20 groups; tier split unchanged 43/92/79). This release restructures the repository around a build pipeline, publishes a documentation site, extends coverage with two external audits and a second AVT-specific framework, and consolidates the roadmap.

### Parser and structured build outputs

New `taxonomy/parse.py` parses every metric from its dimension table (no frontmatter migration needed — derive, don't duplicate). `build.py` now emits to `dist/`:

- `metrics.csv` - 214 flat rows for spreadsheet / BI use
- `metrics.json` - structured catalogue
- `gaps.json` - 89 roadmap candidates with origin tags
- `summary.json` - headline counts

Audit tool (`taxonomy/audit.py`) kept green across the whole release.

### Documentation site (MkDocs Material)

Published as GitHub Pages. Key features:

- One page per group (20 group pages), metrics as anchors
- Tier 1 Quick Reference auto-generated from source
- Per-standard cross-cut pages (one per framework)
- Related-metrics footer on every group page
- Glossary, RSS feed, downloads page (CSV/JSON)
- `mike` version switcher; GitHub Actions deploy
- Site polish: draft banner, Part kicker, applicability quick access, collapsible icon legend, consistent header shape, em-dash sweep

### External coverage audits

Two external-source coverage audits landed alongside the existing 12-framework standards mapping:

- **RSET external review** (Nuffield Trust AVT taxonomy, Feb 2026) — 9 accepted, 4 deferred
- **NHSE IG alignment audit** (Mar 2026) — 4 accepted

Audits archived under `archive/`; findings consolidated into the single roadmap file.

### NHS T.E.S.T. Framework mapping

Added the NHS T.E.S.T. (Technology Evaluation Safety Test) framework to the standards mapping — the AVT-specific ICS-level procurement assurance framework from GOSH/NHS London/C&W/UCL (v11.17625SS, June 2025). Brings total mapped frameworks to twelve.

- **Section A** (platform assurance, 22 binary requirements): 18 directly or strongly covered by existing metrics; 3 are process/product-feature criteria (not metric-shaped); 1 novel gap (translation)
- **Section B** (benefits assessment, 420 points across 12 domains): all 12 domains have at least partial coverage
- **6 novel gap candidates added** to the roadmap: TP.SN-26 (AI Translation Accuracy), GV.PD-15 (Training Data Anonymisation Provenance), GV.OP-13 (Total Cost of Ownership), GV.VT-11 (Multi-Specialty Validation Coverage), IO.FE-9 (Virtual-Care Modality Stratified Performance), GV.VT-12 (Sovereign AI Disclosure)
- Authoritative PDF stored under `reference-docs/` for offline reference

Strongest alignment: T.E.S.T. requirement 18 names three exact taxonomy metrics (hallucination rate, omission rate, WER); requirement 22 (drift) maps directly to the Longitudinal Drift sub-cluster.

### Roadmap consolidation

All gap analyses unified into `taxonomy/_gaps.md`:

- Single source of truth across five origins: RSET, NHSE IG, Standards Mapping, NHS T.E.S.T., Responsible AI Lens
- 89 total candidates (85 accepted/proposed + 4 deferred with preserved reasoning)
- Entry states (`proposed` / `accepted` / `deferred` / `rejected`) so dismissals are durable
- Parsed into `gaps.json` by origin for programmatic use
- Prose gap sections in `_standards-mapping.md` and `_responsible-ai-lens.md` now point here instead of duplicating content

### Repository hygiene

- `.gitignore`: added `.claude/` (local workspace) and the unused 5MB GOSH AAI report; build artefacts (`dist/`, `docs/`, `site/`) already ignored
- `METHODOLOGY.md`: reusable recipe for applying this taxonomy structure to new assurance domains
- `reference-docs/`: new location for authoritative source PDFs cited by mappings

---

## v3.1 (2026-04-18)

### Source Audit Tool

New `taxonomy/audit.py` - parses every group file and verifies:

- Every metric heading has a matching **Reference** row in its dimension table
- Heading tier icon matches the **Priority Tier** row
- Reference-ID prefix matches the group file (e.g. `TP.AC-*` only in `audio-capture.md`)
- No duplicate reference IDs; numbering is contiguous per group
- Tier totals reconcile with `_summary.md` declarations (43 / 92 / 79)
- 214 total metrics across 20 group files
- `_applicability.md` counts sum to 214 (48 + 77 + 89)
- Every metric listed in `_tier-1-quick-reference.md` exists and is still Tier 1
- "See also" cross-references resolve to a known metric (by name or abbreviation)
- All 8 required dimensions present on every metric

Baseline audit at v3.1 tag: **zero findings**. Run `python taxonomy/audit.py` before any future content change.



### Extended Standards Mapping

Added assertion-level or higher-level mapping for seven additional NHS/UK standards. Mapping only - no new metrics added to taxonomy; gaps flagged for future consideration.

**Assertion-level (formal standards):**
- **MHRA SaMD / AIaMD** - Change Programme workstreams (WP1–WP11), SI 2024 No. 1368 Post-Market Surveillance (in force June 2025), Transparency Guiding Principles (June 2024), GMLP 10 principles (Oct 2021)
- **NICE Evidence Standards Framework for DHTs (ECD7)** - all 21 numbered standards across 5 lifecycle areas, Tier A/B/C classification, AI-specific provisions (Standards 4, 5, 6, 15, 16)
- **FHIR UK Core / INTEROPen** - STU1/STU2/STU3 release status, per-profile conformance, UK-specific extensions (NHS Number verification, Ethnic Category, etc.), refinement of TP.WB-6 to mean UK Core not generic FHIR R4

**Higher-level summary:**
- **CQC Assessment for AI** - GP Mythbuster 109 baseline assertions, Five Key Questions (Safe/Effective/Caring/Responsive/Well-led), CSO expectations (flagged as emerging 2025–26)
- **Patient Safety Incident Response Framework (PSIRF)** - four PSIRF principles, response types (AAR, PSII, SEIPS), engagement and board oversight requirements
- **PRSB Clinical Documentation Standards** - Core Information Standard, Outpatient Letter, Discharge, etc.; common header set; narrative vs structured trade-off; relationship to FHIR UK Core
- **Caldicott Principles (2020 revision)** - all 8 principles with direct metric mapping (Principle 8 maps directly to existing GV.CR-1/2/3), Caldicott Guardian role, NDG statutory context

### Proposed New Metrics (Not Yet Implemented)

28 candidate metrics flagged across the 7 new standards to close identified gaps:
- 5 from MHRA (classification, PCCP, PMS reports, transparency, training data)
- 5 from NICE ESF (tier classification, silent mode, subgroup drift, cost-effectiveness, budget impact)
- 3 from FHIR UK Core (per-resource conformance, UK extensions, STU version targeting)
- 4 from CQC (board governance, CSO capacity, AI complaints, Reg 17 record quality)
- 4 from PSIRF (SEIPS analysis, compassionate engagement, Just Culture, learning tracking)
- 4 from PRSB (semantic completeness, narrative preservation, AIS capture, legal status)
- 3 from Caldicott (DPIA justification, consultation appropriateness, per-item necessity)

Distribution: 6 × Tier 1, 19 × Tier 2, 3 × Tier 3. Highest-leverage addition: **TP.WB-11 PRSB Semantic Completeness** (appears as gap across multiple standards).

### New Responsible AI Lens Document

New cross-cutting file `taxonomy/_responsible-ai-lens.md` providing a policy-intent view of the taxonomy complementary to standards mapping and applicability classification.

**Part A: DSIT AI Playbook for the UK Government (Feb 2025) - 10 principles:**
- P1 (Know AI and its limitations), P2 (Lawful/ethical), P3 (Security), P4 (Meaningful human control), P5 (Lifecycle management), P6 (Right tool for the job), P7 (Open and collaborative), P8 (Commercial colleagues), P9 (Skills and expertise), P10 (Organisation policies and assurance)
- Each principle has narrative + metric table + gap notes

**Part B: Six Responsible AI Ethical Themes** (AI Regulation White Paper five + Playbook-added sixth):
- T1 (Safety, Security and Robustness), T2 (Transparency and Explainability), T3 (Fairness), T4 (Accountability and Governance), T5 (Contestability and Redress), T6 (Societal Wellbeing and Public Good)
- Each theme has narrative + metric table + trade-off notes

**Part C: Coverage Matrix** - 25 policy-lever metrics that cross-cut 3+ principles/themes simultaneously. Five "megas" cross 5–6 axes: GV.SG-11 (Adverse Event/LFPSE), GV.VT-4 (Audit Trail), GV.CR-3 (AI Content Labelling), HL.HF-1 (Edit Rate), IO.PX-1 (Patient Opt-Out).

**Part D: Gaps** - 20 principle-level + 18 theme-level gaps identified; cross-referenced to Proposed New Metrics. Societal Wellbeing (T6) has highest gap concentration; P6 (Right tool) and P7 (Openness) weakest principles.

### Build

- `build.py` now assembles from 28 files (was 27) - added `_responsible-ai-lens.md`
- All 214 metric reference IDs preserved; no existing metrics changed
- Tier counts unchanged: 43 Tier 1 / 92 Tier 2 / 79 Tier 3
- All metric references in new sections validated against assembled taxonomy

---

## v3.0 (unreleased)

### Reference IDs
- Every metric now carries a unique reference ID in the format `{Part}.{Group}-{Number}` (e.g. `TP.AC-1`, `GV.CR-7`)
- IDs appear in both the metric heading and the dimensions table
- Part abbreviations: TP (Technical Pipeline), PI (Pipeline Interactions), HL (Human Layer), IO (Impact & Outcomes), GV (System Governance), ES (Evaluation Science)
- 20 group abbreviations documented in the Reference IDs section of How to Use
- Reference key legend added to How to Use section

### Applicability Classification
- New cross-cutting section classifying all 214 metrics by applicability:
  - **AVT-Specific** (48 metrics, 22%) - meaningful only with the audio pipeline
  - **AVT-Contextualised** (77 metrics, 36%) - general concept, AVT-tuned definition
  - **General Healthcare AI** (89 metrics, 42%) - applicable to any clinical AI system
- Summary and per-part breakdown tables included
- Full per-metric classification table with reference IDs

### New Metric Families
- **Medication Safety Thread** (4 metrics: TP.SN-19, TP.SN-21, TP.CC-5, IO.PX-10) - cross-cutting family tracking medication accuracy from summarisation through coding to patient outcomes
- **Demographic Equity Disaggregation** (7 metrics: TP.ASR-4, TP.ASR-5, TP.CC-9, PI.E2E-5, IO.FE-2, IO.FE-4, IO.FE-5) - cross-cutting family applying demographic disaggregation across pipeline layers

### New Sub-clusters
- **Write-back Safety** (4 metrics: TP.WB-1 through TP.WB-4) - the four Tier 1 pre-deployment gates at the EPR integration boundary
- **Coding Fidelity** (7 metrics: TP.CC-1 through TP.CC-6 plus TP.CC-11) - accuracy of individual code assignment across NHS terminology systems

### Standards Mapping
- New cross-cutting section with assertion-level mapping to four NHS/regulatory frameworks:
  - **DTAC v2.0** - all 5 sections (C1 Clinical Safety, C2 Data Protection, C3 Technical Security, C4 Interoperability, D1 Usability)
  - **DSPT v8** - all 10 National Data Guardian standards with individual assertion mapping
  - **DCB0129/DCB0160** - all 7 clinical safety lifecycle stages
  - **NHS England LLM Evaluation & Monitoring Framework v0.2.2** - all 30 dimensions across 3 groups (flagged as draft)
- Gap summary identifying 9 areas where standards require coverage the taxonomy doesn't provide
- Coverage summary identifying 8 areas where the taxonomy extends beyond all standards

### Count Corrections
- Tier breakdown corrected from 42/87/85 to **43/92/79** (Tier 1/Tier 2/Tier 3) in Summary and How to Use
- Human Factors & Workflow metric count corrected from 20 to **19** in Contents
- EPR Write-back tier breakdown corrected from "4 Tier 1 · 1 Tier 2" to **4 Tier 1 · 2 Tier 2 · 1 Tier 3**
- Clinical Coding tier breakdown corrected from "2 Tier 2 · 2 Tier 3" to **1 Tier 1 · 8 Tier 2 · 3 Tier 3**

### Build
- `build.py` now assembles from 27 files (was 25) - added `_applicability.md` and `_standards-mapping.md`
- Family count: 6 (was 4)
- Sub-cluster count: 6 (was 4)
- Unaffiliated metrics: 189 (was 200)

---

## v2.0

- 214 metrics across 20 groups (was 151 metrics across 18 groups in v1)
- 63 new metrics added in batches 1-4
- 2 new groups: NHS Compliance & Regulatory, Environmental & Sustainability
- 4 named metric families: Clinical Content Fidelity, Post-Generation Correction, Clinical Transcription Accuracy, Reference-Based Text Similarity
- 4 sub-clusters: Conversation Analysis, Sociotechnical & Resilience, Patient Clinical Outcomes, Longitudinal Drift & Model Contamination
- 15 underspecification warnings across Tiers A/B/C
- Tier 1 Quick Reference section organised by responsible actor

## v1.0

- Initial release: 151 metrics across 18 groups
- Modular file structure with `build.py` assembler
- Monolithic source split into `taxonomy/` directory
