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

После выполнения вы можете запустить Bench и перейти в систему:

```bash
cd frappe-bench
bench start
```

Затем откройте в браузере `http://localhost:8000` и войдите под учётной записью **Administrator** с паролем `admin`.

## Работа с репозиторием

В проекте используется [pre-commit](https://pre-commit.com/) для запуска форматирования, линтера и тестов. Установите хуки один раз:

```bash
pre-commit install
```

Перед коммитом будет автоматически выполняться `black`, `ruff`, `mypy` и `pytest`. Вы также можете запустить их вручную:

```bash
pre-commit run --all-files
```

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
pre-commit run --all-files
```

## Поддержка

Вопросы и предложения можно оставлять в [issue‑трекере](https://github.com/Dmitriyrus99/ferumdub/issues).

---
Дополнительные материалы доступны в [docs/OUTLINE.md](docs/OUTLINE.md).
