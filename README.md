# Ferum Customs для Frappe

## Описание

`Ferum Customs` — модуль к ERPNext, который автоматизирует работу с сервисными заявками, отчётами и начислениями. Приложение расширяет стандартный функционал Frappe, добавляя удобные роли и механизмы контроля заявок.

## Требования

* Python 3.10+
* Node.js и Yarn
* MariaDB и Redis
* Linux/Unix‑подобная система (рекомендуется)

## Установка

```bash
# загрузите репозиторий
git clone https://github.com/Dmitriyrus99/ferumdub.git
cd ferumdub

# подготовьте окружение и создайте сайт
bash bootstrap.sh
```

Скрипт инициализирует каталог `frappe-bench`, создаёт сайт `dev.localhost` и устанавливает приложение `ferum_customs`.

## Запуск

```bash
cd frappe-bench
bench start
```

После запуска откройте в браузере `http://localhost:8000` и войдите под учётной записью **Administrator** с паролем `admin`.

## Структура репозитория

```
ferum_customs/
├── custom_logic/          # хуки и дополнительная логика
├── doctype/               # определения DocType
├── patches/               # скрипты миграций
├── tests/                 # autotests
bootstrap.sh               # установка окружения
setup.sh                   # пример развертывания ERPNext 15
```

## Разработка и тесты

```bash
pip install -r dev-requirements.txt
bash bootstrap.sh  # инициализация Bench и создание тестового сайта
pytest --app ferum_customs
ruff check ferum_customs
```

## Поддержка

Вопросы и предложения можно оставлять в [issue‑трекере](https://github.com/Dmitriyrus99/ferumdub/issues).

---
Документация находится в активной разработке.
