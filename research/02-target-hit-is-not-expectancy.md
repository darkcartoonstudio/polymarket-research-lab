# A target-hit rate is not a trading edge

## Research question

A short-horizon strategy can have an attractive take-profit hit rate while losing money after costs or at settlement. The metric must match the actual exit rule and include every trial—not just winning exits.

## Reported historical replay

The author's research report recorded:

- Dataset: `kachoio/polymarket-5-minute-crypto-up-down-markets`, reported by the source report as CC0.
- Population: 15,682 five-minute markets.
- Simulated entries: 324,048, with outcomes known for 295,921.
- Stake: 1.00 USDC per entry.
- Entry proxy: best ask only.
- Fee assumption: 0.07, with entry/exit fees included in the net target calculation.
- Rule: no stop loss, a 120-second cutoff, and the first contact per market/zone/side.

The best reported zone for reaching a **net +0.95 USDC target** was F45, defined as an entry price from 0.45 to 0.50: 11,297 of 24,210 entries, or 46.7%.

The companion expectation analysis reported the following mean outcomes per $1 stake for F45:

| Exit rule | Reported mean net P&L |
|---|---:|
| Exit at +0.95 net if hit; otherwise hold to resolution | −0.0719 USDC |
| Always hold to resolution | −0.0588 USDC |

The same report recorded non-positive expectation in every tested zone under both rules. This result applies only to that data, model, cost assumptions and target. It is not a universal finding about every Polymarket market or future strategy.

## Cash-flow meaning of the +0.95 net target

“+0.95 net” is the **profit retained**, not the total cash credited by the sale. In the worked example at entry price 0.20, a $1.00 stake buys 5 shares. Under the assumed fee formula, the entry fee is 0.0560 USDC, so the initial cash outflow is 1.0560 USDC. To make +0.9500 net, sale proceeds must be 2.0060 USDC **after exit fees**: `2.0060 − 1.0000 − 0.0560 = +0.9500`. No separate fee refund is assumed; the net sale proceeds economically cover the entry cost. Full calculation: [`../docs/take-profit-accounting.md`](../docs/take-profit-accounting.md).

If the entire position settles worthless, this example loses 1.0560 USDC. Under the restricted binary-payoff assumption where all wins are +0.95 and all losses are −1.056, break-even is 52.64%. However, **this is not directly comparable with the 46.7% reported target-hit rate**: the historical rule is “TP if hit; otherwise hold to resolution”, and non-hit entries can still receive a settlement payout. Target-hit rate, profitable-trade win rate, and empirical expectancy must be reported separately.

## Why the result is limited

1. **Best ask is not depth.** The dataset did not provide complete time-stamped L2 order-book history. It cannot reliably simulate how much could be filled at the quoted level, queue priority, partial fills or impact.
2. **The fee schedule is an assumption.** Real fee treatment and available order types must be checked for the particular market and current platform implementation.
3. **No stop loss.** This was the strategy as replayed, not an endorsement of that risk choice.
4. **Entry population matters.** A result for one source, window, target, cutoff and sampling rule must not be combined with a different collection campaign as if they were one sample.
5. **The experiment is not independently reproduced here.** The detailed replay code and original raw report package are intentionally not included. Treat the numbers as author-reported until the run, dataset version, exclusions and calculations are independently reproduced.

## The general lesson

A target-touch percentage answers “how often did this event occur under this replay rule?” It does not answer “what was the average net return per trade?”

For every entry rule, report all trades, the exit rule, net proceeds, both-side costs, unresolved outcomes, mean/median P&L, and uncertainty. Do not select a zone using the same sample and then present it as an out-of-sample discovery. Reserve “positive edge” for positive, realistic, reproducible net expectancy on data that were not used to select the strategy.

## Source

Dataset named in the original report: https://github.com/kachoio/polymarket-5-minute-crypto-up-down-markets. Verify that repository's current version and license before reuse.
