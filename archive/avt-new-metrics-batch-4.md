# AVT Metrics Taxonomy — New Metric Entries (Batch 4 — FINAL)

Final batch, completing Part E and Part F additions.

**Contents**
- Privacy & Data Governance — 5 new metrics
- Operational — 3 new metrics
- **Environmental & Sustainability** (new top-level group) — 3 new metrics
- Vendor Transparency & Contractual — 1 new metric
- Meta-evaluation — 2 new metrics

**Total this batch: 14 entries**

---

## Privacy & Data Governance additions (+5)

### 🟡 PII Extraction Attack Success Rate

Adversarial privacy testing: the rate at which a determined attacker can extract patient personal data from the deployed AVT system through model interaction. Includes prompt-based extraction (crafted queries that coax the model to reproduce training content), inversion attacks (reconstructing inputs from outputs), and side-channel extraction. Complements the Membership Inference Attack AUC metric — MIA tells you whether a specific patient was in training; PII extraction tells you what content about them can be recovered.

|Dimension              |Value                                                              |
|-----------------------|-------------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                             |
|**Measurement Cadence**|Periodic audit                                                     |
|**Pipeline Layer**     |Cross-cutting                                                      |
|**Assurance Question** |Safety                                                             |
|**Measurement Method** |Computational                                                      |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                     |
|**Responsible Actors** |Vendor, Academic                                                   |
|**Maturity**           |Emerging                                                           |
|**Outcome Type**       |Proximal                                                           |
|**Source**             |IEEE S&P 2023 LLM PII leakage study; OWASP LLM Top 10 (Sensitive Information Disclosure)|

**Why this tier?**

> Vendor-side red-team testing requirement. Deployers cannot independently test model-internal privacy properties. Should be a procurement requirement with results provided by vendor or independent assessor.

**Formal Definition**

```
Success Rate = |PII_items_successfully_extracted| / |PII_items_attempted|. Attack categories: (1) direct prompting ("what did the patient say about their family history?"); (2) completion-based extraction (prompting partial records and measuring reconstruction); (3) inversion attacks on embeddings; (4) canary extraction using known inserted content. Report per attack category — aggregate success rate obscures category-specific weaknesses.
```

**Limitations**

> Defining the attack surface is itself contested. A test suite that looks adequate today may be outdated tomorrow. Vendors may resist third-party red-teaming on competitive grounds. Extraction that is theoretically possible but requires massive query budgets may or may not be a practical concern depending on threat model.

**Novel Thinking / Implications**

> 💡 The OWASP LLM Top 10 lists Sensitive Information Disclosure as a standard vulnerability class, but most AVT vendors have not engaged with it as a distinct security category — privacy is typically treated as "we don't train on customer data" rather than as an active red-teaming target. The shift from passive privacy posture to adversarial privacy testing is the maturity marker. A vendor who has never had their system red-teamed for PII extraction should not be deployed into NHS clinical settings.

-----

### 🟢 Audio Time-to-Deletion

Measured time from consultation end to verified deletion of the captured audio. Operational implementation of the existing Audio Retention Compliance metric. NHS England's March 2026 IG guidance requires deletion of audio after the summary is signed off, unless explicitly retained for safety monitoring with documented justification. This metric measures whether the deletion is actually happening in the timeframe the policy claims.

|Dimension              |Value                                                        |
|-----------------------|-------------------------------------------------------------|
|**Priority Tier**      |🟢 Tier 1 — Minimum Viable                                    |
|**Measurement Cadence**|Continuous                                                   |
|**Pipeline Layer**     |Cross-cutting                                                |
|**Assurance Question** |Safety                                                       |
|**Measurement Method** |Computational                                                |
|**Lifecycle Phases**   |Continuous                                                   |
|**Responsible Actors** |Vendor, Deployer                                             |
|**Maturity**           |Established                                                  |
|**Outcome Type**       |Proximal                                                     |
|**Source**             |NHSE IG guidance on ambient scribing (March 2026); UK GDPR Article 5(1)(e) storage limitation|

**Why this tier?**

> Direct compliance requirement. Measurable through vendor-provided deletion telemetry. Binary-ish: deletion within policy timeframe or not. Should be continuously monitored rather than periodically audited.

**Formal Definition**

```
Time-to-Deletion = t_deletion_verified - t_consultation_end. Report distribution: median, P95, P99, and count of encounters exceeding policy threshold. Verification requirement: deletion confirmed in primary storage, caches, backups, and any downstream analytic systems. Policy threshold per deployer: typically 24 hours to 7 days depending on DPIA. Compliance = proportion of encounters with verified deletion within threshold.
```

