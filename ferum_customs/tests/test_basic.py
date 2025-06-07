import unittest

import pytest

try:
    import frappe  # noqa: F401
except Exception:  # pragma: no cover - frappe not installed
    pytest.skip("frappe not available", allow_module_level=True)


class TestTestBasic(unittest.TestCase):
    def test_basic(self):
        self.assertTrue(True)
