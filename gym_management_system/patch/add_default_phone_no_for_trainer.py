from distutils.log import debug
import frappe

def execute():
    office_no=9999999999
    # frappe.reload_doc("gym_management_system", "doctype", "gym_trainer")
    frappe.db.sql('''update `tabGym Trainer` set `trainer_contact` = %s''',(office_no))