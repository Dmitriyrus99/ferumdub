import os
import shutil
import pytest

pytest.importorskip("frappe")
import frappe
from frappe.installer import new_site


@pytest.fixture(scope="session")
def frappe_site(tmp_path_factory):
    site_path = tmp_path_factory.mktemp("frappe_site")
    site_name = "test_site"
    cwd = os.getcwd()
    os.chdir(site_path)
    try:
        new_site(site_name, admin_password="admin", mariadb_root_password="root", quiet=True)
        frappe.init(site=site_name, sites_path=str(site_path))
        frappe.connect(site=site_name)
        yield site_name
    finally:
        frappe.destroy()
        os.chdir(cwd)
        shutil.rmtree(site_path)

