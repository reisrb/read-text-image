FROM python:3.8-slim

COPY requirements.txt /opt/read-text/requirements.txt
WORKDIR /opt/read-text/

RUN pip3 install -r requirements.txt

COPY . /opt/read-text/

ENTRYPOINT ["python3", "main.py"]
