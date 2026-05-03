### TP.AC-1 🟡 Signal-to-Noise Ratio (SNR) Monitoring

Continuous measurement of audio input quality. SNR below threshold degrades ASR accuracy unpredictably - the system may continue producing confident-looking but degraded output without alerting the clinician.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.AC-1 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Standard audio engineering; applied to AVT quality assurance |

**Why this tier?**

> Valuable continuous quality signal but requires audio analysis tooling most deployers don't have. Vendor should provide.

**Formal Definition**

```
SNR = 10 × log₁₀(P_signal / P_noise) in dB. Measured per consultation segment. Taxonomy-proposed threshold tiers: >20dB = good; 10–20dB = acceptable with quality warning; <10dB = AVT should warn or pause. Report distribution across encounters, not just mean.

⚠️ Provenance: the underlying SNR formula is standard audio engineering; the specific threshold tiers (>20 / 10–20 / <10 dB) are taxonomy-proposed engineering defaults, not externally validated for AVT-specific deployment. Per the Calibration & Context principle, require local calibration against the deployment's microphone setup and clinical acoustic environment.
```

**Code: SNR estimation from audio**

```python
import numpy as np
import librosa

def estimate_snr(audio_path, sr=16000, frame_length=2048):
    """Estimate SNR using voice activity detection."""
    y, sr = librosa.load(audio_path, sr=sr)
    
    # Simple energy-based VAD
    energy = librosa.feature.rms(y=y, frame_length=frame_length)[0]
    threshold = np.percentile(energy, 30)  # bottom 30% = noise
    
    noise_frames = energy[energy < threshold]
    signal_frames = energy[energy >= threshold]
    
    noise_power = np.mean(noise_frames**2) if len(noise_frames) > 0 else 1e-10
    signal_power = np.mean(signal_frames**2) if len(signal_frames) > 0 else 1e-10
    
    snr_db = 10 * np.log10(signal_power / noise_power)
    
    return {
        "snr_db": round(snr_db, 1),
        "quality": "good" if snr_db > 20 else "acceptable" if snr_db > 10 else "poor",
        "alert": snr_db < 10,
        "recommendation": "Consider pausing AVT" if snr_db < 10 else None
    }
```

**Limitations**

> Simple energy-based SNR is a crude proxy - overlapping speech, reverberation, and non-stationary noise complicate measurement. Clinical environments have complex acoustic profiles.

**Novel Thinking / Implications**

> 💡 The system should degrade gracefully: if SNR drops below threshold mid-consultation, the AVT should flag the note as potentially degraded rather than producing output with false confidence. This is an architectural requirement - the AVT should know when its own input quality is insufficient.

---

### TP.AC-2 🔵 Voice Activity Detection (VAD) Accuracy

Accuracy of detecting when speech is occurring vs silence/noise. VAD errors cause missed speech (content lost) or false activations (noise processed as speech, potentially generating hallucinated content from non-speech audio).

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.AC-2 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Standard speech processing; critical for clinical AVT given variable environment |

**Why this tier?**

> Vendor-side pre-deployment testing. Deployers cannot independently assess VAD performance.

**Formal Definition**

```
VAD Precision = |true_speech_detected| / |all_detected_as_speech|. VAD Recall = |true_speech_detected| / |all_actual_speech|. False activation rate FAR = |noise_detected_as_speech| / |total_noise_duration|. Clinical risk: low recall → content loss; low precision → noise-induced hallucination.
```

**Limitations**

> VAD accuracy is environment-dependent. A VAD validated in quiet rooms may perform poorly with background conversation, equipment noise, or telephone audio.

**Novel Thinking / Implications**

> 💡 False activations are the underappreciated risk: if the VAD activates on background TV, corridor conversation, or equipment alarms, the ASR processes non-clinical audio. The summariser then has to decide what to do with transcribed noise - which may look like clinical content and get included in the note.

---

### TP.AC-3 🟡 Acoustic Environment Profiling

Characterisation of the deployment acoustic environment against the vendor's validated acoustic conditions. Gap between validated and actual environment = unquantified risk.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.AC-3 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Safety |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Periodic Audit |
| **Responsible Actors** | Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Proposed - extends validated use envelope concept to acoustic conditions |

**Why this tier?**

> Deployer should characterise their acoustic environment at setup to confirm it falls within the vendor's validated conditions.

**Formal Definition**

```
Profile vector: [SNR_typical, reverberation_time_RT60, background_noise_type, speaker_distance_range, microphone_type]. Validated envelope V = vendor's tested conditions. Environment gap G = component-wise tolerance check (does each measured component fall within the vendor's validated range?), not a single Euclidean distance over heterogeneous units. G failing on any component → environment outside validated envelope on that dimension.

⚠️ Provenance: the profile-vector composition and the component-wise tolerance approach are taxonomy-proposed; vendor-validated envelopes are deployment-specific and must come from vendor documentation. The "envelope" framing is the substantive idea; the specific operationalisation is calibration work the deployer + vendor jointly own.
```

**Limitations**

> Acoustic conditions vary within a single practice (different rooms, open/closed doors, time of day). Point-in-time profiling may not capture the full range.

