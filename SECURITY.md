# Security policy and publication boundary

This repository is intended for public research notes and original diagrams only.

## Never publish

- Private keys, seed phrases, API secrets, HMAC secrets, access tokens or `.env` contents.
- Wallet addresses or account identifiers unless deliberately reviewed and necessary.
- Raw logs or databases that can contain private account, order, or infrastructure information.
- Unknown binaries, password-protected archives, compiled executables, or vendor DLLs.
- Internal deployment configuration and unreviewed commit-history dumps.

## Reporting an exposure

If you find a credential or sensitive record, do not reproduce it in an issue or pull request. Contact the maintainer privately through the account's available GitHub contact path. If a secret was ever committed to a repository, deleting the latest file is insufficient: revoke/rotate the secret and audit or clean the full Git history. Treat the credential as exposed until confirmed otherwise.

## Scope

This repository is not a live-trading bot and does not accept production credentials. Security reports should describe the affected file/path and the risk without attaching secrets.


## Additional public-research rule

Do not add account screenshots, wallet-linked trade exports, unredacted order/trade IDs, private account balances, or a demo that visually implies guaranteed profits unless the visual is clearly labeled as synthetic. The included prototype is explicitly disclosed as synthetic and is not evidence. Rotate any secret that may ever have entered Git history; deleting the current file is not enough.
