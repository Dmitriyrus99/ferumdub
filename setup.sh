#!/bin/bash

set -e

echo "🔧 Starting setup for ERPNext 15..."

sudo apt-get update
sudo apt-get install -y git python3-dev python3-pip python3-venv mariadb-server redis-server nodejs npm yarn curl

pip3 install frappe-bench

bench init frappe-bench --frappe-branch version-15
cd frappe-bench

bench new-site ferum.local
bench get-app ferum_customs
bench --site ferum.local install-app ferum_customs

bench start
