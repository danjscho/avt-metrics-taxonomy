## Failure Pathways

This page traces realistic AVT failure modes step by step, showing **how the taxonomy works in practice** rather than as an abstract enumeration. Two complementary views:

- **Three failure pathways** — parallel archetypes showing how different failure shapes propagate through the pipeline. Each pathway names the pipeline stages traversed and the Tier 1 metrics that are the catches at each stage.
- **One worked timeline** — a single pathway (silent vendor model update) traced day by day from silent change to bounded response. Shows the closed-loop escalation in concrete time terms.

Both views share an underlying claim: **no single metric covers a whole pathway. The taxonomy is a net, not a filter.** The catches happen at multiple points; whether the failure is bounded depends on whether the catches actually fire and whether they trigger each other.

This page complements [Layers of Defence](layers-of-defence.md) — that page names the prevention / detection / limitation architecture; this page shows what failure looks like *moving through* that architecture.

---

## How failure moves through the pipeline (three archetypes)

Each pathway traces a realistic AVT failure mode step by step. The Tier 1 metrics named at each stage are the catches — the points at which the failure becomes detectable. No single metric covers a whole pathway.

### Pathway I — The hallucination cascade

**Shape:** ASR fabrication → patient safety incident.

**Pipeline stages:** ASR → Summarisation → Human Review → EPR → Detection → Escalation.

**Concrete instance:** a Whisper-style hallucination from a 4-second silence becomes a drug prescribed on a symptom the patient never reported.

**Where the catches sit:**

- **ASR stage.** TP.ASR-12 Hallucination-Under-Noise Rate — pre-deployment gate against hallucination from silence/low-SNR segments. The pre-deployment catch.
- **Summarisation stage.** TP.SN-5 Hallucination Rate — the summariser may compound the ASR error rather than flag it. Detection.
- **Human Review stage.** HL.HF-1 Edit Rate, HL.HF-3a Review-Before-Signing Rate, HL.HF-3b Time-to-Sign Distribution — the clinician is the load-bearing catch here. If review is genuine, the fabricated symptom is queried; if review is rubber-stamping (HL.HF-3b tail-of-very-fast-approvals), the fabrication propagates into the EPR.
- **EPR stage.** TP.WB-1 Write-back Fidelity, TP.WB-3 Field Mapping Accuracy — these don't catch the fabrication itself (the content was correctly captured by the AI); they ensure that when the clinician *does* edit, the correction reaches the EPR cleanly.
- **Detection stage.** GV.SG-3 Performance Degradation Detection Latency — population-level detection fires if hallucination rate drifts up.
- **Escalation stage.** GV.SG-11 Adverse Event / Incident Rate (LFPSE), GV.VT-5 Incident Disclosure Compliance — the formal incident channel once the harm is detected.

**What this pathway tests.** Every layer has a catch, but the *human review* catch is the thinnest — the metric tests that review happened, not whether the clinician spotted the specific fabrication. The pathway only fully closes if the LFPSE step actually fires, which means the harm has been detected after-the-fact.

### Pathway II — The silent write-back failure

**Shape:** content correct, field wrong → interaction warning bypass.

**Pipeline stages:** ASR → Summarisation → Write-back → EPR → Prescribing.

**Concrete instance:** an allergy is correctly transcribed but routed to the free-text field instead of the structured allergy list. No drug interaction warning fires.

**Where the catches sit:**

- **ASR + Summarisation stages.** TP.ASR-1 WER, TP.SN-5 Hallucination Rate, TP.SN-6 Omission Rate — these all *pass* in this pathway. The content is correct; the failure is downstream of capture.
- **Write-back stage.** TP.WB-1 Write-back Fidelity, TP.WB-3 Field Mapping Accuracy — **this is the load-bearing catch**. Field-level routing accuracy is the metric that distinguishes "captured correctly" from "captured to the right place".
- **EPR stage.** TP.WB-8 PRSB Semantic Completeness — the clinical-completeness check that asks "are the mandatory information elements *for this consultation type* present in the right structured locations?" An allergy in a free-text field fails PRSB completeness even though it passes content fidelity.
- **Prescribing stage.** No taxonomy metric fires here directly — the harm is the absence of a CDS warning, which the taxonomy doesn't measure end-to-end. PI.E2E-9 Clinical Decision Equivalence is the closest, but it's Tier 3 (research-grade).

