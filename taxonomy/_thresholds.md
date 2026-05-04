# Threshold Reference

!!! warning "These are starting points, not standards"

    Numbers on this page are **proposed starting points**. They are not validated, not industry consensus, not regulatory thresholds, and not contractual gates. They exist because deployers ask "what's a reasonable starting figure?" and refusing to answer is its own dishonesty — but answering is not the same as knowing.

    **Compound-errors caveat (read this).** Each number on this page was authored independently. The thresholds have not been jointly calibrated against deployment data. A deployment that adopts every threshold as written may sit on a combination of triggers that no single trigger would have produced — for example, simultaneously satisfying the Edit Rate alert, the Time-to-Sign pause trigger, and the Review-Before-Signing pause may indicate one underlying issue counted three times, or three independent issues converging, and this page cannot tell you which. Treat each threshold as one input to a clinical-safety judgement, not as a pass/fail gate.

    **What you should do with these numbers.**

    - Use them to start a conversation with your vendor and your clinical-safety officer.
    - Calibrate them locally before any operational use; document where you diverged and why.
    - Re-calibrate after any deployment change (model update, scope change, population change).
    - Do **not** paste them into procurement contracts as binding gates.
    - Do **not** cite them as authoritative in academic work without explicit prototype-status framing.

    **Why the split.** Earlier versions of this taxonomy embedded these numbers in metric definitions themselves. That made each number look more authoritative than it should have, and it let numbers travel separately from their caveats. Pulling them out into one place — and being structurally loud about what they are — is an attempt to fix that.

## How to read this page

The page has three layers.

**Cited thresholds** (first section below) are numbers attributed to specific external authorities — NAS Day Zero SPI, UK GDPR statutory deadlines, NHS England guidance. These are sourced; the taxonomy is just citing them.

**Per-metric proposed thresholds** (the bulk of the page) are taxonomy-proposed starting points. Each row has a "why this number" provenance column that names the actual reasoning — author judgement, carried-from-prior-version, convention-mirroring, engineering rule-of-thumb. The provenance is honest about the limits.

**Cross-metric conventions** (final sections) are named patterns — severity weights, test-corpus floors, severity-band ladders, gate-vs-boundary distinctions — that recur across multiple metrics. They are gathered here so deployers can see related thresholds together, and so the taxonomy doesn't restate the same convention in five different metric bodies.

The metrics themselves now carry only **Trigger Conditions** (qualitative descriptions of what kinds of patterns matter). Specific numerical starting points live here.

---

## Cited thresholds

These thresholds are attributed to external authorities. They are *not* taxonomy-proposed.

| Metric | Threshold | Source | Use |
|---|---|---|---|
| HL.HF-3a Review-Before-Signing Rate | RBS ≥ 95 % aggregate | NAS Day Zero SPI | Pre-deployment gate |
| HL.HF-3a | Per-clinician RBS ≥ 90 % | NAS Day Zero SPI | Minimum individual performance |
| HL.HF-3a | Aggregate < 85 % for 2 consecutive weeks | NAS Day Zero SPI | Pause trigger |
| HL.HF-3a | T_min = max(15 s, 3 s × word_count / 100) | NAS Day Zero SPI | Dwell-threshold formula for review classification |
| HL.HF-3b Time-to-Sign Distribution | TTS_norm < 0.5 s/word flag | Keyes-Stanford-Monitoring-2025 (rubber-stamping principle); specific value taxonomy-proposed | Rubber-stamping flag (the *concept* is cited; the specific 0.5 s/word value is author-proposed) |
| GV.OP-5 System Availability | ≥ 99.5 % during consultation hours | NAS Day Zero SPI | Operational availability gate |
| GV.PD-10 SAR Fulfilment | ≤ 30 days | UK GDPR Article 15 | Statutory deadline |
| TP.SN-5 Hallucination Rate | ≥ 5 % critical OR > 5 % HR_w / 3 days | NAS Day Zero SPI pause logic | Pause trigger |

These eight thresholds are the only numbers in the catalogue with formal external attribution. Everything else is taxonomy-proposed.

---

## Per-metric proposed starting points

Per-metric tables. Each row has the threshold value, its operational context, and a "why this number" provenance column. The provenance is the most honest part of the row — it names whether the number is author judgement, carried from a prior version, mirrors an external convention, or sits on something firmer.

