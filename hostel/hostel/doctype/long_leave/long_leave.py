# Copyright (c) 2021, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import pandas as pd

class LongLeave(Document):
	@frappe.whitelist()
	def validate(doc):
		long_leave=doc.name
		Al_no=doc.allotment_number
		status_of_reporting=doc.status_of_reporting
		info=''' WHERE `allotment_number`="%s" and `status_of_reporting`!="Close Application"'''%(Al_no)
		Long_leave_df=Long_leave_def(info)
		if len(Long_leave_df)==0 or (Long_leave_df['long_leave_doc_no'][0]==long_leave and Long_leave_df['status_of_reporting'][0]==None):
			if 	len(Long_leave_df)==0 and status_of_reporting=="Notification To Administration":
				status_of_reporting = "Notification To Administration"
				#frappe.db.sql(""" UPDATE `tabLong Leave` SET `status`="%s" WHERE `name`="%s" """%(status_of_reporting,long_leave))
				pass
			else:
				frappe.throw("Please change Status of Reporting to 'Notification To Administration' ")	
		elif len(Long_leave_df)!=0 and Long_leave_df['long_leave_doc_no'][0]==long_leave and \
			Long_leave_df['status_of_reporting'][0]=="Notification To Administration":
			medium_of_communication=doc.medium_of_communication
			if status_of_reporting=="Communication to the Student":
				if medium_of_communication=="Telephone":
					phone_number=int(doc.phone_number)
					if phone_number!=0 and phone_number!=None:
						frappe.db.sql("""UPDATE `tabLong Leave` SET `status_of_application`="%s" WHERE `name`="%s" """%(status_of_reporting,long_leave))
						pass
					else:
						frappe.throw("Communication Phone No is not Mentioned")
				elif medium_of_communication=="Letter / Email":
					attach_email=doc.attach_email
					if attach_email!=None:
						frappe.db.sql("""UPDATE `tabLong Leave` SET `status`="%s" WHERE `name`="%s" """%(status_of_reporting,long_leave))
						pass
					else:
						frappe.throw("letter is not attached")
				else:
					frappe.throw("No Communication Mediam Mantained")				
			else:
				frappe.throw("No communication has been made by University/ College to the students") 	
		elif len(Long_leave_df)!=0 and Long_leave_df['long_leave_doc_no'][0]==long_leave and \
			Long_leave_df['status_of_reporting'][0]=="Communication to the Student":
			info="""UPDATE `tabLong Leave` SET `docstatus` = '1' WHERE `tabLong Leave`.`name` = 'LL-2021-00002';"""
			#frappe.db.sql("""UPDATE `tabLong Leave` SET `status`="%s" WHERE `name`="%s" """%(status_of_reporting,long_leave))
			
			pass					
		else:
			frappe.throw("Application is open on Doc No %s"%(Long_leave_df['long_leave_doc_no'][0]))


		



def Long_leave_def(info):
		Long_leave=frappe.db.sql("""SELECT `name`,`allotment_number`,`student`,`student_name`,`hostel`,`room_number`,`long_leave_start_date`,
		`medium_of_communication`,`reply_of_student`,`yes`,`no`,`reply_by_email__letter`,
		`confirmation_phone_number`,`pending`,`status_of_reporting` from `tabLong Leave`"""+info)

		Long_leave_df=pd.DataFrame({
				'long_leave_doc_no':[],'allotment_number':[],'student':[],'student_name':[],
				'hostel':[],'room_number':[],'long_leave_start_date':[],'medium_of_communication':[],
				'reply_of_student':[],'yes':[],'no':[],'reply_by_email__letter':[],'confirmation_phone_number':[],'pending':[],'status_of_reporting':[]
			})
		
		for t in range(len(Long_leave)):
			s=pd.Series([Long_leave[t][0],Long_leave[t][1],Long_leave[t][2],Long_leave[t][3],Long_leave[t][4],Long_leave[t][5],
						Long_leave[t][6],Long_leave[t][7],Long_leave[t][8],Long_leave[t][9],Long_leave[t][10],Long_leave[t][11],
						Long_leave[t][12],Long_leave[t][13],Long_leave[t][14]],
								index=['long_leave_doc_no','allotment_number','student','student_name',
										'hostel','room_number','long_leave_start_date','medium_of_communication',
										'reply_of_student','yes','no','reply_by_email__letter','confirmation_phone_number','pending','status_of_reporting'])
			Long_leave_df=Long_leave_df.append(s,ignore_index=True)
		return Long_leave_df	