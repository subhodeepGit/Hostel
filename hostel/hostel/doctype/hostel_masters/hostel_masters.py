# Copyright (c) 2021, SOUL and contributors
# For license information, please see license.txt

from math import inf
import frappe
from frappe.model.document import Document
import datetime


class HostelMasters(Document):
	@frappe.whitelist()
	def validate(doc):
		hostel_name=doc.hostel_name
		start_date=datetime.datetime.strptime(doc.start_date,'%Y-%m-%d').date()
		end_date=datetime.datetime.strptime(doc.end_date,'%Y-%m-%d').date()

		Hostel=frappe.db.sql("""select * from `tabHostel Masters` HM WHERE (HM.hostel_name= "%s") 
		and (HM.start_date<=now() and HM.end_date >=now() )"""%(hostel_name))
		if len(Hostel)==0:
			if start_date<=end_date:
				pass
			else:
				frappe.throw("Kindly check the start date and End Date")
		else:
			end_date_info=Hostel[0][20]
			if end_date_info==end_date:
				pass
			else:
				al_info=frappe.db.sql("""SELECT * FROM `tabRoom Allotment` WHERE `hostel_id`="%s" and (`start_date`<=now() and `end_date`>=now())"""%(hostel_name))
				if len(al_info)==0:
					frappe.db.sql("""UPDATE `tabRoom Masters` SET `validity`="Dis-Approved" WHERE `hostel_id`="%s" and `validity`="Approved" """%(hostel_name))
					frappe.msgprint(
									msg='Corresponding Room has been Dis-Approved',
									title='Update',
									)
					pass
				else:
					frappe.throw("Can't be updated as students are already allotted in hostel")				

