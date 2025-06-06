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

# Path to the function returning Notification config.
# The previous value pointed to a non-existing module and caused
# `bench` to fail loading notification settings. Use the actual
# location inside ``ferum_customs.notifications``.
get_notification_config = (
    "ferum_customs.notifications.notifications.get_notification_config"
)

fixtures = [
    "custom_fields",
    "custom_docperm",
    {
        "dt": "Role",
        "filters": [["name", "in", ["Проектный менеджер", "Инженер", "Заказчик"]]],
    },
    {"dt": "Workflow", "filters": [["name", "in", ["Service Request Workflow"]]]},
    "customer",
    "service_project",
    "service_object",
    "service_request",
    "service_report",
    "notification",
    "portal_menu_item",
    "User",
]

try:
    from .dev_hooks import *  # noqa: F401,F403
except ImportError:
    pass
