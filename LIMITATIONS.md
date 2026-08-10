# LIMITATIONS.md

Read this before quoting anything. In order of severity.

## 1. Model, not measurement
Every dollar figure in RESULTS.md is a **Monte Carlo estimate from assumed
distributions**, not an observed cost. No bank, fund, or consultancy gave us
timesheet data. The distributions are anchored to public sources, but the mapping
from "hours surveys + comp surveys + per-slide benchmarks" to "cost per deck" is
our construction. Independent replication would need internal time-tracking data
that, to our knowledge, has never been published.

## 2. The time-share parameter is an assumption — the weakest core input
The share of junior time spent on presentation *production* (IB: 15–55%) is an
**assumption**. Its color comes from (a) a vendor-sponsored finance survey with
n = 178, France-weighted, from 2020, whose PowerPoint stat is a *ceiling*-type signal
("90% report up to 2 h/day"; 10% report 4+ h/day) (S8, C+), (b) a general-corporate,
vendor-commissioned study with Nielsen fieldwork (S7) that is not elite-finance-
specific, and (c) a practitioner claim that junior bankers spend more time in
PowerPoint than Excel (S9, grade C). No A/B source supports any central value; the
primary support is the bottom-up cross-check in METHODOLOGY.md. The distribution is
deliberately wide, was widened downward in the fix pass, and feeds only the
annual/seat numbers, not cost-per-deck — any citation of the ≈$83k/analyst-year
median must carry this caveat and the P10–P90 range ($57k–110k).

## 3. Roughly half the headline deck cost is an assumed review share at VP rates
At the median, senior review is ≈ $6.7k of the $14k pitchbook total (≈ 49%). The
review-share parameter (15–50% of production hours) is an assumption, and it is
priced at the most expensive rate in the model (VP). The junior-rate-only subtotal
($3.3k / $6.8k / $13k) is the defensible floor; RESULTS.md §2 shows the full cost
composition. Quoting the $14k median without this composition overstates what the
sources can carry.

## 4. Deck geometry and per-page effort are assumptions
The two largest tornado drivers — pitchbook length tri(15, 35, 90) and first-draft
hours per page tri(0.25, 0.75, 1.5) — are assumption-labeled inputs corroborated only
by C-grade material (career-prep guides, agency FAQ pages, a practitioner book) plus
our own n = 21 primary sample of filed board/fairness decks (S22, a shorter genre).
All cost-per-deck outputs are conditional on these ranges. If real pitchbooks are
materially shorter or more template-driven than assumed, the headline halves; the P10
column is the honest lower read.

## 5. Survey self-selection everywhere
WSO working-conditions respondents are self-selected, skew junior, and their
professional status is unverified (stated in the report itself). The Goldman 2021
survey covered 13 self-selected analysts during a deal boom — we use it only as an
upper tail. Comp surveys (WSO, M&I, Heidrick, Management Consulted) all oversample
people motivated to report — typically at better-paying firms.

## 6. US/NY-centricity
Compensation sources are US (mostly New York) figures. London, Frankfurt, or
Singapore cost bases are materially lower (S4's data implies EU juniors earn less
and work somewhat less). Our dollar figures do not transfer outside top-tier US
finance without rescaling.

## 7. Dated and vendor-sponsored time-use studies
The two PowerPoint time-use studies (S7, S8) are from 2020 — pre-hybrid-work,
pre-genAI — and both were commissioned by vendors selling PowerPoint productivity
tools, who benefit from large numbers. Nielsen/CSA execution mitigates but does not
eliminate this. If time-in-PowerPoint has fallen since 2020, our annual figures are
overstated; if deck volume grew, understated.

## 8. Thin families, flagged
- **PE IC memo effort** (S18): C-grade vendor anecdotes and process descriptions.
  The IC-deck geometry (15/30/60 pages) is an assumption. Treat IC-deck outputs as
  the least reliable of the three archetypes.
- **PE working hours**: no A-grade public survey exists; we analogized from IB
  surveys and forum consensus.
- **Consulting deck size/volume**: practitioner guides, not surveys.
- **Deck volume per mandate**: we could not source pitchbooks-per-deal credibly, so
  no output depends on it (annual figures run through time-share instead).

## 9. Structural assumptions
Fixed production splits (70/30 analyst/associate in IB; 60/40 in consulting), the
senior-review share (15–50% of production hours, see §3), the consulting reviewer
rate multiple, and the team view's assumption that associates share the analyst
time-share are judgments, not sourced. The review-share and churn parameters
partially overlap conceptually (senior comments *cause* churn); we kept them separate
and show both attributions of churn cost (junior-rate-only medians ≈ 25–33%;
churn-attributable medians ≈ 48–53%) rather than picking the flattering one.

## 10. Scope cuts both ways
We exclude financial modeling, research, and diligence — which makes cost-per-deck
conservative — but we also price *all* production hours at junior/VP loaded rates;
if some production work is done by cheaper presentation-services staff (many banks
run overnight graphics desks), the true junior-hour cost could be lower for the
formatting slice. No public data on graphics-desk throughput exists to size this.

## 11. Triangular distributions
Triangular distributions with judgment-set modes are transparent but crude; they
have hard bounds and linear tails. Real effort distributions are likely
heavier-tailed on the right (all-nighter books, v44 decks). Our P90s are therefore,
if anything, understated for the extreme tail.

## 12. No behavioral response
The model prices current practice. It says nothing about how much of the churn is
*necessary* (real strategic iteration) versus waste (formatting, version confusion)
— S7's 37%-formatting stat hints at the split but cannot resolve it for finance.
