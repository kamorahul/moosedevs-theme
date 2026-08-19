app_name = "moosedevs_theme"
app_title = "Moosedevs ERP"
app_publisher = "Moosedevs Limited"
app_description = "Moosedevs ERP branding and white-label customization"
app_email = "hello@moosedevs.com"
app_license = "MIT"

app_logo_url = "/assets/moosedevs_theme/images/logo.svg"

app_include_css = "/assets/moosedevs_theme/css/moosedevs_theme.css"
web_include_css = "/assets/moosedevs_theme/css/moosedevs_theme.css"

website_context = {
	"app_name": app_title,
	"favicon": "/assets/moosedevs_theme/images/favicon.svg",
	"splash_image": "/assets/moosedevs_theme/images/logo.svg",
}

after_install = "moosedevs_theme.branding.apply_branding"
after_migrate = "moosedevs_theme.branding.apply_branding"
