#!/bin/bash

set -e

APP_NAME="ferum_customs"
SITE_NAME="dev.localhost"
APP_PATH="/workspace/ferumdub"  # путь до вашего репозитория в окружении
FRAPPE_BRANCH="version-14"

echo "📦 Установка Bench CLI..."
pip install frappe-bench

echo "📁 Инициализация Bench окружения..."
bench init frappe-bench --frappe-branch $FRAPPE_BRANCH
cd frappe-bench

echo "🌐 Создание сайта $SITE_NAME..."
bench new-site $SITE_NAME --admin-password admin --mariadb-root-password root

echo "🔗 Подключение кастомного приложения $APP_NAME..."
bench get-app $APP_NAME --source-path $APP_PATH

echo "📥 Установка приложения $APP_NAME в сайт $SITE_NAME..."
bench --site $SITE_NAME install-app $APP_NAME

echo "🧪 Запуск тестов..."
bench --site $SITE_NAME run-tests --app $APP_NAME
