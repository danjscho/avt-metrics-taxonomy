## AI-Substrate Classification

This section names a **derived cut** the taxonomy makes available to readers who want to ask "which metrics test the AI itself, vs the infrastructure around the AI, vs the governance of the AI?" Those are different questions, and they sit orthogonally to the Tier / Family / Layer-of-Defence cuts already documented elsewhere.

This is a **derived** classification (v5.5.3+) — there is no `AI Substrate` field on metric bodies, but the classification is **computed at build time** from cluster + per-metric overrides and surfaced through the `by-ai-substrate/` cross-cut pages and the `ai_substrate` column in CSV / JSON downloads. The page is the canonical home for the framing; the build-time derivation is the operational surface.

### The five substrate classes

- **Pre-AI** — metrics that test infrastructure that exists *before* the AI runs and would still matter if the AI weren't there. Hardware quality, signal capture, data minimisation at the input stage. The AI inherits these but doesn't create them.
- **AI-Substrate** — metrics that test the AI model itself: its outputs, its calibration, its bias, its hallucination rate, its drift. The model is the load-bearing component of the metric.
- **Post-AI** — metrics that test the infrastructure that consumes AI output: write-back fidelity, EPR integration, downstream coding accuracy. The AI produces; these test what happens next.
- **AI-Mediated Workflow** — metrics that test the human-AI interaction: clinician review behaviour, edit patterns, automation bias, time-to-sign. The metric is about how the human and the AI compose, not about either alone.
- **AI-Agnostic Governance** — metrics that test deployer-side or vendor-side governance infrastructure that is *substantively the same whether the system is AI or not*: DPIA completion, board oversight, privacy notice currency, sub-processor disclosure. AI-deployed systems trigger the obligation, but the metric tests organisational behaviour rather than AI behaviour.

### How this cut evolved

