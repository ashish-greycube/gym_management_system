from __future__ import unicode_literals
import frappe
from frappe import _


def get_context(context):
    print('33'*100)
    print('-'*100)
    user=frappe.session.user
    context.user=user
    user='rohit@gmail.com'
    context.data=frappe.db.sql('''SELECT membership.plan, DATEDIFF(membership.end_date,CURDATE()) as remaining_days  FROM `tabGym Member` as `member` inner join `tabGym Membership` as membership on member.name=membership.`member` 
where `member`.`user` =%s''',(user),as_dict=1,)[0]
    # context.past=
    print(user,context)
    return context
    # return {"data1": context.data}
    # return context