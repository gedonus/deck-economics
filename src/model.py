"""Monte Carlo model of deck-production economics in IB / PE / consulting.

Every input distribution is documented in METHODOLOGY.md and tied to source IDs
in SOURCES.md. Outputs are model estimates, not measurements.

Run:  .venv/bin/python src/model.py
Writes: results/*.json, results/*.csv, results/chart-data/*.json
"""

import csv
import json
from pathlib import Path

import numpy as np

SEED = 20260706
N = 200_000

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"
CHART_DATA = RESULTS / "chart-data"
RESULTS.mkdir(exist_ok=True)
CHART_DATA.mkdir(exist_ok=True)

rng = np.random.default_rng(SEED)


def tri(lo, mode, hi, n=N, r=None):
    return (r or rng).triangular(lo, mode, hi, n)


# ---------------------------------------------------------------------------
# Parameters (min, mode, max) — see METHODOLOGY.md table for source IDs
# ---------------------------------------------------------------------------

PARAMS = {
    # compensation, USD/yr total cash [S10, S11, S12]
    "ib_analyst_comp": (165_000, 195_000, 225_000),
    "ib_associate_comp": (285_000, 390_000, 500_000),
    "ib_vp_comp": (525_000, 650_000, 800_000),
    "pe_associate_comp": (180_000, 244_000, 300_000),
    "pe_vp_comp": (300_000, 378_000, 450_000),
    "consultant_comp": (200_000, 270_000, 300_000),
    "consulting_analyst_comp": (115_000, 138_000, 155_000),
    # cost loading and calendar [S13, S14; assumption]
    "load": (1.15, 1.30, 1.45),
    "weeks": (46, 48, 50),
    # weekly hours [S1-S6]
    "ib_analyst_hours": (60, 74, 95),
    "ib_associate_hours": (60, 74, 85),
    "ib_vp_hours": (50, 60, 70),
    "pe_associate_hours": (55, 65, 80),
    "pe_vp_hours": (50, 60, 70),
    "consultant_hours": (48, 57, 70),
    # deck geometry [ASSUMPTION, corroborated by S15, S17, S22; see METHODOLOGY]
    "pitchbook_pages": (15, 35, 90),
    "ic_pages": (15, 30, 60),
    "consulting_pages": (25, 50, 100),
    # first-draft-only effort per page [ASSUMPTION, corroborated by S16 (C), S20, S21, S7]
    "ib_hrs_per_page": (0.25, 0.75, 1.50),
    "pe_hrs_per_page": (0.25, 0.70, 1.50),
    "cons_hrs_per_page": (0.35, 0.80, 1.60),
    # revision churn as multiple of first-draft effort [S7, S9, S17, S18]
    "ib_churn": (0.40, 0.90, 2.00),
    "pe_churn": (0.30, 0.80, 1.80),
    "cons_churn": (0.40, 1.00, 2.00),
    # senior review share of junior production hours [assumption, S17 color]
    "review_share": (0.15, 0.30, 0.50),
    # share of junior work time spent on presentation production
    # [ASSUMPTION, colored by S7, S8, S9 — see METHODOLOGY; widened downward in fix pass]
    "ib_timeshare": (0.15, 0.30, 0.55),
    "cons_timeshare": (0.15, 0.30, 0.50),
}

FIXED = {
    "ib_split_analyst": 0.70,       # analyst share of junior production hours
    "cons_split_analyst": 0.60,     # consulting analyst share
}


def draw_all(r):
    return {k: tri(*v, r=r) for k, v in PARAMS.items()}


def hourly_rate(comp, load, hours_pw, weeks):
    return comp * load / (hours_pw * weeks)


