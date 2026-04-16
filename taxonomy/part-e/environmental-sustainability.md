## Environmental & Sustainability

*Energy, carbon, and water footprint of AVT operation. All three current metrics in this group are Tier 3 — not Day Zero priority for clinical safety assurance, but increasingly required for NHS procurement under Net Zero commitments and cascading through EU-market vendor compliance under forthcoming corporate sustainability reporting requirements.*

*The group exists more as placeholder for an expected future than as a cluster of actionable metrics today. The measurement infrastructure is immature: vendors rarely expose per-inference telemetry; cloud providers are not consistent in sustainability reporting; methodology for attributing training emissions to individual inferences is contested; water consumption data is especially limited. None of the current metrics are deployer-measurable — they are vendor-reported, and deployers currently have no independent verification path.*

*All three metrics may move to Tier 2 as the NHS Net Zero procurement framework matures and as vendor sustainability reporting becomes routine. At the scale of potential NHS AVT deployment (millions of consultations per year), even small per-note environmental differences compound into substantial total footprint, and procurement conversations are starting to ask the question even where answers are uneven.*

**Tier breakdown**: 🔵 3 Tier 3

### GV.EN-1 🔵 Energy Consumption per Clinical Note

Electrical energy cost of generating a single clinical note, measured in watt-hours. Depends on model architecture, hosting infrastructure, and query complexity. Published benchmarks for general-purpose LLM inference range from 0.42 Wh for simple queries to 29 Wh for complex prompts — a 70× range that makes provider choice consequential for total energy footprint.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.EN-1 |
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Source** | Jegham et al., arXiv 2505.09598 (2025) — "How Hungry is AI?" |

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

---

### GV.EN-2 🔵 Carbon Emissions per Inference

Greenhouse gas emissions per clinical note, measured in grams of CO₂-equivalent. Distinct from energy consumption because carbon intensity depends on the hosting region's electricity grid — the same model hosted in a coal-heavy grid vs a renewable-heavy grid has very different carbon footprint despite identical energy use. Relevant to NHS Net Zero procurement and to EU-market vendors under corporate sustainability reporting requirements.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.EN-2 |
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Source** | Mistral AI lifecycle assessment; Jegham et al. 2025 — grid carbon intensity adjustment |

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

---

### GV.EN-3 🔵 Water Consumption per Query

Water consumed by data centre cooling infrastructure per clinical note inference. Measured in millilitres. Increasingly required for NHS Net Zero procurement given water stress considerations in parts of the UK and in cloud hosting regions globally. Less visible than energy and carbon but material at AVT-deployment scale.

| Dimension | Value |
|-----------|-------|
| **Reference** | GV.EN-3 |
| **Priority Tier** | 🔵 Tier 3 — Advanced / Research |
| **Measurement Cadence** | Periodic audit |
| **Pipeline Layer** | Cross-cutting |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Periodic Audit |
| **Responsible Actors** | Vendor |
| **Maturity** | Emerging |
| **Outcome Type** | Distal |
| **Source** | Jegham et al. 2025; Li et al. "Making AI Less Thirsty" |

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

---
