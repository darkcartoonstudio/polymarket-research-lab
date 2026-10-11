# Postmortem: a cloud collection that produced no data

## Incident summary

A cloud-based collection campaign failed to observe markets: **zero markets and zero entries were collected**. The logs pointed to a network-policy response (`403`) when attempting to reach Polymarket's live WebSocket endpoint. The report did not identify lack of budget as the cause.

## What this result means

It is evidence that the chosen environment could not reach the required feed under the configured network policy at that time. It is **not** evidence that the trading hypothesis worked or failed, because the campaign yielded no market sample.

## Diagnostic sequence

1. Validate DNS and TLS reachability from the same runtime where the collector runs.
2. Record the endpoint, status/error, timestamp, region/runtime type and retry behavior—without logging credentials.
3. Compare a simple read-only connectivity test with the production process.
4. Distinguish a remote service response from a local egress firewall or cloud platform policy.
5. Stop the campaign and mark it `infrastructure_blocked` rather than silently keeping it “running”.
6. On restart, confirm that fresh market discovery and stream payloads are actually arriving before counting the campaign as active.

## Research logging recommendation

Every campaign should report four independent states:

- **Infrastructure:** could the runtime connect to the data source?
- **Collection:** were fresh and valid records received?
- **Research sample:** were enough eligible observations and resolved outcomes accumulated?
- **Strategy evaluation:** was the predeclared hypothesis tested with valid metrics?

A run can succeed at one stage and fail at the next. Never let a healthy process status substitute for proof of collection completeness.

## What was deliberately not included

This note omits private host logs, account identifiers, deployment configuration and internal repository paths. Endpoint policies change, so diagnose the specific environment rather than assuming this failure is permanent.
