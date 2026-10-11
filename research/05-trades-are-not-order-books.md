# Why a huge trade-history dataset may still be insufficient for an L2 backtest

A dataset can contain hundreds of millions or billions of executed transactions and still be inadequate for testing a short-horizon strategy whose entry and exit depend on spread, depth, and the cost of immediate execution.

## What transactions tell you

A trade tape can show that a transaction occurred, its timestamp, price and possibly quantity and aggressor side. It is valuable for studying prints, realized volatility, volume and trade-flow features—subject to the fields and quality actually provided.

## What it usually cannot tell you by itself

Without time-aligned order-book state and updates, it does not fully reconstruct:

- the best bid and ask available just before an order;
- how much quantity was displayed at each price level;
- spread and depth as they evolved;
- whether a hypothetical order would have matched immediately or rested;
- queue priority, partial fills and the quantity available before the book changed;
- what price could have been realized when exiting a position.

Inferring a complete L2 book from trades alone requires assumptions that can dominate the result. A trade at price X does not prove that an arbitrary simulated order could have filled at X, at that time, and for that size.

## Data required for more faithful replay

Prefer, where available:

1. Full order-book snapshots with timestamps and quantities by price level.
2. Incremental updates, with sequence IDs or another documented method for detecting gaps.
3. Trades linked to the same market/time axis.
4. Market metadata: tick size, order-size constraints, status, and fee schedule.
5. Order/response/fill data for live or paper reconciliation.
6. Resolution labels and the authoritative reference source.
7. Local receive timestamps to measure feed delays and stale windows.

The collector must preserve enough information to reconstruct the state **at the decision time**, not just a final or periodic snapshot.

## A better benchmark statement

Prefer: “This replay uses best-bid/ask snapshots and cannot model full depth, queue position, or partial fills.”

Avoid: “This backtest precisely simulates execution” when the underlying data only contains trades or top-of-book values.

## Why this matters for short-dated prediction markets

With a narrow expected edge and a short resolution horizon, spread, fees, price jumps and available size can be comparable to the gross target. Ignoring them can turn an untradeable historical pattern into an apparently profitable simulation.

## Takeaway

Dataset size is not the same as execution realism. Choose data based on the mechanism being tested; quantify what is missing and downgrade the claim accordingly.
