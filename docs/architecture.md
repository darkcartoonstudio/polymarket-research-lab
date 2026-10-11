# Architecture: from market events to research claims

![Research architecture](../assets/architecture-overview.svg)

## A. Zone micro-scalping track

1. **Discovery and market identity:** identify the correct market, contract/token, open/end times, and official outcome source. Avoid guessed joins or inferred resolution labels.
2. **Collection:** store raw event timestamps and local receive timestamps. Collect Polymarket market data and, when available, full order-book snapshots/deltas and reference-price feeds.
3. **State integrity:** reconstruct the local book according to the feed contract; remove zero-size levels; recompute best bid/ask; detect stale payloads, reconnect gaps, crossed/invalid books, and clock drift; resynchronize before trusting state.
4. **Feature generation:** tag the price zone, market time remaining, spread, available depth, and explicitly defined order-book imbalance. Each feature must use only data available at the decision timestamp.
5. **Replay and execution model:** simulate an entry only when the declared trigger occurs; apply entry and exit fee assumptions, bid/ask side, depth/size limits, cutoff, partial-fill assumptions and the entire settlement rule. Record exclusions and unresolved cases.
6. **Evaluation:** report target-hit rate, full net P&L distribution, expectancy, uncertainty, sensitivity, regime/time splits, and chronological walk-forward results.
7. **Paper/virtual observation:** keep simulated fills and positions distinct from actual account fills. Reconcile order/trade/position state when observing real APIs.

## B. Directional observer/model track

1. Discover the market and capture the official reference price and resolution metadata.
2. Collect Polymarket odds and multi-source prices with source and receive timestamps.
3. Produce a forecast from a frozen and documented feature version.
4. **O1:** compare predicted direction with the official final resolution; report accuracy and uncertainty against baselines.
5. **O2:** independently replay an entry/exit policy, including real execution assumptions and net P&L.
6. Calibrate model probabilities on separate data; evaluate chronologically and walk-forward. A sigmoid-transformed score is not automatically calibrated.

## Cross-cutting controls

- **Time integrity:** preserve provider/event time and local receive time. Detect clock offsets and stale values.
- **Market resolution:** scheduled resolution must not depend on a coincidental post-end tick; the reference source must be the one that actually governs settlement.
- **Order integrity:** `accepted` is not `filled`. Build P&L only from confirmed matched quantity or authoritative reconciliation.
- **Idempotence:** duplicate trade events must not duplicate inventory or P&L.
- **Failure state:** a collector blocked by network policy or a stale feed should report the failure state clearly; process uptime is not collection success.
- **Research discipline:** lock hypotheses before test; separate exploratory, in-sample, out-of-sample, live-observed, and verified real-fill results.

## Not included

This document is an explanatory architecture, not a drop-in implementation guide. Credentials, private endpoints/configuration, account identities, live trading secrets, and private code are intentionally excluded.