**Limitations**

> Verification across all storage locations is technically difficult — backup systems and distributed caches may retain data after primary deletion. Vendor attestation is often the only feasible verification method. The word "deletion" itself has degrees (logical deletion / physical deletion / cryptographic erasure) that matter for real assurance.

**Novel Thinking / Implications**

> 💡 "Audio is deleted after sign-off" is a policy statement that only has governance value if it's actually measured. The gap between policy and practice on deletion is often substantial — audio persists in backup systems, error logs, annotation pipelines, and quality monitoring infrastructure long after the "deletion" event. Making time-to-deletion a measured metric rather than a policy assertion is the minimum required for the NHS IG guidance to have operational effect.

-----

### 🟢 Transcript Retention Compliance

Parallel metric to Audio Time-to-Deletion, but for transcripts. Often treated as less sensitive than audio — and therefore retained longer — but transcripts are in many ways more risky because they are structured, searchable, and readily consumable by downstream systems. A transcript of a consultation discussing mental health, substance use, or safeguarding concerns is arguably more sensitive than the audio because it removes the friction of listening and enables programmatic analysis.

|Dimension              |Value                                                         |
|-----------------------|--------------------------------------------------------------|
|**Priority Tier**      |🟢 Tier 1 — Minimum Viable                                     |
|**Measurement Cadence**|Continuous                                                    |
|**Pipeline Layer**     |Cross-cutting                                                 |
|**Assurance Question** |Safety                                                        |
|**Measurement Method** |Computational                                                 |
|**Lifecycle Phases**   |Continuous                                                    |
|**Responsible Actors** |Vendor, Deployer                                              |
|**Maturity**           |Established                                                   |
|**Outcome Type**       |Proximal                                                      |
|**Source**             |NHSE IG guidance on ambient scribing (March 2026); UK GDPR Article 5(1)(e)|

**Why this tier?**

> Direct compliance requirement. Should be measured in parallel with Audio Time-to-Deletion. Often more operationally tractable because transcripts are typically held in vendor-controlled systems rather than distributed storage.

**Formal Definition**

```
For each transcript: retention duration = t_current - t_consultation_end. Retention policy specifies maximum duration for each purpose: summary generation (typically hours), review support (typically days), quality monitoring (variable, documented in DPIA). Compliance = |transcripts_retained_within_policy| / |total_transcripts|. Report per retention purpose — aggregating different retention justifications obscures policy adherence.
```

**Limitations**

> Retention for "quality monitoring" is often a catch-all that effectively keeps transcripts indefinitely. Tightening this requires specific retention periods per monitoring purpose. Cross-system retention (transcript in vendor system, derived metadata in deployer analytics, redacted version in research database) creates a tangled retention picture.

**Novel Thinking / Implications**

> 💡 Transcripts are the highest-value/highest-risk intermediate representation in AVT. They contain everything said, in structured form, searchable, and often retained for longer than either the audio or the final note. An attacker who compromises transcript storage has far more exposure than one who compromises the final clinical records. Retention minimisation for transcripts is arguably more important than for audio, but it's rarely treated that way in DPIAs.

-----

### 🟡 Re-identification Risk Assessment

Structured assessment of the risk that de-identified data retained for quality improvement, research, or secondary use can be re-identified. Applies to any dataset derived from AVT operation — anonymised transcripts for model quality review, de-identified notes for research, aggregate statistics that may become identifying at small sample sizes. Standard privacy methodology applied to AVT-specific data flows.

|Dimension              |Value                                                 |
|-----------------------|------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                |
|**Measurement Cadence**|Periodic audit                                        |
|**Pipeline Layer**     |Cross-cutting                                         |
|**Assurance Question** |Safety                                                |
|**Measurement Method** |Human Review                                          |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                        |
|**Responsible Actors** |Deployer, Vendor                                      |
|**Maturity**           |Established                                           |
|**Outcome Type**       |Proximal                                              |
|**Source**             |ICO anonymisation code of practice; NIST privacy framework|

**Why this tier?**

> Standard privacy methodology. Should be part of any DPIA for secondary uses. Periodic reassessment required as new data are added and as re-identification techniques evolve.

**Formal Definition**

```
Per retained dataset: assess re-identification risk against standard criteria — (1) direct identifiers present or removed? (2) quasi-identifiers (age, postcode, date, rare condition) combinable to identify individuals? (3) k-anonymity achieved and at what k? (4) l-diversity for sensitive attributes? (5) differential privacy applied? (6) motivated intruder test — could a determined attacker re-identify individuals given reasonably available auxiliary information? Overall risk rating: low / medium / high / unacceptable. Threshold for retention: risk must be low or medium with explicit justification.
```

