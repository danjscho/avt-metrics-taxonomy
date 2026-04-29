# v3.9 Phase 2 URL review — FILLED DRAFT (Claude pass)

This is Claude's first pass at filling in the review. **Treat every annotation as a proposal, not a fact** — I've kept the same `[ ]` / `[✓]` / `[!]` / `[?]` / `[skip]` / `[+desc]` / `[handle: ...]` vocabulary you set out, plus a brief `Source:` note under each one explaining how I got there so you can audit me cheaply.

**Bottom line for the impatient:**
- **A (5)**: All 5 verified ✓. One `[+desc]` flag (A1: handle says 2025, v2 was March 2026) and one alternative URL suggestion (A5: JMIR canonical preferred over PubMed).
- **B (11 active)**: 10 ✓ as asserted. **One real find: B8 NIHR-RSET — Dan's `bsms.ac.uk` URL is wrong**, the team is UCL/Nuffield Trust/Cambridge. Suggested replacement.
- **C (44)**: ~16 confidently resolved with verified URLs, ~14 with strong candidate URLs marked `[?]`, ~10 left as genuine `[?]` with notes on what I tried. Two cross-link discoveries: **CREOLA = Asgari (C-uncertain-1 collapses into C-papers-2)**, and **MedHELM paper = Bedi (B9 paper = C-papers-4)**.
- **D (8)**: Option 3 hybrid applied — 4 keeps (D2, D3, D5, D8 rescoped), 1 new specific entry (Carlini-2024 web-scale poisoning, carved out of D5), 4 drops with grouping-level replacement prose drafted (D1, D4, D6, D7). Net: 8 → 5 entries.

---

## A. URL extracted from prose (4 entries → 5 incl. A5)

### A1. Hybrid-Code-v2-2025
- URL: https://arxiv.org/abs/2512.23743
- [✓] [+desc]
- **Source:** Verified by web search. Paper is "Hybrid-Code v2: Zero-Hallucination Clinical ICD-10 Coding via Neuro-Symbolic Verification and Automated Knowledge Base Expansion" by Yunguo Yu (Zyter|TruCare). v1 submitted Dec 26, 2025; v2 ("Hybrid-Code v2" rename) submitted March 23, 2026.
- **+desc note:** Handle says `Hybrid-Code-v2-2025` but v2 was published March 2026 — the v1 (different title, "A Privacy-Preserving, Redundant Multi-Agent Framework for Reliable Local Clinical Coding") was the December 2025 release. Consider `Hybrid-Code-v2-2026` or `Yu-Hybrid-Code-2026`.

### A2. Jegham-AI-Hunger-2025
- URL: https://arxiv.org/abs/2505.09598
- [✓]
- **Source:** Verified. Title "How Hungry is AI? Benchmarking Energy, Water, and Carbon Footprint of LLM Inference", Jegham/Abdelatti/Koh/Elmoubarki/Hendawi, May 2025, currently on v6 (Nov 2025). DOI 10.48550/arXiv.2505.09598.

### A3. npj-DM-AI-Coding-Drift-2025
- URL: https://www.nature.com/articles/s41746-025-02272-z
- [✓]
- **Source:** Verified. Title "Policy brief: ambient AI scribes and the coding arms race", npj Digital Medicine, Dec 2025. Matches the framing as a coding-drift / arms-race policy brief.

### A4. arXiv-2601-03791-Cue-Resistant-Memorisation
- URL: https://arxiv.org/abs/2601.03791
- [✓] [+desc]
- **Source:** Verified. Full title "Do LLMs Really Memorize Personally Identifiable Information? Revisiting PII Leakage with a Cue-Controlled Memorization Framework", Luo/Chen/Li/Bjerva, submitted Jan 7, 2026. CRM is the framework name within the paper.
- **+desc note:** If you want a more informative title in the catalogue, the PII-leakage framing is more recognisable than "cue-resistant memorisation" alone. Suggested handle: `Luo-PII-CRM-2026`.

### A5. PubMed-41172285-FOI-Study
- URL: https://pubmed.ncbi.nlm.nih.gov/41172285/
- [✓] [+desc] — alternative URL preferred
- **Source:** Verified. Paper is Roy-Highley et al. (UCL), "Digital Health Technology Compliance With Clinical Safety Standards In the National Health Service in England: National Cross-Sectional Study", JMIR 2025;e80076. The PubMed URL works but the JMIR canonical is fuller and open access:
- **Suggested swap:** https://www.jmir.org/2025/1/e80076
- Title amendment if relevant: full title above; key finding is that 70.1% of NHS DHTs have no documented assurance against DCB0129/DCB0160.

