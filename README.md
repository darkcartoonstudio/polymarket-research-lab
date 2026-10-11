# Polymarket Research Lab

**A public research journal about building — and honestly testing — a BTC 5-minute zone-micro-scalping bot on Polymarket.**

![Research pipeline](assets/research-pipeline.svg)

> **Research status:** exploratory. I have not demonstrated a robust, reproducible, out-of-sample profitable edge. This is not a signal service, a trading product, or financial advice.

## The story: a trader, a hypothesis, and a $1,000 dream

I like prediction markets, and I started by trading on my own Polymarket account manually. That made me curious about what happens underneath a simple UP/DOWN trade: the entry price, the bid/ask spread, available liquidity, the order book, fees, timing, and the path a price takes before resolution.

That curiosity became a research project. I began collecting data, grouping entry prices into zones, replaying historical markets, studying order-book behavior, building an observer for several price feeds, and learning the hard way how easily a backtest can mislead you.

**My personal dream is to build a bot that can one day grow my trading balance toward $1,000 and let me wake up to a balance earned through a system I have tested carefully.** That is an aspiration, not a forecast. I am not claiming that I have achieved it, that the bot currently earns money, that it will happen by a deadline, or that it can make $1,000 per day. I do not know whether this goal is achievable with this strategy.

I am sharing the research because the failures, uncertainties, data pipeline, and negative results may be useful to someone else. I want feedback from people who know prediction markets, market microstructure, execution systems, statistics, and quantitative research. If these notes help someone avoid a mistake, that is already useful.

### The goal, stated plainly — this is the ambitious target, not a claim it has been hit

| Win rate | Winners | Losers | Net profit per day (1,520 trades, $1 stake, +$0.9601/−$1.0567) |
|---|---:|---:|---:|
| 100% | 1,520 | 0 | +$1,459.35 |
| 90% | 1,368 | 152 | +$1,152.70 |
| 80% | 1,216 | 304 | +$846.05 |
| 70% | 1,064 | 456 | +$539.40 |
| 65% | 988 | 532 | +$386.35 |
| 60% | 912 | 608 | +$233.30 |
| 55% | 836 | 684 | +$79.80 |
| **52.4%** | **796** | **724** | **≈ $0 — break-even** |
| 50% | 760 | 760 | −$73.50 |

