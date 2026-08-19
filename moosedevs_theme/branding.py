import frappe

LOGO_URL = "/assets/moosedevs_theme/images/logo.svg"
FAVICON_URL = "/assets/moosedevs_theme/images/favicon.svg"
APP_TITLE = "Moosedevs ERP"


def _set_if_field_exists(doctype, fieldname, value):
	meta = frappe.get_meta(doctype)
	if meta.has_field(fieldname):
		frappe.db.set_single_value(doctype, fieldname, value)


def apply_branding():
	for fieldname, value in {
		"app_name": APP_TITLE,
		"banner_image": LOGO_URL,
		"app_logo": LOGO_URL,
		"favicon": FAVICON_URL,
		"disable_signup": 1,
	}.items():
		_set_if_field_exists("Website Settings", fieldname, value)

	for fieldname, value in {
		"app_logo": LOGO_URL,
		"app_title": APP_TITLE,
	}.items():
		_set_if_field_exists("Navbar Settings", fieldname, value)

	_set_if_field_exists("System Settings", "app_name", APP_TITLE)

	frappe.db.commit()
