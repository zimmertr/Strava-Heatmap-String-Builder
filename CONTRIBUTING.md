# Contributing

Changes come through PRs that TJ reviews.

1. Branch from the latest `main`.
2. Make one change per PR, and title it `type(scope): summary`, such as `feat(main): add a color`.
3. Open the PR. `PR Title`, the three `Lint` checks and `Docker Build` run on it, and a dry run of the release names the version the merge would ship ([docs/CICD.md](docs/CICD.md)).
4. Update the `docs/` page that owns the topic in the same PR, and add a decision record when the PR makes a decision.

Every merge to `main` releases the image to Docker Hub, and the PR title sets the bump.

Build and run it in Docker, so nothing installs on your machine:

```shell
docker build -t strava-heatmap-string-builder:dev .
docker run --rm strava-heatmap-string-builder:dev --help
docker run -it --rm strava-heatmap-string-builder:dev
```

The last command asks for a Strava email and password. Strava disables an account that logs in too many times, so use a throwaway account and don't run it in a loop.

There are no tests yet.
