from __future__ import unicode_literals
import frappe
from frappe import _


def get_context(context):
    print('-'*100)
    user=frappe.session.user
    context.data=frappe.db.sql('''SELECT membership.plan, DATEDIFF(membership.end_date,CURDATE()) as remaining_days  FROM `tabGym Member` as `member` inner join `tabGym Membership` as membership on member.name=membership.`member` 
where `member`.`user` =%s'''.format(user))
    print(user,context)
    return 'data'
    # return context