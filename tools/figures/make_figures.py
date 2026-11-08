#!/usr/bin/env python3
"""Report figures from the pulled datasets (World Bank Pink Sheet, UN Comtrade) and the scenario table."""
import csv, os, collections
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "report", "fig"); os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.family": "Liberation Serif", "font.size": 10, "axes.spines.top": False, "axes.spines.right": False,
                     "svg.fonttype": "none", "axes.edgecolor": "#555", "axes.labelcolor": "#000"})
ACC, GREY = "#1F4E79", "#9AA5B1"

# Figure 1: nickel price, annual average, World Bank Pink Sheet
rows = [r for r in csv.DictReader(open(os.path.join(ROOT, "data/clean/worldbank_pinksheet_monthly.csv"))) if r["commodity"].startswith("Nickel")]
by = collections.defaultdict(list)
for r in rows:
    y = int(r["month"][:4])
    if y >= 2010: by[y].append(float(r["price"]))
ys = sorted(by); av = [sum(by[y]) / len(by[y]) for y in ys]
fig, ax = plt.subplots(figsize=(6.3, 2.4))
ax.plot(ys, av, color=ACC, lw=2, marker="o", ms=3)
for y, v in zip(ys, av):
    if y in (2011, 2016, 2022, 2025): ax.annotate(f"{v:,.0f}", (y, v), textcoords="offset points", xytext=(0, 7), ha="center", fontsize=8)
ax.set_ylabel("USD per tonne"); ax.set_ylim(0, 30000); ax.set_xticks(ys[::2])
fig.savefig(os.path.join(OUT, "fig1_nickel_price.svg"), bbox_inches="tight"); plt.close(fig)

# Figure 2: German exports of nickel mill products by HS code
data = {}
for hs, lab in [("7505", "Bars, rods, wire (7505)"), ("7506", "Plate, sheet, strip (7506)"), ("7507", "Tubes, fittings (7507)")]:
    s = {int(r["year"]): float(r["value_usd"]) / 1e6 for r in csv.DictReader(open(os.path.join(ROOT, f"data/clean/comtrade_{hs}_2019-2024.csv")))
         if r["reporter"] == "Germany" and r["flow"] == "Export" and r["partner"] == "World"}
    data[lab] = s
yrs = sorted(next(iter(data.values())))
fig, ax = plt.subplots(figsize=(6.3, 2.4)); bottom = [0] * len(yrs)
for (lab, s), c in zip(data.items(), [ACC, "#5B8DB8", GREY]):
    vals = [s[y] for y in yrs]; ax.bar(yrs, vals, bottom=bottom, color=c, label=lab, width=0.65)
    bottom = [b + v for b, v in zip(bottom, vals)]
for y, b in zip(yrs, bottom): ax.text(y, b + 20, f"{b:,.0f}", ha="center", fontsize=8)
ax.set_ylabel("USD million"); ax.set_ylim(0, 1600); ax.legend(frameon=False, fontsize=8, ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.12))
fig.savefig(os.path.join(OUT, "fig2_de_nickel_exports.svg"), bbox_inches="tight"); plt.close(fig)

# Figure 3 (fan chart by industry) and figure 4 (supply overlay) are written by model/outlook_2035.py from the Monte Carlo results.
print("figures written")
