# Research status and progress log

**Snapshot date:** 2026-10-11. This is a summary of reports reviewed for the public research package; it is not a live system-health report.

## Status by workstream

| Workstream | What has been done | Current status | What is still missing |
|---|---|---|---|
| Multi-source directional observer | Market discovery, short-market lifecycle tracking, price/reference feeds, candles, database logging, alerting, final-resolution analysis | Prototype/research | Reproduce all claims from version-pinned code and datasets; larger chronological validation; current continuous score is not validated in the reviewed snapshot |
| Zone-based BTC micro-scalping | Price bands, entry logs, zone summaries, target-touch replay, hold-vs-TP expectancy | Historical exploratory study | Full-L2 replay, exact reproducible pipeline, out-of-sample validation, realistic fills and costs |
| Order-book state handling | Snapshot/delta reasoning, freshness watchdogs, reconnection and REST resynchronization ideas, crossed-book handling | Technical lessons documented | Re-verify against current feed/SDK contract; publish isolated public fixtures/tests without private configuration |
| Virtual/paper execution | Position/P&L components, fill-state distinction, stop/re-entry safeguards discussed and tested in reports | Limited experiments | Broader controlled sessions, validated fill model, no claims of profitable live execution |
| Order-book imbalance | A later working note reports a promising threshold combination | Exploratory and unaudited in this package | Exact records, denominator, feature timestamp, threshold-selection protocol, uncertainty and held-out validation |
| Automated live trading | The long-term aspiration exists | **Not validated / not claimed** | Positive robust expectancy, operational risk controls, independent out-of-sample evidence, and sustained monitoring |

## Quantitative evidence available in the reviewed reports

### Historical replay

- 15,682 five-minute markets.
- 324,048 simulated entries; 295,921 with known outcomes.
- $1 stake; best-ask entry proxy; fee rate assumption 0.07; no stop; 120-second cutoff; first contact per market/zone/side.
- Best reported +$0.95 target-hit band: F45 (0.45–0.50) with 11,297/24,210 = 46.7%.
- F45 reported expectancy: −$0.0719 under target-if-hit/otherwise-hold; −$0.0588 under always-hold.
- The companion report said all 20 zones were non-positive under both rules.
- Limitation: no full historical L2 depth; results are reported by author and not independently reproduced by this public package.

### TP cash-flow convention (important for interpreting every target result)

The primary historical target means **+$0.95 net P&L**, not $0.95 total sale proceeds. Under the example at entry 0.20 with a $1 stake, entry fee 0.0560 makes the initial cash outflow 1.0560 USDC. Required sale proceeds are 2.0060 USDC after exit fees, giving `2.0060 − 1.0560 = +0.9500` net. If the position settles worthless, the corresponding full loss is −1.0560 USDC under these assumptions.

The binary payoff break-even rate would be `1.056 / (1.056 + 0.95) = 52.64%` **only if every win is +0.95 and every loss is −1.056**. It must not be confused with the target-hit rate: in the historical “TP if hit, otherwise hold to resolution” rule, a target miss is not automatically a full loss. Full details: [`take-profit-accounting.md`](take-profit-accounting.md).

### Early collection campaign (separate sample)

- 10.83 hours; 663 candidate rows; 621 retained entries; 42 crossed/invalid book cases excluded in the report.
- Best reported F40: 12/22 (54.5%). The denominator is small and this result is not evidence of a durable advantage.

### Separate fine-band campaign (not poolable with the above)

- About 20.92 hours; 5,149 distinct entries; 7,098 zone rows.
- Report counted 4,964 decided outcomes and 2,204 wins (44.4%) under that report's own labeling.
- One market can correspond to multiple zone rows; sample definition differs from the historical target replay.

### Exploratory L2 imbalance lead

Working notes reported approximately 1.7 million order-book snapshots, about 49.5% for a static condition, and around 58.9% for a combination of F400 (0.40–0.425) with imbalance >0.7942. The present package does not yet include a source export or enough methodological detail to audit this. This is a research lead, not a verified metric or profitability claim. Do not use it as a live signal until reproduced on a holdout period.

### Direction-model validation

A report snapshot dated 2026-07-28 described 777 markets in a training/test split (543 train, 234 test) and varying performance by signal bucket. A separate short live observation had only seven complete markets. A later audit of the continuous `raw_signal`/`prob_up_bot`/`edge_gap` action score found no historical replay or walk-forward validation for that continuous score in the reviewed codebase. These counts/results relate to a separate direction-prediction track, not the zone replay.

## Research state labels

- **Reported:** transcribed from a prior report; not reproduced here.
- **Exploratory:** observed during hypothesis generation; may reflect selection effects.
- **Backtested:** run on a named dataset under specified assumptions.
- **Out-of-sample:** evaluated on chronological data not used to select features/thresholds.
- **Live-observed:** recorded from a live feed; does not necessarily mean a real-money trade or real fill.
- **Validated edge:** not claimed by this project at this time.

## Next milestones

1. Freeze and version the target, exact zones, imbalance formula, decision timestamp, and exit rules.
2. Obtain/pin the source dataset and write checksums, exclusions, and a single-command reproduction path.
3. Re-run the target replay and independent expectancy calculator; verify every denominator and fee formula.
4. Build a historical-L2 replay including executable side, depth, partial fills, spread, latency and order-type behavior.
5. Predeclare chronological train/validation/test and walk-forward folds; report confidence intervals and sensitivity to parameters.
6. Audit the F400 + imbalance lead on untouched data.
7. Continue paper/virtual observation; do not infer profitability from small samples.
