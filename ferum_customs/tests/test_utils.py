import pytest

pytest.importorskip("frappe")
import frappe
from types import SimpleNamespace
from ferum_customs.utils import utils


def test_get_engineers_for_service_object(monkeypatch):
    doc = SimpleNamespace(assigned_engineers=[{"engineer": "u1"}, {"engineer": "u1"}, {"engineer": "u2"}])
    monkeypatch.setattr(frappe.db, "exists", lambda *a, **k: True)
    monkeypatch.setattr(frappe, "get_doc", lambda *a, **k: doc)
    result = utils.get_engineers_for_service_object("OBJ")
    assert sorted(result) == ["u1", "u2"]


def test_get_engineers_missing(monkeypatch):
    monkeypatch.setattr(frappe.db, "exists", lambda *a, **k: False)
    result = utils.get_engineers_for_service_object("OBJ")
    assert result == []

