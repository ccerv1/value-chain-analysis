"""
Fetch and process USDA PSD (Production, Supply, and Distribution) coffee data.

Downloads the bulk CSV from USDA FAS, then produces clean analysis-ready CSVs:
  - usda_production_by_country.csv   (annual production in 60-kg bags and MT, with Arabica/Robusta split)
  - usda_supply_demand.csv           (full supply/demand balance by country: production, consumption, trade, stocks)

Source: https://apps.fas.usda.gov/psdonline/downloads/psd_coffee_csv.zip
No API key required.

Usage:
    uv run scripts/fetch_usda_coffee.py
"""

import io
import zipfile
from pathlib import Path

import pandas as pd
import requests

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
DOWNLOAD_URL = "https://apps.fas.usda.gov/psdonline/downloads/psd_coffee_csv.zip"
RAW_DIR = Path("data/raw")
OUT_DIR = Path("data/processed")

# Countries relevant to the SIPA VCA course
FOCUS_COUNTRIES = [
    "Brazil",
    "Vietnam",
    "Colombia",
    "Ethiopia",
    "Rwanda",
    "Uganda",
    "Kenya",
    "Honduras",
    "Guatemala",
    "Indonesia",
    "Costa Rica",
    "Peru",
    "India",
    "Tanzania",
    "Mexico",
    "Nicaragua",
    "El Salvador",
]

# Key attributes in the PSD dataset
# Values in the raw data are in 1000s of 60-kg bags (for production, consumption,
# exports, imports, stocks) or in 1000s of hectares (for area harvested).
PRODUCTION_ATTRS = [
    "Production",
    "Arabica Production",
    "Robusta Production",
]
SUPPLY_DEMAND_ATTRS = [
    "Production",
    "Arabica Production",
    "Robusta Production",
    "Other Production",
    "Beginning Stocks",
    "Domestic Consumption",
    "Exports",
    "Imports",
    "Ending Stocks",
    "Bean Exports",
    "Bean Imports",
    "Roast & Ground Exports",
    "Roast & Ground Imports",
    "Rst,Ground Dom. Consum",
    "Soluble Dom. Cons.",
    "Soluble Exports",
    "Soluble Imports",
    "Total Distribution",
    "Total Supply",
]
KG_PER_BAG = 60


# ---------------------------------------------------------------------------
# Download
# ---------------------------------------------------------------------------
def download_psd_coffee() -> pd.DataFrame:
    """Download and extract the USDA PSD coffee CSV from the bulk ZIP file."""
    print(f"Downloading {DOWNLOAD_URL} ...")
    resp = requests.get(DOWNLOAD_URL, timeout=60)
    resp.raise_for_status()

    zf = zipfile.ZipFile(io.BytesIO(resp.content))
    csv_files = [m for m in zf.namelist() if m.lower().endswith(".csv")]
    if not csv_files:
        raise RuntimeError("No CSV found in ZIP archive")

    csv_name = csv_files[0]
    print(f"  Extracting {csv_name} ({len(zf.read(csv_name)):,} bytes)")

    with zf.open(csv_name) as f:
        df = pd.read_csv(f)

    # Save raw copy
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(RAW_DIR / "usda_psd_coffee.csv", index=False)
    print(f"  Saved raw data: {len(df):,} rows, {df['Country_Name'].nunique()} countries")
    return df


# ---------------------------------------------------------------------------
# Process: Production by country
# ---------------------------------------------------------------------------
def make_production(df: pd.DataFrame) -> pd.DataFrame:
    """Annual coffee production by country (total, Arabica, Robusta)."""
    prod = df[df["Attribute_Description"].isin(PRODUCTION_ATTRS)].copy()
    prod = prod[prod["Country_Name"].isin(FOCUS_COUNTRIES)]

    # Pivot: one row per country-year, columns for each production type
    pivot = prod.pivot_table(
        index=["Country_Name", "Market_Year"],
        columns="Attribute_Description",
        values="Value",
        aggfunc="first",
    ).reset_index()

    pivot.columns.name = None
    pivot = pivot.rename(columns={
        "Country_Name": "country",
        "Market_Year": "year",
        "Production": "production_1000_bags",
        "Arabica Production": "arabica_1000_bags",
        "Robusta Production": "robusta_1000_bags",
    })

    # Convert from 1000s of 60-kg bags to metric tons
    for col in ["production_1000_bags", "arabica_1000_bags", "robusta_1000_bags"]:
        if col in pivot.columns:
            mt_col = col.replace("_1000_bags", "_mt")
            pivot[mt_col] = pivot[col] * 1000 * KG_PER_BAG / 1000  # 1000 bags * 60 kg / 1000 = MT

    pivot = pivot.sort_values(["country", "year"])
    return pivot


# ---------------------------------------------------------------------------
# Process: Full supply-demand balance
# ---------------------------------------------------------------------------
def make_supply_demand(df: pd.DataFrame) -> pd.DataFrame:
    """Full supply-demand balance by country and year."""
    sd = df[df["Attribute_Description"].isin(SUPPLY_DEMAND_ATTRS)].copy()
    sd = sd[sd["Country_Name"].isin(FOCUS_COUNTRIES)]

    pivot = sd.pivot_table(
        index=["Country_Name", "Market_Year"],
        columns="Attribute_Description",
        values="Value",
        aggfunc="first",
    ).reset_index()

    pivot.columns.name = None
    pivot = pivot.rename(columns={"Country_Name": "country", "Market_Year": "year"})

    # Clean column names: lowercase, underscores
    pivot.columns = [
        c.lower().replace(" ", "_").replace(".", "").rstrip("_")
        if c not in ("country", "year") else c
        for c in pivot.columns
    ]

    # All value columns are in 1000s — scale to actual units
    value_cols = [c for c in pivot.columns if c not in ("country", "year")]
    for col in value_cols:
        pivot[col] = pivot[col] * 1000  # now in 60-kg bags (or hectares for area)

    pivot = pivot.sort_values(["country", "year"])
    return pivot


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    df = download_psd_coffee()

    print("\nProcessing production data...")
    df_prod = make_production(df)
    df_prod.to_csv(OUT_DIR / "usda_production_by_country.csv", index=False)
    print(f"  Saved usda_production_by_country.csv ({len(df_prod)} rows)")

    # Show latest production snapshot
    latest_year = df_prod["year"].max()
    top = (
        df_prod[df_prod["year"] == latest_year]
        .sort_values("production_1000_bags", ascending=False)
        .head(10)
    )
    print(f"\n  Top producers ({latest_year}):")
    for _, r in top.iterrows():
        bags = r.get("production_1000_bags", 0) or 0
        print(f"    {r['country']:15s} {bags:>10,.0f} thousand 60-kg bags")

    print("\nProcessing supply-demand balance...")
    df_sd = make_supply_demand(df)
    df_sd.to_csv(OUT_DIR / "usda_supply_demand.csv", index=False)
    print(f"  Saved usda_supply_demand.csv ({len(df_sd)} rows)")

    print("\nDone.")
    print("\nNote: The PSD bulk download does not include Area Harvested data.")
    print("Yield benchmarks are in data/processed/coffee_yields_benchmark.csv (from lecture slides).")


if __name__ == "__main__":
    main()
