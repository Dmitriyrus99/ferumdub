import pytest

pytest.importorskip("frappe")
import frappe
from ferum_customs.custom_logic import service_object_hooks


class DummyDoc:
    def __init__(self, serial_no, name="SO-0001"):
        self.serial_no = serial_no
        self.name = name

    def get(self, key):
        return getattr(self, key, None)


def test_validate_unique(monkeypatch):
    doc = DummyDoc("SN-1")
    monkeypatch.setattr(frappe.db, "exists", lambda *args, **kwargs: None)
    monkeypatch.setattr(
        frappe, "throw", lambda *a, **k: (_ for _ in ()).throw(Exception("throw"))
    )
    # Should not raise
    service_object_hooks.validate(doc)


def test_validate_duplicate(monkeypatch):
    doc = DummyDoc("SN-1")
    monkeypatch.setattr(frappe.db, "exists", lambda *a, **k: "SO-0002")

    def fake_throw(msg, *a, **k):
        raise Exception(msg)

    monkeypatch.setattr(frappe, "throw", fake_throw)

    with pytest.raises(Exception):
        service_object_hooks.validate(doc)