**Limitations**

> Re-identification risk is probabilistic and depends on what auxiliary information an attacker has access to. Small clinical populations (rare conditions, small practices) are re-identifiable from very little information. "De-identified" is not the same as "anonymous".

**Novel Thinking / Implications**

> 💡 A single NHS practice with 5,000 patients has very few patients with any given rare condition — sometimes just one. A "de-identified" transcript mentioning that condition is trivially re-identifiable by anyone with access to the practice's patient list. Re-identification risk assessment forces this question into visibility during DPIA rather than treating de-identification as a technical checkbox.

-----

### 🟡 Training Data Inclusion Status

Clear documentation of whether deployer audio, transcripts, or notes are used by the vendor for model training or fine-tuning. Distinct from the existing Sub-Processor Transparency metric (which covers processing activity) and from privacy policies (which often hedge this question). This metric requires an explicit binary answer: is NHS data flowing into the vendor's training pipeline, yes or no, with documented consent basis if yes.

|Dimension              |Value                                                          |
|-----------------------|----------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                          |
|**Measurement Cadence**|One-off gate                                                    |
|**Pipeline Layer**     |Cross-cutting                                                   |
|**Assurance Question** |Safety                                                          |
|**Measurement Method** |Human Review                                                    |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                  |
|**Responsible Actors** |Vendor, Deployer                                                |
|**Maturity**           |Proposed / Novel                                                |
|**Outcome Type**       |Proximal                                                        |
|**Source**             |UK GDPR transparency requirements; derived from emerging AVT procurement practice|

**Why this tier?**

> Procurement gate. Should be explicitly answered in vendor contracts, not left to policy ambiguity. Annual reassessment on contract renewal.

**Formal Definition**

```
Status recorded as: (a) No — deployer data not used for any training or fine-tuning; (b) Yes — used for training with specified consent basis and opt-out mechanism; (c) Derived — used for aggregated statistics or distilled features without retaining source data. Each status has different governance implications. Documentation must specify which model components may be trained (ASR, summariser, coder) and which data types (audio, transcripts, notes, metadata). Vendor attestation required; independent verification is not currently feasible.
```

**Limitations**

> Verification relies on vendor attestation. The distinction between "training" and "quality improvement" can be blurred by vendors in ways that obscure actual data flows. Aggregate statistics derived from training data may themselves carry privacy risk.

**Novel Thinking / Implications**

> 💡 Many NHS AVT contracts are ambiguous about training data flows because vendors benefit from keeping the option open and deployers often don't ask explicitly. Making this a Tier 2 procurement metric forces the question into contract negotiations. The patient-level consequence is that AVT-using consultations may effectively contribute to training the next generation of commercial AI systems — and patients should know this if it's happening. This is a transparency obligation the existing taxonomy's consent metrics don't capture.

-----

## Operational additions (+3)

### 🟡 Pyjama Time / After-Hours EHR Use

Clinician time spent on EHR and documentation work outside of scheduled clinical hours. Standard burnout-adjacent metric from the Sinsky et al. literature. Applied to AVT assessment, it measures whether documentation burden that was shifted from in-consultation to after-consultation (a known pattern with review-before-signing workflows) has simply moved the burden to outside working hours rather than reducing it.

|Dimension              |Value                                                      |
|-----------------------|------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                      |
|**Measurement Cadence**|Continuous                                                  |
|**Pipeline Layer**     |Cross-cutting                                               |
|**Assurance Question** |Operational                                                 |
|**Measurement Method** |Passive Observational                                       |
|**Lifecycle Phases**   |Day Zero Baseline, Continuous                               |
|**Responsible Actors** |Deployer                                                    |
|**Maturity**           |Established                                                 |
|**Outcome Type**       |Distal                                                      |
|**Source**             |Sinsky et al., Mayo Clinic Proceedings; American Medical Association EHR use studies|

**Why this tier?**

> Established methodology. Derivable from EHR audit logs without additional instrumentation. Essential for distinguishing genuine workload reduction from workload redistribution.

**Formal Definition**

```
Pyjama Time = time spent in EHR outside of scheduled clinic hours per clinician per week. Derived from EHR audit logs (timestamp of user actions vs rostered working hours). Pre/post AVT comparison: ΔPyjama Time = Pyjama_post - Pyjama_pre. A genuine workload reduction shows Pyjama Time decrease; a redistribution shows Pyjama Time stable or increasing even as in-consultation documentation time falls.
```

