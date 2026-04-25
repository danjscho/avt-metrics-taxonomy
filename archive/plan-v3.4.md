# v3.4 — Phase 3 Tightening + Full Tier 1 LOOSE Audit + Audit-Side Enforcement

## Context

v3.3 (just released, tag `v3.3` plus post-release Provenance clarification) introduced the Reference Standard / Operational Specification / Threshold Guidance pattern on nine Tier 1 metrics, plus the Outcomes Boundary cross-cutting file with two new ES.ME meta-metrics. The release is honest, defensible, and shippable, but a self-review identified four genuine weaknesses worth carrying explicitly into v3.4:

1. **Threshold-honesty already addressed.** The post-v3.3 follow-up added a ⚠️ Provenance prelude to every Threshold Guidance block, distinguishing cited from proposed-as-starting-points numbers. v3.4 must make this convention **machine-enforced** so it cannot drift.
2. **No programmatic tracking of which Tier 1 metrics carry the tightening pattern.** Currently CHANGELOG-tracked. Readers and contributors have no audit-time signal for which Tier 1 entries still need the pattern. Auto-tracking is overdue.
3. **The "~17 LOOSE remaining" number is a sample-extrapolation estimate.** v3.3 sampled 20 of 43 Tier 1 metrics. The full audit was deferred. v3.4 owes a complete classification with per-metric reasoning.
4. **Phase 3 four metrics owed.** GV.OP-1, HL.HF-4, IO.PX-1, GV.SG-1. Operational/proxy class — different tightening shape from safety or compliance, so the pattern gets a third stress test.

**Why now:** v3.3 is sitting on `main` and someone could pick it up to use in procurement. The Provenance prelude is currently a documentation convention enforced only by reviewer attention — the kind of convention that drifts within two releases. Promoting it to an audit check closes that loop. The Phase 3 metrics complete the original 13-metric tightening list and let us declare a coherent Tier 1 pattern is in place across all three Tier 1 use-classes (safety / compliance / operational).

**Intended outcome:** complete and audit-enforced Tier 1 tightening pattern; full classification of every Tier 1 metric (TIGHT / LOOSE / SURROGATE) with v3.5 scope auto-derived; provenance honesty machine-checked.

---

## Phase A — Audit-side enforcement (smallest, frames everything else)

### A1. Two new audit checks

Add to `taxonomy/audit.py`:

**Check 1 — `tightening-pattern-presence`:** for every Tier 1 metric, look for the three sub-block headings (`**Reference Standard**`, `**Operational Specification**`, `**Threshold Guidance**`). Either all three present or all three absent. Mixed states are an error. Output classification: `tightened` (all three present) / `not-tightened` (all three absent) / `partial` (error).

**Check 2 — `threshold-provenance-presence`:** for every metric whose state is `tightened`, the Threshold Guidance block must contain a `⚠️ **Provenance**` line within the first 200 characters of the block body. Missing Provenance line is an error.

Both checks run as informational audit output, not blockers, on first introduction. After v3.4 ships, the partial / missing states become hard errors.

### A2. Tightening-status manifest

Audit emits a section in its summary output:

```
Tier 1 tightening status:
  Tightened (13/43): TP.SN-5, TP.SN-6, TP.SN-15, HL.HF-1, TP.WB-1,
                     GV.PD-1, GV.PD-3, GV.CR-1, GV.CR-2,
                     GV.OP-1, HL.HF-4, IO.PX-1, GV.SG-1
  Not tightened (30/43): [list]
```

This becomes the auto-tracked v3.5 scope. CHANGELOG v3.4 lists the count; future releases derive scope from `dist/summary.json` rather than CHANGELOG.

### A3. parse.py extension (if needed)

If parse.py doesn't already extract sub-block boundaries from metric body text, add a minimal extractor that returns the named sub-blocks (`Reference Standard`, `Operational Specification`, `Threshold Guidance`) as parsed fields. The audit checks then operate on parsed fields rather than regex on raw markdown. Decision deferred to execution: if regex-on-raw-markdown is sufficient for the two checks, skip the parse.py change to minimise risk.

---

## Phase B — Phase 3 tightening (4 operational/proxy metrics)

These are the operational-class tightenings. Different shape from safety (TP.SN family) or compliance (GV.PD / GV.CR) — these measure deployment behaviour, not outputs.

| Ref | File | What's loose today | Tightening direction |
|---|---|---|---|
| **GV.OP-1** Documentation Time per Consultation | `taxonomy/part-e/operational.md` | "Documentation time" undefined - in-consultation only? Including review? Including after-hours? Surrogate-without-bounded-proxy-gap (proxy for clinician burden) | Reference Standard: EPR timestamp definition + after-hours boundary; Op Spec: per-clinician baseline, in-vs-out-of-consultation breakdown mandatory, paired with GV.OP-2 Pyjama Time; Threshold Guidance: trajectory-based (like Edit Rate), not absolute |
| **HL.HF-4** Time-to-Sign Distribution | `taxonomy/part-c/human-factors-workflow.md` | Distribution but no minimum / floor; "review quality" surrogate without bounded gap; doesn't address rapid-sign-without-reading | Reference Standard: timestamp from AVT note availability to clinician signature; Op Spec: floor-based (P10 / median / P90 reported; sub-30s sign as a flag); per-clinician baseline; pairs with Edit Rate to detect rapid-sign-without-edit pattern; Threshold Guidance: trajectory + floor pattern from Edit Rate |
| **IO.PX-1** Patient Opt-Out Rate | `taxonomy/part-d/patient-experience.md` | "Opt-out" definition (registration / encounter / blanket); aggregation over which population; no equity check | Reference Standard: distinguish registration-level vs per-encounter opt-out (cross-link to GV.CR-1 Patient Dissent Recording Rate); Op Spec: demographic disaggregation mandatory (a 2 % aggregate that hides 15 % opt-out among one demographic is a fairness signal not an aggregate signal); Threshold Guidance: trajectory + demographic-equity floor |
| **GV.SG-1** Model Version Tracking | `taxonomy/part-e/safety-governance.md` | Tracking what specifically — model weights / prompt template / retrieval index? Update notification timeliness undefined | Reference Standard: explicit list of versioned components (model weights, system prompt, retrieval indices, fine-tunes, safety classifier); Op Spec: per-component version recording mandatory; change-event notification timeline; Threshold Guidance: notification-latency thresholds with regulatory tie-in (EU AI Act / MHRA PMS) |

