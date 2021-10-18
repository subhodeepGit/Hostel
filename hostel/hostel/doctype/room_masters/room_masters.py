# Copyright (c) 2021, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RoomMasters(Document):
	@frappe.whitelist()
	def validate(doc):
		hostel_id=doc.hostel_id
		room_number=doc.room_number
		Hostel=frappe.db.sql(""" SELECT * from `tabRoom Masters` RM WHERE RM.hostel_id="%s" 
								and RM.room_number="%s" and RM.validity="Approved" """%(hostel_id,room_number))
		if len(Hostel)==0:
			pass
		else:
			frappe.throw("Room is already present in the %s room no %s doc no %s"%(hostel_id,room_number,Hostel[0][0]))						

