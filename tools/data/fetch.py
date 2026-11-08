#!/usr/bin/env python3
"""Reproducible data pulls from the structured databases required by the brief.

Every command saves the raw download in data/raw/<source>/, a tidy CSV in data/clean/, and appends a provenance
row to data/sources.csv (type primary, exact query URL, retrieval date), so the market model stays transparent.

  python3 tools/data/fetch.py comtrade  --hs 7502,7505,7506,7507 --reporters 276,842,156,392 --years 2019-2024 [--flow X,M]
  # Prefer a free subscribed key (avoids preview 403). Create at https://comtradeplus.un.org/MyComtrade/APIPortal
  #   export COMTRADE_API_KEY=...
  python3 tools/data/fetch.py comtrade-import --file TradeData_….csv   # browser CSV already in data/raw/comtrade/
  python3 tools/data/fetch.py pinksheet                       # World Bank monthly commodity prices (metals)
  python3 tools/data/fetch.py usgs      [--commodity Nickel]  # USGS MCS 2026 data release (production, reserves)
  python3 tools/data/fetch.py prodcom   --product 24451100,24452100 --reporters EU27_2020,DE --years 2019-2024
  python3 tools/data/fetch.py eurostat  --dataset sts_inpr_a --filters "geo=DE,nace_r2=C24,unit=I21,s_adj=CA"
  python3 tools/data/fetch.py stan      --countries DEU,FRA,USA,JPN,KOR,CHN --activity C24,C25,C29,C30 --measure P1
  python3 tools/data/fetch.py sec       --ticker CRS  (or --cik 1018963) [--concepts Revenues,RevenueFromContractWithCustomerExcludingAssessedTax]
  python3 tools/data/fetch.py who       --indicator WHS9_88
  python3 tools/data/fetch.py list                            # show the HS and PRODCOM codes of the portfolio

Codes: UN M49 reporter codes (276 Germany, 842 USA, 156 China, 392 Japan, 410 Korea, 699 India, 251 France,
826 UK, 380 Italy, 360 Indonesia, 0 World). Note: 250 and 356 are obsolete/empty in current Comtrade
(France is 251; India ...1974 is 356, current India is 699). Not reachable automatically: UNIDO INDSTAT
(bot protection) and www.iea.org (bot check), so the team downloads those by hand into data/raw/unido/
and data/raw/iea/.
"""
import argparse, csv, fcntl, datetime, io, json, os, re, sys, time, urllib.parse, urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RAW, CLEAN = os.path.join(ROOT, "data", "raw"), os.path.join(ROOT, "data", "clean")
UA = os.environ.get("RESEARCH_USER_AGENT", "metals-strategy-2035 research (TUM project study)")
TODAY = datetime.date.today().isoformat()

# The Client portfolio expressed in trade (HS 2022) and PRODCOM codes
HS = {
    "7501": "Nickel mattes and intermediates", "7502": "Unwrought nickel", "7504": "Nickel powders and flakes",
    "7505": "Nickel bars, rods, profiles, wire", "7506": "Nickel plates, sheets, strip, foil",
    "750610": "Nickel plates, sheets, strip, foil, not alloyed",
    "750620": "Nickel plates, sheets, strip, foil, of nickel alloys",
    "7507": "Nickel tubes, pipes, fittings",
    "7508": "Other articles of nickel", "8105": "Cobalt mattes, unwrought cobalt, powders, articles",
    "8109": "Zirconium, unwrought, powders, articles", "8108": "Titanium and articles", "8101": "Tungsten and articles",
    "8102": "Molybdenum and articles", "7202": "Ferro alloys (incl. ferrochromium, ferromolybdenum)",
    "7218": "Stainless steel, primary forms", "7219": "Flat rolled stainless, 600 mm or wider", "7220": "Flat rolled stainless, under 600 mm",
    "7221": "Stainless bars, hot rolled coils", "7222": "Other stainless bars, angles", "7223": "Stainless wire",
    "7403": "Refined copper, unwrought", "7407": "Copper bars, rods, profiles", "7408": "Copper wire", "7409": "Copper plates, sheet, strip",
    "7410": "Copper foil", "7411": "Copper tubes", "7601": "Unwrought aluminium", "7604": "Aluminium bars, rods, profiles",
    "7605": "Aluminium wire", "7606": "Aluminium plates, sheet, strip", "7607": "Aluminium foil",
    "8311": "Wire, rods, electrodes for welding", "2604": "Nickel ores and concentrates", "2605": "Cobalt ores",
    "2615": "Zirconium ores (zircon)", "8411": "Turbojets, turbines (aerospace demand indicator)",
}
PRODCOM = {
    "24451100": "Unwrought nickel", "24451230": "Nickel powders and flakes", "24452100": "Nickel bars, rods, profiles, wire",
    "24452200": "Nickel plates, sheets, strip and foil", "24452300": "Nickel tubes, pipes and fittings",
    "24453030": "Unwrought cobalt, powders; articles", "24453063": "Zirconium, unwrought, powders; articles",
    "24104100": "Stainless steel ingots and primary forms", "24104330": "Flat rolled stainless, cold rolled",
    "24343000": "Stainless steel wire (cold drawn)", "25931300": "Welding electrodes, wire of base metal",
    "24442200": "Copper wire", "24442330": "Copper plates, sheets and strip", "24422200": "Aluminium wire",
    "24422430": "Aluminium plates, sheets and strip",
}


