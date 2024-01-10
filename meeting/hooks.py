from . import __version__ as app_version
from frappe import _

app_name = "meeting"
app_title = "Meeting"
app_publisher = "Diya Baweja"
app_description = "Prepare agendas, send invitations and record minutes."
app_email = "hello@frappe.io"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/meeting/css/meeting.css"
# app_include_js = "/assets/meeting/js/meeting.js"

# include js, css files in header of web template
# web_include_css = "/assets/meeting/css/meeting.css"
# web_include_js = "/assets/meeting/js/meeting.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "meeting/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
website_generators = ["Meeting"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "meeting.utils.jinja_methods",
#	"filters": "meeting.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "meeting.install.before_install"
# after_install = "meeting.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "meeting.uninstall.before_uninstall"
# after_uninstall = "meeting.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "meeting.utils.before_app_install"
# after_app_install = "meeting.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "meeting.utils.before_app_uninstall"
# after_app_uninstall = "meeting.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "meeting.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

#doc_events = {
#	"User": {
#		"after_insert": "meeting.api.make_orientation_meeting"
#	},
#	"ToDo": {
#		"on_update": "meeting.api.update_minute_status",
#		"on_trash": "meeting.api.update_minute_status"
#	}
#}

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# meeting/hooks.py



def get_context(context):
    context.no_cache = 1

# Additional hooks configuration...

# Whitelist the new route
guest_methods = ['meeting.meeting.doctype.meeting.meeting.check_user_login']


# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"meeting.tasks.all"
#	],
#	"daily": [
#		"meeting.tasks.daily"
#	],
#	"hourly": [
#		"meeting.tasks.hourly"
#	],
#	"weekly": [
#		"meeting.tasks.weekly"
#	],
#	"monthly": [
#		"meeting.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "meeting.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "meeting.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "meeting.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["meeting.utils.before_request"]
# after_request = ["meeting.utils.after_request"]

# Job Events
# ----------
# before_job = ["meeting.utils.before_job"]
# after_job = ["meeting.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"meeting.auth.validate"
# ]
