#!/usr/bin/env python3
"""Regional split of the 2035 P50 industry demand index (chapter 7.2, results by region). Team estimate.

A region split is only made where a regional driver is in the repository. The 2035 regional figure is the 2025 regional share of the
driver times the 2035 P50 industry index (share held constant: no regional growth driver exists in the repository for any industry
except chemicals, where BASF gives the Asia Pacific share of growth). Everything else is TODO(data).

Drivers
  energy       IEA WEI 2026 investment in gas power (weight 0.55) and nuclear (0.25) by region, 2025 (data/clean/iea_wei2026_by_region.csv, IEA_WEI_REGION_2026)
  oil_and_gas  IEA WEI 2026 upstream oil and gas investment by region, 2025 (LNG chain weight 0.30 has no regional driver: TODO(data))
  automotive   OICA 2025 vehicle production, Asia Pacific, Europe, United States, rest (OICA_APAC_PROD_2025, OICA_EUR_PROD_2025, OICA_US_PROD_2025, OICA_VEH_PROD_2025)
  chemical     BASF: Asia Pacific takes 80 percent of chemical industry growth to 2035 (BASF_APAC_GROWTH_2035). Increment split only.
  medical      OECD hip and knee procedures 2024 by country group, reporting countries only (no USA, Japan, China in the OECD file: TODO(data))
  aerospace    TODO(data): no Airbus or Boeing regional delivery table in the repository
  electronics  TODO(data): WSTS gives only the Americas (32.2 percent of 2025 sales), no SEMI regional capacity or equipment table in the repository
Regions: IEA "Asia Pacific" includes China (checked: China 29.1 of Asia Pacific 81.8 USD bn gas power, 2025). Output data/clean/model_regional.csv.
"""
import os

import pandas as pd

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CLEAN = os.path.join(ROOT, "data", "clean")
REG = ["North America", "Europe", "Asia Pacific", "Middle East"]


def wei(item, year=2025):
    d = pd.read_csv(os.path.join(CLEAN, "iea_wei2026_by_region.csv"))
    d = d[(d.item == item) & (d.year == year)].set_index("region").usd_bn_2025
    out = {r: float(d[r]) for r in REG}
    out["Rest of world"] = float(d["World"]) - sum(out.values())
    return out, float(d["World"])


def shares(dct, tot):
    return {k: v / tot for k, v in dct.items()}


