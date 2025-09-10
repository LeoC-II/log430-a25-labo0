#!/bin/sh
cd "/home/log430/log430-a25-labo0"

echo "Get updates from git"
git fetch --all
git pull

echo "Build & deploy new image"
docker compose up --build --remove-orphans
docker system prune -af --volumes