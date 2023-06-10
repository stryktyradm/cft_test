#! /usr/bin/env bash

source scripts/test_env_vars.sh

docker run --name test_postgres -e POSTGRES_USER=$POSTGRES_USER -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD -e POSTGRES_DB=$POSTGRES_DB -p 5432:5432 -d postgres

echo "Started testing DB."

python src/tests_pre_start.py

alembic upgrade head

bash ./scripts/test.sh "$@"

docker stop test_postgres

docker rm test_postgres
