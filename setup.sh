#!/bin/bash

set -e

echo "🔧 Создание виртуального окружения..."
python3 -m venv venv
source venv/bin/activate

echo "📦 Установка зависимостей..."
pip install -r requirements.txt
pip install -r dev-requirements.txt
pip install pytest black ruff openai

echo "🧱 Установка frappe-bench..."
pip install frappe-bench
bench init frappe-bench --frappe-branch version-14 --no-redis --no-backups --skip-assets

echo "📁 Подключение проекта..."
cd frappe-bench
bench new-site ferum.local --no-mariadb-socket --admin-password admin --db-name ferumdb --db-root-password root --mariadb-root-password root
bench get-app ferum_customs ../
bench --site ferum.local install-app ferum_customs

echo "✅ Установка завершена. Запустить сервер: bench start"
