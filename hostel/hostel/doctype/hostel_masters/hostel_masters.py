# Copyright (c) 2021, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class HostelMasters(Document):
	@frappe.whitelist()
	def validate(doc):
		hostel_name=doc.hostel_name
		hostel_short_name=doc.hostel_short_name
		start_date=doc.start_date
		end_date=doc.end_date

		Hostel=frappe.db.sql("""select * from `tabHostel Masters` HM WHERE (HM.hostel_name= "%s" or HM.hostel_short_name="%s") 
		and (HM.start_date<=now() and HM.end_date >=now() )"""%(hostel_name,hostel_short_name))
		if start_date<=end_date:
			if len(Hostel)==0:
				pass
			else:
				frappe.throw("Hostel already created kindly check the list")
		else:
			frappe.throw("Kindly check the start date and End Date")		

