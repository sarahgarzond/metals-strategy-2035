#!/usr/bin/env python3
"""Investment case for the 718 billet and remelt (VAR, ESR) plus conversion step. Team estimate, labelled as such.

Inputs (all in the repository)
  capex benchmarks  CO_OUTOKUMPU_AVESTA_NI_2026 (EUR 150 m total, phase 1 EUR 30 m ESR remelting, about 13 kt), CO_APERAM_INVEST_2026 (EUR 160 m, four sites),
                    CO_CRS_CAPEX_2026 (USD 355 to 375 m FY2027 group capex), CO_ALLEIMA_VAR_2025 (fourth VAR, no value), ARGUS_SUPERALLOY (ATI Monroe fifth VIM, 9 kt, no value),
                    CO_HAYN_CAPEX_2026 (USD 200 m, no tonnes)
  sales             EUR 25.4 to 47.1 per kg (family unit values with superalloy premium, model_family_value.csv)
  margins           14.0 percent (CO_ATI_OPINC_2025) to 24.8 percent (CO_HWM_OPINC_2025), the Table A13 peer range, operating profit over sales
  timing            decision Q1 2028 (team plan). Build time from the Avesta (ESR early 2028 from an August 2026 announcement, greenfield melting end 2029 from a H1 2027 decision)
                    and Haynes (announced H1 2026, ready 2028) timelines. Qualification: Boeing "a year or more" (CO_BA_RAWMAT_2025), ATI isothermal forging lead times
                    over two years (CO_ATI_LEAD_2026), furnace approval 12 to 24 months (industry review, round 6, not a repository source).
Output  data/clean/model_investment_case.csv
Simple payback = capex / operating profit at full utilisation, before tax, without working capital, qualification cost or ramp. A ramp case (33, 67, 100 percent
of sales in the first three years after the first approved tonne) is shown as well. Nothing here is a company figure.
"""
import os

import pandas as pd

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CLEAN = os.path.join(ROOT, "data", "clean")
USD_EUR = 1.08          # USD per EUR (team assumption used across the model)
SMALL_SCALE = 1.5       # capex per tonne premium for a 1.5 to 3 kt step against the 13 kt Avesta project (team assumption)
MARGIN = (0.140, 0.194, 0.248)        # operating margin low, mid, high (mid = mean of the peer range)
RAMP = (0.33, 0.67, 1.00)


def payback_with_ramp(capex, profit_full):
    cum, yr = 0.0, 0
    for share in RAMP + (1.0,) * 40:
        yr += 1
        prev = cum
        cum += profit_full * share
        if cum >= capex:
            return yr - 1 + (capex - prev) / (profit_full * share)
    return float("nan")


