"""Product Strategy 2035 market model.

Builds the linked dataset Material > Product form > Application > Industry > Geography > Market size > Growth,
scores the opportunity cells, writes the Excel model and renders all report figures as SVG.
All values in EUR billion (or million where stated), constant 2025 metal prices, base case.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "report", "fig")
os.makedirs(FIG, exist_ok=True)

NAVY, TEAL, CYAN, GREEN, LIME, YELLOW, GREY, LIGHT = (
    "#26307A", "#1590B8", "#33B6D6", "#6DBE45", "#BFD630", "#F2E21C", "#6B7385", "#E8EEF4")
plt.rcParams.update({
    "font.family": "Liberation Serif", "font.size": 9, "axes.edgecolor": "#B8C0CC", "axes.labelcolor": NAVY,
    "xtick.color": NAVY, "ytick.color": NAVY, "axes.spines.top": False, "axes.spines.right": False,
    "svg.fonttype": "none", "axes.titleweight": "bold", "axes.titlecolor": NAVY, "axes.titlesize": 10,
})
YEARS = 10


def cagr_val(v, g):
    return v * (1 + g) ** YEARS


# ---------------------------------------------------------------- Phase I: material families
# name, 2025 volume kt, avg semifinished value EUR/kg, base CAGR, key assumption
MATERIALS = [
    ("Nickel alloys (CRA, heat resistant, superalloys, FeNi)", 450, 37.8, 0.050,
     "About 7% of 3.5 Mt primary nickel use goes into alloys, average Ni content 55%"),
    ("Specialty stainless (6Mo, super duplex, high purity, heat resistant)", 2200, 7.0, 0.035,
     "About 3.4% of 64.2 Mt stainless melt is high alloyed specialty grades"),
    ("High performance copper products (CuNi, CuNiSi, CuCrZr, OF copper)", 550, 13.1, 0.055,
     "Specialty alloy and oxygen free share of roughly 25 Mt copper semis"),
    ("Aluminium specialty strip and wire", 900, 4.4, 0.045,
     "Electrical, battery and high strength niches the Client can serve"),
    ("Welding consumables, high alloyed (Ni base and stainless)", 75, 34.7, 0.045,
     "Ni base filler about 30 kt plus high alloyed stainless filler"),
    ("Cobalt alloys (wear, heat resistant, CoCr medical)", 36, 69.4, 0.055,
     "About 18 kt cobalt in alloys at roughly 50% Co content"),
    ("Zirconium and Zr alloys (nuclear and chemical grade)", 9.5, 147.0, 0.055,
     "Nuclear cladding and chemical Zr 702/705 semifinished"),
    ("Additive manufacturing powders (Ni, Co, Fe, Cu alloys)", 7.5, 73.0, 0.140,
     "Metal AM powder excluding titanium, Wohlers industry growth plus powder share"),
]
MAT = []
for n, kt, p, g, a in MATERIALS:
    v25 = kt * p / 1000  # EUR bn
    MAT.append(dict(name=n, kt=kt, price=p, v25=v25, g=g, v35=cagr_val(v25, g), assumption=a))
TOT25 = sum(m["v25"] for m in MAT)
TOT35 = sum(m["v35"] for m in MAT)
TOT_G = (TOT35 / TOT25) ** (1 / YEARS) - 1

# ---------------------------------------------------------------- Phase II: sectors
SECTORS = [  # name, 2025 EUR bn, CAGR
    ("Chemical process industry", 9.00, 0.025),
    ("Environmental and energy technology", 8.50, 0.065),
    ("Oil and gas", 8.00, 0.020),
    ("Aerospace and defence", 7.50, 0.070),
    ("Electronics and electrical", 6.50, 0.075),
    ("Automotive", 6.00, 0.015),
    ("Medical technology", 2.00, 0.060),
]
other25 = TOT25 - sum(s[1] for s in SECTORS)
other35 = TOT35 - sum(cagr_val(s[1], s[2]) for s in SECTORS)
SECTORS.append(("Other (marine, water, food, general)", other25, (other35 / other25) ** 0.1 - 1))
SEC = [dict(name=n, v25=v, g=g, v35=cagr_val(v, g)) for n, v, g in SECTORS]

REGIONS = [("China", 15.2, 0.047), ("Europe", 12.2, 0.028), ("North America", 11.1, 0.053),
           ("Asia excl. China", 8.1, 0.066), ("Middle East", 2.5, 0.060), ("Rest of world", 1.5, 0.035)]
REG = [dict(name=n, v25=v, g=g, v35=cagr_val(v, g)) for n, v, g in REGIONS]

# ---------------------------------------------------------------- Phase III: opportunity cells
CRIT = [("Market attractiveness", .15), ("Growth to 2035", .20), ("Strategic fit", .15),
        ("Competitive intensity (5 = low)", .10), ("Technology attractiveness", .10),
        ("Customer attractiveness", .10), ("Entry barriers (5 = protective)", .10),
        ("Differentiation potential", .10)]
# id, material, form, application, industry, regions, size EURm 2025, CAGR, scores
CELLS = [
    ("A1", "Ni superalloys 718, 625, 282", "Bar, billet, wire", "Engine discs, shafts, casings, fasteners",
     "Aerospace", "EU, US", 3800, .075, [5, 4, 5, 3, 5, 5, 5, 4]),
    ("A2", "Ni and Co superalloy powder", "AM powder", "Printed combustor, fuel nozzle, rocket engine parts",
     "Aerospace, energy", "US, EU", 350, .150, [2, 5, 4, 3, 5, 4, 4, 5]),
    ("A3", "Ni alloys for defence and space", "Sheet, bar", "Rocket engines, hypersonics, naval propulsion",
     "Aerospace and defence", "US, EU", 700, .090, [3, 5, 5, 4, 5, 4, 5, 4]),
    ("E1", "C-22, C-276, 316L VIM-VAR", "Strip, tube, bar", "Fab gas delivery, wet benches, valves",
     "Electronics", "TW, US, KR, JP, DE", 900, .090, [3, 5, 4, 4, 5, 5, 5, 5]),
    ("E2", "High conductivity and CuNiSi copper", "Strip, busbar", "AI rack power (800 VDC), cold plates, connectors",
     "Electronics and electrical", "US, TW, CN", 1600, .100, [4, 5, 3, 2, 4, 4, 2, 3]),
    ("E3", "FeNi36 (Invar type), FeNi42", "Ultra thin foil, strip", "OLED fine metal masks, lead frames",
     "Electronics", "KR, CN, JP", 400, .080, [2, 4, 5, 3, 5, 4, 5, 5]),
    ("N1", "Alloy 690, 800, Zr alloys", "Tube, strip, plate", "Steam generators, SMR internals, fuel cladding",
     "Energy", "US, CA, EU, IN", 1700, .070, [4, 4, 5, 4, 4, 4, 5, 4]),
    ("N2", "Ferritic Cr interconnect alloy, Ni 201", "Thin strip, mesh, plate", "SOEC stacks, alkaline electrolysers",
     "Energy (hydrogen)", "EU, CN, US", 250, .180, [1, 5, 5, 3, 5, 3, 4, 5]),
    ("N3", "Alloy 625, 622 overlay", "Weld strip, wire", "Waste to energy boilers, FGD, CSP salts",
     "Environmental technology", "EU, ME, CN", 900, .040, [3, 3, 4, 3, 3, 3, 3, 3]),
    ("C1", "C-276, 59, 31, 625", "Plate, sheet, clad", "Acid, chlorine and pharma reactors",
     "Chemical process", "EU, CN, US", 2600, .030, [5, 2, 5, 2, 3, 3, 3, 3]),
    ("C2", "Ni alloys, super duplex, Ti alternatives", "Plate, tube", "HPAL autoclaves, nickel sulphate, lithium refining",
     "Chemical (battery materials)", "ID, CN, US, EU", 600, .090, [2, 5, 4, 3, 4, 3, 3, 4]),
    ("C3", "Zr 702, 705", "Plate, tube", "Acetic acid, urea, sulfuric acid service",
     "Chemical process", "CN, ME, US", 300, .040, [2, 3, 4, 4, 3, 3, 4, 4]),
    ("O1", "Alloy 625, 825, Invar 36, 9% Ni", "Plate, clad, strip", "LNG trains, membrane tanks, cryogenic piping",
     "Oil and gas", "US, QA, KR, CN", 1300, .045, [4, 3, 4, 3, 3, 4, 4, 4]),
    ("O2", "Alloy 825, 625, 718", "Clad pipe, OCTG, bar", "Sour gas, deepwater, CCS injection wells",
     "Oil and gas", "ME, BR, NO", 2200, .020, [4, 2, 4, 2, 3, 3, 3, 3]),
    ("W1", "6Mo and super duplex stainless", "Plate, tube", "Desalination, marine scrubbers, water reuse",
     "Environmental technology", "ME, Asia", 1000, .045, [3, 3, 3, 2, 2, 3, 2, 2]),
    ("M1", "CoCr, MP35N type, 316LVM", "Bar, fine wire", "Hip and knee implants, leads, stents",
     "Medical technology", "US, EU", 1100, .065, [3, 4, 4, 3, 4, 5, 5, 4]),
    ("V1", "Ni 201 strip, Cu busbar, Ni plated strip", "Strip", "EV battery tabs, power electronics, electric motors",
     "Automotive", "CN, EU", 1400, .080, [4, 4, 3, 1, 3, 2, 1, 2]),
    ("V2", "Alloy 600, 601, heat resistant strip", "Strip, wire", "Exhaust sensors, glow and spark plugs, gaskets",
     "Automotive", "EU, CN", 900, -.030, [3, 1, 4, 3, 1, 2, 3, 2]),
]
OPP = []
for cid, mat, form, app, ind, reg, size, g, sc in CELLS:
    score = sum(w * s for (_, w), s in zip(CRIT, sc))
    attract = (sc[0] * .15 + sc[1] * .20 + sc[4] * .10 + sc[5] * .10) / .55
    ability = (sc[2] * .15 + sc[3] * .10 + sc[6] * .10 + sc[7] * .10) / .45
    tier = "A  Win and scale" if score >= 4.0 else ("B  Build options" if score >= 3.5 else "C  Defend or harvest")
    OPP.append(dict(id=cid, mat=mat, form=form, app=app, ind=ind, reg=reg, size=size, g=g,
                    s35=cagr_val(size, g), sc=sc, score=score, attract=attract, ability=ability, tier=tier))

# ---------------------------------------------------------------- prices (annual averages, rounded)
YRS = list(range(2015, 2027))
PRICES = {
    "Nickel (USD/t)": [11860, 9600, 10410, 13120, 13910, 13790, 18470, 25830, 21520, 16810, 15250, 17300],
    "Cobalt (USD/lb)": [13, 12, 27, 37, 16, 15, 23, 30, 15, 11.5, 17, 25],
    "Copper (USD/t)": [5510, 4870, 6170, 6530, 6010, 6180, 9320, 8820, 8490, 9150, 9900, 12800],
    "Aluminium (USD/t)": [1660, 1600, 1970, 2110, 1790, 1700, 2470, 2700, 2250, 2420, 2620, 2850],
}

# ---------------------------------------------------------------- figures
def save(fig, name):
    fig.savefig(os.path.join(FIG, name), format="svg", bbox_inches="tight", transparent=True)
    plt.close(fig)


def fig_materials():
    m = sorted(MAT, key=lambda x: x["v35"])
    lab = [x["name"].split(" (")[0] for x in m]
    fig, ax = plt.subplots(figsize=(6.8, 3.1))
    y = range(len(m))
    ax.barh([i + .2 for i in y], [x["v25"] for x in m], .38, color=TEAL, label="2025")
    ax.barh([i - .2 for i in y], [x["v35"] for x in m], .38, color=GREEN, label="2035 base case")
    for i, x in enumerate(m):
        ax.text(x["v35"] + .3, i - .2, f'{x["v35"]:.1f}  ({x["g"]*100:.1f}% p.a.)', va="center", fontsize=7.5, color=NAVY)
        ax.text(x["v25"] + .3, i + .2, f'{x["v25"]:.1f}', va="center", fontsize=7.5, color=GREY)
    ax.set_yticks(list(y)); ax.set_yticklabels(lab, fontsize=8)
    ax.set_xlabel("Addressable semifinished market, EUR bn, constant 2025 prices")
    ax.set_xlim(0, 34); ax.legend(frameon=False, loc="lower right", fontsize=8)
    save(fig, "f2_materials.svg")


def fig_prices():
    fig, ax = plt.subplots(figsize=(6.8, 2.7))
    cols = [TEAL, NAVY, GREEN, LIME]
    for (k, v), c in zip(PRICES.items(), cols):
        idx = [x / v[0] * 100 for x in v]
        ax.plot(YRS, idx, color=c, lw=2, marker="o", ms=3, label=k.split(" (")[0])
        ax.text(2026.15, idx[-1], f"{idx[-1]:.0f}", color=c, va="center", fontsize=8, fontweight="bold")
    ax.axvspan(2025.5, 2026.5, color=LIGHT, zorder=0)
    ax.text(2026, 285, "2026\nYTD est.", ha="center", fontsize=7, color=GREY)
    ax.set_ylabel("Index, 2015 = 100"); ax.set_xticks(YRS); ax.set_xticklabels([str(y)[2:] for y in YRS])
    ax.legend(frameon=False, ncol=4, fontsize=8, loc="upper left")
    ax.set_ylim(50, 310)
    save(fig, "f3_prices.svg")


def fig_concentration():
    data = [("Cobalt mine", "DR Congo", 73), ("Nickel mine", "Indonesia", 67), ("Stainless melt", "China", 64),
            ("Primary aluminium", "China", 59), ("Refined copper", "China", 48), ("Zircon", "Australia", 24),
            ("Copper mine", "Chile", 23)]
    fig, ax = plt.subplots(figsize=(6.8, 2.4))
    y = range(len(data))[::-1]
    ax.barh(list(y), [d[2] for d in data], color=[NAVY if d[2] >= 50 else TEAL for d in data], height=.6)
    ax.barh(list(y), [100 - d[2] for d in data], left=[d[2] for d in data], color=LIGHT, height=.6)
    for i, d in zip(y, data):
        ax.text(2, i, f"{d[1]}  {d[2]}%", va="center", color="white", fontsize=8, fontweight="bold")
    ax.set_yticks(list(y)); ax.set_yticklabels([d[0] for d in data])
    ax.set_xlim(0, 100); ax.set_xlabel("Share of global output held by the largest producing country, 2025, %")
    save(fig, "f4_concentration.svg")


def fig_sectors():
    s = sorted(SEC, key=lambda x: x["v35"])
    fig, ax = plt.subplots(figsize=(6.8, 3.0))
    y = range(len(s))
    ax.barh([i + .2 for i in y], [x["v25"] for x in s], .38, color=TEAL, label="2025")
    ax.barh([i - .2 for i in y], [x["v35"] for x in s], .38, color=GREEN, label="2035 base case")
    for i, x in enumerate(s):
        ax.text(x["v35"] + .2, i - .2, f'{x["v35"]:.1f}  ({x["g"]*100:+.1f}% p.a.)', va="center", fontsize=7.5, color=NAVY)
    ax.set_yticks(list(y)); ax.set_yticklabels([x["name"] for x in s], fontsize=8)
    ax.set_xlim(0, 21); ax.set_xlabel("Addressable market by sector, EUR bn")
    ax.legend(frameon=False, loc="lower right", fontsize=8)
    save(fig, "f5_sectors.svg")


def fig_regions():
    fig, ax = plt.subplots(figsize=(6.8, 2.3))
    x = range(len(REG))
    ax.bar([i - .2 for i in x], [r["v25"] for r in REG], .38, color=TEAL, label="2025")
    ax.bar([i + .2 for i in x], [r["v35"] for r in REG], .38, color=GREEN, label="2035")
    for i, r in enumerate(REG):
        ax.text(i + .2, r["v35"] + .5, f'{r["g"]*100:.1f}%', ha="center", fontsize=8, color=NAVY, fontweight="bold")
    ax.set_xticks(list(x)); ax.set_xticklabels([r["name"] for r in REG], fontsize=8)
    ax.set_ylabel("EUR bn"); ax.set_ylim(0, 28); ax.legend(frameon=False, fontsize=8)
    save(fig, "f6_regions.svg")


def fig_matrix():
    fig, ax = plt.subplots(figsize=(6.8, 4.4))
    col = {"A": NAVY, "B": TEAL, "C": "#A9B2C0"}
    for o in OPP:
        ax.scatter(o["ability"], o["attract"], s=o["s35"] / 9, color=col[o["tier"][0]], alpha=.78, edgecolor="white", lw=1)
        ax.text(o["ability"], o["attract"], o["id"], ha="center", va="center", fontsize=7.5, color="white", fontweight="bold")
    ax.axhline(3.5, color="#C7CED8", lw=.8, ls=(0, (3, 3))); ax.axvline(3.5, color="#C7CED8", lw=.8, ls=(0, (3, 3)))
    ax.set_xlim(1.8, 5.1); ax.set_ylim(1.4, 5.1)
    ax.set_xlabel("Ability to win (fit, competition, barriers, differentiation), score 1 to 5")
    ax.set_ylabel("Market attractiveness (size, growth,\ntechnology, customers), score 1 to 5")
    for t, x, y in [("Invest to lead", 4.95, 5.0), ("Selective entry", 2.0, 5.0), ("Defend core", 4.95, 1.5), ("Harvest", 2.0, 1.5)]:
        ax.text(x, y, t, ha="right" if x > 3 else "left", va="top" if y > 3 else "bottom", fontsize=8, color=GREY, style="italic")
    from matplotlib.lines import Line2D
    h = [Line2D([], [], marker="o", ls="", color=col[k], ms=8, label=l) for k, l in
         [("A", "Tier A  Win and scale"), ("B", "Tier B  Build options"), ("C", "Tier C  Defend or harvest")]]
    ax.legend(handles=h, frameon=False, fontsize=8, loc="lower center", bbox_to_anchor=(.5, -.32), ncol=3)
    save(fig, "f7_matrix.svg")


BRIDGE = [("Client revenue 2025", 400), ("Market momentum on core", 180), ("Aerospace share gain", 70),
          ("Semiconductor, AI, displays", 70), ("Nuclear and hydrogen", 55), ("AM powders", 35),
          ("Medical", 25), ("ICE automotive erosion", -25), ("Oil, gas, chemical mix", -10), ("Target 2035", 800)]


def fig_bridge():
    fig, ax = plt.subplots(figsize=(6.8, 2.8))
    run = 0
    for i, (l, v) in enumerate(BRIDGE):
        if i in (0, len(BRIDGE) - 1):
            ax.bar(i, v, color=NAVY, width=.62); run = v if i == 0 else run
            ax.text(i, v + 12, f"{v}", ha="center", fontsize=8, fontweight="bold", color=NAVY)
        else:
            c = GREEN if v > 0 else "#D9534F"
            ax.bar(i, v, bottom=run if v > 0 else run + v, color=c, width=.62)
            ax.text(i, max(run, run + v) + 12, f"{v:+d}", ha="center", fontsize=8, color=NAVY)
            run += v
    ax.set_xticks(range(len(BRIDGE))); ax.set_xticklabels([b[0] for b in BRIDGE], rotation=30, ha="right", fontsize=7.5)
    ax.set_ylabel("EUR m"); ax.set_ylim(0, 900)
    save(fig, "f8_bridge.svg")


def fig_scen():
    fig, ax = plt.subplots(figsize=(6.8, 2.5))
    yrs = list(range(2025, 2036))
    for lab, g, c in [("Upside: accelerated transition and AI build out", .063, GREEN),
                      ("Base case", TOT_G, NAVY), ("Downside: fragmented trade, slow transition", .029, "#A9B2C0")]:
        v = [TOT25 * (1 + g) ** (y - 2025) for y in yrs]
        ax.plot(yrs, v, color=c, lw=2.2, label=f"{lab} ({g*100:.1f}% p.a.)")
        ax.text(2035.2, v[-1], f"{v[-1]:.0f}", color=c, va="center", fontweight="bold")
    ax.set_ylabel("EUR bn"); ax.set_xlim(2025, 2036); ax.legend(frameon=False, fontsize=8, loc="upper left")
    save(fig, "f10_scenarios.svg")


# ---------------------------------------------------------------- Excel model
def excel():
    wb = Workbook()
    hdr = Font(bold=True, color="FFFFFF"); fill = PatternFill("solid", fgColor="26307A")

    def sheet(title, cols, rows, first=False):
        ws = wb.active if first else wb.create_sheet()
        ws.title = title
        ws.append(cols)
        for c in ws[1]:
            c.font, c.fill, c.alignment = hdr, fill, Alignment(wrap_text=True)
        for r in rows:
            ws.append(r)
        for i, _ in enumerate(cols):
            ws.column_dimensions[chr(65 + i) if i < 26 else "A"].width = 22
        return ws

    sheet("README", ["Item", "Description"], [
        ["Purpose", "Transparent market model for Product Strategy 2035 (high performance metals)"],
        ["Unit", "EUR, constant 2025 metal prices, base case unless stated"],
        ["Chain", "Material > Product form > Application > Industry > Geography > Market size > Growth"],
        ["Method", "Volume (kt) x semifinished value (EUR/kg) by material, then allocated to sectors and regions; "
                   "growth from driver indicators (aircraft deliveries, fab capex, LNG capacity, nuclear builds, vehicle mix)"],
        ["Status", "Team estimate, triangulated with USGS MCS 2026, IEA, SEMI, Airbus, Boeing, ACEA, Cefic, WorldStainless"],
    ], first=True)
    sheet("1_Materials", ["Material family", "Volume 2025 kt", "Value EUR/kg", "Market 2025 EUR bn",
                          "CAGR 2025-35", "Market 2035 EUR bn", "Key assumption"],
          [[m["name"], m["kt"], m["price"], round(m["v25"], 2), m["g"], round(m["v35"], 2), m["assumption"]] for m in MAT]
          + [["Total", "", "", round(TOT25, 2), round(TOT_G, 4), round(TOT35, 2), ""]])
    sheet("2_Sectors", ["Sector", "Market 2025 EUR bn", "CAGR", "Market 2035 EUR bn"],
          [[s["name"], round(s["v25"], 2), round(s["g"], 4), round(s["v35"], 2)] for s in SEC])
    sheet("3_Regions", ["Region", "Market 2025 EUR bn", "CAGR", "Market 2035 EUR bn"],
          [[r["name"], r["v25"], r["g"], round(r["v35"], 2)] for r in REG])
    sheet("4_Opportunity_cells", ["ID", "Material", "Product form", "Application", "Industry", "Geography",
                                  "Size 2025 EUR m", "CAGR", "Size 2035 EUR m"] + [c for c, _ in CRIT]
          + ["Weighted score", "Attractiveness", "Ability to win", "Tier"],
          [[o["id"], o["mat"], o["form"], o["app"], o["ind"], o["reg"], o["size"], o["g"], round(o["s35"])]
           + o["sc"] + [round(o["score"], 2), round(o["attract"], 2), round(o["ability"], 2), o["tier"]] for o in OPP])
    sheet("5_Weights", ["Criterion", "Weight"], [[c, w] for c, w in CRIT])
    sheet("6_Prices", ["Year"] + list(PRICES), [[y] + [PRICES[k][i] for k in PRICES] for i, y in enumerate(YRS)])
    sheet("7_Bridge", ["Step", "EUR m"], BRIDGE)
    # Round 5: the 2035 outlook outputs (model/outlook_2035.py, model/scoring.py) travel with the workbook. Indices and kt are team estimates.
    import csv as _csv
    for nm, fn, cols in [("8_Outlook_industries", "model_tier1_results.csv", None), ("9_Family_tonnes", "model_family_tonnes.csv", None),
                         ("10_Scores", "model_scores.csv", None), ("11_Supply_shocks", "model_supply_shocks.csv", None)]:
        fp = os.path.join(HERE, "..", "data", "clean", fn)
        if os.path.exists(fp):
            rows_ = list(_csv.reader(open(fp, encoding="utf-8")))
            if nm == "8_Outlook_industries":
                keep = [i for i, h in enumerate(rows_[0]) if h in ("level", "industry", "metal", "unit", "index_p10", "index_p50", "index_p90", "p50_2035_without_backtest_shift", "p50_2035_with_backtest_shift_round4_method", "haircut_median")]
                rows_ = [[r[i] for i in keep] for r in rows_ if r and (r[0] in ("level", "industry", "product_family", "product_family_variant"))]
            sheet(nm, rows_[0], rows_[1:])
    wb.save(os.path.join(HERE, "Product_Strategy_2035_Market_Model.xlsx"))


if __name__ == "__main__":
    for f in (fig_materials, fig_prices, fig_concentration, fig_sectors, fig_regions, fig_matrix, fig_bridge, fig_scen, excel):
        f()
    print(f"Total 2025 {TOT25:.1f} bn, 2035 {TOT35:.1f} bn, CAGR {TOT_G*100:.2f}%")
    _s25, _r25 = sum(s["v25"] for s in SEC), sum(r["v25"] for r in REG)
    _s35, _r35 = sum(s["v35"] for s in SEC), sum(r["v35"] for r in REG)
    print(f"Reconciliation 2025: materials {TOT25:.2f}, sectors {_s25:.2f} ({100*(_s25/TOT25-1):+.2f}%), regions {_r25:.2f} ({100*(_r25/TOT25-1):+.2f}%)")
    print(f"Reconciliation 2035: materials {TOT35:.2f}, sectors {_s35:.2f} ({100*(_s35/TOT35-1):+.2f}%), regions {_r35:.2f} ({100*(_r35/TOT35-1):+.2f}%)")
    for s in SEC:
        print(f'{s["name"]:40s} {s["v25"]:5.2f} {s["v35"]:5.2f} {s["g"]*100:4.1f}%')
    for r in REG:
        print(f'{r["name"]:20s} {r["v25"]:5.1f} {r["v35"]:5.1f}')
    for o in sorted(OPP, key=lambda x: -x["score"]):
        print(f'{o["id"]} {o["score"]:.2f} att {o["attract"]:.2f} abl {o["ability"]:.2f} {o["s35"]:6.0f} {o["tier"]}')
