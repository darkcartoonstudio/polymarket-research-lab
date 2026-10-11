# Calibrate probabilities before turning scores into actions

## Two distinct objectives

The author's separate observer/model project worked with short-window UP/DOWN markets and multiple market/price inputs. The useful design principle is to separate:

- **O1 — direction prediction:** compare a forecast with the official final market direction.
- **O2 — virtual trading:** test whether a defined entry/exit sequence produces positive net P&L after costs.

A high O1 score cannot compensate for an unfillable O2 entry. Positive simulated trading P&L cannot validate a probability model if the replay uses future information or unrealistic fills.

## A numeric score is not automatically a probability

A weighted combination of moving-average classifications, distance to a reference price, momentum, velocity, exchange alignment, and market-signal categories can be transformed through a sigmoid. That gives a number between zero and one—but not necessarily a calibrated probability.

If a model says “80%”, then among comparable predictions assigned 80%, the outcome should occur approximately 80% of the time on genuinely unseen data. This must be tested with reliability diagrams, proper scoring rules such as Brier score or log loss, sufficient sample size, and time-separated evaluation.

## What the reviewed experiment established—and did not

A report dated 2026-07-28 found that the continuous score used by one model version (`raw_signal` → `prob_up_bot` → `edge_gap`) had not been historically replayed or walk-forward validated in that reviewed codebase. It also noted that the displayed “confidence” was a transformation of the score, rather than a demonstrably calibrated probability. Some **discrete** signal buckets had separate historical analysis, but that does not validate the continuous score or its action thresholds.

A separate live observation report counted only seven complete markets in one short test. Such a small count is an operational observation, not proof of a durable predictive edge. Results varied by signal bucket and evaluation sample; apparently excellent historical bucket rates were not stable evidence by themselves.

These reports are snapshots from a particular experimental version, not statements about all current model variants.

## Recommended validation sequence

1. Freeze the feature formula and the exact decision timestamp.
2. Reconstruct features only from information available at that timestamp.
3. Split chronologically into training, validation, and untouched test periods.
4. Compare against meaningful baselines (for example market-implied direction and a majority-class baseline).
5. Measure calibration, discrimination, uncertainty, and abstention—not just accuracy.
6. Use walk-forward folds to test time and regime stability.
7. Evaluate O2 separately with realistic bid/ask, fees, depth, latency, partial fills, exit logic, and settlement.
8. Keep live observation and real-money performance clearly distinguished.

## Suggested reporting table

| Layer | Question | Useful metrics |
|---|---|---|
| Data | Was each market correctly timestamped and resolved? | Missing/stale rate, label audits, excluded rows |
| Prediction | Were probability forecasts calibrated and discriminative? | Brier score, log loss, reliability curve, AUC/accuracy with intervals |
| Execution | Could the orders plausibly fill? | Fill rate, slippage, depth coverage, latency, partial fills |
| Trading | Did positions earn money net of every cost? | Expectancy, drawdown, payoff distribution, tail loss |
| Robustness | Does the result persist over time? | Walk-forward folds, regime/time stability, sensitivity analysis |

## Core lesson

Do not turn a model's score into a live “ENTER UP/DOWN” instruction until the score, decision threshold, and actual execution strategy have each passed their own validation. It is acceptable—and often correct—for the system to abstain when the evidence is insufficient.
