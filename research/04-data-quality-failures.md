# Data-quality failures that can invalidate a trading result

A backtest can be arithmetically correct and still answer the wrong question because its input labels, timestamps, market state, or execution records are wrong.

## Failure patterns observed in the research

### 1. A WebSocket is connected but its data is stale

A stream can stop delivering useful payloads without immediately closing the connection. A process that logs “connected” may keep using old prices. Track the time since the latest valid event, apply read deadlines/watchdogs, and reconnect or mark the feed unavailable when freshness limits are exceeded.

### 2. Resolution depends on receiving one more tick

If a market is marked resolved only when a new price tick arrives after the scheduled end, a quiet feed can leave it unresolved—or cause a stale value to be used. Schedule resolution checks against the market's expected end time, then fetch or reconcile the authoritative outcome. Never use a post-end tick as the only trigger for settlement logic.

### 3. Local clock drift corrupts “time remaining”

Comparing market timestamps with an unsynchronized wall clock changes how remaining time and signal windows are calculated. Prefer a monitored server-time offset or a robust estimate from server timestamps, document the precision, and test the behavior during clock jumps and reconnects.

### 4. Crossed or incomplete local order books

Out-of-order updates, inconsistent snapshots, or lost deltas can produce impossible local states. Validate bid/ask ordering, levels, freshness and update continuity. Mark the book invalid and resynchronize instead of trading from it. Count invalid events explicitly in research reports.

### 5. A risk stop immediately reopens the same position

One paper-trading session contained repeated entries at the same setup after a hard-loss stop. Offline analysis attributed a substantial share of that session's loss to these immediate re-entries. This is an example of a control-loop defect, not proof about expected strategy performance.

Controls worth testing include: refuse entries whose modeled immediate exit already breaches the hard loss limit; add a same-setup cooldown after a stop; make exceptions explicit; and log every blocked or allowed re-entry with a reason. A guard changes behavior but does not create a statistical edge on its own.

## Operational checklist

- Is each price fresh at decision time?
- Are event timestamps and local receive timestamps both stored?
- Is the market-open reference price sourced and time-aligned correctly?
- Can resolution be finalized even if a price feed becomes silent?
- Does a reconnect force local state validation/resynchronization?
- Are order acknowledgement, trade fill, inventory, and P&L reconciled separately?
- Are invalid books, exclusions, missing outcomes, and duplicated messages counted?
- Does a stopped strategy avoid immediate uncontrolled re-entry?

## Takeaway

Data quality is part of the strategy specification. Publish the exclusions, freshness thresholds, resynchronization rules, and outcome source alongside the performance metric. Do not treat operational bug fixes as evidence of profitability.
