FROM python:3.10-slim

# Установка зависимостей
RUN apt-get update && apt-get install -y \
    git \
    mariadb-client \
    redis-server \
    nodejs \
    npm \
    yarn \
    curl

# Создание пользователя frappe
RUN addgroup --system frappe && adduser --system --ingroup frappe frappe

# Переход на пользователя frappe
USER frappe
WORKDIR /home/frappe

# Инициализация фреймворка Frappe
RUN pip install frappe-bench && \
    bench init frappe-bench --frappe-branch version-15
