# Copyright (c) 2022, GreyCube Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class GymLockerBooking(Document):
	def validate(self):
		self.book_locker()

	def book_locker(self):	
		locker=frappe.get_doc('Gym Locker',self.locker)
		if locker.status=='Booked':
			frappe.throw(_('Locker {0} is already Booked'.format(self.locker)))
		else:
			locker.status='Booked'
			locker.save()
			frappe.msgprint(_('Locker {0} is booked'.format(self.locker)))

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_valid_members(doctype, txt, searchfield, start, page_len, filters):
    # your logic
    return frappe.db.sql('''select
	membership.member,
	member.member_name
from
	`tabGym Membership` as membership
inner join `tabGym Member` as member on
	member.name = membership.member
where
	membership.start_date <= CURDATE()
	and membership.end_date >= CURDATE() ''',as_list=1)
