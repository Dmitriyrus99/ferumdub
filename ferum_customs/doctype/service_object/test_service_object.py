import unittest

import pytest

try:
    import frappe
except Exception:  # pragma: no cover
    pytest.skip("frappe not available", allow_module_level=True)


class TestServiceObject(unittest.TestCase):
    def test_description_trim(self):
        doc = frappe.new_doc("Service Object")
        doc.linked_service_project = " PROJECT001 "
        doc.validate()
        self.assertEqual(doc.linked_service_project, "PROJECT001")
