## Prototype status

### AI-coauthored — keep this front of mind

**Substantial portions of this taxonomy were drafted with AI assistance and human-reviewed.** That includes metric prose, Reference Standard / Operational Specification / Threshold Guidance blocks, citation framing, and the standards-mapping cross-references. The author reviewed the AI-drafted output, made structural decisions about what to keep / reframe / discard, and corrected errors that surfaced during review and round-trip review files (e.g. the v3.9 round-2 / FILLED reviews caught wrong DOIs, phantom catalogue entries, mis-attributed papers, and unverifiable specific numeric claims).

**Despite that review, specific claims may still contain:**

- **Confabulations** — fabricated paper titles, author lists, DOIs, or numeric findings that look plausible but don't correspond to a real published source. The v3.9 round-2 review caught several of these (e.g. `Barcelona-JAMA-Network-Open-2025` was a confabulated handle for what turned out to be a different paper; `medRxiv-Model-Autophagy-2026` didn't exist as a real preprint). More may remain undetected.
- **Mis-citations** — real papers attributed to the wrong authors, the wrong year, the wrong venue, or the wrong DOI. Round-2 caught the `SCRIBE-Wang-2025` / `Wang-Duke-MedStar-2025` phantom-duplicate case (one paper cited under two handles, with one of the two carrying a wrong DOI). Same pattern likely exists elsewhere.
- **Mis-paraphrased findings** — a paper's actual finding rephrased in a way that subtly distorts what the paper claims. Round-2 caught the Stults-2025 case (clinician-self-reported attentiveness reframed as objective time-on-task) and the Rwanda-Clinical-LLM-Evaluation case (the cited paper found the *opposite* of what the taxonomy attributed to it). More may remain.
- **Threshold numbers presented with more authority than they deserve.** "Proposed in v3.X as starting points" thresholds are calibrated against the metric's clinical-safety logic during AI-assisted drafting, not externally validated. The Calibration & Context principle says deployers must set their own; the numbers in the document are conversation starters, not defaults. Plan-future item #8 covers a structural rework of this.
- **Code snippets that don't run / don't match the cited library API.** Plan-future item #5 covers verifying every code snippet and Formal Definition against its source.

**What this means for you as a reader.**

- **Verify before you use.** A specific claim, a citation, a threshold number, a code snippet — if it's load-bearing for what you're doing, check it against the cited source. Don't trust the taxonomy on individual specifics until you've checked.
- **Flag errors when you spot them.** This is the most useful thing a reader can do. Feedback on factual errors is genuinely welcome — it makes the next version more accurate. Open an issue at <https://github.com/danjscho/avt-metrics-taxonomy/issues/new/choose> and pick the template that matches what you've found:
    - **Factual error or confabulation** — a specific claim, citation, threshold, or formula in a metric body looks wrong or unsupported.
    - **Tier disagreement** — a metric is at the wrong priority tier for a particular deployment context.
    - **Missing metric / gap** — an assurance question or measurement is missing from the catalogue.
    - **Broken link / dead citation / site bug** — link target is broken, cited URL is dead, or the site renders incorrectly.
    - **Framing / structural feedback** — the catalogue's principles, dimensions, or scope feel wrong-shaped.
- **Read the round-trip review files in `archive/v3.9-reviews/`.** They document the kinds of errors that have already been caught. The pattern of errors there is informative about what to look for elsewhere — if "wrong DOI" and "mis-paraphrased finding" came up multiple times in round-2, they almost certainly remain elsewhere undetected.
- **Treat the structural shape as more reliable than the specifics.** The cluster structure, the responsible-actor split, the assurance-question taxonomy, the tier-tier-tier framing — these survived multiple structural reviews. The specific metric prose, citations, and numbers are where AI-introduced errors are most likely.

The document is **not less useful** for being AI-coauthored — it covers ground that wouldn't have been covered at this scale without AI drafting. But the failure modes are distinct from a fully human-authored document, and reading it without that frame in mind is risky.

### What this is

This taxonomy is a **prototype assurance frame for Ambient Voice Technology (AVT) in NHS clinical settings**, shared openly to provoke conversation about what such a frame should look like *before* it gets settled.

It is published as a starting point for review by clinicians, IG officers, procurement leads, AVT vendors, regulators, academics, and anyone else with a stake in how AVT systems get assured at deployment. The publication strategy is deliberate: a prototype that gets read and pushed back on is more useful than a settled document that gets cited without scrutiny.

### What this is *not*

To be unambiguous about what the artefact's status implies for downstream use:

- **Not an NHS-endorsed standard.** No NHS body has reviewed, approved, or stewarded this taxonomy. The author is sharing personal work, openly, for feedback.
- **Not a regulatory document.** It is not issued or endorsed by MHRA, NHSE, ICO, CQC, NICE, or any other regulator. Where it maps to those bodies' frameworks (Standards Mapping section), it is *attempting to map onto* them, not speaking for them.
- **Not a procurement gate.** It is not a contractual minimum any vendor must meet, nor a pre-approved checklist any deployer is required to use.
- **Not a stable citation target.** Tier assignments, threshold numbers, and metric framings will change in response to feedback. The same metric may move tier, get retired, get split into sub-parts, or get reframed entirely between releases. Cite the specific version (e.g. v3.9) when referencing it; flag the prototype status in academic work.
- **Not policy.** No specific metric, threshold, or tier assignment is policy advice for any specific deployer or vendor. The Calibration & Context principle is explicit that the deployer's local context determines which metrics apply and at what threshold; this taxonomy provides a starting frame, not a contract.

