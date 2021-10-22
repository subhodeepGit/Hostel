# Copyright (c) 2021, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import pandas as pd

class LongLeave(Document):
	@frappe.whitelist()
	def validate(doc):
		Long_leave=frappe.db.sql("""SELECT `name`,`allotment_number`,`student`,`student_name`,`hostel`,`room_number`,`long_leave_start_date`,
		`medium_of_communication`,`reply_of_student`,`yes`,`no`,`reply_by_email__letter`,
		`confirmation_phone_number`,`pending` from `tabLong Leave`""")

		Long_leave_df=pd.DataFrame({
				'long_leave_doc_no':[],'allotment_number':[],'student':[],'student_name':[],
				'hostel':[],'room_number':[],'long_leave_start_date':[],'medium_of_communication':[],
				'reply_of_student':[],'yes':[],'no':[],'reply_by_email__letter':[],'confirmation_phone_number':[]
			})
		
		for t in range(len(Long_leave)):
			s=pd.Series([Long_leave[t][0],Long_leave[t][1],Long_leave[t][2],Long_leave[t][3],Long_leave[t][4],Long_leave[t][5],
						Long_leave[t][6],Long_leave[t][7],Long_leave[t][8],Long_leave[t][9],Long_leave[t][10],Long_leave[t][11],Long_leave[t][12]],
								index=['long_leave_doc_no','allotment_number','student','student_name',
										'hostel','room_number','long_leave_start_date','medium_of_communication',
										'reply_of_student','yes','no','reply_by_email__letter','confirmation_phone_number'])
			Long_leave_df=Long_leave_df.append(s,ignore_index=True)


