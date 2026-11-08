#!/usr/bin/env python3
"""Opportunity matrix scoring (chapter 8, Table 16 and Table A4) computed from explicit rules.

Round 5: three of the eight criteria are computed from data, never typed in:
  Market attractiveness  from the end use specific measured pool (rule table MARKET_RULES)
  Growth to 2035        from the P50 growth a year of the most specific model index (GROWTH_BANDS) or, for early signals, from the earliest volume year
  Supply security       from the weakest input of the lead grades (INPUT_SCORE), using the restriction regime of each input element
The other five criteria (competitive intensity, technology, customers, entry barriers, differentiation) are team judgement on the
anchors of Table A4 and are carried as inputs (JUDGEMENT), because the repository holds no measured data for them. Entry barriers are
TODO(data) in years: Table A13 gives no approval times.

Inputs  data/clean/model_scoring_inputs.csv  (written by model/outlook_2035.py: P50 growth by driver, pools)
Output  data/clean/model_scores.csv          scores, weighted score, tier, equal weight and 20 percent barrier sensitivities (full precision)
Run: python3 model/scoring.py   (also called by model/outlook_2035.py, which passes shock overrides)
"""
import csv
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CLEAN = os.path.join(ROOT, "data", "clean")

CRIT = [("market", 0.15), ("growth", 0.20), ("supply", 0.15), ("competition", 0.10), ("technology", 0.10),
        ("customer", 0.10), ("barrier", 0.10), ("differentiation", 0.10)]
W = dict(CRIT)
assert abs(sum(W.values()) - 1.0) < 1e-12

# ---------------------------------------------------------------- rules (Table A4 style)
# Growth: P50 annual growth of the most specific index. 4.0 percent or more = 5, 3.0 to 3.99 = 4, 2.0 to 2.99 = 3, 0 to 1.99 = 2, below 0 = 1
GROWTH_BANDS = [(0.040, 5), (0.030, 4), (0.020, 3), (0.000, 2)]


def growth_score(g):
    for lo, sc in GROWTH_BANDS:
        if g >= lo:
            return sc
    return 1


def growth_score_signal(year):
    """Early signals have no modelled index: score on the earliest volume year (3 by 2028, 2 for 2029 to 2033, 1 later)."""
    return 3 if year <= 2028 else (2 if year <= 2033 else 1)


# Market: the pool must be specific to the opportunity's end use.
#   measured_kt_co   measured or derived contained cobalt in the end use, kt: 10 or more = 5, 5 to 10 = 4, 2 to 5 = 3, below 2 = 2 (derived pools are capped at 4)
#   estimated_eur_bn wider measured product code (PRODCOM, EU27) times a team estimate end use weight: 1.5 bn or more = 4 (cap, weight unmeasured),
#                    0.75 to 1.5 = 4, 0.30 to 0.75 = 3, below 0.30 = 2
#   company_end_use  revenue of one end use in a company filing, mixed alloys: 3 (measured niche), 4 from EUR 0.75 bn
#   wider_segment    a measured segment that mixes the product with others and has no end use split: 2
#   none             no measured or estimable volume of the product (capacity announcements and activity counts do not count): 1
def market_score(kind, value, derived=False):
    if kind == "measured_kt_co":
        sc = 5 if value >= 10 else (4 if value >= 5 else (3 if value >= 2 else 2))
        return min(sc, 4) if derived else sc
    if kind == "estimated_eur_bn":
        return 4 if value >= 0.75 else (3 if value >= 0.30 else 2)
    if kind == "company_end_use":
        return 4 if value >= 0.75 else 3
    if kind == "wider_segment":
        return 2
    return 1


# Supply security: lowest score over the inputs of the lead grades.
# regime per input: none 5, form_not_used 4 (control on a form that melters do not buy), price_only 4 (ore quota, alloy feed outside the quota),
#   quota_minor 3 (Congo cobalt quota, element below 10 percent of the alloy), licence_minor 2 (Chinese licence regime, element below 10 percent),
#   quota_principal 2 (Congo quota, element above 10 percent), licence_principal 1, halt 1 (active licence halt)
INPUT_SCORE = {"none": 5, "form_not_used": 4, "price_only": 4, "quota_minor": 3, "licence_minor": 2, "quota_principal": 2,
               "licence_principal": 1, "halt": 1}