def deck_cost(d, kind):
    """Return dict of per-draw arrays: hours + cost decomposition for one archetype."""
    if kind == "pitchbook":
        pages, hpp, churn = d["pitchbook_pages"], d["ib_hrs_per_page"], d["ib_churn"]
        junior_rate = (
            FIXED["ib_split_analyst"]
            * hourly_rate(d["ib_analyst_comp"], d["load"], d["ib_analyst_hours"], d["weeks"])
            + (1 - FIXED["ib_split_analyst"])
            * hourly_rate(d["ib_associate_comp"], d["load"], d["ib_associate_hours"], d["weeks"])
        )
        review_rate = hourly_rate(d["ib_vp_comp"], d["load"], d["ib_vp_hours"], d["weeks"])
    elif kind == "ic_deck":
        pages, hpp, churn = d["ic_pages"], d["pe_hrs_per_page"], d["pe_churn"]
        junior_rate = hourly_rate(d["pe_associate_comp"], d["load"], d["pe_associate_hours"], d["weeks"])
        review_rate = hourly_rate(d["pe_vp_comp"], d["load"], d["pe_vp_hours"], d["weeks"])
    elif kind == "consulting_deck":
        pages, hpp, churn = d["consulting_pages"], d["cons_hrs_per_page"], d["cons_churn"]
        junior_rate = (
            FIXED["cons_split_analyst"]
            * hourly_rate(d["consulting_analyst_comp"], d["load"], d["consultant_hours"], d["weeks"])
            + (1 - FIXED["cons_split_analyst"])
            * hourly_rate(d["consultant_comp"], d["load"], d["consultant_hours"], d["weeks"])
        )
        mult = rng.uniform(1.0, 1.6, len(pages))  # reviewer rate multiple, see METHODOLOGY
        review_rate = mult * hourly_rate(d["consultant_comp"], d["load"], d["consultant_hours"], d["weeks"])
    else:
        raise ValueError(kind)

    draft_hours = pages * hpp
    churn_hours = draft_hours * churn
    production_hours = draft_hours + churn_hours
    review_hours = production_hours * d["review_share"]
    total_hours = production_hours + review_hours

    draft_cost = draft_hours * junior_rate
    churn_cost = churn_hours * junior_rate
    review_cost = review_hours * review_rate
    total_cost = draft_cost + churn_cost + review_cost

    return {
        "draft_hours": draft_hours,
        "churn_hours": churn_hours,
        "review_hours": review_hours,
        "total_hours": total_hours,
        "draft_cost": draft_cost,
        "churn_cost": churn_cost,
        "review_cost": review_cost,
        "junior_cost": draft_cost + churn_cost,  # junior-rate floor (no senior review)
        "total_cost": total_cost,
        "churn_share_of_cost": churn_cost / total_cost,
        "churn_share_of_hours": churn_hours / total_hours,
        # churn cost plus the slice of senior review triggered by churned pages
        "churn_attributable_cost_share": (
            churn_cost + review_cost * (churn_hours / production_hours)
        ) / total_cost,
        "blended_rate": total_cost / total_hours,
    }


def pct(a, qs=(10, 50, 90)):
    return {f"p{q}": float(np.percentile(a, q)) for q in qs}


def summarize(res):
    return {k: pct(v) for k, v in res.items()}


# ---------------------------------------------------------------------------
# Main simulation
# ---------------------------------------------------------------------------

draws = draw_all(rng)
decks = {kind: deck_cost(draws, kind) for kind in ("pitchbook", "ic_deck", "consulting_deck")}

# Annual presentation-production cost per junior seat.
# rate × weekly_hours × weeks = comp × load, so annual cost = comp × load × timeshare.
annual = {
    "ib_analyst_seat": draws["ib_analyst_comp"] * draws["load"] * draws["ib_timeshare"],
    "consulting_analyst_seat": draws["consulting_analyst_comp"] * draws["load"] * draws["cons_timeshare"],
}

# Representative IB coverage group: 4 analysts + 2 associates producing, VP review on top.
ib_analyst_annual = draws["ib_analyst_comp"] * draws["load"] * draws["ib_timeshare"]
ib_assoc_annual = draws["ib_associate_comp"] * draws["load"] * draws["ib_timeshare"]
vp_rate = hourly_rate(draws["ib_vp_comp"], draws["load"], draws["ib_vp_hours"], draws["weeks"])
junior_prod_hours_team = (
    4 * draws["ib_timeshare"] * draws["ib_analyst_hours"] * draws["weeks"]
    + 2 * draws["ib_timeshare"] * draws["ib_associate_hours"] * draws["weeks"]
)
team_annual = (
    4 * ib_analyst_annual + 2 * ib_assoc_annual
    + junior_prod_hours_team * draws["review_share"] * vp_rate
)

# Cross-check: implied pitchbook-equivalents per IB analyst-year
analyst_annual_prod_hours = draws["ib_timeshare"] * draws["ib_analyst_hours"] * draws["weeks"]
junior_hours_per_book = decks["pitchbook"]["draft_hours"] + decks["pitchbook"]["churn_hours"]
books_per_analyst_year = analyst_annual_prod_hours / junior_hours_per_book