Starting capital: $4.77. Target: $1,000. Same dollar reused, not grown. This table is arithmetic, not a forecast — see [What the current evidence says](#what-the-current-evidence-says) for what has actually been measured against it.

The +$0.9601 and −$1.0567 figures here are **measured average** outcomes across many trades in the author's own data, distinct from the **+$0.95 / −$1.056 worked single-price example** in [the take-profit accounting note](docs/take-profit-accounting.md), which is why this table's 52.4% break-even and that note's 52.64% break-even are two different, non-interchangeable numbers — not a typo.

## The strategy I am trying to test

The main line of research is **zone-based micro-scalping on Polymarket BTC 5-minute Up/Down markets**. The bot is not validated for unattended live trading; the strategy remains a hypothesis.

The research question is:

1. Divide candidate entry prices into predefined price bands. An early grid used fine zones across roughly **$0.01–$0.50**, with **$0.025** increments; reports also evaluate broader and overlapping bands such as F40 (0.40–0.45) and F45 (0.45–0.50).
2. Observe the market and, where available, the order book around each entry zone. Explore whether the zone alone or zone plus order-book imbalance contains information about subsequent price movement.
3. Test whether a trade opened in a zone can reach a defined **net take-profit target after entry and exit fees**, before resolution, and compare it with holding to resolution.
4. Evaluate every entry, including failures, fees, unresolved outcomes, execution limits, and realistic fill assumptions. A zone with the highest target-hit rate is not automatically the best strategy.
5. Keep data collection, historical replay, paper/virtual trading, and any real-money observation separate.

The principal historical replay summarized below used a **+$0.95 net profit target per $1 stake**. A separate visual prototype in [`prototypes/`](prototypes/) shows +$0.96; it is a UI sketch with a synthetic price path, not research evidence. Those values must not be mixed as though they came from the same experiment.

### Exactly what +$0.95 net means

For a $1.00 stake entered at 0.20 under the example fee formula, 5 shares are bought and the entry fee is 0.0560 USDC. The initial cash outflow is therefore **1.0560 USDC**. To finish with **+$0.9500 net P&L**, the sale must credit **2.0060 USDC after exit fees have already been deducted**: `2.0060 − 1.0000 stake − 0.0560 entry fee = +0.9500`. The fee is not literally refunded as a separate payment; the net sale proceeds must economically cover it.

If the position instead settles worthless, the full loss under these assumptions is −1.0560 USDC. With only two possible outcomes—exactly +0.95 for every winner and exactly −1.056 for every loser—the theoretical break-even win rate is **52.64%**. That threshold does **not** automatically apply to the historical “take profit if hit, otherwise hold to resolution” replay, because a trade that misses the TP may still receive a settlement payout. A target-hit rate is not the same as a win rate. See the full [take-profit cash-flow explanation](docs/take-profit-accounting.md), [French version](docs/take-profit-accounting-fr.md), and the executable arithmetic example [`tools/tp_accounting_example.py`](tools/tp_accounting_example.py).

## What I have done so far

- Built an observer/collector concept around short-duration BTC/ETH/SOL/XRP UP/DOWN markets and multiple reference-price feeds.
- Built a separate zone-research line focused on BTC 5-minute markets, price bands, book state, entry/exit simulation, fee handling, and P&L reconciliation.
- Studied CLOB order-book snapshots and deltas, local order-book reconstruction, reconnects, stale data, crossed books, timestamps, and market resolution.
- Replayed a public historical market dataset to test target-touch rates and net expectation under explicitly stated assumptions.
- Separated **O1** (predict final UP/DOWN direction) from **O2** (whether a specified entry/exit path could produce positive net P&L). A correct direction prediction does not prove a profitable trade.
- Documented failures: an API-accepted order is not necessarily a fill; a connected WebSocket can still be stale; a large trade dataset does not substitute for complete L2 order-book history; repeated re-entry after a stop can compound losses.

More detail and status labels are in [the project map](docs/project-map.md), [the architecture note](docs/architecture.md), and [the progress log](docs/research-status.md).

## What the current evidence says

### Historical target replay (author-reported, not independently reproduced here)

One report replays **15,682 five-minute markets**, **324,048 simulated entries**, and **295,921 entries with known outcomes** from [`kachoio/polymarket-5-minute-crypto-up-down-markets`](https://github.com/kachoio/polymarket-5-minute-crypto-up-down-markets). The simulation used a $1 stake, best-ask entry proxy, fee-rate assumption of 0.07, no stop loss, a 120-second cutoff, and the first contact per market/zone/side.

- Best reported band for touching the **+$0.95 net target**: **F45 (0.45–0.50), 11,297 / 24,210 = 46.7%**.
- F45 reported average net result: **−$0.0719 per $1 stake** under “take profit if hit, otherwise hold to resolution”; **−$0.0588** under “always hold to resolution”.
- The companion report reported non-positive expectation across all 20 tested zones under both exit rules.
- The source data did not contain full time-stamped L2 depth, so it cannot faithfully model queue position, partial fills, order-book depletion, and actual executable costs.

The summary tables are available as CSV in [`data/`](data/). The original replay code and raw market data are not shipped with this public repository, so these numbers are **transcribed from my research reports, not independently verified or reproduced by this package**. Some price bands overlap; the rows are not independent samples.

### Earlier collection campaigns are different samples

An early campaign report recorded about **10.83 hours**, 663 candidates, and 621 retained entries after 42 invalid crossed-book observations were excluded. Its best reported F40 result was **12/22 (54.5%)** — far too small to support a reliable claim.

A separate report for a roughly **20.92-hour** collection used 5,149 distinct entries and 7,098 zone rows. It reported 4,964 decided outcomes and 2,204 wins under its own outcome labeling. This is a different collection and denominator from the historical replay; do not pool the figures.

### Exploratory order-book lead — not a validated result

Later working notes described approximately 1.7 million L2 snapshots and an exploratory combination involving band F400 (0.40–0.425) and order-book imbalance above 0.7942. The reported hit rate was around 58.9%, compared with about 49.5% for a static condition. The public package does **not** yet include the exact export, denominator, event-label definition, exclusions, time split, or reproducible calculation for that observation. Treat it as an **unverified research lead**, potentially affected by selection bias or overfitting—not as a validated win rate or proof of profitability. It should not drive trading until the evaluation is reproducible and out-of-sample.

## Architecture at a glance

![Project architecture](assets/architecture-overview.svg)

The work has two related but distinct tracks:

- **Zone micro-scalping:** collect market/book data → validate and timestamp it → classify price zones and candidate features → simulate entry/exit with costs → measure expectancy and robustness.
- **Directional observer/model:** collect Polymarket odds and multiple reference-price feeds → generate a forecast → evaluate direction against final resolution (**O1**) and evaluate a separate virtual entry/exit path (**O2**).

They share research principles, but their scores and outcomes must not be blended. The reviewed continuous direction score was not historically replayed or walk-forward validated in the reviewed version. Small live-observation samples did not prove an edge.

See [Architecture](docs/architecture.md) for the data path and [Research protocol](docs/research-protocol.md) for evaluation rules.

## What is still unfinished

- Reproduce the historical replay from a pinned dataset version and publish checksums, exact filters, code, and run instructions.
- Replay with historical L2 snapshots and more realistic bid/ask, depth, fees, latency, and partial fills.
- Freeze the zone/imbalance hypothesis before testing; use chronological train/validation/test splits and walk-forward evaluation.
- Audit the reported F400 + imbalance result, including denominator, outcome, uncertainty, parameter selection, and independent holdout.
- Evaluate expectancy, drawdown, calibration where relevant, and robustness—not only win rate or target-hit rate.
- Keep paper/virtual trading separate from any real-money bot. A live automated edge has not been established.

## How the community can help

I would especially value feedback on: L2 replay and fill assumptions, order-book imbalance definitions, avoiding leakage and overfitting, walk-forward test design, fee modeling, and reproducibility of the reported tables. Please challenge the methods and denominators, not just the headline percentage. The focused questions are collected in [community-questions.md](docs/community-questions.md).

## What this repository deliberately excludes

This is a research notebook, not a mirror of my private bot repositories. It does not include wallet keys, API credentials, `.env` files, executables, binary archives, full account logs, or a copy of all private source code. I am publishing the methods, architecture, selected results, lessons, and clearly labeled gaps—not compromising private systems to make the project look complete. See [SECURITY.md](SECURITY.md).

## Disclaimer

Educational research only; not investment advice. Polymarket trades can lose the entire amount staked. Historical results and synthetic demonstrations are not evidence of future performance. No claim of profitability is made.

## Start here

- [Research status and progress log](docs/research-status.md)
- [Strategy, objective, and boundaries](docs/strategy-and-objective.md)
- [Take-profit cash-flow accounting (+$0.95 net)](docs/take-profit-accounting.md)
- [Runnable arithmetic example](tools/tp_accounting_example.py)
- [Architecture](docs/architecture.md)
- [Data and experiment register](docs/data-status-and-datasets.md)
- [Research protocol](docs/research-protocol.md)
- [Reported CSV summary and caveats](data/README.md)
- [Visual prototype disclosure](prototypes/README.md)
- [French overview](README_FR.md)
