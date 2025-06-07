import os
import pytest
import subprocess
import frappe

@pytest.fixture(scope="session")
def frappe_test_context():
    """
    Создает полноценный тестовый сайт Frappe один раз за сессию.
    """
    test_site_name = "test_site"
    cwd = os.getcwd()

    try:
        subprocess.run(["bench", "drop-site", test_site_name, "--force"], check=False)
        subprocess.run([
            "bench", "new-site", test_site_name,
            "--admin-password", "admin",
            "--mariadb-root-password", os.environ.get("MYSQL_ROOT_PASSWORD")
        ], check=True)

        subprocess.run(["bench", "use", test_site_name], check=True)
        subprocess.run(["bench", "install-app", "erpnext"], check=True)
        subprocess.run(["bench", "install-app", "ferum_customs"], check=True)

        frappe.init(site=test_site_name)
        frappe.connect()
        frappe.flags.in_test = True

        yield

    finally:
        frappe.destroy()
        subprocess.run(["bench", "drop-site", test_site_name, "--force"], check=True)
        os.chdir(cwd)

@pytest.fixture(autouse=True)
def use_frappe_test_context(frappe_test_context):
    yield
    frappe.db.rollback()
