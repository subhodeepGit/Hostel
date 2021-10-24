# Copyright (c) 2021, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class IndisciplinaryComplaintRegistration(Document):
	pass


# @frappe.whitelist()
# @frappe.validate_and_sanitize_search_inputs
# def ra_query(doctype, txt, searchfield, start, page_len, filters):
#     return frappe.db.sql("""
#         SELECT `name`,`student`,`student_name` FROM `tabRoom Allotment` WHERE `start_date` <= now() AND `end_date` >= now() 
#     """
#     )   