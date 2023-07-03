import frappe
from frappe import _

def execute(filters=None):
    columns = [
        
		{
            "label": _("Date"),
            "fieldname": "date",
            "fieldtype": "Date",
            "width": 100
        },
        {
            "label": _("Parameter"),
            "fieldname": "parameter",
            "fieldtype": "Data",
            "width": 100
        },
        {
            "label": _("Value"),
            "fieldname": "value",
            "fieldtype": "Float",
            "width": 100
        },
         {
            "label": _("Member Name"),
            "fieldname": "full_name",
            "fieldtype": "Data",
            "width": 300
        },
        # Add more columns for other tracked data
    ]

    data = get_data(filters)

    return columns, data

def get_data(filters):
    # Retrieve the data for the specified gym member
    return frappe.db.sql("""
     SELECT
            v.`date`,
            v.`parameter`,
            v.`value`,
            m.`full_name`
        FROM
            `tabGym Member Vital and Body Measurements` v
        INNER JOIN
            `tabGym Member` m ON m.`name` = v.`parent`
        WHERE
            v.`parenttype` = 'Gym Member'
            AND v.`parent` = %(member)s
        ORDER BY
            v.`date`
    """, filters, as_dict=1)
    #     SELECT
    #         `date`,
    #         `parameter`,
    #         `value`
    #     FROM
    #         `tabGym Member Vital and Body Measurements`
    #     WHERE
    #         `parenttype` = 'Gym Member'
    #         AND `parent` = %(member)s
    #     ORDER BY
    #         `date`
    # """, filters, as_dict=1)
	
