# Copyright (c) 2021, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import money_in_words
from frappe.model.document import Document
from erpnext.accounts.general_ledger import make_reverse_gl_entries

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

	def on_submit(self):
		self.create_fees()
		
	def calculate_total(self):
		"""Calculates total amount."""
		self.grand_total = 0
		for d in self.components:
			self.grand_total += d.amount
		self.outstanding_amount = self.grand_total
		self.grand_total_in_words = money_in_words(self.grand_total)



	def create_fees(self):
		fees = frappe.new_doc("Fees")
		fees.student = self.student
		fees.valid_from = self.valid_from
		fees.valid_to = self.valid_to
		fees.due_date = self.due_date
		fees.program_enrollment = self.program_enrollment
		fees.programs = self.programs
		fees.program = self.program
		fees.student_batch = self.student_batch
		fees.academic_year = self.academic_year
		fees.academic_term = self.academic_term
		# fees.fee_structure = self.hostel_fee_structure
		ref_details = frappe.get_all("Fee Component",{"parent":self.hostel_fee_structure},['fees_category','amount','receivable_account','income_account','company','grand_fee_amount','outstanding_fees'])
		for i in ref_details:
			fees.append("components",{
				'fees_category' : i['fees_category'],
				'amount' : i['amount'],
				'receivable_account' : i['receivable_account'],
				'income_account' : i['income_account'],
				'company' : i['company'],
				'grand_fee_amount' : i['grand_fee_amount'],
				'outstanding_fees' : i['outstanding_fees'],
			})
		fees.save()
		fees.submit()	
		self.fees_id = fees.name
		frappe.db.set_value("Hostel Fees",self.name,"fees_id",fees.name)	

@frappe.whitelist()
def get_fee_components(hostel_fee_structure):
	"""Returns Fee Components.

	:param fee_structure_hostel: Fee Structure Hostel.
	"""
	if hostel_fee_structure:
		fs = frappe.get_all("Fee Component", fields=["fees_category", "description", "amount", "receivable_account", "income_account", "waiver_type", "waiver_amount", "grand_fee_amount", "outstanding_fees"] , filters={"parent": hostel_fee_structure}, order_by= "idx")
		return fs


# def cancel_fees(doc):
#     for ce in frappe.get_all("Fees",{"program_enrollment":doc.name}):
#         make_reverse_gl_entries(voucher_type="Fees", voucher_no=ce.name)

# def create_fees(self):
# 	fees = frappe.new_doc("Fees")
# 	fees.student = self.student
# 	fees.valid_from = self.valid_from
# 	fees.valid_to = self.valid_to
# 	fees.due_date = self.due_date
# 	fees.program_enrollment = self.program_enrollment
# 	fees.programs = self.programs
# 	fees.program = self.program
# 	fees.student_batch = self.student_batch
# 	fees.academic_year = self.academic_year
# 	fees.academic_term = self.academic_term
# 	# fees.fee_structure = self.hostel_fee_structure
# 	ref_details = frappe.get_all("Fee Component",{"parent":self.hostel_fee_structure},['fees_category','amount','receivable_account','income_account','company','grand_fee_amount','outstanding_fees'])
# 	for i in ref_details:
# 		fees.append("components",{
# 			'fees_category' : i['fees_category'],
# 			'amount' : i['amount'],
# 			'receivable_account' : i['receivable_account'],
# 			'income_account' : i['income_account'],
# 			'company' : i['company'],
# 			'grand_fee_amount' : i['grand_fee_amount'],
# 			'outstanding_fees' : i['outstanding_fees'],
# 		})
# 	fees.save()
# 	fees.submit()	
# 	self.fees_id = fees.name

