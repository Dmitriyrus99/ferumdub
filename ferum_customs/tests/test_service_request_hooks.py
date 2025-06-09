import pytest

try:
    import frappe
    from frappe.tests.utils import FrappeTestCase
except Exception:  # pragma: no cover - frappe not installed
    pytest.skip("frappe not available", allow_module_level=True)

from ferum_customs.custom_logic import service_request_hooks


class TestServiceRequestHooks(FrappeTestCase):
    def test_get_engineers(self, patch_frappe_get_doc, frappe_site):
        patch_frappe_get_doc()
        result = service_request_hooks.get_engineers_for_object("OBJ")
        self.assertEqual(set(result), {"u1", "u2"})

    def test_get_engineers_missing(self, patch_frappe_get_doc_missing, frappe_site):
        patch_frappe_get_doc_missing()
        result = service_request_hooks.get_engineers_for_object("OBJ")
        self.assertEqual(result, [])
