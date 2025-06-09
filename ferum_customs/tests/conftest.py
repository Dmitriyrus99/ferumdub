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


from types import SimpleNamespace

from ferum_customs.custom_logic import service_request_hooks


class DummyEntry(SimpleNamespace):
    """Helper entry object with ``get`` method for table rows."""

    def get(self, key):
        return getattr(self, key, None)


@pytest.fixture()
def engineers_doc():
    """Return a dummy Service Object doc with assigned engineers."""

    return SimpleNamespace(
        assigned_engineers=[
            DummyEntry(engineer="u1"),
            DummyEntry(engineer="u1"),
            DummyEntry(engineer="u2"),
        ]
    )


@pytest.fixture()
def patch_frappe_get_doc(monkeypatch, engineers_doc):
    """Patch ``frappe.get_doc`` to return ``engineers_doc``."""

    monkeypatch.setattr(frappe, "get_doc", lambda *a, **k: engineers_doc)
    return engineers_doc


@pytest.fixture()
def patch_frappe_get_doc_missing(monkeypatch):
    """Patch ``frappe.get_doc`` to raise ``DoesNotExistError``."""

    class DoesNotExist(Exception):
        pass

    monkeypatch.setattr(
        service_request_hooks.frappe,
        "DoesNotExistError",
        DoesNotExist,
        raising=False,
    )

    def raise_missing(*_a, **_k):
        raise DoesNotExist

    monkeypatch.setattr(frappe, "get_doc", raise_missing)
    return DoesNotExist
