# SOURCES.md — Deck Economics Study

Every model parameter traces to one or more sources below. Grades:

- **A** — primary survey/data with documented method and sample size
- **B** — reputable outlet or named vendor study citing a specific survey/method; or primary data with material caveats (small n, self-selection, vendor sponsorship)
- **C** — weak/anecdotal (career blogs, forum consensus, single anecdotes). **C sources never drive core parameters** — they only color or corroborate.

Retrieval date for all sources: 2026-07-06.

---

## Family 1 — Working hours

### S1 — WSO 2024 Investment Banking Working Conditions Survey (grade A)
- URL: https://www.wallstreetoasis.com/files/2024%20WSO%20IB%20Working%20Conditions%20Survey.pdf
- Publisher: Wall Street Oasis. Date: January 2025 (fieldwork 8 Oct 2024 – 14 Jan 2025).
- Method: online survey, n = 531 banking professionals (373 analysts, 104 associates, 46 VPs/Directors); professional status not verified (stated in the report).
- Exact claims: "How many hours have you worked per week on average?" — **First-year analyst 74.00 h; second-year analyst 72.72 h; associate 74.47 h**. Sleep: 5.95 / 6.28 / 6.27 h per night. Tail: the report's headline text (p.6) says **17% work 90+ h/week and 6% work 100+ h/week**; a bank-level panel in the same report shows 13% / 4% — we cite the headline figures and note the internal discrepancy.
- Notes: self-selected sample skewed to juniors; unverified respondents. Still the best recent public IB hours dataset.

### S2 — WSO 2023 Investment Banking Working Conditions Survey (grade A)
- URL: https://www.wallstreetoasis.com/files/2023%20WSO%20IB%20Working%20Conditions%20Survey%20.pdf (results thread: https://www.wallstreetoasis.com/forum/investment-banking/wso-2023-investment-banking-work-conditions-survey)
- Publisher: Wall Street Oasis. Date: 2023. 3rd annual edition.
- Exact claims: **first-year analysts averaged 77 h/week**, sleeping under 6 h/night; associates ~73 h/week. Average sleep improved from 5.85 h (2021) to 6.03 h (2023); 30% still average ≤5 h sleep.
- Notes: same method family as S1; used for year-over-year corroboration.

### S3 — Goldman Sachs first-year analyst "Working Conditions Survey" (grade B)
- URLs: https://www.cnn.com/2021/03/18/investing/goldman-sachs-analyst-workplace ; https://www.fintechfutures.com/data-privacy-security/goldman-sachs-analysts-reveal-abusive-working-conditions-in-leaked-survey ; https://www.forbes.com/sites/palashghosh/2021/03/18/goldman-sachs-first-year-analysts-face-100-hour-weeks-abusive-behavior-stress-survey-says/
- Publisher: internal GS analyst presentation (Feb 2021), leaked; reported by CNN/Forbes/FinTech Futures, March 2021.
- Method: self-organized survey of **13 first-year analysts** (self-selected), IBD.
- Exact claims: **average 98 h/week worked; 105 h in the week ending 13 Feb 2021; "working over 95 hours per week and sleeping five hours per night"**; requested cap of 80 h/week; 100% said hours hurt relationships.
- Notes: primary in origin but tiny, self-selected, crisis-period sample. Used only as an upper tail anchor, never as a central estimate.

### S4 — eFinancialCareers, "The banks with the best and worst working hours" (grade B)
- URL: https://www.efinancialcareers.com/news/working-hours-banks
- Publisher: eFinancialCareers. Date: 7 May 2025 (verified from page metadata, re-fetched 2026-07-06).
- Method: eFC salary-and-hours survey, "responses from over **2,500 professionals in the financial services sector**"; the article states the survey "is not limited to either front-office or American staff" — all seniorities and functions, not just IBD juniors.
- Exact claims: "The average working week across the **sell-side** (investment banks, for all functions) was **52.6 hours**." Boutique banks (Evercore, Lazard, Moelis aggregated) "had higher average working hours than any individual bank."
- Notes: includes senior staff and non-IBD roles, hence far below S1/S2 junior averages. Used only as a lower-bound anchor for hours dispersion. (A previous revision of this entry pointed at a different eFC URL and attributed a juniors-vs-average claim to this survey; the junior numbers in the article are quoted from WSO data, i.e. our S1 family, so we attribute them there.)