# Opportunity definitions. inputs: (element, regime); judgement: comp, tech, cust, barr, diff carried from round 4 (anchors in Table A4).
# growth: ("index", key) or ("signal", earliest volume year). pool: key into the pool table written by outlook_2035.py.
OPPS = [
    dict(id="Turbine remelt stock and sheet", growth=("index", "energy"), pool="turbine", derived=True,
         inputs=[("cobalt", "quota_minor"), ("nickel", "none"), ("chromium", "none")],
         sens_inputs=[("tungsten (not evidenced for these alloys, TODO(data))", "licence_minor")],
         judgement=dict(competition=2, technology=4, customer=5, barrier=5, differentiation=4)),
    dict(id="Engine bar and billet", growth=("index", "aerospace"), pool="aviation", derived=False,
         inputs=[("cobalt", "quota_minor"), ("nickel", "none"), ("niobium and chromium", "none")], sens_inputs=[],
         judgement=dict(competition=2, technology=5, customer=5, barrier=4, differentiation=4)),
    dict(id="FeNi36 foil and FeNi strip", growth=("index", "feni"), pool="feni", derived=False,
         inputs=[("nickel", "none"), ("iron", "none")], sens_inputs=[],
         judgement=dict(competition=2, technology=5, customer=3, barrier=3, differentiation=4)),
    dict(id="CoCr implant bar and powder", growth=("index", "medical"), pool="medical", derived=False,
         inputs=[("cobalt (about 60 percent of Co28Cr6Mo)", "quota_principal"), ("chromium", "none")], sens_inputs=[],
         judgement=dict(competition=3, technology=4, customer=4, barrier=5, differentiation=3)),
    dict(id="Sour service bar, strip, wire", growth=("index", "oil_and_gas"), pool="sour", derived=False,
         inputs=[("nickel", "none"), ("molybdenum (powder control only)", "form_not_used")], sens_inputs=[],
         judgement=dict(competition=3, technology=3, customer=3, barrier=5, differentiation=3)),
    dict(id="Chemical plate, welding wire", growth=("index", "chemical"), pool="chemical", derived=False,
         inputs=[("nickel", "none"), ("molybdenum (powder control only)", "form_not_used"),
                 ("tungsten in C-276 (about 4 percent) under the Chinese licence", "licence_minor")], sens_inputs=[],
         judgement=dict(competition=2, technology=3, customer=3, barrier=3, differentiation=3)),
    dict(id="Alloy 690 bar and hollows", growth=("index", "nuclear"), pool="alloy690", derived=False,
         inputs=[("nickel", "none"), ("chromium", "none")], sens_inputs=[],
         judgement=dict(competition=3, technology=4, customer=4, barrier=3, differentiation=3)),
    dict(id="Solid oxide cell strip", growth=("signal", 2026), pool="none", derived=False,
         inputs=[("chromium (ferritic steel)", "none"), ("nickel coating", "none")], sens_inputs=[],
         judgement=dict(competition=3, technology=4, customer=2, barrier=3, differentiation=4)),
    dict(id="Alloy C-276 fusion tape foil", growth=("signal", 2030), pool="none", derived=False,
         inputs=[("nickel", "none"), ("molybdenum (powder control only)", "form_not_used"),
                 ("tungsten in C-276 (about 4 percent) under the Chinese licence", "licence_minor")], sens_inputs=[],
         judgement=dict(competition=4, technology=5, customer=2, barrier=3, differentiation=5)),
    dict(id="AM powder, CoCr and nickel superalloy", growth=("index", "aero_new"), pool="am_powder", derived=False,
         inputs=[("cobalt (CoCr lead grade F75)", "quota_principal"), ("nickel", "none")], sens_inputs=[],
         judgement=dict(competition=2, technology=4, customer=4, barrier=3, differentiation=3)),
    dict(id="Car exhaust and turbo alloys", growth=("index", "automotive_thermal"), pool="car", derived=False,
         inputs=[("nickel", "none"), ("chromium", "none")], sens_inputs=[],
         judgement=dict(competition=3, technology=1, customer=2, barrier=3, differentiation=2)),
]

# Round 4 hand scored matrix (Table 16 of report v4), kept only to show what the rules changed: mkt, gro, sup, comp, tech, cust, barr, diff
ROUND4 = {
    "Turbine remelt stock and sheet": (4, 5, 3, 2, 4, 5, 5, 4), "Engine bar and billet": (5, 4, 3, 2, 5, 5, 4, 4),
    "FeNi36 foil and FeNi strip": (3, 5, 5, 2, 5, 3, 3, 4), "CoCr implant bar and powder": (3, 4, 2, 3, 4, 4, 5, 3),
    "Sour service bar, strip, wire": (4, 2, 4, 3, 3, 3, 5, 3), "Chemical plate, welding wire": (5, 2, 4, 2, 3, 3, 3, 3),
    "Alloy 690 bar and hollows": (2, 2, 5, 3, 4, 4, 3, 3), "Solid oxide cell strip": (2, 3, 4, 3, 4, 2, 3, 4),
    "Alloy C-276 fusion tape foil": (1, 2, 4, 4, 5, 2, 3, 5), "AM powder, CoCr and nickel superalloy": (2, 3, 3, 2, 4, 4, 3, 3),
    "Car exhaust and turbo alloys": (3, 1, 5, 3, 1, 2, 3, 2)}