**Limitations**

> Audit logs may not capture all EHR activity (mobile access, shadow work in parallel documents). Definition of "working hours" varies by role and contract. Some pyjama time reflects preferred work pattern rather than workload pressure.

**Novel Thinking / Implications**

> 💡 This is the metric that catches the most common AVT failure mode for clinician wellbeing: the system reduces typing time during consultations but creates after-hours review work that the clinician was not previously doing. In-consultation time savings are visible and marketable; after-hours burden is invisible and unpaid. A deployment that shows documentation time saved per consultation should also show pyjama time decreased — if only the first moves, the value proposition is shifted burden, not reduced burden.

-----

### 🟡 Note Turnaround Time

Elapsed time from consultation end to note availability in the EPR, measured from the clinician's perspective rather than the pipeline's internal latency. Extends the existing Full-Pipeline Latency Budget (which is a technical metric) into an operational workflow metric that directly affects review quality. If the note arrives after the clinician has started the next patient, review happens later in lower-quality conditions or not at all.

|Dimension              |Value                                                      |
|-----------------------|------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                      |
|**Measurement Cadence**|Continuous                                                  |
|**Pipeline Layer**     |End-to-End                                                  |
|**Assurance Question** |Operational                                                 |
|**Measurement Method** |Computational                                               |
|**Lifecycle Phases**   |Continuous                                                  |
|**Responsible Actors** |Vendor, Deployer                                            |
|**Maturity**           |Established                                                 |
|**Outcome Type**       |Proximal                                                    |
|**Source**             |Standard operational workflow metric; extends Full-Pipeline Latency Budget|

**Why this tier?**

> Operational metric derivable from EPR workflow data. Directly affects review quality and therefore safety. Should be continuously monitored and reported.

**Formal Definition**

```
Turnaround Time = t_note_available_in_EPR - t_consultation_end. Report distribution: median, P50, P90, P99. Clinically relevant threshold: proportion of notes available before the start of the next patient's consultation. A turnaround time distribution with long tails creates selective review failure — the notes most delayed are the ones most likely to be approved without meaningful review.
```

**Limitations**

> End of consultation is not always cleanly timestamped. Network conditions, EPR availability, and other operational factors affect turnaround independent of AVT processing time.

**Novel Thinking / Implications**

> 💡 The existing Full-Pipeline Latency Budget captures technical processing time; note turnaround captures the clinically meaningful delay. The difference is everything else — queueing, EPR write-back latency, user interface delays, notification lag. A vendor who optimises only their pipeline latency without addressing end-to-end turnaround is optimising for the wrong metric.

-----

### 🟡 Documentation Workload Composite

Composite metric grouping Documentation Time per Consultation, Pyjama Time, and Note Turnaround Time into a single workload assessment. The family-level metric for documentation burden. Reports change in total workload rather than change in individual components — which is the number that matters for the value proposition and clinician wellbeing assessment.

|Dimension              |Value                                                                 |
|-----------------------|----------------------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                                |
|**Measurement Cadence**|Periodic audit                                                        |
|**Pipeline Layer**     |Cross-cutting                                                         |
|**Assurance Question** |Operational                                                           |
|**Measurement Method** |Computational                                                         |
|**Lifecycle Phases**   |Day Zero Baseline, Periodic Audit                                     |
|**Responsible Actors** |Deployer                                                              |
|**Maturity**           |Proposed / Novel                                                      |
|**Outcome Type**       |Distal                                                                |
|**Source**             |Sinsky et al. extended to AVT context; NHS workforce wellbeing frameworks|

**Why this tier?**

> Composite metric built from component metrics measured separately. Quarterly rollup enables trajectory reporting to clinical leadership without requiring separate measurement work.

**Formal Definition**

```
Workload Composite = w1 × Documentation_Time + w2 × Pyjama_Time + w3 × Verification_Burden. Weights reflect relative clinical significance; default equal weights. Per-clinician and aggregate reporting. Change metric: ΔWorkload = Workload_post_AVT - Workload_pre_AVT. Negative ΔWorkload = genuine net reduction; positive = net increase despite in-consultation savings.
```

**Limitations**

> Aggregation hides component-level patterns. A composite that stays stable may mask simultaneous decrease in documentation time and increase in pyjama time — the stable number obscures the pattern shift. Report composite alongside components, not instead of them.

**Novel Thinking / Implications**

