# Data dictionary for research notes

This document standardizes terms used across the notes. Exact field names vary by implementation; these are conceptual definitions.

| Term | Meaning | Common failure mode |
|---|---|---|
| `market_id` / condition ID | Stable identifier for a particular prediction market/condition | Joining by display title or guessed slug can mix markets. |
| `decision_ts` | Timestamp when the strategy had all required information and made the decision | Using data received later introduces look-ahead. |
| `event_ts` | Timestamp assigned by the data provider to a market-data event | Provider clocks and local clocks may differ. |
| `receive_ts` | Local timestamp when the collector received the event | Needed to measure delay and staleness. |
| `price_to_beat` / PTB | Reference price used by a market's up/down condition | The reference source and exact opening timestamp must be verified. |
| `best_bid` | Highest displayed buy price | It may not have enough size to exit the intended position. |
| `best_ask` | Lowest displayed sell price | It may not have enough size to enter the intended position. |
| L2 order book | Price levels with displayed quantities, beyond only the best bid/ask | Snapshots without updates/gap handling can be stale or inconsistent. |
| crossed book | A local book state where bid is equal to or above ask under conditions where that is invalid | May indicate asynchronous updates, parsing issues, or feed state mismatch. |
| accepted order | API accepted the request for processing | Does not prove any quantity matched. |
| confirmed fill | Matched trade/filled quantity reconciled with a trade event or authoritative account state | Treating an acknowledgement as a fill overstates execution. |
| implied probability | Contract price interpreted approximately as probability under a stated convention | Bid/ask, fees, market impact, and resolution mechanics can break a simplistic reading. |
| `p_model` | Model-estimated probability of an outcome | Needs calibration and out-of-sample validation. |
| `p_market` | Market-implied probability under a defined price/midpoint convention | The chosen price and fee treatment must be disclosed. |
| edge | Difference between model probability and market-implied probability under a stated definition | A positive numeric gap is not itself a proven profitable edge. |
| hit rate | Fraction of trials satisfying a specific event, e.g. touching a take-profit level | Not the same as profitable trade rate or positive expectancy. |
| expectancy | Average net outcome per trade after all stated costs and outcome rules | Omitting losses, fees, or unresolved cases biases it. |
| O1 | Direction-prediction objective: forecast compared with official resolution | Can be right while the trade is unprofitable or unfillable. |
| O2 | Intra-market trade simulation objective: entry/exit and net P&L | Requires execution assumptions, not just directional labels. |
| staleness | Age of the latest relevant value when a decision is made | Quiet or blocked WebSockets can leave a process apparently connected but stale. |
| `net_sale_proceeds` | Gross sale proceeds minus exit fees and other explicitly modeled sell-side costs | State whether displayed costs are already deducted. |
| `initial_cash_outflow` | Stake plus entry fees and other explicitly modeled entry-side costs | This is more than the nominal stake when fees apply. |
| `net_pnl` | Net sale/settlement proceeds minus initial cash outflow and any other declared costs | A +0.95 net target means +0.95 profit, not 0.95 total received. |
| `target_hit_rate` | Share of entries that reached the net TP threshold under the defined replay rule | Not automatically the profitable-trade win rate. |
| `win_rate` | Share of trades whose final P&L after the declared fees and exit/settlement rules is positive | Must be derived from the final trade outcome, not target touch. |
