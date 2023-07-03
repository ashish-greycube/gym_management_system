import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():
    custom_fields = {
        "Gym Member": [
            dict(
                fieldname="age",
                label="Age",
                fieldtype="Int",
                insert_after="date_of_birth",
                read_only=1
            ),
        ]   
    }

    create_custom_fields(custom_fields, update=True)