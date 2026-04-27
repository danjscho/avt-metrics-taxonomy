# AVT Metrics Taxonomy - Change Plan v1

Mapping the research findings from the exhaustiveness review onto specific, located changes in `avt-metrics-taxonomy.md`. The plan is organised by change type so you can approve or reject each block independently before I execute anything.

## Summary of proposed changes

- **~38 new metrics** (conservative count, assuming you accept all architectural decisions below)
- **~12 existing metrics reframed or regrouped** under parent constructs
- **~15 underspecification flags** added to existing metric entries
- **3 new sections** proposed (Clinical Coding expansion, NHS Compliance cluster, Longitudinal Drift & Contamination)
- **1 new Part** proposed (Part D.5 or extended Part E for NHS Compliance)
- Taxonomy total would move from **151 → ~189** metrics

The expansion is material but proportionate - roughly +25%, concentrated in the three areas the research identified as the largest gaps (clinical coding, NHS-specific compliance, longitudinal drift). Most of the change is additive; very little existing content needs rewriting.

---

## Architectural decisions needed before execution

These are the five decisions that determine the final shape. I'd suggest we work through these before I touch the file.

**Decision 1 - NHS Compliance cluster: new section or distributed?**
The Jan–Mar 2026 NHS guidance suite (AVT Supplier Registry, DTAC v2, IG guidance, CIO/CCIO guidance) generates ~8 trackable compliance metrics. Options:
- **(a)** New dedicated section `NHS Compliance & Regulatory Tracking` under Part E (cleanest, makes the NHS-specific requirements visually prominent for NHS audiences)
- **(b)** Distribute across existing Privacy & Data Governance, Vendor Transparency, and Safety & Governance sections (less disruption, but buries the compliance story)
- **My recommendation:** (a). NHS audiences need to see the compliance requirements as a distinct cluster, not scattered.

**Decision 2 - Clinical Coding expansion: extend existing section or restructure?**
Current Clinical Coding section has 4 metrics. Research identified 8 additional metrics in this area, making it the largest single gap. Options:
- **(a)** Extend existing section to ~12 metrics (keeps structure, section becomes larger)
- **(b)** Split into subsections: `Coding Accuracy` (SNOMED, ICD-10/11, OPCS-4, dm+d, code hallucination) vs `Coding Governance` (upcoding, E/M shift, revenue equity)
- **My recommendation:** (b). The accuracy vs governance distinction mirrors how CSOs and ICB teams think about coding risk and maps cleanly onto the responsible-actor axis.

**Decision 3 - Hallucination subtype taxonomy: embed or new metric?**
Research recommends the CREOLA-derived subtype taxonomy (fabrication, context conflation, incorrect negation, speculation) be made explicit. Options:
- **(a)** Embed as a reporting requirement in the existing `Hallucination Rate` entry (adds ~10 lines to that entry)
- **(b)** Create a new metric `Hallucination Subtype Distribution` as a Tier 2 companion metric
- **My recommendation:** both. Embed the requirement in Hallucination Rate (so the subtype reporting is mandatory at Tier 1) AND add the distribution as a distinct Tier 2 metric (because tracking the *distribution shift* over time is diagnostically valuable and distinct from the rate itself).

**Decision 4 - Patient outcomes: how much weight?**
Coiera & Fraile-Navarro's critique is the biggest conceptual gap. The file has `Clinical Decision Equivalence` (Tier 3) and `Therapeutic Relationship Impact` (Tier 3). Options:
- **(a)** Add 2–3 more distal outcome metrics under Patient Experience and let the Meta-evaluation section carry the framing
- **(b)** Create a new Part G `Patient & Clinical Outcomes` with 5–6 metrics, explicitly structured as the distal counterweight to the proximal-heavy taxonomy
- **My recommendation:** (a) for now. The taxonomy is honest about being proximal-weighted; creating a whole Part G risks implying we have measurable distal metrics we don't. Better to add the 2–3 metrics we can actually define and lean on Meta-evaluation's `Proximal vs Distal` entry to carry the structural critique.

**Decision 5 - Environmental / sustainability: include or defer?**
Research identified energy, carbon, and water metrics. These are Tier 3, not yet NHS-mandated, but EU AI Act adjacency is rising. Options:
- **(a)** Add as a small new subsection (3 metrics) under Operational
- **(b)** Defer to a v2 of the taxonomy with a one-line acknowledgement in Meta-evaluation
- **My recommendation:** (a). Three metrics is a small investment, NHS Net Zero is a real commitment, and it future-proofs the taxonomy against EU AI Act cascading.

