"""
Fetch coffee market data from public APIs (no keys required).

Produces:
  - coffee_prices_monthly.csv     (FRED: Arabica + Robusta monthly prices, 1992-present)
  - arabica_futures_daily.csv     (Yahoo Finance: ICE "C" daily OHLCV, 2000-present)
  - exchange_rates_annual.csv     (World Bank: LCU per USD for coffee-producing countries)
  - brl_usd_daily.csv             (FRED: daily BRL/USD)
  - development_indicators.csv    (World Bank: GDP, agriculture %, population, rural %)
  - coffee_exports_by_country.csv (UN COMTRADE: annual export volume and value, HS 0901)

Usage:
    uv run --with requests --with pandas --with yfinance scripts/fetch_market_data.py
"""

import time
from pathlib import Path

import pandas as pd
import requests

OUT_DIR = Path("data/processed")
RAW_DIR = Path("data/raw")

# Coffee-producing countries (ISO2 for World Bank, UN codes for COMTRADE)
WB_COUNTRIES = "BR;VN;CO;ET;RW;UG;KE;HN;GT;CR;ID"
COMTRADE_COUNTRIES = {
    "076": "Brazil",
    "704": "Vietnam",
    "170": "Colombia",
    "231": "Ethiopia",
    "646": "Rwanda",
    "800": "Uganda",
    "404": "Kenya",
    "340": "Honduras",
    "320": "Guatemala",
    "360": "Indonesia",
    "188": "Costa Rica",
    "604": "Peru",
}


# ---------------------------------------------------------------------------
# FRED: Coffee prices + BRL/USD
# ---------------------------------------------------------------------------
def fetch_fred_csv(series_id: str, filename: str) -> pd.DataFrame:
    """Download a FRED series as CSV (no API key needed)."""
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    print(f"  Fetching FRED {series_id}...")
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    path = RAW_DIR / filename
    path.write_bytes(resp.content)
    return pd.read_csv(path, parse_dates=["observation_date"])


def fetch_coffee_prices():
    """Monthly Arabica and Robusta prices from FRED (IMF commodity series)."""
    print("\n=== Coffee Prices (FRED) ===")
    df_a = fetch_fred_csv("PCOFFOTMUSDM", "arabica_prices.csv")
    df_r = fetch_fred_csv("PCOFFROBUSDM", "robusta_prices.csv")

    df_a = df_a.rename(columns={"observation_date": "date", "PCOFFOTMUSDM": "arabica_cents_per_lb"})
    df_r = df_r.rename(columns={"observation_date": "date", "PCOFFROBUSDM": "robusta_cents_per_lb"})

    df_a["arabica_cents_per_lb"] = pd.to_numeric(df_a["arabica_cents_per_lb"], errors="coerce")
    df_r["robusta_cents_per_lb"] = pd.to_numeric(df_r["robusta_cents_per_lb"], errors="coerce")

    df = df_a.merge(df_r, on="date", how="outer").sort_values("date")
    df["arabica_usd_per_kg"] = df["arabica_cents_per_lb"] * 2.20462 / 100
    df["robusta_usd_per_kg"] = df["robusta_cents_per_lb"] * 2.20462 / 100
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month

    df.to_csv(OUT_DIR / "coffee_prices_monthly.csv", index=False)
    print(f"  Saved coffee_prices_monthly.csv ({len(df)} rows, {df['date'].min().date()} to {df['date'].max().date()})")


def fetch_brl_usd():
    """Daily BRL/USD exchange rate from FRED."""
    print("\n=== BRL/USD Daily (FRED) ===")
    df = fetch_fred_csv("DEXBZUS", "brl_usd.csv")
    df = df.rename(columns={"observation_date": "date", "DEXBZUS": "brl_per_usd"})
    df["brl_per_usd"] = pd.to_numeric(df["brl_per_usd"], errors="coerce")
    df.to_csv(OUT_DIR / "brl_usd_daily.csv", index=False)
    print(f"  Saved brl_usd_daily.csv ({len(df)} rows)")


# ---------------------------------------------------------------------------
# Yahoo Finance: Arabica futures
# ---------------------------------------------------------------------------
def fetch_arabica_futures():
    """Daily ICE 'C' Arabica futures from Yahoo Finance."""
    print("\n=== Arabica Futures (Yahoo Finance) ===")
    try:
        import yfinance as yf
    except ImportError:
        print("  SKIPPED: yfinance not installed. Run with --with yfinance")
        return

    kc = yf.Ticker("KC=F")
    df = kc.history(period="max")
    if df.empty:
        print("  WARNING: no data returned")
        return

    df = df.reset_index()
    df["Date"] = pd.to_datetime(df["Date"]).dt.tz_localize(None)
    df = df.rename(columns={
        "Date": "date", "Open": "open", "High": "high",
        "Low": "low", "Close": "close", "Volume": "volume",
    })
    df = df[["date", "open", "high", "low", "close", "volume"]].copy()
    df["close_usd_per_kg"] = df["close"] * 2.20462 / 100
    df.to_csv(OUT_DIR / "arabica_futures_daily.csv", index=False)
    print(f"  Saved arabica_futures_daily.csv ({len(df)} rows, {df['date'].min().date()} to {df['date'].max().date()})")


