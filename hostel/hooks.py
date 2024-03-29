from . import __version__ as app_version

app_name = "hostel"
app_title = "Hostel"
app_publisher = "SOUL"
app_description = "SUSTAINABLE OUTREACH AND UNIVERSAL LEADERSHIP LIMITED"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "soul@soulunileaders.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hostel/css/hostel.css"
# app_include_js = "/assets/hostel/js/hostel.js"

# include js, css files in header of web template
app_include_js = "/assets/js/aka.min.js"
# web_include_css = "/assets/hostel/css/hostel.css"
# web_include_js = "/assets/hostel/js/hostel.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "hostel/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
        "Student" : "public/js/student.js",
        "Fees" : "public/js/fees.js"
}
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
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "hostel.utils.jinja_methods",
# 	"filters": "hostel.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "hostel.install.before_install"
# after_install = "hostel.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hostel.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Payment Entry": {
        "on_submit": "hostel.hostel.validations.payment_entry.on_submit",
		"on_cancel": "hostel.hostel.validations.payment_entry.on_cancel",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"hostel.tasks.all"
# 	],
# 	"daily": [
# 		"hostel.tasks.daily"
# 	],
# 	"hourly": [
# 		"hostel.tasks.hourly"
# 	],
# 	"weekly": [
# 		"hostel.tasks.weekly"
# 	],
# 	"monthly": [
# 		"hostel.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "hostel.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "hostel.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "hostel.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"hostel.auth.validate"
# ]
# fixtures = [
# 	{"dt": "Custom DocPerm", "filters": [
# 		[
# 			"parent", "not in", [
# 				"DocType"
# 			]
# 		]
# 	]},
#     {"dt": "Role"},
#     {"dt": "Role Profile"},
#     {"dt": "Module Profile"},
# ]
after_migrate = [
        'hostel.patches.migrate_patch.add_roles',
        'hostel.patches.migrate_patch.set_custom_role_permission',
]