---

## Part A - New metrics to add, by location

### A.1 Audio Capture & Environment (currently 9 metrics → +0, no changes)

Already well-covered. No additions.

### A.2 ASR / Transcription (currently 12 → +2)

- **Speaker Role Identification F1 / cpHEWER** (Tier 2, Vendor). Distinct from DER because it identifies clinical roles (clinician / patient / family / interpreter) rather than just two-speaker diarisation. Source: mpathic.ai ASR benchmark (2025). Insert after Demographic-Disaggregated WER.
- **Error Transmission Rate** (Tier 2, Vendor). The proportion of ASR errors that propagate into the final note. 19.5% in OHSU five-platform study (Anderson et al., Mayo Clinic Proceedings Digital Health, 2025). Pipeline-level compound metric. Insert after ASR Confidence Calibration - or consider moving to Part B (Partial-Pipeline) since it spans ASR + summarisation.

### A.3 Diarisation (currently 4 → +3)

- **Code-Switching Detection Rate** (Tier 2, Vendor). Critical for NHS consultations involving bilingual patients, interpreters, or EAL populations switching between languages mid-utterance. Source: ACL SigDial 2023; IJCAI-22 multi-party dialogue survey.
- **Addressee Recognition Accuracy** (Tier 3, Vendor). In multi-party consultations, who is the speaker addressing? Matters for attribution of questions vs statements. Research-grade.
- **Turn-Taking Accuracy in Overlapping Speech** (Tier 3, Vendor). Distinct from Speaker Overlap Rate (which is about input conditions) - this measures whether the system correctly handles overlap. Research-grade.

### A.4 Summarisation / NLP (currently 20 → +3)

- **Hallucination Subtype Distribution** (Tier 2, Deployer). Per the research, distribution of errors across {fabrication, context conflation, incorrect negation, speculation}. Complements the aggregate Hallucination Rate. Insert after Hallucination Rate.
- **Context Conflation Rate** (Tier 2, Deployer/Vendor). Content misattributed between speakers or between parts of the conversation - the 43% CREOLA fabrication subtype that the current `Hallucination Rate` entry doesn't separate out. Note: if Decision 3 is (a)-only, this becomes absorbed into Hallucination Rate as a required subcategory.
- **Medication Event Classification Accuracy** (Tier 2, Vendor). Distinct from general medication extraction - classifies each medication mention as start/stop/increase/decrease/continue. F1 0.92+ in n2c2 shared tasks. High clinical safety value.

### A.5 Clinical Coding (currently 4 → +8, restructured per Decision 2)

Assuming Decision 2 = (b), new structure:

**Coding Accuracy subsection:**
- Keep: **SNOMED Code Accuracy** (existing)
- Add: **ICD-10/ICD-11 Coding Precision at Full Specificity** (Tier 2, Vendor/Deployer). Per Hybrid-Code v2 evaluations showing drop from 93% at 3-character to 82% at full specificity.
- Add: **OPCS-4 Procedure Coding Accuracy** (Tier 2, Vendor/Deployer). NHS-specific, no published AI benchmarks. Flag as critical gap.
- Add: **dm+d Medication Coding Accuracy** (Tier 1, Vendor/Deployer). NHS-specific, directly safety-critical. Proposed as Tier 1 because it's the NHS medication standard and errors are direct prescribing risk.
- Add: **Code Hallucination Rate** (Tier 1, Vendor). Rate of AI-generated codes that do not exist in the target code set. Distinct from general hallucination. Hybrid-Code framework.
- Keep: **Code Specificity Index** (existing)
- Keep: **Code Suggestion Latency** (existing)

**Coding Governance subsection:**
- Keep: **Coding Inflation Detection** (existing, move here)
- Add: **E/M Level Shift Monitoring** (Tier 2, Regional ICB). Per *npj Digital Medicine* policy brief: documented diagnoses rose from 3.0 to 4.1 per encounter, HCC capture +14%, wRVU +11%. NHS variant would track QOF/LTC register composition shift.
- Add: **Coding Equity Across Demographics** (Tier 2, Regional ICB). Whether coding improvements are equitably distributed or systematically concentrated. Extends existing equity framing.

### A.6 EPR Write-back (currently 5 → +2)

