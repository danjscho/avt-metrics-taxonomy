# Methodology: Building a Healthcare-AI Assurance Taxonomy

A reusable recipe for constructing, maintaining, and publishing an assurance-metrics taxonomy for any healthcare-AI system class (ambient voice, triage / access / navigation, clinical-decision support, voice-AI agents, decentralised multi-agent healthcare systems, clinical imaging AI, etc.).

This document describes the process and artefacts, not the AVT content itself. Everywhere you see `<SYSTEM>` or `<SYSTEM-ABBR>` substitute your own system class (e.g. "AI Triage, Access & Navigation" / `TAN`).

---

## 1. What this methodology produces

A set of interlocking artefacts, not a single document:

| Artefact | Purpose |
|---|---|
| **Metric catalogue** | Every measurable assurance property of the system, scoped by pipeline layer and cross-cutting axes |
| **Applicability classification** | For each metric, whether it's `<SYSTEM>`-specific, `<SYSTEM>`-contextualised, or general healthcare AI - tells adopters what's portable |
| **Standards mapping** | Per-metric cross-reference to every regulatory / professional standard the system must meet |
| **Responsible-AI lens** | Separate view: how metrics map to policy / ethical principles (DSIT Playbook, ethical themes) |
| **Tiered assurance ladder** | Tier 1 = minimum viable assurance; Tier 2 = recommended; Tier 3 = advanced/aspirational |
| **Gap register** | Candidate metrics not yet specified, with their origin (standard, principle, theme) and status |
| **Stable reference IDs** | `{Part}.{Group}-{Number}` - citable, permanent, survives renames |
| **Automated audit** | Script that verifies internal consistency of the whole corpus |
| **Buildable output** | Single assembled document for offline/archival use, plus derived machine-readable formats (CSV, JSON) and a public website |

The whole thing is **pure Markdown** in the source of truth. Structured data (CSV, JSON, site, PDF) is *derived*, never authored twice.

---

## 2. Core design principles

These drove every structural decision. Copy them first; the rest follows.