In v5.4.0 the taxonomy considered three options for surfacing this cut (plan-future #10):

1. **Add an `AI Substrate` dimension** on every metric body — high authoring cost (236 entries), structurally enforceable.
2. **Derive at build time** from existing dimensions — low cost, covers ~80% cleanly, with a `disputed` category for genuine edge cases.
3. **Documentation-only framing page** — lowest cost, no structural change, depends on the reader doing the lookup.

**v5.5.0 landed Option 3** as a starting point. The plan-future #10 promotion criteria were: prototype Option 2 against ~30 metrics; if `disputed` covers >20% of metrics, the cut is too fuzzy and Option 3 stays.

**v5.5.3 promotes to Option 2.** Prototyping the derivation against the full 236-metric catalogue (cluster defaults + ~10 per-metric overrides for genuine edge cases) yielded **0% disputed** — well under the >20% rule. The classification is now build-time-derived and surfaced as a per-metric attribute (CSV/JSON `ai_substrate` field) and a cross-cut site surface (`by-ai-substrate/` pages, one per class).

**The promotion is non-structural** — there is still no `AI Substrate` field on metric bodies. The classification lives in `parse._AI_SUBSTRATE_GROUP_DEFAULTS` and `parse._AI_SUBSTRATE_OVERRIDES`. This keeps cluster files unchanged while making the cut operationally available.

### How to derive class from existing dimensions

For most metrics, the class is obvious from Pipeline Layer + Cluster:

| Pipeline Layer | Typical class |
|---|---|
| Audio Capture (TP.AC) | Pre-AI |
| ASR / Diarisation / Summarisation / Clinical Coding (TP.ASR / TP.DI / TP.SN / TP.CC) | AI-Substrate |
| Downstream Write-back (TP.WB) | Post-AI |
| Cross-cutting + Cluster: HL | AI-Mediated Workflow |
| Cross-cutting + Cluster: GV | mostly AI-Agnostic Governance, with exceptions |
| Cross-cutting + Cluster: IO.PX | AI-Mediated Workflow (patient experience of the AI-using clinician) |
| Cross-cutting + Cluster: IO.FE | AI-Substrate (fairness of the model) or AI-Mediated (fairness of the human-AI workflow), depending on the metric |
| Cross-cutting + Cluster: ES | AI-Substrate (most ES.ME metrics test the model) |

GV is the cluster with the most class diversity:

- **AI-Substrate** subset of GV: GV.SG (most safety-governance metrics test the model — drift, contamination, hazard logs); GV.SC (most security metrics test AI-specific attack surfaces — prompt injection, jailbreak); parts of GV.PD (training-data metrics).
- **AI-Agnostic Governance** subset of GV: GV.CR (most compliance-regulatory metrics test attestations); GV.VT (vendor-transparency metrics test contractual relationships); most of GV.PD (data-handling metrics that pre-exist AI); GV.OP (operational metrics that test deployment economics, not AI behaviour); GV.TC (training-and-competency metrics that test clinician knowledge); GV.EN (environmental metrics).

### Worked examples

**TP.SN-5 Hallucination Rate** — clearly **AI-Substrate**. The metric is exactly "the AI is producing content that isn't in the source"; without the AI there is no metric.

**TP.AC-1 Signal-to-Noise Ratio Monitoring** — **Pre-AI**. The microphone hardware would matter for any audio capture (clinical or not, AI or not). The AI inherits the SNR; it doesn't create it.

**TP.WB-8 PRSB Semantic Completeness** — **Post-AI**. The AI generates the output; this metric tests whether the output, once written to the EHR, contains the mandatory PRSB elements. The AI can pass content fidelity (TP.WB-1) and field mapping (TP.WB-3) and still fail PRSB completeness — a Post-AI failure mode.

**HL.HF-1 Edit Rate** — **AI-Mediated Workflow**. The metric is exactly "what proportion of AI-generated notes do clinicians edit before signing?" — neither pure AI-Substrate (the human's behaviour is the load-bearing variable) nor pure governance (the metric is per-encounter not organisational).

**GV.CR-7 DPIA Template Completion Rate** — **AI-Agnostic Governance**. DPIAs pre-date AVT; the metric tests whether the deployer has filled out the standard form, not anything specific to the AI's behaviour. AI deployment triggers the obligation but the metric tests deployer documentation discipline.

**GV.SG-3 Performance Degradation Detection Latency** — **AI-Substrate**. The metric is about detecting when the *model's behaviour* has degraded; it requires AI-specific telemetry that no non-AI system would generate.

**GV.PD-12 Training Data Representativeness Documentation** — **disputed**: simultaneously AI-Substrate (the underlying concern is whether the model can perform across the population) and AI-Agnostic Governance (the metric tests whether documentation exists). For now: classify as AI-Substrate because the underlying construct is model-fairness-readiness; the documentation is the surface.

**GV.SC-1 Prompt Injection Resistance Rate** — **AI-Substrate**. Prompt injection is an LLM-specific attack surface; pre-LLM systems do not have this failure mode.

**GV.SC-12 Cyber Essentials Plus Certification Status** — **AI-Agnostic Governance**. Cyber Essentials Plus is a general organisational cyber-hygiene certification; the AI-deployed organisation needs it for the same reasons any digital health organisation does.

### Why care about this cut

Different audiences want different views of the catalogue. This cut serves four concrete questions:

1. **Vendor evaluation teams** building model-evaluation infrastructure want the **AI-Substrate** subset — they're the metrics that need new test harnesses, datasets, and continuous-integration tooling. (~40-50% of the catalogue.)

2. **Deployer IG and governance teams** want the **AI-Agnostic Governance** subset — these are obligations they already have for non-AI systems, recontextualised for AVT. The work is mostly extending existing processes rather than building new ones. (~30% of the catalogue.)

3. **Clinical safety officers** want the **AI-Mediated Workflow** subset — these are the metrics that test how clinicians actually use the system, where the highest-leverage behaviour-change interventions sit. (~10-15%.)

4. **Procurement officers** want the **Pre-AI** + **Post-AI** subsets — the infrastructure compatibility checks and integration-correctness checks that determine whether the AI can be deployed at all. (~10-15%.)

The AI-Substrate cut **complements but does not replace** the existing cuts:

- **Tier** says how essential a metric is.
- **Layer of Defence** says what role it plays in the assurance architecture (prevention / detection / limitation).
- **AI Substrate** (this page) says where the metric sits relative to the AI itself.
- **Family** says which named construct the metric belongs to.

A metric like TP.SN-5 Hallucination Rate is simultaneously: Tier 1 / Detection layer / AI-Substrate / Clinical Content Fidelity family. Different readers come at it from different angles.

### Status and future

**v5.5.3 status:** Option 2 (derived classification at build time) is live. Cross-cut pages live at `by-ai-substrate/` for each of the five classes. CSV / JSON downloads carry an `ai_substrate` field. 0 metrics classified as `disputed`; the override list in `parse._AI_SUBSTRATE_OVERRIDES` handles the genuine edge cases (training-data metrics, downstream outcome metrics, system-availability infrastructure, governance-of-the-AI-stack metrics).

**Future structural promotion (Option 1) remains open** if the cut becomes contractually load-bearing — e.g. if procurement teams start citing "AI-Substrate metrics" as a procurement gate. The decision criterion would be: do readers want audit-enforceable structural commitments per metric, or is the build-time derivation sufficient? For now, Option 2 is sufficient and lower-friction.

**Override hygiene.** Per-metric overrides should be added when a metric's cluster default is wrong; current overrides are documented in `parse._AI_SUBSTRATE_OVERRIDES` with comments explaining each. Adding new overrides should be a small per-release task as the catalogue grows.
