// Copyright (c) 2023, puja and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Locker Booking', {
	setup: function(frm) {

		frm.set_query("locker", function() {
			return{
				"filters": {
					"status": "Available"
				}
			}
		});
	}
});
