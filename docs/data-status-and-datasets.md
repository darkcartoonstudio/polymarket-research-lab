# Data status and experiment register

## External historical dataset used by one report

- **Name:** `kachoio/polymarket-5-minute-crypto-up-down-markets`
- **URL:** https://github.com/kachoio/polymarket-5-minute-crypto-up-down-markets
- **License status:** the author's source report identified it as CC0. Check the dataset version and current license before reuse.
- **Reported population:** 15,682 markets; 324,048 simulated entries; 295,921 known outcomes.
- **Fields relevant to replay:** market identifiers/outcomes and historical best-ask contact information, as summarized in the research report.
- **Important gap:** not a complete time-stamped L2 order-book history. It cannot support a faithful queue, partial-fill, or full-depth replay.
- **Public reproduction status:** summary tables only; raw dataset and original replay code are not bundled, so the tables are not independently reproduced by this repository.

## Private/collected data

Earlier collection reports described separate runs: an initial ~10.83-hour campaign with 621 retained entries, and a ~20.92-hour campaign with 5,149 unique entries and 7,098 zone rows. These reports have different eligibility criteria and denominators. They must not be merged as if they were one continuous sample.

Later work notes report a large L2 snapshot archive of approximately 1.7 million snapshots and an exploratory imbalance threshold combination. That summary is not independently auditable from the files published here yet. No raw account logs, private account identifiers, credentials, private configuration, or full private databases are included in this repo.

## CSV summaries

See [`../data/`](../data/) for the aggregate target-hit and expectancy tables transcribed from the historical report. They are designed to make the reported results inspectable without publishing all private source code. See [`data/README.md`](../data/README.md) for caveats.

## Minimum manifest to add for a future reproducible release

For each data file/run, publish (when legally and ethically shareable):

- source URL and dataset version/date retrieved;
- license and redistribution permission;
- SHA-256 checksum;
- time range, market universe, and timezone;
- row counts at each processing stage;
- field dictionary and units;
- excluded-row categories and reason codes;
- target labels, fee function, order-side assumption, and decision timestamp;
- script/commit that produced each table;
- exact command to reproduce outputs;
- what cannot be reconstructed (e.g., missing order-book depth or unknown fills).

Never publish private account traces or secrets merely to make an experiment reproducible. Prefer public data, synthetic fixtures, aggregated results, or redacted examples.
