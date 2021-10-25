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
		workflow_state=doc.workflow_state
		if workflow_state=="Notification To Administration":
			info=''' WHERE `allotment_number`="%s" and  workflow_state!="Close Application" '''%(Al_no)
			long_leave_df=Long_leave_def(info)
			if len(long_leave_df)==0:
				pass
			else:
				frappe.throw("Alreay Document ")
						







def Long_leave_def(info):
		Long_leave=frappe.db.sql("""SELECT name,allotment_number,student,student_name,hostel,room_number,start_date,data_11,medium_of_communicatinon,
									letter_attacmnent,phone_no,medium_of_communicatinon_from_student,communication_phone_no,repply_of_letter
								from `tabLong Leave`"""+info)

		Long_leave_df=pd.DataFrame({
				'long_leave_doc_no':[],'allotment_number':[],'student':[],'student_name':[],'hostel':[],'room_number':[],
								'start_date':[],'status':[],'medium_of_communicatinon':[],'letter_attacmnent':[],'phone_no':[],
								'medium_of_communicatinon_from_student':[],'communication_phone_no':[],'repply_of_letter':[]
			})
		
		for t in range(len(Long_leave)):
			s=pd.Series([Long_leave[t][0],Long_leave[t][1],Long_leave[t][2],Long_leave[t][3],Long_leave[t][4],Long_leave[t][5],
						Long_leave[t][6],Long_leave[t][7],Long_leave[t][8],Long_leave[t][9],Long_leave[t][10],Long_leave[t][11],
						Long_leave[t][12],Long_leave[t][13]],
								index=['long_leave_doc_no','allotment_number','student','student_name','hostel','room_number',
								'start_date','status','medium_of_communicatinon','letter_attacmnent','phone_no',
								'medium_of_communicatinon_from_student','communication_phone_no','repply_of_letter'])
			Long_leave_df=Long_leave_df.append(s,ignore_index=True)
		return Long_leave_df	
	