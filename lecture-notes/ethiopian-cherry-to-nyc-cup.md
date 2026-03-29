# From Ethiopian Cherry to NYC Cup

*How $5.71 becomes $288 — the coffee value chain in one worked example*

![Ethiopian farmer among coffee trees](../photos/ethiopian-farmer-coffee-trees.jpg)

---

## The Question

An Ethiopian farmer picks coffee cherry from her trees and sells it to a collector. That cherry is processed, exported, roasted, and brewed into a pour-over at a specialty cafe in Brooklyn. How much does she receive, and how much does the customer pay?

This page walks through the math step by step, with sources and assumptions documented so you can replicate or update it.

---

## Step 1: What the Farmer Receives

### Cherry price at the farm gate

The starting point is the price a farmer receives for raw coffee cherry — the red fruit picked from the tree.

In the 2025/26 Ethiopian harvest season, cherry prices at the collector/ECX level reached approximately **145 ETB/kg** ([Sucafina Ethiopia 2025/26 Harvest Update](https://sucafina.com/emea/news/ethiopia-2025-26-harvest-update)). This is a sharp increase from 35-40 ETB/kg in the prior season, driven by the birr devaluation and surging global prices.

The farmer does not receive the full collector price. Collectors add transport, aggregation, and their own margin. A reasonable estimate is that the farmer receives roughly **80% of the collector price**:

> 145 ETB/kg x 0.80 = **116 ETB/kg cherry**

| Variable | Value | Source |
|----------|-------|--------|
| ECX/collector cherry price | 145 ETB/kg | Sucafina 2025/26 harvest report |
| Farmer share of collector price | ~80% | Course estimate (Ethiopian farmers typically receive 60-80% of ECX price; 80% reflects current tight supply) |
| **Farmer cherry price** | **116 ETB/kg** | Calculated |

### Convert to USD

Ethiopia floated the birr in July 2024. The exchange rate moved from ~55 ETB/USD to over 120 ETB/USD within months.

> 116 ETB/kg ÷ 127 ETB/USD = **$0.91/kg cherry**

| Variable | Value | Source |
|----------|-------|--------|
| Exchange rate | ~127 ETB/USD | Post-float rate, early 2026. World Bank annual data shows 82.60 for 2024 (annual average, includes pre-float months). |
| **Farmer cherry price in USD** | **$0.91/kg** | Calculated |

### Convert cherry to green equivalent

The farmer sells cherry, but international coffee is traded as green (the processed, export-ready bean). To compare the farmer's price to the export price, we need to convert using the cherry-to-green ratio.

For Ethiopian Arabica, the ratio is approximately **6.25:1** — it takes 6.25 kg of cherry to produce 1 kg of green coffee. This ratio is driven by species, varietal, and agro-climatic conditions (including altitude), not by the processing method.

> $0.91/kg cherry x 6.25 = **$5.71/kg green equivalent**

| Variable | Value | Source |
|----------|-------|--------|
| Cherry-to-green ratio (Ethiopian Arabica) | 6.25:1 | Course reference. Ranges from 6:1 to 7:1 for Arabica depending on altitude and varietal. Ethiopia is mid-range. Rwanda is ~7:1 (higher altitude). |
| **Farmer price in green equivalent** | **$5.71/kg green** | Calculated |

> **What this means:** The farmer receives $5.71 worth of cherry for every kilogram of green coffee that will eventually be exported. This is the number we can compare to the export price.

---

## Step 2: The Export Price

Ethiopian washed Arabica is a premium origin. The FOB (Free On Board) export price — what the buyer pays at the port — reflects the global Arabica benchmark (ICE "C" futures) plus Ethiopia's quality differential.

In early 2026, with the ICE "C" above 300 cents/lb ($6.61/kg) and Ethiopian washed commanding a positive differential, the FOB price is approximately **$8.00/kg green**.

> Farmer share = $5.71 / $8.00 = **71%**

| Variable | Value | Source |
|----------|-------|--------|
| ICE "C" Arabica futures | ~310 cents/lb (~$6.83/kg) | FRED/Yahoo Finance, March 2026 |
| Ethiopian differential | +$0.50 to +$1.50/lb | Typical for washed Ethiopian; varies by grade and lot |
| **Estimated FOB export price** | **~$8.00/kg green** | Estimated from C + differential |
| **Farmer share of export price** | **71%** | Calculated |

> **Context:** A 71% farmer share is higher than Ethiopia's historical average (~65%) but consistent with the current tight supply environment. For comparison: Vietnam ~95%, Colombia ~80%, Rwanda ~54%.

---

## Step 3: What Happens Between Export and Cup

The green coffee travels from Addis Ababa to a roaster in the US through several stages, each adding cost:

### Shipping and import

> $8.00 + $1.00 = **$9.00/kg landed cost**

The $1.00 covers ocean freight, insurance, import duties, and handling. This is approximate — actual costs vary by contract terms and volume.

### Roasting

Roasting causes a ~16% weight loss (moisture evaporates). The raw material cost per kilogram of roasted coffee is:

> $9.00 ÷ 0.84 = **$10.71/kg roasted** (raw material only)

Add roasting labor, energy, equipment depreciation, packaging, and overhead — roughly $4/kg for a specialty roaster:

> $10.71 + $4.00 = **$14.71/kg roasted**

For reference, Sey Coffee in Brooklyn sells 250g bags at $25 ($100/kg retail). Blue Bottle sells at similar prices. The roaster's margin on bags is substantial — but bags are not where most coffee is consumed.

### Brewing at the cafe

A cafe buys roasted coffee at wholesale (roughly $40-60/kg from a specialty roaster) and brews it into individual cups. Industry standard: **1 kg of green coffee produces approximately 50 cups** of 12oz brewed coffee (accounting for roasting weight loss and the ~17g dose per cup).

The cafe's cost of the coffee itself is small relative to its other costs:

> $14.71 ÷ 50 cups = **$0.29/cup in coffee cost**

The other $5.46 of a $5.75 pour-over pays for the barista, the rent, the equipment, the cups, the water, the electricity, the insurance, and the profit. In Manhattan and Brooklyn, rent and labor alone dominate.

---

## Step 4: What the Customer Pays

![Pour-over brewing with a V60](../photos/pour-over-brewing.jpg)

NYC coffee prices as of March 2026:

| Venue | Drink | Price | Source |
|-------|-------|-------|--------|
| Starbucks | Grande brewed drip (16oz) | $1.95 | [HackTheMenu](https://hackthemenu.com/starbucks/menu-prices/coffee-espresso/) |
| Independent cafe | Drip coffee (12oz) | $4.50-6.00 | Estimated from NYC cafe surveys |
| Blue Bottle | Pour-over (12oz) | $5.75 | [FullMenuPrices](https://fullmenuprices.com/blue-bottle-coffee-menu-with-prices/) |
| Specialty (Sey, Devocion) | Single-origin Ethiopian pour-over | $7-9 | Estimated |

---

## The Full Picture

For a **$5.75 pour-over at Blue Bottle** — 50 cups from 1 kg of green:

| Stage | Amount | % of Retail |
|-------|--------|-------------|
| **Ethiopian farmer** | **$5.71** | **2.0%** |
| Collectors and ECX | $1.43 | 0.5% |
| Export and shipping | $1.86 | 0.6% |
| Roasting and wholesale | $5.71 | 2.0% |
| Cafe (labor, rent, cups, profit) | $272.79 | 94.9% |
| **Customer pays (50 cups x $5.75)** | **$287.50** | **100%** |

### Across different retail formats

| Retail format | Cup price | 50 cups | Farmer's $5.71 as % |
|---------------|-----------|---------|---------------------|
| Starbucks grande drip | $1.95 | $97.50 | 5.9% |
| Independent cafe drip | $5.00 | $250.00 | 2.3% |
| Blue Bottle pour-over | $5.75 | $287.50 | 2.0% |
| Specialty Ethiopian pour-over | $8.00 | $400.00 | 1.4% |

> **The paradox:** The more a cafe charges for single-origin Ethiopian coffee — emphasizing its provenance and the farmer's story — the smaller the farmer's share of the final price becomes. A $8 pour-over returns $0.11 per cup to the farmer. An $8 pour-over that is "premium because it's Ethiopian" does not mean "more money goes to Ethiopia."

---

## Key Assumptions and Sensitivity

Every number in this analysis rests on assumptions. Here is where the uncertainty lives:

| Assumption | Value used | Range | Impact if wrong |
|-----------|-----------|-------|-----------------|
| Farmer share of collector price | 80% | 60-80% | At 60%, farmer receives $4.28/kg green instead of $5.71 |
| Exchange rate (ETB/USD) | 127 | 120-135 | At 135, farmer receives $5.36/kg green |
| Cherry-to-green ratio | 6.25:1 | 6:1 to 7:1 | At 7:1, farmer receives $6.40/kg green |
| FOB export price | $8.00/kg | $7-9/kg | Changes farmer share of export from 63% to 82% |
| Cups per kg green | 50 | 45-55 | Changes retail total proportionally |
| NYC pour-over price | $5.75 | $5-8 | Changes farmer % of retail |

### The claim that is robust

Regardless of which assumptions you adjust, the structural finding holds: **the farmer captures 1-6% of the retail value of a cup of coffee**. This is not primarily a function of exploitation in the supply chain — the Ethiopian farmer receives a reasonable share of the export price (71%). It is a function of the enormous cost of labor and real estate in a consuming-country city.

### The claim that is sensitive

The **farmer share of the export price** (71%) is sensitive to the farmgate discount (80% assumed) and the exchange rate. If the farmer receives only 60% of the collector price at 135 ETB/USD, the share drops to ~53%. If the birr stabilizes and cherry prices in ETB don't keep pace, the share could compress further.

---

## Replicating This Analysis

To update these numbers with current data:

1. **Cherry price:** Check the latest Sucafina or Trabocca harvest reports for ECX cherry prices
2. **Exchange rate:** Use the [World Bank API](https://api.worldbank.org/v2/country/ET/indicator/PA.NUS.FCRF?format=json) or check xe.com for current ETB/USD
3. **Export price:** Check ICE "C" futures at [FRED](https://fred.stlouisfed.org/series/PCOFFOTMUSDM) and add Ethiopia's differential (~$0.50-1.50/lb for washed)
4. **NYC cafe prices:** Check Blue Bottle or Sey Coffee menus (or delivery apps for current pricing)
5. **Run the math:** All conversion factors are in `data/processed/coffee_conversion_factors.csv`

The datasets in this project's [data pack](../data/README.md) provide the historical context for each of these variables.

---

## Discussion Questions

1. The farmer captures 2% of the retail value but 71% of the export price. Which number is more meaningful for understanding the farmer's position? Why?

2. Cafe costs (labor, rent) account for ~95% of the retail price. Does this mean the supply chain is "fair"? What would need to change for the farmer to capture a meaningfully larger share of retail value?

3. The birr devaluation in 2024 increased the farmer's cherry price in ETB (from 35 to 116 ETB/kg) while decreasing its dollar value. Is the Ethiopian farmer better off or worse off after the devaluation? What additional information would you need to answer this?

4. A specialty roaster sells a 250g bag of Ethiopian single-origin for $25 ($100/kg). The green coffee cost them ~$9/kg. Is this markup justified? What does it pay for?

5. If you could redesign one element of this value chain to increase the farmer's absolute income, what would it be — and what are the practical barriers to implementing it?

---

*This analysis uses data from the [course data pack](../data/README.md) and public sources. For the analytical framework, see [Value Chain Analysis: Lecture Notes](value-chain-analysis.md). For conversion factors and methodology, see [Skill 3: Unit Conversion](../skills/03-unit-conversion-and-price-analysis.md).*