> 💡 The composite is the honest answer to "did AVT reduce workload?" that the individual metrics cannot give alone. A practice reporting "saved 3 minutes per consultation" without composite reporting is answering a convenient question; a practice reporting composite workload change is answering the real one. Clinical leadership and commissioners should request composite reporting rather than selective component reporting.

-----

# Environmental & Sustainability — NEW TOP-LEVEL GROUP (+3)

*Energy, carbon, and water footprint of AVT operation. Not Day Zero priority for clinical safety assurance but increasingly required for NHS procurement (Net Zero commitments) and for EU-market vendors under forthcoming sustainability reporting requirements. All Tier 3 currently because the measurement infrastructure is immature and the metrics are not deployer-actionable — but they are well-defined conceptually and may move to Tier 2 as the NHS Net Zero procurement framework matures.*

*Tier breakdown: 🔵 3 Tier 3*

### 🔵 Energy Consumption per Clinical Note

Electrical energy cost of generating a single clinical note, measured in watt-hours. Depends on model architecture, hosting infrastructure, and query complexity. Published benchmarks for general-purpose LLM inference range from 0.42 Wh for simple queries to 29 Wh for complex prompts — a 70× range that makes provider choice consequential for total energy footprint.

|Dimension              |Value                                                      |
|-----------------------|------------------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                              |
|**Measurement Cadence**|Periodic audit                                              |
|**Pipeline Layer**     |Cross-cutting                                               |
|**Assurance Question** |Operational                                                 |
|**Measurement Method** |Computational                                               |
|**Lifecycle Phases**   |Periodic Audit                                              |
|**Responsible Actors** |Vendor                                                      |
|**Maturity**           |Emerging                                                    |
|**Outcome Type**       |Distal                                                      |
|**Source**             |Jegham et al., arXiv 2505.09598 (2025) — "How Hungry is AI?"|

**Why this tier?**

> Vendor-side measurement. Not deployer-actionable today but reportable. NHS procurement will increasingly ask this question as Net Zero commitments mature.

**Formal Definition**

```
Energy per Note (Wh) = total_inference_energy / number_of_notes_generated. Measured at the inference infrastructure level. Per-model reporting required because architecture choice dominates the metric. Break down into: ASR energy, summarisation energy, coding energy. Scale: multiply by annual note volume to estimate annual energy cost of deployment.
```

**Limitations**

> Vendor access to per-note energy telemetry is typically not exposed to customers. Hosting infrastructure varies, making direct vendor comparison difficult. Published benchmarks use standardised prompts that don't reflect real clinical usage patterns.

**Novel Thinking / Implications**

> 💡 At the NHS scale (potentially millions of consultations per year using AVT), even small per-note energy differences compound into substantial total footprint. An NHS-wide AVT deployment using a 29 Wh/note model consumes ~70× more energy than the same deployment on a 0.42 Wh/note model. This is not a dominant clinical assurance question but it is a material procurement question under NHS Net Zero — and reporting it creates the data visibility that lets procurement use it.

-----

### 🔵 Carbon Emissions per Inference

Greenhouse gas emissions per clinical note, measured in grams of CO₂-equivalent. Distinct from energy consumption because carbon intensity depends on the hosting region's electricity grid — the same model hosted in a coal-heavy grid vs a renewable-heavy grid has very different carbon footprint despite identical energy use. Relevant to NHS Net Zero procurement and to EU-market vendors under corporate sustainability reporting requirements.

|Dimension              |Value                                                             |
|-----------------------|-------------------------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                                     |
|**Measurement Cadence**|Periodic audit                                                     |
|**Pipeline Layer**     |Cross-cutting                                                      |
|**Assurance Question** |Operational                                                        |
|**Measurement Method** |Computational                                                      |
|**Lifecycle Phases**   |Periodic Audit                                                     |
|**Responsible Actors** |Vendor                                                             |
|**Maturity**           |Emerging                                                           |
|**Outcome Type**       |Distal                                                             |
|**Source**             |Mistral AI lifecycle assessment; Jegham et al. 2025 — grid carbon intensity adjustment|

**Why this tier?**

> Vendor-reported metric. NHS Net Zero relevant for procurement. Cannot be measured by deployers.

**Formal Definition**

```
gCO₂e per Note = energy_per_note × grid_carbon_intensity(hosting_region, time). Report: (a) current grid intensity at hosting location; (b) marginal emissions (electricity that would not have been consumed without this inference); (c) embodied emissions amortised over model lifetime. NHS procurement comparison: total annual gCO₂e = gCO₂e_per_note × annual_note_volume. Compare against NHS trust carbon budgets to contextualise.
```

**Limitations**

