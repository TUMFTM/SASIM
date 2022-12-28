#!/bin/bash

echo "killing old docker processes"
sudo docker compose rm -fs

echo "building docker containers"
sudo docker compose up --build -d