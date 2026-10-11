# An accepted order is not an executed trade

## Problem

Trading integrations often receive a successful API response and treat it as proof that a position exists. That mixes several distinct events: request accepted, order resting or matched, trade confirmed, and resulting inventory reconciled.

## Why the distinction matters

- A limit order may remain resting or expire without a match.
- A marketable order can be partially filled or fail depending on available liquidity and order type.
- Market-data acknowledgements do not represent private account fills.
- The best displayed price may have less size than the desired order.
- Fees, spreads, latency and price movement between observation and arrival can change realized execution.

## Safer accounting model

1. Record the client order ID and exchange order ID, if returned.
2. Maintain explicit states such as `submitted`, `accepted`, `resting`, `partially_filled`, `filled`, `cancelled`, `expired`, and `rejected`.
3. Build inventory and realized P&L from matched trade/fill records, not from an order acknowledgement.
4. Reconcile the user stream with REST/account state after reconnects, missed messages, or uncertain state.
5. Make duplicate events idempotent: processing the same trade twice must not double-count quantity or P&L.
6. Keep order state and position state separate, and record every state transition with event and receive timestamps.

## Local order-book state also needs integrity checks

A streaming local order book commonly needs a full snapshot followed by deltas. Snapshot and update handling must be documented precisely; in the implementation researched here, a delta replaces the size at the given price level and a zero size removes that level. The best bid and ask are recomputed from the current levels. This behavior must be verified against the current feed contract and client version rather than assumed forever.

On reconnect, “the socket is connected” is not proof that the local book is complete. Watch for stale payloads, sequence gaps if the feed provides sequence information, and implausible/crossed local states. Resynchronize from a fresh snapshot when needed.

## A practical safety rule

Never report a simulated or real fill until the matched quantity is supported by a trade/fill event or an authoritative reconciled account state. If the feed is stale or the book is not trustworthy, stop opening positions rather than silently trading from the last known state.

## What remains unproven

These controls improve measurement and operational correctness. They do not establish a profitable strategy. API endpoints, field names, order semantics, and fee schedules change; confirm current official documentation before implementing.
