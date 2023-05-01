# start the postgres container1
docker run -p 5432:5432 --name projectpostgres -e POSTGRES_PASSWORD=de300hardpassword -v "$(pwd):/tmp" -e "PGDATA=/var/lib/postgresql/data/pgdata" -d projectpostgres-image
while ! docker container ls | grep projectpostgres > /dev/null; do
  sleep 1
done

echo "Container is now running"
