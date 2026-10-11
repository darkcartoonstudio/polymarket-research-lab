# Project map: two research tracks, one research discipline

This public repository combines selected methodological lessons from two distinct private research lines. It does not copy their private source trees.

## Track A — BTC zone micro-scalping

**Question:** When a BTC 5-minute Up/Down token enters a predefined price band, does the subsequent path offer a realistic, net-positive exit opportunity after fees and execution constraints?

Research components documented so far:

1. Market discovery and lifecycle labels.
2. Live market data and order-book collection.
3. Local book snapshot/delta handling, freshness checks, reconnect/resynchronization, crossed-book exclusion.
4. Fine/overlapping price-zone analysis and entry-trigger tracking.
5. Historical target-hit replay and a companion expectancy calculation.
6. Paper/virtual execution, position state, fee/P&L accounting, re-entry guard design.
7. Planned next step: reproduce the runs and validate L2-aware entry/exit on untouched time periods.

Current result: the historical replay summarized in this repository showed no positive expectancy in its tested zones under the two stated exit rules. The data used best-ask proxies and lacked complete L2 depth.

## Track B — directional observer and model

**Question:** Can reference-price feeds, Polymarket odds, and defined market features forecast the final direction? Separately, can a virtual trade made from a decision point be executed and make money net of costs?

Conceptual pipeline:

1. Discover short markets and record their reference/price-to-beat and resolution time.
2. Observe Polymarket odds and multiple reference-price sources.
3. Build features/signals from EMAs, distance to reference, momentum, velocity, and cross-source alignment.
4. Evaluate **O1** against the final official UP/DOWN label.
5. Evaluate **O2** separately as virtual entries/exits, costs, and P&L.

Current result: a reviewed report found that one continuous score used for live-looking action suggestions had not been historically replayed or walk-forward validated. A separate short live observation included only seven complete markets. Those facts do not prove the model is useless, but they do not establish a reliable edge.

## Shared lesson

Prediction, data quality, execution, and expectancy are different gates. A project can collect data successfully but lack enough outcomes; a model can predict direction but fail net P&L; a bot can run without proving that its inputs are fresh.

## Publication boundary

This repo publishes a research narrative, selected aggregate tables, schemas, and methodological notes. Private implementation repositories, wallet material, account logs, credentials, executable archives, and unreviewed source dumps remain out of scope.

## Shared accounting convention

The historical +0.95 USDC target means net P&L, not sale receipts. Use the worked cash-flow example in [`take-profit-accounting.md`](take-profit-accounting.md) before interpreting target-hit data or break-even calculations.
