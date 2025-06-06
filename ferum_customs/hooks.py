# Ferum Customs - hooks

from .custom_hooks import DOC_EVENTS

app_name = "ferum_customs"
app_title = "Ferum Customs"
app_publisher = "Ferum LLC"
app_description = "Specific custom functionality for ERPNext"
app_email = "support@ferum.ru"
app_license = "MIT"


to_populate: list[str] = []


doc_events = DOC_EVENTS

get_notification_config = "ferum_customs.config.notifications"

fixtures = [
    "custom_fields",
    "custom_docperm",
    {
        "dt": "Role",
        "filters": [["name", "in", ["Проектный менеджер", "Инженер", "Заказчик"]]],
    },
    {"dt": "Workflow", "filters": [["name", "in", ["Workflow Service Request"]]]},
    "service_report_workflow",
    "customer",
    "service_project",
    "service_object",
    "service_request",
    "service_report",
    "portal_menu_item",
    "User",
]

try:
    from .dev_hooks import *  # noqa: F401,F403
except ImportError:
    pass
