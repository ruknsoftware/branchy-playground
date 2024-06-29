import frappe
from frappe import _

def get_employee_by_user(user):
    if not user:
        user = frappe.session.user
    try:
        employee = frappe.get_value("Employee", {"user_id": user}, "name")
        if not employee:
            frappe.throw(f"error: Employee not found for the given user {user}")

        return employee
    except Exception as e:
        raise e