- **FHIR R4 Resource Conformance Rate** (Tier 2, Vendor). Validated structural conformance against FHIR R4 profiles. Referenced in NHS England's AVT guidance but without a standard measurement protocol. ADS/Harvard SPIE 2025 achieved 95% data field retention via FHIR.
- **FHIR Terminology Binding Validation** (Tier 2, Vendor). Whether coded values correctly bind to SNOMED CT / dm+d via FHIR terminology services. Insert after Field Mapping Accuracy.

*Note on openEHR:* deliberately not adding openEHR archetype conformance as a separate metric - too niche for the audience. Can add a footnote to FHIR Conformance noting it if you disagree.

### A.7 Human Factors & Workflow (currently 15 → +3)

- **AI-Off Performance Test** (Tier 3, Deployer). Clinical documentation quality when AVT is temporarily unavailable. Concrete operationalisation of the existing (Tier 3) `Clinical Documentation Skill Attenuation` metric. Lancet Gastroenterology 2025 - endoscopist ADR fell from 28.4% to 22.4% when AI removed - the canonical real-world deskilling evidence.
- **Work-as-Imagined vs Work-as-Done Gap** (Tier 3, Deployer). From Safety-II / FRAM literature. Subsumes off-label use, workarounds, and adaptive creativity. Assessed via ethnographic observation and workflow analysis.
- **Verification Burden Measurement** (Tier 2, Deployer). Additional cognitive workload of checking AI against reality. Distinct from Cognitive Load (which is general). SEIPS-based; operationalised via TimeCat time-motion in the GOSH pilot.

### A.8 Patient Experience (currently 6 → +2, per Decision 4 = (a))

- **Full Attentiveness Rate** (Tier 2, Deployer). Proportion of consultation time clinician is fully attentive to patient. Stults et al. reported increase from 57.9% to 93.0% with ambient AI. Objective (eye-tracking, observation) or subjective (patient-reported).
- **Patient Dissent/Objection Rate** (Tier 1, Deployer). Distinct from Opt-Out Rate - dissent is an active objection during or after the consultation rather than a pre-consultation opt-out. NHSE IG guidance (March 2026) requires this be recorded and respected.

### A.9 Fairness & Equity (currently 5 → +1)

