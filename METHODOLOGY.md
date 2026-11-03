# METHODOLOGY.md — What deck production costs in IB / PE / consulting

## Scope and definitions

We estimate the **production cost of presentation documents** (pitchbooks, IC decks/memos,
consulting client decks): assembling, laying out, charting, formatting, revising and
reviewing the document itself. We **exclude** the underlying analytical work (financial
modeling, diligence, research) except where it is inseparable from building an exhibit.
This makes every estimate conservative relative to "total cost of the deliverable".

All cost figures are **model estimates, not measurements**. Inputs are distributions tied
to graded sources or explicitly labeled assumptions (see `SOURCES.md` and the parameter
tables below); outputs are reported as P10/P50/P90 percentiles, rounded to 2 significant
figures. Outputs that depend on assumption-labeled parameters are conditional estimates.

## Simulation

- Monte Carlo, `numpy` (seed **20260706**), **N = 200,000** draws per quantity.
- Every input is a distribution — triangular (min, mode, max) unless noted. Triangular is
  chosen deliberately: our sources justify a floor, a central value and a ceiling, not a
  parametric shape. No orphan parameters: each row below cites source IDs.
- Loaded hourly cost per role: `rate = total_cash_comp × load_multiplier / (weekly_hours × weeks_per_year)`.
  Using survey weekly hours (e.g., 74 h for IB analysts) in the denominator *lowers* the
  hourly rate versus a 40-h assumption — conservative by construction.

## Parameter table — compensation & rates

| Parameter | Distribution (min / mode / max) | Sources | Notes |
|---|---|---|---|
| IB analyst total cash comp (USD/yr) | tri(165k, 195k, 225k) | S10 | 25th–75th pct large-bank NY range; mode = midpoint |
| IB associate total cash comp | tri(285k, 390k, 500k) | S10 | same |
| IB VP total cash comp | tri(525k, 650k, 800k) | S10 | same |
| PE associate total cash comp | tri(180k, 244k, 300k) | S11 | LQ / mean / UQ, funds $1.0–1.49bn AUM, 2024; carry excluded. **Deliberate truncation:** S11 reports full low/high of $100k/$400k; we bound at the interquartile range, which narrows the PE rate spread (and hence the IC-deck cost distribution), and we use the mean as the triangular mode. Documented judgment |
| PE VP total cash comp | tri(300k, 378k, 450k) | S11 | same construction (LQ/mean/UQ), same truncation caveat |
| Consultant (post-MBA) total cash comp | tri(200k, 270k, 300k) | S12 | mode = BCG total ($270k); min stretches toward tier-2 firms; max $300k sits above Bain's $285k total to leave headroom for Bain plus part of the $30k signing bonus S12 reports separately |
| Consulting analyst (UG) total cash comp | tri(115k, 138k, 155k) | S12 | MBB undergrad totals ~137–140k |
| Load multiplier on cash comp | tri(1.15, 1.30, 1.45) | S13, S14 | BLS: benefits 29.9% of employer cost, but ECEC "benefits" includes bonuses we already count and excludes overhead; HR guides 1.25–1.4 on base. 1.30 mode on *total cash* is a middle path; documented judgment |
| Weeks worked per year | tri(46, 48, 50) | assumption | vacation/holiday allowance; flagged |
| IB analyst hours/week | tri(60, 74, 95) | S1, S2, S3, S4 | mode = WSO-2024 first-years (74.0); min anchored toward eFC all-seniority 53 (juniors above that); max = GS-2021 crisis tail (95–105) |
| IB associate hours/week | tri(60, 74, 85) | S1 | WSO 2024 associates 74.47 |
| IB VP hours/week | tri(50, 60, 70) | S1, S4 | assumption anchored to seniority decline + eFC average; flagged |
| PE associate hours/week | tri(55, 65, 80) | S1-family analogy, forum consensus | **assumption-heavy**, flagged; no A-grade PE hours survey found |
| PE VP hours/week | tri(50, 60, 70) | assumption | flagged |
| Consultant / consulting analyst hours/week | tri(48, 57, 70) | S6 | Consultancy.eu overtime data; MBB 50–65 consensus |

## Parameter table — deck effort

