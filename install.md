# Установка и запуск

Этот документ описывает шаги для развёртывания проекта с нуля.

## Системные требования
- Docker и docker-compose
- Статический IP-адрес или домен
- 4 ГБ RAM
- Доступ по SSH

## Быстрый запуск
```bash
git clone https://github.com/Dmitriyrus99/ferumdub.git
cd ferumdub
bash setup-environment.sh
```

## Конфигурация
- **Домен:** задаётся при запуске скрипта развертывания
- **База данных:** PostgreSQL
- **Прокси-сервер:** Traefik