### TP cluster

#### TP.AC-5 — Microphone & Hardware Validation { #tp-ac-5 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | 100 Hz – 8 kHz frequency response | Minimum acceptable hardware spec | Standard speech-frequency range; matches consumer microphone specs and the band carrying clinical-conversation intelligibility |
    | > 99.9 % uptime | Connectivity reliability gate | Three-nines is a common SLA convention; the *meaningful* gate is "no consultations lost to mic failure" |

#### TP.ASR-12 — Hallucination-Under-Noise Rate { #tp-asr-12 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≥ 50 samples per category | Test-corpus floor | Statistical floor for stable per-category rate estimation. See [Test-corpus floor convention](#test-corpus-floor-convention) for the rare-event-rate caveat |
    | 0 critical-class hallucinations | Pre-deployment gate | Definitional category boundary, not a percentage threshold. See [Aggregate-rate gates vs zero-tolerance boundaries](#aggregate-rate-gates-vs-zero-tolerance-category-boundaries) |
    | < 1 % moderate-class | Per-category alert | Author judgement; in line with TP.SN-5 critical-subtype rate (< 0.5 %) but loosened by class severity |
    | < 5 % benign-class | Per-category alert | Author judgement; an order of magnitude looser than moderate |
    | HUN_w severity-weighted formula | Aggregation method | See [Severity-weighting convention](#severity-weighting-convention) |
    | > 25 % drift sustained two audit cycles | Pause / escalation trigger | **v4.5.1-tightened from > 50 % drift** (was too loose — by then the system has visibly degraded); now matches the v3.4 drift conventions in the GV.PD metrics |

#### TP.ASR-13 — Numeric Accuracy { #tp-asr-13 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | 100 % dosage accuracy | Pre-deployment gate | Zero-tolerance category boundary. Any wrong dose is a safety event |
    | ≥ 99 % unit accuracy | Pre-deployment gate | Author judgement; one nine below dosage |
    | ≥ 95 % integer / decimal / date / range | Per-subtype pre-deployment floor | Author judgement; conventional pre-deployment floor (cluster with [Aggregate-rate gates](#aggregate-rate-gates-vs-zero-tolerance-category-boundaries)) |
    | ≥ 200 numeric tokens per sub-type | Test-corpus floor | See [Test-corpus floor convention](#test-corpus-floor-convention) |
    | ≥ 1000 total tokens | Aggregate test-corpus floor | Five sub-types × 200 = 1000; derived consistency, not independent claim |
    | > 2 % sustained drift below baseline / two months | Continuous-monitoring alert | Two-month sustainment window is generous; defensible as a real signal rather than noise |
    | < 90 % for any sub-type | Pause / escalation trigger | Five-percentage-point gap from the 95 % gate |

#### TP.CC-6 — Code Hallucination Rate { #tp-cc-6 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | 0.0 hallucination rate | Pre-deployment gate | Definitional category boundary. Any non-existent code is an architectural failure of the coding pipeline |

#### TP.SN-5 — Hallucination Rate { #tp-sn-5 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≤ 2 % HR_w on ≥ 500-note test set | Pre-deployment gate | Author judgement; two orders of magnitude tighter than benign-class TP.ASR-12 because hallucination affects clinical signal directly |
    | < 0.5 % critical-subtype | Pre-deployment ceiling | Five times tighter than aggregate; critical-subtype carries the safety load |
    | > 3 % sustained two weeks | Continuous-monitoring alert | Above pre-deployment but not yet at pause; useful gradient. Carries the v3.3 "1.5× pre-deployment gate" pattern |
    | HR_w severity-weighted formula | Aggregation method | See [Severity-weighting convention](#severity-weighting-convention) |

(Pause trigger ≥ 5 % critical OR > 5 % HR_w / 3 days is **cited** above — see [Cited thresholds](#cited-thresholds))

#### TP.SN-6 — Omission Rate { #tp-sn-6 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≤ 3 % OR_w on ≥ 500-note test set | Pre-deployment gate | One percentage point looser than hallucination — omissions are easier to make and harder to verify in unstructured prose |
    | < 1 % critical-category per category | Per-category pre-deployment floor | Twice the SN-5 critical-subtype rate (0.5 %); category is broader than subtype |
    | > 5 % critical / mandatory category | Continuous alert | Five-times-floor pattern |
    | > 1.5× deployment-baseline drift | Aggregate-drift alert | Multiplicative-drift convention |
    | ≥ 10 % critical OR > 8 % aggregate | Pause trigger | Pause-trigger ladder |
    | OR_w severity-weighted formula | Aggregation method | See [Severity-weighting convention](#severity-weighting-convention) |

#### TP.SN-15 — Negation Handling Accuracy { #tp-sn-15 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≥ 98 % real-consultation NA_w | Pre-deployment gate | Negation handling is high-stakes (allergy "no penicillin" → "penicillin" is a safety event); two percentage points above the more general 95 % cluster |
    | ≥ 90 % adversarial-test | Adversarial pre-deployment gate | Eight-point loosening for adversarial test — adversarial sets are constructed to fail |
    | ≥ 200-sentence adversarial floor | Test-corpus floor | See [Test-corpus floor convention](#test-corpus-floor-convention) |
    | 0 allergy-category negation failures | Zero-tolerance | Definitional category boundary |
    | < 95 % NA_w / two cycles | Pause trigger | Three-point drop from 98 % gate |
    | NA_w severity-weighted formula | Aggregation method | See [Severity-weighting convention](#severity-weighting-convention) |

#### TP.SN-20 — Uncertainty Marker Preservation { #tp-sn-20 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≥ 95 % UMP_w real-consultation | Pre-deployment gate | Loosens from SN-15's 98 % because uncertainty preservation is harder (more subjective) than negation |
    | ≥ 90 % adversarial UMP_w | Adversarial pre-deployment gate | Five-point adversarial loosening (vs SN-15's eight) — asymmetry in adversarial test difficulty |
    | ≥ 200 markers / cycle | Test-corpus floor | See [Test-corpus floor convention](#test-corpus-floor-convention) |
    | ≥ 30 markers per epistemic level | Per-level floor | Statistical floor per level (~5 levels × 30 + tails) |
    | ≥ 100 adversarial markers | Adversarial test-set size | Half the real-test floor; standard 2:1 ratio |
    | 0 safety-critical inflation events | Zero-tolerance | Definitional category boundary |
    | ≥ 85 % conditional-uncertainty preservation | Pre-deployment gate (conditionals) | Loosened ten points from real-consultation gate — conditional structures are harder to preserve |
    | < 85 % UMP_w / two cycles | Pause / escalation trigger | Same gap pattern as SN-15 |
    | Asymmetric severity weights | Aggregation method | The asymmetry is *the* point of UMP — over-confidence (inflation) is more dangerous than under-confidence (deflation). See [Severity-weighting convention](#severity-weighting-convention) for the asymmetric variant |

#### TP.WB-1 — Write-back Fidelity { #tp-wb-1 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≥ 200 cases per EPR | Test-corpus floor | See [Test-corpus floor convention](#test-corpus-floor-convention) |
    | ≥ 40 safety-critical cases | Over-representation floor | 20 % of the corpus floor explicitly safety-critical |
    | ICC ≥ 0.85 inter-rater | Test-case construction consistency | See [Test-corpus floor convention](#test-corpus-floor-convention) for the paired ICC ≥ 0.85 convention |
    | 100 % safety-critical fidelity | Pre-deployment gate | Definitional category boundary. See [Aggregate-rate gates vs zero-tolerance boundaries](#aggregate-rate-gates-vs-zero-tolerance-category-boundaries) |
    | ≥ 95 % free-text fidelity | Pre-deployment gate | Cluster with [Aggregate-rate gates](#aggregate-rate-gates-vs-zero-tolerance-category-boundaries) |
    | 0 type-(iii) failures (hallucinated safety-critical) | Zero-tolerance | Definitional |
    | ≥ 99 % monthly safety-critical | Continuous monitoring | Continuous-monitoring loosening from 100 % pre-deployment — acknowledges real-world drift |

#### TP.WB-2 — Integration Error Rate { #tp-wb-2 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | IER < 0.001 | SLA target baseline | **v4.5.1-tightened (provenance only)**: previously "standard SLA target" (vague); now flagged as "standard healthcare integration SLA convention". Three-nines reliability is the standard for healthcare integration SLAs |
    | < 0.0005 / 0.0003 / 0.0002 | Per-error-type sub-thresholds | Sums to 0.001; allocation reflects severity of error type |
    | 0 critical-class events | Pre-deployment | Definitional |
    | > 50 % above per-EPR baseline / 7 days | Drift alert | Multiplicative drift convention |
    | > 5 × SLA / 24 hours | Pause / escalation | Order-of-magnitude alert ladder |

#### TP.WB-3 — Field Mapping Accuracy { #tp-wb-3 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≥ 200 cases per EPR | Test-corpus floor | See [Test-corpus floor convention](#test-corpus-floor-convention) |
    | ICC ≥ 0.85 | Field-map authoring consistency | See [Test-corpus floor convention](#test-corpus-floor-convention) |
    | 100 % safety-critical mapping | Pre-deployment | Definitional. See [Aggregate-rate gates vs zero-tolerance boundaries](#aggregate-rate-gates-vs-zero-tolerance-category-boundaries) |
    | ≥ 95 % per-category | Pre-deployment | Cluster |
    | 0 type-(iii) safety-critical failures | Zero-tolerance | Definitional |
    | ≥ 99 % monthly | Continuous monitoring | |
    | < 90 % per-category in audit | Alert | Five-point gap from 95 % gate |
    | < 95 % aggregate safety-critical / monthly audit | Pause / escalation | |

#### TP.WB-4 — Update vs Append Behaviour { #tp-wb-4 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≥ 50 cases per cell | Test-corpus floor | Statistical floor for cell-level rates |
    | ≥ 1250 total per EPR | Aggregate test-corpus | 5 × 5 × 50; derived |
    | ICC ≥ 0.85 | Rule-document authoring consistency | See [Test-corpus floor convention](#test-corpus-floor-convention) |
    | 0 safety-critical critical-failure events | Zero-tolerance | Definitional |
    | ≥ 95 % per-cell behaviour correctness | Pre-deployment | Cluster |
    | ≥ 90 % per-cell in audit | Alert | Five-point gap |
    | < 95 % aggregate quarterly | Pause / escalation | |

### HL cluster

#### HL.HF-1 — Edit Rate (% Notes Edited) { #hl-hf-1 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | Substantive ER 30 – 80 % during first 4 weeks | Day-Zero baseline expectation | Range is wide because deployment context dominates — specialty mix, patient population, platform maturity all move it. The *range* is the right shape; the *anchors* are author-judgement |
    | > 15 pp drop sustained ≥ 4 weeks | Continuous monitoring (complacency) | Carried from prior taxonomy versions; defensible as a real-world meaningful drop magnitude |
    | < 50 % of per-clinician baseline / 4 weeks | Pause / review trigger | Half-of-baseline pause logic; pattern matches NAS-style ladders |
    | Zero safety-critical / 4 weeks while stylistic > 10 % | Trust-calibration review | Zero-tolerance category combined with continued non-zero behaviour as a discrimination test |

#### HL.HF-3a — Review-Before-Signing Rate { #hl-hf-3a }

!!! note "Starting points (cited values are above in Cited thresholds)"

    | Threshold | Context | Why this number |
    |---|---|---|
    | Per-clinician > 10 pp drop from baseline | Individual complacency signal | Author judgement; standard "drop from baseline" magnitude |
    | Per-clinician < 75 % / 1 week | Individual severe-failure trigger | Twenty-point gap from the 95 % aggregate gate |

#### HL.HF-3b — Time-to-Sign Distribution { #hl-hf-3b }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | P5 of TTS_norm < 0.3 s/word | Continuous-monitoring lower-tail floor | 60 % tighter than the 0.5 s/word flag; author judgement |
    | > 10 pp rise above baseline (rate of below-flag-threshold notes) | Alert | Standard drop-from-baseline magnitude |
    | Weekly P10 < 0.3 s/word AND HL.HF-1 substantive < 25 % | Pause / review trigger | Joint-trigger; conservative because it requires two signals |

### IO cluster

#### IO.PX-1 — Patient Opt-Out Rate { #io-px-1 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | > 2 pp rise from baseline | Monthly aggregate alert | Author judgement; standard "noticeable drift" magnitude |
    | ≥ 2 × practice-mean disparity ratio with χ² Holm-corrected | Demographic-disparity alert | Two-fold disparity is the conventional alert magnitude in health-equity work; χ²-Holm controls multiple comparisons |
    | ≥ 3 × practice-mean sustained 2 months | Pause / review (systematic equity failure) | Three-fold + sustainment; conservative |
    | > 5 pp rise | Pause / review (trust deterioration) | 2.5 × the alert magnitude |

### GV cluster

#### GV.CR-1 — Patient Dissent Recording Rate { #gv-cr-1 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | 100 % all dissent events recorded and respected | Target gate | Definitional (consent-respect is binary at the event level). See [Aggregate-rate gates vs zero-tolerance boundaries](#aggregate-rate-gates-vs-zero-tolerance-category-boundaries) |
    | ≥ 99 % monthly per sub-metric | Continuous monitoring | Continuous-monitoring loosening from 100 % |
    | < 95 % sub-metric / month | Pause / escalation | Four-point gap |
    | < 0.5 % of AVT-eligible consultations (recorded rate) | Sampling-verification trigger | If recorded rate is implausibly low, sample to verify |

#### GV.CR-2 — Verbal Notification Compliance { #gv-cr-2 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | 100 % delivery target | Target gate | Definitional |
    | ≥ 95 % self-report compliance | Pre-deployment | |
    | ≥ 90 % overall quarterly survey/audio audit | Continuous monitoring | Self-report tends to over-state; five-point gap between self-report and audit measure is empirically common |
    | ≥ 85 % every content element | Per-element floor | Internal consistency constraint |
    | < 75 % any content element | Escalation trigger | Twenty-point gap |
    | ≥ 30 patients / clinician / quarter | Sample-size floor | Statistical floor for per-clinician estimates |

#### GV.CR-3 — AI-Generated Content Labelling Compliance { #gv-cr-3 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | 100 % labelling | Zero-tolerance target | Definitional. Every AI-generated entry must be labelled |

#### GV.CR-4 — AVT Supplier Registry Listing Verification { #gv-cr-4 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≤ 12 months attestation currency | Currency target | Annual review cadence — standard for procurement-side compliance evidence |
    | > 9 months alert (60-day grace) | Currency alert | Three-month early-warning |

#### GV.CR-5 — ICB Engagement Documentation { #gv-cr-5 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≥ 14 days notification before go-live | Pre-deployment | Two weeks is conventional NHS-side notification window |
    | 2 unanswered notifications same ICB / 12 months | Pattern-of-non-response trigger | |

#### GV.CR-6 — Clinical Safety Case Completeness { #gv-cr-6 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | 100 % all eight DCB0129 sections | Structural compliance | Definitional (DCB0129 mandates the section structure) |
    | ≤ 30 days post-trigger update | Currency window | One-month convention; matches DCB0160 update cadence |
    | > 90 days unupdated | Escalation | Three-month |
    | ≤ 24 months external CSO review | External review cadence | Two-year cycle matches CSO review conventions |

#### GV.CR-7 — DPIA Template Completion Rate { #gv-cr-7 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | 100 % deployments with complete DPIA | Target gate | Definitional |
    | ≤ 30 days post-significant-change re-review | Review window | One-month convention |
    | > 12 months stale | Escalation | Annual review cadence |

#### GV.OP-1 — Documentation Time per Consultation { #gv-op-1 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | 4 weeks per-clinician baseline | Baseline-establishment window | Same baseline window as HL.HF-1; consistency |
    | > 25 % deviation from baseline | Flag-for-review | Quarter-of-baseline change is the conventional "noticeable" magnitude |
    | Out-of-consultation > 0 + in-consultation increase | Burden-displacement rule-out | Operational shape, not numeric |

#### GV.OP-14 — Historical Output Continuity { #gv-op-14 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | 24-hour synthetic-retirement test before go-live | Pre-deployment gate | Day-long disconnection is a meaningful operational test; longer would impede go-live, shorter wouldn't surface issues |
    | 100 % three-sub-metric pre-deployment gate | Pre-deployment gate | Definitional category boundary across commit-completeness / provenance-dereference / patient-portal access |
    | ≥ 95 % per-event provenance-dereference rate at retirement-day +30 | Per-event monitoring | Five-percentage-point gap from the 100 % pre-deployment gate; one-month sustainment window |
    | ≥ 7 years contractual access window | Procurement gate | Aligns with NHS clinical-record retention; specialty-specific rules may apply (paediatric to 25 years, mental health to 20) |

#### GV.PD-1 — Audio Retention Compliance { #gv-pd-1 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≥ 99.5 % monthly per location | Continuous monitoring | Continuous loosening from 100 % gate |
    | < 95 % per-location / month | Escalation | |

#### GV.PD-2 — Audio Time-to-Deletion { #gv-pd-2 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≤ 24 hours median TTD | Continuous monitoring | DPIA-conventional retention horizon |
    | ≤ 7 days P99 ceiling | Tail-distribution gate | One week as upper limit on edge cases |
    | < 1 % encounters exceeding | Edge-case ceiling | One-percent ceiling |
    | ≥ 99.5 % per-storage-location | Continuous monitoring | |

#### GV.PD-3 — Transcript Retention Compliance { #gv-pd-3 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≥ 99.5 % monthly per-purpose × location | Continuous monitoring | |
    | ≥ 90 % "quality monitoring" sub-categorisation coverage | Granularity floor | |
    | < 95 % per-purpose | Escalation | |

#### GV.PD-8 — Consent Verification Accuracy { #gv-pd-8 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≥ 30 patients / quarter / practice | Survey floor | Statistical floor with demographic stratification |
    | > 25 pp gap (compliance − understanding) | Gap-trigger alert | Quarter-scale gap; operationally meaningful |
    | < practice mean − 20 pp on demographic axis | Demographic-disparity alert | Twenty-point demographic gap |
    | > 40 pp gap / 2 quarters | Escalation | Sustained large gap |
    | < 50 % understanding on any axis | Escalation | Half-of-patients-don't-understand is a meaningful absolute floor |

#### GV.PD-10 — Subject Access Request Fulfilment { #gv-pd-10 }

(See [Cited thresholds](#cited-thresholds) for the statutory ≤ 30-day deadline.)

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | 100 % locate-rate | Target | Definitional |
    | 100 % export-rate | Target | Definitional |
    | ≥ 95 % timeliness within 30 days | Continuous monitoring | Continuous loosening from statutory deadline |
    | > 30 % using two-month extension | Systematic-failure alert | A third of SARs needing extension suggests process failure |

#### GV.PD-11 — Right to Erasure Compliance { #gv-pd-11 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≤ 30 days fulfilment | Erasure window | Mirrors GDPR Article 15 / 17 statutory cadence |

#### GV.PD-16 — Decommissioning Data Handling Compliance { #gv-pd-16 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≤ 90 days deletion completion | Deletion-target window | Three-month operational target |
    | ≤ 180 days with sub-processor cascade | Cascade-target window | Six-month; doubles primary target for sub-processor coordination |
    | > 50 % timeline overrun | Escalation | Half-of-target overrun |
    | < 95 % per-location coverage | Escalation | |

#### GV.SG-1 — Model Version Tracking { #gv-sg-1 }

!!! note "Starting points (severity ladder cross-references the convention below)"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≤ 24 hours median deployer-notification latency | Continuous monitoring | See [Severity-band notification ladder convention](#severity-band-notification-ladder-convention) |
    | > 7 days unnotified | Alert | (same convention) |
    | > 14 days unnotified | Escalation | (same convention) |
    | 100 % per-inference component-version coverage | Structural gate | Definitional. Any inference missing a versioned component is a defect |

#### GV.SG-14 — Near-Miss Reporting Rate { #gv-sg-14 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≥ 25 % active-to-inferred ratio | Safety-culture floor | Author judgement; the qualitative "active reporting at least matches passive inference at material rate" is defensible — the specific quarter is a starting figure |

#### GV.SG-17 — Hazard Log Completeness { #gv-sg-17 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≤ 30 days update window after new failure mode discovery | Currency target | One-month convention matches GV.CR-6 / GV.CR-7 cadence |

#### GV.TC-1 — Clinician Training Completion Rate { #gv-tc-1 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | 100 % completion governance gate | Structural | Definitional |
    | Engagement floor per module — deployer-set based on module length, audited via session-time telemetry | Engagement floor | **v4.5.1-loosened from 30 / 15 / 20-minute floors** — the specific minute counts added false precision; deployer should set local floors based on actual module length |
    | 12-month M3 / annual M4 refresh | Refresh cadence | Annual cadence is standard for clinical compliance training |
    | 14-day grace for late onboarders | Onboarding window | Two-week onboarding is operationally typical |
    | < 95 % aggregate / 2 months | Escalation | |

#### GV.VT-1 — Model Change Notification Compliance { #gv-vt-1 }

!!! note "Starting points (severity ladder cross-references the convention below)"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≥ 14 / 7 / 0 days advance notice (Major / Moderate / Minor) | Pre-deployment | See [Severity-band notification ladder convention](#severity-band-notification-ladder-convention) |
    | 100 % per-element completeness | Structural | Definitional |
    | < 95 % completeness 90-day rolling | Escalation | |

#### GV.VT-5 — Incident Disclosure Compliance { #gv-vt-5 }

!!! note "Starting points (severity ladder cross-references the convention below)"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≤ 24 / 72 / 168 / 720 hours (Critical / High / Medium / Low) | Disclosure ladder | See [Severity-band notification ladder convention](#severity-band-notification-ladder-convention) — 24 h / 72 h / 7 d / 30 d. Lineage: HSE incident-classification timeframes (where known) |
    | 100 % five-element completeness per incident | Structural | Definitional |
    | Critical disclosed > 72 hours | Escalation | |

#### GV.VT-7 — Sub-Processor Transparency { #gv-vt-7 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≥ 30 days advance notice for material entries | Change-notification window | One-month change-notification window is the GDPR-conventional period |
    | 100 % material sub-processor disclosure | Disclosure gate | Definitional |
    | Quarterly discovered-vs-disclosed audit | Audit cadence | |
    | Annual per-material-sub-processor DPA review | Review cadence | |

#### GV.VT-13 — Evidence Pack Freshness { #gv-vt-13 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≤ 12 months "Fresh" threshold | Currency target | Annual review cadence; matches procurement-side compliance evidence conventions |
    | > 24 months "Stale" on any axis | Pause / escalation | Two-year window; doubles the Fresh threshold for a clear staleness step |
    | ≥ 3 components Aging | Pause / escalation | Pattern-of-staleness trigger across the three component axes |

#### GV.VT-14 — Indicative Pricing Transparency { #gv-vt-14 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≤ 12 months matrix currency | Currency target | Annual review cadence |
    | ±20 % materiality threshold | Procurement-review trigger | Author judgement; conventional "material" threshold for procurement-side change review |
    | > 24 months stale on any contracted use case | Pause / escalation | Two-year window matches GV.VT-13 staleness convention |

#### GV.VT-15 — Retirement Notification Compliance { #gv-vt-15 }

!!! note "Starting points"

    | Threshold | Context | Why this number |
    |---|---|---|
    | ≥ 12 months product-retirement notice | Notice period (full retirement) | Annual notice; allows deployer to find replacement |
    | ≥ 6 months major-feature-withdrawal notice | Notice period (feature withdrawal) | Half the retirement window for partial withdrawal |
    | ≥ 90 days integration-withdrawal notice | Notice period (technical withdrawal) | Quarter-year for narrow technical changes |
    | < 50 % of contracted lead time | Escalation | Multiplicative drift trigger |
    | < 80 % completeness | Escalation | Twenty-point completeness gap |

---

## Cross-metric conventions

Patterns that recur across multiple metrics. Defining them once here means metric bodies don't restate the same convention five times — and means cross-metric inconsistencies become visible.

### Severity-weighting convention

Used by **TP.ASR-12, TP.SN-5, TP.SN-6, TP.SN-15** for symmetric severity weighting; **TP.SN-20** uses an intentionally asymmetric variant.

!!! note "Starting points — symmetric variant"

    `weighted_rate = (0.1 · benign + 0.5 · moderate + 1.0 · critical) / N_total`

    The weights express a judgement that critical errors are an order of magnitude worse than benign, and roughly twice as bad as moderate. Five metrics independently arrived at these weights — but the choice is *one author judgement copied across five metrics*, not five independent decisions.

    A clinician-feedback round could plausibly argue for steeper benign-to-moderate gaps (0.05 / 0.5 / 1.0) or shallower critical gaps (0.1 / 0.3 / 1.0). The convention exists because *some* multi-class aggregation is needed to produce a scalar; the specific weights are starting points.

!!! note "Starting points — asymmetric variant (UMP_w only)"

    For Uncertainty Marker Preservation (TP.SN-20), the weights are *intentionally asymmetric*: certainty-inflation (over-confidence) gets full critical weight; certainty-deflation (under-confidence) gets benign weight. Same shape; different semantics — over-confidence is more dangerous than under-confidence in clinical contexts.

    This asymmetry is the *point* of UMP. It is not a copy of the symmetric convention.

### Test-corpus floor convention

Used by **TP.ASR-13, TP.SN-15, TP.SN-20, TP.WB-1, TP.WB-3, TP.WB-4** (cases-per-EPR variant).

!!! note "Starting points"

    **Floor:** ≥ 200 cases per per-category rate measurement.

    **Inter-rater consistency (paired):** ICC ≥ 0.85 for test-case construction.

    **Rare-event-rate caveat (important).** 200 is a *floor*, not a target. For rates below 5 %, push the floor above ~10 expected events per category — for sub-1 % rates this means corpora above 1000. The current taxonomy uses 200 universally; this caveat is the most honest acknowledgement of a measurement-science gap the consolidation can produce.

    The 200 figure is rule-of-thumb-territory: for a 5 % event rate, 200 trials gives roughly ±3 % at 95 % confidence; for a 1 % event rate it is barely informative. The number is defensible as a starting point but is *not* the right floor for tight thresholds.

    The ICC ≥ 0.85 figure is a standard psychometric convention for "substantial" agreement and matches the CHECK paper's reported floor.

### Severity-band notification-ladder convention

Used by **GV.SG-1, GV.VT-1, GV.VT-5, GV.VT-15**.

!!! note "Starting points — meta-pattern, not a fixed ladder"

    **Shape:** 3 or 4 severity bands. Most-severe band is "immediate" (≤ 24 h or "before the change"). Ratios between bands cluster around 3-7×.

    The four metrics that use this pattern have *different* ladder values because they encode different decisions:

    - GV.VT-5 — incident disclosure (retroactive, severity-of-incident): 24 h / 72 h / 7 d / 30 d
    - GV.SG-1 — model-version notification latency (latency-since-event): 24 h / 7 d / 14 d
    - GV.VT-1 — model-change advance notification (severity-of-change): 14 d / 7 d / 0 d
    - GV.VT-15 — retirement notice (severity-of-withdrawal): 12 mo / 6 mo / 90 d

    Picking different ladders is correct — the underlying decisions differ in time direction (retroactive vs advance) and severity meaning (of-incident vs of-change vs latency vs of-withdrawal). The *shape* (3-4 bands, immediate-most-severe, 3-7× ratios) is the convention; the specific values are per-metric author choices, often sourced from different lineages (HSE incident-classification timeframes; vendor change-control conventions).

### Aggregate-rate gates vs zero-tolerance category boundaries

Used widely. **The most important reframe in this page.**

!!! warning "Two distinct semantic flavours that look identical numerically"

    Many "100 %" thresholds in this catalogue are **zero-tolerance category boundaries**, not stringent percentage gates. The numbers look the same; the asks are fundamentally different.

    **Aggregate-rate gate (95 % / 99 % / 100 %):** the metric measures a rate; the gate says "rate must be at least this". Continuous-monitoring loosening (e.g. 99 % monthly after 100 % pre-deployment) is meaningful because rates can drift in operation. Used for free-text fidelity, mapping accuracy aggregate, training completion rate.

    **Zero-tolerance category boundary (100 %):** the metric counts events in a class; the gate says "no events in this class". 100 % shorthand for "every safety-critical field wrote correctly" is just "zero failures on safety-critical". Continuous-monitoring loosening is *not* a 1 % loosening — it acknowledges that real-world drift will produce some events, and the rate at which it does is its own metric. Used for safety-critical fidelity, dosage accuracy, code hallucinations, allergy-negation failures, AI-generated content labelling.

    **Why this matters.** A deployer reading "must reach 100 %" assumes an absurdly stringent percentage; they should be reading "no events in this class". A vendor pasting "100 % safety-critical fidelity" into a contract treats it as percentage-based; the actual operational ask is event-based.

    On this page, definitional 100 % gates carry the marker *"Definitional category boundary"* in their context column. Aggregate-rate gates do not. Read the column.

---

## Cross-references

- Each metric's **Trigger Conditions** block in its source file links here.
- See [Versioning](versioning.md) for what each release-version digit means and how thresholds versioned to specific releases.
- See [Metric history](metric-history.md) for which metrics changed in each release.
- The CSV / JSON downloads include per-threshold rows (see [Downloads](downloads.md)).
