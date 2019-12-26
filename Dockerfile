FROM python:3.7-slim-buster

ENV PYTHONUNBUFFERD 1

COPY ./requirements.txt /requirements.txt
RUN pip3 install --retries 20 --timeout 1000 -v -r  /requirements.txt 

RUN mkdir /app
WORKDIR /app

COPY ./app /app