# ferum_customs/tests/conftest.py
import os
import pytest
import frappe
from frappe.utils import get_bench_path

@pytest.fixture(scope="session")
def frappe_test_context():
    """
    Эта фикстура создает полноценный тестовый сайт Frappe один раз за сессию,
    устанавливает необходимые приложения и корректно очищает окружение после тестов.
    """
    # Устанавливаем флаг, что мы находимся в тестовом режиме
    frappe.flags.in_test = True

    # Определяем имя тестового сайта
    test_site_name = "test_site"
    sites_path = os.getcwd()
    site_path = os.path.join(sites_path, test_site_name)

    # Принудительно очищаем окружение от предыдущих запусков, если они были
    frappe.destroy()
    frappe.local.sites_path = sites_path

    try:
        # --- Создание сайта ---
        # Устанавливаем соединение с базой данных по умолчанию
        frappe.local.db = frappe.database.get_db()
        # Создаем новую базу данных для сайта
        frappe.new_site(
            test_site_name,
            admin_password="admin",
            mariadb_root_password=os.environ.get("MYSQL_ROOT_PASSWORD"),
            db_type=os.environ.get("DB_TYPE"),
            force=True,
            reinstall=True,
        )

        # --- Инициализация и установка приложений ---
        # Устанавливаем сайт как текущий контекст
        frappe.use_site(test_site_name)

        # Устанавливаем базовые приложения
        print("Installing erpnext...")
        frappe.install_app("erpnext", verbose=False)
        print("Installing ferum_customs...")
        frappe.install_app("ferum_customs", verbose=False)

        # Применяем все миграции
        frappe.db.commit()

        # Передаем управление тестовой сессии
        yield

    finally:
        # --- Очистка после тестов ---
        # Завершаем соединение и удаляем сайт
        frappe.destroy()

@pytest.fixture(autouse=True)
def use_frappe_test_context(frappe_test_context):
    """
    Эта фикстура автоматически применяется ко всем тестам
    и обеспечивает их выполнение в созданном контексте.
    """
    pass
