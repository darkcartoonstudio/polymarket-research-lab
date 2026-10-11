# Strategy, goal, accounting, and boundaries

## Personal motivation

I started with manual trades on my own Polymarket account. The project grew from a practical question: can market microstructure, entry-price zones, and order-book conditions help identify repeatable opportunities in BTC five-minute UP/DOWN contracts?

My personal aspiration is to work toward a $1,000 account balance earned through a well-tested bot. It is a dream, not an income target, guarantee, forecast, or timeline. I have not achieved it; I do not know if the strategy can achieve it. This repo exists to record what I have tested, what failed, and what still needs evidence.

## Strategy hypothesis

- **Universe:** short-horizon Polymarket crypto UP/DOWN markets, with the main scalping study focused on BTC 5-minute markets.
- **Entry grid:** an early design divided candidate prices across roughly 0.01–0.50 using 0.025 increments; finer and overlapping bands have also been compared. A band name is only meaningful together with its exact bounds.
- **Candidate signal:** price entering a predefined zone, optionally combined with order-book variables such as bid/ask depth or imbalance.
- **Exit hypothesis:** attempt to reach a declared net take-profit target after applicable entry and exit fees before resolution; compare with holding to resolution and other explicit exit rules.
- **Historical replay target:** +0.95 USDC net profit per 1.00 USDC stake. A separate visual prototype uses +0.96 and a synthetic price path; it is not part of the historical replay.
- **Evaluation:** include all eligible entries, actual modeled sale proceeds, losses, unresolved outcomes, fees, realistic depth, latency, partial fills, and sample uncertainty.

## Exact meaning of the historical +0.95 net target

Using the worked example documented in [`take-profit-accounting.md`](take-profit-accounting.md): for a 1.00 USDC stake at entry price 0.20, 5 shares are bought. Under the report's illustrative 0.07 fee formula, entry fees are 0.0560 USDC, so initial cash outflow is 1.0560 USDC. To realize +0.9500 net P&L, the account must receive 2.0060 USDC in sale proceeds **after exit fees** have been deducted. The accounting is `2.0060 − 1.0000 − 0.0560 = +0.9500`.

The entry fee is not literally refunded as a separate platform payment; it is economically covered by the net sale proceeds needed to reach the stated net P&L. If the position settles worthless, the full loss under these assumptions is −1.0560 USDC.

If every winner earns exactly +0.95 and every loser loses exactly −1.056, the binary-payoff break-even rate is `1.056 / (1.056 + 0.95) = 52.64%`. This threshold is conditional: it is not a universal threshold for variants with partial exits, additional costs, or settlement payouts after a target is missed. In the historical replay, “TP if hit, otherwise hold to resolution” means a non-hit is not automatically a full loss.

See the [French explanation](take-profit-accounting-fr.md) and run the [arithmetic example](../tools/tp_accounting_example.py).

## Do not confuse these metrics

- `target_hit_rate`: share of entries that touched the specified target under a replay rule.
- `win_rate`: share of trades that finished profitable under a fully specified exit/settlement rule.
- `expectancy`: mean net P&L per eligible trade, including the full outcome distribution and stated costs.
- `direction_accuracy`: share of market-direction predictions matching final resolutions.
- `fill_rate`: fraction of intended orders/quantity that plausibly or actually filled under the chosen definition.

A high target-hit rate is not automatically a positive expectancy. Accurate direction is not automatically an executable or profitable trade. A score labelled `80%` is not a calibrated probability until tested.

## Status of the hypothesis

The best reported historical target-hit band was F45 at 46.7% for the +0.95 net target. The companion report recorded negative mean expectancy under both tested exit rules. The replay lacked full L2 depth. Therefore, no positive edge is established by the currently documented results. **Do not compare the 46.7% target-hit rate directly with the 52.64% binary-payoff break-even threshold as if they measured the same thing.**

## Visual prototype is separate

`prototypes/mechanism-100-100-visual-prototype.html` is a UI prototype with a hand-authored synthetic price path and hard-coded successful exits. It is not a backtest, does not include a complete losing-trade distribution, and must not be used to infer expected earnings. Its +0.96 target is different from the +0.95 historical replay. Its accounting also defines the target as net P&L after the modelled entry and exit fees; see [`prototypes/README.md`](../prototypes/README.md).
