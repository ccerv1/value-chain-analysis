# Value Chain Analysis

**[Browse the course site](https://ccerv1.github.io/value-chain-analysis/)**

Course materials for a guest lecture on Value Chain Analysis at Columbia SIPA. Uses coffee as the primary case study to teach a general methodology for understanding how agricultural commodities move from farm to export, who captures value along the way, and what can be done about it.

Current version: March 2026. All data and prices are updated to the most recent available.

## Site Contents

- [Why VCA?](lecture-notes/why-vca.md) -- Introduction, background, and a worked example
- [Coffee 101](lecture-notes/coffee-value-chain.md) -- Visual guide to the processing chain
- [The VCA Framework](skills/01-mapping-a-value-chain.md) -- Mapping, value flows, benchmarking, recommendations
- [Case Studies](case-studies/README.md) -- Vietnam, Rwanda, Honduras, Colombia, Ethiopia
- [Practical Tips](lecture-notes/practical-tips.md) -- Fieldwork advice
- [Using AI](lecture-notes/using-ai.md) -- Prompt template for your own analysis

## For Developers

```bash
uv sync
uv run python scripts/fetch_usda_coffee.py
uv run python scripts/fetch_market_data.py
```
