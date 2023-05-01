#!/bin/bash

echo "psql create entered"
PGPASSWORD=de300hardpassword
psql -U postgres -f scripts/create_db.sql
psql -U postgres -d heart -f scripts/create_tables.sql

psql -U postgres -d heart -f scripts/import_csv.sql