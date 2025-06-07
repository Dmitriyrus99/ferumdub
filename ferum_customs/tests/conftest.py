import os
import sys
import subprocess
import pytest

try:
    import frappe
except Exception:  # pragma: no cover - frappe not installed
    frappe = None


@pytest.fixture(scope="session")
def frappe_test_context():
    """
    Создает полноценный тестовый сайт Frappe один раз за сессию.
    """
    if frappe is None:
        pytest.skip("frappe not available")

    test_site_name = "test_site"
    cwd = os.getcwd()

    try:
        subprocess.run(
            [
                sys.executable,
                "-m",
                "bench.cli",
                "drop-site",
                test_site_name,
                "--force",
            ],
            check=False,
        )
        subprocess.run(
            [
                sys.executable,
                "-m",
                "bench.cli",
                "new-site",
                test_site_name,
                "--admin-password",
                "admin",
                "--mariadb-root-password",
                os.environ.get("MYSQL_ROOT_PASSWORD"),
            ],
            check=True,
        )

        subprocess.run(
            [
                sys.executable,
                "-m",
                "bench.cli",
                "use",
                test_site_name,
            ],
            check=True,
        )
        subprocess.run(
            [
                sys.executable,
                "-m",
                "bench.cli",
                "install-app",
                "erpnext",
            ],
            check=True,
        )
        subprocess.run(
            [
                sys.executable,
                "-m",
                "bench.cli",
                "install-app",
                "ferum_customs",
            ],
            check=True,
        )

        frappe.init(site=test_site_name)
        frappe.connect()
        frappe.flags.in_test = True

        yield

    finally:
        frappe.destroy()
        subprocess.run(
            [
                sys.executable,
                "-m",
                "bench.cli",
                "drop-site",
                test_site_name,
                "--force",
            ],
            check=True,
        )
        os.chdir(cwd)


@pytest.fixture(autouse=True)
def use_frappe_test_context(frappe_test_context):
    yield
    frappe.db.rollback()
