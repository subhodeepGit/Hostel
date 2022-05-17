# Copyright (c) 2021, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class StudentHostelAdmission(Document):
	
	# @frappe.whitelist()
	def before_save(doc):
		student = doc.student
		a=frappe.db.sql("""SELECT SA.Name 
						from `tabStudent Applicant` as SA 
						JOIN `tabStudent` S on S.student_applicant=SA.name
						WHERE S.name="%s" """%(student))
		if len(a)!=0:				
			pass
		else:
			frappe.throw("Student Applicant not maintained")

	# @frappe.whitelist()
	def on_submit(doc):
			student = doc.student
			frappe.db.sql(""" UPDATE `tabStudent Applicant` as SA 
								JOIN `tabStudent` S on S.student_applicant=SA.name
								SET SA.hostel_required = 1
								WHERE S.name="%s" """%(student))
			pass

	# @frappe.whitelist()
	def on_cancel(doc):
			student = doc.student
			frappe.db.sql(""" UPDATE `tabStudent Applicant` as SA 
								JOIN `tabStudent` S on S.student_applicant=SA.name
								SET SA.hostel_required = 0
								WHERE S.name="%s" """%(student))
			frappe.msgprint("Your Application is cancelled")
			pass

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def hostel_query(doctype, txt, searchfield, start, page_len, filters):
	return frappe.db.sql("""SELECT `name`,`hostel_type` from `tabHostel Masters` WHERE `start_date`<=now() and `end_date`>=now()""")


@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def room_query(doctype, txt, searchfield, start, page_len, filters):
	return frappe.db.sql("""SELECT `name`,`feature`,`capacity` from `tabRoom Type` WHERE `start_date`<=now() and `end_date`>=now()""")