> Grid carbon intensity data are approximate and vary by time of day. Marginal vs average emissions methodology is contested. Embodied emissions from model training are difficult to attribute to individual inferences.

**Novel Thinking / Implications**

> 💡 Hosting region choice is a lever NHS procurement could use: a vendor hosted in regions with lower-carbon grids has lower per-note emissions for identical models. This creates a potential procurement criterion distinct from clinical performance — and may create pressure for vendors to offer UK or low-carbon hosting options as a Net Zero differentiator. Whether NHS procurement will actually weight this remains to be seen.

-----

### 🔵 Water Consumption per Query

Water consumed by data centre cooling infrastructure per clinical note inference. Measured in millilitres. Increasingly required for NHS Net Zero procurement given water stress considerations in parts of the UK and in cloud hosting regions globally. Less visible than energy and carbon but material at AVT-deployment scale.

|Dimension              |Value                                              |
|-----------------------|----------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                      |
|**Measurement Cadence**|Periodic audit                                      |
|**Pipeline Layer**     |Cross-cutting                                       |
|**Assurance Question** |Operational                                         |
|**Measurement Method** |Computational                                       |
|**Lifecycle Phases**   |Periodic Audit                                      |
|**Responsible Actors** |Vendor                                              |
|**Maturity**           |Emerging                                            |
|**Outcome Type**       |Distal                                              |
|**Source**             |Jegham et al. 2025; Li et al. "Making AI Less Thirsty"|

**Why this tier?**

> Vendor-reported. Least mature of the environmental metrics but increasingly appearing in sustainability frameworks.

**Formal Definition**

```
mL per Note = data_centre_water_usage_effectiveness (WUE) × energy_per_note. Direct water (cooling) and indirect water (electricity generation). Report per-note and annual total. Compare against regional water stress indices for hosting locations.
```

**Limitations**

> Water consumption data are rarely reported by cloud providers. Estimation methodology is in early development. Indirect water (electricity generation) typically dominates direct water, so attribution is complex.

**Novel Thinking / Implications**

> 💡 Water consumption is the sustainability metric that feels abstract until it becomes locally consequential. An AVT deployment drawing on a data centre in a water-stressed region is indirectly connected to water policy there. NHS sustainability frameworks are still developing their position on this, but it will become a procurement question over the next few years as water stress visibility increases.

-----

## Vendor Transparency & Contractual additions (+1)

### 🟡 Intermediate Output Access

Whether the vendor provides contractual access to intermediate pipeline outputs — the raw transcript, the diarised transcript, the pre-coding summary, the model-internal confidence scores — rather than exposing only the final note. Prerequisite for the existing Error Attribution Analysis metric, and necessary for meaningful incident investigation. Without intermediate outputs, when an error is discovered in the final note, the investigation cannot determine which pipeline stage introduced it.

|Dimension              |Value                                                    |
|-----------------------|----------------------------------------------------------|
|**Priority Tier**      |🟡 Tier 2 — Recommended                                    |
|**Measurement Cadence**|One-off gate                                              |
|**Pipeline Layer**     |Cross-cutting                                             |
|**Assurance Question** |Meta-evaluation                                           |
|**Measurement Method** |Human Review                                              |
|**Lifecycle Phases**   |Pre-deployment                                            |
|**Responsible Actors** |Vendor                                                    |
|**Maturity**           |Proposed / Novel                                          |
|**Outcome Type**       |Proximal                                                  |
|**Source**             |Prerequisite for existing Error Attribution Analysis metric; Stanford monitoring framework|

**Why this tier?**

> Procurement gate. Should be contractually specified. Required for any deployer intending to run Error Attribution Analysis, Chain of Custody traces, or Safety-Critical Information Chain of Custody (which is Tier 2 in the existing taxonomy but depends on intermediate output access to be executable).

**Formal Definition**

```
Access assessed across stages: (1) raw ASR transcript; (2) diarised transcript with speaker labels; (3) pre-summarisation processing outputs; (4) generated summary before coding; (5) coding suggestions before selection; (6) final output; (7) model confidence scores per stage. Access granularity: on-demand for individual encounters (required for incident investigation); bulk export for audit (required for Error Attribution Analysis); real-time streaming (optional, useful for monitoring). Binary per stage; target is full access to stages 1–6 on demand, with confidence scores (7) as advanced capability.
```

**Limitations**

> Vendors resist intermediate output access on commercial grounds — the intermediate outputs reveal pipeline architecture and model choices. Contractual access may be granted at high cost or with usage restrictions. Without independent verification, deployers cannot confirm that the "intermediate outputs" provided are authentic rather than reconstructions.

