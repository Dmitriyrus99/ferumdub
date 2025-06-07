import unittest

import pytest

try:
    import frappe
except Exception:  # pragma: no cover
    pytest.skip("frappe not available", allow_module_level=True)


class TestProjectObjectItem(unittest.TestCase):
    def test_description_trim(self):
        doc = frappe.new_doc("Project Object Item")
        doc.description = " Test description "
        doc.validate()
        self.assertEqual(doc.description, "Test description")