def get(url, binary=False, retries=6):
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
            with urllib.request.urlopen(req, timeout=120) as r:
                data = r.read()
            if binary:
                return data
            try:
                return data.decode("utf-8")
            except UnicodeDecodeError:
                return data.decode("cp1252", "replace")
        except Exception as e:  # noqa: BLE001
            code = getattr(e, "code", None)
            # Hard daily quota: stop immediately so the orchestrator can pause for hours.
            if code == 403 and "Quota" in str(e):
                raise
            if i == retries - 1:
                raise
            wait = 30 * (i + 1) if code == 429 else 3 * (i + 1)
            print(f"  retry after error: {e} (sleep {wait}s)", file=sys.stderr)
            time.sleep(wait)


def save_raw(source, name, data):
    d = os.path.join(RAW, source)
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, name)
    with open(p, "wb" if isinstance(data, bytes) else "w", **({} if isinstance(data, bytes) else {"encoding": "utf-8"})) as f:
        f.write(data)
    return p


def write_clean(name, rows, fields):
    os.makedirs(CLEAN, exist_ok=True)
    p = os.path.join(CLEAN, name)
    with open(p, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print(f"  wrote {len(rows)} rows to {os.path.relpath(p, ROOT)}")
    return p


def log_source(data_id, metric, source, author, title, url, notes, year=""):
    path = os.path.join(ROOT, "data", "sources.csv")
    lock = open(path + ".lock", "w")
    fcntl.flock(lock, fcntl.LOCK_EX)  # several agents may log at the same time
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    fields = list(rows[0].keys())
    row = {k: "" for k in fields}
    row.update(data_id=data_id, metric=metric, source=source, publisher=author, author=author, intext_author=author,
               pub_date=year or TODAY[:4], ref_type="dataset", title=title, url=url, retrieved=TODAY,
               type="primary", confidence="high", notes=notes)
    rows = [r for r in rows if r["data_id"] != data_id] + [row]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    fcntl.flock(lock, fcntl.LOCK_UN)
    print(f"  logged source {data_id}")


def years(spec):
    a, _, b = spec.partition("-")
    return list(range(int(a), int(b or a) + 1))


# ------------------------------------------------------------------ UN Comtrade
def comtrade_url(q):
    """Prefer free subscribed Data API when COMTRADE_API_KEY is set; else public preview."""
    key = os.environ.get("COMTRADE_API_KEY", "").strip()
    params = {k: v for k, v in q.items() if v}
    if key:
        params["subscription-key"] = key
        params.setdefault("maxRecords", "100000")
        return "https://comtradeapi.un.org/data/v1/get/C/A/HS?" + urllib.parse.urlencode(params), True
    return "https://comtradeapi.un.org/public/v1/preview/C/A/HS?" + urllib.parse.urlencode(params), False


def cmd_comtrade(a):
    out = []
    used_key = False
    for hs in a.hs.split(","):
        for rep in a.reporters.split(","):
            for flow, yr in [(f, y) for f in a.flow.split(",") for y in years(a.years)]:
                q = {"reporterCode": rep, "period": str(yr), "cmdCode": hs,
                     "flowCode": flow, "partnerCode": a.partners or None, "includeDesc": "true"}
                url, used_key = comtrade_url(q)
                try:
                    txt = get(url)
                except Exception as e:  # noqa: BLE001
                    # Propagate hard quota so a sequential pull can stop for the day.
                    if getattr(e, "code", None) == 403 and "Quota" in str(e):
                        raise
                    print(f"  FAILED {hs} {rep} {flow} {yr}: {e}")
                    continue
                save_raw("comtrade", f"hs{hs}_r{rep}_{flow}_{yr}.json", txt)
                for r in json.loads(txt).get("data", []):
                    out.append({"hs": hs, "hs_desc": HS.get(hs, r.get("cmdDesc", "")), "reporter": r.get("reporterDesc") or rep,
                                "reporter_code": r.get("reporterCode"), "partner": r.get("partnerDesc"), "partner_code": r.get("partnerCode"),
                                "flow": r.get("flowDesc") or flow, "year": r.get("period"), "value_usd": r.get("primaryValue"),
                                "net_weight_kg": r.get("netWgt"), "qty": r.get("qty"), "qty_unit": r.get("qtyUnitAbbr")})
                # Free subscribed API: 1 call/s; preview: keep ≥3 to 5 s between calls
                time.sleep(1.2 if used_key else 4.0)
    tag = a.out or f"comtrade_{a.hs.replace(',', '-')}_{a.years}"
    write_clean(f"{tag}.csv", out, ["hs", "hs_desc", "reporter", "reporter_code", "partner", "partner_code", "flow", "year",
                                     "value_usd", "net_weight_kg", "qty", "qty_unit"])
    api_note = "Subscribed Data API (COMTRADE_API_KEY)" if used_key else "Public preview API"
    log_source(re.sub(r"[^A-Z0-9]+", "_", f"COMTRADE_{a.hs}_{a.years}".upper())[:60], f"Trade flows HS {a.hs}, reporters {a.reporters}, {a.years}", "UN Comtrade database",
               "United Nations Statistics Division", f"UN Comtrade database [HS {a.hs}, {a.years}]",
               "https://comtradeplus.un.org/", f"{api_note}, flows {a.flow}. Clean file data/clean/{tag}.csv", year=TODAY[:4])


def cmd_comtrade_import(a):
    """Turn a Comtrade Plus browser CSV in data/raw/comtrade/ into data/clean/."""
    path = a.file if os.path.isabs(a.file) else os.path.join(RAW, "comtrade", a.file)
    if not os.path.exists(path):
        path = a.file
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows_in = list(csv.DictReader(f))
    out = []
    for r in rows_in:
        hs = (r.get("cmdCode") or r.get("commodityCode") or "").strip()
        if not hs or hs.lower().startswith("all"):
            continue
        out.append({
            "hs": hs,
            "hs_desc": HS.get(hs, r.get("cmdDesc") or r.get("commodityDesc") or ""),
            "reporter": r.get("reporterDesc") or r.get("reporterISO") or "",
            "reporter_code": r.get("reporterCode") or "",
            "partner": r.get("partnerDesc") or r.get("partnerISO") or "",
            "partner_code": r.get("partnerCode") or "",
            "flow": r.get("flowDesc") or r.get("flowCode") or "",
            "year": r.get("refYear") or r.get("period") or "",
            "value_usd": r.get("primaryValue") or r.get("cifValue") or r.get("fobValue") or "",
            "net_weight_kg": r.get("netWgt") or "",
            "qty": r.get("qty") or "",
            "qty_unit": r.get("qtyUnitAbbr") or r.get("qtyUnit") or "",
        })
    if not out:
        raise SystemExit(f"No usable commodity rows in {path} (got All Commodities or empty).")
    hs_set = sorted({r["hs"] for r in out})
    tag = a.out or f"comtrade_{'-'.join(hs_set[:6])}_import"
    write_clean(f"{tag}.csv", out, ["hs", "hs_desc", "reporter", "reporter_code", "partner", "partner_code", "flow", "year",
                                     "value_usd", "net_weight_kg", "qty", "qty_unit"])
    log_source(re.sub(r"[^A-Z0-9]+", "_", f"COMTRADE_IMPORT_{'-'.join(hs_set[:4])}".upper())[:60],
               f"Trade flows from Comtrade Plus CSV, HS {','.join(hs_set)}", "UN Comtrade database",
               "United Nations Statistics Division", f"UN Comtrade database [import {os.path.basename(path)}]",
               "https://comtradeplus.un.org/", f"Browser download imported from {path}. Clean file data/clean/{tag}.csv",
               year=TODAY[:4])


# ------------------------------------------------------------------ World Bank Pink Sheet
PINK_URL = os.environ.get("PINKSHEET_URL", "https://thedocs.worldbank.org/en/doc/18675f1d1639c7a34d463f59263ba0a2-0050012025/related/CMO-Historical-Data-Monthly.xlsx")


def cmd_pinksheet(a):
    import openpyxl
    data = get(PINK_URL, binary=True)
    p = save_raw("worldbank", "CMO-Historical-Data-Monthly.xlsx", data)
    wb = openpyxl.load_workbook(p, read_only=True, data_only=True)
    ws = wb["Monthly Prices"]
    rows = list(ws.iter_rows(values_only=True))
    hdr_i = next(i for i, r in enumerate(rows) if r and any(isinstance(c, str) and "Aluminum" in c for c in r))
    names = [str(c).strip() if c else "" for c in rows[hdr_i]]
    units = [str(c).strip() if c else "" for c in rows[hdr_i + 1]]
    keep = [i for i, n in enumerate(names) if re.search(r"Aluminum|Copper|Nickel|Iron ore|Lead|Tin|Zinc|Cobalt|Molybd|Crude oil, Brent|Natural gas, Europe", n)]
    out = []
    for r in rows[hdr_i + 2:]:
        if not r or not r[0] or not re.match(r"\d{4}M\d{2}", str(r[0])):
            continue
        for i in keep:
            if r[i] not in (None, "", "…"):
                out.append({"month": r[0], "commodity": names[i], "unit": units[i], "price": r[i]})
    write_clean("worldbank_pinksheet_monthly.csv", out, ["month", "commodity", "unit", "price"])
    log_source("WB_PINKSHEET", "Monthly commodity prices (metals, energy)", "Commodity Markets Outlook historical data (Pink Sheet)",
               "World Bank", "World Bank commodity price data (The Pink Sheet), monthly prices", PINK_URL,
               "Clean file data/clean/worldbank_pinksheet_monthly.csv. Cobalt is not in the Pink Sheet.")


# ------------------------------------------------------------------ USGS
USGS_ITEM = "69837e43b66b01367d7ec7c7"


def cmd_usgs(a):
    meta = json.loads(get(f"https://www.sciencebase.gov/catalog/item/{USGS_ITEM}?format=json"))
    f = next(x for x in meta["files"] if x["name"].endswith(".csv"))
    txt = get(f["url"])
    save_raw("usgs", f["name"], txt)
    rows = list(csv.DictReader(io.StringIO(txt)))
    if a.commodity:
        key = next((k for k in rows[0] if "ommodity" in k), None)
        rows = [r for r in rows if key and a.commodity.lower() in (r.get(key) or "").lower()]
    write_clean(f"usgs_mcs2026{('_' + a.commodity.lower()) if a.commodity else ''}.csv", rows, list(rows[0].keys()) if rows else ["empty"])
    log_source("USGS_MCS2026_DATA", "World mine production, reserves and U.S. salient statistics by commodity",
               "Mineral Commodity Summaries 2026 Data Release", "U.S. Geological Survey",
               "Mineral commodity summaries 2026 data release: Commodity salient U.S. and world statistics",
               f"https://www.sciencebase.gov/catalog/item/{USGS_ITEM}", "Raw CSV in data/raw/usgs/", year="2026")


# ------------------------------------------------------------------ Eurostat PRODCOM and other Eurostat tables
def cmd_prodcom(a):
    out = []
    for prod in a.product.split(","):
        for rep in a.reporters.split(","):
            for y in years(a.years):
                url = ("https://ec.europa.eu/eurostat/api/comext/dissemination/statistics/1.0/data/DS-059358?format=JSON&lang=EN&"
                       + urllib.parse.urlencode({"time": y, "product": prod, "reporter": rep}))
                try:
                    d = json.loads(get(url))
                except Exception as e:  # noqa: BLE001
                    print(f"  FAILED {prod} {rep} {y}: {e}")
                    continue
                save_raw("prodcom", f"{prod}_{rep}_{y}.json", json.dumps(d))
                ind = d["dimension"]["indicators"]["category"]
                order = sorted(ind["index"], key=lambda k: ind["index"][k])
                for pos, val in d.get("value", {}).items():
                    code = order[int(pos) % len(order)] if len(order) else pos
                    out.append({"product": prod, "product_desc": PRODCOM.get(prod, ""), "reporter": rep, "year": y,
                                "indicator": ind["label"].get(code, code), "value": val})
                time.sleep(0.3)
    # Never overwrite the portfolio file when a subset of product codes is requested.
    default_all = ",".join(PRODCOM)
    if a.out:
        tag = a.out if a.out.endswith(".csv") else f"{a.out}.csv"
    elif a.product == default_all:
        tag = f"prodcom_{a.years}.csv"
    else:
        tag = f"prodcom_{a.product.replace(',', '-')}_{a.years}.csv"
    write_clean(tag, out, ["product", "product_desc", "reporter", "year", "indicator", "value"])
    log_source("EUROSTAT_PRODCOM", f"Sold production, exports, imports, PRODCOM {a.product}", "PRODCOM DS-059358",
               "Eurostat", "Sold production, exports and imports (PRODCOM, DS-059358)",
               "https://ec.europa.eu/eurostat/web/prodcom/database", "Confidential cells are missing, not zero.")


def cmd_eurostat(a):
    q = dict(kv.split("=", 1) for kv in a.filters.split(",") if kv)
    url = f"https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/{a.dataset}?format=JSON&lang=EN&" + urllib.parse.urlencode(q)
    d = json.loads(get(url))
    save_raw("eurostat", f"{a.dataset}.json", json.dumps(d))
    t = d["dimension"]["time"]["category"]
    times = sorted(t["index"], key=lambda k: t["index"][k])
    out = [{"dataset": a.dataset, "filters": a.filters, "time": times[int(p) % len(times)], "value": v} for p, v in d.get("value", {}).items()]
    write_clean(f"eurostat_{a.dataset}.csv", out, ["dataset", "filters", "time", "value"])
    log_source(f"EUROSTAT_{a.dataset.upper()}", d.get("label", a.dataset), a.dataset, "Eurostat", d.get("label", a.dataset),
               f"https://ec.europa.eu/eurostat/databrowser/view/{a.dataset}/default/table", f"Filters {a.filters}")


# ------------------------------------------------------------------ OECD STAN
def cmd_stan(a):
    key = f"A.{a.countries.replace(',', '+')}.{a.activity.replace(',', '+')}.{a.measure}.V.XDC"
    url = f"https://sdmx.oecd.org/public/rest/data/OECD.STI.PIE,DSD_STAN@DF_STAN_2025,1.0/{key}?startPeriod={a.start}&format=csvfilewithlabels"
    txt = get(url)
    save_raw("oecd", f"stan_{a.measure}.csv", txt)
    rows = list(csv.DictReader(io.StringIO(txt)))
    write_clean(f"oecd_stan_{a.measure}.csv", rows, list(rows[0].keys()) if rows else ["empty"])
    log_source(f"OECD_STAN_{a.measure}", f"STAN {a.measure} by activity {a.activity}", "STAN Database for Structural Analysis (2025 edition)",
               "OECD", "STAN database for structural analysis (ISIC Rev. 4), 2025 edition",
               "https://data-explorer.oecd.org/", f"Key {key}. Measures: P1 output, B1G value added, EMP employment.")


# ------------------------------------------------------------------ SEC EDGAR (company filings)
def cmd_sec(a):
    if a.ticker:
        known = {r["sec_ticker"].upper(): r["sec_cik"] for r in csv.DictReader(open(os.path.join(ROOT, "data", "companies.csv"), encoding="utf-8")) if r.get("sec_cik")}
        if a.ticker.upper() in known:
            a.ticker, a.cik = "", known[a.ticker.upper()]
    if a.ticker:  # needs RESEARCH_USER_AGENT with a contact name and e-mail (SEC fair access policy)
        tick = json.loads(get("https://www.sec.gov/files/company_tickers.json"))
        hit = next((v for v in tick.values() if v["ticker"].upper() == a.ticker.upper().replace(".", "-")), None)
        if not hit:
            sys.exit(f"Ticker {a.ticker} not found at the SEC (company may not file there: use its IR site instead)")
        a.cik = str(hit["cik_str"])
    cik = f"{int(a.cik):010d}"
    sub = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik}.json"))
    save_raw("sec", f"submissions_{cik}.json", json.dumps(sub))
    name = sub.get("name", cik)
    rec = sub["filings"]["recent"]
    filings = [{"form": f, "date": d, "url": f"https://www.sec.gov/Archives/edgar/data/{int(a.cik)}/{acc.replace('-', '')}/{doc}"}
               for f, d, acc, doc in zip(rec["form"], rec["filingDate"], rec["accessionNumber"], rec["primaryDocument"])
               if f in ("10-K", "20-F", "10-Q", "8-K", "40-F")][:40]
    facts = json.loads(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"))
    save_raw("sec", f"companyfacts_{cik}.json", json.dumps(facts))
    out = []
    for concept in a.concepts.split(","):
        for unit, vals in facts.get("facts", {}).get("us-gaap", {}).get(concept, {}).get("units", {}).items():
            for v in vals:
                if v.get("form") in ("10-K", "20-F") and v.get("fp") == "FY":
                    out.append({"company": name, "concept": concept, "unit": unit, "fy": v.get("fy"), "end": v.get("end"), "value": v.get("val"), "form": v.get("form")})
    slug = re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")
    write_clean(f"sec_{slug}_facts.csv", out, ["company", "concept", "unit", "fy", "end", "value", "form"])
    write_clean(f"sec_{slug}_filings.csv", filings, ["form", "date", "url"])
    log_source(f"SEC_{slug.upper()}"[:60], f"Filings and XBRL financials of {name}", "SEC EDGAR", name,
               f"{name} filings (Form 10-K, 10-Q, 8-K) and XBRL company facts", f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}",
               f"Latest annual filing: {next((f['url'] for f in filings if f['form'] in ('10-K', '20-F')), 'n/a')}")


