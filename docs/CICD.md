# CI

Every PR to `main` runs these, all from zimmertr/yggdrasil's modules:

| Check | Does |
|---|---|
| `PR Title / PR Title` | Refuses a title that isn't `type(scope): summary` |
| `Lint / actionlint` | Lints the workflows |
| `Lint / zizmor` | Audits the workflows for unsafe patterns |
| `Lint / semgrep` | Refuses a Dockerfile `FROM` that has a tag but no digest |
| `Docker Build / Docker Build` | Lints the Dockerfile, builds the image (not pushed), posts a Trivy table, runs the smoke test, and fails on any fixable Critical or High |
| `Release / Build & Push (<image>)` | On a PR, a dry run: the job summary names the version the merge would release. Nothing is pushed |

The smoke test is in `pr.yml`.

## Release

Every merge to `main` releases. GitVersion reads the bump from the squash commit's title (`feat` is a minor, `fix` a patch, `!` a major). The release module pushes `ghcr.io/zimmertr/strava-heatmap-string-builder:<version>`, scans it, then tags and releases the commit. The push uses the job's own `GITHUB_TOKEN`.

Renovate proposes updates to the workflow pins, the Dockerfile's base image and `requirements.txt`, once a release is seven days old. `.github/renovate.json` extends zimmertr/yggdrasil's shared preset (its record 0056), and yggdrasil's own modules don't wait. Everything below a major merges itself once the required checks pass; a major waits for TJ.
