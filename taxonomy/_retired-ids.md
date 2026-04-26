# Retired Metric IDs

This registry records every reference ID that was used in a prior taxonomy version and has subsequently been retired. Retired IDs are not reused — every prior taxonomy version, the standards-mapping file, classification artefacts, duplication review, and external citations may reference them, and renumbering would silently break those references.

When a metric is retired, its content is preserved either as a sub-part of a new parent metric (Phase 2.1 redundancy resolution) or as a folded body absorbed into another metric (Phase 2.3 US-flavour resolution). The redirect note records where the content went.

The audit (`taxonomy/audit.py`) reads this registry. The `check_numbering` check tolerates integer gaps in a group's metric numbering iff the gap ID appears here. Any retired ID referenced from elsewhere in the taxonomy without an existing redirect target produces an audit warning.

## Format

| Retired ID | Retired in | Redirect target | Reason |
|---|---|---|---|

(no entries pre-v3.7)

## v3.7 retirements

| Retired ID | Retired in | Redirect target | Reason |
|---|---|---|---|
| TP.SN-8 | v3.7 (Phase 2.1) | TP.SN-7b | Folded as sub-part under new parent **TP.SN-7 Factual Verification**. TP.SN-8 (VeriFact Factual Verification) and previous TP.SN-7 (Confabulation Detection) measured the same construct (factual support) using different instruments; v3.6 duplication review flagged as redundant. Now TP.SN-7a (Confabulation Detection) and TP.SN-7b (VeriFact Factual Verification) under parent TP.SN-7. |
| TP.SN-10 | v3.7 (Phase 2.1) | TP.SN-9b | Folded as sub-part under new parent **TP.SN-9 LLM-Judge Methodology**. TP.SN-10 (MedHELM LLM-Jury) and previous TP.SN-9 (LLM-as-a-Judge / PDSQI-9 Proxy) measured the same construct (LLM-judge evaluation) at different ensemble configurations; v3.6 duplication review flagged as redundant. Now TP.SN-9a (LLM-as-a-Judge) and TP.SN-9b (MedHELM LLM-Jury) under parent TP.SN-9. |
| HL.HF-4 | v3.7 (Phase 2.1) | HL.HF-3b | Folded as sub-part under new parent **HL.HF-3 Inadequate-Review Detection**. HL.HF-4 (Time-to-Sign Distribution) and previous HL.HF-3 (Review-Before-Signing Rate) both detect inadequate clinician review; v3.6 duplication review flagged as redundant; v3.4 already mandated pairing. Now HL.HF-3a (Review-Before-Signing Rate) and HL.HF-3b (Time-to-Sign Distribution) under parent HL.HF-3. HL.HF-3b retains its v3.4 tightening pattern. |
| TP.CC-8 | v3.7 (Phase 2.3) | TP.CC-7 | Folded into TP.CC-7 (renamed *Coding Drift Detection — UK Framing*). TP.CC-8 (E/M Level Shift Monitoring) was a US-specific specialisation of TP.CC-7's SPC-based drift detection; the v3.6 duplication review and v3.7 US-flavour audit identified the overlap. KL-divergence and demographic-disaggregation content from TP.CC-8 absorbed into TP.CC-7's Operational Specification; E/M coding called out as US analogue. |

## Convention

- **Don't reuse retired IDs.** A new metric in the same group takes the next free integer (or sub-part suffix), never a retired-ID slot.
- **Don't renumber surviving metrics around retirements.** The integer sequence carries gaps; the audit tolerates them.
- **Cross-references to retired IDs** are flagged by the audit and should be updated to the redirect target. The registry above is the authoritative redirect map.
- **External citations** to retired IDs remain valid (this registry tells future readers where the content went).

---
