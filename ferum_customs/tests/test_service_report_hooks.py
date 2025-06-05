import pytest

pytest.importorskip("frappe")
import frappe
from types import SimpleNamespace
from ferum_customs.custom_logic import service_report_hooks
from ferum_customs.constants import STATUS_VYPOLNENA


class DummyDoc(SimpleNamespace):
    def get(self, key):
        return getattr(self, key, None)


def test_validate_ok(monkeypatch):
    doc = DummyDoc(service_request="REQ-1", name="SR-1")
    monkeypatch.setattr(frappe.db, "exists", lambda *a, **k: True)
    monkeypatch.setattr(frappe.db, "get_value", lambda *a, **k: STATUS_VYPOLNENA)
    service_report_hooks.validate(doc)


def test_validate_missing_request(monkeypatch):
    doc = DummyDoc(service_request=None, name="SR-1")
    monkeypatch.setattr(frappe, "throw", lambda *a, **k: (_ for _ in ()).throw(Exception("throw")))
    with pytest.raises(Exception):
        service_report_hooks.validate(doc)


def test_validate_wrong_status(monkeypatch):
    doc = DummyDoc(service_request="REQ-1", name="SR-1")
    monkeypatch.setattr(frappe.db, "exists", lambda *a, **k: True)
    monkeypatch.setattr(frappe.db, "get_value", lambda *a, **k: "Открыта")
    monkeypatch.setattr(frappe, "throw", lambda *a, **k: (_ for _ in ()).throw(Exception("throw")))
    with pytest.raises(Exception):
        service_report_hooks.validate(doc)
