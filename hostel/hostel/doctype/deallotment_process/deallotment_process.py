# Copyright (c) 2021, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import pandas as pd

class DeallotmentProcess(Document):
	#frappe.db.sql(""" UPDATE `tabEmployee Hostel Allotment`  SET  start_date= '2000-09-01' where name='RAN-2021-00001';""")	
	# @frappe.whitelist()
	def validate(doc):
		Al_no=doc.allotment_number
		workflow_state=doc.workflow_state
		End_date=doc.end_date
		De_allotment_info=frappe.db.sql("""select `name`,`allotment_number`,`student`,`student_name`,`hostel`,`room_number`,
		`room_no`,`workflow_state`,`room_type`,`application_status` FROM `tabDeallotment Process` WHERE `allotment_number`= "%s" """%(Al_no))
		De_allotment_df=pd.DataFrame({
			'Deall_doc_no':[],'allotment_number':[],'student':[],'student_name':[],
			'hostel':[],'Room_id':[],'Room_no':[],'workflow_state':[],
			'room_type':[],'application_status':[]
		})
		for t in range(len(De_allotment_info)):
			s=pd.Series([De_allotment_info[t][0],De_allotment_info[t][1],De_allotment_info[t][2],De_allotment_info[t][3],De_allotment_info[t][4],De_allotment_info[t][5],
						De_allotment_info[t][6],De_allotment_info[t][7],De_allotment_info[t][8],De_allotment_info[t][9]],
								index=['Deall_doc_no','allotment_number','student','student_name',
										'hostel','Room_id','Room_no','workflow_state','room_type','application_status'])
			De_allotment_df=De_allotment_df.append(s,ignore_index=True)
		Chk_df=De_allotment_df[(De_allotment_df['workflow_state']!="Clearence From Hostel")|
								(De_allotment_df['workflow_state']!="Rejected")|
								(De_allotment_df['workflow_state']!="Withdrawl of Application")]	
		if workflow_state=="Submit":
			Chk_df=Chk_df[(Chk_df['application_status'].isnull())|(Chk_df['application_status']=="Open")].reset_index()
			if len(Chk_df)!=0:
				frappe.throw("Document already Present Dco no %s"%(Chk_df['Deall_doc_no'][0]))
			else:
				pass
		elif workflow_state=="Clearence From Hostel":
			if End_date==None:
				frappe.throw("Please provide End Date")	
			else:
				Al_data=frappe.db.sql("""select `start_date`,`end_date`,`room_id` from `tabRoom Allotment` as RA WHERE `name`="%s" """%(Al_no))
				al_st_date=Al_data[0][0]
				al_end_date=Al_data[0][1]
				room_id=Al_data[0][2]
				if al_st_date<=End_date and al_end_date>=End_date:
					frappe.db.sql("""UPDATE `tabRoom Allotment` SET `end_date`="%s",`allotment_type`="De-Allotted" WHERE `name`="%s" """%(End_date,Al_no))
					frappe.db.sql("""UPDATE `tabRoom Masters` SET `vacancy`=`vacancy`+1 WHERE `name`="%s" """%(room_id))
					pass
				else:
					frappe.throw("End date is not in range of allotment no:- %s"%(Al_no))