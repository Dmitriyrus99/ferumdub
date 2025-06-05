FROM python:3.10-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    git \
    mariadb-client \
    redis-server \
    nodejs \
    npm \
    curl && \
    rm -rf /var/lib/apt/lists/*

# Установка конкретной версии Yarn 1.x
RUN npm install -g yarn@1.22.19

# Создание пользователя frappe
RUN useradd -ms /bin/bash frappe

# Переход на пользователя frappe
USER frappe
WORKDIR /home/frappe

# Установка bench и инициализация проекта
ENV PATH="/home/frappe/.local/bin:$PATH"
RUN pip install --user frappe-bench && \
    bench init frappe-bench --frappe-branch version-15 --skip-assets
