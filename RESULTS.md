# RESULTS.md — Deck-production economics (model estimates)

**Everything below is a model estimate**, produced by the seeded Monte Carlo simulation in
`src/model.py` (seed 20260706, n = 200,000), with every input distribution tied to graded
sources or explicitly labeled assumptions (`SOURCES.md`, `METHODOLOGY.md`). Values are
P10 / P50 / P90 of the simulated distributions, rounded to 2 significant figures. Raw
outputs: `results/summary.json`, `results/deck_percentiles.csv`, `results/derived.json`.
Scope: producing and reviewing the *document* (layout, charts, formatting, revisions,
senior markup) — underlying analysis excluded, so these are conservative floors for
"cost of the deliverable".

**Epistemic note:** P10/P90 express the spread implied by our input assumptions, not
statistical confidence intervals — they carry no sampling-error meaning. The two largest
cost drivers (deck length and first-draft effort per page) and the time-share parameter
are **assumptions** corroborated by C-grade sources, not sourced measurements; every
number below is conditional on those ranges (see METHODOLOGY.md).

## 1. Cost per deck

| Deck type | P10 | P50 | P90 | Team hours (P10/P50/P90) |
|---|---|---|---|---|
| Pitchbook (IB) | $6.6k | **$14k** | $26k | 48 / 97 / 180 h |
| IC deck / memo (PE)&nbsp;* | $4.1k | **$7.8k** | $14k | 36 / 68 / 120 h |
| Client deck (consulting) | $7.7k | **$14k** | $25k | 77 / 140 / 240 h |

\* Thin source family — treat the IC-deck row as the least reliable of the three
archetypes (LIMITATIONS §8).

Figure: `results/figures/cost_per_deck_distributions.png`
(data: `results/chart-data/cost_distributions.json`)

Blended loaded team rate implied by the model: IB **$120–160/h**, PE **$100–130/h**,
consulting **$87–120/h** (P10–P90). These are *costs*, not client billing rates —
an MBB engagement bills roughly $500k per team-month (S19), several multiples of cost.

## 2. Where the hours and the dollars go (median pitchbook)

Hours: first draft ≈ **36 h** → revision churn ≈ **37 h** → senior review ≈ **23 h** →
total ≈ **97 h** per book. (Component medians; they need not sum exactly to the
median of the total.)

Cost: first draft ≈ **$3.3k** → revision churn ≈ **$3.4k** → senior review ≈ **$6.7k**
(median components). **Roughly half of the median pitchbook cost is senior-review time
priced at VP rates — and the review-share parameter (15–50% of production hours) is an
assumption**, not a sourced number. The junior-rate-only subtotal (draft + churn, no
review) is a defensible floor: **$3.3k / $6.8k / $13k** (P10/P50/P90). For PE and
consulting decks the review slice is ≈ 35% of the median cost.

Figures: `results/figures/hours_waterfall_pitchbook.png`,
`results/figures/cost_composition.png`
(data: `results/chart-data/hours_waterfall.json`, `results/chart-data/cost_composition.json`)

## 3. Revision churn

Two attributions, shown side by side — quote them together:

- Churn (rework of already-drafted pages) consumes **27–47% of all deck hours**
  (P10–P90 across all three deck types; medians 37–40% by type).
- Priced at **junior rates only**, churn is **19–41% of deck cost** (medians
  **25–33%** by type).
- Attributing to churn a proportional share of the senior review it triggers, churn
  accounts for **36–62% of total production cost** (medians **48–53%** by type —
  roughly half). This attribution choice is ours; the junior-rate-only view above is
  the floor a skeptic should start from.

## 4. Annual presentation-production cost (conditional estimates)

These figures are driven by the **time-share parameter — an assumption, and the
weakest core input in the model** (see METHODOLOGY.md and LIMITATIONS §2). Quote them
only as ranges with that caveat.

| Unit | P10 | P50 | P90 |
|---|---|---|---|
| One IB analyst seat, per year | $57k | **$83k** | $110k |
| One consulting analyst seat, per year | $39k | **$55k** | $74k |
| IB coverage group (4 analysts + 2 associates + VP review), per year | $0.88M | **$1.3M** | $1.9M |
| Consulting engagement, deck production per team-month (6-person team) | $33k | **$47k** | $63k |

The per-seat figure is algebraically `loaded comp × share of time on presentation
production` — the weekly-hours terms cancel — so it is driven by the comp sources
(S10–S12), the loading (S13) and the time-share assumption (colored by S7–S9). The
coverage-group view additionally assumes associates share the analyst time-share.

