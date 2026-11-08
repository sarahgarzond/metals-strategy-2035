#!/usr/bin/env python3
"""Alloy only nickel mill product trade at HS 6 digit (UN Comtrade), 2023 and 2024.

HS 2022 separates pure nickel from nickel alloys at six digits: 750511 / 750512 (bars, rods, profiles), 750521 / 750522 (wire),
750610 / 750620 (plates, sheets, strip, foil), 750711 / 750712 (tubes and pipes). A four digit total mixes both. This script uses only
the alloy codes 750512, 750522, 750620 and 750712, pulled with tools/data/fetch.py comtrade (public preview endpoint, World partner,
ten reporters: Germany, USA, China, Japan, Korea, India, France, UK, Italy, Indonesia, flows X and M, 2023 and 2024).

Inputs  data/clean/comtrade_750512_750522_750712_2023-2024.csv, data/clean/comtrade_750620_2019-2024.csv, data/clean/comtrade_{7505,7506,7507}_2019-2024.csv
Outputs data/clean/comtrade_hs6_alloy_2023-2024.csv          long file, one row per code, reporter, flow, year (values, net weight, unit value)
        data/clean/comtrade_hs6_alloy_summary_2023-2024.csv  totals, unit values and the alloy share of the four digit total on the eight reporters of the four digit files
        research/model/comtrade_hs6_alloy.md                 compact tables for chapter 6 and appendix A2.4
Run: python3 model/comtrade_hs6.py   (called by model/outlook_2035.py, reads clean files only, no network)
Unit values are USD per kg of net weight, reporter rows without a net weight are excluded from the unit value and the tonnage (counted in n_rows_without_weight).
EUR per kg uses 1.08 USD per EUR, the same team assumption as the scoring inputs (no annual average rate is logged in the repository).
"""
import os

import pandas as pd

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CLEAN = os.path.join(ROOT, "data", "clean")
NOTE = os.path.join(ROOT, "research", "model", "comtrade_hs6_alloy.md")
EUR_USD = 1.08
GROUPS = {"750512": ("Bars, rods, profiles", 7505), "750522": ("Wire", 7505), "750620": ("Plates, sheets, strip, foil", 7506), "750712": ("Tubes and pipes", 7507)}
FAMILY = {"bar_rod_wire": (["750512", "750522"], 7505), "flat": (["750620"], 7506), "tube": (["750712"], 7507)}


def load():
    a = pd.read_csv(os.path.join(CLEAN, "comtrade_750512_750522_750712_2023-2024.csv"), dtype={"hs": str})
    b = pd.read_csv(os.path.join(CLEAN, "comtrade_750620_2019-2024.csv"), dtype={"hs": str})
    b = b[b.year.isin([2023, 2024])]
    d = pd.concat([a, b], ignore_index=True)
    d = d[d.partner == "World"].copy()
    d["unit_value_usd_per_kg"] = d.value_usd / d.net_weight_kg
    return d


def hs4(hs):
    y = pd.read_csv(os.path.join(CLEAN, f"comtrade_{hs}_2019-2024.csv"))
    return y[(y.partner == "World") & (y.year.isin([2023, 2024]))]