# Consulting engagement month: 6-person team (3 analysts, 3 consultants modeled via split),
# deck production cost for one month vs S19 ~$500k/month price (context only).
cons_junior_rate = (
    FIXED["cons_split_analyst"]
    * hourly_rate(draws["consulting_analyst_comp"], draws["load"], draws["consultant_hours"], draws["weeks"])
    + (1 - FIXED["cons_split_analyst"])
    * hourly_rate(draws["consultant_comp"], draws["load"], draws["consultant_hours"], draws["weeks"])
)
cons_month_prod_hours = 6 * draws["cons_timeshare"] * draws["consultant_hours"] * (52 / 12.0)
cons_month_deck_cost = cons_month_prod_hours * cons_junior_rate * (1 + draws["review_share"] * 0.5)

summary = {
    "meta": {
        "seed": SEED,
        "n_draws": N,
        "note": "All figures are model estimates (USD). See METHODOLOGY.md and SOURCES.md.",
    },
    "decks": {k: summarize(v) for k, v in decks.items()},
    "annual_seat_cost": {k: pct(v) for k, v in annual.items()},
    "ib_team_annual_cost_4a2a_plus_vp_review": pct(team_annual),
    "books_per_analyst_year_crosscheck": pct(books_per_analyst_year),
    "consulting_engagement_month_deck_cost": pct(cons_month_deck_cost),
}

(RESULTS / "summary.json").write_text(json.dumps(summary, indent=2))

