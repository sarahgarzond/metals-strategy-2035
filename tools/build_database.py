#!/usr/bin/env python3
"""Build report/metals_database.xlsx from data/clean and data/sources.csv."""
import csv, glob, os, re, collections
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter

ROOT = os.path.join(os.path.dirname(__file__), "..")
C = lambda f: os.path.join(ROOT, "data", "clean", f)
OUT = os.path.join(ROOT, "report", "metals_database.xlsx")
wb = Workbook(); wb.remove(wb.active)
HEAD = Font(bold=True); FILL = PatternFill("solid", fgColor="D9D9D9")


def num(x):
    try:
        return float(str(x).replace(",", "").strip())
    except ValueError:
        return None


def sheet(name, header, rows, widths=None):
    ws = wb.create_sheet(name)
    ws.append(header)
    for c in ws[1]:
        c.font = HEAD; c.fill = FILL
    for r in rows:
        ws.append(r)
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    for i, h in enumerate(header, 1):
        ws.column_dimensions[get_column_letter(i)].width = (widths or {}).get(h, max(10, min(40, len(h) + 4)))
    return ws


src = list(csv.DictReader(open(os.path.join(ROOT, "data", "sources.csv"), encoding="utf-8")))
label = {r["data_id"]: f'{r.get("intext_author") or r.get("author")}, {r.get("pub_date", "")[:4]}' for r in src}

# 1 Map: material, form, application, industry
ind = {"05_1": "Automotive", "05_2": "Oil and gas", "05_3": "Energy", "05_4": "Aerospace", "05_5": "Chemical",
       "05_6": "Electronics", "05_7": "Medical"}
