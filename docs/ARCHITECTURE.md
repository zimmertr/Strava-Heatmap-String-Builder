# Architecture

`main.py` is the whole program, and it makes no choices beyond its arguments.

1. It parses the options (`-s`, `-a`, `-c`, `-r`, `-t`, `-o`), which the README tables.
2. It builds the URL prefix: the Strava Heatmap server, activity, color and resolution, in either the default form or the OpenStreetMap form (`-o`), optionally with a `tms:` prefix (`-t`).
3. It asks for a Strava email and password, and passes them to the `stravacookies` package, which logs in and returns the cookie string. A failed login prints an error and exits with status 4.
4. It prints the prefix plus the cookie string, and the date seven days out, when Strava's cookies are about to expire.

Nothing is stored. The credentials and the URL exist only in the process.

The Dockerfile starts from a pinned `python` image, installs `requirements.txt` (`stravacookies`), copies the repo into `/opt/app`, and runs `python main.py`.