**Novel Thinking / Implications**

> 💡 Many of the highest-value metrics in this taxonomy — Error Attribution Analysis, Source-to-Record Concordance, Safety-Critical Information Chain of Custody, Error Cascade Analysis — depend on intermediate output access that vendors rarely provide. Making this a procurement gate creates pressure for vendors to either provide access or compete on terms with those who do. Without contractual intermediate output access, most sophisticated assurance metrics are theoretical rather than operational.

-----

## Meta-evaluation additions (+2)

### 🔵 LLM-Judge Bias Quantification

Systematic measurement of known biases in LLM-as-a-Judge evaluation: position bias (prefers first response in pairwise comparison), verbosity bias (prefers longer responses), self-enhancement bias (prefers outputs from the same model family), and fine-grained scoring unreliability (inconsistent discrimination at high score ranges). Required for interpreting LLM-Judge metrics responsibly. The Croxford et al. 2025 study found GPT-o3-mini achieving ICC 0.818 with human evaluators on PDSQI-9 — but a separate Rwanda clinical LLM evaluation study found LLM judges correlated more strongly with non-expert than expert annotators, indicating that apparent reliability may reflect alignment with a particular class of evaluator rather than with ground truth.

|Dimension              |Value                                                                |
|-----------------------|---------------------------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                                       |
|**Measurement Cadence**|Periodic audit                                                       |
|**Pipeline Layer**     |Cross-cutting                                                        |
|**Assurance Question** |Meta-evaluation                                                      |
|**Measurement Method** |Computational                                                        |
|**Lifecycle Phases**   |Pre-deployment, Periodic Audit                                       |
|**Responsible Actors** |Academic, National Body                                              |
|**Maturity**           |Emerging                                                             |
|**Outcome Type**       |Proximal                                                             |
|**Source**             |Croxford et al. 2025 (npj Digital Medicine); Rwanda clinical LLM evaluation study|

**Why this tier?**

> Research-grade meta-evaluation. Academic and national body responsibility. Not routinely performed but necessary for anyone relying on LLM-as-a-Judge outputs for safety-critical decisions.

**Formal Definition**

```
Bias tests: (1) Position bias — reverse pairwise ordering and measure agreement with original judgment (perfect judge = 100% consistency under reversal); (2) Verbosity bias — compare judgments on pairs matched on quality but varying in length; (3) Self-enhancement — test judge on outputs from its own model family vs other families; (4) Score range reliability — measure inter-rater agreement at high scores (e.g. 4 vs 5 on Likert) vs across full range. Composite: bias-adjusted reliability = raw reliability corrected for each bias type.
```

**Limitations**

> Bias testing requires carefully constructed adversarial test sets. Results don't transfer across judge models or domains. Bias adjustments are approximations, not corrections.

**Novel Thinking / Implications**

> 💡 The Rwanda finding is the uncomfortable one: LLM judges may correlate well with human evaluators while correlating poorly with ground truth. This is the worst failure mode for evaluation — apparent reliability that validates a biased assessment. Any deployment relying on LLM-as-a-Judge for safety decisions (not just for efficiency) needs to have run bias quantification and documented the residual uncertainty. Otherwise the high ICC number is theatrical rather than informative.

-----

### 🔵 Automated-Human Metric Concordance

Systematic measurement of how well automated metrics correlate with expert human evaluation across deployments. Meta-metric that validates (or invalidates) the automated metrics themselves. Without concordance measurement, automated metrics are running on the assumption that they track what human experts would measure — but the ROUGE Kendall-Tau finding of 0.080 with human clinical judgment (Croxford et al. 2025) shows that assumption can be wildly wrong.

|Dimension              |Value                                                             |
|-----------------------|-------------------------------------------------------------------|
|**Priority Tier**      |🔵 Tier 3 — Advanced / Research                                     |
|**Measurement Cadence**|Periodic audit                                                     |
|**Pipeline Layer**     |Cross-cutting                                                      |
|**Assurance Question** |Meta-evaluation                                                    |
|**Measurement Method** |Hybrid                                                             |
|**Lifecycle Phases**   |Periodic Audit                                                     |
|**Responsible Actors** |National Body, Academic                                            |
|**Maturity**           |Emerging                                                           |
|**Outcome Type**       |Distal                                                             |
|**Source**             |Standard meta-evaluation methodology; Croxford et al. 2025 (ROUGE Kendall-Tau 0.080)|

**Why this tier?**

> Meta-evaluation requiring paired automated and human assessment data. National evaluation programme responsibility. Establishes the evidence base for treating automated metrics as trustworthy proxies.

