set -e
set -x

pytest --cov=src --cov-report=html src/tests "${@}"