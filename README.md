# Value Chain Analysis

**Browse the site: [ccerv1.github.io/value-chain-analysis](https://ccerv1.github.io/value-chain-analysis/)**

Course materials for a guest lecture on Value Chain Analysis at Columbia SIPA. Uses coffee as the primary case study to teach a general methodology for understanding how agricultural commodities move from farm to export, who captures value along the way, and what can be done about it.

---

## Start Here

Read these in order before the lecture:

1. **[Coffee: Cherry to Cup](lecture-notes/coffee-value-chain.md)** -- How coffee goes from a fruit on a tree to a cup in your hand, in nine stages
2. **[From Ethiopian Cherry to NYC Cup](lecture-notes/ethiopian-cherry-to-nyc-cup.md)** -- Worked example tracing one kilogram from an Ethiopian farm to a Morningside Heights pour-over
3. **[The VCA Framework](lecture-notes/value-chain-analysis.md)** -- Map, Breakdown, Benchmark: the three-step methodology
4. **Pick a case study** -- [Vietnam](case-studies/vietnam.md) (efficiency), [Rwanda](case-studies/rwanda.md) (quality), or [Honduras](case-studies/honduras.md) (resilience)

---

## Case Studies

| Country | Central Question |
|---------|-----------------|
| [Vietnam](case-studies/vietnam.md) | How did policy engineering create the world's most efficient coffee supply chain, and at what environmental cost? |
| [Rwanda](case-studies/rwanda.md) | Can premium quality positioning close the living income gap on 0.1-hectare farms? |
| [Honduras](case-studies/honduras.md) | How does a smallholder export economy survive compounding climate shocks? |
| [Colombia](case-studies/colombia.md) | When does institutional strength become institutional cost? |
| [Ethiopia](case-studies/ethiopia.md) | What is the economic value of traceability? |

## Skills Guides

For building your own VCA. Each guide teaches one step of the framework.

| Skill | Framework Step |
|-------|---------------|
| [1. Mapping](skills/01-mapping-a-value-chain.md) | Map |
| [2. Value Flows](skills/02-breaking-down-value-flows.md) | Breakdown |
| [3. Unit Conversion](skills/03-unit-conversion-and-price-analysis.md) | Breakdown |
| [4. Benchmarking](skills/04-benchmarking.md) | Benchmark |
| [5. Recommendations](skills/05-prioritizing-recommendations.md) | Action |
| [6. Deep Dive](skills/06-conducting-a-value-chain-deep-dive.md) | Full methodology |

## Reference

- [Reading List](reading-list/README.md) -- Background PDFs: case study sources, USAID/WFP guides, glossary
- [Slides by Year](lectures/README.md) -- Lecture decks from 2017-2025 as downloadable PDFs
- [Using AI](lecture-notes/using-ai.md) -- Prompt template for conducting your own VCA with an AI assistant

## For Developers

Data scripts and schemas for extending the analysis: [`scripts/`](https://github.com/ccerv1/value-chain-analysis/tree/main/scripts)

```bash
uv sync
uv run python scripts/fetch_usda_coffee.py
uv run python scripts/fetch_market_data.py
```
