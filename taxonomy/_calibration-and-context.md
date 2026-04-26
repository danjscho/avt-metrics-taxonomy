## Calibration & Context

This section is a first-class principle of the taxonomy, parallel to the [Outcomes Boundary](#outcomes-boundary): **tier assignments and threshold numbers are calibration starting points, not universal gates.** Any deployment using this taxonomy must calibrate against its specific context before contractual use. The principle is named here so it cannot be lost in the per-metric detail.

### What's calibrated

The following are deployment-context-dependent and the taxonomy provides defaults that should be revisited:

- **Tier assignments** — which metrics are Minimum Viable, Recommended, or Advanced for *your* deployment
- **Threshold numbers** — pre-deployment gate values, continuous-monitoring alert levels, pause / escalation triggers
- **Mandatory vs optional sub-metric breakdowns** — what the headline figure must report (per-clinician, per-category, per-storage-location, etc.)
- **Audit cadences** — weekly / monthly / quarterly review frequencies
- **Sample-size floors** — how many notes / patients / recordings constitute a meaningful audit cycle

None of these are universal. They reflect a default deployment context — a moderately-resourced NHS Trust or PCN with a single mature AVT vendor, mixed acute-and-routine workload, and average patient population. Any specific deployment will differ on at least one axis, often several.

### What's not calibrated

The following are stable and should not be re-derived per deployment:

- **The metric constructs themselves** — what hallucination rate measures, what edit rate measures, what write-back fidelity measures
- **The dimensional axes** — Pipeline Layer, Assurance Question, Measurement Method, Lifecycle Phases, Responsible Actors, Maturity, Outcome Type, Applicability
- **The reference IDs** — TP.SN-5, GV.PD-1, etc. These are the public API
- **The Outcomes Boundary itself** — what this taxonomy assures (deployment safety) versus what national research bodies must validate (clinical outcomes)

Calibration changes parameters; it does not change structure.

### Six deployment-setting axes

A deployment's calibration should respond to at least these six contextual axes. Each axis can shift tier assignments, threshold numbers, or both.

#### 1. Specialty mix

Acute vs primary care vs mental health vs paediatrics; emergency vs routine; high-stakes diagnostic settings vs documentation-heavy settings.

A paediatric outpatient clinic and an A&E majors ward should not measure [TP.SN-5 Hallucination Rate](#tp-sn-5) against the same threshold. A psychiatric consultation has different hallucination-severity dynamics from a routine medication review. An emergency department's [HL.HF-4 Time-to-Sign Distribution](#hl-hf-4) thresholds should be tighter because rapid-sign patterns under genuine time pressure are harder to distinguish from rubber-stamping than in an outpatient clinic.

#### 2. Patient population

EAL (English as Additional Language) prevalence, deprivation index, accessibility needs (dysarthria, aphasia, hearing impairment), multi-party consultations (interpreter, family member, carer present).

Demographic-disaggregated metrics rise from Tier 2 to Tier 1 where the population's distribution is uneven. A practice with 40% EAL patients should treat [TP.ASR-4 Demographic-Disaggregated WER](#tp-asr-4) as Tier 1, not Tier 2. A practice routinely conducting multi-party consultations should treat [PI.PP-2 Multi-Party Conversation Robustness](#pi-pp-2) as Tier 1. The taxonomy's defaults assume an "average" population; that assumption breaks where it matters most.

#### 3. Platform maturity

Single-vendor vs mixed-vendor portfolio; integrated EHR vs federated; v1.0 vendor product vs mature deployment with N years of telemetry.

[IO.FE-8 Cross-Platform Fairness Consistency](#io-fe-8) shifts up where platforms are mixed across services within an ICS. [GV.SG-1 Model Version Tracking](#gv-sg-1) thresholds change at v1.0 (when component-version logging is being established) versus a mature deployment (where the question is drift detection on top of stable telemetry).

#### 4. Governance capacity

Embedded Clinical Safety Officer presence, regional CCIO support, IG team depth, audit-function maturity.

Audit cadences and sample-size floors are not feasible at the same level for a 4-clinician practice and a 200-clinician Trust. [GV.CR-2 Verbal Notification Compliance](#gv-cr-2)'s "≥ 30 patients per clinician per quarter" floor is straightforward at scale and impossible at solo-practice level — local calibration may shift to "all eligible patients audited quarterly" instead. [GV.CR-5 ICB Engagement Documentation](#gv-cr-5)'s carve-out logic explicitly assumes regional CCIO capacity that is not universal (see GV.CR-5 Limitations).

#### 5. Risk appetite

The DPIA-stated retention window, the contractual SLA tightness, the deployer's institutional appetite for IG-incident reportability.

Threshold *gate* values are at the deployer's risk appetite; the taxonomy provides starting points, not regulator-issued numbers. [GV.PD-2 Audio Time-to-Deletion](#gv-pd-2)'s 24-hour median target is a starting point; a deployer's DPIA may set 4 hours (lower risk appetite) or 7 days (with explicit DPIA justification). The Threshold Guidance Provenance prelude on every tightened metric distinguishes cited thresholds from proposed-as-starting-points; calibration acts on the latter.

#### 6. Volume / scale

Per-clinician disaggregation feasibility, sampled vs full audit, weekly vs monthly cadence — feasibility shifts with the count of consultations per clinician per week.

A solo GP and a Trust-scale ED workflow have different floors for "statistically meaningful". [HL.HF-1 Edit Rate](#hl-hf-1)'s per-clinician baseline establishment over the first 4 weeks of live use produces a defensible signal at 100 consultations per week per clinician; at 5 consultations per week per clinician it does not, and the calibration should extend the baseline window or aggregate to practice level. [GV.SG-14 Near-Miss Reporting Rate](#gv-sg-14)'s active-to-inferred-ratio safety-culture diagnostic needs minimum monthly volume to be informative.

### How to apply the principle

1. **Read each metric's Reference Standard / Operational Specification / Threshold Guidance (where present) as the default calibration**, not the universal answer. The pattern is in place on 25 of 43 Tier 1 metrics as of v3.7; see [`taxonomy/audit.py`](#) output for current status.

2. **Read the ⚠️ Provenance prelude carefully.** Cited thresholds (NAS Day Zero SPI, UK GDPR, NHSE IG guidance) carry external authority and should not be relaxed without explicit justification. Proposed-as-starting-points thresholds are explicitly the calibration surface — they were chosen as defensible defaults during taxonomy authoring, not as regulator-issued numbers, and require local calibration before contractual use.

3. **Document the local calibration in the deployer's governance file** alongside the DPIA and Clinical Safety Case. The local-calibration document should record, per metric:
   - The taxonomy default (tier and threshold values as published)
   - The local calibration (what was changed, with reasoning)
   - The deployment-context axis or axes driving the change (which of the six above applies)
   - The named decision-maker (CSO, IG lead, named clinical lead) and date
   Auditors and reviewers should see both the taxonomy default and the local calibration, with the reasoning visible.

4. **Promoting tier assignments up is encouraged and lower-friction.** A deployment with elevated context risk on an axis (high EAL prevalence, mixed platform, low governance capacity) can promote any Tier 2 or Tier 3 metric to Tier 1 with a one-line justification. This makes the taxonomy more conservative, not less, and the audit will not flag it.

5. **Promoting tier assignments down requires explicit justification.** A Tier 1 metric treated as Tier 2 because of low-risk context (e.g. an established routine outpatient setting with mature governance and homogeneous population) requires a substantive risk assessment, the named decision-maker, and review at the next governance cycle. Documentation should be available for ICB / CQC review.

6. **Threshold-number calibration follows the same logic.** Tighter thresholds (lower gate values, more sensitive alerts, faster pause triggers) are encouraged where context warrants. Looser thresholds require risk assessment and named accountability.

### What this principle is not

- **Not an excuse to disregard Tier 1 metrics.** Calibration shifts which metrics are Tier 1 for *your* deployment; it does not let you stop measuring them altogether. Every metric in the Tier 1 set after local calibration must be measured.
- **Not a way to argue threshold numbers are negotiable in vendor contracts.** The contractual gate is the deployer's local calibration, not the taxonomy's published starting point. Once the deployer has calibrated, the calibrated number is the contract; the taxonomy default is no longer in scope.
- **Not a way to avoid the [Outcomes Boundary](#outcomes-boundary).** The Boundary names what's out of scope (clinical-outcome validation, RCT evidence). Calibration cannot bring distal-outcome work into the deployer's scope; that responsibility stays with national research bodies, MHRA post-market surveillance, and vendor-side regulatory claims.

### Cross-references

- [Outcomes Boundary](#outcomes-boundary) — parallel principle, different boundary. Outcomes are out-of-scope; tier assignments and threshold numbers are in-scope but context-dependent.
- The "Adapting to Local Context" paragraph in [How to Use This Taxonomy](#how-to-use-this-taxonomy) provides practical examples; this principle file states the underlying commitment.
- The Threshold Guidance Provenance preludes on tightened Tier 1 metrics show calibration acting in practice, distinguishing cited from proposed-as-starting-points thresholds.

### Future direction

This principle may be refined as deployment experience accumulates. The six axes named here are an initial structural cut; real deployments may surface a seventh (e.g. consultation-modality mix where virtual-care is dominant), and the taxonomy will accept evolution of this principle as part of a future release. The structural commitment — that calibration is named, documented, and reviewable — is the part that doesn't change.

---
