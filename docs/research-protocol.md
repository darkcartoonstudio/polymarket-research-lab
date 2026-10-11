# Research protocol

This protocol is the default standard for claims in this repository. It is deliberately stricter than “the backtest looks good”.

## 1. State the hypothesis before running the test

Record the market population, observation window, signal/entry rule, side, price band, stake, exit rule, cutoff, fee model, and primary metric before examining outcomes. Keep exploratory analyses labelled exploratory.

## 2. Separate the questions

- **Data validity:** are timestamps, market IDs, book states, fees, and final outcomes correct and complete?
- **Prediction (O1):** does a forecast match the official market resolution?
- **Execution (O2):** could the intended order have filled at the assumed price and quantity?
- **Trading expectancy:** after fees and the full exit/settlement rule, is average net P&L positive?
- **Operational reliability:** were feeds fresh, state synchronized, and every position reconciled?

Passing one layer never implies the next one passes.

## 3. Prevent leakage

1. Split chronologically, not randomly, when market conditions or features evolve through time.
2. Choose features and thresholds on the training period only.
3. Use validation for model/threshold selection and keep the test set untouched until final evaluation.
4. For live-like testing, use walk-forward folds and report each fold, not only a pooled average.
5. Fit calibration on a separate calibration set; never calibrate on the final test set.
6. Ensure every feature was available at the recorded decision timestamp. Never use post-resolution data to construct an entry signal.

## 4. Model execution costs honestly

At minimum, document spread, fee schedule, entry side, exit side, order type, stake size, displayed depth, slippage, partial fills, rejected/expired orders, and latency assumptions. Apply fees at both entry and exit when applicable. If the source has only best bid/ask, say so and do not call it a full L2 execution replay.

For live event reconstruction, differentiate order acknowledgement from a matched and confirmed trade. Reconcile positions against trade/fill records and balances; do not infer a fill from an accepted response alone.

## 4A. Keep take-profit accounting explicit

Define the target in terms of **net P&L**, and separately record (1) stake, (2) entry fees, (3) initial cash outflow, (4) gross sale/settlement proceeds, (5) exit fees, (6) net proceeds after exit fees, and (7) final net P&L. Under the example used in this repository, a 1.00 USDC stake bought at 0.20 incurs 0.0560 USDC entry fees; the initial cash outflow is 1.0560 USDC. For +0.95 net, sale proceeds after exit fees must be 2.0060 USDC. See [`take-profit-accounting.md`](take-profit-accounting.md).

The simplified 52.64% break-even rate assumes every win is +0.95 and every loss is −1.056. Do not apply it blindly to a rule where entries that miss the TP are held to market resolution; those trades may have settlement payouts other than zero. Never use target-hit rate as a substitute for the final trade win rate or net expectancy.

## 5. Report more than win rate

Depending on the question, include:

- sample count and exclusions;
- hit rate with a confidence interval;
- mean and median net P&L per entry;
- expectancy, payoff ratio, max drawdown, and tail loss;
- calibration curve, Brier score, or log loss for probability models;
- coverage and abstention rate;
- performance by time period/regime and per walk-forward fold;
- missing-data rate, feed staleness, crossed-book rate, and unresolved outcomes.

Always show denominators. A 12/22 result is an early observation, not proof of an edge.

## 6. Handle missing or invalid data explicitly

Keep separate counts for collected rows, valid rows, excluded rows, outcomes known, outcomes unresolved, and markets omitted. Never silently drop invalid crossed books or stale observations. Publish exclusion rules and repeat key results with/without borderline records if material.

## 7. Predefine stop criteria

Examples: pause a data run when a price feed becomes stale; stop opening new positions if the local book is incomplete; disallow entries whose modeled immediate exit already breaches the hard loss limit; apply a cooldown after a stop to avoid repeated identical re-entry. These are risk controls, not evidence of profitability.

## 8. Minimum claim language

- **Observed:** directly recorded in a named session/dataset.
- **Exploratory:** a pattern seen during hypothesis generation.
- **Backtested:** evaluated on a specified historical dataset under declared assumptions.
- **Out-of-sample tested:** evaluated on time-separated data not used to choose the method.
- **Live-observed:** recorded on a live market, but not necessarily a real-money trade.
- **Validated edge:** reserve this phrase for evidence with a robust, reproducible positive net expectancy after realistic execution costs and independent out-of-sample validation.

Do not call an experimental score “confidence” unless calibration supports a probability interpretation.
