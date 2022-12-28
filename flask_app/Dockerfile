# syntax=docker/dockerfile:1
FROM python:3.6.7

WORKDIR flask_app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
