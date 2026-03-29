# SIPA Value Chain Analysis — Course Materials

![Coffee cherries on the branch](photos/coffee-cherries-on-branch.png)

Companion materials for the Value Chain Analysis guest lecture at Columbia's School of International and Public Affairs. The course uses coffee as the primary case study to teach a general VCA methodology.

Instructor: Carl Cervone

---

## Repository Structure

```
sipa/
├── lecture-notes/          Evergreen written companion to the slides
├── skills/                 Six standalone VCA skill guides
├── case-studies/           Country case studies (Vietnam, Rwanda, Colombia, Ethiopia)
├── lectures/               Slide decks organized by year (2017-2025)
├── data/
│   ├── processed/          Analysis-ready CSVs
│   ├── raw/                Original downloads
│   └── exercises/          Student exercises (Ethiopia dataset, waterfall model)
├── scripts/                Python scripts to regenerate data
├── reading-list/
│   ├── case-studies/       Source PDFs for the country cases
│   ├── reference-guides/   USAID, WFP, and other methodology docs
│   └── glossary/           Coffee industry terminology
└── pyproject.toml          Python dependencies (use `uv sync` to install)
```

## Written Materials

### [Lecture Notes](lecture-notes/README.md)

Evergreen reference document covering the stable, year-over-year foundations of the course: Coffee 101, global market dynamics, the VCA framework (Map / Breakdown / Benchmark), fieldwork advice, and open questions.

- [The Coffee Value Chain: Cherry to Cup](lecture-notes/coffee-value-chain.md) — Visual guide to every processing stage with photographs
- [Value Chain Analysis](lecture-notes/value-chain-analysis.md) — Framework, market dynamics, methodology

### [Skills Guides](skills/README.md)

Six standalone guides, each teaching one discrete VCA skill. Read in order or reference individually.

1. [Mapping a Value Chain](skills/01-mapping-a-value-chain.md) — Actors, roles, relationships, parallel channels
2. [Breaking Down Value Flows](skills/02-breaking-down-value-flows.md) — Costs, revenues, margins, waterfall charts
3. [Unit Conversion and Price Analysis](skills/03-unit-conversion-and-price-analysis.md) — Local units to international standards
4. [Benchmarking](skills/04-benchmarking.md) — Cross-country and cross-time comparison
5. [Prioritizing Recommendations](skills/05-prioritizing-recommendations.md) — Impact-feasibility matrix
6. [Conducting a Value Chain Deep Dive](skills/06-conducting-a-value-chain-deep-dive.md) — Full methodology + coffee appendix

### [Case Studies](case-studies/README.md)

Hybrid write-ups: narrative story followed by analytical Map / Breakdown / Benchmark framework.

**Current** (2024-2025 lectures):
- [Vietnam](case-studies/vietnam.md) — Engineered growth: 95% farmer share, highest yields, environmental cost
- [Rwanda](case-studies/rwanda.md) — Premium positioning on tiny farms: quality strategy vs living income gap

**Archival** (earlier lecture years):
- [Colombia](case-studies/colombia.md) — Strong institutions, eroding margins: the FNC model under pressure
- [Ethiopia](case-studies/ethiopia.md) — Traceability lost and found: the ECX experiment

## [Slides](lectures/README.md)

Lecture slide decks organized by year. The course has been taught annually since 2017, evolving from a two-day format to a single combined deck.

| Year | Format | Notes |
|------|--------|-------|
| 2025 | Single deck + data workbook | Current |
| 2024 | Single deck + data workbook | |
| 2017-2023 | Day 1 + Day 2 | See [lectures/](lectures/) for details |

## [Data](data/README.md)

13 analysis-ready CSVs covering production, prices, trade, exchange rates, and development indicators. See [`data/README.md`](data/README.md) for full schema documentation.

Highlights:
- **USDA production** — 17 countries, 1960-2025, Arabica/Robusta split
- **Coffee prices** — Monthly (1992-present) and daily futures (2000-present)
- **Trade data** — 12 countries' annual exports from UN COMTRADE
- **Country lookup** — Master table for joining across data sources

Regenerate with:
```bash
uv sync
uv run python scripts/fetch_usda_coffee.py
uv run python scripts/fetch_market_data.py
```

## [Reading List](reading-list/README.md)

Background readings organized by type: case study source documents, USAID/WFP methodology guides, and a coffee glossary.
