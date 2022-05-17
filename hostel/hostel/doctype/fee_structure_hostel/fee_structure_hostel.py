# Copyright (c) 2021, SOUL and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc


class FeeStructureHostel(Document):
	def validate(self):
		self.calculate_total()
		self.calculate_amount()

	def calculate_total(self):
		"""Calculates total amount."""
		self.total_amount = 0
		for d in self.components:
			self.total_amount += d.amount
			
	def calculate_amount(self):
		for events in self.get("components"):
			events.grand_fee_amount=events.amount
			events.outstanding_fees=events.amount


@frappe.whitelist()
def make_fee_schedule(source_name, target_doc=None):
	return get_mapped_doc("Fee Structure", source_name,	{
		"Fee Structure": {
			"doctype": "Fee Schedule",
			"validation": {
				"docstatus": ["=", 1],
			}
		},
		"Fee Component": {
			"doctype": "Fee Component"
		}
	}, target_doc)

