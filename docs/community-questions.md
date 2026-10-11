# Questions for the community

This project is shared to learn, not to market a profitable bot. Criticism is welcome, especially when it identifies a denominator, leakage path, execution assumption, or a more convincing baseline.

## Questions I am actively investigating

1. What is a defensible way to replay short-duration Polymarket order books when the public historical dataset contains only best ask or trades?
2. How should order-book imbalance be defined for a token book with rapidly changing depth? Which levels, normalization, and event timestamps should be used?
3. How can I guard against choosing a zone/threshold because it worked on the same sample where I discovered it?
4. What is the best practical walk-forward design for 5-minute markets with overlapping zones and repeated observations per market?
5. What cost components most often invalidate small-target prediction-market scalping: spread, dynamic fees, available depth, latency, adverse selection, partial fills, queue position, or settlement assumptions?
6. How should target-hit rate, net expectancy, drawdown and uncertainty be reported together for a strategy with rare large losses?

## What would make the research more useful

- A reproducible script and pinned input dataset, or a clear explanation of what cannot be reproduced.
- A test that could falsify the idea, not merely show it in the best light.
- A critique of the reported +$0.95 replay or the preliminary F400/imbalance lead using clearly defined metrics.
- Safer and more faithful order/fill-state accounting.

Please do not send private keys, wallet seed phrases, API tokens, or sensitive account data in issues.
