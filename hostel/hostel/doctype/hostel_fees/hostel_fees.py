# Copyright (c) 2021, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import money_in_words
from frappe.model.document import Document

class HostelFees(Document):
	def validate(self):
		self.calculate_total()

	def set_indicator(self):
		"""Set indicator for portal"""
		if self.outstanding_amount > 0:
			self.indicator_color = "orange"
			self.indicator_title = ("Unpaid")
		else:
			self.indicator_color = "green"
			self.indicator_title = ("Paid")

	def calculate_total(self):
		"""Calculates total amount."""
		self.grand_total = 0
		for d in self.components:
			self.grand_total += d.amount
		print("\n\n\n\n")
		print(self.grand_total)
		self.outstanding_amount = self.grand_total
		self.grand_total_in_words = money_in_words(self.grand_total)

@frappe.whitelist()
def get_fee_components(hostel_fee_structure):
	"""Returns Fee Components.

	:param fee_structure_hostel: Fee Structure Hostel.
	"""
	if hostel_fee_structure:
		fs = frappe.get_all("Fee Component", fields=["fees_category", "description", "amount", "receivable_account", "income_account", "waiver_type", "waiver_amount", "grand_fee_amount", "outstanding_fees"] , filters={"parent": hostel_fee_structure}, order_by= "idx")
		return fs

