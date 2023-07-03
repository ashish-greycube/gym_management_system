# Copyright (c) 2023, Vijay and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    columns = [
        {
            "label": "Membership",
            "fieldtype": "Link",
            "options": "Gym Membership",
            "fieldname": "gym_membership",
            "width": 300,
        },
        {
            "label": "Revenue",
            "fieldtype": "Currency",
            "fieldname": "revenue",
            "width": 300,
            "currency": "INR",
        },
    ]
    data = get_data(filters)
    return columns, data, get_summary(data)


def get_data(filters):
    return frappe.db.sql(
        """
        SELECT
            `name` AS `gym_membership`,
            `fees_paid` AS `revenue`
        FROM
            `tabGym Membership`
        WHERE
            `docstatus` = 1
        """,
        as_dict=True,
    )


def get_summary(data):
    return [
        {
            "value": sum(d.revenue for d in data),
            "label": _("Total Revenue"),
            "datatype": "Currency",
            "currency": "INR",
        },
    ]