| Parameter | Distribution | Sources | Notes |
|---|---|---|---|
| Pitchbook pages | tri(15, 35, 90) | **assumption**; S17, S22, S15 (color) | No A/B-grade survey of pitchbook lengths exists. Mode 35 sits in the overlap of the S17 guide ranges (typical books 20–60 pages; sell-side M&A 30–50) and above the S22 filed-deck sample median (25 pages, n=21); min 15 covers the short board decks that dominate the S22 sample's lower half; max 90 covers appendix-heavy books approaching the ~100-page DealBreaker description quoted in S15. Widened from tri(20,40,80) in the fix pass; **results are conditional on this range** (see sensitivity §) |
| IC deck/memo pages | tri(15, 30, 60) | S18 | **thin family — assumption flagged**; IC materials often mix memo + deck |
| Consulting client deck pages | tri(25, 50, 100) | S19-family | practitioner guides; steering-committee decks; **assumption flagged** |
| First-draft (only) production hours per page (IB) | tri(0.25, 0.75, 1.5) | **assumption**; S16 (C), S20, S21, S7 | No A/B-grade effort-per-slide source exists; graded honestly, this is a judgment corroborated by agency guidance. Construction: agency benchmark 1–3 h per *finished* slide (S16) less the 1–2 embedded feedback rounds of 0.5–1 h it includes → ≈0.5–2 h first-draft-only, further discounted because 39% of decks build on existing decks and 56% on templates (S7) and banks reuse library pages; min 0.25 also reflects graphics-desk offloading; excludes analysis. S20 (1.2–3.0 h/slide *all-in*, incl. research and rehearsal) bounds it from above. **Results are conditional on this range** |
| First-draft hours per page (PE) | tri(0.25, 0.7, 1.5) | **assumption**; as above, S18 | as above |
| First-draft hours per page (consulting) | tri(0.35, 0.8, 1.6) | **assumption**; as above | consultants draw fewer library pages than banks; slightly higher mode and floor |
| Revision-churn factor (IB), × first-draft effort | tri(0.4, 0.9, 2.0) | S7, S9, S17 | 3–5+ revision cycles (S17); v44 tails (S9); the mode is consistent with S7's finding that 37% of PowerPoint time is formatting, though formatting is an imperfect proxy for churn (first drafts also involve formatting, and S7 is general-corporate, not IB) |
| Revision-churn factor (PE) | tri(0.3, 0.8, 1.8) | S18 | weeks of interim drafts before IC; thin, flagged |
| Revision-churn factor (consulting) | tri(0.4, 1.0, 2.0) | S7, S6 | iteration culture; steercos repaginated repeatedly |
| Senior-review share, × junior production hours | tri(0.15, 0.30, 0.50) | assumption (S17 color) | seniors mark up drafts repeatedly; priced at VP (IB/PE) or senior-consultant-multiple rate; flagged. **At the median this parameter accounts for roughly half of deck cost** — see the cost-composition section of RESULTS.md |
| IB junior production split analyst/associate | 70% / 30% fixed | assumption | flagged; sensitivity-tested implicitly via comp overlap |
| Consulting production split analyst/consultant | 60% / 40% fixed | assumption | flagged |
| Consulting reviewer rate multiple (× consultant rate) | uni(1.0, 1.6) | S12, S10 ratio logic | EM/partner comp not directly sourced; bounded by MBA/UG comp ratio ≈1.9 applied to consultant baseline vs consultant self-review |
| IB analyst share of work time on presentation production | tri(0.15, 0.30, 0.55) | **assumption**, colored by S7, S8, S9 | **weakest core parameter**, deliberately wide and widened downward in the fix pass. No A/B source supports a central value. Primary support is the bottom-up cross-check: at the model's own junior hours per book (median ≈ 73 h of draft+churn), an analyst carrying one full pitchbook-equivalent of junior effort every 2–6 weeks implies ≈16–49% of a 74-h week — essentially the distribution's span; practitioner accounts of several concurrent live books (S9, S17) make that cadence plausible without supporting any particular central value. Color: 10% of finance professionals report 4+ h/day in PowerPoint and 90% report *up to* 2 h/day (S8, C+, n=178, 2020, vendor-sponsored — a weak ceiling-type signal, not a floor); juniors in IB spend more time in PowerPoint than Excel (S9, C). Flagged and stress-tested in tornado; the annual seat/team outputs are **conditional estimates** on this parameter. In the team view the associate inherits the analyst time-share (additional unflagged-until-now assumption, now flagged) |
| Consulting analyst share of time on presentation production | tri(0.15, 0.30, 0.50) | **assumption**, colored by S7, S8, S6 | consulting-department PPT hours are the highest of any department in S7 (8 h/wk general-corporate); wide, flagged |