For consulting, deck production of ≈ $47k per team-month compares to ≈ $500k/month
billed (S19): document production alone consumes on the order of **7–13% of engagement
price at cost** — before any of the analysis that fills the pages. (The engagement-month
view deliberately half-weights review — METHODOLOGY §Outputs — and inherits the C/B-
$500k price anchor; keep "on the order of".)

## 5. Sensitivity (tornado, median pitchbook cost ≈ $14k base)

Figure: `results/figures/tornado_pitchbook.png` (data: `results/chart-data/tornado.json`)

| Parameter (pinned at its own P10 / P90) | Median cost range | Swing |
|---|---|---|
| Pitchbook length (pages) | $8.5k – $22k | $13k |
| First-draft hours per page | $8.6k – $20k | $12k |
| Revision-churn factor | $11k – $17k | $5.9k |
| Senior-review share | $12k – $16k | $4.2k |
| Cost-loading multiplier | $13k – $15k | $1.7k |
| VP total comp | $13k – $14k | $1.6k |
| Associate / analyst comp, hours, weeks | ≤ $1.0k each | — |

**Reading:** deck cost is dominated by *how much gets built and rebuilt* (length,
effort per page, churn, review), not by pay levels. Note the two dominant levers are
also the model's two assumption-labeled geometry/effort inputs — the tornado is as much
an uncertainty ranking as a leverage ranking. All scenario numbers below are persisted
in `results/derived.json`:

- Even pinning **every comp-side parameter** (analyst, associate and VP comp, plus the
  loading multiplier) at its P10 simultaneously leaves a median pitchbook of **$11k**.
- Measured swing against swing, the volume levers (pages, effort/page, churn, review
  share) carry **2.7–8.4×** the P10–P90 swing of the largest single compensation
  parameter (VP total comp), and **6.9–22×** the swing of analyst comp. (The loading
  multiplier, also a comp-side input, swings $1.7k — still below every volume lever.)
- Pinning first-draft effort per page at its own P10 moves the median by ≈ **$5.1k**;
  a **true halving** of effort per page halves the median cost per draw, moving it by
  ≈ **$6.8k** (to ≈ $6.8k — cost scales linearly in effort per page).

## 6. Cross-check

Implied pitchbook-equivalents per IB analyst-year: **7.8 – 16 – 35** (P10/P50/P90).
The median (≈ 1.3 full books' junior effort per month) sits *below* practitioner
folklore of juniors touching several live books per month (S9, S17) — consistent in
order of magnitude if several concurrent books share one analyst's effort, and
conservative relative to taking the folklore literally. It is also coherent with the
corporate baseline of ~12 (much smaller) presentations per PowerPoint-using
employee-month (S7).

## Candidate headline statistics

1. A single IB pitchbook costs **≈ $6.6k–26k (median ≈ $14k)** in fully-loaded team
   time to produce — before any of the analysis behind it. Model estimate conditional
   on assumption-labeled geometry/effort inputs; roughly half of the median is
   senior-review time at VP rates, and the junior-rate floor is ≈ $3.3k–13k
   (median $6.8k).
2. A pitchbook consumes **≈ 97 team-hours at the median** (P10–P90: 48–180 h) —
   model estimate, same conditions as #1.
3. Rework consumes **27–47% of deck hours**. Priced at junior rates that is
   **19–41% of deck cost (medians 25–33%)**; attributing the senior review of
   reworked pages to churn as well raises it to **36–62% (medians 48–53%)**. Always
   quote both attributions.
4. One IB analyst seat represents **≈ $57k–110k/year of presentation-production cost
   (median ≈ $83k)** — conditional estimate; the driving time-share parameter is an
   assumption (LIMITATIONS §2).
5. An IB coverage group of six juniors plus VP review burns **≈ $0.88–1.9M per year
   (median ≈ $1.3M)** on deck production — same conditionality as #4.
6. Deck cost is driven by pages built and rebuilt, not pay: the P10–P90 swing of
   first-draft effort per page (≈ $12k) is ≈ **19×** the swing of analyst comp
   (≈ $0.6k), and pinning every comp parameter at its P10 still leaves a **$11k**
   median book (`results/derived.json`).
7. In a 2020 vendor-sponsored survey of finance professionals (UpSlide/CSA, n = 178,
   France-weighted), **10% reported 4+ hours per day in PowerPoint, 30% reported 4+
   hours per day in Excel, and 86% said they lack time for core work** — source stats,
   grade C+, not model outputs.
8. First-year IB analysts averaged **74-hour weeks** in the latest WSO survey
   (n = 531, Jan 2025 — source stat, grade A, not model output).
