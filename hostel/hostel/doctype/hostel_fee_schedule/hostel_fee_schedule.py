# Copyright (c) 2022, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class HostelFeeSchedule(Document):
	global length
	
	def validate(self):
		self.calculate()
	def calculate(self):
		a=frappe.db.sql(""" Select RA.*,CED.*,RA.name as room_allotment  from `tabRoom Allotment` as RA
				Join `tabCurrent Educational Details` as CED on CED.parent=RA.Student
				where CED.programs="%s" and CED.semesters="%s" and CED.academic_term="%s" and CED.academic_year="%s" and (RA.room_type="%s" and RA.docstatus=1 and (RA.start_date <=now() and RA.end_date>=now()))
				"""%(self.programs,self.program,self.academic_term,self.academic_year,self.room_type),as_dict = True)
		length=len(a)  
		self.grand_total=self.total_amount*length

		
	def on_submit(self):
		pass	

@frappe.whitelist()
def get_students(academic_term=None, programs=None,program=None,academic_year=None,room_type=None):   
	a=frappe.db.sql(""" Select RA.*,CED.*,RA.name as room_allotment  from `tabRoom Allotment` as RA
	Join `tabCurrent Educational Details` as CED on CED.parent=RA.Student
	where CED.programs="%s" and CED.semesters="%s" and CED.academic_term="%s" and CED.academic_year="%s" and (RA.room_type="%s" and RA.docstatus=1 and (RA.start_date <=now() and RA.end_date>=now()))
	"""%(programs,program,academic_term,academic_year,room_type),as_dict = True)
	length=len(a)       
	return a
