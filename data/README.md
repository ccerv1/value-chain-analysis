# Data Pack — SIPA Value Chain Analysis

Datasets for the Value Chain Analysis course at Columbia SIPA. All data can be regenerated from public sources using the scripts in `scripts/`.

## Quick Start

```bash
# Install dependencies (first time)
uv sync

# Regenerate all data
uv run python scripts/fetch_usda_coffee.py     # USDA production & supply-demand
uv run python scripts/fetch_market_data.py      # prices, trade, exchange rates, indicators
```

No API keys are required. All sources are public.

---

## Processed Datasets (`processed/`)

Analysis-ready CSVs. These are the files you should use.

### USDA Production & Supply-Demand

Source: [USDA PSD](https://apps.fas.usda.gov/psdonline/) bulk CSV download. No API key needed. Values are in 60-kg bags (the standard unit for coffee trade statistics).

**[`usda_production_by_country.csv`](https://github.com/ccerv1/value-chain-analysis/raw/main/data/processed/usda_production_by_country.csv)** — Annual coffee production with Arabica/Robusta split

| Column | Type | Description |
|--------|------|-------------|
| `country` | str | Country name (matches `usda_name` in `country_lookup.csv`) |
| `year` | int | Market year (coffee crop year, not calendar year) |
| `production_1000_bags` | float | Total production in thousands of 60-kg bags |
| `arabica_1000_bags` | float | Arabica production in thousands of 60-kg bags |
| `robusta_1000_bags` | float | Robusta production (0 for Arabica-only countries) |
| `production_mt` | float | Total production in metric tons |
| `arabica_mt` | float | Arabica production in metric tons |
| `robusta_mt` | float | Robusta production in metric tons |

Coverage: 17 countries, 1960-2025 (1,122 rows). Use this for production trends, Arabica/Robusta shares, and country comparisons.

**[`usda_supply_demand.csv`](https://github.com/ccerv1/value-chain-analysis/raw/main/data/processed/usda_supply_demand.csv)** — Full supply-demand balance

| Column | Type | Description |
|--------|------|-------------|
| `country` | str | Country name |
| `year` | int | Market year |
| `production` | float | Total production (60-kg bags) |
| `arabica_production` | float | Arabica production (60-kg bags) |
| `robusta_production` | float | Robusta production (60-kg bags) |
| `domestic_consumption` | float | Domestic consumption (60-kg bags) |
| `exports` | float | Total exports (60-kg bags) |
| `imports` | float | Total imports (60-kg bags) |
| `beginning_stocks` | float | Beginning stocks (60-kg bags) |
| `ending_stocks` | float | Ending stocks (60-kg bags) |
| `bean_exports` | float | Green bean exports |
| `bean_imports` | float | Green bean imports |
| `roast_and_ground_exports` | float | Roasted coffee exports |
| `roast_and_ground_imports` | float | Roasted coffee imports |
| `rstground_dom_consum` | float | Roast & ground domestic consumption |
| `soluble_dom_cons` | float | Instant/soluble domestic consumption |
| `soluble_exports` | float | Instant/soluble exports |
| `soluble_imports` | float | Instant/soluble imports |
| `total_supply` | float | Total supply (production + imports + stocks) |
| `total_distribution` | float | Total distribution (consumption + exports + stocks) |

Coverage: 17 countries, 1960-2025 (1,122 rows). All values in 60-kg bags. Use this for consumption analysis, trade balances, and stock-to-use ratios.

---

### Market Prices

**[`coffee_prices_monthly.csv`](https://github.com/ccerv1/value-chain-analysis/raw/main/data/processed/coffee_prices_monthly.csv)** — Monthly Arabica and Robusta prices

Source: [FRED](https://fred.stlouisfed.org/) (IMF/World Bank commodity price series)

| Column | Type | Description |
|--------|------|-------------|
| `date` | str | First of month (YYYY-MM-DD) |
| `arabica_cents_per_lb` | float | ICO Other Mild Arabicas indicator, US cents/lb |
| `robusta_cents_per_lb` | float | ICO Robusta indicator, US cents/lb |
| `arabica_usd_per_kg` | float | Arabica converted to USD/kg |
| `robusta_usd_per_kg` | float | Robusta converted to USD/kg |
| `year` | int | Year |
| `month` | int | Month |

Coverage: 1992-2026 (410 rows). These are monthly averages of ICO indicator prices, not futures prices. Good for long-run trend analysis and the coffee crisis narrative.

**[`arabica_futures_daily.csv`](https://github.com/ccerv1/value-chain-analysis/raw/main/data/processed/arabica_futures_daily.csv)** — Daily ICE "C" Arabica futures

Source: [Yahoo Finance](https://finance.yahoo.com/) via `yfinance` (ticker `KC=F`)

| Column | Type | Description |
|--------|------|-------------|
| `date` | str | Trading date (YYYY-MM-DD) |
| `open` | float | Opening price, US cents/lb |
| `high` | float | Day high, US cents/lb |
| `low` | float | Day low, US cents/lb |
| `close` | float | Closing price, US cents/lb |
| `volume` | int | Trading volume (contracts) |
| `close_usd_per_kg` | float | Closing price converted to USD/kg |

Coverage: 2000-2026 (6,577 rows). Daily front-month futures. Use for price volatility analysis and the $4/kilo framing. Volume is 0 on some days (holidays, data gaps).

---

### Trade Data

**[`coffee_exports_by_country.csv`](https://github.com/ccerv1/value-chain-analysis/raw/main/data/processed/coffee_exports_by_country.csv)** — Annual coffee exports by producing country

Source: [UN COMTRADE](https://comtradeapi.un.org/) public preview API (HS code 0901, exports to World)

| Column | Type | Description |
|--------|------|-------------|
| `year` | int | Calendar year |
| `country_code` | int | UN numeric country code (join to `comtrade_code` in lookup) |
| `country` | str | Country name |
| `export_volume_mt` | float | Export volume in metric tons (may be null for some country-years) |
| `export_value_million_usd` | float | Export value in millions of USD |
| `avg_price_usd_per_kg` | float | Implied average price (value / volume; null if volume missing) |

Coverage: 12 countries, 2000-2023 (249 rows). Use for market share analysis, price positioning comparisons, and export trend charts. Note: COMTRADE aggregates all coffee sub-codes under HS 0901 (green, roasted, instant), so volumes include some processed coffee.

Data quality notes:
- Rwanda 2015 dropped (volume anomaly: 35 MT vs typical ~15,000 MT)
- Ethiopia 2020 and Indonesia 2017 have null volumes (weight data missing from source)

---

### Exchange Rates

**[`exchange_rates_annual.csv`](https://github.com/ccerv1/value-chain-analysis/raw/main/data/processed/exchange_rates_annual.csv)** — Annual official exchange rates

Source: [World Bank](https://api.worldbank.org/) indicator `PA.NUS.FCRF`

| Column | Type | Description |
|--------|------|-------------|
| `country_code` | str | ISO3 country code (join to `wb_code` in lookup) |
| `country` | str | World Bank display name (e.g., "Viet Nam" not "Vietnam") |
| `year` | int | Calendar year |
| `exchange_rate_lcu_per_usd` | float | Local currency units per 1 USD, period average |

Coverage: 11 countries, 1990-2024 (385 rows). Use for converting farmer prices from local currency to USD (the unit conversion skill). Some early years may be null for countries that didn't report.

**[`brl_usd_daily.csv`](https://github.com/ccerv1/value-chain-analysis/raw/main/data/processed/brl_usd_daily.csv)** — Daily BRL/USD exchange rate

Source: [FRED](https://fred.stlouisfed.org/) series `DEXBZUS`

| Column | Type | Description |
|--------|------|-------------|
| `date` | str | Date (YYYY-MM-DD) |
| `brl_per_usd` | float | Brazilian Real per 1 USD |

Coverage: 1995-2026 (7,828 rows). Weekends and holidays are excluded. Useful for Brazil-specific analysis where annual averages are too coarse.

---

### Development Indicators

**[`development_indicators.csv`](https://github.com/ccerv1/value-chain-analysis/raw/main/data/processed/development_indicators.csv)** — Country-level context data

Source: [World Bank](https://api.worldbank.org/)

| Column | Type | Description |
|--------|------|-------------|
| `country_code` | str | ISO3 country code |
| `country` | str | World Bank display name |
| `year` | int | Calendar year |
| `agriculture_pct_gdp` | float | Agriculture, forestry, fishing as % of GDP |
| `arable_land_pct` | float | Arable land as % of total land area (some nulls) |
| `gdp_per_capita_usd` | float | GDP per capita in current USD |
| `population` | float | Total population |
| `rural_population_pct` | float | Rural population as % of total |

Coverage: 11 countries, 2000-2024 (275 rows). Provides context for value chain analysis: how important is agriculture to the economy, how rural is the population, what is the income level?

---

### Reference Data

Small hand-curated datasets from lecture content. These capture the key numbers used in slides and case studies.

**[`coffee_yields_benchmark.csv`](https://github.com/ccerv1/value-chain-analysis/raw/main/data/processed/coffee_yields_benchmark.csv)** — The benchmark yield chart from the slides

| Column | Type | Description |
|--------|------|-------------|
| `country` | str | Country (some entries split by species, e.g., "Brazil (Robusta)") |
| `species` | str | Arabica, Robusta, or Mixed |
| `avg_yield_mt_per_ha` | float | Average yield in metric tons green per hectare |
| `source` | str | Data source citation |
| `notes` | str | Additional context (may be blank) |

10 rows. Use for the benchmark comparison chart. Note: the USDA PSD bulk download does not include area harvested, so these yield figures come from USDA attaché reports and TechnoServe analysis as cited in the slides.

**[`supply_chain_breakdowns.csv`](https://github.com/ccerv1/value-chain-analysis/raw/main/data/processed/supply_chain_breakdowns.csv)** — Vietnam and Rwanda waterfall numbers

| Column | Type | Description |
|--------|------|-------------|
| `country` | str | Vietnam or Rwanda |
| `species` | str | Robusta or Arabica |
| `export_price_usd_per_kg_green` | float | FOB export price |
| `farmer_share_pct` | int | Farmer's share of export price (%) |
| `farmer_price_usd_per_kg_green` | float | What the farmer receives in green-equivalent USD |
| `supply_chain_cost_pct` | int | Supply chain's share (100 - farmer share) |
| `price_date` | str | When these prices were observed |
| `source` | str | Data source |

2 rows. The core data for the waterfall chart comparison between an efficient chain (Vietnam, 95%) and a processing-intensive chain (Rwanda, 54%).

**[`coffee_country_profiles.csv`](https://github.com/ccerv1/value-chain-analysis/raw/main/data/processed/coffee_country_profiles.csv)** — Key stats per country

| Column | Type | Description |
|--------|------|-------------|
| `country` | str | Country name |
| `num_farmers` | float | Estimated number of coffee farmers (null if unknown) |
| `avg_farm_size_ha` | float | Average farm size in hectares |
| `pct_world_supply` | float | Approximate share of global coffee supply |
| `main_species` | str | Arabica, Robusta, or Mixed |
| `farmer_share_pct` | float | Farmer's share of export price (null if not analyzed) |
| `export_channel` | str | Primary export channel description |
| `domestic_consumption_pct` | int | Estimated % of production consumed domestically |

5 rows (the countries covered in the case studies). A quick reference for the numbers that anchor each case study.

**[`coffee_conversion_factors.csv`](https://github.com/ccerv1/value-chain-analysis/raw/main/data/processed/coffee_conversion_factors.csv)** — Standard conversion factors for coffee

| Column | Type | Description |
|--------|------|-------------|
| `conversion` | str | What is being converted |
| `ratio` | str | Range (text, e.g., "6:1 to 7:1") |
| `typical` | float | Typical value to use in calculations |
| `unit` | str | Units of the ratio |
| `notes` | str | When to adjust |

6 rows. Reference for unit conversion exercises (Skill 3).

---

### Country Lookup Table

**[`country_lookup.csv`](https://github.com/ccerv1/value-chain-analysis/raw/main/data/processed/country_lookup.csv)** — Master lookup for joining data across sources

| Column | Type | Description |
|--------|------|-------------|
| `display_name` | str | Canonical display name (use this in all outputs) |
| `iso2` | str | ISO 3166-1 alpha-2 code |
| `iso3` | str | ISO 3166-1 alpha-3 code |
| `usda_code` | str | USDA FAS country code (e.g., "VM" for Vietnam) |
| `usda_name` | str | Name as it appears in USDA data |
| `comtrade_code` | str | UN numeric code for COMTRADE queries (blank if not in our pull) |
| `wb_code` | str | World Bank ISO3 code (blank if not in our pull) |
| `wb_name` | str | Name as it appears in World Bank data (e.g., "Viet Nam") |
| `currency_code` | str | ISO 4217 currency code |
| `currency_name` | str | Currency name |
| `region` | str | Geographic grouping |
| `main_species` | str | Arabica, Robusta, or Mixed |

18 rows. Use this to join datasets. Example:

```python
import pandas as pd

lookup = pd.read_csv("data/processed/country_lookup.csv", dtype={"comtrade_code": str})
usda = pd.read_csv("data/processed/usda_production_by_country.csv")
exports = pd.read_csv("data/processed/coffee_exports_by_country.csv", dtype={"country_code": str})

# Join USDA to lookup
usda = usda.merge(lookup[["display_name", "usda_name", "region"]],
                   left_on="country", right_on="usda_name", how="left")

# Join COMTRADE to lookup
exports = exports.merge(lookup[["display_name", "comtrade_code"]],
                         left_on="country_code", right_on="comtrade_code", how="left")
```

---

## Raw Data (`raw/`)

Original downloads before processing. Kept for reproducibility and debugging. You should not need to use these directly.

| File | Source | Size |
|------|--------|------|
| `usda_psd_coffee.csv` | USDA PSD bulk download (all 94 countries, all attributes) | ~8 MB |
| `comtrade_coffee_exports.csv` | COMTRADE bilateral trade data (pre-aggregation) | ~400 KB |
| `arabica_prices.csv` | FRED series PCOFFOTMUSDM | 12 KB |
| `robusta_prices.csv` | FRED series PCOFFROBUSDM | 12 KB |
| `brl_usd.csv` | FRED series DEXBZUS | 145 KB |
| `wb_exchange_rates.csv` | World Bank API PA.NUS.FCRF | 12 KB |
| `wb_development_indicators.csv` | World Bank API (5 indicators) | 26 KB |
| `yf_arabica_futures.csv` | Yahoo Finance KC=F | 535 KB |

---

## Data Sources

| Source | What We Get | Access | URL |
|--------|-------------|--------|-----|
| USDA PSD | Production, supply-demand balance (17 countries, 1960-2025) | Bulk CSV, no key | apps.fas.usda.gov/psdonline/ |
| FRED | Monthly coffee prices, daily BRL/USD | Direct CSV, no key | fred.stlouisfed.org |
| Yahoo Finance | Daily Arabica futures | `yfinance` library, no key | finance.yahoo.com |
| UN COMTRADE | Annual coffee exports (12 countries, 2000-2023) | Public API, no key | comtradeapi.un.org |
| World Bank | Exchange rates, development indicators (11 countries) | REST API, no key | api.worldbank.org |

## Not Included

- **USDA Area Harvested / Yield** — not in the PSD bulk download. Yield benchmarks from the lecture slides are in `coffee_yields_benchmark.csv`.
- **ICO indicator prices** — requires ICO membership or academic request to stats@ico.org. A [Kaggle mirror](https://www.kaggle.com/datasets/yamaerenay/ico-coffee-dataset-worldwide) has data through ~2021.
- **Robusta futures (daily)** — the Yahoo Finance ticker `RC=F` is no longer available. Monthly Robusta prices from FRED are included in `coffee_prices_monthly.csv`.

---

*Data last generated: 2026-03-29*
