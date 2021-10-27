# Copyright (c) 2021, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.exceptions import Redirect
from frappe.model.document import Document
import pandas as pd
import datetime


class RoomAllotment(Document):
	@frappe.whitelist()
	def validate(doc):
		Stu_info=frappe.db.sql(""" select * from `tabRoom Allotment` as RA where RA.student="%s" """%(doc.student))
		df1=pd.DataFrame({
			'Al_no':[],'creation':[],'modified':[],'modified_by':[],
			'owner':[],'docstatus':[],'parent':[],'parentfield':[],
			'parenttype':[],'idx':[],'naming_series':[],'student':[],
			'student_name':[],'hostel_id':[],'start_date':[],'allotment_type':[],
			'end_date':[],'room_id':[],'room_type':[],'employee':[],'employee_name':[]
		})
		for t in range(len(Stu_info)):
			s=pd.Series([Stu_info[t][0],Stu_info[t][1],Stu_info[t][2],Stu_info[t][3],Stu_info[t][4],Stu_info[t][5],
						Stu_info[t][6],Stu_info[t][7],Stu_info[t][8],Stu_info[t][9],Stu_info[t][10],Stu_info[t][11],
						Stu_info[t][12],Stu_info[t][13],Stu_info[t][14],Stu_info[t][15],Stu_info[t][16],Stu_info[t][17],
						Stu_info[t][18],Stu_info[t][19],Stu_info[t][20]],
								index=['Al_no','creation','modified','modified_by',
										'owner','docstatus','parent','parentfield',
										'parenttype','idx','naming_series','student',
										'student_name','hostel_id','start_date','allotment_type',
										'end_date','room_id','room_type','employee','employee_name'])
			df1=df1.append(s,ignore_index=True)					
		if len(df1)==0:
			pass
		else:
			ck_data=df1[(df1['start_date']<=datetime.date.today())&(df1['end_date']>=datetime.date.today())].reset_index()
			if len(ck_data)!=0:
				frappe.throw("Student is already allotted in Hostel %s Room no %s"%(ck_data['hostel_id'][0],ck_data['room_id'][0]))
			else:
				pass


@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def test_query(doctype, txt, searchfield, start, page_len, filters):
	User=frappe.session.user
	if frappe.session.user!="Administrator":
		return frappe.db.sql("""
				SELECT `hostel_masters` from `tabEmployee Hostel Allotment` WHERE employees="%s" and
				(`start_date`<=now() and `end_date`>=now())"""%(User))
	else:
		return frappe.db.sql("""
				SELECT `hostel_name` from `tabHostel Masters` WHERE `start_date`<=now() and `end_date`>=now()""")			
			
# @frappe.whitelist()
# @frappe.validate_and_sanitize_search_inputs
# def test_query(doctype, txt, searchfield, start, page_len, filters):
# 	return frappe.db.sql("""
# 		SELECT hostel_name
# 		FROM `tabHostel Masters`
# 	"""
# 	)	

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def vacancy_query(doctype, txt, searchfield, start, page_len, filters):
	return frappe.db.sql("""SELECT HR.name,HR.room_number,HR.actual_capacity,HR.hostel_id, 
							(SELECT count(RA.room_id)
							from `tabRoom Allotment` RA
							WHERE RA.room_id=HR.name
							And (RA.start_date<=now() and RA.end_date>=now()) 
							)AS Vacancy 
							from `tabRoom Masters` as HR
							where HR.validity="Approved" """)	
