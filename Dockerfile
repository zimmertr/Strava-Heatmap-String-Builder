FROM python
WORKDIR /opt/app
COPY . /opt/app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]