# Per-deck percentile CSV
with open(RESULTS / "deck_percentiles.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["deck_type", "metric", "p10", "p50", "p90"])
    for kind, res in decks.items():
        for metric, arr in res.items():
            p = pct(arr)
            w.writerow([kind, metric, round(p["p10"], 2), round(p["p50"], 2), round(p["p90"], 2)])

# ---------------------------------------------------------------------------
# Tornado sensitivity on median pitchbook cost
# ---------------------------------------------------------------------------

TORNADO_PARAMS = [
    ("pitchbook_pages", "Pitchbook length (pages)"),
    ("ib_hrs_per_page", "First-draft hours per page"),
    ("ib_churn", "Revision-churn factor"),
    ("ib_analyst_comp", "Analyst total comp"),
    ("ib_associate_comp", "Associate total comp"),
    ("ib_vp_comp", "VP total comp"),
    ("ib_analyst_hours", "Analyst weekly hours"),
    ("load", "Cost-loading multiplier"),
    ("review_share", "Senior-review share"),
    ("weeks", "Weeks worked per year"),
]

# Base median for the tornado is computed from the SEED+1 draws — the same
# randomness every pinned run uses — so pins and base share a sampling basis.
# (The SEED-draw headline median in summary.json differs by ~0.1% at n=200k.)
base_draws_t = draw_all(np.random.default_rng(SEED + 1))
base_median = float(np.median(deck_cost(base_draws_t, "pitchbook")["total_cost"]))
tornado = []
for key, label in TORNADO_PARAMS:
    lo_v, mode_v, hi_v = PARAMS[key]
    row = {"param": key, "label": label}
    for tag, q in (("low", 10), ("high", 90)):
        r2 = np.random.default_rng(SEED + 1)  # same randomness for all pins
        d2 = draw_all(r2)
        pin = float(np.percentile(tri(lo_v, mode_v, hi_v, r=np.random.default_rng(7)), q))
        d2[key] = np.full(N, pin)
        # deck_cost uses module-level rng for the consulting reviewer multiple only;
        # pitchbook path is deterministic given d2.
        c2 = deck_cost(d2, "pitchbook")
        row[tag] = float(np.median(c2["total_cost"]))
    row["swing"] = abs(row["high"] - row["low"])
    tornado.append(row)

tornado.sort(key=lambda r: -r["swing"])
tornado_out = {"base_median": base_median, "rows": tornado}

# ---------------------------------------------------------------------------
# Derived scenario outputs — persisted so every prose claim traces to a file
# ---------------------------------------------------------------------------

headline_median = float(np.median(decks["pitchbook"]["total_cost"]))

# Scenario 1: true halving of first-draft effort per page (SEED draws).
# Every cost component scales linearly in hrs-per-page, so this halves cost per draw.
halved = dict(draws)
halved["ib_hrs_per_page"] = draws["ib_hrs_per_page"] * 0.5
halved_median = float(np.median(deck_cost(halved, "pitchbook")["total_cost"]))

# Scenario 2: every comp-side parameter (three comps + loading) pinned at its own
# P10 simultaneously, volume parameters resampled freely (SEED+1 basis, as tornado).
COMP_PARAMS = ["ib_analyst_comp", "ib_associate_comp", "ib_vp_comp", "load"]
d3 = draw_all(np.random.default_rng(SEED + 1))
for key in COMP_PARAMS:
    lo_v, mode_v, hi_v = PARAMS[key]
    pin = float(np.percentile(tri(lo_v, mode_v, hi_v, r=np.random.default_rng(7)), 10))
    d3[key] = np.full(N, pin)
all_comp_p10_median = float(np.median(deck_cost(d3, "pitchbook")["total_cost"]))

# Like-for-like swing ratios: volume levers vs comp levers (P10–P90 swings, tornado).
t_by_key = {r["param"]: r for r in tornado}
VOLUME_LEVERS = ["ib_hrs_per_page", "pitchbook_pages", "ib_churn", "review_share"]
swing_ratios = {
    ref: {
        k: round(t_by_key[k]["swing"] / t_by_key[ref]["swing"], 2)
        for k in VOLUME_LEVERS
    }
    for ref in ("ib_vp_comp", "ib_analyst_comp")
}

derived = {
    "note": (
        "Persisted scenario outputs backing RESULTS.md prose. Halving scenario uses "
        "the SEED draws; pinned scenarios use the SEED+1 basis like the tornado."
    ),
    "pitchbook_median_base": headline_median,
    "halve_ib_hrs_per_page": {
        "median": halved_median,
        "delta_vs_base": headline_median - halved_median,
    },
    "pin_ib_hrs_per_page_p10": {
        "median": t_by_key["ib_hrs_per_page"]["low"],
        "delta_vs_tornado_base": base_median - t_by_key["ib_hrs_per_page"]["low"],
    },
    "pin_ib_analyst_comp_p10": {
        "median": t_by_key["ib_analyst_comp"]["low"],
        "delta_vs_tornado_base": base_median - t_by_key["ib_analyst_comp"]["low"],
    },
    "pin_all_comp_params_p10": {
        "params": COMP_PARAMS,
        "median": all_comp_p10_median,
    },
    "swing_ratio_volume_levers_vs": swing_ratios,
}
(RESULTS / "derived.json").write_text(json.dumps(derived, indent=2))

# ---------------------------------------------------------------------------
# Chart-data JSONs (underlying data for every figure — mandatory)
# ---------------------------------------------------------------------------

def hist_data(arr, bins=60, clip_pct=99.5):
    hi = np.percentile(arr, clip_pct)
    counts, edges = np.histogram(arr[arr <= hi], bins=bins, density=True)
    return {"bin_edges": [float(x) for x in edges], "density": [float(x) for x in counts]}

chart_cost_dist = {
    "title": "Cost per deck (model estimate, USD)",
    "series": {
        kind: {
            "histogram": hist_data(decks[kind]["total_cost"]),
            "percentiles": pct(decks[kind]["total_cost"]),
        }
        for kind in decks
    },
}
(CHART_DATA / "cost_distributions.json").write_text(json.dumps(chart_cost_dist, indent=2))

wf = {
    "title": "Hours per sell-side pitchbook (median, model estimate)",
    "steps": [
        {"label": "First draft", "hours": float(np.median(decks["pitchbook"]["draft_hours"]))},
        {"label": "Revision churn", "hours": float(np.median(decks["pitchbook"]["churn_hours"]))},
        {"label": "Senior review", "hours": float(np.median(decks["pitchbook"]["review_hours"]))},
    ],
    "note": "Median of each component; component medians need not sum exactly to the median total.",
    "median_total": float(np.median(decks["pitchbook"]["total_hours"])),
}
(CHART_DATA / "hours_waterfall.json").write_text(json.dumps(wf, indent=2))
(CHART_DATA / "tornado.json").write_text(json.dumps(tornado_out, indent=2))

cost_comp = {
    "title": "Cost composition per deck (median of each component, USD)",
    "note": (
        "Component medians; they need not sum exactly to the median total. "
        "Senior review is priced at VP (IB/PE) or senior-consultant rates; the "
        "review-share parameter is an assumption (tri 0.15/0.30/0.50)."
    ),
    "series": {
        kind: {
            "draft_cost_median": float(np.median(decks[kind]["draft_cost"])),
            "churn_cost_median": float(np.median(decks[kind]["churn_cost"])),
            "review_cost_median": float(np.median(decks[kind]["review_cost"])),
            "junior_cost_percentiles": pct(decks[kind]["junior_cost"]),
            "total_cost_percentiles": pct(decks[kind]["total_cost"]),
        }
        for kind in decks
    },
}
(CHART_DATA / "cost_composition.json").write_text(json.dumps(cost_comp, indent=2))

print(json.dumps(summary, indent=2))
