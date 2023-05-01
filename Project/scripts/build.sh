
scripts_folder=$(pwd)/tmp

docker pull postgres

docker build -t projectpostgres-image .
exit