# ---------------------------------------------------------------------------
# World Bank: Exchange rates + development indicators
# ---------------------------------------------------------------------------
def fetch_wb_indicator(indicator_id: str, name: str, date_range: str = "1990:2024") -> list[dict]:
    """Fetch a World Bank indicator for coffee-producing countries."""
    url = (
        f"https://api.worldbank.org/v2/country/{WB_COUNTRIES}"
        f"/indicator/{indicator_id}?format=json&per_page=1000&date={date_range}"
    )
    resp = requests.get(url, timeout=30)
    data = resp.json()
    if len(data) <= 1 or not data[1]:
        return []
    return [
        {
            "country_code": r["countryiso3code"],
            "country": r["country"]["value"],
            "year": int(r["date"]),
            name: r["value"],
        }
        for r in data[1]
    ]


def fetch_exchange_rates():
    """Annual official exchange rates (LCU per USD) from World Bank."""
    print("\n=== Exchange Rates (World Bank) ===")
    rows = fetch_wb_indicator("PA.NUS.FCRF", "exchange_rate_lcu_per_usd")
    df = pd.DataFrame(rows).sort_values(["country_code", "year"])
    df.to_csv(OUT_DIR / "exchange_rates_annual.csv", index=False)
    print(f"  Saved exchange_rates_annual.csv ({len(df)} rows, {df['country'].unique().tolist()})")


def fetch_development_indicators():
    """Key development indicators from World Bank."""
    print("\n=== Development Indicators (World Bank) ===")
    indicators = {
        "NV.AGR.TOTL.ZS": "agriculture_pct_gdp",
        "NY.GDP.PCAP.CD": "gdp_per_capita_usd",
        "SP.POP.TOTL": "population",
        "SP.RUR.TOTL.ZS": "rural_population_pct",
        "AG.LND.ARBL.ZS": "arable_land_pct",
    }

    all_rows = []
    for ind_id, ind_name in indicators.items():
        print(f"  Fetching {ind_name}...")
        rows = fetch_wb_indicator(ind_id, ind_name, "2000:2024")
        all_rows.extend(rows)
        time.sleep(0.5)

    df = pd.DataFrame(all_rows)
    # Merge rows for same country-year across indicators
    df = df.groupby(["country_code", "country", "year"], as_index=False).first()
    df = df.sort_values(["country_code", "year"])
    df.to_csv(OUT_DIR / "development_indicators.csv", index=False)
    print(f"  Saved development_indicators.csv ({len(df)} rows)")


# ---------------------------------------------------------------------------
# UN COMTRADE: Coffee exports
# ---------------------------------------------------------------------------
def fetch_comtrade_exports():
    """Annual coffee exports (HS 0901) by country from UN COMTRADE public API."""
    print("\n=== Coffee Exports (UN COMTRADE) ===")
    all_rows = []

    for code, name in COMTRADE_COUNTRIES.items():
        for year in range(2000, 2024):
            url = (
                f"https://comtradeapi.un.org/public/v1/preview/C/A/HS"
                f"?cmdCode=0901&period={year}&reporterCode={code}&partnerCode=0&flowCode=X"
            )
            try:
                resp = requests.get(url, timeout=15)
                if resp.status_code == 200:
                    data = resp.json()
                    if "data" in data and data["data"]:
                        for r in data["data"]:
                            all_rows.append({
                                "year": year,
                                "country_code": code,
                                "country": name,
                                "net_weight_kg": r.get("netWgt"),
                                "primary_value_usd": r.get("primaryValue"),
                            })
            except Exception:
                pass
            time.sleep(0.3)
        print(f"  {name}: done")

    if not all_rows:
        print("  WARNING: no data retrieved")
        return

    df = pd.DataFrame(all_rows)
    df_agg = df.groupby(["year", "country_code", "country"], as_index=False).agg(
        net_weight_kg=("net_weight_kg", "sum"),
        primary_value_usd=("primary_value_usd", "sum"),
    )
    df_agg["export_volume_mt"] = df_agg["net_weight_kg"] / 1000
    df_agg["export_value_million_usd"] = df_agg["primary_value_usd"] / 1e6
    df_agg["avg_price_usd_per_kg"] = df_agg.apply(
        lambda r: r["primary_value_usd"] / r["net_weight_kg"]
        if r["net_weight_kg"] and r["net_weight_kg"] > 0 else None,
        axis=1,
    )
    df_agg = df_agg[
        ["year", "country_code", "country", "export_volume_mt", "export_value_million_usd", "avg_price_usd_per_kg"]
    ].sort_values(["country", "year"])
    df_agg.to_csv(OUT_DIR / "coffee_exports_by_country.csv", index=False)
    print(f"  Saved coffee_exports_by_country.csv ({len(df_agg)} rows)")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    fetch_coffee_prices()
    fetch_brl_usd()
    fetch_arabica_futures()
    fetch_exchange_rates()
    fetch_development_indicators()
    fetch_comtrade_exports()

    print("\n=== All done ===")
    print(f"\nFiles in {OUT_DIR}/:")
    for f in sorted(OUT_DIR.iterdir()):
        print(f"  {f.name:45s} {f.stat().st_size:>10,} bytes")


if __name__ == "__main__":
    main()
