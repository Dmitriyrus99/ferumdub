import pytest

pytest.importorskip("frappe")
import frappe
from types import SimpleNamespace
from ferum_customs.custom_logic import service_request_hooks


class DummyEntry(SimpleNamespace):
    def get(self, key):
        return getattr(self, key, None)


def test_get_engineers(monkeypatch):
    doc = SimpleNamespace(
        assigned_engineers=[
            DummyEntry(engineer="u1"),
            DummyEntry(engineer="u1"),
            DummyEntry(engineer="u2"),
        ]
    )
    monkeypatch.setattr(frappe, "get_doc", lambda *a, **k: doc)
    result = service_request_hooks.get_engineers_for_object("OBJ")
    assert set(result) == {"u1", "u2"}


def test_get_engineers_missing(monkeypatch):
    class DoesNotExist(Exception):
        pass

    monkeypatch.setattr(
        service_request_hooks.frappe, "DoesNotExistError", DoesNotExist, raising=False
    )

    def raise_missing(*a, **k):
        raise DoesNotExist

    monkeypatch.setattr(frappe, "get_doc", raise_missing)
    result = service_request_hooks.get_engineers_for_object("OBJ")
    assert result == []
