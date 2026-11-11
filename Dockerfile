FROM python:3.15@sha256:8c9a3bf2d6dea60d60a2ae2a07c2b2fb1e7d8daed64b146b6792c74ae0d62ac4

# The base image lags Debian's security fixes, and the image scan refuses a
# fixable High. APP_COMMIT, which the release sets, changes on every build, and
# BuildKit keys a RUN on the build arguments in scope, so a layer cache can't
# freeze this layer and keep a fixed CVE out.
ARG APP_COMMIT=unknown
RUN apt-get update \
    && apt-get upgrade -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/app
COPY . /opt/app
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python", "main.py"]