# ------------------------------------------------------------------ WHO GHO
def cmd_who(a):
    txt = get(f"https://ghoapi.azureedge.net/api/{a.indicator}")
    save_raw("who", f"{a.indicator}.json", txt)
    rows = [{"indicator": a.indicator, "country": r.get("SpatialDim"), "year": r.get("TimeDim"), "dim1": r.get("Dim1"), "value": r.get("NumericValue")}
            for r in json.loads(txt).get("value", [])]
    write_clean(f"who_{a.indicator}.csv", rows, ["indicator", "country", "year", "dim1", "value"])
    log_source(f"WHO_{a.indicator}", f"WHO GHO indicator {a.indicator}", "Global Health Observatory", "World Health Organization",
               f"Global Health Observatory data: {a.indicator}", f"https://www.who.int/data/gho/data/indicators", "")


def cmd_list(a):
    print("HS codes:")
    for k, v in HS.items():
        print(f"  {k}  {v}")
    print("PRODCOM codes:")
    for k, v in PRODCOM.items():
        print(f"  {k}  {v}")


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("comtrade"); p.add_argument("--hs", required=True); p.add_argument("--reporters", default="276,842,156,392,410,699,251,826,380,360")
    p.add_argument("--years", default="2019-2024"); p.add_argument("--flow", default="X,M"); p.add_argument("--partners", default=""); p.add_argument("--out", default="")
    p = sp.add_parser("comtrade-import"); p.add_argument("--file", required=True); p.add_argument("--out", default="")
    sp.add_parser("pinksheet")
    p = sp.add_parser("usgs"); p.add_argument("--commodity", default="")
    p = sp.add_parser("prodcom"); p.add_argument("--product", default=",".join(PRODCOM)); p.add_argument("--reporters", default="EU27_2020,DE")
    p.add_argument("--years", default="2019-2024"); p.add_argument("--out", default="")
    p = sp.add_parser("eurostat"); p.add_argument("--dataset", required=True); p.add_argument("--filters", default="")
    p = sp.add_parser("stan"); p.add_argument("--countries", default="DEU,FRA,ITA,USA,JPN,KOR,GBR"); p.add_argument("--activity", default="C24,C25,C27,C28,C29,C30")
    p.add_argument("--measure", default="P1"); p.add_argument("--start", default="2010")
    p = sp.add_parser("sec"); p.add_argument("--cik", default=""); p.add_argument("--ticker", default="")
    p.add_argument("--concepts", default="Revenues,RevenueFromContractWithCustomerExcludingAssessedTax,OperatingIncomeLoss,CostOfRevenue")
    p = sp.add_parser("who"); p.add_argument("--indicator", required=True)
    sp.add_parser("list")
    a = ap.parse_args()
    globals()[f"cmd_{a.cmd}"](a)


if __name__ == "__main__":
    main()
