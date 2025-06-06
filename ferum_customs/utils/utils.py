# ferum_customs/utils/utils.py
"""
Общие вспомогательные (utility) функции для приложения `ferum_customs`.

Эти функции могут быть вызваны из разных частей приложения,
включая хуки, серверные скрипты или другие утилиты.

Whitelisted-функции из этого модуля могут быть вызваны с клиента через `frappe.call`.
"""
from __future__ import annotations
