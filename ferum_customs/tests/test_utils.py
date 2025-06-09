import pytest

pytest.importorskip("frappe")
import frappe  # noqa: E402
from frappe.tests.utils import FrappeTestCase  # noqa: E402
from ferum_customs.custom_logic import service_request_hooks  # noqa: E402


class TestUtils(FrappeTestCase):
    def test_get_engineers_for_object(self, patch_frappe_get_doc, frappe_site):
        patch_frappe_get_doc()
        result = service_request_hooks.get_engineers_for_object("OBJ")
        self.assertEqual(set(result), {"u1", "u2"})

    def test_get_engineers_missing(self, patch_frappe_get_doc_missing, frappe_site):
        patch_frappe_get_doc_missing()
        result = service_request_hooks.get_engineers_for_object("OBJ")
        self.assertEqual(result, [])