**What this pathway tests.** Field-mapping is the most often-overlooked Tier 1 catch in AVT assurance — readers focus on hallucination/omission and miss the routing failure. The pathway demonstrates that the *integration layer* is as load-bearing as the *generation layer*. Cross-link to the [PRSB Semantic Completeness & Write-back Fidelity family](families.md#prsb-semantic-completeness-and-write-back-fidelity) — that family exists precisely to keep the four write-back catches paired.

### Pathway III — The undisclosed model update

**Shape:** silent vendor change → population accuracy drift.

**Pipeline stages:** Vendor → Telemetry → Workflow → Audit → Governance Action.

**Concrete instance:** a vendor deploys a new model without notification. Accuracy drops 14% on EAL (English-as-additional-language) patients. Without version tracking, the cause is invisible.

**Where the catches sit:**

- **Vendor stage.** GV.VT-1 Model Change Notification Compliance — **the catch that should have fired pre-deployment**. If the vendor honours the notification clause, the failure pathway never starts.
- **Telemetry stage.** GV.SG-1 Model Version Tracking — even when notification fails, version tracking detects the silent change via hash check. The deployer-side fallback for vendor non-compliance.
- **Workflow stage.** HL.HF-1 Edit Rate, TP.SN-5 Hallucination Rate, TP.ASR-4 Demographic-Disaggregated WER — population-level signals that show the impact of the change. Demographic-disaggregated WER is the signal that surfaces the EAL-specific drift; aggregate WER might not.
- **Audit stage.** GV.SG-3 Performance Degradation Detection Latency, GV.SG-9 Safety Performance Indicators with Thresholds (DSCMS) — the formal audit cadence that confirms drift exceeds tolerable thresholds.
- **Governance Action stage.** GV.SG-11 LFPSE Reporting, GV.VT-5 Incident Disclosure Compliance, TP.WB-5 Write-back Rollback Capability — the bounded-response toolkit. Rollback returns the deployment to the prior model version; LFPSE files the regulatory record.

**What this pathway tests.** This is the pathway that the *worked timeline* below traces day by day — see the next section.

---

## The taxonomy in motion (worked timeline: the model update)

A vendor silently updates their foundation model. ASR accuracy degrades 6% overall and 14% on EAL patients. The Tier 1 metrics catch it at six points across 17 days, governing a closed loop from silent change to bounded response.

### Day 0 — Silent update

**What happens.** Vendor deploys new model version without prior deployer notification.

**Catch:** **GV.VT-1 Model Change Notification Compliance** (Limitation layer). The notification clause is breached. This is the *catch that should have fired* — in a well-governed pathway the failure ends here. Because it didn't, the deployer-side fallback chain has to do the work.

### Day 1 — Version detected

**What happens.** Hash check logs the new version; re-evaluation workflow triggered.

**Catch:** **GV.SG-1 Model Version Tracking** (Limitation layer). Per-component versioning at inference time is the deployer-side detection mechanism that doesn't depend on the vendor honouring its notification clause. Version mismatch fires the [GV.SG-2 Model Update Impact Score](#gv-sg-2) workflow.

### Day 3–7 — Edit rate climbs

**What happens.** 3% rise in edit rate. Within noise but trending upward.

**Catch:** **HL.HF-1 Edit Rate (% Notes Edited)** (Detection layer). Clinicians are the early-warning population — edit rate is the workflow signal that surfaces the impact of the model change before a formal performance audit completes. *Within noise but trending upward* is exactly the right framing — the metric flags the trend, not yet the trigger.

### Day 14 — SPI breach

**What happens.** Review threshold crossed. Hallucination audit advanced.

**Catch:** **GV.SG-9 Safety Performance Indicators with Thresholds (DSCMS)** (Limitation layer). The SPI threshold breach is the formal trigger that escalates from "trend" to "bounded review". The Hallucination audit cadence advances to confirm.

### Day 16 — Audit confirms

**What happens.** 5.2% vs 1.8% baseline hallucination rate. Pause threshold crossed.

**Catch:** **TP.SN-5 Hallucination Rate** (Detection layer). The audit confirms that the detection signal is real — the rise in edit rate corresponds to a measurable rise in hallucination, exceeding the pre-defined pause threshold.

### Day 17 — Pause & file

**What happens.** Automatic pause activated. LFPSE entry filed. Disclosure requested.

**Catch:** **GV.SG-11 Adverse Event / Incident Rate (LFPSE Reporting)** (Limitation layer). The closed-loop response — the deployment is bounded by the rollback capability ([TP.WB-5](#tp-wb-5)), the regulatory record is filed via LFPSE, and disclosure is requested from the vendor through [GV.VT-5 Incident Disclosure Compliance](#gv-vt-5).

### What the timeline demonstrates

- **The closed loop works when the metrics are wired.** Six catches across six steps; each triggers the next. Notification failed on Day 0, but the deployer-side fallback chain (version tracking → edit-rate signal → SPI breach → audit → pause → LFPSE) bounded the response within 17 days.
- **Five of the six catches are Limitation-layer.** This timeline is what a *fully-wired Limitation layer* looks like in practice. The architectural-gap finding in [Layers of Defence](layers-of-defence.md) — that Limitation is the thinnest layer in the catalogue — only fires when the deployer hasn't actually wired these particular metrics. The timeline shows the alternative.
- **Time matters.** A 17-day window from silent change to bounded response is fast by NHS-incident-handling standards but still long enough that some patients see the degraded outputs. The timeline isn't claiming zero harm; it's claiming bounded harm with a documented response.
- **Demographic-disaggregated detection is upstream of aggregate detection.** The 14%-on-EAL signal surfaces faster than the 6%-overall signal because it's stratified. The pathway implicitly relies on [TP.ASR-4 Demographic-Disaggregated WER](#tp-asr-4) being measured continuously — without disaggregation, the aggregate 6% might fall within noise for longer.

### What's not in this timeline

- **Patient harm.** The pathway shows bounded response, not zero harm. Some patients between Day 0 and Day 17 saw degraded outputs.
- **Inter-deployer correlation.** A single deployer running this loop catches its own deployment. Multi-deployer signal aggregation (per-vendor across NHS) would catch silent changes faster — that's a national-level capability the catalogue describes but doesn't yet operationalise.
- **The Limitation layer for non-AI failure modes.** This pathway is AI-specific (silent model change). Other failure modes (e.g. EPR integration breakage, hardware failure, network outage) trigger different Limitation catches not shown here.

---

## How to use this page

When designing or reviewing an AVT assurance plan:

1. **Walk a pathway.** Pick one of the three archetypes. Trace it through your own deployment. At each stage, name the metric you'd actually rely on. If the answer is "we don't measure that", you've found a gap.
2. **Test the closed loop.** For the timeline pathway specifically, ask: if Day 0 happened in your deployment today, would you reach Day 17 in 17 days, or would the loop break somewhere? Common breaks: vendor doesn't expose hash for version tracking; edit-rate isn't measured continuously; no SPI threshold defined; no rollback capability.
3. **Stratify before aggregating.** The pathway makes visible that demographic-disaggregated detection is faster than aggregate detection. If you're only measuring aggregate WER, you're choosing a slower loop.
4. **The metrics are the catches; the wiring is the work.** Having the metrics in the catalogue is necessary but not sufficient. The pathway closes only when each metric *triggers* the next — that's a deployer-side wiring task the taxonomy can't do for you.

This page is a documentation artefact, not a structural cut. It complements [Layers of Defence](layers-of-defence.md) (architectural framing) and [Families](families.md) (construct framing) by providing **scenario framing** — what failure actually looks like moving through the architecture.
