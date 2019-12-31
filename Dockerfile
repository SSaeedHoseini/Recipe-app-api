FROM python:3.7-alpine

ENV PYTHONUNBUFFERD 1

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client 
RUN apk add --update --no-cache -virtual .tmp-build-deps \
    gss libc-dev linux-headers postgresql-dev

RUN pip3 install -r  /requirements.txt 

RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app

COPY ./app /app