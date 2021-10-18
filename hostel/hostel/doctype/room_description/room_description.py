# Copyright (c) 2021, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RoomDescription(Document):
	@frappe.whitelist()
	def validate(doc):
		room_description=doc.room_description
		start_date=doc.start_date
		end_date=doc.end_date
		if start_date<=end_date:
			Room_des_info=frappe.db.sql("""select * from `tabRoom Description` RD where 
			RD.room_description="%s" and (RD.start_date<= now() and RD.end_date>=now())"""%(room_description))
			if len(Room_des_info)==0:
				pass
			else:
				frappe.throw("Room Description already present and valid")
		else:
			frappe.throw("Kindly check the start date and End Date")