## Effort definition: first-draft-only, and the churn double-count question

`hrs_per_page` is defined as **first-draft-only** effort: the hours to take a page from
blank (or from a library/template starting point) to the first version that goes to a
senior for review. Revision effort is carried **exclusively** by the churn multiplier.
This matters because the S16 agency benchmark (1–3 h) describes *finished* slides and,
per S16's own text, includes 1–2 client-feedback rounds of 30–60 min each — i.e. the
benchmark embeds revision effort. Our discount from that benchmark therefore covers
**two** things: (a) stripping the embedded feedback rounds (≈0.5–2 h of the 1–3 h), and
(b) template/library reuse (39% of decks built on existing decks, 56% on templates —
S7; banks additionally reuse library pages). Bounding check: the resulting
tri(0.25, 0.75, 1.5) spans 12–75% of the midpoint of the finished-slide range, and its
mode (0.75 h) is 37% of the 2 h finished-slide midpoint — comfortably below the
first-draft-only share implied by stripping 1–2 embedded rounds, so first-draft effort
and churn are not obviously counted twice. The residual risk — that some revision
effort still leaks into the first-draft parameter — would bias costs **upward**; the
churn-share outputs (which depend on the *ratio* of churn to draft) would be biased
correspondingly. We flag rather than claim to eliminate this.

We also do **not** equate churn with formatting: S7's 37%-formatting share is quoted as
*consistent with* the churn mode, not as its derivation — first drafts involve
formatting too, and S7 measures general corporates, not IB.

## Outputs

1. **Cost per deck**, by archetype (IB pitchbook, PE IC deck, consulting client deck):
   full distributions; P10/P50/P90. (The IB archetype was renamed from "sell-side
   pitchbook" in the fix pass: the sourced length ranges span pitch types, and the S22
   primary sample is board/fairness materials, so the narrower label was not earned.)
2. **Hours per deck** decomposition: first draft → revision churn → senior review.
3. **Churn share**: revision cost / total deck cost.
4. **Annual presentation-production cost per junior seat** (IB analyst; consulting
   analyst): `total loaded comp × time-share` (weekly hours cancel algebraically —
   documented in code).
5. **Representative team/engagement view**: IB coverage group (4 analysts + 2
   associates + VP review overhead — associates inherit the analyst time-share, an
   assumption); consulting engagement month (6-person team, S19 $500k/month price as
   context). The consulting engagement month applies the review share at **half
   weight** (`review_share × 0.5`) and prices review at the junior blended rate rather
   than the 1.0–1.6× reviewer multiple used in the deck model — a deliberate
   conservative simplification for a view where much month-level review happens inside
   the team's own hours; both choices bias this figure downward.
6. **Tornado sensitivity**: change in median pitchbook cost when each parameter is
   pinned at its own P10 / P90 while all others resample freely. The tornado's base
   median is computed from the same random draws the pinned runs use (SEED+1), so bars
   and base line share a sampling basis; it differs from the headline SEED-draw median
   by ~0.1% at n = 200,000.
7. **Persisted scenario outputs** (`results/derived.json`): a true halving of
   first-draft effort per page; all comp-side parameters pinned at their P10
   simultaneously; like-for-like swing ratios of volume levers vs comp levers. Every
   scenario quoted in RESULTS.md traces to this file.

## Cross-checks

- Implied pitchbooks per analyst-year = annual presentation hours ÷ junior hours per
  pitchbook — reported and sanity-checked against practitioner accounts (S9, S17)
  and the corporate baseline of 12 presentations/month (S7; corporate decks are far
  smaller, so IB deck-equivalents must come out far lower).
- Cost per deck-hour reported separately so readers can recompose our arithmetic.

## Honesty rules

- C-grade sources never set a parameter alone; where a family is thin (deck geometry,
  effort per page, time-share, IC memos, PE hours), the parameter is labeled an
  **assumption** in the table above, carries a wide distribution, and results inherit
  the caveat in `RESULTS.md` and `LIMITATIONS.md`. Headline outputs that depend on an
  assumption-labeled parameter are quoted as **conditional estimates**.
- Rounding: 2 significant figures everywhere in prose.
- Model outputs are labeled as model estimates, never as measurements.