**Novel Thinking / Implications**

> 💡 This is the acoustic equivalent of the compound boundary risk model. A system validated with a lapel mic at 30cm in a quiet room may be deployed with a desk mic at 1.5m in a busy practice with a door open to the waiting room. Each acoustic parameter crossing the validated boundary compounds risk - and unlike clinical domain boundaries, acoustic boundaries are invisible to governance processes.

---

### TP.AC-4 🔵 Bystander Voice Detection Rate

Ability to detect and flag speech from individuals who have not consented to AVT processing: patients in adjacent rooms, reception staff audible through walls, family members who arrive mid-consultation without being informed.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.AC-4 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Patient Experience |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Identified in NHSE IG guidance on ambient scribing privacy implications; CQC Mythbuster 109 context |

**Why this tier?**

> Technology for reliable bystander detection does not yet exist. Important research direction but not actionable today.

**Formal Definition**

```
Detection rate = |bystander_speech_detected| / |total_bystander_speech|. False positive rate = |participant_speech_flagged_as_bystander| / |total_participant_speech|. Requires speaker enrolment or real-time speaker count monitoring.
```

**Limitations**

> Technically challenging - requires distinguishing expected speakers from unexpected ones without prior voice enrolment. Current diarisation can count speakers but cannot determine consent status.

**Novel Thinking / Implications**

> 💡 This sits at the intersection of audio capture, privacy, and consent. UK GDPR requires lawful basis for processing personal data - bystander speech captured and processed by AVT has no consent basis. The NHSE IG guidance (March 2026) flags this but provides no technical solution. A detection-and-redaction pipeline for non-consented speech would be architecturally significant.

---

### TP.AC-5 🟢 Microphone & Hardware Validation

Verification that the capture hardware meets minimum specifications for the AVT system. Includes microphone frequency response, placement distance, device compatibility, and Bluetooth/connectivity reliability.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.AC-5 |
| **Priority Tier** | 🟢 Tier 1 - Minimum Viable |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment |
| **Responsible Actors** | Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Standard audio hardware validation; vendor deployment requirements |

**Why this tier?**

> Basic pre-deployment hardware check. No AVT should go live without confirming capture hardware meets minimum specifications. Measurable today by any deployer.

**Formal Definition**

```
Hardware compliance checklist: (1) Frequency response 100Hz–8kHz minimum; (2) Sensitivity within vendor spec; (3) Placement within validated distance range; (4) Connectivity uptime >99.9% during sessions. Binary pass/fail per criterion.

⚠️ Provenance: the 100Hz–8kHz frequency range and 99.9% uptime targets are taxonomy-proposed engineering defaults — reasonable for clinical-speech capture against modern hardware norms, but not externally validated as procurement gates. Per the Calibration & Context principle, require local calibration; specifically, vendor-spec frequency-response and uptime requirements should drive the contract, not these defaults. **TP.AC-5 is currently a Tier 1 metric without the full Reference Standard / Operational Specification / Threshold Guidance tightening pattern; promotion is queued for a future release** alongside the broader threshold-recommendation review (plan-future #8).
```

**Limitations**

> Point-in-time test. Hardware degrades, batteries die mid-consultation, Bluetooth drops. Continuous hardware health monitoring is rarely implemented.

---

### TP.AC-6 🔵 Speaker Overlap Rate

Proportion of audio time with simultaneous speech from multiple speakers. Common in real consultations (interruptions, agreement utterances, talking over) and most ASR/diarisation systems handle overlap poorly - often dropping content from one speaker entirely.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.AC-6 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | One-off gate |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Standard speech processing; particularly relevant for clinical consultations |

**Why this tier?**

> Vendor pre-deployment characterisation. Deployers cannot easily measure but should understand whether their consultation style falls within the validated overlap range.

**Formal Definition**

```
Overlap Rate = T_overlap / T_total_speech, where T_overlap is the duration where >=2 speakers are simultaneously active. Report distribution across encounters. High overlap rates indicate the system is operating in conditions most benchmarks don't cover.
```

**Limitations**

> Overlap detection itself can be inaccurate. Some legitimate consultation patterns (back-channelling 'mmhm', agreement) are technically overlap but don't represent meaningful content loss.

**Novel Thinking / Implications**

> 💡 Real consultations contain meaningful overlap — back-channels, interruptions, simultaneous speech during family-present encounters — at rates that vary by consultation style and specialty. Specific overlap-rate ranges in dialogue research are reported at single digits to mid-teens of percent, but ranges vary widely by recording protocol and definition. A vendor benchmarking on scripted dyadic dialogue may report excellent performance that doesn't translate to spontaneous clinical interaction. Overlap rate should be a procurement question — what conditions was the system validated under, and what overlap rate should the deployer expect in their consultation style?

---

### TP.AC-7 🟡 Audio Clipping / Saturation Rate

Frequency of audio level exceeding the dynamic range of the capture system, causing waveform distortion. Different from SNR - clipping is a hardware/gain issue that destroys content even in quiet environments. Commonly caused by mic too close, gain set too high, or sudden loud sounds.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.AC-7 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Standard audio engineering |

