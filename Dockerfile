FROM python:3.10-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    git \
    mariadb-client \
    redis-server \
    nodejs \
    npm \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Установка корректной версии Yarn через npm
RUN npm install -g yarn

# Создание пользователя frappe
RUN useradd -ms /bin/bash frappe

# Переход на пользователя frappe
USER frappe
WORKDIR /home/frappe

# Установка bench и инициализация проекта
RUN pip install --user frappe-bench && \
    ~/.local/bin/bench init frappe-bench --frappe-branch version-15 --skip-assets
