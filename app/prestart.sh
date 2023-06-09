#! /usr/bin/env bash

# Let the DB start.
python src/backend_pre_start.py

# Run migrations.
alembic upgrade head

# Create initial data in DB if need.
if [ "$INITIAL_TEST_DATA" = "True" ]; then
    python src/initial_data.py
else
    echo "Initial test data not required."
fi
