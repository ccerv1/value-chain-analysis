# For Agents

You can use an AI assistant (Claude, ChatGPT, or similar) to conduct your own value chain analysis for a different commodity or country. This page has two sections: a starter prompt for working with an AI interactively, and a structured agent reference that gives an AI the exact steps, data sources, and output formats it needs.

## Starter Prompt

Copy and paste this to get started. Replace `[commodity]` and `[country]` with your own.

```text
I am conducting a value chain analysis of [commodity] in [country] using the Map / Breakdown / Benchmark framework.

Read the agent reference at: https://ccerv1.github.io/value-chain-analysis/lecture-notes/using-ai/#agent-reference

Data files are at: https://github.com/ccerv1/value-chain-analysis/tree/main/data/processed

Help me work through these steps:

1. Map the value chain: identify key actors from production to export, the flow of the product through each stage, and any parallel channels.
2. Break down the value flows: trace the price from the farmer/producer to the export or retail level, converting units and currency as needed.
3. Benchmark against peer countries or commodities: compare yields, prices, farmer share, and costs.
4. Recommend interventions using an impact-feasibility matrix.

Start by asking me what I already know about the [commodity] value chain in [country], then help me fill in the gaps with publicly available data.
```

**Tips for working with AI.** Give it real data, not just questions. Check the conversion math yourself. Push back on generic recommendations ("improve market access") by asking for specifics: which markets, what mechanism, what cost, funded by whom. The coffee-specific features (cherry-to-green ratio, ICE "C" benchmark, Arabica/Robusta split) don't transfer directly to other commodities. Ask the AI to help you find the analogous features for your commodity.

---

## Agent Reference

The sections below are structured for an AI agent to consume directly. Each step specifies inputs, outputs, method, and data sources.

### Step 1: Map

**Input:** Country name, commodity (default: coffee)

**Output:** A table of actors with columns: Stage, Actor Type, Estimated Count, Function, and a description of 1-2 parallel channels.

**Method:**

1. Identify the main stages: Input Supply, Production, Processing, Aggregation/Trade, Export
2. For each stage, list the actor types. For coffee, the standard categories are:
    - Smallholder farmer (<5 ha), estate/plantation (>50 ha)
    - Mobile collector/middleman, cooperative
    - Coffee washing station (wet mill), dry mill
    - Exporter, importer, roaster, retailer
3. Estimate the number of actors at each stage using USDA production data and country profiles
4. Identify at least two parallel channels (eg, washed vs natural, cooperative vs private, export vs domestic)

**Data sources:**

- `data/processed/usda_production_by_country.csv` for production volumes
- `data/processed/coffee_country_profiles.csv` for farmer counts, farm sizes, species
- `data/processed/country_lookup.csv` for country code mapping

### Step 2: Breakdown

**Input:** Farm-gate price (in local currency per kg cherry), export price (USD/kg green), exchange rate, cherry-to-green conversion ratio

**Output:** A conversion table (local currency → USD → green equivalent → farmer share %) and a waterfall table showing where value goes between farmer and export.

**Method:**

1. Convert farm-gate price to USD:
    - `price_usd = price_local / exchange_rate`
2. Convert cherry price to green equivalent:
    - `price_green = price_usd * cherry_to_green_ratio`
    - Arabica ratio: 6:1 to 7:1 (depends on altitude/varietal; Ethiopia ~6:1, Rwanda ~7:1)
    - Robusta ratio: ~5:1
3. Calculate farmer share:
    - `farmer_share = price_green / export_price_usd`
4. Build waterfall: farmer → processing costs → transport → taxes/fees → exporter margin → FOB export price

**Data sources:**

- `data/processed/exchange_rates_annual.csv` for exchange rates
- `data/processed/coffee_conversion_factors.csv` for cherry-to-green ratios
- `data/processed/supply_chain_breakdowns.csv` for Vietnam and Rwanda waterfall reference data
- `data/processed/coffee_prices_monthly.csv` for Arabica/Robusta benchmark prices
- For current farm-gate prices: check Sucafina or Trabocca harvest reports

**Validation:** Farmer share should be between 40-95% of export price. If it's above 100%, the conversion is wrong. If it's below 30%, double-check the exchange rate and cherry-to-green ratio.

### Step 3: Benchmark

**Input:** Country name, production/export/yield/price data from Steps 1-2

**Output:** A comparison table with 3-5 peer countries across: production volume, yield (MT/ha), export price ($/kg), farmer share (%), and a supply curve position.

**Method:**

1. Select 3-5 peer countries based on:
    - Same species (Arabica vs Robusta)
    - Similar region or farm structure
    - Include at least one "best in class" comparator (Vietnam for efficiency, Colombia for institutions, Rwanda for quality)
2. Pull data for each peer:
    - Production: `usda_production_by_country.csv`
    - Export volume and price: `coffee_exports_by_country.csv` or `supply_curve_complete.csv`
    - Yields: `coffee_yields_benchmark.csv`
3. Calculate the target country's position on the supply curve relative to peers
4. Flag metrics where the target country is notably above or below peers

**Data sources:**

