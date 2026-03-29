# Scripts

Reusable Python scripts for fetching and processing coffee industry data. All scripts output clean CSVs to `data/processed/`.

## Usage

```bash
# Install dependencies (first time)
uv sync

# Fetch USDA production and supply-demand data
uv run python scripts/fetch_usda_coffee.py

# Fetch market prices, trade data, exchange rates, and development indicators
uv run python scripts/fetch_market_data.py
```

No API keys are required. All data sources are public.

## Scripts

### `fetch_usda_coffee.py`

Downloads the USDA PSD (Production, Supply, and Distribution) bulk CSV for coffee and produces:

- `usda_production_by_country.csv` — Annual production (1960-2025) with Arabica/Robusta split for 17 countries
- `usda_supply_demand.csv` — Full supply-demand balance: production, consumption, exports, imports, stocks

Source: [USDA FAS PSD Online](https://apps.fas.usda.gov/psdonline/) bulk download (no key needed).

### `fetch_market_data.py`

Fetches data from multiple public APIs and produces:

| Output | Source |
|--------|--------|
| `coffee_prices_monthly.csv` | FRED (IMF commodity prices) |
| `arabica_futures_daily.csv` | Yahoo Finance (`KC=F`) |
| `coffee_exports_by_country.csv` | UN COMTRADE (HS 0901) |
| `exchange_rates_annual.csv` | World Bank API |
| `brl_usd_daily.csv` | FRED |
| `development_indicators.csv` | World Bank API |

Note: The COMTRADE fetch queries 12 countries x 24 years individually (to avoid the 500-row cap on the public preview API), so it takes several minutes to run.

## Dependencies

Managed via `pyproject.toml` at the project root:

- `pandas` — Data processing
- `requests` — HTTP downloads
- `yfinance` — Yahoo Finance futures data
