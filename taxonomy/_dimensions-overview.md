## Dimensions Overview

This page is the reader's orientation to the **structural cuts** the taxonomy makes. Every metric body carries a dimensions table with up to 12 fields; this page explains what each cut does, why it exists separately from the others, and how to use it. Readers commonly conflate cuts that are structurally distinct (Tier vs Layer of Defence, Family vs Cluster, Cadence vs Lifecycle Phase) — this page names those distinctions.

Per-dimension detail lives in the dedicated cross-cutting pages where present. This page is the **map** to those cuts; the dedicated pages are the territory.

---

## What's a dimension?

A **dimension** is an attribute that every (or most) metrics carry, audit-enforced where the value is a closed enum, and used to drive the cross-cutting site pages (by tier, by applicability, by responsible actor, etc.). A dimension is a structural taxonomy concern — different from per-metric attributes that vary too freely to enumerate (the metric's name, its formal definition, its limitations prose).

The taxonomy distinguishes two kinds of structural attribute:

- **Closed-enum dimensions** — values come from a fixed list (Tier ∈ {1, 2, 3}; Maturity ∈ {Established, Emerging, Vendor-Proprietary, Proposed/Novel}). Audit-enforced; used to build cross-cut site pages.
- **Open-text dimensions** — values are free text from a curated convention but not enum-bounded (Source row, Family value before audit-enforcement). Surfaced in CSV/JSON but not structurally constrained.

Sub-clusters and italic intro paragraphs are *not* dimensions — they are within-group readability aids. Named metric families *are* dimension-shaped (audit-enforced via the Family field) but are documented separately on the [Families](families.md) page.

---

## The cuts at a glance

| Dimension | Answers | Values | Strongest contrast |
|---|---|---|---|
| **Reference** | What is this metric's stable identifier? | TP.AC-1, GV.PD-13, etc. | n/a — identity not classification |
| **Priority Tier** | How essential is this metric to a defensible deployment? | 🟢 1 / 🟡 2 / 🔵 3 | vs Layers of Defence (function) — Tier is *importance*, Layer is *role in assurance architecture* |
| **Applicability** | How AVT-specific is this metric? | AVT-Specific / AVT-Contextualised / General Healthcare AI | vs Cluster — Applicability is about generalisability; Cluster is about pipeline placement |
| **Family** | Is this metric part of a named construct cluster? | One of 8 declared families, or absent | vs Cluster — Family is shared *construct*, Cluster is shared *pipeline location* |
| **Pipeline Layer** | Where in the AVT processing chain does this metric sit? | Audio Capture / ASR / Diarisation / Summarisation / Coding / Downstream Write-back / Cross-cutting | vs Cluster — Layer is the technical pipeline stage; Cluster is the catalogue's content-organisation grouping |
| **Assurance Question** | What kind of question does this metric answer? | Safety / Privacy / Fairness / Quality / Patient Experience / Transparency / Governance / Meta-evaluation / Human Factors | vs Cluster — Assurance Question is *what we want to know*, Cluster is *where the metric lives* |
| **Measurement Method** | How is this metric measured? | Computational / Human Review / Hybrid / Passive Observational | vs Lifecycle Phase — Method is *how*, Lifecycle is *when* |
| **Lifecycle Phases** | When in the deployment lifecycle is this metric measured? | Pre-deployment / Day Zero Baseline / Periodic Audit / Continuous | vs Cadence — Lifecycle is *what phase*, Cadence is *how often* |
| **Measurement Cadence** | How often is this metric re-measured? | One-off gate / Periodic audit / Continuous / Event-triggered (multi-valued, semicolon-separated) | vs Lifecycle Phase — Cadence is *frequency within a phase*, Lifecycle is *which phase* |
| **Responsible Actors** | Who is accountable for measuring or acting on this metric? | Vendor / Deployer / Clinician / Regional (ICB) / National (NHSE) (multi-valued) | vs Layers of Defence — Actor is *who*, Layer is *what role in the architecture* |
| **Maturity** | How well-established is this metric's measurement science? | Established / Emerging / Vendor-Proprietary / Proposed/Novel | vs Tier — Maturity is *measurement-science maturity*, Tier is *deployment importance*; a Proposed/Novel metric can be Tier 1 |
| **Outcome Type** | Is this metric proximal (what we measure now) or distal (downstream patient outcome)? | Proximal / Distal | vs Assurance Question — Outcome Type names *measurement scope*, Assurance Question names *content area* |
| **Source** | What external authority anchors this metric? | One or more catalogue handles + free-text rationale | vs Maturity — Source is *what's cited*, Maturity is *how settled the science is* |

---

## Per-dimension detail

### Reference (Reference ID)

**Answers:** what is this metric's stable identifier?

**Format:** `<Cluster>.<Group>-<Number>` (e.g. `TP.AC-1`, `GV.PD-13`). Sub-parts use a single lowercase letter suffix (`HL.HF-3a`).

**What it's NOT:** Reference is *identity*, not classification. Two metrics with adjacent ref-IDs (`GV.PD-13` and `GV.PD-14`) are not necessarily related — they share a cluster and group, but their family / tier / layer-of-defence membership is independent. Reference IDs are stable across releases per the [deprecate-don't-renumber convention](versioning.md#deprecation-policy); retired IDs are recorded in `_retired-ids.md` and never reused.

**See also:** [Versioning](versioning.md) for the v5.3.0 gap-candidate ID-allocation convention shift.

### Priority Tier

**Answers:** how essential is this metric to a defensible deployment?

**Values:** 🟢 Tier 1 (Minimum Viable Assurance) / 🟡 Tier 2 (Recommended Assurance) / 🔵 Tier 3 (Advanced / Research).

**What it's NOT:** Tier is **not** a layer of defence. Tier 1 metrics span all three layers (prevention, detection, limitation); a Tier 1 metric can be a one-off prevention gate (GV.CR-11), a continuous detection signal (GV.SG-3), or limitation infrastructure (GV.CR-12). Tier is also **not** maturity — a Proposed/Novel metric can be Tier 1 if the obligation it tests is named in regulation even when the measurement science is unsettled (e.g. GV.CR-13 Refusal Impact-Explanation Quality at Tier 2 with rubric pending; GV.VT-10 MHRA Transparency Content Completeness at Tier 2 with WP-2 pending).

**See also:** [How to use this taxonomy](how-to-use.md) for the tier-by-actor minimum-set; [Tier 1 quick reference](tier-1-quick-reference.md) for the full Tier 1 enumeration; [Layers of Defence](layers-of-defence.md) for the architectural cut.

### Applicability

**Answers:** how AVT-specific is this metric?

**Values:** AVT-Specific (50 metrics) / AVT-Contextualised (79) / General Healthcare AI (105).

**What it's NOT:** Applicability is **not** Pipeline Layer or Cluster. A metric can be AVT-Specific in any cluster (e.g. TP.AC-1 SNR Monitoring is AVT-Specific because microphone SNR matters specifically to ambient capture); a metric can be General Healthcare AI in the TP cluster (e.g. several TP.WB write-back metrics generalise to any clinical AI writing to an EPR). Applicability is about whether the metric's *construct* generalises; Cluster is about where it sits in the catalogue's content organisation.

**See also:** [Applicability](applicability.md) for the per-cluster breakdown and worked examples.

### Family *(new in v5.4.0)*

**Answers:** is this metric part of a named construct cluster?

**Values:** one of 8 declared families (see [Families](families.md)) or absent. Family is *optional* — most metrics are unaffiliated.

**What it's NOT:** Family is **not** Cluster. Cluster (TP / PI / HL / IO / GV / ES) groups by pipeline location and content-organisation; Family groups by *shared construct*, often crossing clusters. The Demographic Equity Disaggregation family spans TP, IO, and (implicitly) PI; the NHSE IG Attestation family spans GV.CR and GV.PD. A metric belongs to at most one family (no multi-membership) but to exactly one cluster.

**See also:** [Families](families.md) for the family framings and member lists.

### Pipeline Layer

**Answers:** where in the AVT processing chain does this metric sit?

**Values:** Audio Capture / ASR / Diarisation / Summarisation / Clinical Coding / Downstream Write-back / Cross-cutting. (Cross-cutting metrics — most of GV — don't sit at a single pipeline stage.)

**What it's NOT:** Pipeline Layer is **not** Cluster. Cluster is a *taxonomy organisation* attribute (which folder the metric lives in); Pipeline Layer is a *technical architecture* attribute (which processing stage the metric tests). They overlap heavily — TP cluster maps onto pipeline layers TP.AC through TP.WB — but GV metrics with `Pipeline Layer: Cross-cutting` live across the technical pipeline, not at a single stage.

### Assurance Question

**Answers:** what kind of question does this metric answer for the deployer?

**Values:** Safety / Privacy / Fairness / Quality / Patient Experience / Transparency / Governance / Meta-evaluation / Human Factors.

**What it's NOT:** Assurance Question is **not** Cluster or Pipeline Layer. A Privacy metric can sit in any cluster (e.g. TP.SN-24 Stigmatising Language Replication Rate has Assurance Question: Patient Experience but lives in TP.SN). The cut answers *what concern the metric addresses*, not *where it sits in the pipeline*.

### Measurement Method

**Answers:** how is this metric measured in practice?

**Values:** Computational (algorithmic / automated) / Human Review (sample-based human assessment) / Hybrid (computational pre-filter + human verification) / Passive Observational (telemetry / log analysis without active measurement intervention).

**What it's NOT:** Method is **not** Cadence or Lifecycle Phase. The same metric can be Continuous Computational (TP.SN-5 in production), or One-off Human Review (GV.CR-9 at procurement gate). Method is *how the data is gathered*; Cadence is *how often*; Lifecycle Phase is *during which deployment phase*.

### Lifecycle Phases

**Answers:** during which deployment lifecycle phase is this metric measured?

**Values:** Pre-deployment / Day Zero Baseline / Periodic Audit / Continuous (multi-valued — a metric can be measured across multiple phases).

**What it's NOT:** Lifecycle Phase is **not** Cadence. Lifecycle Phase names *which deployment phase the measurement happens in*; Cadence names *how often it repeats within that phase*. Many metrics are `Lifecycle: Continuous` and `Cadence: Continuous` — but a metric can be `Lifecycle: Pre-deployment` and `Cadence: One-off gate` (GV.CR-9), or `Lifecycle: Continuous` and `Cadence: Event-triggered` (GV.SG-2 Model Update Impact Score — continuously eligible to fire, fires only when a model update happens).

### Measurement Cadence

**Answers:** how often is this metric re-measured?

**Values:** One-off gate / Periodic audit / Continuous / Event-triggered. **Multi-valued** since v5.1.0 — a metric can be `Continuous; Event-triggered` (continuously logged, with re-test triggered by specific events).

**What it's NOT:** Cadence is **not** Lifecycle Phase (see above). Cadence is also **not** Layer of Defence — though there's a strong correlation (one-off gate ≈ prevention; continuous ≈ detection; event-triggered often ≈ limitation), the cut surfaces are different. A One-off gate cadence can serve any layer (a one-off vendor-retirement notification check is limitation-layer infrastructure measured at one-off cadence).

**See also:** [Versioning](versioning.md) for the v5.1.0 multi-valued-cadence convention; [Layers of Defence](layers-of-defence.md) for the related-but-distinct architectural cut.

### Responsible Actors

**Answers:** who is accountable for measuring this metric or acting on its results?

**Values:** Vendor / Deployer / Clinician / Regional (ICB) / National (NHSE). Multi-valued — most metrics name two actors (a measurement actor and an action actor; or a vendor-side measurement and a deployer-side verification).

**What it's NOT:** Responsible Actor is **not** Layer of Defence. Vendor-attributed metrics serve all three layers (vendor-side prevention via PCCP documentation; vendor-side detection via telemetry; vendor-side limitation via incident disclosure). A metric can also have multiple Responsible Actors at different layers — e.g. GV.SG-1 Model Version Tracking is Vendor (provides logs) + Deployer (triggers GV.SG-2 workflow on change-event).

### Maturity

**Answers:** how well-established is the measurement science behind this metric?

**Values:** Established (validated, in use at scale) / Emerging (concept defined, AVT-specific validation thin) / Vendor-Proprietary (one or more vendors have implemented internally; not openly published) / Proposed / Novel (taxonomy-author proposed, not yet measured at scale).

**What it's NOT:** Maturity is **not** Tier. Tier is *deployment importance*; Maturity is *measurement-science maturity*. A regulator-named obligation (e.g. NHSE IG section X) creates a Tier 1 importance even if no validated rubric exists yet — those metrics land at Tier 1 with Maturity: Proposed/Novel and a follow-up to upgrade Maturity once a rubric is piloted.

**See also:** the underspecification warnings (in the [Summary](index.md#by-underspecification-warning)) flag the 15 metrics where Maturity is genuinely contested (Tier A: no methodology / Tier B: concept defined no AVT validation / Tier C: technically defined but clinical validity unproven).

### Outcome Type

**Answers:** is this metric measuring a proximal signal (what's happening in the AVT pipeline now) or a distal signal (downstream patient outcome)?

**Values:** Proximal / Distal.

**What it's NOT:** Outcome Type is **not** Pipeline Layer. Pipeline Layer names *where in the AVT processing chain*; Outcome Type names *how far downstream from the AVT system the measurement reaches*. A Pipeline-Layer-Cross-cutting metric can be Proximal (GV.SG-1 Model Version Tracking) or Distal (IO.PX-9 Downstream Diagnostic Accuracy). The Outcomes Boundary principle limits how far Distal the taxonomy reaches — clinical-outcome validation belongs to national research bodies, not deployers.

**See also:** [Outcomes Boundary](outcomes-boundary.md).

### Source

**Answers:** what external authority or evidence base anchors this metric?

**Values:** one or more `[CatalogueHandle]` references plus free-text rationale. Catalogue handles resolve to entries in `_references.md` with title, publisher, URL, Wayback snapshot, and retrieval date.

**What it's NOT:** Source is **not** Maturity. Source names *what the metric cites*; Maturity names *how settled the underlying measurement science is*. A metric can have a strong Source (peer-reviewed paper, regulatory guidance) but Proposed/Novel Maturity if the AVT-specific operationalisation has not been validated. The pairing matters: Source + Maturity together tell the reader how much weight to give the metric's recommended thresholds.

**See also:** [References catalogue](references.md) for the canonical handle resolutions.

---

## How dimensions compose

The 12 dimensions are deliberately overlapping but structurally distinct. A reader who finds two cuts confusing is usually looking at one of three patterns:

**Pattern 1 — orthogonal cuts that look correlated.**
Tier and Maturity correlate weakly (most Tier 1 metrics are Established or Emerging) but are not the same — see Maturity above. Family and Cluster correlate moderately (most Clinical Content Fidelity members are in TP.SN) but a family can span clusters.

**Pattern 2 — derived cuts that look like new dimensions.**
Layers of Defence is *not* a recorded dimension — it is derived from Cadence + Lifecycle Phase + Cluster. AI-Substrate (a future v5.5+ candidate, see plan-future #10) is similarly derived from Pipeline Layer + Responsible Actor. Derived cuts are documented as cross-cutting principle pages, not as per-metric attributes.

**Pattern 3 — hierarchy that looks flat.**
Cluster contains Group contains Metric. Pipeline Layer is mostly determined by Group but has Cross-cutting as a non-pipeline value. Some readers expect a single hierarchy; the taxonomy uses several overlapping hierarchies because no single structure captures every assurance question.

---

## Where each dimension lives

- **Per-metric body** (dimensions table): all 12 listed above.
- **CSV / JSON downloads:** all 12 listed above (under field names: `ref_id`, `tier`, `applicability`, `family`, `pipeline_layer`, `assurance_question`, `measurement_method`, `lifecycle_phases`, `cadence`, `responsible_actors`, `maturity`, `source`).
- **Site cross-cuts:** by-tier, by-applicability, by-cluster, by-Playbook-principle, by-ethical-theme (the Playbook + theme cuts are *not* per-metric dimensions; they are derived from the Responsible AI Lens).
- **Audit:** closed-enum dimensions are audit-enforced (Tier, Applicability, Family, Maturity, Cadence, plus presence checks for Source).
