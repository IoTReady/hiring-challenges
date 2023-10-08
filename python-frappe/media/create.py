# link_bundler/link_bundler/page/create/create.py

import frappe

def get_context(context):
    if frappe.session.user == "Guest":
        frappe.local.flags.redirect_location = "/login"  # Redirect guest users to the login page
        raise frappe.Redirect

def create_bundle():
    bundle = frappe.new_doc("LinkBundle")
    bundle.creator = frappe.session.user
    bundle.save()

    return bundle

@frappe.whitelist()
def add_link(link_url, bundle_name):
    bundle = frappe.get_doc("LinkBundle", bundle_name)
    link_item = bundle.append("links", {})
    link_item.link_url = link_url
    bundle.save()

    return link_item.name
