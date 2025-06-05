FROM python:3.10-slim

# Установка зависимостей (включая cron)
RUN apt-get update && apt-get install -y \
    git \
    mariadb-client \
    redis-server \
    nodejs \
    npm \
    curl \
    cron \
    && npm install -g yarn@1.22.19

# Создание пользователя frappe с домашним каталогом
RUN useradd -ms /bin/bash frappe

# Переключение на пользователя frappe
USER frappe
WORKDIR /home/frappe

# Установка bench и инициализация проекта
RUN pip install --user frappe-bench && \
    ~/.local/bin/bench init frappe-bench --frappe-branch version-15 --skip-assets
