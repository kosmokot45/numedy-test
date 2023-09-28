FROM python:3.11

SHELL [ "/bin/bash", "-c" ]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /usr/src/numedy

COPY . .

RUN pip install -r requirements.txt