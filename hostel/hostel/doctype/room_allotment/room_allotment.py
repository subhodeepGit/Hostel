# Copyright (c) 2021, SOUL and contributors
# For license information, please see license.txt

from dataclasses import fields
import re
import frappe
from frappe.exceptions import Redirect
from frappe.model.document import Document
import pandas as pd
import datetime


class RoomAllotment(Document):
	# @frappe.whitelist()
	def validate(doc):
		student=doc.student
		df1=vacancy_quety_vali("Student_info",student)					
		if len(df1)==0:
			pass
		else:
			ck_data=df1[(df1['start_date']<=datetime.date.today())&(df1['end_date']>=datetime.date.today())].reset_index()
			if len(ck_data)!=0:
				frappe.throw("%s is already allotted in %s, Room No. %s (%s)"%(ck_data['student_name'][0],ck_data['hostel_id'][0],ck_data['Room_No'][0],ck_data['room_id'][0]))	
			else:
				room_id=doc.room_id
				room_info_vac=vacancy_quety_vali("Genaral",room_id)
				if room_info_vac["validity"][0]=="Approved":
					if room_info_vac["Room_al_status"][0]=="Allotted":
						if room_info_vac["Vacancy"][0]>0:
							ck_data=df1[(df1['allotment_type']=="Debar") | (df1['allotment_type']=="University Debar") | (df1['allotment_type']=="Passout")
										| (df1['allotment_type']=="Cancellation of Admission") | (df1['allotment_type']=="Death") ].reset_index()
							if len(ck_data)==0:
								pass
							else:
								frappe.throw("Student can't be allotted")
						else:
							Al_stu=vacancy_quety_vali("Alloted_student",room_id)
							a=""
							for t in range(len(Al_stu)):
								b="%s "%(Al_stu["Al_no"][t])
								a=a+b
							frappe.throw("Already Room is full with allotment No. "+a)
					else:
						frappe.throw("Room is not allottable for the student")
				else:
					frappe.throw("Room is not valid")	
				
	# @frappe.whitelist()
	def on_submit(doc):
		room_id=doc.room_id
		# room_info_vac=vacancy_quety_vali("Genaral",room_id)
		# if room_info_vac["validity"][0]=="Approved":
		# 	if room_info_vac["Room_al_status"][0]=="Allotted":
		# 		if room_info_vac["Vacancy"][0]>0:
		# 			room_id=doc.room_id
		# 			frappe.db.sql("""UPDATE `tabRoom Masters` SET `vacancy`=`vacancy`-1 WHERE `name`="%s" """%(room_id)) 
		# 			frappe.db.set_value("Student Hostel Admission",doc.hostel_registration_no, "allotment_status", "Allotted") 
		# 			pass
		# 		else:
		# 			Al_stu=vacancy_quety_vali("Alloted_student",room_id)
		# 			a=""
		# 			for t in range(len(Al_stu)):
		# 				b="%s "%(Al_stu["Al_no"][t])
		# 				a=a+b
		# 			frappe.throw("Already Room is full with Allotment No. "+a)
		# 	else:
		# 		frappe.throw("Room is not allottable to the student")
		# else:
		# 	frappe.throw("Room is not valid")
		frappe.db.sql("""UPDATE `tabRoom Masters` SET `vacancy`=`vacancy`-1 WHERE `name`="%s" """%(room_id)) 
		frappe.db.set_value("Student Hostel Admission",doc.hostel_registration_no, "allotment_status", "Allotted") 


	# @frappe.whitelist()
	def on_cancel(doc):
		room_id=doc.room_id
		frappe.db.sql("""UPDATE `tabRoom Masters` SET `vacancy`=`vacancy`+1 WHERE `name`="%s" """%(room_id))
		frappe.db.set_value("Student Hostel Admission",doc.hostel_registration_no, "allotment_status", "Cancelled") 
	


@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def test_query(doctype, txt, searchfield, start, page_len, filters):
	User=frappe.session.user
	if frappe.session.user!="Administrator":
		return frappe.db.sql("""
				SELECT `hostel_masters` from `tabEmployee Hostel Allotment` WHERE user_name="%s" and
				(`start_date`<=now() and `end_date`>=now())"""%(User))
	else:
		return frappe.db.sql("""
				SELECT `hostel_name` from `tabHostel Masters` WHERE `start_date`<=now() and `end_date`>=now()""")			
			
	



