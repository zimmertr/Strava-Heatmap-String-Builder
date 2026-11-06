# CI

Every PR to `main` runs these, all from zimmertr/yggdrasil's modules:

| Check | Does |
|---|---|
| `PR Title / PR Title` | Refuses a title that isn't `type(scope): summary` |
| `Lint / actionlint` | Lints the workflows |
| `Lint / zizmor` | Audits the workflows for unsafe patterns |
| `Lint / semgrep` | Refuses a Dockerfile `FROM` that has a tag but no digest |

Nothing builds the image or runs the script in CI. Do that locally in Docker ([CONTRIBUTING.md](../CONTRIBUTING.md)).

Dependabot proposes updates to the workflow pins, the Dockerfile's base image and `requirements.txt`, daily, after a release is three days old. A patch or minor update merges itself once the required checks pass (`Dependabot auto-merge`); a major waits for TJ.
