# syntax=docker/dockerfile:1
FROM python:3.10.7-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR flask_app
COPY requirements.txt .
RUN pip install --upgrade pip --no-cache-dir -r requirements.txt
COPY . .
