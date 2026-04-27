# RSET Coverage Audit - Nuffield Trust AVT (Feb 2026)

**Date:** 2026-04-18
**Taxonomy baseline:** v3.1 (214 metrics, 20 groups)
**Sources reviewed:**
- Nuffield Trust RSET AVT Taxonomy PDF (Feb 2026) - the 50-item product-capability taxonomy (10 essential + 40 additional)
- RSET AVT Phase 1 slide deck (Jan 2026) - scoping review, logic model, metric framework

## What the RSET taxonomy is (and isn't)

The RSET taxonomy is a **product-capability checklist** (does the product *do* X), not a metrics taxonomy (how well does X *work*). These are complementary. The valuable cross-check is:

- **Coverage direction 1 (RSET → ours):** For every RSET capability, does our taxonomy have a metric that would *assure* that capability operates safely and correctly?
- **Coverage direction 2 (slide deck → ours):** The scoping-review metric categories (pp. 13–17 of the deck) are the evaluation-science framing - do our metrics align with what the field is actually measuring?

## Direction 1 - RSET 50-item capability → our metric coverage

### Essential (10 items - minimum to *be* an AVT product)

| # | RSET item | Our coverage |
|---|---|---|
| 1 | Captures audio between user and patient | TP.AC-1 SNR · TP.AC-2 VAD · TP.AC-5 Microphone & Hardware Validation · **covered** |
| 2 | Produces substantially accurate transcript | TP.ASR-1 WER · TP.ASR-2 M-WER · TP.ASR-3 CK-ER · TP.ASR-12 Hallucination-Under-Noise · **covered** |
| 3 | Transcript can be reviewed by user | **partial gap** - we assume review is possible but don't measure review ergonomics. See Gap-RSET-A below. |
| 4 | Able to identify UK-relevant medical terms | TP.ASR-3 CK-ER · TP.ASR-9 OOV Rate · TP.CC-2 SNOMED CT Concept Mapping · **covered** |
| 5 | Able to distinguish between user and patient/others | TP.DI-1 DER · TP.DI-2 Speaker Attribution · TP.DI-5 Speaker Role ID · TP.AC-4 Bystander Voice Detection · **covered** |
| 6 | Consultation summary produced and presented back | TP.SN-1..24 (whole summarisation group) · **covered** |
| 7 | Summary outputs can be edited by user | HL.HF-1 Edit Rate · HL.HF-2 Edit Type · HL.HF-7 Edit Location · **covered** |
| 8 | Summary outputs can be entered into patient record systems | TP.WB-1..8 (Write-back group) · **covered** |
| 9 | Data is processed securely | GV.SC-1..11 · GV.PD-* · **covered** |
| 10 | Compliant with data protection and medical device regulations | GV.CR-6 Clinical Safety Case · GV.CR-7 DPIA · GV.PD-* · Standards Mapping (MHRA, DCB0129/0160, UK GDPR) · **covered** |

**Essential coverage: 9/10 direct, 1/10 partial.**

### Additional (40 items - capability differentiators)

Mapping the less-obvious ones; straightforward UX capabilities (e.g. "runs on a phone app") deliberately out of scope for a metrics taxonomy.

