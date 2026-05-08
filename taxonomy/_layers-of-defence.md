## Layers of Defence

This section is a first-class principle of the taxonomy, parallel to the [Outcomes Boundary](#outcomes-boundary) and the [Calibration & Context principle](#calibration-context): **AVT assurance composes from three layers, and no layer is sufficient on its own**. The principle is named here so the architectural shape of the taxonomy is visible — not just the per-metric detail.

### The three layers

- **Prevention** — gates that stop bad systems entering service. One-off pre-deployment checks, procurement-time attestations, regulatory classification, contractual commitments. Prevention is necessary but never sufficient: the deployment landscape changes, the model updates, the population drifts, the failure modes that pass at gate-time emerge later.

- **Detection** — continuous monitoring that catches emerging failures. In-service measurement of model behaviour, workflow signals, and downstream outcomes. Detection is what gives prevention its teeth retrospectively (you find out the gate missed something) and gives limitation its trigger (an alert fires that activates the response). Detection is necessary but never sufficient: a metric with no escalation path is just a number.

- **Limitation** — governance infrastructure that bounds damage when detection fires. Incident reporting, board-level oversight, vendor-side correction commitments, deployer-side rollback capability, post-market surveillance, retirement notification, decommissioning data handling. Limitation is what turns a detected failure into a closed-loop response rather than an open-loop drift.

**Why all three.** A capability tested only at prevention is exposed to deployment-time drift. A capability tested only at detection has no closed-loop response to alerts. A capability tested only at limitation is responding to failures that better prevention or detection should have caught earlier. **Defensible AVT assurance requires all three layers for every safety-critical failure mode** — and the catalogue is structured so this composition can be checked.

### How metrics are classified into layers

**Two-tier classification (v5.5.0+).** Some metrics carry an **explicit `Layer` field** in their dimensions table (Prevention / Detection / Limitation); others fall back to a **cadence heuristic**.

- **Explicit `Layer`** is the authoritative answer where present. Seeded in v5.5.0 with 33 metrics from an early-draft slide-deck classification (the original "minimum viable assurance" presentation). Future releases will extend explicit classification to the rest of the catalogue.
- **Cadence heuristic** is the v5.5.0 fallback for the ~200 metrics that don't yet have an explicit `Layer`: One-off gate → Prevention; Continuous / Periodic audit → Detection; Event-triggered → Limitation. **The heuristic is wrong about a third of the time** — it conflates always-on limitation infrastructure with detection (e.g. LFPSE incident reporting runs continuously but its purpose is to bound damage, not detect drift) and miscategorises pre-deployment gates with continuous nominal cadence as detection. Treat as a starting point.

The by-layer-of-defence cross-cut page renders both cohorts separately so the distinction is visible to readers.

### How the layers correlate with other dimensions

Even with explicit classification, the cadence / lifecycle / cluster signals correlate with layer membership in predictable ways:

| Layer | Strongest signal | Cluster bias | Cadence bias | Lifecycle Phase bias |
|---|---|---|---|---|
| **Prevention** | One-off pre-deployment gates | GV.CR (compliance), parts of GV.VT (vendor transparency), GV.SG (safety case) | `One-off gate` | `Pre-deployment` |
| **Detection** | Continuous in-service measurement | TP (pipeline), HL (workflow), IO (outcomes), parts of GV.SG (drift) | `Continuous` / `Periodic audit` | `Continuous` |
| **Limitation** | Incident response + governance infrastructure | GV.SG (incident metrics), GV.VT (disclosure / retirement), GV.CR-12 (board oversight), GV.PD (decommissioning) | `Event-triggered` (often paired with another) | `Continuous` (the infrastructure is always-on; activation is event-driven) |

**The cluster bias is approximate, not definitive.** A metric in GV.CR can act as a detection signal (e.g. GV.CR-13 Refusal Impact-Explanation Quality is periodic-audit detection of explanation drift), and a metric in TP can act as a prevention gate (e.g. TP.AC-5 Microphone Hardware Validation is a one-off pre-deployment hardware gate). The cluster signals which layer the metric *typically* serves; the per-metric Cadence and Lifecycle Phase tell you which layer it actually serves in this particular construct.

### Worked examples

These walk through three failure modes and show how the three layers compose. The aim is not to enumerate every relevant metric — it is to show whether the chain is connected: *does each layer have something, and do the metrics in adjacent layers actually trigger each other?*

#### Hallucination (clinical-content fabrication or distortion)

- **Prevention:** [GV.CR-9 FDA PCCP-Equivalent Pre-Defined Acceptance Criteria](#gv-cr-9), [GV.SG-18 PCCP Documentation Completeness](#gv-sg-18), [GV.PD-12 Training Data Representativeness Documentation](#gv-pd-12), [GV.CR-11 Medical Device Classification Documentation](#gv-cr-11) — pre-deployment gates that stop a known-fabricating model from going live or being retrained without acceptance criteria.
- **Detection:** [TP.SN-5 Hallucination Rate](#tp-sn-5), [TP.SN-7 Factual Verification](#tp-sn-7), [HL.HF-1 Edit Rate](#hl-hf-1), [HL.HF-2 Edit Type Classification](#hl-hf-2), [GV.SG-3 Performance Degradation Detection Latency](#gv-sg-3) — in-service measurement that catches fabrication emerging from a passing-at-gate model.
- **Limitation:** [GV.SG-11 Adverse Event / Incident Rate (LFPSE)](#gv-sg-11), [GV.SG-15 Time-to-Correct](#gv-sg-15), [GV.VT-5 Incident Disclosure Compliance](#gv-vt-5), [GV.CR-12 Board-Level AI Governance Mechanism](#gv-cr-12), [TP.WB-5 Write-back Rollback Capability](#tp-wb-5) — incident response infrastructure that bounds damage when detection fires.

The chain is **complete**: detection metrics fire (HR rises) → limitation metrics activate (incident logged via LFPSE; board sees it; rollback activated). The connection between *layer 2 firing* and *layer 3 activating* is partly contractual (vendor side) and partly procedural (deployer side); the metric catalogue makes both visible but does not enforce the connection.

#### Bias drift (population-stratified performance degradation)

- **Prevention:** [GV.PD-12 Training Data Representativeness Documentation](#gv-pd-12) (population coverage at training time), [GV.PD-7 Training Data Inclusion Status](#gv-pd-7) (data flow disclosure).
- **Detection:** [TP.ASR-4 Demographic-Disaggregated WER](#tp-asr-4), [TP.ASR-5 Speaker-Stratified WER](#tp-asr-5), [TP.CC-9 Coding Equity Index](#tp-cc-9), [IO.FE-1 Deployment Equity Index](#io-fe-1), [IO.FE-2 Accent Taxonomy Standardisation](#io-fe-2), [IO.FE-4 Intersectional Performance](#io-fe-4) — the entire Demographic Equity Disaggregation family is detection.
- **Limitation:** thinner. [GV.SG-4 Retraining Trigger Threshold Specification](#gv-sg-4) names the threshold; [GV.VT-1 Model Change Notification Compliance](#gv-vt-1) requires the vendor to communicate retraining; [GV.CR-12 Board-Level AI Governance Mechanism](#gv-cr-12) provides oversight. **There is no dedicated bias-incident-reporting metric** equivalent to GV.SG-11 for safety incidents.

The chain has a **named gap at limitation** — bias drift detected by IO.FE-1 has no analogue to LFPSE for routing the finding into a deployer-side or national-level incident response. This is one of the ways the layers-of-defence cut surfaces actionable architectural gaps.

#### Medication error

- **Prevention:** [GV.CR-9](#gv-cr-9) acceptance criteria for medication-coding accuracy at gate-time; [GV.PD-12](#gv-pd-12) representative training data covering medication contexts.
- **Detection:** the entire [Medication Safety Thread family](families.md#medication-safety-thread) — [TP.SN-19 Medication Attribute Extraction F1](#tp-sn-19), [TP.SN-21 Medication Event Classification](#tp-sn-21), [TP.CC-5 dm+d Medication Coding Accuracy](#tp-cc-5), and the downstream [IO.PX-10 Medication Error Rate Differential](#io-px-10).
- **Limitation:** [GV.SG-11 Adverse Event / Incident Rate (LFPSE)](#gv-sg-11) (medication errors are reportable patient safety incidents), [GV.SG-15 Time-to-Correct](#gv-sg-15), [GV.VT-5 Incident Disclosure Compliance](#gv-vt-5).

The chain is **complete and well-instrumented across all three layers** — partly because medication safety has a long-established NHS reporting infrastructure (LFPSE) that the AVT-specific metrics dock into. This is what a fully-connected three-layer chain looks like.

### Capabilities currently exposed at fewer than three layers

Honest known gaps where the three-layer composition is incomplete in the current catalogue:

- **Bias drift** — limitation layer is thin (no dedicated bias-incident-reporting analogue to LFPSE). See bias-drift example above.
- **Privacy notice currency** — [GV.PD-13](#gv-pd-13) is detection (annual currency check) and prevention (initial publication), but limitation is implicit: there is no metric that names *what activates when a privacy notice is found stale*. Caught by IG inspection rather than by a named limitation metric.
- **AVT-specific cybersecurity** — [GV.SC-1/-2/-6](#gv-sc-1) prompt-injection / jailbreak / template-injection are detection-flavoured, but the prevention and limitation layers depend on general organisation-level cybersecurity (DSPT, Cyber Essentials Plus via [GV.SC-12](#gv-sc-12)) rather than AVT-specific named gates. The MHRA WP5 and FTS notice are silent on AVT-specific cybersecurity testing cadence — this is partly why the v5.3.0 promotions held GV.SC-1/-2/-6 at Tier 2.
- **Patient experience / harm to therapeutic relationship** — strong detection layer ([IO.PX-2](#io-px-2), [IO.PX-6](#io-px-6), [IO.PX-7](#io-px-7)), but prevention is implicit (Caldicott-Guardian sign-off via [GV.PD-17](#gv-pd-17) is the closest gate) and limitation is documentation-shaped (board oversight via [GV.CR-12](#gv-cr-12), patient complaint handling — a deferred §2d gap).

### How to use this principle

When designing or reviewing an AVT assurance plan:

1. **List the safety-critical failure modes** the deployment is exposed to (hallucination, bias drift, medication error, privacy breach, etc.).
2. **For each failure mode, identify metrics at all three layers.** If any layer is missing or thin, document the architectural gap.
3. **Verify the inter-layer connections** — does the detection metric have a named escalation path? Does the limitation infrastructure have a documented activation trigger? The catalogue makes the metrics visible; the deployer is responsible for connecting them.
4. **Calibrate by failure-mode severity** — for the highest-severity modes, all three layers should be substantively instrumented; for lower-severity modes, partial coverage may be defensible.

The taxonomy does not enforce the three-layer composition because failure modes vary by deployment context. It surfaces the architectural shape so the composition is visible and gaps are nameable.

### Relationship to other taxonomy principles

- **[Outcomes Boundary](#outcomes-boundary)** names what is *out of scope* (clinical-outcome validation belongs to national research bodies). Layers of Defence names how *in-scope* assurance composes.
- **[Calibration & Context](#calibration-context)** says tier assignments and threshold numbers are starting points, not universal gates. Layers of Defence says no single layer is sufficient regardless of how well-calibrated each individual metric is — composition matters as much as calibration.
- **[Named Metric Families](families.md)** group metrics by shared *construct*; layers of defence groups them by shared *function* in the assurance architecture. The two cuts are orthogonal: the Demographic Equity Disaggregation family is mostly detection-layer; the NHSE IG Attestation family spans all three layers.
