# Copyright (c) 2022, GreyCube Technologies and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [], []
	columns=[
  {
   "fieldname": "group__class",
   "fieldtype": "Link",
   "label": " Group Class ",
   "options": "Gym Group Class",
   "width": 0
  },
  {
   "fieldname": "no_of_booking",
   "fieldtype": "Int",
   "label": "No of Booking",
   "width": 0
  }
 ]
	data=frappe.db.sql('''SELECT  group__class, count(name) as no_of_booking FROM `tabGym Group Class Booking` group by group__class ''')
	return columns, data
