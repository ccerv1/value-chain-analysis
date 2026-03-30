# Value Chain Analysis

![Value Chain Analysis](photos/vca-hero.png)

My name is [Carl Cervone](https://cerv.one). I have been teaching this guest lecture with Professor Glenn Denning at Columbia SIPA since 2017. This site is the written companion to the lecture. It covers how to trace the flow of value from farm to cup, diagnose where the problems are, and turn analysis into actionable recommendations.

You can browse all the [past lecture slides](lectures/README.md) (2017-2025). What follows is the current version, presented in March 2026 at Columbia SIPA.

### About me

I came to coffee through development work. After studying environmental science in my undergrad, I moved to Tanzania in 2004 to work in microfinance. In 2006, I joined [TechnoServe](https://www.technoserve.org/) and spent a decade working on coffee value chains across East Africa and Latin America. In 2016, I cofounded [Enveritas](https://www.enveritas.org/), which uses satellite data and machine learning to map and verify sustainability across coffee supply chains. In 2023, I cofounded [Kariba Labs](https://www.kariba.network/), which applies similar techniques to software (not agriculture) value chains. I am also a Columbia Business School alum.

The examples in this course draw from both my work in coffee, international business, and data science.

---

## Why do value chain analysis?

Value chain analysis is a powerful tool for a variety of disciplines. It is obviously useful in international development, but it is also used in business, finance, technology, and many other fields. At the most fundamental level, it is a framework for thinking about how things are made -- who does what, who gets paid what, and who controls the value. That's useful in any industry, from building rockets and semi-conductors to growing coffee and bananas.

Today we'll just be talking about coffee.

One of the most common questions I have gotten from students over the years is: *"What share of the price the consumer pays actually goes back to the farmer?"*

I have been tracking this at a high level every year as part of the lecture:

| Year | Farm-gate price ($/kg green equiv.) | NYC specialty cup price | Farmer's share of retail |
|------|-------------------------------------|------------------------|--------------------------|
| 2025 | ~$4.50 | ~$6.00 | ~1.5% |
| 2024 | ~$4.00 | ~$6.00 | ~1.3% |
| 2023 | ~$4.00 | ~$5.00 | ~1.6% |
| 2022 | ~$4.00 | ~$4.00 | ~2.0% |

The precise answer depends on the country, the buyer, and all the value chain steps in between. But, by and larger, the farmer's share of the retail cup price has stayed between 1-2% for as long as I have been measuring it. The absolute prices move. The structural ratio barely budges.

Why? And what, if anything, can be done about it?

Today you will learn not just how to answer questions like this yourself, but a framework for doing much more. Let me walk through the math for this year's numbers.

---

## This year's example: Ethiopian cherry to a Columbia campus cup

An Ethiopian farmer picks coffee cherry from her trees and sells it at the local market. That cherry is processed, exported, roasted, and brewed into a pour-over at a specialty cafe near Columbia's campus. Here is the complete conversion, step by step.

### Step 1: What the farmer receives

In the 2025/26 Ethiopian harvest season, farm-gate cherry prices averaged approximately **120 ETB/kg** ([Sucafina Ethiopia 2025/26 Harvest Update](https://sucafina.com/emea/news/ethiopia-2025-26-harvest-update)). This is a sharp increase from 35-40 ETB/kg in the prior season, driven by the birr devaluation and surging global prices.

Ethiopia floated the birr in July 2024. The exchange rate moved from ~55 ETB/USD to over 120 ETB/USD within months.

> 120 ETB/kg ÷ 127 ETB/USD = **$0.94/kg cherry**

For Ethiopian Arabica, the cherry-to-green ratio is approximately **6:1**. It takes 6 kg of cherry to produce 1 kg of exportable green coffee. (Why multiply? Because each kilogram of green embodies 6x the cherry value.)

> $0.94/kg cherry x 6 = **$5.67/kg green equivalent**

| Step | Calculation | Result |
|------|-------------|--------|
| Farm-gate price | 120 ETB/kg cherry | 120 ETB/kg |
| Convert to USD | 120 ÷ 127 | $0.94/kg cherry |
| Convert to green | $0.94 x 6 | **$5.67/kg green** |

### Step 2: The export price

Ethiopian washed Arabica is a premium origin. With the ICE "C" above 300 cents/lb and Ethiopian washed commanding a positive differential, the FOB export price is approximately **$8.00/kg green**.

> Farmer share = $5.67 / $8.00 = **71%**

A 71% farmer share is higher than Ethiopia's historical average (~65%) but consistent with the current tight supply environment. For comparison: Vietnam ~95%, Colombia ~80%, Rwanda ~54%.

### Step 3: From export to cup

| Stage | What happens | Cost |
|-------|-------------|------|
| Shipping and import | Ocean freight, insurance, duties | +$1.00/kg |
| Landed cost | | $9.00/kg green |
| Roasting | 16% weight loss + $4/kg overhead | $14.71/kg roasted |
| Brewing | 1 kg green = ~50 cups at ~17g/cup | $0.29/cup in coffee |

The other $5.46 of a $5.75 pour-over pays for the barista, the rent, the equipment, the cups, the water, and the profit.

### Step 4: What the customer pays

Near Columbia's campus, as of March 2026:

| Venue | Price |
|-------|-------|
| Starbucks grande drip (16oz) | $3.00-3.50 |
| Joe Coffee drip (12oz) | $4.50-5.50 |
| Blue Bottle pour-over (12oz) | $5.75 |
| Joe Coffee single-origin pour-over | $6.50-8.00 |

### The full picture

For a $5.75 pour-over, 50 cups from 1 kg of green:

| Stage | Amount | % of Retail |
|-------|--------|-------------|
| **Ethiopian farmer** | **$5.67** | **2.0%** |
| Processing and export | $3.33 | 1.2% |
| Roasting and wholesale | $5.71 | 2.0% |
| Cafe (labor, rent, cups, profit) | $272.79 | 94.9% |
| **Customer pays** | **$287.50** | **100%** |

The farmer's $5.67 becomes $287.50 at the register. The farmer captures **2%** of the retail value but **71%** of the export price. Which number matters more? That is one of the questions this course will help you answer.

> **The paradox:** The more a cafe charges for single-origin Ethiopian coffee, emphasizing its provenance and the farmer's story, the smaller the farmer's share of the final price becomes.

---

## What you will learn today

This worked example illustrates the core methodology: **convert, compare, contextualize**. The rest of the course teaches you to apply this systematically:

1. **[Coffee 101](coffee-value-chain.md)** -- Understand the product and the processing chain
2. **The VCA Framework**
    - [Map the actors](skills/01-mapping-a-value-chain.md)
    - [Break down the value flows](skills/02-breaking-down-value-flows.md) and [convert units](skills/03-unit-conversion-and-price-analysis.md)
    - [Benchmark against peers](skills/04-benchmarking.md)
    - [Turn insights into recommendations](skills/05-prioritizing-recommendations.md)
3. **[Case studies](case-studies/README.md)** -- Vietnam, Rwanda, Honduras, Colombia, Ethiopia
4. **[Practical tips](practical-tips.md)** -- How to do this in the field
5. **[Using AI](using-ai.md)** -- Prompt template for conducting your own VCA with an AI assistant

The goal is not just to understand coffee. It is to learn a methodology you can apply to any agricultural commodity in any country.

---

## Assumptions and sensitivity

Every number above rests on assumptions. Here is where the uncertainty lives:

| Assumption | Value used | Range | Impact if wrong |
|-----------|-----------|-------|-----------------|
| Farm-gate cherry price | 120 ETB/kg | 100-145 | At 100 ETB, farmer receives $4.72/kg green |
| Exchange rate (ETB/USD) | 127 | 120-135 | At 135, farmer receives $5.33/kg green |
| Cherry-to-green ratio | 6:1 | 6:1 to 7:1 | At 7:1, farmer receives $6.61/kg green |
| FOB export price | $8.00/kg | $7-9/kg | Changes farmer share from 63% to 81% |

Regardless of which assumptions you adjust, the structural finding holds: **the farmer captures 1-6% of the retail value of a cup of coffee**. This is not primarily exploitation. The farmer receives a reasonable share of the export price. The gap is a function of what it costs to employ someone and lease space in Manhattan.

*Data last verified: March 2026.*
