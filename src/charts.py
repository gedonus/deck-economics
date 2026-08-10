"""Publication figures for the deck-economics study.

Reads results/chart-data/*.json (written by model.py) so every figure's
underlying data ships alongside it. Light surface, validated reference palette
(fixed categorical order), thin marks, recessive chrome.

Run:  .venv/bin/python src/charts.py
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
CHART_DATA = ROOT / "results" / "chart-data"
FIGURES = ROOT / "results" / "figures"
FIGURES.mkdir(exist_ok=True)

# Reference palette (validated set, fixed slot order; light mode)
SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK2 = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
BASE = "#c3c2b7"
SERIES = {"pitchbook": "#2a78d6", "ic_deck": "#1baf7a", "consulting_deck": "#eda100"}
LABELS = {
    "pitchbook": "Pitchbook (IB)",
    "ic_deck": "IC deck / memo (PE)",
    "consulting_deck": "Client deck (consulting)",
}
SEQ = ["#86b6ef", "#3987e5", "#1c5cab", "#0d366b"]  # sequential blue, ordinal-safe
DIV_LO, DIV_HI = "#2a78d6", "#e34948"  # diverging pair

plt.rcParams.update({
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica Neue", "Arial", "DejaVu Sans"],
    "text.color": INK,
    "axes.edgecolor": BASE,
    "axes.labelcolor": INK2,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "axes.grid": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.spines.left": False,
    "font.size": 11,
})


def kfmt(x):
    return f"${x/1000:.0f}k" if x >= 1000 else f"${x:.0f}"


# ---------------------------------------------------------------------------
# Figure 1 — cost-per-deck distributions (small multiples, one series each)
# ---------------------------------------------------------------------------

data = json.loads((CHART_DATA / "cost_distributions.json").read_text())
fig, axes = plt.subplots(3, 1, figsize=(8.6, 8.2), sharex=True)
fig.subplots_adjust(hspace=0.50, top=0.87, bottom=0.09, left=0.06, right=0.97)

for ax, kind in zip(axes, ("pitchbook", "ic_deck", "consulting_deck")):
    s = data["series"][kind]
    edges = np.array(s["histogram"]["bin_edges"])
    dens = np.array(s["histogram"]["density"])
    centers = (edges[:-1] + edges[1:]) / 2
    ax.fill_between(centers, dens, color=SERIES[kind], alpha=0.10, linewidth=0)
    ax.plot(centers, dens, color=SERIES[kind], linewidth=2, solid_joinstyle="round")
    p = s["percentiles"]
    ymax = dens.max()
    for q, lbl in (("p10", "P10"), ("p50", "P50"), ("p90", "P90")):
        ax.vlines(p[q], 0, ymax * (1.04 if q == "p50" else 0.75), color=BASE, linewidth=1)
        ax.annotate(
            f"{lbl}  {kfmt(p[q])}",
            (p[q], ymax * (1.06 if q == "p50" else 0.78)),
            ha="center", fontsize=9,
            color=INK if q == "p50" else INK2,
            fontweight="bold" if q == "p50" else "normal",
        )
    ax.set_title(LABELS[kind], loc="left", fontsize=11.5, color=INK, pad=14, fontweight="bold")
    ax.set_yticks([])
    ax.set_ylim(0, ymax * 1.28)
    ax.grid(axis="x", color=GRID, linewidth=1)
    ax.set_axisbelow(True)

axes[-1].set_xlim(0, 45000)
axes[-1].set_xticks(range(0, 45001, 5000))
axes[-1].set_xticklabels([kfmt(x) for x in range(0, 45001, 5000)])
axes[-1].set_xlabel("Fully-loaded production cost per deck (USD, model estimate)")
fig.suptitle("What a single deck costs to produce", x=0.06, y=0.975, ha="left",
             fontsize=15, fontweight="bold", color=INK)
fig.text(0.06, 0.935, "Monte Carlo model estimate; production and review of the document only, "
         "excluding underlying analysis. Seed 20260706, n = 200,000.",
         fontsize=9, color=MUTED)
fig.savefig(FIGURES / "cost_per_deck_distributions.png", dpi=200)
plt.close(fig)

# ---------------------------------------------------------------------------
# Figure 2 — tornado sensitivity (diverging around base median)
# ---------------------------------------------------------------------------

t = json.loads((CHART_DATA / "tornado.json").read_text())
rows = t["rows"]
base = t["base_median"]

fig, ax = plt.subplots(figsize=(8.6, 5.4))
fig.subplots_adjust(left=0.30, right=0.95, top=0.86, bottom=0.12)
ys = np.arange(len(rows))[::-1]
for y, r in zip(ys, rows):
    lo, hi = r["low"], r["high"]
    left, right = min(lo, base), max(hi, base)
    ax.barh(y, base - left, left=left, height=0.52, color=DIV_LO,
            edgecolor=SURFACE, linewidth=2)
    ax.barh(y, right - base, left=base, height=0.52, color=DIV_HI,
            edgecolor=SURFACE, linewidth=2)
    ax.annotate(kfmt(min(lo, hi)), (left, y), xytext=(-6, 0), textcoords="offset points",
                ha="right", va="center", fontsize=9, color=INK2)
    ax.annotate(kfmt(max(lo, hi)), (right, y), xytext=(6, 0), textcoords="offset points",
                ha="left", va="center", fontsize=9, color=INK2)
ax.vlines(base, -0.6, len(rows) - 0.4, color=INK, linewidth=1)
ax.annotate(f"base median {kfmt(base)}", (base, len(rows) - 0.28), ha="center",
            fontsize=9, color=INK, fontweight="bold")
ax.set_yticks(ys)
ax.set_yticklabels([r["label"] for r in rows], fontsize=10, color=INK)
xlo = 3000 * int(min(min(r["low"], r["high"]) for r in rows) // 3000)
xhi = 3000 * (int(max(max(r["low"], r["high"]) for r in rows) // 3000) + 1)
ax.set_xlim(xlo, xhi)
ax.set_xticks(range(xlo, xhi + 1, 3000))
ax.set_xticklabels([kfmt(x) for x in range(xlo, xhi + 1, 3000)])
ax.grid(axis="x", color=GRID, linewidth=1)
ax.set_axisbelow(True)
ax.tick_params(length=0)
ax.set_xlabel("Median pitchbook cost when parameter pinned at its P10 (blue) / P90 (red)")
fig.suptitle("What moves the cost of a pitchbook", x=0.06, ha="left",
             fontsize=15, fontweight="bold", color=INK)
fig.text(0.06, 0.90, "One-at-a-time sensitivity: each parameter pinned at its own P10/P90, "
         "all others resampled. Model estimate.", fontsize=9, color=MUTED)
fig.savefig(FIGURES / "tornado_pitchbook.png", dpi=200)
plt.close(fig)

# ---------------------------------------------------------------------------
# Figure 3 — hours-decomposition waterfall (ordinal sequential ramp)
# ---------------------------------------------------------------------------

wf = json.loads((CHART_DATA / "hours_waterfall.json").read_text())
steps = wf["steps"]
cum_total = sum(s["hours"] for s in steps)   # top of the stacked component bars
total = wf["median_total"]                    # true median of the total distribution

fig, ax = plt.subplots(figsize=(8.6, 4.6))
fig.subplots_adjust(left=0.07, right=0.97, top=0.82, bottom=0.10)
cum = 0.0
xs = np.arange(len(steps) + 1)
for i, s in enumerate(steps):
    ax.bar(i, s["hours"], bottom=cum, width=0.56, color=SEQ[i],
           edgecolor=SURFACE, linewidth=2)
    ax.annotate(f"{s['hours']:.0f} h", (i, cum + s["hours"] / 2), ha="center",
                va="center", fontsize=10, fontweight="bold",
                color="#ffffff" if i >= 1 else INK)
    cum += s["hours"]
    if i < len(steps) - 1:
        ax.hlines(cum, i + 0.28, i + 1 - 0.28, color=BASE, linewidth=1)
ax.hlines(cum, len(steps) - 1 + 0.28, len(steps) - 0.28, color=BASE, linewidth=1)
ax.bar(len(steps), total, width=0.56, color=SEQ[3], edgecolor=SURFACE, linewidth=2)
ax.annotate(f"{total:.0f} h", (len(steps), total / 2), ha="center", va="center",
            fontsize=11, fontweight="bold", color="#ffffff")
ax.set_xticks(xs)
ax.set_xticklabels([s["label"] for s in steps] + ["Total per book"], fontsize=10.5, color=INK)
ax.set_ylim(0, max(total, cum_total) * 1.18)
ax.set_yticks(range(0, int(max(total, cum_total) * 1.15), 25))
ax.grid(axis="y", color=GRID, linewidth=1)
ax.set_axisbelow(True)
ax.tick_params(length=0)
ax.set_ylabel("Team hours (median of each component)")
fig.suptitle("Where the hours in a pitchbook go", x=0.06, ha="left",
             fontsize=15, fontweight="bold", color=INK)
fig.text(0.06, 0.88, "IB pitchbook, median hours; total bar = median of the total "
         "distribution (components need not sum to it). Model estimate.",
         fontsize=9, color=MUTED)
fig.savefig(FIGURES / "hours_waterfall_pitchbook.png", dpi=200)
plt.close(fig)

# ---------------------------------------------------------------------------
# Figure 4 — cost composition per deck (stacked bars, median components)
# ---------------------------------------------------------------------------

cc = json.loads((CHART_DATA / "cost_composition.json").read_text())
kinds = ["pitchbook", "ic_deck", "consulting_deck"]
COMPONENTS = [
    ("draft_cost_median", "First draft (junior rate)", SEQ[0]),
    ("churn_cost_median", "Revision churn (junior rate)", SEQ[1]),
    ("review_cost_median", "Senior review (VP / senior rate)", SEQ[3]),
]

fig, ax = plt.subplots(figsize=(8.6, 4.4))
fig.subplots_adjust(left=0.24, right=0.95, top=0.70, bottom=0.14)
ys = np.arange(len(kinds))[::-1]
for y, kind in zip(ys, kinds):
    s = cc["series"][kind]
    left = 0.0
    for key, _, color in COMPONENTS:
        v = s[key]
        ax.barh(y, v, left=left, height=0.5, color=color, edgecolor=SURFACE, linewidth=2)
        share = v / sum(s[k] for k, _, _ in COMPONENTS)
        if share > 0.10:
            ax.annotate(f"{kfmt(v)}", (left + v / 2, y), ha="center", va="center",
                        fontsize=9, fontweight="bold",
                        color="#ffffff" if color != SEQ[0] else INK)
        left += v
ax.set_yticks(ys)
ax.set_yticklabels([LABELS[k] for k in kinds], fontsize=10, color=INK)
xmax = max(sum(cc["series"][k][key] for key, _, _ in COMPONENTS) for k in kinds)
ax.set_xlim(0, xmax * 1.12)
ax.set_xticks(range(0, int(xmax * 1.12) + 1, 3000))
ax.set_xticklabels([kfmt(x) for x in range(0, int(xmax * 1.12) + 1, 3000)])
ax.grid(axis="x", color=GRID, linewidth=1)
ax.set_axisbelow(True)
ax.tick_params(length=0)
ax.set_xlabel("Median cost of each component (USD, model estimate)")
handles = [plt.Rectangle((0, 0), 1, 1, color=c) for _, _, c in COMPONENTS]
ax.legend(handles, [lbl for _, lbl, _ in COMPONENTS], loc="lower left",
          bbox_to_anchor=(0.0, 1.02), ncol=3, frameon=False, fontsize=9)
fig.suptitle("Where the cost of a deck sits", x=0.06, y=0.97, ha="left",
             fontsize=15, fontweight="bold", color=INK)
fig.text(0.06, 0.875, "Median cost components (model estimate). Senior review is priced at VP / "
         "senior rates; its share (15–50%) is an assumption.",
         fontsize=9, color=MUTED)
fig.savefig(FIGURES / "cost_composition.png", dpi=200)
plt.close(fig)

print("figures written:", sorted(p.name for p in FIGURES.glob("*.png")))
