# Security Policy

## Supported Versions

There are no versions. `main` is the supported code, and a fix ships as the next merge.

## Reporting a Vulnerability

Please report vulnerabilities privately through GitHub:
[Report a vulnerability](https://github.com/zimmertr/Strava-Heatmap-String-Builder/security/advisories/new).
Do not open a public issue for security problems.

Include what you found, where it lives (file or workflow), and how to reproduce it.

What to expect:

- **Acknowledgement** within a few days. This is a one-person project, so response times are best effort.
- **Fix**: a confirmed vulnerability is fixed in the next merge.
- **Credit** in the advisory, unless you'd rather not.

## Scope

In scope: `main.py`, the Dockerfile and the CI workflows. The script handles Strava credentials only in memory.

Out of scope: the Python packages and base image it depends on. Report issues in those to their maintainers.

There is no bounty program. Reports are still appreciated.