def build(idx, co_energy_t):
    """idx: dict industry -> P50 index 2035 (2025 = 100). co_energy_t: energy cobalt base in t (6,000)."""
    rows = []

    def add(ind, region, share, driver, src, status, note, base_t=None):
        r = dict(industry=ind, region=region, share_2025_pct=(round(100 * share, 1) if share is not None else ""),
                 industry_index_2035_p50=(round(idx[ind], 1) if ind in idx else ""),
                 regional_index_points_2035=(round(share * idx[ind], 1) if share is not None and ind in idx else ""),
                 contained_co_2035_p50_t=(round(share * idx[ind] / 100.0 * base_t) if share is not None and base_t else ""),
                 driver=driver, sources=src, status=status, note=note)
        rows.append(r)

    # energy
    g, gt = wei("Gas")
    n, nt = wei("Nuclear")
    for k in g:
        s = (0.55 * g[k] / gt + 0.25 * n[k] / nt) / 0.80
        add("energy", k, s, "IEA WEI 2026 investment 2025: gas power (weight 0.55) and nuclear (0.25), shares of world", "IEA_WEI_REGION_2026, MODEL_EN_W",
            "driver exists, share held constant", "Investment share is a proxy for where turbines and reactors are ordered and built, not where alloy is melted. No regional growth driver, so the 2025 share is held. Asia Pacific includes China.", co_energy_t)
    # oil and gas
    u, ut = wei("Memo: Oil & gas upstream")
    for k in u:
        add("oil_and_gas", k, u[k] / ut, "IEA WEI 2026 upstream oil and gas investment 2025, share of world (542 USD bn)", "IEA_WEI_UPSTREAM_REGION_2026",
            "driver exists, share held constant", "Upstream only (weight 0.70). The LNG chain (weight 0.30) has no regional driver in the repository (TODO(data)). Asia Pacific includes China.")
    # automotive
    p = {"Asia Pacific": 59.2, "Europe": 17.2, "North America": 10.24}
    rest = 96.4 - sum(p.values())
    p["Rest of world (incl. Canada and Mexico)"] = rest
    for k, v in p.items():
        add("automotive", k, v / 96.4, "OICA 2025 vehicle production, share of 96.4 million", "OICA_APAC_PROD_2025, OICA_EUR_PROD_2025, OICA_US_PROD_2025, OICA_VEH_PROD_2025",
            "driver exists, share held constant", "North America is the United States only (10.24 million), Canada and Mexico are in the rest. Electric share rises faster in China, so Asia Pacific is probably understated for the EV sub index (no regional EV path in the repository).")
    # chemical: increment only
    inc = idx["chemical"] - 100.0
    rows.append(dict(industry="chemical", region="Asia Pacific", share_2025_pct="", industry_index_2035_p50=round(idx["chemical"], 1), regional_index_points_2035=round(0.80 * inc, 1),
                     contained_co_2035_p50_t="", driver="BASF: 80 percent of chemical industry growth to 2035 in Asia Pacific (increment of the index, not level)", sources="BASF_APAC_GROWTH_2035, CEFIC_CN_SHARE_2024",
                     status="growth split only", note=f"Index points added 2025 to 2035: {inc:.1f} in total, 80 percent Asia Pacific. Level split TODO(data): China is 46 percent of world chemical sales (Cefic 2024), other regions not in the repository."))
    rows.append(dict(industry="chemical", region="Rest of world", share_2025_pct="", industry_index_2035_p50=round(idx["chemical"], 1), regional_index_points_2035=round(0.20 * inc, 1),
                     contained_co_2035_p50_t="", driver="Remainder of the growth", sources="BASF_APAC_GROWTH_2035", status="growth split only", note="Europe and North America not separated (TODO(data))."))
    # medical: reporting countries only
    d = pd.read_csv(os.path.join(CLEAN, "oecd_health_hip_knee_procedures.csv"))
    grp = {"Europe": ["AUT", "BEL", "BGR", "CHE", "CYP", "CZE", "DEU", "DNK", "ESP", "EST", "FIN", "FRA", "GBR", "GRC", "HRV", "HUN", "IRL", "ISL", "ITA", "LTU", "LUX", "LVA", "MDA", "MKD", "MLT", "NLD", "NOR", "POL", "PRT", "ROU", "SRB", "SVK", "SVN", "SWE", "TUR"],
           "North America": ["CAN", "MEX"], "Asia Pacific": ["AUS", "KOR", "NZL", "THA"]}
    t24 = d[d.year == 2024].groupby("country").procedures.sum()
    ctry = [c for c in d.country.unique() if d[d.country == c].year.nunique() == d.year.nunique()]
    tot24 = {}
    for r, cs in grp.items():
        cs = [c for c in cs if c in ctry and c in t24.index]
        a = d[(d.country.isin(cs)) & (d.year == 2013)].procedures.sum()
        b = d[(d.country.isin(cs)) & (d.year == 2024)].procedures.sum()
        tot24[r] = (b, (b / a) ** (1 / 11) - 1 if a else float("nan"), len(cs))
    all24 = sum(v[0] for v in tot24.values())
    for r, (b, gr, nc) in tot24.items():
        rows.append(dict(industry="medical", region=r, share_2025_pct=round(100 * b / all24, 1), industry_index_2035_p50=round(idx["medical"], 1), regional_index_points_2035="",
                         contained_co_2035_p50_t="", driver=f"OECD hip and knee procedures 2024, {nc} reporting countries, own 2013 to 2024 growth {100 * gr:.1f} percent a year",
                         sources="MED_OECD_HK_COUNT_2023", status="reporting countries only", note="Share of the reporting countries only, not of the world. The OECD file has no United States, Japan or China (TODO(data)), so North America and Asia Pacific are heavily understated. No world regional index is given."))
    # TODO rows
    rows.append(dict(industry="aerospace", region="all", share_2025_pct="", industry_index_2035_p50=round(idx["aerospace"], 1), regional_index_points_2035="", contained_co_2035_p50_t="",
                     driver="none", sources="", status="TODO(data)", note="TODO(data): Airbus GMF or Boeing CMO regional delivery tables are not in the repository, and the cobalt base (11,499 t) has no regional split."))
    rows.append(dict(industry="electronics", region="all", share_2025_pct="", industry_index_2035_p50=round(idx["electronics"], 1), regional_index_points_2035="", contained_co_2035_p50_t="",
                     driver="WSTS Americas 32.2 percent of 2025 chip sales only", sources="WSTS_AMERICAS_2025, WSTS_WORLD_2025", status="TODO(data)",
                     note="TODO(data): SEMI regional equipment spending or 300 mm capacity by region is not in the repository. WSTS gives the Americas only (256,476 of 795,640 USD m). Fab strip and tube demand follows tool installs, not chip sales."))
    return pd.DataFrame(rows)


if __name__ == "__main__":
    print("run via model/outlook_2035.py")