1. **Single source of truth** - every fact appears in exactly one file. Any other view (PDF, CSV, standard-specific page, site navigation) is generated.
2. **Additive change only once published** - never rename or delete a published metric. Deprecate + supersede. Reference IDs are a durable citation contract.
3. **Each metric is a full atomic unit** - a name, a formal definition, limitations, its dimensions table, and (where possible) operational measurement code. A metric that can't be measured isn't a metric yet - it's a gap.
4. **Separate the "what" from the "why it matters"** - metric definitions live in content files; standards mappings and ethical lenses are parallel cross-cutting layers.
5. **Tier on actionability, not importance** - Tier 1 is "every adopter must do this now, with existing tools". Importance alone doesn't justify Tier 1 if the instrumentation doesn't yet exist.
6. **Make gaps first-class** - unknowns, underspecified metrics, and proposed-but-not-yet-written metrics get explicit first-class representation. Silence is worse than "TODO: see gap register".
7. **Automate invariants** - the cost of a drift bug (e.g. Tier 1 reference listing a metric that's since been reclassified) is paid months later by readers. Write the audit script first, fix once, re-run forever.
8. **Derive what you can, author what you must** - frontmatter/YAML/tags are tempting but rot. If the information is already in a structured table in prose, parse the table.

---

## 3. Structural model

Six layers. Start with these; specialise inside them.

### 3.1 Parts

A **part** is a top-level division of the system's concerns. Keep them stable once chosen - they become reference-ID prefixes (`TP`, `PI`, `GV` …). A reasonable generic split:

- **Technical Pipeline** - the system's computational stages (input → processing → output)
- **Pipeline Interactions** - partial + end-to-end cross-stage behaviours
- **Human Layer** - clinician workflow, handover, oversight, automation bias
- **Impact & Outcomes** - patients, populations, fairness, equity
- **System Governance** - safety, compliance, security, privacy, operations, sustainability, training, vendor transparency
- **Evaluation Science** - how we know our measurements themselves are valid (meta-evaluation)

For very different system classes the names change (e.g. for multi-agent healthcare systems you'd add "Inter-Agent Coordination" as a technical-pipeline subdivision, or as its own part).

### 3.2 Groups

A **group** is a cohesive cluster of metrics inside a part. Typical size: 5–25 metrics. Groups become the unit of file organisation and (later) the unit of web pagination.

### 3.3 Metrics

Each metric is the atomic unit. Every metric has:

- **Reference ID** (`{Part}.{Group}-{Number}`) - both in the heading and in the dimensions table. Never reused.
- **Tier icon** in the heading - visual marker, also in the dimensions table.
- **Dimensions table** - the 8 canonical axes (below).
- **"Why this tier?"** block - one-sentence rationale.
- **Formal Definition** block - mathematical or operational definition, precise enough to implement.
- **Limitations** - known failure modes of the metric itself.
- **Novel Thinking / Implications** (optional) - editorial expansion.
- **Code** (optional) - reference implementation, illustrative not authoritative.

### 3.4 Cross-cutting axes (the dimensions table)

Every metric carries these eight dimensions - they define the shape of the metric space and enable faceting:

1. **Priority Tier** - 1 (minimum viable) / 2 (recommended) / 3 (advanced)
2. **Measurement Cadence** - gate (pre-deployment) / continuous / audit (periodic)
3. **Pipeline Layer** - which stage of the system is under scrutiny
4. **Assurance Question** - the deeper question being answered (fidelity, safety, fairness, usability, compliance, …)
5. **Measurement Method** - computational / human-in-the-loop / patient-reported / clinical-audit / operational-telemetry
6. **Lifecycle Phase** - pre-deployment, post-deployment, continuous, decommissioning
7. **Responsible Actor** - vendor / deployer / regional body / national body / academic / regulator
8. **Maturity** - established / emerging / vendor-proprietary / proposed

Plus a **Reference** row carrying the ID, and an optional **Outcome Type** (proximal / distal) where relevant.

### 3.5 Metric families and sub-clusters

Two kinds of thematic grouping *within* the metric layer - distinct mechanisms:

- **Named metric families** - parent-construct groupings that may span multiple groups. A family has a structured block-quote framing at the first member's appearance. Use when 3+ metrics share a common conceptual parent (e.g. "Clinical Content Fidelity" spans hallucination + omission + negation + certainty inflation).
- **Sub-clusters** - thematic groupings inside a single group. A sub-cluster has an italic 1–2 sentence intro paragraph. Use when a group is large enough to benefit from internal topology.

Don't invent other grouping primitives - two is enough.

### 3.6 Cross-cutting content files

Prefix these with underscore (`_`) to sort them above group files in directory listings and to distinguish "about the whole taxonomy" from "content":

- `_header.md` - title, metric count, preamble
- `_how-to-use.md` - tier definitions, cadence, actors, reference-ID legend
- `_summary.md` - tier breakdown, maturity breakdown, family list
- `_tier-1-quick-reference.md` - actor-organised Tier 1 view (auto-generatable)
- `_contents.md` - table of contents with per-group metric counts and family annotations
- `_applicability.md` - `<SYSTEM>`-specific / `<SYSTEM>`-contextualised / general classification
- `_standards-mapping.md` - assertion-level mapping to every relevant standard
- `_responsible-ai-lens.md` - policy/principle/theme mapping

---

## 4. Phased construction process

This is the order in which to build it. Each phase produces something shippable.

### Phase 0 - Scoping (1–2 days)

- Define the system class precisely. One paragraph, no hedging.
- Decide the parts (usually 5–7). Lock these before writing anything - they're the reference-ID prefixes.
- Decide the group abbreviations (2–3 letters each). Write them into `_how-to-use.md` as the legend from day one.
- Write `_header.md` with a placeholder metric count.

### Phase 1 - Metric seeding (2–4 weeks)

- Brainstorm groups within each part. Aim for ~20 groups total; don't sub-divide prematurely.
- For each group, draft 5–15 metrics. A first pass should be exhaustive and messy; cull later.
- For each metric, fill in:
  - Name, reference ID, tier (first-pass guess - revisit)
  - Full dimensions table
  - Formal definition (even if provisional; better to have a wrong definition to critique than none)
  - Limitations
- Don't write code yet. Don't worry about consistency yet.

### Phase 2 - Consistency pass

- Build the audit script. See `taxonomy/audit.py` in this repo for a reference implementation. Minimum checks:
  - Reference-ID prefix matches group file
  - Heading tier icon matches dimensions-table tier
  - Dimensions table complete on every metric
  - Tier totals reconcile with `_summary.md`
  - Internal cross-references (`See also: X`) resolve to a known metric name
- Fix everything it finds. Do not skip warnings - they compound.
- Tag a v1.0 at this point. Reference IDs from v1.0 onward are a contract.

### Phase 3 - Enrichment layers

Add the cross-cutting files *after* the metric catalogue stabilises:

1. **Applicability** - walk every metric; classify as system-specific / contextualised / general. Build a summary table per part, then per group. This is also a cull-or-promote signal: metrics that are hard to classify often aren't well-defined.
2. **Families + sub-clusters** - only now identify the semantic groupings. Writing framings forces you to articulate what the family is *for*, which sometimes reveals that the family is spurious.
3. **Underspecification warnings** - flag metrics where the field doesn't yet have consensus. These are often more valuable than well-specified metrics because they signal where assurance effort should go.
4. **Standards mapping** - this is the longest file. Structure: one section per standard, with assertion-level mapping to metric IDs. Gaps fall out naturally ("standard X requires Y; no metric covers Y").
5. **Responsible-AI lens** - parallel view. Map metrics to principles (e.g. DSIT Playbook 10 principles) and ethical themes (your own set of 4–8). Produces a second, independent gap analysis.

### Phase 4 - Gap consolidation

After enrichment, you'll have two or more scattered gap lists. Unify into a single `gaps.yaml` or `gaps.md`:

```yaml
- id: GAP-STD-001
  origin: standards     # or: rai-principle, rai-theme, expert-review
  status: proposed      # proposed / accepted / deferred / rejected
  proposed_metric_name: ...
  related_standards: [STD.Assertion-4]
  related_principles: [accountability]
  rationale: ...
```

This becomes the public roadmap. Every new metric round draws from here.

### Phase 5 - Validation against external sources

Cross-check against what the field already has:

- Find every existing taxonomy, guidance document, framework, or standard for your system class.
- Build a coverage matrix: external concept → your metric ID (or `GAP`).
- Add missing concepts as either new metrics (if well-specified) or new gap entries (if not).

**This is how you avoid reinventing the wheel.** If a policy body has already articulated a concern, cite them and map to them - don't paraphrase.

### Phase 6 - Publish

Two outputs, one source:

- **Monolithic document** (Markdown → optional PDF) - archival, offline, citable.
- **Website** (MkDocs Material recommended; Docusaurus if you need heavy React). Pages:
  - Home / how-to-use / quick start (Tier 1)
  - 20 group pages (one per group)
  - Per-standard coverage pages (generated)
  - Per-principle / per-theme pages (generated)
  - Applicability views (generated)
  - Roadmap (from unified gaps file)
  - Downloads (full MD, PDF, CSV, JSON)
  - Changelog / versions

Stable URL contract: metric anchors are lowercase reference IDs (`#tp-ac-1`), **not** slugs of the metric name. Names can rename; IDs can't.

---

## 5. Build-system pattern

```
<repo-root>/
  <system>-metrics-taxonomy.md          # built monolithic output
  CHANGELOG.md
  METHODOLOGY.md
  taxonomy/
    _header.md
    _how-to-use.md
    _summary.md
    _tier-1-quick-reference.md           # auto-generated in later versions
    _contents.md
    _applicability.md
    _standards-mapping.md
    _responsible-ai-lens.md
    part-a/ part-b/ part-c/ …            # one directory per part, one .md per group
    build.py                             # concatenates source → monolithic MD
    audit.py                             # verifies invariants
    parse.py                             # (later) shared parser used by build + site
    build_site.py                        # (later) emits MkDocs content + CSV + JSON
  archive/                               # versioned input artefacts, superseded drafts
  .github/workflows/                     # CI: audit → build → site → deploy
```

Key properties:

- **Idempotent builds** - running `build.py` twice produces byte-identical output.
- **Explicit file order** in `build.py` - not alphabetical, because pipeline order is editorial.
- **Audit gates the build** - CI fails if audit finds errors, so drift can't ship.

---

## 6. Governance conventions

Adopt these early; they save merge pain later:

- **Commit prefix** - pick one character/emoji and use it on every commit. Makes the git log legible at a glance. This repo uses 🦞.
- **Additive-only policy for published metrics** - written into CLAUDE.md / CONTRIBUTING.md. No renames, no deletions, no reordering of existing sections once a version is tagged.
- **Locked decisions list** - decisions that recur (e.g. "is X a sub-cluster or a family?") get codified in CLAUDE.md. Don't re-litigate them.
- **"When to stop and ask"** - explicit list of situations where an automated pass should halt rather than guess (e.g. "final metric count disagrees with declared count" → stop, ask human).
- **Version strategy** - semver-ish. Major bump on structural changes (new part, new grouping primitive). Minor bump on additive content rounds. Patch bump for corrections.
- **Review gates between phases** - a "batch" PR should not also include cross-cutting renames. Gate-1: content. Gate-2: cross-cuts. Gate-3: meta.

---

## 7. Porting this to a new system class

Checklist for starting a new taxonomy from this template:

- [ ] Pick system name + short name (`<SYSTEM>` / `<SYSTEM-ABBR>`)
- [ ] Fork or scaffold the repo structure above
- [ ] Write a 1-page scope doc: what's in, what's out, what neighbouring classes it touches
- [ ] Decide the parts (aim for 5–7). Lock them.
- [ ] Decide the groups inside each part (aim for ~20 total). Lock the 2–3-letter abbreviations.
- [ ] Draft the `_how-to-use.md` tier definitions. Don't copy AVT tiers verbatim; the thresholds for "minimum viable" depend on the system class.
- [ ] Build the audit script before writing any metrics. Yes, really.
- [ ] Phase 1: seed metrics. Aim for ~150. Expect 20% to be culled.
- [ ] Phase 2: audit-clean, tag v1.0.
- [ ] Phase 3: layer on applicability, families, standards, RAI lens.
- [ ] Phase 4: unify gaps.
- [ ] Phase 5: external-source validation pass.
- [ ] Phase 6: site + publish.

---

## 8. What not to do

Hard-won lessons from this project:

- **Don't start with the website.** Content structure first; presentation is derived. Every hour spent on the site before the metric catalogue is stable is re-work.
- **Don't add YAML frontmatter speculatively.** If the information is already in a structured table in prose, parse the table. Frontmatter rots; prose tables are reviewed every time a human edits the metric.
- **Don't invent a new grouping primitive every time something feels "different".** Two primitives (families, sub-clusters) cover every real case we've encountered across 200+ metrics. (As of v5.5.x in the AVT instance: 8 named families, ~10 sub-clusters across 236 metrics.)
- **Don't treat Tier 1 as "the important ones".** Tier 1 means "measurable today with existing tools and consensus definitions". A profoundly important metric with no agreed-upon definition is Tier 2 or 3 with a gap flag, not Tier 1.
- **Don't conflate the taxonomy with the implementation guide.** This produces the *what* to measure and roughly *how*; it does not produce local clinical SOPs, vendor-specific test plans, or DPIAs. Keep those downstream.
- **Don't let gaps drift into multiple files.** Unify them, or they will contradict each other within a year.
- **Don't skip the audit script.** It pays for itself the first time someone changes a tier in one place and forgets the summary.

---

## 9. Artefact templates

Minimum viable starter files for a new taxonomy. Copy from the existing `taxonomy/` directory and substitute.

### Metric skeleton

```markdown
### <ID> <ICON> <Metric Name>

<One-paragraph description of what the metric measures and why it matters.>

| Dimension | Value |
|-----------|-------|
| **Reference** | <ID> |
| **Priority Tier** | <🟢/🟡/🔵> Tier <1/2/3> - <label> |
| **Measurement Cadence** | <Gate / Continuous / Audit> |
| **Pipeline Layer** | <layer name> |
| **Assurance Question** | <fidelity / safety / fairness / …> |
| **Measurement Method** | <Computational / Audit / Patient-reported / …> |
| **Lifecycle Phases** | <Pre-deployment, Continuous, …> |
| **Responsible Actors** | <Vendor, Deployer, …> |
| **Maturity** | <Established / Emerging / Proposed> |
| **Outcome Type** | <Proximal / Distal>           (optional)
| **Source** | <citation / origin>               (optional)

**Why this tier?**

> <One sentence.>

**Formal Definition**

```
<Precise operational or mathematical definition.>
```

**Limitations**

> <Known failure modes of the metric itself.>
```

### Group-file skeleton

```markdown
# Part X - <Part Name>

## <Group Name>

*<Italic 1–2 sentence framing of what this group covers and why it's a group.>*

**Tier breakdown**: 🟢 <n> Tier 1 · 🟡 <n> Tier 2 · 🔵 <n> Tier 3

<metric 1>
---
<metric 2>
---
…
```

### Audit-script invariants (minimum set)

Replicate these for any new system class (see `taxonomy/audit.py`):

1. Every metric heading has a matching **Reference** row.
2. Reference ID is unique across the corpus.
3. Reference-ID prefix matches group file.
4. Heading tier icon matches dimensions-table tier value.
5. Tier totals match `_summary.md` declarations.
6. Every required dimension present on every metric.
7. Every "See also" name resolves to a known metric.
8. `_applicability.md` counts sum to total metric count.
9. Every metric in `_tier-1-quick-reference.md` exists and is still Tier 1.

---

## 10. Attribution

This methodology was distilled from constructing the AVT Metrics Taxonomy (236 metrics, 20 groups, 13 mapped standards as of v5.5.x). The patterns survived through major additive rounds (v1.0 → v2.0 first major extension; v3.x tier-1 tightening waves; v4.0 cluster-code restructure; v5.x Phase-5 minimum-set extension) without structural rewrite — that's the strongest evidence they work. The concrete files referenced above (`audit.py`, `build.py`, `_applicability.md`, `_standards-mapping.md`, `_responsible-ai-lens.md`) exist in this repo as worked examples.

Several primitives accumulated since the original methodology was written and now form part of the recipe:

- **Per-metric `Family`** (v5.4.0): named cross-construct groupings as an audit-enforced dimension; canonical home in `_families.md` rather than scattered cluster-file framings.
- **Layers of Defence** (v5.4.0): Prevention / Detection / Limitation as a per-metric explicit dimension. Names the architectural shape rather than leaving readers to derive it.
- **AI-Substrate classification** (v5.5.0+): five-class derived cut surfacing which metrics test the AI itself vs the infrastructure around it vs the governance of it.
- **Failure Pathways** (v5.5.1): worked failure-mode archetypes plus a day-by-day timeline showing how the taxonomy operates in motion. Complements the architectural framing with scenario framing.
- **Threshold Reference structural split** (v5.0.0): numerical thresholds live on a dedicated reference page, freeing metric bodies for qualitative Trigger Conditions.

These are recipe extensions, not replacements — the original primitives remain load-bearing.

When adapting, cite this repo as the methodology source and your own work as the content; the structure is transferable, the metric choices are not.