**Why this tier?**

> Vendor should monitor and alert. Deployer should be notified when clipping rates exceed threshold so hardware/positioning can be corrected.

**Formal Definition**

```
Clipping Rate = N_clipped_samples / N_total_samples, where clipped samples are those at or beyond the maximum amplitude (typically +/-32767 for 16-bit). Taxonomy-proposed alert threshold: >0.1% sustained over 1 second indicates significant content degradation.

⚠️ Provenance: the underlying clipping definition is standard audio engineering; the >0.1% / 1-second sustained threshold is a taxonomy-proposed engineering default, not externally validated. Per the Calibration & Context principle, require local calibration against the deployment's automatic-gain-control behaviour and clinical content sensitivity.
```

**Code: Clipping detection**

```python
import numpy as np

def detect_clipping(audio_samples, threshold_pct=0.1):
    max_val = 32767
    near_clip = np.abs(audio_samples) >= (max_val * 0.99)
    clip_pct = (np.sum(near_clip) / len(audio_samples)) * 100
    return {
        'clipping_pct': round(clip_pct, 3),
        'alert': clip_pct > threshold_pct,
        'recommendation': 'Reduce mic gain or distance' if clip_pct > threshold_pct else None
    }
```

**Limitations**

> Modern AVT systems often use automatic gain control which masks clipping. The metric may be invisible to deployers unless the vendor exposes raw audio quality telemetry.

**Novel Thinking / Implications**

> 💡 A clipped consonant in a drug name destroys recognition deterministically. Unlike SNR-related errors which are probabilistic, clipping creates hard content loss that no downstream processing can recover.

---

### TP.AC-8 🟡 Codec & Sampling Rate Compliance

Whether audio meets minimum bit depth and sample rate specifications for the AVT system. Telephone audio at 8kHz degrades ASR significantly compared to 16kHz studio quality. Compressed codecs (e.g. heavily lossy Bluetooth audio) introduce artifacts.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.AC-8 |
| **Priority Tier** | 🟡 Tier 2 - Recommended |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Fidelity & Accuracy |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Pre-deployment, Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Established |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Standard audio engineering; vendor minimum specifications |

**Why this tier?**

> Automated check per encounter. Should be enforced architecturally - non-compliant audio should be flagged before processing.

**Formal Definition**

```
Compliance check per encounter: (1) sample_rate >= vendor_minimum (typically 16kHz); (2) bit_depth >= vendor_minimum (typically 16-bit); (3) codec in approved_codecs. Binary pass/fail per criterion. Non-compliant audio should trigger pre-processing warning or rejection.
```

**Limitations**

> Telephone consultations are increasingly common in NHS practice but most AVT systems are validated on 16kHz+ audio. The mismatch is often invisible until accuracy degrades.

**Novel Thinking / Implications**

> 💡 Telephone consultations are a hidden boundary risk. A practice using AVT for in-person consultations and then extending to telephone is operating outside the validated codec envelope. The system may produce confident-looking output of much lower accuracy.

---

### TP.AC-9 🔵 Microphone Drift Detection

Detection of gradual hardware degradation over time: declining battery performance, mechanical wear, positioning shift, accumulated debris, Bluetooth interference patterns. Different from initial validation - this catches problems that develop after deployment.

| Dimension | Value |
|-----------|-------|
| **Reference** | TP.AC-9 |
| **Priority Tier** | 🔵 Tier 3 - Advanced / Research |
| **Measurement Cadence** | Continuous |
| **Pipeline Layer** | Audio Capture |
| **Assurance Question** | Operational |
| **Measurement Method** | Computational |
| **Lifecycle Phases** | Continuous |
| **Responsible Actors** | Vendor, Deployer |
| **Maturity** | Proposed / Novel |
| **Outcome Type** | Proximal |
| **Applicability** | AVT-Specific |
| **Source** | Proposed - extends hardware validation to ongoing monitoring |

**Why this tier?**

> Conceptually valuable but requires telemetry infrastructure most vendors don't provide. Better suited for vendor-side implementation.

**Formal Definition**

```
Track baseline audio quality metrics (SNR, frequency response, noise floor) over time. Drift = significant deviation from baseline established at hardware validation. Taxonomy-proposed alert thresholds: SNR drops >5dB from baseline OR frequency response shifts >10%.

⚠️ Provenance: baseline-vs-current drift detection is a standard hardware-monitoring construct; the specific >5dB SNR-drop and >10% frequency-response-shift thresholds are taxonomy-proposed engineering defaults, not externally validated. Per the Calibration & Context principle, require local calibration against the deployment's hardware lifecycle and clinical-acoustic environment. Source row already correctly says "Proposed - extends hardware validation to ongoing monitoring".
```

**Limitations**

> Requires establishing per-device baselines and tracking longitudinally. Most AVT systems treat hardware as a black box.

**Novel Thinking / Implications**

> 💡 Hardware degrades silently. A wireless lapel mic that worked perfectly at deployment may have degraded battery contacts six months later, producing intermittent dropout that the clinician doesn't notice but that affects ASR accuracy. Drift detection is proactive maintenance - catching the problem before it causes a clinical incident.

---

