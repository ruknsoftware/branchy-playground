import frappe
from frappe import _

def get_employee_by_user(user):
    if not user:
        frappe.throw(_("User ID must be provided"))

    employee = frappe.get_value("Employee", {"user_id": user}, "name")
    if not employee:
        frappe.throw(_(f"Employee not found for the given user ID: {user}"))
        
    return employee