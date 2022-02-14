import frappe
from frappe.sessions import clear
from frappe.core.doctype.activity_log.activity_log import add_authentication_log
from frappe.utils import get_fullname
import json

def role_check(user, target):
    if user == target: # Don't allow impersonating self
        return False
    if user == "Administrator" or "System Manager" in frappe.get_roles():
        is_privileged_user = target == "Administrator" or "System Manager" in frappe.get_roles(target)
        return not is_privileged_user
    return False



@frappe.whitelist()
def impersonate(user):
    # if frappe.session.user == "Administrator" or "System Manager" in frappe.get_roles():
    if role_check(frappe.session.user, user):
        clear()
        message = "{a} impersonates {u}".format(a=get_fullname(frappe.session.user), u=user, operation="Impersonation")
        add_authentication_log(message, frappe.session.user)
        frappe.local.login_manager.login_as(user)
        # Create 2 entries in authentication log
        add_authentication_log("{u} logged in".format(u=user), user)
        return {"status": "Success", "message": frappe._("Impersonated ") + str(user)}

    return {"status": "Fail", "message": frappe._("Not allowed to impersonate ") + str(user)}

