import inspect
import os
import shutil

import pytest

try:
    import frappe
    from frappe.installer import _new_site
except Exception:  # pragma: no cover - frappe not installed
    pytest.skip("frappe not available", allow_module_level=True)


@pytest.fixture(scope="session")
def frappe_site(tmp_path_factory):
    site_path = tmp_path_factory.mktemp("frappe_site")
    site_name = "test_site"
    cwd = os.getcwd()
    os.chdir(site_path)
    try:
        params = inspect.signature(_new_site).parameters
        kwargs = {
            "admin_password": "admin",
            "db_root_password": "root",
            "db_root_username": "root",
            "verbose": False,
            "install_apps": ["erpnext", "ferum_customs"],
        }
        if "db_root_password" not in params:
            kwargs.pop("db_root_password")
            kwargs.pop("db_root_username")
            kwargs["mariadb_root_password"] = "root"

        _new_site(None, site_name, **{k: v for k, v in kwargs.items() if k in params})
        frappe.init(site=site_name, sites_path=str(site_path))
        frappe.connect(site=site_name)
        frappe.use_site(site_name)
        yield site_name
    finally:
        frappe.destroy()
        os.chdir(cwd)
        shutil.rmtree(site_path)
