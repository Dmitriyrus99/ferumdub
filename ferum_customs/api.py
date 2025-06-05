import frappe
from frappe import _, whitelist
from frappe.exceptions import PermissionError
from typing import Optional


@whitelist()
def validate_service_request(docname: str) -> Optional[dict]:
    """Return the service request document as a dict after permission check."""
    if not frappe.has_permission("Service Request", "read"):
        frappe.throw(_("Not permitted"), PermissionError)

    try:
        doc = frappe.get_doc("Service Request", docname)
        return doc.as_dict()
    except Exception:
        frappe.log_error(frappe.get_traceback(), "Error validating Service Request")
        raise


@whitelist()
def on_submit_service_request(docname: str) -> None:
    """Hook executed when a Service Request is submitted."""
    frappe.logger(__name__).info(f"Service Request '{docname}' submitted")


@whitelist()
def cancel_service_request(docname: str) -> None:
    """Hook executed when a Service Request is cancelled."""
    frappe.logger(__name__).info(f"Service Request '{docname}' cancelled")


@whitelist()
def validate_service_report(docname: str) -> Optional[dict]:
    """Return the service report document as a dict after permission check."""
    if not frappe.has_permission("Service Report", "read"):
        frappe.throw(_("Not permitted"), PermissionError)

    try:
        doc = frappe.get_doc("Service Report", docname)
        return doc.as_dict()
    except Exception:
        frappe.log_error(frappe.get_traceback(), "Error validating Service Report")
        raise


@whitelist()
def on_submit_service_report(docname: str) -> None:
    """Hook executed when a Service Report is submitted."""
    frappe.logger(__name__).info(f"Service Report '{docname}' submitted")
