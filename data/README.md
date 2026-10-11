# Public aggregate tables

These CSVs transcribe selected aggregate results from the author's historical research reports. They are **not raw market data and have not been independently reproduced by this public package**.

- `historical-replay-target-hit.csv`: reported **net TP target-touch** counts and percentages by zone for +$0.95, +$0.85, and +$0.75. The `hit_net_095_*` columns count target touches, not all profitable trades under the hold-to-resolution fallback.
- `historical-replay-expectancy.csv`: reported expectancy for target-if-hit/otherwise-hold and always-hold.
- `take-profit-cashflow-example.csv`: the worked $1 stake / 0.20 entry / +$0.95 net cash-flow example and its conditional break-even arithmetic.

## What the +0.95 net target means

For a $1.00 stake entered at 0.20, the example fee formula gives 0.0560 USDC entry fees. Initial cash outflow is 1.0560 USDC. The trade reaches +0.95 net only when sale proceeds after exit fees reach 2.0060 USDC (`2.0060 − 1.0000 − 0.0560 = +0.9500`). The $0.95 is net profit, not the amount received by the sale. See [`../docs/take-profit-accounting.md`](../docs/take-profit-accounting.md) for the formula and exit-fee treatment.

## Interpretation rules

1. These results use a specific replay rule and dataset, with best ask as entry proxy, $1 stake, assumed fee rate 0.07, no stop loss, 120-second cutoff, and first contact per market/zone/side.
2. The underlying source did not provide complete historical L2 depth; they are not a faithful L2 execution simulation.
3. Some zones overlap (e.g., fine bands and aggregate bands). Do not add their counts together as though the entries were disjoint or independent.
4. The +$0.95 figure is net profit after recovering the stake and covering applicable costs; it is not the total sale proceeds, not an exit price, and not a forecast.
5. A target-hit rate is not automatically a strategy win rate, and neither one is expectancy. The companion report was negative in all 20 zones under both tested exit rules.
6. The exact dataset snapshot, filters, and calculation code must be pinned before calling these figures independently reproducible.
