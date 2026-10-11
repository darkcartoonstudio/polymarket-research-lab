# Publish this clean research repository

For a complete ready-to-copy Claude Code prompt, see [`CLAUDE_PUBLISH_PROMPT.md`](CLAUDE_PUBLISH_PROMPT.md).

The GitHub connection available in this session can read repositories and write files to existing repositories, but it does not expose a repository-creation or visibility-setting operation. Therefore this package has **not** been pushed or made public by this workflow.

## Create the new repository

1. Open https://github.com/new while signed in as `darkcartoonstudio`.
2. Set repository name to `polymarket-research-lab`.
3. Use this description: `A trader's public research journal: Polymarket BTC 5m zone micro-scalping, L2 data, execution realism, experiments, failures, and an unproven $1,000-balance dream.`
4. Select **Public**.
5. Do **not** initialize it with a README, `.gitignore`, or license; those are already included in this package.
6. Create the repository. Do not change the visibility of any existing private repository.

## Push from Windows PowerShell

Unzip the archive, open PowerShell in the `Polymarket-Research-Lab` folder, and run:

```powershell
git init
git add .
git commit -m "Publish initial research notes"
git branch -M main
git remote add origin https://github.com/darkcartoonstudio/polymarket-research-lab.git
git push -u origin main
```

If Git asks you to authenticate, use Git Credential Manager or the official GitHub sign-in flow. Do not paste access tokens or private keys into this repository or into chat.

## Before announcing it

- Verify the repository URL and make sure the visibility is Public.
- Check that both SVGs render in the README.
- Review the README's caveat that reported numbers have not been independently reproduced in this public package.
- Keep the original implementation repositories private until their complete Git history has been audited and any potentially exposed credentials have been rotated.


## Final review of the story and research claims

Before publishing or reposting the project:

- Keep the $1,000 balance goal framed as a personal aspiration, not a promise, deadline, or $1,000/day claim.
- Keep the historical +$0.95 net-profit replay separate from the visual prototype's +$0.96 net-profit parameter.
- Explain that +$0.95 net is profit after recovering the $1 stake and covering entry fees; in the $1 stake / 0.20 entry example, the fee is $0.056, total cash outflow is $1.056, and required sale proceeds after exit fees are $2.006.
- State that the 52.64% break-even rate applies only to the simplified binary payoff (+$0.95 for every win, −$1.056 for every full loss); do not compare it directly with target-hit rates or use it as the threshold for hold-to-resolution outcomes.
- Do not describe the 58.9% F400/imbalance figure as a validated win rate; it is an unverified research lead until the underlying export, denominator, label, and holdout evaluation are added.
- Keep reported metrics labelled as author-reported unless the run is reproduced from a pinned public dataset and code.
- Do not call the approach profitable or a validated edge while the available reports show negative expectancy in the historic replay.
