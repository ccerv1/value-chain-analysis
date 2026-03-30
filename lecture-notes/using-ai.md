# Using AI for Value Chain Analysis

You can use an AI assistant (Claude, ChatGPT, or similar) to help you conduct your own value chain analysis for a different commodity or country. The most effective approach is to give the AI access to this course's framework and then work through the analysis together.

## Starter Prompt

Copy and paste this prompt to get started. Replace the bracketed sections with your own commodity and country.

---

> I am conducting a value chain analysis of **[commodity]** in **[country]** using the Map / Breakdown / Benchmark framework from a Columbia SIPA course on value chain analysis.
>
> The course materials are at: https://ccerv1.github.io/value-chain-analysis/
>
> Key reference pages:
> - Framework: https://ccerv1.github.io/value-chain-analysis/lecture-notes/value-chain-analysis/
> - Worked example (coffee, Ethiopia to NYC): https://ccerv1.github.io/value-chain-analysis/lecture-notes/ethiopian-cherry-to-nyc-cup/
> - Skills guides: https://ccerv1.github.io/value-chain-analysis/skills/
>
> Please help me work through the following steps:
>
> 1. **Map** the value chain: identify the key actors from production to export (or retail), the flow of the product through each stage, and any parallel channels.
> 2. **Break down** the value flows: trace the price from the farmer/producer to the export or retail level, converting units and currency as needed. Build a waterfall showing where the money goes.
> 3. **Benchmark** against peer countries or commodities: compare yields, prices, farmer share, and costs.
> 4. **Recommend** interventions using an impact-feasibility matrix.
>
> Start by asking me what I already know about the **[commodity]** value chain in **[country]**, and then help me fill in the gaps with publicly available data.

---

## Tips for Working with AI

**Give it real data.** AI works best when you feed it actual numbers: farm-gate prices, exchange rates, production volumes, export data. The analysis will be more grounded than if you ask it to generate numbers from training data.

**Use the course datasets.** The datasets in this project are downloadable CSVs. You can upload them directly to an AI assistant and ask it to cross-reference, calculate, or chart from the data. See [Data & Schemas](../data/README.md) in the Developer section.

**Check the math.** AI assistants can make conversion errors. Run through the unit conversion steps yourself using the method in [Skill 3](../skills/03-unit-conversion-and-price-analysis.md). If the AI gives you a farmer share above 100% or below 10%, something is wrong.

**Push back on generic answers.** If the AI gives you a recommendation like "improve farmer access to markets," ask it to be specific: which markets, through what mechanism, at what cost, funded by whom. The [Recommendations skill guide](../skills/05-prioritizing-recommendations.md) has the framework for this.

**Adapt, don't copy.** The coffee value chain has specific features (the cherry-to-green conversion, the ICE "C" benchmark, the Arabica/Robusta split) that don't transfer directly to other commodities. Ask the AI to help you identify the analogous features for your commodity: What is the equivalent of "cherry to green"? What is the benchmark price? Where is the hourglass?
