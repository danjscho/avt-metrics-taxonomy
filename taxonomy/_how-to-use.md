## How to Use This Taxonomy

This taxonomy is designed to serve multiple audiences — from a practice CSO deploying their first AVT system to a national body designing evaluation infrastructure. The tiering system, cadence labels, and responsible actor assignments are designed to help each reader find the metrics that are relevant, actionable, and appropriately prioritised for their role.

### Priority Tiers

Each metric is assigned to one of three priority tiers. The tier reflects a composite judgement across three dimensions: how consequential the metric is for patient safety, whether it is measurable today with existing tools and data, and what governance burden it imposes on the responsible actor. A metric can be critically important but placed in Tier 3 because the infrastructure to measure it does not yet exist — the tier reflects actionability, not importance.

**🟢 Tier 1 — Minimum Viable Assurance** (33 metrics)

The smallest set of metrics that a deployer cannot responsibly skip. Every metric in Tier 1 meets all three criteria: it addresses a safety-critical or governance-essential function, it is measurable today by the responsible actor without requiring infrastructure that doesn't yet exist, and the burden of measurement is proportionate to the risk it monitors. A deployer operating AVT without measuring these metrics is operating without adequate governance — regardless of the vendor's own quality claims.

**🟡 Tier 2 — Recommended Assurance** (59 metrics)

What a deployer or regional body should measure given reasonable governance capacity and vendor cooperation. Tier 2 metrics are important for comprehensive assurance but either require some vendor cooperation that may need contractual enforcement, involve more resource-intensive measurement methods, or provide granularity that strengthens but is not strictly essential for basic safe operation.

**🔵 Tier 3 — Advanced / Research** (59 metrics)

Metrics that are important for advancing the field but are not actionable at individual deployer level today. Tier 3 metrics fall into this category for one of three reasons: they require national infrastructure that hasn't been built, they require research methods not yet scalable to routine deployment, or they are vendor-proprietary approaches that inform what a national standard should require but cannot be independently replicated. Tier 3 is not 'unimportant' — several Tier 3 metrics address the most fundamental questions about AVT safety. They are Tier 3 because the answer to 'can a CSO do this tomorrow?' is currently no.

### Measurement Cadence

Each metric carries a cadence label indicating how often it should be measured:

**🚪 One-off gate (pre-deployment)** — measured once before go-live as an acceptance criterion. Includes hardware validation, write-back fidelity testing, acoustic environment profiling, and pre-deployment benchmarks. Gate metrics must pass before the system enters clinical use. Some should be re-tested when significant changes occur (new EPR version, hardware change, model update), but they are not continuous monitoring requirements.

**📡 Continuous** — measured on an ongoing basis during operational use, ideally automated. Includes edit rate, time-to-sign, system availability, integration error rate, model version tracking, and the automated self-consistency checks. Continuous metrics should feed into dashboards visible to the clinical lead and CSO. Many can be derived from EPR workflow telemetry without additional clinical effort.

**🔄 Periodic audit** — measured at defined intervals through deliberate assessment activity. Includes hallucination/omission rate audits, error injection testing (quarterly), trust calibration surveys (annually), demographic WER re-testing, and the safety-critical chain of custody trace. Periodic audits require protected time and clinical resource — they are the most expensive cadence and should be scheduled in advance.

The cadence and tier interact: a Tier 1 continuous metric (edit rate) is low-burden and high-value — it should be running from Day Zero. A Tier 2 periodic metric (error injection audit) is higher-burden but provides uniquely valuable data — it should be scheduled quarterly once the system is stable. A Tier 3 periodic metric (clinical decision equivalence) is too resource-intensive for routine deployment but should be performed by national evaluation programmes.

### Responsible Actors

Each metric identifies who should measure it. The same metric may appear under multiple actors with different roles:

**Vendor** — responsible for pre-deployment benchmarking, continuous system telemetry, model version transparency, and security testing. Vendors control the data and infrastructure for many metrics that deployers cannot independently assess (WER, DER, demographic disaggregation, adversarial robustness). Vendor-side metrics should be contractually specified at procurement.

**Deployer** (practice, trust, or provider) — responsible for operational monitoring that occurs at the point of clinical use: edit rates, review behaviour, patient opt-out, training compliance, and periodic clinical note audits. Deployers are the primary actor for human factors metrics because these can only be measured where the human-AI interaction occurs.

**Regional (ICB)** — responsible for cross-practice comparison, deployment equity monitoring, coding drift detection, and CSO capacity oversight. The regional tier exists because some metrics only become meaningful when aggregated across multiple deployer sites — cross-practice variance is invisible to any individual practice.

**National Body** — responsible for infrastructure that enables everyone else's metrics: establishing evaluation standards, creating independent benchmark datasets, defining LFPSE reporting categories, and funding national evaluation programmes. Many Tier 3 metrics would move to Tier 2 or Tier 1 if national infrastructure existed.

**Academic** — responsible for developing and validating new metrics, conducting the resource-intensive evaluations (clinical decision equivalence, chilling effect, skill attenuation), and providing independent evidence that is not conflicted by vendor or deployer interests.

A metric listed under 'Vendor, Deployer' typically means the vendor must provide the data or infrastructure, and the deployer must use it for governance — for example, model version tracking requires the vendor to log versions but the deployer to monitor for changes and trigger re-evaluation.

### Adapting to Local Context

Tier assignments reflect a general assessment of priority and actionability. Local context should adjust them:

A practice with a high proportion of EAL (English as Additional Language) patients should treat demographic-disaggregated WER as Tier 1 rather than Tier 2 — the equity risk is elevated for their population. A practice using AVT for multi-party consultations (interpreter-mediated, family present) should treat multi-party robustness as Tier 1 because they are routinely operating in a scenario most systems are not validated for. A practice where clinicians have been customising prompt templates should treat template underspecification and template injection vulnerability as Tier 1 because the safety case may have been invalidated by modifications. An ICB with AVT deployed across practices of varying digital maturity should prioritise cross-practice variance and deployment equity.

The principle is: if a Tier 2 or Tier 3 metric addresses a risk that is elevated in your specific context, promote it. The tiers are a starting point, not a ceiling.

