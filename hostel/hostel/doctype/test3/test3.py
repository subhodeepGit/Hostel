# Copyright (c) 2021, SOUL and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class test3(Document):
	def get_full_name(self):
		"Returns the person's full name"
		return self.first_name + ' ' + self.last_name