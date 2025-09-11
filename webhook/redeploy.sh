#!/bin/sh
#cd "/home/log430/log430-a25-labo0"

echo "Get updates from git"
git fetch origin master
git reset --hard origin/master

echo "Build & deploy new image"
docker stop $(docker ps -q --filter ancestor=labo0-calculator:latest)
docker system prune -af --volumes
docker build -t labo0-calculator .
docker run -it labo0-calculator