### S5 — Michel, A., multi-year Wall Street ethnography (grade A, dated)
- URLs: https://journals.sagepub.com/doi/10.1177/0001839212437519 ; https://business.time.com/2012/02/17/study-working-on-wall-street-is-bad-for-your-health/
- Publisher: Administrative Science Quarterly (2011); author ex-Goldman, U. Penn. Date: fieldwork ~1999–2010s, published 2011/2014.
- Method: 9–12 year ethnography of two investment banks; 136 formal interviews; observation 5–7 days/week.
- Exact claims: junior bankers habitually worked **80–120 h/week**; "many juniors were working 120 hours a week".
- Notes: academic gold standard for the phenomenon, but 15–25 years old. Used only to justify the fat upper tail of the IB hours distribution.

### S6 — Consulting working hours (grade B/C composite)
- URLs: https://www.consultancy.eu/career/work-life-balance (B) ; https://www.hackingthecaseinterview.com/pages/consulting-hours-per-week (C) ; https://www.casebasix.com/pages/consulting-working-hours-firm-level (C) ; https://strategycase.com/how-much-consultants-work/ (C)
- Exact claims: Consultancy.eu research: **77% of top-market consultants work more than contract hours; average overtime 9.3 h/week; in strategy consulting overtime averages ~20 h/week** (implying ~55–60+ h on a 40-h contract). Career-prep sites converge on **50–65 h/week** at MBB, with 80-h crunch weeks the exception.
- Notes: the B-grade Consultancy.eu figure anchors the mode; C sources only corroborate the range.

---

## Family 2 — Time spent on presentations / slides

