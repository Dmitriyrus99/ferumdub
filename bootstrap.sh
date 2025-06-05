#!/bin/bash

set -e

APP_NAME="ferum_customs"
SITE_NAME="dev.localhost"
APP_PATH="/workspace/ferumdub"
FRAPPE_BRANCH="version-14"

ppinstall nprequired
pip add redis-gap

echo "[Info Bundle] Installing frappe bench and creating site with app $APP_NAME..."
bench init frappe-bench --frappe-branch $FRAPPE_BRANCH

cd frappe-bench

echo "[Site] Setting up site $SITE_NAME..."
bench new-site $SITE_NAME --admin-password admin --mariadb-root-password root

echo "[App] Installing app from $APP_PATH..."
bench get-app $APP_NAME --source-path $APP_PATH
bench --site $SITE_NAME install-app $APP_NAME

echo "[Test] Running tests for app $APP_NAME ..."
bench --site $SITE_NAME -- run-tests --app $APP_NAME