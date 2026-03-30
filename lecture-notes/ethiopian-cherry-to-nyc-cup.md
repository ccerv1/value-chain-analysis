# From Ethiopian Cherry to NYC Cup

*How $5.67 becomes $288 in one worked example*

---

## The Question

An Ethiopian farmer picks coffee cherry from her trees and sells it at the local market. That cherry is processed, exported, roasted, and brewed into a pour-over at a specialty cafe in Morningside Heights. How much does she receive, and how much does the customer pay?

This page walks through the math step by step, with sources and assumptions documented so you can replicate or update it.

---

## Step 1: What the Farmer Receives

### Cherry price at the farm gate

The starting point is the price a farmer receives for raw coffee cherry.

In the 2025/26 Ethiopian harvest season, farm-gate cherry prices averaged approximately **120 ETB/kg** ([Sucafina Ethiopia 2025/26 Harvest Update](https://sucafina.com/emea/news/ethiopia-2025-26-harvest-update)). Prices at peak season reached as high as 145 ETB/kg, but the season average is lower. This is a sharp increase from 35-40 ETB/kg in the prior season, driven by the birr devaluation and surging global prices.

| Variable | Value | Source |
|----------|-------|--------|
| **Farm-gate cherry price** | **120 ETB/kg** | Sucafina 2025/26 harvest report (season average) |

### Convert to USD

Ethiopia floated the birr in July 2024. The exchange rate moved from ~55 ETB/USD to over 120 ETB/USD within months.

> 120 ETB/kg ÷ 127 ETB/USD = **$0.94/kg cherry**

| Variable | Value | Source |
|----------|-------|--------|
| Exchange rate | ~127 ETB/USD | Post-float rate, early 2026. World Bank annual data shows 82.60 for 2024 (annual average, includes pre-float months). |
| **Farmer cherry price in USD** | **$0.94/kg** | Calculated |

### Convert cherry to green equivalent

The farmer sells cherry, but international coffee is traded as green (the processed, export-ready bean). To compare the farmer's price to the export price, we need to convert using the cherry-to-green ratio.

For Ethiopian Arabica, the ratio is approximately **6:1**. It takes 6 kg of cherry to produce 1 kg of green coffee. This ratio is driven by species, varietal, and agro-climatic conditions, not by the processing method. A washed and a natural coffee from the same origin have essentially the same ratio.

> $0.94/kg cherry x 6 = **$5.67/kg green equivalent**

*(Why multiply? Because 6 kg of cherry are needed per 1 kg of green, each kilogram of green embodies 6x the cherry value.)*

| Variable | Value | Source |
|----------|-------|--------|
| Cherry-to-green ratio (Ethiopian Arabica) | 6:1 | Course reference. Ranges from 6:1 to 7:1 for Arabica depending on altitude and varietal. Ethiopia is at the lower end. Rwanda is ~7:1 (higher altitude). |
| **Farmer price in green equivalent** | **$5.67/kg green** | Calculated |

> **What this means:** The farmer receives $5.67 worth of cherry for every kilogram of green coffee that will eventually be exported. This is the number we can compare to the export price.

---

## Step 2: The Export Price

Ethiopian washed Arabica is a premium origin. The FOB (Free On Board) export price reflects the global Arabica benchmark (ICE "C" futures) plus Ethiopia's quality differential.

In early 2026, with the ICE "C" above 300 cents/lb ($6.61/kg) and Ethiopian washed commanding a positive differential, the FOB price is approximately **$8.00/kg green**.

> Farmer share = $5.67 / $8.00 = **71%**

| Variable | Value | Source |
|----------|-------|--------|
| ICE "C" Arabica futures | ~310 cents/lb (~$6.83/kg) | FRED/Yahoo Finance, March 2026 |
| Ethiopian differential | +$0.50 to +$1.50/lb | Typical for washed Ethiopian; varies by grade and lot |
| **Estimated FOB export price** | **~$8.00/kg green** | Estimated from C + differential |
| **Farmer share of export price** | **71%** | Calculated |

> **Context:** A 71% farmer share is higher than Ethiopia's historical average (~65%) but consistent with the current tight supply environment. For comparison: Vietnam ~95%, Colombia ~80%, Rwanda ~54%. These are point-in-time estimates that move with prices and exchange rates.

---

## Step 3: What Happens Between Export and Cup

The green coffee travels from Addis Ababa to a roaster in the US through several stages, each adding cost:

### Shipping and import

> $8.00 + $1.00 = **$9.00/kg landed cost**

The $1.00 covers ocean freight, insurance, import duties, and handling. Approximate; actual costs vary by contract terms and volume.

### Roasting

Roasting causes a ~16% weight loss (moisture evaporates). The raw material cost per kilogram of roasted coffee is:

> $9.00 ÷ 0.84 = **$10.71/kg roasted** (raw material only)

Add roasting labor, energy, equipment depreciation, packaging, and overhead, roughly $4/kg for a specialty roaster:

> $10.71 + $4.00 = **$14.71/kg roasted**

The roaster's margin on wholesale is roughly $25-45/kg, covering labor, packaging, sales, and profit.

### Brewing at the cafe

A cafe buys roasted coffee at wholesale (roughly $40-60/kg from a specialty roaster) and brews it into individual cups. Industry standard: **1 kg of green coffee produces approximately 50 cups** of 12oz brewed coffee (accounting for roasting weight loss and the ~17g dose per cup).

The cafe's cost of the coffee itself is small relative to its other costs:

> $14.71 ÷ 50 cups = **$0.29/cup in coffee cost**

The other $5.46 of a $5.75 pour-over pays for the barista, the rent, the equipment, the cups, the water, and the profit. In Manhattan, rent and labor alone dominate.

---

## Step 4: What the Customer Pays

NYC coffee prices near Columbia's campus, as of March 2026:

| Venue | Drink | Price | Source |
|-------|-------|-------|--------|
| Starbucks | Grande brewed drip (16oz) | $3.00-3.50 | Estimated for NYC |
| Joe Coffee | Drip coffee (12oz) | $4.50-5.50 | Morningside Heights location |
| Blue Bottle | Pour-over (12oz) | $5.75 | [FullMenuPrices](https://fullmenuprices.com/blue-bottle-coffee-menu-with-prices/) |
| Joe Coffee | Single-origin pour-over (12oz) | $6.50-8.00 | Estimated for specialty single-origin |

---

## The Full Picture

For a **$5.75 pour-over** at a specialty cafe near campus, 50 cups from 1 kg of green:

| Stage | Amount | % of Retail |
|-------|--------|-------------|
| **Ethiopian farmer** | **$5.67** | **2.0%** |
| Processing and export | $3.33 | 1.2% |
| Roasting and wholesale | $5.71 | 2.0% |
| Cafe (labor, rent, cups, profit) | $272.79 | 94.9% |
| **Customer pays (50 cups x $5.75)** | **$287.50** | **100%** |

### Across different retail formats

| Retail format | Cup price | 50 cups | Farmer's $5.67 as % |
|---------------|-----------|---------|---------------------|
| Starbucks grande drip | $3.25 | $162.50 | 3.5% |
| Joe Coffee drip | $5.00 | $250.00 | 2.3% |
| Blue Bottle pour-over | $5.75 | $287.50 | 2.0% |
| Single-origin Ethiopian pour-over | $7.50 | $375.00 | 1.5% |

> **The paradox:** The more a cafe charges for single-origin Ethiopian coffee, emphasizing its provenance and the farmer's story, the smaller the farmer's share of the final price becomes.

---

## Key Assumptions and Sensitivity

Every number in this analysis rests on assumptions. Here is where the uncertainty lives:

| Assumption | Value used | Range | Impact if wrong |
|-----------|-----------|-------|-----------------|
| Farm-gate cherry price | 120 ETB/kg | 100-145 | At 100 ETB, farmer receives $4.72/kg green |
| Exchange rate (ETB/USD) | 127 | 120-135 | At 135, farmer receives $5.33/kg green |
| Cherry-to-green ratio | 6:1 | 6:1 to 7:1 | At 7:1, farmer receives $6.61/kg green |
| FOB export price | $8.00/kg | $7-9/kg | Changes farmer share of export from 63% to 81% |
| Cups per kg green | 50 | 45-55 | Changes retail total proportionally |
| NYC pour-over price | $5.75 | $5-8 | Changes farmer % of retail |

### The claim that is robust

Regardless of which assumptions you adjust, the structural finding holds: **the farmer captures 1-6% of the retail value of a cup of coffee**. This is not primarily a function of exploitation in the supply chain. The Ethiopian farmer receives a reasonable share of the export price (71%). The gap is a function of the enormous cost of labor and real estate in a consuming-country city.

### The claim that is sensitive

The **farmer share of the export price** (71%) is sensitive to the cherry price and the exchange rate. If the cherry price drops to 100 ETB/kg at an exchange rate of 135, the share drops to ~59%. If the birr stabilizes and cherry prices in ETB don't keep pace, the share could compress further.

---

## Replicating This Analysis

To update these numbers with current data:

1. **Cherry price:** Check the latest Sucafina or Trabocca harvest reports for farm-gate cherry prices
2. **Exchange rate:** Use the [World Bank API](https://api.worldbank.org/v2/country/ET/indicator/PA.NUS.FCRF?format=json) or check xe.com for current ETB/USD
3. **Export price:** Check ICE "C" futures at [FRED](https://fred.stlouisfed.org/series/PCOFFOTMUSDM) and add Ethiopia's differential (~$0.50-1.50/lb for washed)
4. **NYC cafe prices:** Check Joe Coffee or Blue Bottle menus, or delivery apps for current pricing
5. **Run the math:** All conversion factors are in `data/processed/coffee_conversion_factors.csv`

---

## Discussion Questions

1. The farmer captures 2% of the retail value but 71% of the export price. Which number is more meaningful for understanding the farmer's position? Why?

2. Cafe costs (labor, rent) account for ~95% of the retail price. Does this mean the supply chain is "fair"? What would need to change for the farmer to capture a meaningfully larger share of retail value?

3. The birr devaluation in 2024 increased the farmer's cherry price in ETB (from 35 to 120 ETB/kg) while decreasing its dollar value. Is the Ethiopian farmer better off or worse off after the devaluation? What additional information would you need to answer this?

4. A specialty roaster sells a 250g bag of Ethiopian single-origin for $25 ($100/kg). The green coffee cost them ~$9/kg. Break down where the $91/kg margin goes. How much is cost, how much is brand, and how much is margin?

5. If you could redesign one element of this value chain to increase the farmer's absolute income, what would it be, and what are the practical barriers to implementing it?

---

*Data last verified: March 2026. Cherry prices, exchange rates, and NYC cafe prices should be updated before reuse.*
