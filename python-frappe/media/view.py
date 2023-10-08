# link_bundler/link_bundler/page/view/view.py

import frappe
from frappe import _

def get_context(context):
    view_link = frappe.local.form_dict.view_link

    # Retrieve the bundle based on the view link
    bundle = frappe.get_all("LinkBundle", filters={"name": view_link}, fields=["name", "links"])

    if not bundle:
        frappe.msgprint(_("Bundle not found"))
        frappe.local.flags.redirect_location = "/"  # Redirect to the home page or an error page
        raise frappe.Redirect

    context.bundle = bundle[0]

    # You can use the context.bundle object to display the links in your HTML template
