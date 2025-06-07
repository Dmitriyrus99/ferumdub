import pytest

try:
    import frappe  # noqa: F401
    from frappe.tests.utils import FrappeTestCase
except Exception:  # pragma: no cover
    pytest.skip("frappe not available", allow_module_level=True)

from ferum_customs import api


pytestmark = pytest.mark.usefixtures("frappe_site")


class TestAPI(FrappeTestCase):
    def test_validate_service_request(self):
        """Test validate_service_request method"""
        doc = api.validate_service_request("test_docname")
        self.assertIsNotNone(doc)
        self.assertEqual(doc.name, "test_docname")