def build(write_note=True):
    d = load()
    d[["hs", "hs_desc", "reporter", "flow", "year", "value_usd", "net_weight_kg", "unit_value_usd_per_kg"]].to_csv(os.path.join(CLEAN, "comtrade_hs6_alloy_2023-2024.csv"), index=False)
    rows = []
    for (hs, flow, yr), g in d.groupby(["hs", "flow", "year"]):
        w = g[g.net_weight_kg.notna() & (g.net_weight_kg > 0)]
        uv = w.value_usd.sum() / w.net_weight_kg.sum()
        rows.append(dict(hs=hs, product=GROUPS[hs][0], flow=flow, year=int(yr), n_reporters=int(g.reporter.nunique()), n_rows_without_weight=int(len(g) - len(w)),
                         value_usd_m=round(w.value_usd.sum() / 1e6, 1), net_weight_kt=round(w.net_weight_kg.sum() / 1e6, 2), unit_value_usd_per_kg=round(uv, 2),
                         unit_value_eur_per_kg=round(uv / EUR_USD, 2), basis="ten reporters, World partner"))
    summ = pd.DataFrame(rows)
    # alloy share of the four digit total, on the reporters present in the four digit files
    sh = []
    for fam, (codes, h4) in FAMILY.items():
        t4 = hs4(h4)
        t4 = t4[t4.net_weight_kg.notna() & (t4.net_weight_kg > 0)]      # rows without a net weight are dropped from value and tonnage alike
        reps = sorted(t4.reporter.unique())
        for flow in ("Export", "Import"):
            for yr in (2023, 2024):
                tot = t4[(t4.flow == flow) & (t4.year == yr)].net_weight_kg.sum() / 1e6
                dd = d[(d.hs.isin(codes)) & (d.flow == flow) & (d.year == yr) & (d.reporter.isin(reps)) & d.net_weight_kg.notna() & (d.net_weight_kg > 0)]
                al = dd.net_weight_kg.sum() / 1e6
                alv = dd.value_usd.sum() / 1e6
                tv = t4[(t4.flow == flow) & (t4.year == yr)].value_usd.sum() / 1e6
                sh.append(dict(family=fam, codes="+".join(codes), four_digit=h4, flow=flow, year=yr, reporters=len(reps), total_four_digit_kt=round(tot, 2), alloy_only_kt=round(al, 2),
                               alloy_share_of_weight_pct=round(100 * al / tot, 1), total_four_digit_usd_m=round(tv, 1), alloy_only_usd_m=round(alv, 1),
                               alloy_share_of_value_pct=round(100 * alv / tv, 1), pure_nickel_and_other_kt=round(tot - al, 2),
                               unit_value_alloy_usd_per_kg=round(alv / al, 2), unit_value_four_digit_usd_per_kg=round(tv / tot, 2)))
    share = pd.DataFrame(sh)
    summ.to_csv(os.path.join(CLEAN, "comtrade_hs6_alloy_summary_2023-2024.csv"), index=False)
    share.to_csv(os.path.join(CLEAN, "comtrade_hs6_alloy_share_of_four_digit_2023-2024.csv"), index=False)
    # main reporters 2024 exports
    main = d[(d.flow == "Export") & (d.year == 2024)].pivot_table(index="reporter", columns="hs", values=["net_weight_kg", "value_usd"], aggfunc="sum")
    mrows = []
    for rep in main.index:
        r = dict(reporter=rep)
        for hs in GROUPS:
            kg, usd = main.loc[rep, ("net_weight_kg", hs)], main.loc[rep, ("value_usd", hs)]
            r[f"{hs}_kt"] = round(kg / 1e6, 2) if pd.notna(kg) else None
            r[f"{hs}_usd_per_kg"] = round(usd / kg, 1) if pd.notna(kg) and kg > 0 else None
        mrows.append(r)
    mr = pd.DataFrame(mrows).sort_values("750512_kt", ascending=False)
    mr.to_csv(os.path.join(CLEAN, "comtrade_hs6_alloy_main_reporters_2024.csv"), index=False)
    if write_note:
        def md(df):
            cols = list(df.columns)
            o = ["| " + " | ".join(cols) + " |", "|" + "|".join("---" for _ in cols) + "|"]
            for _, r in df.iterrows():
                o.append("| " + " | ".join("n/a" if pd.isna(v) else str(v) for v in r) + " |")
            return "\n".join(o)
        L = ["# Alloy only nickel mill product trade, HS 6 digit (UN Comtrade, 2023 and 2024)\n",
             "Generated by model/comtrade_hs6.py. Do not edit by hand. Source: UN Comtrade public preview API pulled with tools/data/fetch.py comtrade (data_id COMTRADE_750512_750522_750712_2023_2024 and COMTRADE_750610_750620_2019_2024). "
             "Reporters: Germany, USA, China, Japan, Korea, India, France, United Kingdom, Italy, Indonesia, partner World, flows X and M. Re-exports are counted by each reporter, so the totals are a traded floor and not a production figure.\n",
             "HS 2022 separates pure nickel from nickel alloys at six digits (750511 and 750512 bars, 750521 and 750522 wire, 750610 and 750620 flat, 750711 and 750712 tubes). Official four digit totals therefore do not have to mix the two: the alloy codes are used here.\n",
             "## Totals and unit values of the alloy codes\n", md(summ.drop(columns=["basis"])),
             "\n## Alloy share of the four digit total (eight reporters of the four digit files)\n",
             md(share[["family", "codes", "flow", "year", "reporters", "total_four_digit_kt", "alloy_only_kt", "alloy_share_of_weight_pct", "alloy_share_of_value_pct", "unit_value_alloy_usd_per_kg", "unit_value_four_digit_usd_per_kg"]]),
             "\n## Main exporters 2024, kt and USD per kg\n", md(mr),
             "\nReading: bars, wire, flat and tubes of nickel are almost all alloy in the traded floor, so the HS 7505, 7506 and 7507 floors used for the family tonnes overstate alloy tonnage by only the pure nickel share shown above. "
             "2024 is the basis. In 2023 Japan reports no net weight for 750522 and 750620 exports (USD 35 m and 321 m), so the 2023 flat and wire tonnage and alloy shares are biased low. In 2024 only Indonesia 750522 (USD 0.2 m) and Italy 750620 (USD 7.9 m) lack a weight. "
             "Unit values here are customs values per kg of net weight and include every alloy from Alloy 625 to Alloy 400, so they are not superalloy prices. EUR per kg uses 1.08 USD per EUR (team assumption).\n"]
        open(NOTE, "w", encoding="utf-8").write("\n".join(L))
    return d, summ, share, mr


if __name__ == "__main__":
    d, summ, share, mr = build()
    print(summ.to_string())
    print(share.to_string())
