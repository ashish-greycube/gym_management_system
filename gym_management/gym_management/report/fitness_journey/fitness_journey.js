// Copyright (c) 2023, puja and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Fitness Journey"] = {
	"filters": [
		{
            "fieldname": "member",
            "label": ("Gym Member"),
            "fieldtype": "Link",
            "options": "Gym Member",
            "reqd": 1
        }
	]
};
