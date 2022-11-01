// Copyright (c) 2022, GreyCube Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Locker Booking', {
	setup: function(frm) {
		frm.set_query('locker', () => {
			return {
				filters: {
					status: 'Available'
				}
			}
		})
		frm.set_query('member', () => {
			return {
				query: 'gym_management_system.gym_management_system.doctype.gym_locker_booking.gym_locker_booking.get_valid_members',
			}
		})				
	}
});