**Formal Definition**

```
For each automated metric m in deployed use: collect a sample of N encounters scored by both m and by expert human evaluators using a validated instrument (e.g. PDSQI-9, CREOLA taxonomy). Compute correlation (Pearson, Spearman, Kendall's tau). Concordance Threshold: metric is "adequate as proxy" only if correlation > 0.5. Metrics with correlation < 0.3 should not be used as standalone quality indicators regardless of technical sophistication. Report concordance per metric with confidence intervals.
```

**Limitations**

> Requires paired human-automated scoring, which is expensive. Inter-human agreement is itself imperfect, creating a ceiling on achievable concordance. Results may not transfer across deployment contexts (a metric that concords well in primary care may fail in secondary care).

**Novel Thinking / Implications**

> 💡 This is the metric that polices the other metrics. Without concordance data, the taxonomy's automated metrics are running on an unverified assumption that they measure what human experts measure. The ROUGE finding is the canonical example of that assumption failing — a metric in widespread use has essentially zero correlation with clinical judgment and is used anyway because it's easy to compute. Periodic concordance measurement should be a national evaluation programme responsibility, and any metric with concordance < 0.3 should be explicitly flagged in the taxonomy as inadequate as a standalone indicator.

-----

# End of Batch 4 — DRAFTING COMPLETE

**Metrics drafted in this batch: 14**
- Privacy & Data Governance: 5 (PII Extraction Attack Success Rate, Audio Time-to-Deletion, Transcript Retention Compliance, Re-identification Risk Assessment, Training Data Inclusion Status)
- Operational: 3 (Pyjama Time / After-Hours EHR Use, Note Turnaround Time, Documentation Workload Composite)
- Environmental & Sustainability — new top-level group: 3 (Energy Consumption per Clinical Note, Carbon Emissions per Inference, Water Consumption per Query)
- Vendor Transparency & Contractual: 1 (Intermediate Output Access)
- Meta-evaluation: 2 (LLM-Judge Bias Quantification, Automated-Human Metric Concordance)

**Final total across Batches 1–4: 63 new metric entries drafted**

---

## Summary of the complete drafting exercise

| Batch | Sections | New metrics |
|---|---|---|
| 1 | ASR, Diarisation, Summarisation, Clinical Coding, EPR Write-back | 21 |
| 2 | End-to-End, Human Factors, Patient Experience, Fairness | 12 |
| 3 | Longitudinal Drift, NHS Compliance & Regulatory (new group), Security | 16 |
| 4 | Privacy, Operational, Environmental & Sustainability (new group), Vendor, Meta-evaluation | 14 |
| **Total** | | **63** |

**Tier distribution of new metrics:**
- 🟢 Tier 1 — Minimum Viable: 9 new metrics (8 of which are in NHS Compliance & Regulatory, plus Code Hallucination Rate in Clinical Coding)
- 🟡 Tier 2 — Recommended: 28 new metrics
- 🔵 Tier 3 — Advanced / Research: 26 new metrics

**New groups added:** 2
- NHS Compliance & Regulatory (10 metrics)
- Environmental & Sustainability (3 metrics)

**New sub-clusters within existing groups:** 4
- Conversation Analysis (in Diarisation, 5 metrics)
- Sociotechnical & Resilience (in Human Factors & Workflow, 4 metrics)
- Patient Clinical Outcomes (in Patient Experience, 4 metrics)
- Longitudinal Drift & Model Contamination (in Safety & Governance, 4 metrics)

**Post-integration taxonomy total: 151 + 63 = 214 metrics across 20 groups**

---

## Next passes required (separate from new-metric drafting)

The new entries are now drafted and ready for integration. Three follow-up passes remain before the v2 taxonomy is complete:

1. **Consolidation framings** — four parent-construct introductory paragraphs (Clinical Content Fidelity, Post-Generation Correction, Clinical Transcription Accuracy, Reference-Based Text Similarity) plus cross-reference additions between existing metrics in those families
2. **Underspecification warnings** — ~15 additions to existing metrics flagging specific literature findings (ROUGE Kendall-Tau 0.080, trust calibration instrument gaps, attention drift definitional absence, etc.)
3. **Cross-cutting additions** — the resource gap callout on ACI Bench and PriMock as the only two public benchmarks; updates to the Summary and Tier 1 Quick Reference sections to reflect the new metrics; the new-group introductory paragraphs for NHS Compliance & Regulatory and Environmental & Sustainability

These are smaller exercises than the metric drafting and can each be completed in a single pass on request.
