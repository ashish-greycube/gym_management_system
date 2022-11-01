# Copyright (c) 2022, GreyCube Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class GymWorkoutPlan(WebsiteGenerator):
	def validate(self):
		self.route=self.name
		self.published=1
