FROM python:3.15@sha256:8c9a3bf2d6dea60d60a2ae2a07c2b2fb1e7d8daed64b146b6792c74ae0d62ac4
WORKDIR /opt/app
COPY . /opt/app
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python", "main.py"]
