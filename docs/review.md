# Connect Claude Code to CareBud

The repository includes one workflow named **CareBud PR review**. It uses a Claude subscription token with the workflow's built-in GitHub token. The unit reviewer needs one Claude credential for this repository.

1. Open a terminal and run `claude setup-token`. Sign in with the Claude account that has Pro and approve in your browser.
2. Open [CareBud's new Actions secret](https://github.com/aly570/CareBud/settings/secrets/actions/new). Name it `CLAUDE_CODE_OAUTH_TOKEN` and paste the generated token directly into the secret value. Keep it out of chat, PRs and source files.
3. Open the first completed unit as a ready PR. Under **Checks**, look for **Claude unit review**, then check the verdict comment and commit ID. If you added the secret after an initial failure, re-run the job in Actions.

The command is documented in [Claude Code authentication](https://code.claude.com/docs/en/authentication). The action accepts a subscription token as described in [Anthropic's GitHub setup](https://code.claude.com/docs/en/github-actions).

## Review budget and merge

All reviews share one Claude Pro usage limit, so the workflow reviews each PR once when it becomes ready, not on every push. It uses Sonnet, an eight-turn cap and read-only access to the diff. Draft PRs are skipped. A missing credential, rate limit, invalid result or changes-needed verdict cannot produce a passing check.

To keep reviews cheap:

1. Keep the PR in draft while building and fixing. Mark it ready only after the unit check passes and the evidence is in the PR.
2. After a changes_needed verdict, convert to draft, push all fixes together, then mark ready again. That starts exactly one new review.
3. Keep one unit per PR. Smaller diffs cost less and get better reviews.
4. Before merging, check that the verdict comment names the PR's latest commit. A push after the verdict is not reviewed until the PR is marked ready again.

Teammates do not need a Claude account. They need Write access to this repository, because reviews refuse PRs from forks. If the subscription reaches its usage limit, retry when it resets. Claude can read the review packet and produce findings; the team handles pushes, fixes and merges.

The repository owner can require **Claude unit review** for `main` under Settings → Branches when the account plan supports private branch protection. Otherwise the team checks the latest verdict before using Merge. Semantic clinical sign-off stays with the human reviewer.
