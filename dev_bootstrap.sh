#!/bin/bash
set -e

APP_NAME="ferum_customs"
SITE_NAME="${SITE_NAME:-dev.localhost}"
FRAPPE_BRANCH="${FRAPPE_BRANCH:-version-15}"
BENCH_DIR="${BENCH_DIR:-frappe-bench}"
APP_PATH="$(pwd)"

if [ ! -d "$BENCH_DIR" ]; then
    bench init "$BENCH_DIR" --frappe-branch "$FRAPPE_BRANCH" --skip-assets
fi

cd "$BENCH_DIR"

if ! bench --site "$SITE_NAME" ls >/dev/null 2>&1; then
    bench new-site "$SITE_NAME" \
        --admin-password "${ADMIN_PASSWORD:-admin}" \
        --mariadb-root-password "${MYSQL_ROOT_PASSWORD:-root}"
fi

if ! bench list-apps | grep -q "$APP_NAME"; then
    bench get-app "$APP_NAME" --source-path "$APP_PATH"
    bench --site "$SITE_NAME" install-app "$APP_NAME"
fi

bench start
