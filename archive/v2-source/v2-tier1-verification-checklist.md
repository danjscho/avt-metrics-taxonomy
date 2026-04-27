# Tier 1 Verification Checklist

10 new Tier 1 metrics were added in v2. Verify all are present in the batch files and land in the correct target sections during integration.

## Quick check

```bash
grep "### 🟢" avt-new-metrics-batch-*.md
```

Expected: 10 hits (1 from batch-1, 0 from batch-2, 7 from batch-3, 2 from batch-4).

## Metric locations

| Metric | Source file | Target section |
|---|---|---|
| Code Hallucination Rate | batch-1 | Clinical Coding |
| Patient Dissent Recording Rate | batch-3 | NHS Compliance & Regulatory |
| Verbal Notification Compliance | batch-3 | NHS Compliance & Regulatory |
| AI-Generated Content Labelling Compliance | batch-3 | NHS Compliance & Regulatory |
| AVT Supplier Registry Listing Verification | batch-3 | NHS Compliance & Regulatory |
| ICB Engagement Documentation | batch-3 | NHS Compliance & Regulatory |
| Clinical Safety Case Completeness | batch-3 | NHS Compliance & Regulatory |
| DPIA Template Completion Rate | batch-3 | NHS Compliance & Regulatory |
| Audio Time-to-Deletion | batch-4 | Privacy & Data Governance |
| Transcript Retention Compliance | batch-4 | Privacy & Data Governance |

## Count correction

plan.md says "Tier 1 count is 42". Correct value is **43** (33 original + 10 new). Update the success criteria in plan.md accordingly. Have Claude Code recount all three tiers from the assembled document at Review Gate 3 rather than trusting pre-specified numbers.

## Standalone reference

The full text of all 10 metrics is also available in `avt-new-tier-1-metrics.md` as a standalone document if needed for cross-checking content during integration.