### S7 — empower (vendor-commissioned), Nielsen fieldwork, "The Ultimate Global PowerPoint Study" (grade B)
- URL: https://www.empowersuite.com/hubfs/Marketing/Downloads/PowerPoint%20Studie%202020/Englisch/The%20Ultimate%20Global%20PowerPoint%20Study%20-%20empower.pdf
- Publisher: empower GmbH (PowerPoint add-in vendor), fieldwork by **Nielsen**. Date: May 2020.
- Method: online survey, **n = 1,102 employees** who work ≥50% of their time on computers; companies ≥50 employees, HQ in Germany and USA.
- Exact claims: average **7 h/week in PowerPoint** per *PowerPoint-using* employee — the PDF states only 54% of corporate employees work with PowerPoint at all ("almost a full working day"); by department: **Consulting 8 h, Business Development 8 h, Management 8 h**; by position: employee 6 h, manager 8 h, **director 9 h**. **37% of PowerPoint working time is spent on formatting** (≈2.6 h/week). Average **12 presentations created per month** per employee (consulting departments: 12). 39% of presentations built from an existing presentation, 56% from templates. The PDF also reports 9 h/week in meetings *with* PowerPoint; whether this overlaps the 7 h creation time is not stated (treating it as additional is our inference, not the PDF's claim).
- Notes: vendor-commissioned (incentive to inflate) with Nielsen fieldwork, stated n and population; cite as "vendor-commissioned, Nielsen fieldwork", never as "a Nielsen study". General corporates, **not** elite finance. Used for the formatting/churn share and as a corporate-baseline reference point, not for IB analyst time-share.

### S8 — UpSlide + CSA, "Productivity in Finance" study (grade C+, downgraded from B in fix pass)
- URLs: https://www.docaufutur.fr/2020/03/26/etude-csa-et-upslide-86-des-professionnels-en-finance-estiment-ne-pas-avoir-assez-de-temps-a-consacrer-a-leur-coeur-de-metier/ (press copy of the March 2020 release, re-verified 2026-07-06) ; https://www.silicon.fr/press-release/etude-csa-et-upslide-86-des-professionnels-en-finance-estiment-ne-pas-avoir-assez-de-temps-consacrer-leur-cur-de-mtier ; original UpSlide article now redirects to the upslide.com homepage.
- Publisher: UpSlide (finance PowerPoint/Excel add-in vendor), fieldwork by **CSA** (French market-research institute). Date: March 2020.
- Method: 15-minute online questionnaire, **n = 178 professionals** from banking, financial and insurance sectors (CSA panel; France-centric).
- Exact claims (verified against the 2020 press release): "90% des professionnels de la finance interrogés disent passer **jusqu'à 2h** par jour sur PowerPoint" — 90% report spending **up to 2 hours** per day in PowerPoint (a *ceiling*, not a floor); **10% spend 4+ hours/day in PowerPoint; 30% spend 4+ h/day in Excel**; **86% feel they don't have enough time for core business functions**; copy-paste from Excel to PowerPoint *or Word* is among the most-performed tasks; ~70% consider themselves overqualified for the repetitive, time-consuming tasks they perform (not formatting specifically).
- Notes: small n, vendor-sponsored, France-weighted, 2020 (pre-hybrid-work, pre-genAI). **Integrity flag:** UpSlide's *current* blog page carries a TL;DR reading "2+ hours per day", which reverses the 2020 release's "up to 2h" and is absent from the 2020-10-01 Wayback snapshot of the same article — i.e. retrofitted later by the vendor. We cite only the 2020 release wording. Downgraded to C+ for this discrepancy; colors the time-share parameter, drives nothing alone.

### S9 — Mergers & Inquisitions, "Investment Banking Pitch Books" (grade C — color only)
- URL: https://mergersandinquisitions.com/investment-banking-pitch-books/
- Publisher: Mergers & Inquisitions (Brian DeChesare). Date: continuously updated.
- Exact claims: "most junior bankers spend more time in PowerPoint than Excel"; "It's not uncommon to see 'v44' at the end of file names"; valuation section "1-2 slides in a short pitch book or 20+ slides in a longer one"; shorter books "a few hours", others "spiral into never-ending projects that require all-nighters"; senior bankers "make changes well past the point of diminishing returns".
- Notes: practitioner-authored and widely respected, but anecdotal — colors churn and time-share, drives nothing.

---

## Family 3 — Compensation and loaded cost

### S10 — Mergers & Inquisitions, "Investment Banker Salary and Bonus Report: 2026" (grade B)
- URL: https://mergersandinquisitions.com/investment-banker-salary/
- Publisher: Mergers & Inquisitions. Date: 2026 report (end-of-2025 bonuses).
- Method: ~200 collected salary/bonus data points; figures = "roughly the 25th to 75th percentile ranges across the 'large banks'", New York front-office, excluding boutiques; base + year-end bonus, excluding signing/stub/benefits.
- Exact claims (total compensation, USD): **Analyst $165–225K (base $100–125K); Associate $285–500K (base $175–225K); VP $525–800K (base $250–300K)**; Director/SVP $700–900K; MD $1–2M+.
- Notes: method stated, sample modest; consistent with WSO Company Database ranges (Analyst $120–195K total per WSO benchmarking threads).

### S11 — Heidrick & Struggles, 2025 North America PE Investment Professional Compensation Survey (grade A)
- URL: https://www.heidrick.com/-/media/heidrickcom/publications-and-reports/north-america-pe-investment-professional-compensation-survey_2025.pdf
- Publisher: Heidrick & Struggles Private Capital Practice. Date: 2025.
- Method: survey of **656 PE investment professionals** in North America; quartile tables by AUM band and title.
- Exact claims (2024 actuals, USD thousands, funds $1.0–1.49bn AUM): **Associate/senior associate mean base 140, mean bonus 115, mean total 244 (LQ 180 / UQ 300, low 100 / high 400)**; **VP mean base 240, mean bonus 181, mean total 378 (LQ 300 / UQ 450, low 160 / high 600)**; smaller funds (<$250m): associate mean total 207; $500–749m funds: associate mean total 230, VP mean total 380.
- Notes: definitive public PE comp source; excludes carry (which we also exclude — carry is not a cash cost of deck production).

### S12 — Management Consulted salary data via Poets&Quants (grade B)
- URLs: https://poetsandquants.com/2026/01/26/consulting-pay-what-mbas-earned-in-2025/ (citing Management Consulted "Consulting Salaries Report 2026", 130+ firms) ; https://managementconsulted.com/consultant-salary/
- Publisher: Management Consulted (annual offer-data collection), reported by Poets&Quants. Date: Jan 2026, 2025 offer data.
- Exact claims (USD): MBA level — **McKinsey base $192K, perf bonus $40K, total $267K; BCG base $190K, total $270K; Bain base $192K, perf bonus $63K, total $285K** (signing bonus $30K each). Undergraduate level — **McKinsey base $112K (+$18K bonus); BCG $110K (+$22K); Bain $112K (+up to $22.5K); total comp ~$137–140K**. Base salaries "largely frozen since 2023".
- Notes: collected from actual offers across 130+ firms; the standard public reference for consulting pay.

### S13 — U.S. BLS, Employer Costs for Employee Compensation (ECEC) (grade A)
- URLs: https://www.bls.gov/news.release/ecec.htm ; https://www.bls.gov/news.release/archives/ecec_06132025.pdf
- Publisher: U.S. Bureau of Labor Statistics. Date: 2025 (Dec 2025 release; March 2025 archive).
- Exact claims: private-industry workers, December 2025: **wages and salaries averaged $32.36/h = 70.1% of total employer costs; benefits $13.79/h = 29.9%**. (March 2025: 70.3% / 29.7%.) Benefit categories: paid leave, supplemental pay (incl. bonuses), insurance, retirement, legally required.
- Notes: primary federal data. Caveat for our use: ECEC "benefits" includes supplemental pay/bonuses, which our cash-comp figures already contain; and ECEC excludes overhead (real estate, IT, support). Net: a 1.15–1.45 loading on total cash comp is defensible (see S14 and METHODOLOGY).

### S14 — Fully-loaded cost multiplier guides (grade C — corroboration only)
- URLs: https://scalearmy.com/blog/calculate-fully-loaded-cost-of-an-employee/ ; https://www.glencoyne.com/guides/fully-loaded-cost-us-employee ; https://www.hibob.com/financial-metrics/fully-burdened-labor-rate/
- Exact claims: typical total cost **1.3–1.4× base salary**, full range **1.25–1.8×** depending on benefits/overhead; "30% to 40% in mandatory taxes, benefits, equipment, and administrative overhead".
- Notes: HR-industry secondary content; corroborates the S13-derived loading range.

---

## Family 4 — Deck size, effort per slide, revision churn

### S15 — Wall Street Prep, "Investment Banking Pitchbook" (grade C — color only; corrected in fix pass)
- URL: https://www.wallstreetprep.com/knowledge/investment-banking-pitchbook/
- Publisher: Wall Street Prep (training firm staffed by ex-bankers). Date: current (re-fetched 2026-07-06).
- Exact claims: the page contains exactly **one** page-count sentence — "Your team puts together a forty-page slide deck with sixty pages of appendices" — and that sentence is WSP **quoting a DealBreaker article** (third-hand rhetorical color inside a passage mocking wasted pitch effort). No other page-count ranges appear on the page.
- Notes: a previous revision of this entry attributed "20–60 pages" and "sell-side ~10–25 slides" to this page; **those ranges are not on the page** and the attribution was wrong. The DealBreaker quote (≈100 pages incl. appendices) is used only as upper-tail color for `pitchbook_pages`.

### S16 — SlideGenius production-rate FAQ pages (grade C — regraded from B- in fix pass; corroboration only)
- URLs: https://www.slidegenius.com/cm-faq-question/what-is-the-average-time-required-to-produce-a-high-quality-presentation-slide ; https://www.slidegenius.com/cm-faq-question/what-are-the-average-production-rates-for-creating-powerpoint-slides
- Publisher: SlideGenius (presentation design agency). Date: undated FAQ content.
- Exact claims (re-fetched 2026-07-06): "The average time to produce a high-quality presentation slide typically ranges from **1 to 3 hours per slide**"; simple slides "30 to 60 minutes"; detailed slides "1 to 2 hours"; highly technical/data-driven slides "2 to 3 hours or more"; client feedback adds **1–2 rounds of 30–60 min per round**; complex custom slides "4-8 hours per slide or more".
- Notes: **unstable and method-free** — both URLs returned 404 during the 2026-07-06 adversarial review, and the second page's slug changed; they resolved again later the same day (snapshot requested at web.archive.org). SEO/FAQ micro-pages: no survey, no n, no author, no date. Under our own rubric this is a **C source** and cannot drive a parameter — `hrs_per_page` is therefore an explicit assumption (see METHODOLOGY), with S16 as one corroborating agency benchmark for *finished* slides (i.e. including revision rounds).

### S17 — Pitchbook structure, length and revisions — career-prep guides (grade C — color and range corroboration)
- URLs: https://ibinterviewquestions.com/blog/pitch-book-structure-sections (IB IQ, re-fetched 2026-07-06) ; https://www.quora.com/What-does-an-investment-banking-pitch-book-look-like-What-do-investment-banking-analysts-and-associates-spend-100-hours-a-week-preparing
- Exact claims (IB IQ, verified): section page budgets for "a typical **20-60 page** book"; typical lengths by type: "M&A Sell-Side: **30-50 pages**; M&A Buy-Side: 25-40 pages; Capital Raising: 25-45 pages; Restructuring: 30-50 pages"; books "rebuilt through **3-5+** rounds of senior edits on a **7-10 day** clock"; drafts reviewed by seniors with extensive comments; v44/v57-style version counts common (with S9). Similar ranges appear in vendor content (Deckary, Feb 2026: initial books 15-25 slides, comprehensive 30-60, sell-side M&A 30-50) citing the same guide family.
- Notes: career-prep and forum content, no survey or method; corroborates the `pitchbook_pages` range and revision-cycle counts, drives nothing alone.

### S18 — PE IC memo effort (grade C — thin, flagged)
- URLs: https://www.cadencetranslate.com/The-Beginner's-Guide/chapter-6-the-investment-committee ; https://www.meridian-ai.com/blog/how-the-best-firms-run-investment-committee ; https://agentman.ai/blog/ic-memo-that-wrote-itself
- Exact claims: IC process from concept to final memo averages **~2 months** with interim drafts "in the days and weeks leading up to IC"; one firm reported memo prep "typically took **12 to 15 hours** per deal" (vendor anecdote, likely per-cycle rather than cumulative); best practice: memo submitted Thursday 8pm for Monday IC.
- Notes: **thin family.** IC deck parameters are marked assumption-heavy in METHODOLOGY.md and results for IC memos carry wider uncertainty and a lower evidence grade.

### S19 — Consulting engagement structure and pricing (grade B-/C)
- URLs: https://www.hackingthecaseinterview.com/pages/consulting-project-team-structure ; https://www.rocketblocks.me/guide/business-model.php
- Exact claims: MBB case teams **3–6 people across 4 levels**; engagements typically **3–12 weeks** (average project ~3–4 months at the long end); MBB engagements price around **"$500,000 for a six-person team for one month"**.
- Notes: career-prep sources written by ex-consultants; used for the illustrative engagement frame, not for core cost-per-hour parameters.

### S20 — Nancy Duarte, *slide:ology* effort benchmark (grade C — practitioner book, corroboration only)
- URLs: https://sixminutes.dlugan.com/presentation-skills-book-review-slideology-by-nancy-duarte/ (review quoting the estimate; verified 2026-07-06) ; https://www.duarte.com/resources/books/slideology/
- Publisher: Nancy Duarte (founder of Duarte Inc., the largest US presentation-design firm), *slide:ology*, O'Reilly 2008.
- Exact claims: **36–90 hours to create a 30-slide, one-hour presentation** — i.e. **1.2–3.0 h/slide all-in**, including research, storyboarding, building and rehearsing.
- Notes: widely-cited practitioner rule of thumb, no survey or method; the scope (research + rehearsal) is broader than our document-production-only scope, so it bounds our per-page effort from above. Corroborates the magnitude of S16.

### S21 — Per-slide market pricing compilations (grade C — corroboration only)
- URLs: https://plusai.com/blog/how-much-does-a-slide-cost (compiled from public agency/freelancer/consulting price points; verified 2026-07-06) ; https://24slides.com/pricing/slide-prices
- Exact claims: freelance-marketplace slide work "$10 to $125+ per slide" at "$32/hour to as high as $250/hour"; agency price points from "$22/slide" to premium packages; 24Slides fixed prices **$11–16 per slide** for redesign/fix-up work (24–72 h turnaround); implied MBB "cost" per slide of $3–5k+ (project fees ÷ slide counts — a billing artifact, not effort).
- Notes: prices, not hours; vendor content without stated method. Used only to sanity-check that sub-hour to low-single-digit-hours per finished slide is the market's operating range.

### S22 — Publicly filed IB board/fairness presentations, page-count sample (grade B — primary documents, convenience sample)
- URLs: index at https://www.10xebitda.com/investment-banking-presentations/ (mirror of presentations filed in SEC merger proxies); per-deck URLs in `results/pitchdeck_page_sample.csv`.
- Method: we downloaded a systematic sample (every 5th entry of the deduplicated index) of **n = 21** real investment-bank presentations (Barclays, Goldman Sachs, JPMorgan, Centerview, Evercore, Lazard, Moelis, Credit Suisse, Deutsche Bank et al., 2003–2024) and counted PDF pages programmatically. Retrieved 2026-07-06.
- Exact result: **median 25 pages, mean 22.3, range 3–38**; 38% of the sample is ≤20 pages. Full per-deck table persisted in `results/pitchdeck_page_sample.csv`.
- Notes: these are *live-deal board and fairness discussion materials* — a genre that skews shorter than bake-off marketing pitchbooks (no credentials section, thin appendices), and the mirror's selection is not random. Used to anchor the lower half of `pitchbook_pages` with real artifacts; the upper half rests on the S17 guide ranges and S15 color.

---

## Explicitly rejected / not used

- Grunt ("consultants spend 20 hours/week on low-value PowerPoint tasks") — vendor blog scenario, no method → rejected for parameters.
- Rokoko "8,500 professionals" leadership stat — could not verify method or original publication → not used.
- Quora/PrepLounge consulting time-share percentages — C-grade forum estimates → not used as parameters (noted only as consistent with the wide band chosen).
- WSO Compensation Report 2025 page — 403 behind account wall; replaced by S10/S11 (M&I ranges cross-checked against WSO benchmarking forum summaries).
- CFI "Investment Banking Pitch Book" guide — fetched 2026-07-06; contains **no page counts** → cannot corroborate deck length.
- FinanceWalk pitch-book guide ("ideally 10 to 20 pages/slides") — no method, low credibility, inconsistent with all other sources → not used.
- WSO pitch-book resource pages — Cloudflare 403 to automated fetch on 2026-07-06 → could not verify content, not cited.
- WSO forum threads on PE IC memo lengths (surfaced in search: ~20 pages incl. appendix at one fund; 30–40-page preliminary memos; 2–4-page Word + 20–25 slides at others) — could not be fetched directly for verbatim verification (403) → noted here for transparency but **not** cited as a source; `ic_pages` remains a flagged assumption.