rows = []
for f in sorted(glob.glob(os.path.join(ROOT, "sections", "05_[1-7]_*.md"))):
    i = ind[os.path.basename(f)[:4]]
    for line in open(f, encoding="utf-8"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if line.startswith("|") and len(cells) == 3 and not cells[0].startswith(("Outlook", "---")):
            rows.append([i, cells[1], cells[2], cells[0]])
sheet("Map", ["Industry", "Application", "Material and product form", "Outlook 2035"], rows,
      {"Application": 60, "Material and product form": 45, "Industry": 14, "Outlook 2035": 14})

# 2 Supply: USGS world production, 10 metals, 2024 and 2025
MET = {"NICKEL": "Nickel", "COBALT": "Cobalt", "CHROMIUM": "Chromium", "MOLYBDENUM": "Molybdenum",
       "TITANIUM AND TITANIUM DIOXIDE": "Titanium", "TITANIUM MINERAL CONCENTRATES": "Titanium minerals",
       "TUNGSTEN": "Tungsten", "ZIRCONIUM AND HAFNIUM": "Zirconium", "COPPER": "Copper", "ALUMINUM": "Aluminium",
       "BAUXITE AND ALUMINA": "Bauxite and alumina", "MANGANESE": "Manganese"}
rows = []
for r in csv.DictReader(open(C("usgs_mcs2026.csv"), encoding="utf-8")):
    if r["MCS chapter"] in MET and r["Section"].startswith("World") and r["Statistics"] != "Reserves" \
            and r["Year"] in ("2024", "2025") and num(r["Value"]) is not None:
        rows.append([MET[r["MCS chapter"]], r["Statistics_detail"].replace("Production: ", ""), r["Country"],
                     int(r["Year"]), num(r["Value"]), r["Unit"], "U.S. Geological Survey, 2026"])
for r in csv.DictReader(open(C("iea_critical_minerals_supply_2026.csv"), encoding="utf-8")):
    m, _, stage = r["mineral_stage"].partition(" - ")
    if m in ("Nickel", "Cobalt", "Copper") and num(r["kt"]) is not None:
        rows.append([m, stage + " (IEA base case)", r["country"], int(r["year"]), num(r["kt"]) * 1000, "metric tons",
                     "International Energy Agency, 2026"])
sheet("Supply", ["Material", "Stage", "Country", "Year", "Value", "Unit", "Source"], rows,
      {"Stage": 34, "Country": 22, "Source": 30})

# 3 Prices: World Bank annual averages
acc = collections.defaultdict(list)
for r in csv.DictReader(open(C("worldbank_pinksheet_monthly.csv"))):
    if r["commodity"] in ("Nickel", "Copper", "Aluminum", "Zinc", "Tin") and 2015 <= int(r["month"][:4]) <= 2025:
        acc[(r["commodity"].replace("Aluminum", "Aluminium"), int(r["month"][:4]))].append(float(r["price"]))
rows = [[m, y, round(sum(v) / len(v), 0), "USD per t", len(v), "World Bank, 2026"] for (m, y), v in sorted(acc.items())]
sheet("Prices", ["Material", "Year", "Annual average", "Unit", "Months", "Source"], rows, {"Source": 22})

# 4 Demand: IEA demand by use and scenario
rows = [[r["mineral"], r["item"], r["scenario"], int(r["year"]), num(r["kt"]), "kt", "International Energy Agency, 2026"]
        for r in csv.DictReader(open(C("iea_critical_minerals_demand_2026.csv"), encoding="utf-8"))
        if r["mineral"] in ("Nickel", "Cobalt", "Copper") and "Share" not in r["item"]]
sheet("Demand", ["Material", "Use", "Scenario", "Year", "Value", "Unit", "Source"], rows,
      {"Use": 36, "Scenario": 18, "Source": 30})

# 5 Trade: Comtrade, partner World
rows = []
for r in csv.DictReader(open(C("comtrade_portfolio_world_2019-2024.csv"), encoding="utf-8")):
    v, w = num(r["value_usd"]), num(r["net_weight_kg"])
    rows.append([r["hs"], r["hs_desc"], r["reporter"], r["flow"], int(r["year"]), v, w])
ws = sheet("Trade", ["HS", "Product", "Reporter", "Flow", "Year", "Value USD", "Net weight kg", "USD per kg"], rows,
           {"Product": 34, "Reporter": 16})
for i in range(2, ws.max_row + 1):
    ws[f"H{i}"] = f'=IF(AND(ISNUMBER(G{i}),G{i}>0),F{i}/G{i},"")'
    ws[f"F{i}"].number_format = ws[f"G{i}"].number_format = "#,##0"; ws[f"H{i}"].number_format = "0.00"

# 6 Mirror: partner reported flows for non reporting countries
rows = [[r["hs"], r["country"], r["year"], r["mirror_flow"].split(" ")[0], num(r["value_usd"]), num(r["net_weight_kg"]),
         int(r["n_reporters"])] for r in csv.DictReader(open(C("comtrade_mirror_extra6_2022-2024.csv"), encoding="utf-8"))]
sheet("Mirror", ["HS", "Country", "Year", "Flow", "Value USD", "Net weight kg", "Reporting partners"], rows,
      {"Country": 20})

# 7 EU apparent consumption (tonnes from PRODCOM, value from trade unit values)
rows = []
for r in csv.DictReader(open(C("apparent_consumption_prodcom_2019-2024.csv"), encoding="utf-8")):
    if r["product"].startswith("2445") and r["reporter"] in ("EU27_2020", "DE"):
        rows.append([r["product"], r["product_desc"], r["reporter"], int(r["year"])] +
                    [(num(r[k]) or 0) / 1000 for k in ("sold_production_qty", "imports_qty", "exports_qty")] +
                    [(num(r[k]) or 0) / 1e6 for k in ("imports_eur", "exports_eur")])
ws = sheet("EU consumption", ["PRODCOM", "Product", "Area", "Year", "Production t", "Imports t", "Exports t",
                              "Imports EUR m", "Exports EUR m", "Apparent consumption t", "Import EUR per kg",
                              "Export EUR per kg", "Value low EUR m", "Value high EUR m"], rows, {"Product": 34})
for i in range(2, ws.max_row + 1):
    ws[f"J{i}"] = f"=E{i}+F{i}-G{i}"
    ws[f"K{i}"] = f'=IF(F{i}>0,H{i}*1000/F{i},"")'
    ws[f"L{i}"] = f'=IF(G{i}>0,I{i}*1000/G{i},"")'
    ws[f"M{i}"] = f'=IFERROR(J{i}*MIN(K{i},L{i})/1000,"")'
    ws[f"N{i}"] = f'=IFERROR(J{i}*MAX(K{i},L{i})/1000,"")'
    for col in "EFGHIJMN":
        ws[f"{col}{i}"].number_format = "#,##0"
    for col in "KL":
        ws[f"{col}{i}"].number_format = "0.0"

# 8 Investment: IEA WEI
rows = [[r["region"], r["item"].replace("Memo: ", ""), int(r["year"]), num(r["usd_bn_2025"]), "USD bn (2025)",
         "International Energy Agency, 2026"] for r in csv.DictReader(open(C("iea_wei2026_by_region.csv"), encoding="utf-8"))]
sheet("Investment", ["Region", "Item", "Year", "Value", "Unit", "Source"], rows, {"Region": 24, "Item": 30, "Source": 30})

# 9 Hydrogen: electrolysis capacity by status and technology
agg = collections.defaultdict(lambda: [0, 0.0])
for r in csv.DictReader(open(C("iea_h2_electrolysis_projects_june2026.csv"), encoding="utf-8")):
    k = (r["status"], r["technology"], r["country_iso3"]); agg[k][0] += int(r["projects"]); agg[k][1] += float(r["capacity_mwel"])
rows = [[*k, n, round(c, 1), "International Energy Agency, 2026"] for k, (n, c) in sorted(agg.items())]
sheet("Hydrogen", ["Status", "Technology", "Country", "Projects", "Capacity MWel", "Source"], rows,
      {"Status": 20, "Technology": 20, "Source": 30})

# 10 Facts: every other logged number
CHAIN = [("AERO", "Aerospace"), ("AUTO", "Automotive"), ("OG_", "Oil and gas"), ("EE_", "Energy"), ("CHEM", "Chemical"),
         ("CEFIC", "Chemical"), ("VCI", "Chemical"), ("ELEC", "Electronics"), ("SEMI", "Electronics"), ("MED", "Medical"),
         ("CO_", "Company"), ("COMTRADE", "Trade"), ("AC_", "Market size"), ("EU_", "Trade")]
rows = []
for r in src:
    if r["data_id"].startswith("REF_") or num(r["value"]) is None:
        continue
    link = next((v for k, v in CHAIN if r["data_id"].startswith(k)), "Material")
    rows.append([r["data_id"], link, r["material"], r["industry"], r["geography"], r["metric"], r["year"], num(r["value"]),
                 r["unit"], label[r["data_id"]]])
sheet("Facts", ["ID", "Link", "Material", "Industry", "Geography", "Metric", "Year", "Value", "Unit", "Source"], rows,
      {"ID": 30, "Metric": 50, "Source": 34, "Unit": 18})

# 11 Scenarios: index = 100 x (1 + g)^10
SC = [("Aerospace", 2.0, 4.5, 6.0), ("Energy", 0.5, 4.0, 6.5), ("Electronics", 0.0, 3.0, 5.0), ("Medical", 1.0, 2.5, 4.0),
      ("Chemical", -1.0, 1.0, 2.5), ("Oil and gas", -1.0, 0.5, 1.5), ("Automotive", -3.0, -1.5, 0.0)]
ws = sheet("Scenarios", ["Industry", "Downside %", "Base %", "Upside %", "Downside 2035", "Base 2035", "Upside 2035"],
           [list(s) for s in SC])
for i in range(2, len(SC) + 2):
    for src_c, dst in zip("BCD", "EFG"):
        ws[f"{dst}{i}"] = f"=100*(1+{src_c}{i}/100)^10"; ws[f"{dst}{i}"].number_format = "0"
pr = ws.max_row + 2
ws.cell(pr, 1, "Product family").font = HEAD; ws.cell(pr, 6, "Base 2035").font = HEAD
FAM = [("Superalloy bar, billet and remelt stock", [2, 3]), ("Nickel alloy bars, rods and wire", [2, 3, 7]),
       ("Plate, sheet, strip and foil", [6, 4, 3, 7]), ("Tubes and fittings", [6, 3, 7]), ("Precision FeNi strip and foil", [4, 8])]
for j, (name, idx) in enumerate(FAM, pr + 1):
    ws.cell(j, 1, name); ws.cell(j, 6, "=AVERAGE(" + ",".join(f"F{k}" for k in idx) + ")").number_format = "0"
ws.column_dimensions["A"].width = 40

# 12 Scores: weighted opportunity matrix
OPP = []
for line in open(os.path.join(ROOT, "sections", "08_recommendations.md"), encoding="utf-8"):
    c = [x.strip() for x in line.strip().strip("|").split("|")]
    if line.startswith("|") and len(c) == 11 and c[1].isdigit():
        OPP.append([c[0]] + [int(x) for x in c[1:9]])
hdr = ["Opportunity", "Market", "Growth", "Supply security", "Competition", "Technology", "Customers", "Barriers",
       "Differentiation", "Score", "Tier"]
ws = sheet("Scores", hdr, OPP, {"Opportunity": 62})
n = len(OPP) + 1
ws.cell(n + 2, 1, "Weight").font = HEAD
for k, w in enumerate([0.15, 0.20, 0.15, 0.10, 0.10, 0.10, 0.10, 0.10], 2):
    ws.cell(n + 2, k, w).number_format = "0%"
for i in range(2, n + 1):
    ws[f"J{i}"] = f"=SUMPRODUCT(B{i}:I{i},$B${n + 2}:$I${n + 2})"; ws[f"J{i}"].number_format = "0.00"
    ws[f"K{i}"] = f'=IF(ROUND(J{i},2)>=4,1,IF(ROUND(J{i},2)>=3.1,2,IF(ROUND(J{i},2)>=2.6,3,"Harvest")))'

# 13 Sources
rows = [[r["data_id"], r.get("intext_author") or r.get("author"), r.get("pub_date", ""), r.get("title", ""), r.get("url", "")]
        for r in src if r.get("url")]
sheet("Sources", ["ID", "Author", "Date", "Title", "URL"], rows, {"ID": 30, "Author": 30, "Title": 60, "URL": 60})

wb.save(OUT)
print(OUT, [f"{s.title}:{s.max_row - 1}" for s in wb.worksheets])