def build(uv_lo, uv_mid, uv_hi):
    """uv: EUR per kg low, mid, high (superalloy family unit values with premium)."""
    avesta_total, avesta_p1, avesta_kt = 150.0, 30.0, 13.0
    k_lo, k_hi_flat = avesta_p1 / avesta_kt * 1000.0, avesta_total / avesta_kt * 1000.0     # EUR k per annual tonne: 2.31 and 11.54
    k_hi = k_hi_flat * SMALL_SCALE
    rows = []

    def r(block, item, case="", lo="", mid="", hi="", unit="", basis="", ids="", note=""):
        rows.append(dict(block=block, item=item, case=case, low=lo, mid=mid, high=hi, unit=unit, basis=basis, data_ids=ids, note=note))

    # 1. benchmarks
    r("benchmark", "Outokumpu Avesta high nickel programme, phase 1 (ESR remelting)", "remelt only, flat route", "", round(k_lo), "", "EUR per annual tonne",
      "EUR 30 m for the remelting step against about 13 kt of added capacity (the 13 kt belongs to the whole programme, so this pairs a step with the programme: it is a floor)",
      "CO_OUTOKUMPU_AVESTA_NI_2026, CO_OUTOKUMPU_HINI_CAP_2026", "Bounds the remelt part of the step from below. Not a billet conversion cost. ESR operational early 2028 from an August 2026 announcement.")
    r("benchmark", "Outokumpu Avesta high nickel programme, total (phase 1 plus greenfield melting and casting)", "melt, cast and flat rolling route", "", round(k_hi_flat), "", "EUR per annual tonne",
      "EUR 150 m for about 13 kt", "CO_OUTOKUMPU_AVESTA_NI_2026, CO_OUTOKUMPU_HINI_CAP_2026",
      "Bounds remelt plus conversion from above for a large step: it includes new melting and casting, which a remelt and billet step does not need, but its flat route has cheaper conversion than forging. Greenfield melting decision H1 2027, production end 2029.")
    r("benchmark", "Aperam Imphy VIM complex inside the four site programme", "VIM (melting), not remelt", "", "", 160, "EUR m (upper bound for the whole programme)",
      "EUR 160 m covers Genk, Chatelet, Gueugnon and the Imphy VIM complex, split and kilotonnes not disclosed", "CO_APERAM_INVEST_2026",
      "No per tonne value possible. VIM is the melt before remelt, so it bounds the upstream step, not VAR or ESR. Ceiling for the VIM complex only.")
    r("benchmark", "Carpenter Athens brownfield expansion", "mixed, group capex", "", "", "355 to 375", "USD m (FY2027 group capex guidance)",
      "FY2026 capex USD 242.7 m, FY2027 guidance USD 355 to 375 m, mainly Athens, furnace types and tonnes not stated", "CO_CRS_CAPEX_2026",
      "No per tonne value possible (furnace types and tonnes TODO(data)). Shows the scale of one integrated brownfield step, a ceiling for the step including powder and finishing.")
    r("benchmark", "Alleima fourth VAR furnace at Sandviken", "remelt (VAR)", "", "", "not published", "capex not disclosed",
      "Installed summer 2025, operational autumn 2025, about four months from installation to operation", "CO_ALLEIMA_VAR_2025", "Timing anchor for a VAR furnace only. No capex or tonnes in the repository (TODO(data)).")
    r("benchmark", "ATI Monroe fifth VIM furnace", "VIM (melting), not remelt", "", 9000, "", "tonnes a year",
      "About 9 kt a year from H2 2027, capex not disclosed", "ARGUS_SUPERALLOY", "Scale anchor only. A 1.5 kt step is 17 percent and a 3 kt step 33 percent of one Monroe VIM furnace.")
    r("benchmark", "Acerinox (Haynes) US high performance alloys programme", "melt, forge, rolling", "", "", 200, "USD m, ready 2028",
      "Induction furnace, rotary forge, large diameter bar finishing and hot rolling at Kokomo and Ghent, tonnes not stated", "CO_HAYN_CAPEX_2026",
      "No per tonne value possible (TODO(data)). Timing anchor: announced H1 2026, ready 2028, about two years for a melt and conversion programme.")
    r("assumption", "Capex per annual tonne used", "low / central / high", round(k_lo), round(k_hi_flat), round(k_hi), "EUR per annual tonne",
      f"Low = Avesta phase 1 remelting. Central = Avesta total. High = Avesta total times {SMALL_SCALE} (small scale premium for a 1.5 to 3 kt step, team assumption)", "CO_OUTOKUMPU_AVESTA_NI_2026",
      "Team estimate. Only one pair of capex and tonnes exists in the repository, so the range is wide on purpose. Excludes qualification cost, working capital and the VIM stage (existing melt stock is bought or toll melted).")

    # 2. cheque
    out = {}
    for kt in (1.5, 3.0):
        cap = (kt * k_lo / 1000.0, kt * k_hi_flat / 1000.0, kt * k_hi / 1000.0)      # EUR m
        sales = (kt * uv_lo, kt * uv_mid, kt * uv_hi)
        # cases: best = low capex, high price, high margin; central; worst = high capex, low price, low margin
        prof = (sales[2] * MARGIN[2], sales[1] * MARGIN[1], sales[0] * MARGIN[0])
        # payback ranges: best, central, worst
        pb = (cap[0] / prof[0], cap[1] / prof[1], cap[2] / prof[2])
        pbr = (payback_with_ramp(cap[0], prof[0]), payback_with_ramp(cap[1], prof[1]), payback_with_ramp(cap[2], prof[2]))
        out[kt] = dict(cap=cap, sales=sales, prof=prof, pb=pb, pbr=pbr)
        r("cheque", f"Capex for {kt:g} kt a year", "low / central / high", round(cap[0], 1), round(cap[1], 1), round(cap[2], 1), "EUR m", f"{kt:g} kt times capex per annual tonne", "CO_OUTOKUMPU_AVESTA_NI_2026", "Team estimate.")
        r("economics", f"Annual sales at {kt:g} kt", "low / mid / high unit value", round(sales[0], 1), round(sales[1], 1), round(sales[2], 1), "EUR m",
          f"{kt:g} kt times EUR {uv_lo:.1f} / {uv_mid:.1f} / {uv_hi:.1f} per kg (superalloy family unit values with premium)", "AC_EU_NI_UNITVAL_2024, TE_NI_HPA_FINISH_UV_2025, MODEL_VALUE_SUPER_PREMIUM",
          "Full utilisation. Remelt stock sells below bar, so the high end is an upper indication." + (" EUR 38 to 71 m." if kt == 1.5 else ""))
        r("economics", f"Operating profit at {kt:g} kt", "worst / central / best", round(prof[2], 1), round(prof[1], 1), round(prof[0], 1), "EUR m a year",
          "Low sales at 14.0 percent, mid sales at 19.4 percent, high sales at 24.8 percent", "CO_ATI_OPINC_2025, CO_HWM_OPINC_2025", "Peer operating margins are group margins of ATI (14.0) and Howmet (24.8), not margins of a remelt step. Team estimate.")
        r("economics", f"Simple payback at {kt:g} kt", "best / central / worst", round(pb[0], 1), round(pb[1], 1), round(pb[2], 1), "years of full utilisation",
          "Capex over operating profit, before tax, no working capital, no ramp, no qualification cost", "", "Best = low capex with best profit. Worst = high capex with worst profit.")
        r("economics", f"Payback with a three year ramp at {kt:g} kt", "best / central / worst", round(pbr[0], 1), round(pbr[1], 1), round(pbr[2], 1), "years from the first approved tonne",
          "Sales at 33, 67 and 100 percent in years 1 to 3", "", "Counts from the first approved tonne, not from the decision.")

    # 3. timing (decision Q1 2028 = 2028.1)
    d = 2028.1
    build = (1.5, 2.0, 2.5)   # years to commissioning: Avesta ESR 1.5, Haynes about 2, Avesta greenfield melting 2.5
    qual = (0.5, 1.5, 2.0)    # years from commissioning to first approved tonne (fast: non rotating AMS 5662/5663 with parallel qualification, central 18 months, slow: 24 months rotating)
    first = tuple(d + b + q for b, q in zip(build, qual))
    r("timing", "Decision", "", "", 2028.1, "", "year (Q1 2028)", "Team plan", "", "")
    r("timing", "Build and commissioning of the remelt step", "fast / central / slow", build[0], build[1], build[2], "years",
      "Avesta ESR 1.5 years (August 2026 announcement to early 2028), Haynes about 2 years (H1 2026 to 2028), Avesta greenfield melting 2.5 years (H1 2027 decision to end 2029), Alleima VAR about 4 months from installation to operation (excluded: installation only)",
      "CO_OUTOKUMPU_AVESTA_NI_2026, CO_HAYN_CAPEX_2026, CO_ALLEIMA_VAR_2025", "Team estimate from three disclosed timelines.")
    r("timing", "Qualification from commissioning to first approved tonne", "fast / central / slow", qual[0], qual[1], qual[2], "years",
      "Fast: non rotating Alloy 718 bar to AMS 5662 and 5663, qualification runs in parallel with commissioning. Central: 12 to 24 months furnace approval (industry review). Slow: rotating grades, ATI isothermal forging lead times over two years.",
      "CO_BA_RAWMAT_2025, CO_ATI_LEAD_2026", "Boeing says qualifying an alternative source of titanium and aluminium products can take a year or more (a metal other than nickel, used as a lower bound for the order of magnitude). The 12 to 24 month furnace approval is an industry reviewer statement, not a logged source.")
    r("timing", "First approved tonne (year)", "fast / central / slow", round(first[0], 1), round(first[1], 1), round(first[2], 1), "calendar year",
      "Decision Q1 2028 plus build plus qualification", "", "Team estimate. First revenue from added capacity about 2031 in the central case, matching the industry review.")
    window = 2030
    r("timing", "Competitor capacity on stream (window narrows)", "", "", "end 2029", "", "year",
      "Alleima fourth VAR autumn 2025, ATI Monroe fifth VIM H2 2027, Avesta ESR early 2028, Haynes programme 2028, Avesta greenfield melting end 2029", "CO_ALLEIMA_VAR_2025, ARGUS_SUPERALLOY, CO_OUTOKUMPU_AVESTA_NI_2026, CO_HAYN_CAPEX_2026",
      "The window narrows around 2030 because the announced additions of the other melters are all on stream by the end of 2029.")
    verdict = []
    for name, y in zip(("fast", "central", "slow"), first):
        verdict.append(f"{name} {y:.1f} ({'in' if int(y) <= window else 'after'} 2030)")
    r("timing", "Lands before the window narrows (2030)?", "fast / central / slow", "yes (2030)" if int(first[0]) <= window else "no", "yes" if int(first[1]) <= window else "no", "yes" if int(first[2]) <= window else "no", "",
      "; ".join(verdict), "", "Only the fast case (non rotating 718 bar qualified alongside commissioning, first tonne in Q1 2030) lands in 2030, at the edge of the window. The central and slow cases land after the window narrows, so the remelt step must be positioned for share of growth and for replacement of cobalt bearing and imported stock, not for scarcity.")
    return pd.DataFrame(rows), out, first


if __name__ == "__main__":
    df, out, first = build(25.4, 35.9, 47.1)
    print(df[["block", "item", "low", "mid", "high", "unit"]].to_string())
