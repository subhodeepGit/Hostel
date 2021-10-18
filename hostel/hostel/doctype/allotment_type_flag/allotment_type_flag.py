# Copyright (c) 2021, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AllotmentTypeFlag(Document):
	def validate(doc):
		description=doc.description
		Alt_Type=frappe.db.sql("""SELECT * FROM `tabAllotment Type Flag` ATF WHERE ATF.description="%s" 
								"""%(description))
		if len(Alt_Type)==0:
			pass
		else:
			frappe.throw("Already Allotment type exist in the list")
