# Ferum Customs for Frappe

## 📌 Описание

Ferum Customs — это модуль Frappe для автоматизации сервисных заявок, отчетов, начислений и взаимодействия с рабочими ролями в ERP-среде.

## 🚀 Возможности

* Создание и управление заявками на обслуживание (ServiceRequest)
* Генерация отчетов (ServiceReport)
* Интеграция с начислениями (PayrollEntryCustom)
* Гибкая настройка ролей и разрешений

## ⚙️ Установка

```bash
git clone https://github.com/Dmitriyrus99/ferumdub.git
cd ferumdub
bash bootstrap.sh
```

## ▶️ Быстрый старт

```bash
cd frappe-bench
bench start
```

Откройте в браузере: `http://localhost:8000`

## 📁 Структура проекта

```
ferum_customs/
├── custom_logic/          # Пользовательская логика и хуки
├── ferum_customs/         # Doctypes и приложения
├── patches/               # Скрипты миграций
├── tests/                 # Тесты (unit/integration)
├── entrypoint.sh          # Точка входа для Docker
├── bootstrap.sh           # Скрипт развертывания среды
└── README.md              # Документация
```

## 🧪 Разработка и тесты

```bash
pip install -r dev-requirements.txt
pytest --app ferum_customs
ruff check ferum_customs
```

## 💬 Поддержка

Обратная связь, предложения и ошибки: [issues](https://github.com/Dmitriyrus99/ferumdub/issues)

---

> Документация, миграции и CI находятся в процессе активной разработки.