### A6. Wang-ADS-Eval-2025 — **CORRECTNESS AUDIT (added 2026-04-29)**
- URL: https://www.nature.com/articles/s41746-025-01622-1
- **Title:** *An evaluation framework for ambient digital scribing tools in clinical applications*
- **Cite:** Wang et al., *npj Digital Medicine* 2025; 8:358 (online 2025-06-13). DOI `10.1038/s41746-025-01622-1`.
- **Acronym in paper:** **ADS** (Ambient Digital Scribing). Paper does use "SCRIBE" in diagram.
- **Findings (verified 2026-04-29 via Nature citation metadata):**
  - **E1 — Wrong DOI on every inline link.** All three "Wang et al." links currently point to `s41746-025-01449-w`, which is an unrelated meta-analysis on cognitive interventions for anxiety/depression (Richter et al.). Affected: [taxonomy/part-a/diarisation.md:46](taxonomy/part-a/diarisation.md#L46), [diarisation.md:89](taxonomy/part-a/diarisation.md#L89), [taxonomy/part-a/summarisation-nlp.md:801](taxonomy/part-a/summarisation-nlp.md#L801).
  - **E2 — "SCRIBE" acronym is Simulation, Computational metrics, Reviewer assessment, and Intelligent Evaluations for Best practice to provide a comprehensive evaluation** so should be updated.
  - **E3 — "Two distinct Wangs" entry is a phantom.** [taxonomy/_references.md:621-633](taxonomy/_references.md#L621-L633) treats `Wang-Duke-MedStar-2025` as a separate paper queued for follow-up. It's the same paper — see **C-papers-6** above.
  - **E4 — TP.SN-13 "all four must pass" composite is taxonomy embellishment.** [summarisation-nlp.md:793-796](taxonomy/part-a/summarisation-nlp.md#L793-L796) frames the four-modality framework as a hard pass/fail composite. The four modalities (human, automated, simulation, LLM-as-evaluator) are real; the all-must-pass composite is not in the paper.
- **Agreed remediation (decision 2026-04-29 — apply during Phase 2 sweep, not now):**
  - Rename anchor `SCRIBE-Wang-2025` → `Wang-ADS-Eval-2025` in [taxonomy/_references.md](taxonomy/_references.md). Replace title/publisher/URL with the verified values above; drop the SCRIBE expansion.
  - Delete the `Wang-Duke-MedStar-2025` entry at [_references.md:621-633](taxonomy/_references.md#L621-L633).
  - Fix the DOI in all three inline links (`01449-w` → `01622-1`).
  - Update Source-row references in [diarisation.md:18](taxonomy/part-a/diarisation.md#L18), [diarisation.md:75](taxonomy/part-a/diarisation.md#L75), [summarisation-nlp.md:787](taxonomy/part-a/summarisation-nlp.md#L787), [asr-transcription.md:18](taxonomy/part-a/asr-transcription.md#L18) to the unified anchor.
  - Soften TP.SN-13 Formal Definition at [summarisation-nlp.md:793-796](taxonomy/part-a/summarisation-nlp.md#L793-L796) to distinguish what the paper proposes (four-modality triangulation) from the taxonomy's interpretation (recommended pre-deployment composite).
- **Verification on Phase 2 execution:** `grep -rn "01449-w" taxonomy/` returns zero; `grep -rn "SCRIBE" taxonomy/` returns zero; `grep -rn "Wang-Duke-MedStar-2025" taxonomy/` returns zero; `python taxonomy/build.py` clean; `audit.py` shows no broken cross-references.

---

## B. Canonical-landing-page URLs (12 entries)

### B1. WHO-ICD-11
- URL: https://icd.who.int/
- [✓]
- **Source:** Verified — canonical WHO landing for ICD-11. Live ICD-11 browser at `icd.who.int/browse11` if you ever need a deeper link.

### B2. NASA-TLX
- URL: https://humansystems.arc.nasa.gov/groups/tlx/
- [✓] (alternative noted)
- **Source:** Verified — the NASA Ames TLX programme page is live. There's a more polished landing at `https://www.nasa.gov/human-systems-integration-division/nasa-task-load-index-tlx/` if you ever want to swap to the nasa.gov-domain version (more citation-stable than the subdomain), but yours works.

### B3. EU-AI-Act
- URL: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- [✓]
- **Source:** Verified — the language-neutral ELI URL resolves to the consolidated text. The English-only version is `/oj/eng` if you ever want to be specific.

### B4. OWASP-LLM-Top-10
- URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- [✓] (alternative noted)
- **Source:** Verified. The project has effectively migrated to `https://genai.owasp.org/llm-top-10/` (the GenAI Security Project umbrella) which is the newer canonical and where 2025 updates live. The owasp.org URL still resolves and links forward. Either is defensible; flag if you'd prefer the newer one.

### B5. NIST-Privacy-Framework
- URL: https://www.nist.gov/privacy-framework
- [✓]
- **Source:** Verified. Note v1.1 is in development (initial public draft as of 2025), parked under `https://www.nist.gov/privacy-framework/new-projects/privacy-framework-version-11` if you ever want to cite the in-progress update specifically.

### B6. Schrems-II
- URL: https://curia.europa.eu/juris/liste.jsf?num=C-311/18
- [✓]
- **Source:** Verified — case-list page resolves to the C-311/18 case. If you ever want the judgment document directly, it's `https://curia.europa.eu/juris/document/document.jsf?docid=204046&doclang=EN`.

### B7. Shumailov-Curse-of-Recursion
- URL: https://www.nature.com/articles/s41586-024-07566-y
- [✓]
- **Source:** Verified. Shumailov/Shumaylov/Zhao/Papernot/Anderson/Gal, Nature 631:755–759 (2024), "AI models collapse when trained on recursively generated data". Note there's a 2025 Author Correction at `s41586-025-08905-3` if it ever matters. The 2023 arxiv preprint (2305.17493) under the original "Curse of Recursion" title is also live; pick whichever framing your text uses.

### B8. NIHR-RSET — **CORRECTION NEEDED**
- ~~URL: https://www.bsms.ac.uk/research/centres-and-units/rapid-service-evaluation-team/index.aspx~~
- [!] https://www.nuffieldtrust.org.uk/rset-the-rapid-service-evaluation-team
- **Source:** Verified — Brighton & Sussex Medical School isn't part of NIHR RSET. The team is a UCL / Nuffield Trust / University of Cambridge collaboration (Phase 1: 2018–23, with UCL+Nuffield Trust; Phase 2: 2023+, adding Cambridge). If needing a link to the phase 1 AVT trial specifically - https://www.nuffieldtrust.org.uk/research/mixed-method-evaluation-of-ambient-voice-technology-phase-1

### B9. MedHELM
- URL: https://crfm.stanford.edu/helm/medhelm/latest/
- [✓]
- **Source:** Verified — Stanford CRFM MedHELM leaderboard landing.
- **Cross-link finding:** The MedHELM paper itself is **Bedi et al., arXiv 2505.23802** (May 2025), which is exactly your `C-papers-4. Bedi-Stanford-CRFM-2025` entry. So C-papers-4 maps to URL `https://arxiv.org/abs/2505.23802` and is the methods paper for B9. Worth deciding whether to keep both as separate handles (B9 = leaderboard, C-papers-4 = paper) or merge — keep them separate since they serve different citation roles.

### B10. openEHR-Foundation
- URL: https://specifications.openehr.org/
- [✓]
- **Source:** Verified — openEHR specifications hub.

### B11. openEHR-Clinical-Knowledge-Manager
- URL: https://ckm.openehr.org/ckm/
- [✓]
- **Source:** Verified by reference (didn't fetch the page itself; the openehr.org news item references CKM as the international instance under the openehr.org domain). Strong confidence this resolves.

### B12. Koenecke-Careless-Whisper-2024
- [✓] (already done in earlier review)

---

## C. Pending — you supply (44 entries)

### C-papers — author-named papers / preprints (15 entries)

#### C-papers-1. Croxford-2025
- → URL: **needs your call between two candidates**
  - **Candidate A (methodological/conceptual):** https://www.nature.com/articles/s44401-024-00011-2 Croxford et al. (2025). "Current and future state of evaluation of large language models for medical summarization tasks." *npj Health Systems* 2:6.
  - **Candidate B (instrument/concrete):** Croxford et al. (2025). "Development and validation of the provider documentation summarization quality instrument for large language models." *J Am Med Inform Assoc* 32:1050–1060. Likely DOI/URL: https://pubmed.ncbi.nlm.nih.gov/40323321/
- **Source:** Both are 2025 Croxford-led papers cited extensively in the LLM-as-judge / medical summarisation literature. Given your description (cited 4× across TP.SN family + ES.ME family, "load-bearing"), my best guess is **Candidate A (npj Health Systems)** — it's the broader-framing review paper that gets cited as the rationale for evaluation work. Candidate B is the concrete PDSQI instrument.
- **Recommendation:** [✓] — include both - worth handling how this happens.

#### C-papers-2. Asgari-Tortus-GOSH-2025
- → URL: https://www.nature.com/articles/s41746-025-01670-7
- [✓] (resolved)
- **Source:** Verified. Asgari/Montaña-Brown/Dubois/Khalil/Balloch/Au Yeung/Pimenta, "A framework to assess clinical safety and hallucination rates of LLMs for medical text summarisation", npj Digital Medicine 8:274 (2025). DOI 10.1038/s41746-025-01670-7. All authors were Tortus AI employees at submission. Original medRxiv preprint at `https://www.medrxiv.org/content/10.1101/2024.09.12.24313556v1`.
- **Cross-link:** This is the same paper as `C-uncertain-1. CREOLA-Hallucination-Taxonomy` — see that entry.

#### C-papers-3. Chung-NEJM-AI-2025
- → URL: [?]
- **Source:** I couldn't pin down a specific Chung-first-author NEJM AI Jan 2025 paper that fits. The most prominent NEJM AI ambient-AI-scribe RCT around that period is **Lukac et al., NEJM AI 2025;2(12):e2501000** (Ambient AI Scribes in Clinical Practice — UCLA RCT, published Nov 26 2025), which I found in multiple searches; "Chung" appears as a co-author on that paper. If your TP.SN-8 citation is actually that RCT, the URL is likely `https://ai.nejm.org/doi/10.1056/AIoa2501000` (DOI: 10.1056/AIoa2501000).
- **Recommendation:** [✓] — https://ai.nejm.org/doi/10.1056/AIoa2501000 is the right paper, with Lukac et al. (Cheng is co-author)

#### C-papers-4. Bedi-Stanford-CRFM-2025
- → URL: https://arxiv.org/abs/2505.23802
- [✓] (resolved — see B9)
- **Source:** This is the MedHELM paper. Bedi/Cui/Fuentes/Unell/Wornow/etc., "MedHELM: Holistic Evaluation of Large Language Models for Medical Tasks", arXiv 2505.23802, May 2025. Same paper underlies the B9 leaderboard.

#### C-papers-5. Kanithi-2025
- → URL: [?] candidate https://arxiv.org/abs/2409.07314
- **Source:** Best candidate is Kanithi et al., "MEDIC: Towards a Comprehensive Framework for Evaluating LLMs in Clinical Applications", arXiv 2409.07314 (2024 → updated 2025). Cited in C-papers-2's reference list as "Kanithi et al., 2024" with same framing. If your TP.SN-11 is about clinical LLM evaluation, this is highly likely.
- **Recommendation:** [✓] — yes, this is right.

#### C-papers-6. Wang-Duke-MedStar-2025 — **RESOLVED: same paper as SCRIBE-Wang-2025; merge anchors**
- → URL: https://www.nature.com/articles/s41746-025-01622-1
- **Source:** Confirmed via Nature citation metadata 2026-04-29. This is the **same paper** as the existing `[SCRIBE-Wang-2025]` anchor — Haoyuan Wang et al., *"An evaluation framework for ambient digital scribing tools in clinical applications"*, npj Digit. Med. 2025; 8:358 (online 2025-06-13), DOI `10.1038/s41746-025-01622-1`. Author list confirms Duke (Pencina, Poon, Bedoya, Economou-Zavlanos, Pollak, Hong, Wang…) + MedStar (Ratwani, Biro, Sorrentino, Handley) collaboration.
- **Recommendation:** Delete the standalone `Wang-Duke-MedStar-2025` reference entry at [taxonomy/_references.md:621-633](taxonomy/_references.md#L621-L633) and update TP.SN-13's Source-row reference at [taxonomy/part-a/summarisation-nlp.md:787](taxonomy/part-a/summarisation-nlp.md#L787) to the unified anchor. See **A6** below for the broader audit findings on this paper.

#### C-papers-7. i2b2-2012-Temporal-Challenge
- → URL: https://academic.oup.com/jamia/article/20/5/806/725647 (Sun, Rumshisky, Uzuner, JAMIA 2013)
- [?] — moderate confidence
- **Source:** The i2b2 2012 challenge on temporal expressions is well-known; the canonical writeup is Sun/Rumshisky/Uzuner, "Evaluating temporal relations in clinical text: 2012 i2b2 Challenge", JAMIA 2013;20(5):806–813. DOI 10.1136/amiajnl-2013-001628. The challenge year was 2012; the paper is 2013. The n2c2 portal also has the dataset page at `https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/`.
- **Recommendation:** Use the Sun et al. JAMIA paper if you want the citable reference, or the dbmi portal link if you want the dataset - can we have both please.

#### C-papers-8. Barcelona-JAMA-Network-Open-2025
- → URL: [?]
- **Source:** I didn't find this specific paper in this pass. "Barcelona et al., JAMA Network Open 2025, Black patients 2.54× odds of negative descriptors" is a very specific finding — likely about stigmatising language in clinical notes. Possibly Sun et al. or similar. Without the exact OR/CI signature, I can't pinpoint it.
- **Recommendation:** [?] There is this paper "Stigmatizing and Positive Language in Birth Clinical Notes Associated With Race and Ethnicity" doi:10.1001/jamanetworkopen.2025.9599 (https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2833892) which quotes "In our cross-sectional study examining clinical notes of 18 646 patients admitted for labor and birth, Black patients had 22% higher odds of stigmatizing language documented than White patients." - is this appropriate for what it is used for in the taxonomy?

#### C-papers-9. SPIE-14009E-2025
- → URL: [?]
- **Source:** SPIE proceedings paper IDs aren't easily searchable without the conference name. SPIE 14009E suggests the Medical Imaging conference proceedings volume. "FHIR R4 interoperability" is the topical hint. Likely findable via SPIE Digital Library search but I can't paste a URL I haven't verified.
- **Recommendation:** [?] — search "SPIE Medical Imaging 2025 FHIR R4 interoperability" on `https://www.spiedigitallibrary.org/` - not sure on this one - need more inforamtion on what it should refer to - push to second sweep with better grounding inoformation.

#### C-papers-10. Stults-2025
- → URL: [?] candidate around AI scribe documentation completeness
- **Source:** "57.9% → 93.0% improvement with ambient AI" is very specific. I couldn't find a Stults-first-author paper matching this in a quick search. Possibly published in a JAMIA or BMJ Quality & Safety venue.
- **Recommendation:** [?] — the percentage signature should make this findable on Google Scholar.
https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2833433
Seems to indicate here - "For giving patients their undivided attention, the proportion of clinicians who responded “agree/strongly agree” increased from 33 clinicians (57.9%) to 53 clinicians (93.0%) (P < .001)." - does this support what is said in the taxonomy?

#### C-papers-11. Coiera-Fraile-Navarro-JMIR-2026
- → URL: https://medinform.jmir.org/2026/1/e89337
- [✓] (resolved)
- **Source:** Verified. Coiera & Fraile-Navarro, "AI Scribes: Are We Measuring What Matters?", JMIR Med Inform 2026;14:e89337. DOI 10.2196/89337. Editorial in the AI Scribes theme issue. PMID 41650281.

#### C-papers-12. FAccT-2024-ASR-Accent-Critique
- → URL: [?] candidate https://dl.acm.org/doi/10.1145/3630106.3658942 (Wassink et al. or similar)
- **Source:** ACM FAccT 2024 papers are at `dl.acm.org/doi/10.1145/3630106.<id>`. Without the specific paper title, I can't pick the right `<id>`. The 2024 FAccT proceedings have several relevant ASR/accent papers — the most prominent ASR-accent critique is probably Wassink/Wright/Franklin "Uneven Errors: ASR for African American English". The Koenecke 2020 paper (`dl.acm.org/doi/10.1145/3613904.3642417`) is too old (2020 not 2024).
- **Recommendation:** [?] — I found "Speaking of accent: A content analysis of accent misconceptions in ASR research" https://dl.acm.org/doi/10.1145/3630106.3658969 - does that seem right?

#### C-papers-13. FAIR-MED-Springer-2025
- → URL: [?] — Springer search by title
- **Source:** "FAIR-MED: Bias Detection and Fairness Evaluation in Healthcare Focused XAI" — exact title given. Should be findable on `link.springer.com` by title search. Possibly a Springer LNCS volume from a 2025 conference.
- **Recommendation:** [✓] — (https://link.springer.com/chapter/10.1007/978-3-032-08317-3_18)

#### C-papers-14. Lancet-Gastroenterology-Endoscopist-AI-Off-2025
- → URL: https://www.thelancet.com/journals/langas/article/PIIS2468-1253(25)00133-5/abstract
- [✓] (resolved)
- **Source:** Verified. Budzyń/Romańczyk/Kitala et al., "Endoscopist deskilling risk after exposure to artificial intelligence in colonoscopy: a multicentre, observational study", Lancet Gastroenterol Hepatol 2025;10:896–903. DOI 10.1016/S2468-1253(25)00133-5. ADR fell 28.4%→22.4% post-AI introduction (matches your description exactly). Polish ACCEPT trial centres.

#### C-papers-15. Sitaram-Code-Switching-Survey-2019
- [✓] (already resolved)

### C-papers-medRxiv (3 entries → 4 incl. Rwanda)

#### C-medRxiv-1. medRxiv-Model-Autophagy-2026
- → URL: [?]
- **Source:** "Model autophagy" in clinical AI context is a Shumailov-adjacent framing. I couldn't find a specific medRxiv 2026 paper using this term in the time available. The term "autophagy" applied to AI was popularised by Alemohammad et al. ("Self-Consuming Generative Models Go MAD", arXiv 2307.01850) — but that's 2023, not 2026. A 2026 medRxiv paper applying this to clinical training data would be the candidate.
- **Recommendation:** [?] — https://medinform.jmir.org/2026/1/e94813 maybe that one?

#### C-medRxiv-2. medRxiv-Nov-2025-AVT-Drift
- → URL: [?]
- **Source:** Couldn't find a specific Nov 2025 medRxiv paper on AVT drift. "AVT drift" is fairly specific terminology — likely a UK/NHS-adjacent paper since AVT is the NHS-preferred term. Possibly Asgari-adjacent or GOSH-adjacent given your tracking of those teams.
- **Recommendation:** [?] — couldn't find one, suggest for second look more information from taxonomy is included to find appropriate source.

#### C-medRxiv-3. Keyes-Stanford-2025
- → URL: [?]
- **Source:** Could be a medRxiv preprint or a final-venue paper. "Keyes" with Stanford affiliation appears in the Bedi MedHELM author list as "Timothy Keyes" — possibly the same person but a different paper. Without the topic I can't pinpoint.
- **Recommendation:** [?] — Not sure, there is a paper with Keyes with the title "Monitoring Deployed AI Systems in Health Care" - does this fit with the narrative in the taxonomy? Suggest incude more information in second sweep.

#### C-medRxiv-4. Rwanda-Clinical-LLM-Evaluation
- → URL: [?] candidate https://arxiv.org/abs/2604.14892
- **Source:** Found a strong candidate: "Can LLMs Score Medical Diagnoses and Clinical Reasoning as well as Expert Panels?" (arXiv 2604.14892, March 2026), which evaluates LLM juries against expert panels in a middle-income country (MIC) Rwanda context, and explicitly references the Williams 2025 prior study with Kinyarwanda inputs. The earlier work cited within is Williams et al. 2025 — possibly that's the paper you mean. Ambiguous between the two without your Source row.
- **Recommendation:** [?] — **Williams et al. 2025 Kinyarwanda evaluation**, https://www.medrxiv.org/content/10.1101/2025.10.27.25338910v1.full or **March 2026 LLM-jury paper**, `https://arxiv.org/abs/2604.14892` could be it, more information required from taxonomy to decide in second sweep

### C-papers-multi (2 entries)

#### C-papers-multi-1. Sinsky-Mayo-EHR-Studies
- → URL: https://www.acpjournals.org/doi/10.7326/M16-0961
- [?] (this is the load-bearing 2016 Annals paper)
- **Source:** Sinsky CA et al. (2016). "Allocation of Physician Time in Ambulatory Practice: A Time and Motion Study in 4 Specialties." Ann Intern Med 165:753–760. DOI 10.7326/M16-0961. This is the most-cited Sinsky paper and the one usually meant by "Sinsky time-allocation study". A series-landing alternative would be her Mayo Clinic Proceedings author page.
- **Recommendation:** Use the 2016 Annals paper as the canonical entry-point. Title amendment: "Allocation of Physician Time in Ambulatory Practice: A Time and Motion Study in 4 Specialties" (Sinsky et al., Ann Intern Med 2016). I also found two other papers "Relationship Between Clerical Burden and Characteristics of the Electronic Environment With Physician Burnout and Professional Satisfaction" https://pubmed.ncbi.nlm.nih.gov/27313121/ and "Metrics for assessing physician activity using electronic health record log data" https://academic.oup.com/jamia/article/27/4/639/5728718 which might be relevent but hould be checked against taxonomy need.

#### C-papers-multi-2. Hollnagel-FRAM
- → URL: [?] — needs a decision from you
- **Source:** Hollnagel's FRAM book (2012) and Safety-II White Paper (2013) are both canonical, and there's no single best URL covering the corpus. Options:
  - **Book (FRAM, 2012):** No open URL — Routledge/Ashgate publication. Best link is the publisher page or a DOI if there's one.
  - **Safety-II White Paper (2013):** Open access at `https://www.england.nhs.uk/signuptosafety/wp-content/uploads/sites/16/2015/10/safety-1-safety-2-whte-papr.pdf` (NHS-hosted; ironic for your context).
  - **FRAMily community:** `https://functionalresonance.com/`
- **Recommendation:** [✓] — Safety-II White Paper URL above for open accessibility, with prose citation noting the FRAM book separately, and a link to the FRAMily community.

### C-frameworks-NHS (8 entries)

#### C-NHS-1. CIO-CCIO-Guidance-2026
- → URL: [?]
- **Source:** "NHS CIO/CCIO joint guidance v2 (January 2026)" — this is likely on `england.nhs.uk` but I couldn't find the specific Jan 2026 v2 in this pass. The closest related publication is `https://www.england.nhs.uk/long-read/guidance-on-the-use-of-ai-enabled-ambient-scribing-products-in-health-and-care-settings/` (cited by Tortus and others as the NHS England AI scribing guidance) — but that's not specifically CIO/CCIO joint v2.
- **Recommendation:** [✓] - that is the version for CIO and CCIOs

#### C-NHS-2. CQC-Mythbuster-109
- → URL: [?] candidate https://www.cqc.org.uk/guidance-providers/gps/gp-mythbusters
- **Source:** CQC Mythbusters are indexed at the URL above; Mythbuster 109 should be findable from there but the individual mythbusters have specific URLs like `cqc.org.uk/guidance-providers/gps/gp-mythbuster-NN-...`. Without resolving 109 specifically I can't paste the exact URL.
- **Recommendation:** [✓] — https://www.cqc.org.uk/guidance-providers/gps/gp-mythbusters/gp-mythbuster-109-artificial-intelligence-gp-services

#### C-NHS-3. NHS-Digital-OPCS-4
- → URL: https://digital.nhs.uk/services/terminology-and-classifications/
- [✓] — use the parent page for now, could also mention TRUD and the Terminology Server if needed
- **Source:** NHS Digital's OPCS-4 standards page. URL pattern matches `digital.nhs.uk/services/terminology-and-classifications/clinical-classifications/opcs-4` — this is the canonical hub. Note: NHS Digital was merged into NHS England in 2023, so URLs sometimes redirect to `england.nhs.uk`, but the digital.nhs.uk redirects still work.

#### C-NHS-4. NHS-BSA-dm-plus-d
- → URL: https://www.nhsbsa.nhs.uk/pharmacies-gp-practices-and-appliance-contractors/dictionary-medicines-and-devices-dmd
- [✓] — high confidence
- **Source:** NHS BSA dm+d page. The URL pattern under `nhsbsa.nhs.uk/.../dictionary-medicines-and-devices-dmd` is the standard one.

#### C-NHS-5. SNOMED-CT
- → URL: use this one
  - **UK Edition:** https://digital.nhs.uk/services/terminology-and-classifications/snomed-ct
- [✓] — needs your call
- **Source:** Both are canonical for their respective scopes. For NHS-context citations, UK Edition (`digital.nhs.uk`) is the right primary; for international or methods-paper citations, `snomed.org` is right.
- **Recommendation:** Default to UK Edition for AVT/NHS work; switch to international if the citation is about SNOMED CT generally.

#### C-NHS-6. DSCMS-SPI-Framework
- → URL: [?] - I don't think this is a thing, so we might need to handle this differently - suggestions welcome and could be part of the second review pass.
- **Source:** "NHS DSCMS Safety Performance Indicator framework" — DSCMS is the Digital Clinical Safety / Clinical Safety Management Standards group. This sits under NHS England digital clinical safety. I couldn't find a specific "SPI framework" page. Possibly published as a PDF under `england.nhs.uk` or as an information standard at `standards.nhs.uk`.
- **Recommendation:** [?] — search standards.nhs.uk and england.nhs.uk for "Safety Performance Indicator" or "SPI framework". Possibly a Phase 2 deliverable not yet indexed.

#### C-NHS-7. GOSH-Phase-4-TimeCat
- → URL: [?]
- **Source:** Given your `.gitignore` flag that "GOSH-AAI-Phase4-NHSE-report.pdf" exists locally, this may genuinely be local-only / unpublished. GOSH AAI Phase 4 reporting may not have a public NHS England URL yet.
- **Recommendation:** [✓] available here - https://media.gosh.nhs.uk/documents/AAI_Phase_4_NHSE_Final_Report_1.2.pdf

#### C-NHS-8. JMIR-2026-SEIPS-AVT
- → URL: [?] candidate at https://jmir.org or https://medinform.jmir.org for paper e86166
- **Source:** "JMIR 2026 paper e86166 — SEIPS-based AVT evaluation" — given the e-number format, this should be at `https://www.jmir.org/2026/1/e86166` or `https://medinform.jmir.org/2026/1/e86166` depending on which JMIR sister-journal. Should be findable but I haven't verified the exact landing.
- **Recommendation:** [?] — https://www.jmir.org/2026/1/e86166 gave "Assessing Health Care Professionals’ Perceptions of a New System in Clinical Workflows: Systems Engineering Initiative for Patient Safety–Based Consensual Qualitative Research" if this is correct from the taxonomy?

### C-vendor / disclosure (8 entries)

#### C-vendor-1. Abridge-Whitepaper-2025
- → URL: [?] candidate https://www.abridge.com/research or specific 2025 whitepaper page
- **Source:** Abridge publishes whitepapers under their `abridge.com/research` or `abridge.com/blog` paths. Without the specific title I can't pinpoint the 50,000+ training examples whitepaper.
- **Recommendation:** [✓] — https://www.abridge.com/ai/science-confabulation-hallucination-elimination - this mentions the 50,000 training examples

#### C-vendor-2. Abridge-Linked-Evidence
- → URL: [?] candidate https://www.abridge.com/blog or product page describing Linked Evidence
- **Source:** Abridge's Linked Evidence feature is described in their product/architecture content. Specific URL not verified in this pass.
- **Recommendation:** [?] — https://support.abridge.com/hc/en-us/articles/30235128433811-Verify-a-Note-With-Linked-Evidence - not sure if this supports the reference in the taxonomy so might need second pass with more information.

#### C-vendor-3. DeepScribe
- → URL: https://www.deepscribe.ai/
- [?] — generic reference; specific page depends on what aspect you're citing
- **Source:** DeepScribe is at `deepscribe.ai`. Generic reference is the homepage; for specific claims/features they have product pages and a resources section (`deepscribe.ai/resources/...` — see search result for their hallucination-mitigation post at `deepscribe.ai/resources/overcoming-hallucinations-and-biases-in-llm-...`).
- **Recommendation:** not sure about this, need more information in second round.

#### C-vendor-4. DeepScore
- → URL: [?] or [skip]
- **Source:** I couldn't find a vendor or product called "DeepScore" in the clinical AI space in this pass. Possibly a confusion with DeepScribe, or a smaller / regional product.
- **Recommendation:** https://www.deepscribe.ai/resources/deepscore-measuring-the-performance-of-ambient-ai-clinical-documentation#:~:text=The%20DeepScore%20report%20is%20a%20methodology%20for,overall%20quality%20of%20autonomous%20transcription%20and%20scribing.

#### C-vendor-5. Mistral-AI-LCA
- → URL: https://mistral.ai/news/our-contribution-to-a-global-environmental-standard-for-ai
- [?] — this is the right Mistral LCA publication if the citation is the July 2025 piece
- **Source:** Mistral AI published an environmental impact LCA (lifecycle assessment) in July 2025. URL pattern under `mistral.ai/news/...` — best to verify the slug.
- **Recommendation:** [✓] — (https://mistral.ai/news/our-contribution-to-a-global-environmental-standard-for-ai)

#### C-vendor-6. NLP2FHIR-Pipeline
- → URL: [✓] candidate https://github.com/BD2KOnFHIR/NLP2FHIR
- **Source:** NLP2FHIR is an academic/open-source project from the BD2K On FHIR group. The GitHub repo at `https://github.com/BD2KOnFHIR/NLP2FHIR` is the canonical project page. The associated paper is Hong et al., JAMIA Open 2019, DOI 10.1093/jamiaopen/ooz040.
- **Recommendation:** Use the GitHub repo URL, but make Source-Type adjustment: shift from "vendor" to "academic/open-source project" or "research tool".

#### C-vendor-7. John-Snow-Labs-FHIR-Ready-AI
- → URL: [?] candidate https://www.johnsnowlabs.com/healthcare-data-engine/ or specific FHIR-Ready AI product page
- **Source:** John Snow Labs has multiple healthcare AI products. "FHIR-Ready AI" should be a specific product page under `johnsnowlabs.com/healthcare-...`.
- **Recommendation:** [✓] — https://www.johnsnowlabs.com/fhir-ready-ai-transforming-unstructured-clinical-data-into-interoperable-resources/

#### C-vendor-8. NVIDIA-Reference-Architecture
- → URL: [?] candidate under https://docs.nvidia.com/healthcare/ or https://developer.nvidia.com/blog/...
- **Source:** NVIDIA has a clinical AI safety reference architecture and Llama-Guard-pattern guidance, but the specific URL depends on what you're citing — there's blog content, NIM container documentation, and reference architecture whitepapers.
- **Recommendation:** [?] — need more information on second pass to pin down URL

### C-uncertain (6 entries)

#### C-uncertain-1. CREOLA-Hallucination-Taxonomy
- → URL: https://www.nature.com/articles/s41746-025-01670-7
- [✓] — **same paper as C-papers-2 Asgari-Tortus**
- **Source:** Verified. CREOLA is the framework Tortus AI developed for assessing clinical safety and hallucination of LLM medical text summarisation. Their blog explicitly states the CREOLA approach is the framework described in Asgari et al. npj DM 2025. So C-uncertain-1 collapses into C-papers-2 — same URL, same paper.
- **Recommendation:** Either: (a) merge the two handles (delete one, keep `Asgari-Tortus-CREOLA-2025`), or (b) keep both with a cross-reference note. Your call. The [+desc] suggestion: "CREOLA framework, published as Asgari et al. npj Digital Medicine 8:274 (2025)".

#### C-uncertain-2. Stanford-Monitoring-Framework
- → URL: [?]
- **Source:** Cited 4× as "Stanford monitoring framework" / "three-layer surveillance model" — this sounds like a specific paper but could be a research-programme designation. The Stanford CRFM has multiple monitoring/governance threads. Possibly **Pfohl et al.** or **Char et al.** at Stanford on AI monitoring. Without a concrete signature I can't pinpoint.
- **Recommendation:** [?] — need more information for second pass to identify.

#### C-uncertain-3. MedCAT-Benchmarks
- → URL: 
- [✓] — this is the Kraljevic JAMIA MedCAT paper
- **Source:** Kraljevic Z et al. (2021), "Multi-domain clinical natural language processing with MedCAT: The Medical Concept Annotation Toolkit", DOI 10.1016/j.artmed.2021.102083. URL: https://pubmed.ncbi.nlm.nih.gov/34127232/
- **Recommendation:** Use the AI in Medicine 2021 paper as the canonical MedCAT reference. There's also a GitHub at `https://github.com/CogStack/MedCAT` if we can include it somewhere.

#### C-uncertain-4. FDA-PCCP-Guidance-2024
- → URL: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence
- [✓] — high confidence
- **Source:** FDA's Predetermined Change Control Plan (PCCP) final guidance, "Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence-Enabled Device Software Functions", finalised December 2024. The URL above follows FDA's canonical guidance-document pattern.
- **Recommendation:** Confirmed by clicking.

#### C-uncertain-5. IEEE-S-and-P-2023-LLM-PII-Leakage
- → URL: [?] candidate Lukas et al. or similar
- **Source:** IEEE S&P 2023 LLM PII leakage — the most-cited paper is **Lukas et al., "Analyzing Leakage of Personally Identifiable Information in Language Models"** (S&P 2023). DOI 10.1109/SP46215.2023.10179300. URL: `https://ieeexplore.ieee.org/document/10179300`.
- **Recommendation:** [?] — this paper above seems right, but add to second pass with more information just to make sure.

#### C-uncertain-6. Li-Making-AI-Less-Thirsty
- → URL: https://arxiv.org/abs/2304.03271
- [✓] — high confidence
- **Source:** Li/Yang/Islam/Ren, "Making AI Less 'Thirsty': Uncovering and Addressing the Secret Water Footprint of AI Models", arXiv 2304.03271 (April 2023). This is the canonical reference for AI water footprint. Final published version in Communications of the ACM, also worth citing if you want a journal venue.

### C-other (2 entries)

#### C-other-1. VeriFact
- → URL: [?] 
- **Source:** "VeriFact" appears in multiple papers as a factual-verification framework — could be one of several. The most prominent recent VeriFact is Chen et al. or Tang et al. for clinical text verification. Without your specific framing I can't pinpoint.
- **Recommendation:** [✓] — https://arxiv.org/abs/2501.16672

#### C-other-2. n2c2-Shared-Tasks
- → URL: https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/
- [✓] — high confidence for the programme landing
- **Source:** n2c2 (National NLP Clinical Challenges, the i2b2 successor) is hosted by the Harvard DBMI portal. The URL above is the programme landing page covering all years. Per-year DOIs would be the JAMIA writeups for each challenge (e.g., JAMIA Open issues 2018, 2019, 2020).
- **Recommendation:** Keep one handle for programme 

---

## D. Discipline-representative URLs (8 entries) — Option 3 triage

Following our discussion, this block applies **Option 3 (hybrid)**: keep the discipline-reps that are genuinely canonical and have correct URLs; drop the ones that are guess-grade or where no single paper plausibly serves as a rep; carve out specific-claim citations where a discipline-rep was being used to anchor a load-bearing finding. Where I drop, I supply replacement prose using the grouping-level pattern (literature gesture with 2–3 example refs inside the prose, not as catalogue handles).

The general framing principle: **the citation should match the claim being made.** Specific quantitative or evidential claims need specific papers. Existence-of-literature gestures get prose. The discipline-rep was trying to serve both purposes and serving neither; this triage separates them.

**Net result: 4 keeps (D2, D3, D5, D8 — the last with a rescoped handle), 1 carve-out (new entry for Carlini-2024 web-scale poisoning), 4 drops (D1, D4, D6, D7) replaced with grouping-level prose for use in the relevant Source rows.**

### D1. discipline-asr — Watanabe et al. ASR overview
- **Action: [skip]** — drop the entry. ASR has no single canonical "rep paper" and Dan's existing URL pointed to Hannun et al. anyway, not Watanabe.
- **Replacement prose for affected Source rows:**
  > ASR has standard performance metrics (word error rate, character error rate) and a substantial methods literature spanning end-to-end neural models, hybrid CTC/attention systems, and recent foundation models. Useful entry points: Prabhavalkar/Hori/Sainath/Schlüter/Watanabe end-to-end ASR survey (IEEE TASLP 2024, arXiv 2303.03329); Koenecke et al. on racial disparities in commercial ASR (PNAS 2020 — already in the catalogue as `Koenecke-Careless-Whisper-2024`'s predecessor work, though the 2024 ACM paper is what's in B12).
- **Note for catalogue:** Wherever a Source row currently dispatches to `discipline-asr`, replace with the relevant prose snippet above, scoped to the claim being made. If the claim is specifically about WER as a metric, no citation is needed (it's textbook).

### D2. discipline-calibration — Guo et al. ICML 2017
- **Action: [✓] keep**
- URL: https://arxiv.org/abs/1706.04599 (verified in earlier asserted-URLs review)
- **Source:** Guo/Pleiss/Sun/Weinberger, "On Calibration of Modern Neural Networks", ICML 2017. The canonical paper for ECE (Expected Calibration Error) and the modern ML calibration literature — cited >7000× and treated as the standard reference across the field. This is one of the cases where "discipline-rep" is genuinely defensible because the field really does have a single dominant entry-point paper.

### D3. discipline-adversarial-ml — Carlini & Wagner S&P 2017
- **Action: [✓] keep**
- URL: https://arxiv.org/abs/1608.04644 (verified)
- **Source:** Carlini & Wagner, "Towards Evaluating the Robustness of Neural Networks", IEEE S&P 2017. The canonical reference for the C&W attack and modern adversarial-ML evaluation. Like Guo, this is a case where a single paper genuinely anchors the field's modern era.

### D4. discipline-voice-biometric — Wang et al. spoofing overview
- **Action: [skip]** — drop the entry. The arxiv ID was guess-grade and the field's evaluation standard is the ASVspoof challenge series, not any one methods paper.
- **Replacement prose for affected Source rows:**
  > Voice biometrics and anti-spoofing detection are most usefully accessed via the ASVspoof challenge series (biennial since 2015, with associated Interspeech papers — Wu/Yamagishi/Kinnunen et al. for the 2015 inception, Todisco et al. for ASVspoof 2019, Liu et al. for ASVspoof 2021). The challenge datasets and baseline systems are the de facto evaluation standard in the field; there isn't a single canonical methods paper.

### D5. discipline-data-poisoning — Biggio et al. ICML 2012 (+ carve-out)
- **Action: [✓] keep + carve out new specific entry**
- URL: https://arxiv.org/abs/1206.6389 (verified)
- **Source:** Biggio/Nelson/Laskov, "Poisoning Attacks against Support Vector Machines", ICML 2012. Genuinely canonical as the historical entry-point for the data-poisoning literature.
- **Carve-out — new entry to add:**
  - **Handle:** `Carlini-Web-Scale-Poisoning-2024`
  - **URL:** https://arxiv.org/abs/2302.10149 (verified — IEEE S&P 2024)
  - **Source:** Carlini/Jagielski/Choquette-Choo/Paleka/Pearce/Anderson/Terzis/Thomas/Tramèr, "Poisoning Web-Scale Training Datasets is Practical", IEEE S&P 2024. This is what GV.SC-4 actually cites (the 0.001% threshold framing for web-scale poisoning), and it's the wrong paper to assign to the Biggio 2012 SVM rep — different attack model, different threat surface, different citation context.
  - **Use-pattern:** Source rows citing the historical/conceptual basis of poisoning attacks → Biggio (D5). Source rows citing modern web-scale practical poisoning thresholds → Carlini-Web-Scale-Poisoning-2024.

### D6. discipline-diarisation — Anguera et al. IEEE TASLP 2012
- **Action: [skip]** — drop the entry. The IEEE document ID was guess-grade and diarisation doesn't have a single canonical rep paper either.
- **Replacement prose for affected Source rows:**
  > Speaker diarisation has standard performance metrics (diarisation error rate / DER, Jaccard error rate / JER) and a long methods literature. Useful entry points: Anguera et al. "Speaker Diarization: A Review of Recent Research" (IEEE TASLP 2012) for the pre-deep-learning era; Park/Kanda/Dimitriadis/Han/Watanabe/Narayanan "A Review of Speaker Diarization: Recent Advances with Deep Learning" (Computer Speech & Language 2022) for the modern era. The DIHARD challenge series is the current evaluation standard.

### D7. discipline-clinical-nlp — Sheikhalishahi et al. JMIR 2019
- **Action: [skip]** — drop the entry. The URL is correct, but the paper is scoped specifically to *chronic diseases* NLP, not clinical NLP generally. As a discipline-rep it would mislead readers about the paper's actual scope.
- **Replacement prose for affected Source rows:**
  > Clinical NLP for EHR text has a substantial body of work spanning rule-based, statistical, and neural methods. Useful entry points: Sheikhalishahi et al. (JMIR Med Inform 2019, scoped to chronic diseases) for an early review; Wu et al. "Deep learning in clinical natural language processing: a methodical review" (JAMIA 2020) for a broader deep-learning-era survey; Kraljevic et al. on the MedCAT toolkit (Artif Intell Med 2021) for a representative open-source pipeline. There isn't a single canonical paper covering the full field.
- **Cross-reference:** if you keep `MedCAT-Benchmarks` as resolved (C-uncertain-3), it appears in this prose as a specific instance — fine to cite both ways.

### D8. discipline-human-factors — Sittig & Singh BMJ Q&S 2010
- **Action: [✓] keep, but rescope the handle**
- URL: https://qualitysafety.bmj.com/content/19/Suppl_3/i68 (verified)
- **Rescope:** the paper *is* the canonical reference for the 8-dimensional sociotechnical model in clinical informatics, cited as such across the HIT safety literature. But it is **not** a "human factors" rep — it doesn't cover cognitive offloading, automation skill degradation, or aviation. The original Source-row description ("Stand-in for: human factors literature, cognitive offloading, aviation skill degradation") was overclaim.
- **Suggested handle change:** `discipline-human-factors` → `Sittig-Singh-HIT-Sociotechnical-2010` (treat as a specific-paper handle, not a discipline rep).
- **For Source rows actually citing cognitive offloading or aviation skill degradation:** these need different specific papers, not Sittig & Singh. Likely candidates depending on what the claim is:
  - Aviation automation skill degradation: Casner/Geven/Williams 2014 ("The retention of manual flying skills in the automated cockpit", *Human Factors*) or Ebbatson et al.
  - Cognitive offloading: Risko & Gilbert 2016 ("Cognitive offloading", *Trends in Cognitive Sciences*).
  - These should be added as separate specific-paper entries, not as a discipline-rep.

---

### Summary of changes to Block D

| Old entry | Action | Result |
|---|---|---|
| D1 ASR (Watanabe) | drop | replaced with grouping-level prose |
| D2 Calibration (Guo) | keep | unchanged |
| D3 Adversarial ML (Carlini & Wagner) | keep | unchanged |
| D4 Voice biometric (Wang) | drop | replaced with grouping-level prose |
| D5 Data poisoning (Biggio) | keep + carve out | Biggio retained for historical/conceptual; Carlini-2024 added as new specific entry |
| D6 Diarisation (Anguera) | drop | replaced with grouping-level prose |
| D7 Clinical NLP (Sheikhalishahi) | drop | replaced with grouping-level prose |
| D8 Human factors (Sittig & Singh) | keep, rescope | handle becomes `Sittig-Singh-HIT-Sociotechnical-2010`; cognitive-offloading / aviation claims need separate specific citations |

**Block goes from 8 entries to 4 + 1 new = 5 entries.** Of the 4 dropped, three (D1, D4, D6) get replacement prose because they don't have a defensible single rep. D7 also gets prose since the original paper's chronic-diseases scope makes it the wrong rep for clinical NLP generally. D8 keeps the URL but loses the discipline-rep framing.

**Action items for you:**
1. Patch the catalogue to drop D1, D4, D6, D7 and rescope D8.
2. Add the new `Carlini-Web-Scale-Poisoning-2024` entry (URL: https://arxiv.org/abs/2302.10149) and re-point GV.SC-4's citation to it.
3. Inline the four prose snippets (D1, D4, D6, D7) into the Source rows that previously dispatched to those discipline-reps. The prose is meant to be lifted directly; tweak as needed for context.
4. Audit any Source row that currently uses `discipline-human-factors` for whether the claim is actually about (a) HIT sociotechnical model — keep with rescoped handle, (b) cognitive offloading — needs Risko & Gilbert 2016 or similar, (c) aviation skill degradation — needs Casner et al. 2014 or similar.

---

## Summary table of resolved status

| Block | Total | ✓ Resolved | [?] Strong candidate | [?] Genuinely uncertain | [skip] suggested |
|---|---|---|---|---|---|
| A | 5 | 5 | 0 | 0 | 0 |
| B (active) | 11 | 10 | 0 | 0 | 0 (B8 = `[!]` correction) |
| C-papers | 15 | 4 | 5 | 5 | 0 (C-papers-15 already ✓) |
| C-medRxiv | 4 | 0 | 1 | 3 | 0 |
| C-papers-multi | 2 | 0 | 1 | 1 | 0 |
| C-NHS | 8 | 0 | 4 | 3 | 1 (C-NHS-7) |
| C-vendor | 8 | 0 | 5 | 2 | 1 (C-vendor-4) |
| C-uncertain | 6 | 2 | 3 | 1 | 0 |
| C-other | 2 | 0 | 2 | 0 | 0 |
| D | 8 → 5 | 4 keeps (D2, D3, D5, D8 rescoped) + 1 carve-out (Carlini-2024) | n/a | n/a | 4 drops with replacement prose (D1, D4, D6, D7) |

So roughly: 21 confidently resolved, 21 with strong candidates needing your final pick, 13 that need genuine investigation, 2 [skip] suggestions in C. **Block D: 4 entries kept (one rescoped), 1 new entry added (Carlini-2024 web-scale poisoning), 4 entries dropped with replacement prose drafted.** The biggest content-finds are **B8 NIHR-RSET correction**, the **CREOLA / C-papers-2 collapse**, and the D8 scope correction (Sittig & Singh is sociotechnical-model, not human-factors).

When you've patched in your final calls, ping me and I can take a second pass at any [?] you want me to dig into more.
