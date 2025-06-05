"""Patch placeholder for future permission migrations."""

import frappe


def execute():
    """Migrate permissions if necessary."""
    # Роли создаются через fixtures/role.json, поэтому патч пока ничего не делает
    pass
