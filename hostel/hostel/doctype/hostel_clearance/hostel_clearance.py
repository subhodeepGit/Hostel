# Copyright (c) 2021, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class HostelClearance(Document):
	@frappe.whitelist()
	def validate(doc):
		Hol_cle_doc_no=doc.name
		allotment_number=doc.allotment_number
		due_status=doc.due_status
		type_of_clearance=doc.type_of_clearance
		end_date=doc.end_date
		due_amount=doc.due_amount
		reason_of_due=doc.reason_of_due
		workflow_state=doc.status
		pass