- **Stigmatising Language Replication Rate** (Tier 2, Deployer/Academic). Per Barcelona et al. (JAMA Network Open 2025): Black patients had 2.54× odds of negative descriptors in clinical documentation. AVT trained on such notes amplifies this. Extends existing `Cultural & Linguistic Appropriateness` (which is conceptually adjacent but doesn't explicitly address training data bias replication).

### A.10 Safety & Governance (currently 13 → +3)

- **AI-Generated Data Contamination / Model Autophagy Monitoring** (Tier 3, National Body). medRxiv 2026: when AI-generated clinical content enters training pipelines, vocabulary reduced 98.9% by generation 4. National-tier responsibility.
- **Performance Degradation Detection Latency** (Tier 2, Regional ICB / Vendor). Time between onset of degradation and detection. Operational metric that complements Model Update Impact Score.
- **Model Retraining Trigger Thresholds** (Tier 2, Vendor). Pre-defined statistical and clinical criteria that trigger recalibration. Required by FDA PCCP guidance.

### A.11 Security & Adversarial Robustness (currently 9 → +2)

- **Cross-Patient Information Leakage Rate** (Tier 1, Vendor). Rate at which content from one patient's encounter contaminates another's generated note. Distinct from general PII leakage - can occur through context window contamination. MIT Jameel Clinic (2026). Should be Tier 1 given the severity.
- **Membership Inference Attack AUC** (Tier 3, Vendor/Academic). Adversarial privacy testing metric. Undefended LLMs show AUC 0.96, collapsing to 0.505 with differential privacy (IEEE S&P 2023). Research-tier.

### A.12 Privacy & Data Governance (currently 6 → +3)

- **Data Retention Deletion Verification** (Tier 1, Deployer). Stronger than the existing `Audio Retention Compliance` - requires verified deletion of audio and transcripts after summary sign-off, not just policy compliance. Directly mandated by NHSE IG guidance March 2026.
- **DPIA Completion per Deployment** (Tier 1, Deployer). Tracked as compliance metric. Currently implicit in governance but not a standalone metric.
- **Consent Recording Completeness** (Tier 1, Deployer). Proportion of encounters with captured recording consent before AVT activation. GOSH pilot: 92% baseline. Distinct from existing `Consent Verification Accuracy` which addresses patient understanding rather than consent event capture.

### A.13 NEW SECTION - NHS Compliance & Regulatory Tracking (per Decision 1 = (a))

Inserted as a new section in Part E between `Privacy & Data Governance` and `Operational`. All metrics Tier 1 by default because they represent compliance obligations, not recommendations. All metrics have Deployer as primary responsible actor.

- **AVT Supplier Registry Listing Verification** - binary check that the supplier is on NHSE's AVT Supplier Registry before procurement.
- **DTAC v2.0 Completion Status** - structured completion check against the February 2026 DTAC update.
- **Verbal Notification Compliance Rate** - per-consultation check that clinicians verbally inform patients at session start.
- **AI-Generated Content Labelling Compliance** - verification of the mandatory suffix (e.g. "Audio Dictation (24771000000105)") on AI-generated records.
- **ICB Engagement / Approval Tracking** - evidence of ICB digital team consultation prior to deployment per NHS CIO priority notification.
- **Clinical Safety Case Completeness Score** - DCB0129/0160 compliance check. The 2025 FOI study revealed widespread non-compliance; this makes the compliance gap visible.
- **Patient Information Notice Currency** - whether the practice's patient-facing information about AVT use is current with NHSE guidance.
- **Information Commissioner Notification (where applicable)** - for deployments processing special category data at scale.

### A.14 NEW SECTION - Longitudinal Drift & Contamination

Small new section (3 metrics) under Part E, between Safety & Governance and Security. Alternatively, these can be distributed into Safety & Governance. Content duplicates A.10 above - pick one location.

### A.15 Operational (currently 6 → +3, per Decision 5 = (a))

New subsection **Environmental Sustainability:**
- **Energy Consumption per Note** (Tier 3, Vendor). Range 0.42 Wh to 29 Wh per query depending on complexity. Jegham et al. (arXiv 2505.09598, 2025).
- **Carbon Emissions per Inference** (Tier 3, Vendor). gCO2e, hosting-location dependent.
- **Water Consumption per Query** (Tier 3, Vendor). Data centre cooling footprint.

### A.16 Patient Experience / Outcomes (per Decision 4 = (a))

- **Patient Comprehension of AI-Generated Summaries** (Tier 3, Deployer/Academic). Particularly relevant for after-visit summaries via NHS App.
- **Patient-Reported Outcome Linkage** (Tier 3, Academic/National Body). Linking AVT deployment to PROMs over time. Coiera's distal critique in operational form.

### A.17 Meta-evaluation (currently 5 → +2)

- **Automated-Human Metric Concordance** (Tier 3, Academic). Whether automated metrics (VeriFact, LLM-as-Judge, edit rate) agree with structured human review at the encounter level. Required by TRIPOD-LLM.
- **Benchmark Dataset Currency** (Tier 3, National Body). Whether the benchmarks used for pre-deployment evaluation reflect current clinical practice, patient populations, and language use. Directly addresses the "only two public datasets" infrastructure gap.

---

## Part B - Existing metrics to reframe or regroup

These are the consolidation recommendations from the research. None of them delete metrics; they add framing that makes the relationships explicit.

### B.1 Hallucination family - add parent construct framing

In Summarisation / NLP, immediately before `Hallucination Rate`, add a short framing paragraph (~4 lines) introducing "Clinical Content Fidelity" as the parent construct family encompassing:
- Hallucination Rate (aggregate)
- Hallucination Subtype Distribution (new, A.4)
- Omission Rate
- Negation Handling Accuracy
- Uncertainty Marker Preservation
- Quantifier Preservation
- Temporal Accuracy
- Context Conflation Rate (new, A.4)

Update the `Hallucination Rate` entry's `Formal Definition` to require subtype reporting (fabrication / context conflation / incorrect negation / speculation / transcription-derived). This is a ~6-line addition to one entry.

### B.2 Edit metric family - add tiered framing

In Human Factors & Workflow, immediately before `Edit Rate (% Notes Edited)`, add a short framing paragraph introducing "Post-Generation Correction" as a tiered family:
- Edit Rate - cheapest, system-level
- Edit Type Classification - diagnostic
- Edit Location Distribution - structural diagnostic
- Edit-Pattern Monitoring at Scale - governance
- Time-to-Sign - effort proxy

No new metrics needed; this is a framing block only.

### B.3 Medical WER / M-WER / CK-ER - consolidate framing

In ASR / Transcription, add a 3-line framing note before `Word Error Rate` explaining that WER, M-WER, and CK-ER are three tiers of the same underlying construct (Clinical Transcription Accuracy):
- Raw WER (technical benchmarking)
- M-WER (clinical relevance weighting)
- CK-ER (safety-critical keyword binary)

All three should be reported together. No deletions.

### B.4 Reference-based text similarity family

In Summarisation / NLP, add a 2-line framing before `ROUGE Scores` grouping ROUGE + BERTScore as "Reference-Based Text Similarity Metrics" and flagging that this family is insufficient for clinical quality assessment and must always be paired with human or LLM-as-Judge evaluation. The existing entries already make this point; the framing makes it collective.

### B.5 Automation bias / complacency / over-reliance

In Human Factors & Workflow, add a short framing note introducing "Over-Reliance Risk" as the parent construct covering:
- Automation Bias Detection (cognitive bias - decision-making)
- Edit Rate complacency signal (attentional - monitoring vigilance)
- Trust Halo Decay Rate
- Cognitive Offloading Rate
- Clinical Documentation Skill Attenuation
- AI-Off Performance Test (new, A.7)

Parasuraman & Manzey (2010) provides the canonical distinction between bias and complacency - both are retained, framed as distinct facets of the parent construct.

### B.6 Documentation workload family

In Operational, add a brief framing note grouping Documentation Time per Consultation with variants (pyjama time, after-hours EHR use). Current entry only explicitly tracks one - worth flagging that the GOSH 51.7% documentation reduction was measured at individual clinician level, not aggregate. Optional new metric: **After-Hours EHR Use Delta** (Tier 2).

---

## Part C - Underspecification flags to add to existing entries

Each of these is a small addition to the `Limitations` or a new `Underspecification` subsection in the existing metric entry. They make the current definitional weaknesses visible without deleting anything.

1. **Hallucination Rate** - add flag noting definition varies 1–3% (deployed) to 43–67% (benchmarks), with no standardised operational definition. Recommend CREOLA subtype taxonomy as interim standard.
2. **Omission Rate** - add flag: automated detection at scale unsolved, only two public reference datasets (ACI Bench, PriMock).
3. **Trust Halo Decay Rate** - flag: no validated measurement approach in clinical AI context; boundary with automation bias not empirically established.
4. **Off-Label Use Detection Rate** - flag: no established methodology; use-case taxonomy defining intended vs off-label boundaries does not exist; requires vendor collaboration to define validated use envelope.
5. **Trust Calibration Survey** - flag: TIAS/HATAS/AITI-H exist but none validated for ambient scribe contexts. Dokkyo Medical 2024: "no accurate objective measures" for clinical AI trust calibration.
6. **Automation Bias Detection (Error Injection)** - flag: no standardised audit protocol for production AVT; no established acceptable threshold rate; one study found 7% automation bias rate in pathology but no clinical documentation benchmark. Active RCT NCT07328815.
7. **Cognitive Load Assessment** - flag: no AVT-specific subscale selection, no standard measurement timing, no documentation-specific instrument. NASA-TLX ICC 0.71–0.81 individual, lower group.
8. **ROUGE Scores** - flag: ROUGE-L max Kendall-Tau 0.080 with human judgments in clinical diagnosis generation; "catastrophic failure modes" with negative Spearman in some medical contexts.
9. **BERTScore** - flag: correlates poorly with clinician quality judgements despite semantic awareness.
10. **Diarisation Error Rate (DER)** - flag: no clinical-specific benchmarks exist; no validated link between DER and downstream documentation quality.
11. **Demographic-Disaggregated WER** - flag: no standardised accent category taxonomy; FAccT 2024 identified current race/geography/education categorisations as sociolinguistically flawed. Proposed NHS taxonomy should include British regional, South Asian English varieties, West African, Caribbean, Eastern European English at minimum.
12. **LLM-as-a-Judge (PDSQI-9 Proxy)** - flag known biases: position bias, verbosity bias, self-enhancement bias. One Rwanda study: LLM judges correlate better with non-expert than expert annotators.
13. **Edit Rate** - flag: no standardised threshold values; no consensus on acceptable rate; DeepScribe's <10% word edit threshold is vendor-specific.
14. **Clinically significant WER** (referenced in M-WER entry) - flag: no consensus definition of "clinically significant"; Fu et al. (JAMIA 2024) 43-class error taxonomy is a starting point but lacks severity weights.
15. **Severity-weighted error rate** (referenced in M-WER entry) - flag: no standard weighting scheme; ICD hierarchy distance (Scientific Reports 2023) and AHRQ harm scales are candidates but neither validated for documentation errors.

Also add a new Meta-evaluation entry or subsection: **Cross-Cutting Resource Gap - Public Benchmark Availability.** Only ACI Bench and PriMock are public. Inter-rater reliability is rarely reported. This undermines the operationalisation of nearly every metric in the taxonomy. Worth stating explicitly because it justifies why so many metrics carry Tier 3 status.

---

## Part D - Housekeeping updates

These are mechanical changes that flow from the additions above.

### D.1 Counts and headline numbers

Update the opening:
- **"151 metrics across 18 groups"** → **"~189 metrics across 20 groups"** (exact number pending architectural decisions)
- Tier breakdown: recalculate
- Maturity breakdown: most new additions will be Proposed/Novel or Emerging
- Priority Tier summary counts: need recalc after decisions

### D.2 Contents list

- Add new section entries per Decisions 1, 2, 5
- Update metric counts per section

### D.3 Tier 1 Quick Reference

New Tier 1 entries to add to the quick reference:
- dm+d Medication Coding Accuracy (Vendor, Deployer)
- Code Hallucination Rate (Vendor)
- Cross-Patient Information Leakage Rate (Vendor)
- Patient Dissent/Objection Rate (Deployer)
- Data Retention Deletion Verification (Deployer)
- DPIA Completion per Deployment (Deployer)
- Consent Recording Completeness (Deployer)
- All 8 NHS Compliance metrics if Decision 1 = (a)

That's ~15 additions to the Tier 1 Quick Reference, bringing it from 33 to ~48. Worth checking whether 48 is still "minimum viable" or whether some NHS Compliance metrics should drop to Tier 2.

### D.4 "How to Use" section

Minor addition to the "Adapting to Local Context" block: add an example noting that NHS Compliance metrics are non-negotiable for NHS deployment regardless of local context (they are compliance obligations, not recommendations).

Also update the Responsible Actors section to acknowledge that many NHS Compliance metrics have the Deployer as sole responsible actor (vendor is not involved in e.g. ICB engagement tracking).

### D.5 New framing note in introduction

Add a ~5-line paragraph to the introduction acknowledging:
- The taxonomy is proximal-weighted by necessity (tooling for distal measurement does not yet exist)
- This is a direct response to Coiera & Fraile-Navarro's critique
- The Meta-evaluation section's `Proximal vs Distal Outcome Distinction` metric is the structural counterweight
- Tier 3 metrics addressing distal outcomes (Clinical Decision Equivalence, Chilling Effect, etc.) are intentionally preserved despite not being operationally measurable today, because they mark where national evaluation programmes should invest

---

## Implementation sequence

Suggested order once architectural decisions are confirmed:

1. **Framing additions first** (Part B) - these are small, low-risk, and establish the parent constructs that subsequent additions slot into
2. **Underspecification flags** (Part C) - small edits to existing entries, improve honesty of the taxonomy without changing structure
3. **New sections** (A.13 NHS Compliance, A.14 Longitudinal Drift, A.15 Environmental subsection) - largest single change, needs the architectural decisions
4. **New metrics in existing sections** (A.1–A.12, A.16–A.17) - additive, lowest risk after structural decisions are made
5. **Housekeeping** (Part D) - counts, contents, Tier 1 Quick Reference, introduction paragraph - must come last because they depend on the final shape

Rough effort estimate: with decisions confirmed, this is probably a 2–3 hour edit pass. The file will grow from ~2,800 lines to ~3,400 lines.

---

## What I need from you before executing

1. Decisions 1–5 above (the architectural choices)
2. Confirmation on whether any of the "+1" additions should be dropped as out-of-scope for this iteration
3. Whether to preserve the current maturity breakdown ("Proposed / Novel: 76") or recalibrate - most additions will be Proposed/Novel, pushing that number to ~110 which may start to feel top-heavy and warrant a note about taxonomy maturity
4. Whether the Tier 1 count expanding from 33 → ~48 is acceptable or whether we should re-tier some items
5. Any research findings you want to explicitly reject or defer (the research was deliberately expansive; not everything needs to land in v2)

Once these are settled, I can work through the file in the order above and produce a diff-style summary of what actually changed so you can review before replacing the master copy.
