# Take-profit cash-flow accounting: what “+$0.95 net” actually means

This note is the accounting reference for this repository. The historical zone replay uses a **+$0.95 net-profit target per $1.00 stake**. The visual prototype is separate and uses +$0.96.

## The key distinction

**A “+$0.95 net TP” is the profit kept after the original stake and applicable trading fees are covered. It is not the total amount received from selling.** The sale proceeds must be large enough to cover the initial cash outflow and leave another $0.95 in the account.

Entry fees are not literally refunded by Polymarket. They are economically recovered only if the net sale proceeds cover the stake **and** the entry fees, plus the target profit. Exit fees are deducted before calculating net sale proceeds.

## Worked example: $1 stake bought at 0.20

Assumptions for this example only:

- Stake: 1.0000 USDC
- Entry price: 0.20 USDC per share
- Shares bought: `1.00 / 0.20 = 5.00`
- Fee-model rate: `0.07`, using `fee = shares × rate × price × (1 − price)`
- Target net P&L: +0.9500 USDC
- No other costs are included. Actual applicable fees and fills must be checked for the specific market and order.

### Cash leaving the account at entry

| Item | Amount |
|---|---:|
| Stake used to buy 5 shares | 1.0000 USDC |
| Entry fee under the stated assumption | 0.0560 USDC |
| **Total initial cash outflow** | **1.0560 USDC** |

The entry fee is `5 × 0.07 × 0.20 × (1 − 0.20) = 0.0560 USDC`.

### Net sale proceeds needed to realize +0.95

| Item | Amount |
|---|---:|
| Recovery of stake and entry cost (economic recovery, not a fee refund) | 1.0560 USDC |
| Additional net profit targeted | 0.9500 USDC |
| **Required sale proceeds after exit fees** | **2.0060 USDC** |

So the account cash flow is:

`net P&L = sale proceeds after exit fees − stake − entry fees`

`net P&L = 2.0060 − 1.0000 − 0.0560 = +0.9500 USDC`

This is the exact meaning of “+$0.95 net”. The 2.0060 USDC is the amount credited to the cash balance **after exit fees have already been deducted**. Gross sale proceeds would be higher by the exit fee.

With the same assumed 0.07 fee model, the modelled exit price that produces this example is approximately `0.418232`; the gross sale proceeds would be about `2.091160`, exit fees about `0.085160`, and net proceeds `2.006000`. These are equation outputs under the stated fee assumption, not a claim that a real order could fill at that price.

### Account balance walkthrough

| Stage | Cash balance |
|---|---:|
| Before the trade | 4.7700 USDC |
| After paying stake and entry fee | 4.7700 − 1.0560 = 3.7140 USDC |
| After sale, with 2.0060 USDC net proceeds | 3.7140 + 2.0060 = 5.7200 USDC |
| **Net change from starting balance** | **+0.9500 USDC** |

## What happens on a full-loss trade?

If the position expires worthless and there is no recovery from selling or settlement, the stake and entry fee are both lost. Under this example that is `−1.0560 USDC`, not merely `−1.00 USDC`.

Do **not** automatically label every trade that fails to hit the TP as a full-loss trade. In the historical replay rule “take profit if hit; otherwise hold to resolution”, a trade that misses the TP can still receive a settlement payout. Partial exits and other exit rules also produce different realized outcomes. The full-loss assumption applies only where the entire position and entry fee are lost.

## Simplified break-even win rate

If, and only if, every winning trade earns exactly `+0.9500 USDC` net and every losing trade loses exactly `−1.0560 USDC`, with no additional costs or other outcomes, the break-even win rate is:

`w × 0.95 − (1 − w) × 1.056 = 0`

`w = 1.056 / (0.95 + 1.056) = 0.52642… ≈ 52.64%`

Under this simplified binary payoff model:

- Above 52.64%: positive arithmetic expectancy before any omitted costs or execution errors.
- At 52.64%: break-even expectancy.
- Below 52.64%: negative arithmetic expectancy.

**This 52.64% threshold must not be compared directly with the historical 46.7% target-hit rate as though they were the same metric.** A target-hit rate measures how often the take-profit threshold was reached under a replay rule. It is not automatically the strategy win rate, and in the “otherwise hold to resolution” rule, non-hit trades do not all necessarily lose the full stake. Use the actual net P&L of every trade to calculate empirical expectancy.

## Fee and execution caveats

- The `0.07` rate is the assumption used by the described replay/prototype model. It must not be treated as a universal or permanent fee rate for every Polymarket market or order.
- The price used in the calculation is not a guaranteed fill price. Spread, depth, latency, partial fills, queue position, order type, and live fee rules can change the result.
- A target price appearing on a chart is not proof that the position could be sold in the required quantity at that price.
- Report gross sale value, exit fees, net sale proceeds, initial cash outflow, and final net P&L as separate fields wherever possible.

## Reproducibility status

The worked example is a transparent arithmetic illustration. The historical zone tables in `../data/` are transcribed from earlier author reports and have not been independently reproduced by this package. Their reported F45 expectancy was negative under both compared exit rules. No profitable edge is established by those tables.