- `data/processed/usda_production_by_country.csv` for production volumes (1960-2025, 17 countries)
- `data/processed/supply_curve_complete.csv` for price and market share (25 countries, 2019-2023)
- `data/processed/coffee_yields_benchmark.csv` for yield benchmarks
- `data/processed/development_indicators.csv` for GDP, agriculture share, population context

### Step 4: Recommend

**Input:** Findings from Steps 1-3, country context

**Output:** A 2x2 impact-feasibility matrix with 4-6 candidate interventions, each placed in a quadrant with justification.

**Method:**

1. Generate candidate interventions from the diagnosis:
    - If farmer share is low: improve market competition, strengthen cooperatives, reduce intermediary margins
    - If yields are low: tree renovation, extension services, input access
    - If prices are below benchmark: quality improvement, certification, traceability
    - If environmental footprint is high: shade management, water efficiency, diversification
2. Score each intervention on two dimensions:
    - **Impact** (High/Medium/Low): how much would this change farmer income, productivity, or sustainability?
    - **Feasibility** (High/Medium/Low): can this be implemented within 3-5 years given existing institutions, funding, and political constraints?
3. Place on the matrix:
    - High impact + High feasibility → top priority
    - High impact + Low feasibility → long-term investment
    - Low impact + High feasibility → quick win (do if resources allow)
    - Low impact + Low feasibility → skip
4. For each recommendation: state who benefits, who pays, and what the mechanism is

**Validation:** Every recommendation must name a specific actor segment (not "farmers" generically), a specific mechanism, and a funding source. "Improve farmer productivity" is not a recommendation. "Fund IHCAFE extension agents to train 20,000 smallholders in the western highlands on rust-resistant varieties, funded by a $2M USAID grant" is a recommendation.

### Step 5: Generate Charts

**Input:** Data from Steps 1-4

**Output:** Four charts in the course's visual style (black/white, no gridlines, clean axes)

**Method:**

Charts to generate using matplotlib:

1. **Production trend** (bar chart): country production 1990-2025 from `usda_production_by_country.csv`
2. **Supply curve position** (stacked bar): country highlighted on the global supply curve from `supply_curve_complete.csv`
3. **Supply-demand balance** (line chart): production, exports, domestic consumption from `usda_supply_demand.csv`
4. **Export price vs benchmark** (line + area): country export price vs Arabica/Robusta benchmark from `coffee_prices_monthly.csv` and `supply_curve_complete.csv`

**Chart style:**

```python
plt.rcParams.update({
    "axes.grid": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.edgecolor": "#333",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "figure.dpi": 150,
})
BLACK, GRAY, LIGHT = "#000000", "#999999", "#dddddd"
```

**Data sources:**

- All CSV files in `data/processed/`
- Scripts for regenerating data: `scripts/fetch_usda_coffee.py`, `scripts/fetch_market_data.py`

---

## Data Access

All datasets are in the GitHub repository: [github.com/ccerv1/value-chain-analysis](https://github.com/ccerv1/value-chain-analysis/tree/main/data/processed)

To download any CSV directly, use:
```
https://github.com/ccerv1/value-chain-analysis/raw/main/data/processed/FILENAME.csv
```

To regenerate all data from source:
```bash
uv sync
uv run python scripts/fetch_usda_coffee.py
uv run python scripts/fetch_market_data.py
```

---

## Coffee Reference Data

Reference material for agents working on coffee value chains specifically.

### Actor Categories

- **Smallholder farmer**: <5 hectares, family labor, diversified crops, sells cherry
- **Estate/plantation**: >50 hectares, hired labor, may process on-site
- **Mobile collector/middleman**: Buys cherry from farmers, aggregates, sells to mill or exporter
- **Coffee washing station (wet mill)**: De-pulps, ferments, washes, dries cherry into parchment
- **Dry mill**: Hulls parchment to green, grades, bags for export
- **Cooperative**: Farmer-owned organization that may operate washing stations, aggregate volume, and export directly
- **Exporter**: Consolidates green coffee, arranges shipping, manages export documentation
- **Trader/importer**: International buyers who purchase FOB and sell to roasters
- **Roaster**: Blends and roasts green coffee for consumer market
- **Retailer**: Sells roasted/ground coffee or brewed coffee to consumers

### Price Benchmarks

- **ICE "C" contract** (New York): Global Arabica benchmark, quoted in US cents per pound. Physical coffee trades at a differential to this price. Watch the units: 310.00 means $3.10/lb, not $310/lb.
- **ICE London**: Global Robusta benchmark, quoted in USD per metric ton.
- **Country differentials**: Colombia typically trades at C + $0.15-0.30 (premium). Ethiopia at C + $0.20-0.50 (premium, varies by grade). Vietnam Robusta trades relative to London. Brazil trades near or slightly below C.

### Quality Grading

- **SCA cupping score**: Scored out of 100. Coffee scoring 80+ is specialty grade.
- **Specialty threshold**: 80 points. Below 80 is commercial. Above 85 is excellent. Above 90 is exceptional and very rare.
- **Quality premiums**: Specialty coffee commands $0.50-2.00+ per pound above the C price. This premium is the economic engine behind quality-focused interventions.
