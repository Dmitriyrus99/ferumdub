import pytest

try:
    import frappe  # noqa: F401
except Exception:  # pragma: no cover
    pytest.skip("frappe not available", allow_module_level=True)

from ferum_customs import api


def test_validate_service_request():
    """Test validate_service_request method"""
    doc = api.validate_service_request("test_docname")
    assert doc is not None
    assert doc.name == "test_docname"
