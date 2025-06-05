#!/bin/bash

echo "📦 Установка зависимостей..."

# Установка инструментов для анализа кода
pip install -U pip
pip install openai flake8 black pylint mypy isort

# Если requirements.txt существует, устанавливаем
if [ -f requirements.txt ]; then
    echo "🔗 Установка зависимостей из requirements.txt..."
    pip install -r requirements.txt
fi

echo "✅ Установка завершена."
