import os
import pytest
import frappe

@pytest.fixture(scope="session")
def frappe_test_context():
    """
    Эта фикстура создает полноценный тестовый сайт Frappe один раз за сессию,
    устанавливает необходимые приложения и корректно очищает окружение после тестов.
    """
    frappe.flags.in_test = True
    test_site_name = "test_site"

    # Запоминаем текущую директорию и переходим во временную
    cwd = os.getcwd()
    sites_path = os.getcwd()
    os.chdir(sites_path)

    try:
        # --- Создание сайта ---
        # Уничтожаем предыдущий сайт, если он остался от неудачного запуска
        frappe.destroy()

        # Создаем новый сайт с необходимыми параметрами
        frappe.new_site(
            test_site_name,
            admin_password="admin",
            mariadb_root_password=os.environ.get("MYSQL_ROOT_PASSWORD"),
            install_apps=["erpnext", "ferum_customs"],
            force=True,
            reinstall=True,
        )

        # --- Подключение к сайту ---
        # Устанавливаем сайт как текущий глобальный контекст
        frappe.connect(site=test_site_name)

        # Передаем управление тестовой сессии
        yield

    finally:
        # --- Очистка после тестов ---
        # Завершаем соединение и полностью удаляем сайт и базу данных
        frappe.destroy()
        # Возвращаемся в исходную директорию
        os.chdir(cwd)

@pytest.fixture(autouse=True)
def use_frappe_test_context(frappe_test_context):
    """
    Эта фикстура автоматически применяется ко всем тестам
    и обеспечивает их выполнение в созданном контексте.
    """
    # frappe.db.commit() можно использовать для чистого состояния перед каждым тестом
    yield
    # frappe.db.rollback() откатывает изменения после каждого теста
    frappe.db.rollback()
    и обеспечивает их выполнение в созданном контексте.
    """
    pass