| # | RSET item | Our coverage |
|---|---|---|
| 11 | Transcript strips out irrelevant information | TP.SN-11 MEDIC Cross-Examination · TP.SN-6 Omission Rate (inverse) · **partial** - no dedicated "relevance/signal-preservation" metric. Gap-RSET-B. |
| 12 | Distinct people tagged in transcript | TP.DI-2 Speaker Attribution · TP.DI-5 Speaker Role ID · **covered** |
| 13 | Transcript can be edited by user | HL.HF-* (edit metrics apply to transcript too if editable) · **partial** - our edit metrics target the summary, not the transcript. Gap-RSET-C. |
| 14 | Transcript editing function can be turned off | **gap** - a configurability metric. Not our concern, arguably. See Gap-RSET-D. |
| 15 | Summary outputs pre-formatted by prompt engineering | TP.SN-14 Template Modification Underspecification · **covered** (obliquely) |
| 16 | Summary outputs editable by voice/AI-supported chat | **gap** - we don't cover AI-mediated editing modalities. Gap-RSET-E. |
| 17 | Summary outputs editable by templating | TP.SN-14 (above) · **covered** |
| 18 | Summary outputs integrated directly into EHR | TP.WB-1..8 · **covered** |
| 19 | Summary includes suggested clinical codes | TP.CC-1..12 · **covered** |
| 20 | User is able to review clinical codes | **partial gap** - we assume review happens but don't have a review-ergonomics metric for codes. Folds into Gap-RSET-A. |
| 21 | Auto-populates referral letters | **partial** - TP.WB-* covers structured write-back; letter generation as a discrete output has no dedicated metric. Gap-RSET-F. |
| 22 | Creates patient-facing summaries (e.g. letters) | IO.PX-8 Patient Comprehension of AI-Generated Summaries · **covered** |
| 23 | Incorporates patient information from beyond the consultation | **gap** - contextual data fusion from prior EHR content. Gap-RSET-G. |
| 24 | Summary can be created some time in the future | **gap** - latency-to-output is TP.ASR-7 (real-time factor) + PI.E2E-10 (full-pipeline latency) but deferred / asynchronous summarisation as a workflow isn't distinctly measured. Minor - not a content gap. |
| 25 | Summary includes list of suggested tasks | **gap** - "task extraction" as a distinct output is not covered. Gap-RSET-H. |
| 26 | AI tech trained on diverse data | GV.PD-7 Training Data Inclusion Status · GV.VT-3 Benchmark & Evaluation Data Accessibility · **covered** |
| 27 | Transcripts accurate - age | TP.ASR-4 Demographic-Disaggregated WER · IO.FE-* · **covered** |
| 28 | Transcripts accurate - gender | TP.ASR-4 · IO.FE-* · **covered** |
| 29 | Transcripts accurate - native-anglophone accents | TP.ASR-4 · IO.FE-2 Accent Taxonomy Standardisation · **covered** |
| 30 | Transcripts accurate - English-as-second-language accents | TP.ASR-4 · IO.FE-2 · **covered** |
| 31 | Transcripts accurate - specific disorders/disabilities | TP.ASR-4 · IO.FE-7 Health Literacy Performance Variation (loose fit) · **partial** - disability-specific sub-populations (dysarthria, aphasia, hearing-impaired speech) not called out explicitly. Gap-RSET-I. |
| 32 | Captures third-party translated consultations | **gap** - translator/interpreter-mediated consultations as a distinct evaluation context not covered. Gap-RSET-J. |
| 33 | Patient-facing summaries customisable for specific needs | IO.PX-4 Cultural & Linguistic Appropriateness · IO.PX-8 · **covered** |
| 34 | Different subscription/service levels | out of scope - commercial, not assurance |
| 35 | Patient account management functions | out of scope |
| 36 | Captures patient consent status | GV.PD-8 Consent Verification Accuracy · GV.CR-1 Dissent Recording · GV.CR-2 Verbal Notification · **covered** |
| 37 | Incorporates patient information through EHR integration | overlaps Gap-RSET-G (RSET #23) |
| 38 | Continues to function if internet drops | GV.OP-5 System Availability · HL.HF-19 AI-Off Performance Test · **partial** - offline-mode integrity as a distinct property not called out. Gap-RSET-K. |
| 39 | Works with non face-to-face interactions | TP.AC-* covers audio quality variance; remote-consultation context-drift not distinctly measured. Minor gap - folds into TP.AC-3 Acoustic Environment Profiling. |
| 40 | Runs on desktop/laptop | out of scope |
| 41 | Runs in web browser | out of scope |
| 42 | Runs on phone app | out of scope |
| 43 | Audio is stored by product | GV.PD-1 Audio Retention Compliance · GV.PD-2 Audio Time-to-Deletion · **covered** |
| 44 | Transcript is stored | GV.PD-3 Transcript Retention Compliance · **covered** |
| 45 | Summary is stored | **partial** - summaries typically land in EHR (TP.WB-*); if retained separately, policy is ambiguous. Minor. |
| 46 | User edit information is stored | GV.VT-4 Audit Trail Completeness · **covered** |
| 47 | Informs user if technical/accuracy problems exist | GV.SG-3 Performance Degradation Detection Latency · GV.SG-9 SPI with Thresholds · TP.ASR-10 ASR Confidence Calibration · TP.ASR-11 ASR Confidence Exposure · **covered** |
| 48 | Has features to prevent/capture misuse | GV.SG-10 Off-Label Use Detection Rate · GV.SC-10 Clinician Identity Authentication · **covered** |
| 49 | Information from interaction used to train AI | GV.PD-7 Training Data Inclusion Status · GV.VT-1 Model Change Notification · **covered** |
| 50 | AI tech is regularly updated and improved | GV.SG-1 Model Version Tracking · GV.SG-2 Model Update Impact · GV.VT-1 Model Change Notification · **covered** |

**Additional coverage summary (of 32 in-scope items):** 22 covered · 8 partial · 2 gap. 8 items deliberately out of scope (commercial/platform/runtime properties not meaningful as assurance metrics).

## Direction 2 - scoping-review metric categories (slide deck pp. 13–17)

The deck groups measures the scoping-review literature used into staff / patient / provider-system buckets. Our coverage:

### Staff metrics (deck p. 14)

| Literature metric | Our equivalent |
|---|---|
| Documentation burden (time in notes, turnaround, after-hours) | GV.OP-1 Documentation Time per Consultation · GV.OP-2 Pyjama Time · GV.OP-3 Note Turnaround Time · GV.OP-4 Documentation Workload Composite · **covered** |
| Clinician time saved | GV.OP-1 (differential pre/post) · **covered** |
| Subjective accuracy / usefulness | HL.HF-8 Trust Calibration Survey · **covered** |
| Wellbeing / burnout / cognitive burden | HL.HF-10 Cognitive Load Assessment · HL.HF-15 Note Review Fatigue Trajectory · **partial** - we don't have a named validated-instrument wellbeing metric (e.g. Maslach Burnout Inventory). Gap-RSET-L. |

### Patient metrics (deck p. 14)

| Literature metric | Our equivalent |
|---|---|
| Patient experience / care quality | IO.PX-6 Therapeutic Relationship · IO.PX-7 Full Attentiveness · **covered** |
| Patient trust/comfort with AI | IO.PX-1 Opt-Out Rate · GV.CR-2 Verbal Notification · **covered** |
| Consent processes | GV.CR-1 Dissent · GV.CR-2 Verbal Notification · GV.PD-8 Consent Verification · **covered** |

### Provider / system metrics (deck p. 14)

| Literature metric | Our equivalent |
|---|---|
| Reported patient safety events | GV.SG-11 Adverse Event / Incident Rate (LFPSE) · GV.SG-14 Near-Miss Reporting · **covered** |
| Accuracy (provider note contribution, BERTScore) | TP.SN-2 BERTScore · TP.SN-12 Linked Evidence / Provenance Tracing · **covered** |
| Document quality (PDQI-9, PDQI-10) | TP.SN-3 PDSQI-9 · **covered** (PDQI variants are instrument-family; we reference the main construct) |
| Documentation time | GV.OP-1..4 · **covered** |
| Completion / referral / letter turnaround | GV.OP-3 Note Turnaround · overlaps Gap-RSET-F (letters) |
| Productivity: wRVU, appointment rates | TP.CC-10 wRVU / Tariff Impact Attribution · GV.OP-6 Adoption Rate · **covered** |
| Appointment duration / overruns | **gap** - consultation-duration impact as a metric is missing. Gap-RSET-M. |
| AVT utilisation rate | GV.OP-6 Adoption Rate & Selective Use Patterns · **covered** |
| Equity of adoption | IO.FE-1 Deployment Equity Index · **covered** |
| Backlog clearance | GV.OP-3 Note Turnaround (proxy) · **partial** - distinct backlog-clearance metric missing. Minor. |

### Logic-model inputs/activities/outputs (deck p. 28)

Our governance & operational metrics align well with the logic model's inputs (secure recording, model accuracy, training, secure storage) and activities (record, transcribe, generate, validate, EHR integration, consent). No structural gaps.

## Consolidated gap list

Proposed entries for `gaps.yaml` under `origin: external-review`, source `RSET-Feb-2026`:

| Gap ID | Title | RSET ref | Notes |
|---|---|---|---|
| Gap-RSET-A | Transcript / code review-ergonomics metric | #3, #20 | Not just "can review" but "how easily/reliably clinician reviews" - ties to HL.HF-3 Review-Before-Signing but at the review-UI level |
| Gap-RSET-B | Transcript relevance / signal-preservation | #11 | How well does the product strip irrelevant content without losing signal? |
| Gap-RSET-C | Transcript edit metrics (parallel to summary edits) | #13 | HL.HF-* applies to summary; extend to transcript if transcript is editable |
| Gap-RSET-D | Configurability surface integrity | #14 | Whether safety-critical features can be toggled off - meta-property of the product |
| Gap-RSET-E | AI-mediated editing modality integrity | #16 | Voice/chat-based editing introduces new hallucination surface |
| Gap-RSET-F | Letter / referral generation quality | #21, slide p. 14 | Discrete from summary write-back; patient-facing and clinician-facing letters |
| Gap-RSET-G | Contextual data fusion accuracy | #23, #37 | When product pulls prior EHR data into the summary, fidelity of that fusion |
| Gap-RSET-H | Task / action-item extraction accuracy | #25 | Separate construct from summary; can misattribute or fabricate tasks |
| Gap-RSET-I | Disability-specific speech performance | #31 | Dysarthria, aphasia, hearing-impaired speech - explicit sub-populations beyond current IO.FE |
| Gap-RSET-J | Interpreter-mediated consultation performance | #32 | Translation pass distorts speaker turns, content, and consent flow |
| Gap-RSET-K | Offline-mode integrity | #38 | Functional, safety, and data-handling properties when connectivity drops |
| Gap-RSET-L | Validated wellbeing-instrument metric | deck p. 14 | Named validated instrument (MBI, Copenhagen Burnout, etc.) rather than ad-hoc surveys |
| Gap-RSET-M | Consultation duration / overrun impact | deck p. 14 | Time per encounter, overrun rate - operational metric absent |

## Recommendations

1. **Add the 13 RSET-derived gaps to `gaps.yaml`** (Phase 2c) with `origin: external-review`, `source: RSET-Feb-2026`, `status: proposed`.
2. **Tier triage** - most of these are Tier 2 (recommended). Gap-RSET-A (review ergonomics) and Gap-RSET-K (offline-mode integrity) are arguable Tier 1 because they bear on everyday safe use.
3. **Do not add metrics yet** - flag and hold until the user approves. Several may consolidate (e.g. RSET-B and RSET-G are related).
4. **Update `_contents.md` and CHANGELOG** when metrics are added in a later round.
5. **Tag this audit artefact** in the CHANGELOG v3.2 section as an input to the restructure work.

## Strengths the RSET work validates

The RSET taxonomy's essential-vs-additional framing independently converges on many of our Tier 1 choices (write-back, consent, security, accuracy). The scoping-review metric categories match our Parts A/C/D/E boundaries. This is external validation that the structural choices in our taxonomy are sensible.

## Where we go beyond RSET

- RSET does not address: Responsible-AI lens, cross-standards mapping (11 standards), pipeline-interaction failure modes, meta-evaluation, environmental sustainability, applicability classification, metric families.
- RSET is a capability list; we are a measurement framework. Both are needed and should cite each other.
