#!/bin/bash
set -e

BENCH_FOLDER="${BUNCH_NAME}:-bench"

# Initialization scripts
bench init frappe-bench --frappe-branch version-14 --no-redis --no-backups --skip-assets

cd frappe-bench

bench new-site dev.localhost --admin-password admin --mariadb-root-password root

bench get-app ferum_customs --source-path /workspace
bench --site dev.localhost install-app ferum_customs

echo "[Info Bundle] Will run tests..."
pytest --app ferum_customs

exec "$@"
