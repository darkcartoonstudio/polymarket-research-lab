# Visual prototype — read this first

`mechanism-100-100-visual-prototype.html` (French) and `mechanism-100-100-visual-prototype_EN.html` (English, same file, every label and script string translated, identical math) are a UI/interaction sketch submitted by the author to illustrate the aspiration of reaching a $1,000 balance through repeated zone entries and net-target exits. Download either one and open it in a browser — GitHub only displays the source code, it never runs the page.

**It is not a backtest, not a live trading report, and not evidence that the strategy wins.** The animated price path is hand-authored, not fetched from historical market data. The prototype transitions to a win when its synthetic path reaches the target; it does not represent a complete distribution of losing, expired, rejected, partially filled, or unresolved trades. The visible `$4.77` start, `$1,000` target, and repeated day counter are illustrative values and must not be interpreted as a verified account statement or timeline.

## Cash-flow accounting inside the animation

The prototype target is **+$0.96 net P&L**, after the modeled entry and exit fees. The amount subtracted from the cash balance at entry is `stake + entry fee`, not the stake alone. At sale, the amount credited is **gross sale proceeds minus the modeled exit fee**. The code solves for an exit price where:

`net sale proceeds − initial cash outflow = +0.96`

So the `+$0.96` label is not the total amount received at sale. The fee assumption in the prototype is `fee = shares × 0.07 × price × (1 − price)`; it is an illustrative model, not a guarantee of current applicable fees or a real fill. A fee is not literally refunded by the platform; it must be economically covered by the eventual net proceeds.

The main historical replay uses **+$0.95 net per $1 stake**, not +$0.96. Keep those values separate. The full +$0.95 worked cash-flow example and conditional 52.64% binary-payoff break-even calculation are in [`../docs/take-profit-accounting.md`](../docs/take-profit-accounting.md). The 52.64% threshold is not interchangeable with the historical target-hit rate, especially when a missed TP is followed by holding to resolution.

The prototype's price path is synthetic and hard-coded with successful exits. Its repeated wins must not be interpreted as a strategy result or a prediction of how long it would take to reach $1,000.

The next honest evolution would replace the synthetic trajectory with an explicitly chosen historical sample and show wins, losses, unresolved states, spread, fees, size/depth limits, and expectancy, with the dataset and calculations linked.
