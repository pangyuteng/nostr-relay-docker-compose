FROM docker.io/library/python:3.8.16-slim-bullseye

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /opt/flask
COPY . /opt/flask