def weighted(sc, weights=W):
    return sum(weights[k] * sc[k] for k in weights)


def tier(score, evidence, cap=True):
    score = round(score, 9)   # guards the thresholds against floating point noise only
    if evidence == "E" and cap:
        return "Option" if score >= 3.0 else "Monitor"
    if score >= 3.75:
        return "1"
    if score >= 3.0:
        return "2"
    return "Monitor" if score >= 2.75 else "Harvest"


def barrier_weights_proportional(share=0.20):
    rest = 1.0 - W["barrier"]
    return {k: (share if k == "barrier" else W[k] * (1.0 - share) / rest) for k in W}


def barrier_weights_equal_cut(share=0.20):
    d = (share - W["barrier"]) / (len(W) - 1)
    return {k: (share if k == "barrier" else W[k] - d) for k in W}


EQUAL = {k: 1.0 / len(W) for k in W}


def read_inputs(path=None):
    path = path or os.path.join(CLEAN, "model_scoring_inputs.csv")
    d = {}
    for r in csv.DictReader(open(path, encoding="utf-8")):
        d[(r["kind"], r["key"])] = r
    return d


def score_all(inp, supply_override=None, growth_override=None, label=""):
    """supply_override: {element keyword: regime} replaces the regime of matching inputs (shock runs).
    growth_override: {index key: P50 annual growth} replaces the model growth (severe aerospace run)."""
    out = []
    for o in OPPS:
        sc = {}
        # market
        pr = inp[("pool", o["pool"])]
        sc["market"] = market_score(pr["pool_kind"], float(pr["pool_value"]) if pr["pool_value"] not in ("", "none") else 0.0, o["derived"])
        # growth
        gk, gv = o["growth"]
        if gk == "index":
            g = (growth_override or {}).get(gv, float(inp[("growth", gv)]["p50_cagr"]))
            sc["growth"] = growth_score(g)
        else:
            g = None
            sc["growth"] = growth_score_signal(gv)
        # supply
        regimes = []
        for el, rg in o["inputs"]:
            for kw, newrg in (supply_override or {}).items():
                if kw in el:
                    rg = newrg
            regimes.append((el, rg, INPUT_SCORE[rg]))
        sc["supply"] = min(x[2] for x in regimes)
        sens = min([x[2] for x in regimes] + [INPUT_SCORE[rg] for _, rg in o["sens_inputs"]])
        sc.update(o["judgement"])
        ev = "E" if pr["pool_kind"] == "none" else "M"
        s = weighted(sc)
        out.append(dict(opportunity=o["id"], evidence=ev, **{k: sc[k] for k, _ in CRIT}, growth_p50_cagr_pct=("" if g is None else g * 100.0),
                        market_basis=f"{pr['pool_kind']} {pr['pool_value']} {pr['unit']}", supply_weakest=min(regimes, key=lambda x: x[2])[0],
                        supply_if_untested_inputs_counted=sens,
                        weighted_score=s, tier=tier(s, ev), tier_without_early_signal_cap=tier(s, ev, cap=False),
                        score_equal_weights=weighted(sc, EQUAL), tier_equal_weights=tier(weighted(sc, EQUAL), ev),
                        score_barriers_20pct_proportional=weighted(sc, barrier_weights_proportional()),
                        score_barriers_20pct_equal_cut=weighted(sc, barrier_weights_equal_cut()),
                        round4_score=weighted(dict(zip([k for k, _ in CRIT], ROUND4[o["id"]]))),
                        case=label))
    return out


def write(rows, path=None):
    path = path or os.path.join(CLEAN, "model_scores.csv")
    flds = list(rows[0].keys())
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=flds)
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    inp = read_inputs()
    rows = score_all(inp, label="base")
    write(rows)
    for r in sorted(rows, key=lambda x: -x["weighted_score"]):
        print(f"{r['opportunity']:42s} {r['weighted_score']:.3f} tier {r['tier']:8s} (uncapped {r['tier_without_early_signal_cap']}) mkt {r['market']} gro {r['growth']} sup {r['supply']}")