### B1. Provenance prelude on every new Threshold Guidance block

Mandatory from the outset for these four — write the Provenance line as you write the block, don't bolt it on after.

### B2. New v3.4 commitments

After Phase B lands, the count of tightened metrics is 13/43. CHANGELOG v3.4 declares this the floor and names the remaining 30 as the audit-output-driven v3.5+ pool.

---

## Phase C — Full Tier 1 LOOSE audit

For the remaining 30 Tier 1 metrics not yet tightened, run a complete classification:

- **TIGHT:** formal definition operational; vendors would compute the same value from the same data
- **LOOSE:** formal definition uses unoperationalised terms or omits reference standard / window / population
- **SURROGATE:** proxy for something else without bounded proxy gap

The v3.3 sample found 7 TIGHT, 11 LOOSE, 2 SURROGATE in 20. Full audit may shift these proportions. Output: a table in a new `archive/v3.3-tier1-classification.md` (research artefact, not user-facing) listing every Tier 1 metric with its classification + one-sentence reasoning.

This audit is the deliverable; tightening of additional metrics beyond Phase B's four is **deferred to v3.5+**. v3.4 is "audit + 4 metrics + enforcement", not a third tightening wave.

### C1. Audit method

For each Tier 1 metric not yet tightened:

1. Read the formal definition
2. Check: does it specify reference standard? Window? Population? Aggregation rule?
3. Check: are limitations / novel-thinking sections doing the work that the tightening pattern would lift?
4. Classify TIGHT / LOOSE / SURROGATE with one-sentence reason

### C2. Output document

`archive/v3.3-tier1-classification.md` — frozen snapshot at v3.4 ship date, intended as input to v3.5+ scoping.

---

## Phase D — CHANGELOG, version, release

CHANGELOG v3.4 entry covers:
- Phase A: audit-side enforcement (Provenance + tightening-status manifest)
- Phase B: 4 operational/proxy metrics tightened (GV.OP-1, HL.HF-4, IO.PX-1, GV.SG-1)
- Phase C: full Tier 1 LOOSE classification (deferred tightening to v3.5+)
- Header version bump to v3.4 / [date]

Counts unchanged: 216 metrics, 43/94/79.

---

## Branching & release

Match v3.3 pattern:
- Branch: `v3-4-phase3-and-enforcement` off `main` (current head includes the v3.3 + Provenance follow-up)
- Phase A as one commit; Phase B as one commit (or one per metric if execution surfaces friction); Phase C as one commit; CHANGELOG as final commit
- Merge with `--no-ff`, tag `v3.4`
- All commits 🦞-prefixed

---

## Critical files

**Phase A:**
- `taxonomy/audit.py` (two new checks, manifest output)
- `taxonomy/parse.py` (only if regex-on-raw is insufficient — defer decision)

**Phase B:**
- `taxonomy/part-e/operational.md` (GV.OP-1)
- `taxonomy/part-c/human-factors-workflow.md` (HL.HF-4)
- `taxonomy/part-d/patient-experience.md` (IO.PX-1)
- `taxonomy/part-e/safety-governance.md` (GV.SG-1)

**Phase C:**
- `archive/v3.3-tier1-classification.md` (new research artefact)

**Release:**
- `CHANGELOG.md` (v3.4 entry)
- `taxonomy/_header.md` (version bump)
- `taxonomy/_how-to-use.md` (update tightened-metric count from 9 to 13)

---

## Functions & utilities to reuse

- `taxonomy/parse.py` — extract Tier 1 metrics; existing logic returns metric body, sufficient for sub-block detection via regex
- `taxonomy/audit.py` — existing structural checks; the new checks fit alongside cleanly
- `taxonomy/build.py` — no change

---

## Verification

1. **Audit clean:** `python3 taxonomy/audit.py` — zero findings, plus new manifest section showing 13/43 tightened with the four new metric IDs included
2. **Build clean:** 216 metrics, tier split unchanged, 20 groups
3. **Provenance enforcement:** intentionally remove a ⚠️ Provenance prelude from one tightened metric, confirm audit flags it; restore
4. **Phase 3 metrics readable cold:** read GV.OP-1 cold and answer six vendor-comparability questions about documentation time (in/out of consultation, after-hours boundary, baseline, demographic stratification, escalation triggers)
5. **Classification document complete:** every Tier 1 metric not tightened in v3.4 appears in `archive/v3.3-tier1-classification.md` with TIGHT / LOOSE / SURROGATE label and one-sentence reasoning
6. **CHANGELOG v3.4** explicitly names: Provenance audit check is now hard-error; tightened-metric count 13/43; v3.5+ scope auto-derived from audit output
