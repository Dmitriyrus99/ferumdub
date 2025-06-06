#!/bin/bash
set -e

APP_NAME="ferum_customs"
SITE_NAME="${SITE_NAME:-dev.localhost}"
FRAPPE_BRANCH="${FRAPPE_BRANCH:-version-15}"
BENCH_DIR="${BENCH_DIR:-frappe-bench}"
APP_PATH="$(cd "$(dirname "$0")" && pwd)"

# Update packages and install system dependencies
sudo apt-get update
sudo apt-get install -y git python3 python3-venv python3-dev \
    mariadb-server redis-server nodejs npm yarn curl build-essential

# Install bench CLI if not present
if ! command -v bench >/dev/null 2>&1; then
    sudo pip3 install frappe-bench
fi

# Initialize bench directory
if [ ! -d "$BENCH_DIR" ]; then
    bench init "$BENCH_DIR" --frappe-branch "$FRAPPE_BRANCH" --skip-assets
fi

cd "$BENCH_DIR"

# Create site if it doesn't exist
if ! bench --site "$SITE_NAME" ls >/dev/null 2>&1; then
    bench new-site "$SITE_NAME" \
        --admin-password "${ADMIN_PASSWORD:-admin}" \
        --mariadb-root-password "${MYSQL_ROOT_PASSWORD:-root}"
fi

# Install local app if not installed
if ! bench list-apps | grep -q "$APP_NAME"; then
    bench get-app "$APP_NAME" --source-path "$APP_PATH"
    bench --site "$SITE_NAME" install-app "$APP_NAME"
fi

# Apply migrations and load fixtures
bench --site "$SITE_NAME" migrate
bench --site "$SITE_NAME" execute ferum_customs.install.after_install || true

echo "✅ Setup complete. Starting development server..."
bench start