### What you are invited to do

- **Flag factual errors.** Given the AI-coauthored caveat above, this is the single most useful thing a reader can do. Wrong citations, fabricated DOIs, mis-paraphrased findings, code snippets that don't run, threshold numbers that don't match the cited source — all genuinely welcome. Open an issue with what's wrong and the correct version if you have it.
- **Disagree.** The most useful response to any specific metric, threshold, or tier assignment is a reasoned objection. Open an issue, write a comment, send the author an email, raise it in a meeting.
- **Propose changes.** New metrics, sub-cluster reframings, tier promotions or demotions, thresholds that should be looser or tighter or replaced with calibration guidance, framings that miss the actual NHS context — all welcome. The roadmap (`_gaps.md`) explicitly tracks these.
- **Point at gaps.** Where AVT clinical reality is not represented in the taxonomy, that's a more important signal than where the existing metrics are imprecise. Tell the author what's missing.
- **Share with colleagues.** Send it to the IG officer, the CSO, the AVT vendor, the procurement lead. The artefact's value increases with the diversity of readers pushing back on it.
- **Ask for re-framings.** If the cluster shape, the responsible-actor split, the assurance-question taxonomy, or the priority tiers don't reflect how your team actually thinks about AVT assurance, that's a re-framing question worth raising.
- **Screenshot for slides.** With the caveat that slides should preserve the AI-coauthored prototype framing (don't crop the banner; include the version number).

### What you should not do

- **Paste threshold numbers into contracts or SLAs.** Threshold numbers in the Threshold Guidance blocks are flagged as either **cited** (externally validated, e.g. UK GDPR storage limits) or **proposed in vX.Y as starting points** (calibrated against the metric's clinical-safety logic during taxonomy authoring, but *not* externally validated). The proposed-as-starting-points numbers are explicitly conversation starters, not contractual gates. Pasting them into procurement language gives them an authority they don't have.
- **Cite metrics as authoritative in academic work without flagging the prototype status.** A paper citing "TP.SN-5 Hallucination Rate" without "[prototype-for-discussion v3.9]" risks creating the citation-loop problem the v3.9 references-validity sweep was created to address one layer up.
- **Treat any specific metric as policy.** Not for your deployment. Not for your vendor. Not for your trust. The taxonomy is calibrated against a notional reference profile (medium-volume general practice, mature governance) and most of its specifics are deployment-dependent — see the [Calibration & Context principle](#calibration-context).
- **Wait for it to settle before engaging.** The taxonomy is shared *because* feedback shapes it. Waiting for the settled version is the slower path; engaging now is the faster one.

### How the prototype evolves

- **Release cadence:** roughly monthly, larger releases with new metrics; smaller patch releases for tooling, citations, and corrections.
- **Roadmap:** see `_gaps.md` (rendered at /gaps/) for the proposed-but-not-yet-drafted metric list, classified `proposed` → `accepted` (drafted) / `deferred` (with reasoning preserved) / `rejected` (with reasoning preserved). The roadmap is shaped by reader pushback as much as by the author's pre-baked plan.
- **Plan-future:** longer-horizon items (test suites, citation-grammar reviews, threshold-numbers reviews, ISO/BSI scope, deprecation metrics) live in `plan-future.md` at the repo root.
- **Tier shifts:** a metric moves between tiers when its calibration evidence changes, when a regulatory framework is added/updated, or when reader feedback surfaces a deployment context where the prior tier doesn't fit. Each tier shift is documented in the CHANGELOG.
- **Metric retirement:** the taxonomy uses a "deprecate-don't-renumber" pattern (introduced v3.7) — retired ref-IDs are listed in `_retired-ids.md` so anyone citing an old ID can see what replaced it.
- **GitHub issues:** the formal channel for proposed changes is <https://github.com/danjscho/avt-metrics-taxonomy/issues>. Substantive proposals end up in `_gaps.md`; small corrections get applied directly.

### What "settled" would look like

The artefact will stop being a prototype-for-discussion when *some* of the following are true:

- **Substantive review** by an NHS body (NHSE digital, MHRA, NICE, CQC), an academic group, a standards organisation (BSI, ISO), or an equivalent reviewer has occurred and is documented.
- **Reader engagement evidence** has been collected — issues opened, feedback consolidated, calibration documented across multiple deployment contexts.
- **A licence is declared** (see Licence TBD note in the repo README).
- **A 1.x major release** has been cut — semantically signalling that the structure is stable enough to build on.

Until then, the prototype-for-discussion framing is load-bearing, not cosmetic. Engage with it; don't quote it.

### How to reach the author

- **GitHub issues:** <https://github.com/danjscho/avt-metrics-taxonomy/issues> (preferred for substantive proposals)
- **Email:** the author's contact details are in the repo's `pyproject.toml` and the GitHub profile

