import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {
            "label": _("Group Class"),
            "fieldname": "group_class",
            "fieldtype": "Link",
            "options": "Gym Group Classes",
            "width": 200
        },
        {
            "label": _("Bookings"),
            "fieldname": "bookings",
            "fieldtype": "Int",
            "width": 100
        }
    ]

    data = get_data(filters)

    return columns, data

def get_data(filters):
    return frappe.db.sql("""
        SELECT
            `joined_any_group_class` AS `group_class`,
            COUNT(*) AS `bookings`
        FROM
            `tabGym Member`
        WHERE
            `joined_any_group_class` IS NOT NULL
        GROUP BY
            `joined_any_group_class`
        ORDER BY
            `bookings` DESC
    """, as_dict=True)
