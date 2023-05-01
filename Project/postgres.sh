#!/bin/bash

postgres_folder=$(pwd)/postgres_data
scripts_folder=$(pwd)/tmp

docker pull postgres:latest
# start the postgres container
docker run -p 5432:5432 --name projectpostgres -e POSTGRES_PASSWORD=de300hardpassword -v "$(pwd):/tmp" -e "PGDATA=/var/lib/postgresql/data/pgdata" -d postgres:latest
docker build -t projectcontainer

docker run -d --name projectcontainer --link projectpostgres:projectpostgres -v $(pwd):/tmp projectcontainer:latest