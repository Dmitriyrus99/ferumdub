# Ferum Customs - hooks

from .custom_hooks import DOC_EVENTS

app_name = "ferum_customs"
app_title = "Ferum Customs"
app_publisher = "Ferum LLC"
app_description = "Specific custom functionality for ERPNext"
app_email = "support@ferum.ru"
app_license = "MIT"

app_include_js = ["/assets/ferum_customs/js/ferum_customs.js"]

to_populate: list[str] = []


doc_events = DOC_EVENTS

get_notification_config = "ferum_customs.config.notifications"

fixtures = [
    "custom_fields",
    "custom_docperm",
    {"dt": "Role", "filters": [["name", "in", ["Custom Role"]]]},
    {"dt": "Workflow", "filters": [["name", "in", ["Workflow Service Request"]]]},
    "service_report_workflow",
]