def vacancy_quety_vali(flag,info):
	if flag=="Genaral":
		vac_info=frappe.db.sql("""SELECT HR.name,HR.room_number,HR.actual_capacity,HR.hostel_id,HR.validity,HR.room_description,HR.status,
								(HR.actual_capacity-(SELECT count(RA.room_id)
								from `tabRoom Allotment` RA
								WHERE RA.room_id=HR.name
								And (RA.start_date<=now() and RA.end_date>=now()) and RA.docstatus!=2 and RA.docstatus!=0
								))AS Vacancy 
								from `tabRoom Masters` as HR
								where HR.name="%s" """%(info))
		df1=pd.DataFrame({
			"Room_id":[],"room_number":[],"present_capacity":[],"hostel_id":[],"validity":[],"room_description":[],"Room_al_status":[],"Vacancy":[] 
			})
		for t in range(len(vac_info)):
			s=pd.Series([vac_info[t][0],vac_info[t][1],vac_info[t][2],vac_info[t][3],vac_info[t][4],vac_info[t][5],vac_info[t][6],vac_info[t][7]],
								index=["Room_id","room_number","present_capacity","hostel_id","validity","room_description","Room_al_status","Vacancy"])
			df1=df1.append(s,ignore_index=True)			
		return df1
	elif flag=="Student_info":	
		# Stu_info=frappe.db.sql(""" select * from `tabRoom Allotment` as RA where RA.student="%s" and RA.docstatus!=2 """%(info))

		Stu_info=frappe.db.sql(""" select name,creation,modified,modified_by,owner,docstatus,parent,parentfield,parenttype,
			idx,naming_series,student,student_name,hostel_id,start_date,allotment_type,end_date,room_id,
			room_type,employee,employee_name,room_number from `tabRoom Allotment` where student="%s" and docstatus!=2 and docstatus!=0 """%(info))


		df1=pd.DataFrame({
			'Al_no':[],'creation':[],'modified':[],'modified_by':[],
			'owner':[],'docstatus':[],'parent':[],'parentfield':[],
			'parenttype':[],'idx':[],'naming_series':[],'student':[],
			'student_name':[],'hostel_id':[],'start_date':[],'allotment_type':[],
			'end_date':[],'room_id':[],'room_type':[],'employee':[],'employee_name':[],'Room_No':[]
		})
		for t in range(len(Stu_info)):
			s=pd.Series([Stu_info[t][0],Stu_info[t][1],Stu_info[t][2],Stu_info[t][3],Stu_info[t][4],Stu_info[t][5],
						Stu_info[t][6],Stu_info[t][7],Stu_info[t][8],Stu_info[t][9],Stu_info[t][10],Stu_info[t][11],
						Stu_info[t][12],Stu_info[t][13],Stu_info[t][14],Stu_info[t][15],Stu_info[t][16],Stu_info[t][17],
						Stu_info[t][18],Stu_info[t][19],Stu_info[t][20],Stu_info[t][21]],
								index=['Al_no','creation','modified','modified_by',
										'owner','docstatus','parent','parentfield',
										'parenttype','idx','naming_series','student',
										'student_name','hostel_id','start_date','allotment_type',
										'end_date','room_id','room_type','employee','employee_name','Room_No'])
			df1=df1.append(s,ignore_index=True)	
		return df1
	elif flag=="Alloted_student":
		stu_info=frappe.db.sql("""SELECT `name`,`room_id` FROM `tabRoom Allotment` WHERE `room_id`="%s" and (`start_date`<=now() and `end_date`>=now())"""%(info))
		df1=pd.DataFrame({
			"Al_no":[],"room_id":[]
		})		
		for t in range(len(stu_info)):
			s=pd.Series([stu_info[t][0],stu_info[t][1]],
								index=["Al_no","room_id"])
			df1=df1.append(s,ignore_index=True)	
		return df1	




@frappe.whitelist()
# @frappe.validate_and_sanitize_search_inputs
def hostel_req_query(doctype, txt, searchfield, start, page_len, filters):						
	# return frappe.db.sql(""" SELECT S.name,SA.name,SA.hostel_required,S.title
	# 						from `tabStudent Applicant` as SA
	# 						JOIN `tabStudent` S on S.student_applicant=SA.name 
	# 						where SA.hostel_required=1""") ##### Student Applicant
	############################## Search Field Code################# 
	searchfields = frappe.get_meta(doctype).get_search_fields()
	searchfields = " or ".join("S."+field + " like %(txt)s" for field in searchfields)

	data=frappe.db.sql(""" SELECT S.name,SHA.name,S.title from `tabStudent Hostel Admission` as SHA 
							JOIN `tabStudent` S on S.name=SHA.student 
							where (SHA.{key} like %(txt)s or {scond})  and 
	       					SHA.allotment_status="Not Reported" and SHA.docstatus=1 """.format(
								**{
									"key": searchfield,
									"scond": searchfields,
								}),{"txt": "%%%s%%" % txt, "start": start, "page_len": page_len})


	# return frappe.db.sql(""" SELECT S.name,SHA.name,S.title from `tabStudent Hostel Admission` as SHA 
	# 						JOIN `tabStudent` S on S.name=SHA.student 
	# 						where SHA.allotment_status="Not Reported" and SHA.docstatus=1 """)
	return data
						

@frappe.whitelist()
# @frappe.validate_and_sanitize_search_inputs
def allotment(student):
	data=frappe.get_all("Student Hostel Admission",fields=[["student","=",student],["allotment_status","!=","Allotted"],
					["allotment_status","!=","De-Allotted"],["docstatus","=",1]])
	if len(data)>0:
		return data[0]
			

@frappe.whitelist()
# @frappe.validate_and_sanitize_search_inputs
def employee():
	user=frappe.session.user
	if user == "Administrator":
		pass
	else:
		employee_name=frappe.get_all("Employee",fields=[["prefered_email","=",user]])
	if user == "Administrator":
		name=""
	else:
		name=employee_name[0]['name']
	if len(name)>0:
		return name
	
