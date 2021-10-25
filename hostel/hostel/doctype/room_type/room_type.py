# Copyright (c) 2021, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RoomType(Document):
	@frappe.whitelist()
	def validate(doc):
		start_date=doc.start_date
		end_date=doc.end_date
		room_type=doc.room_type
		description=doc.description
		if start_date<=end_date:
			RT_info=frappe.db.sql("""SELECT * from `tabRoom Type` RT WHERE (RT.room_type="%s" and RT.description="%s") and (RT.start_date<=now() 
			and RT.end_date>=now())"""%(room_type,description))
			if len(RT_info)==0:
				pass
			else:
				frappe.throw("Room Type is already valid Kindly check")
		else:
			frappe.throw("Kindly check the start date and End Date")
