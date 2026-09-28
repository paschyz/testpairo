# testpairo

A throwaway sandbox repository used to test [pairo](https://github.com/paschyz/pairo) — an AI-powered pull request reviewer currently under development.

## What this repo is for

This repository holds no real project. It exists purely as a target for pairo:
a safe place to open pull requests, push intentionally flawed code, and watch how
the reviewer responds.

Typical uses:

- **Trigger reviews** — open a PR and confirm pairo picks it up and comments.
- **Test detection** — introduce bugs, style issues, or risky patterns on purpose
  and check what pairo catches (and what it misses).
- **Check false positives** — push clean, correct changes and verify the reviewer
  stays quiet instead of inventing problems.
- **Exercise the integration** — webhooks, permissions, comment formatting,
  re-reviews after new commits.

## What to expect here

- Code in this repo may be broken, incomplete, or deliberately wrong.
- Branches and pull requests are disposable and may be force-pushed or deleted.
- Nothing here is intended for reuse in other projects.

If you're looking for the actual reviewer, it lives at
[paschyz/pairo](https://github.com/paschyz/pairo).
