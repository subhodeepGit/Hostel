# Copyright (c) 2021, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import pandas as pd

class IndisciplinaryActions(Document):
	@frappe.whitelist()
	def before_save(doc):
		#doc status-0
		type_of_decision=doc.type_of_decision
		if type_of_decision=="Warning Letter":
			date_of_letter=doc.date_of_letter
			attachment_of_warnning_letter=doc.attachment_of_warnning_letter

			if date_of_letter!=None and attachment_of_warnning_letter!=None:
				pass
			else:
				frappe.throw("Kindly provide 'Date of Letter Issue' and 'Attach the Warning Letter'")
		elif type_of_decision=="Fine Letter":
			issue_of_letter=doc.issue_of_letter
			attachment_of_fine_letter=doc.attachment_of_fine_letter
			fine_amount=doc.fine_amount
			if issue_of_letter!=None and attachment_of_fine_letter!=None and fine_amount!=None:
				pass
			else:
				frappe.throw("Kindly provide 'Date of Letter Issue' and 'Fine Letter'")		
		elif type_of_decision=="Suspension Letter":
			issue_of_suspension_letter=doc.issue_of_suspension_letter
			attachment_of_suspention_letter=doc.attachment_of_suspention_letter
			type_of_suspension=doc.type_of_suspension
			if type_of_suspension!="":
				if attachment_of_suspention_letter!=None and attachment_of_suspention_letter!=None:
					indisciplinary_complaint_registration_id=doc.indisciplinary_complaint_registration_id
					info=frappe.db.sql("""SELECT `allotment_number` from `tabIndisciplinary Complaint Registration Student` WHERE `parent`="%s" """%\
													(indisciplinary_complaint_registration_id))						
					for t in range(len(info)):
						frappe.db.sql("""UPDATE `tabRoom Allotment` SET `allotment_type`="%s" WHERE `name`="%s" """%(type_of_suspension,info[t][0]))							
					pass
				else:
					frappe.throw("Kindly provide 'Date of Letter Issue' and 'Suspension Letter'")
			else:
				frappe.throw("Suspention Type Not Selected")		
		elif type_of_decision=="Debar Letter":
			issue_of_debar_letter=doc.issue_of_debar_letter
			attachment_of_debar_letter=doc.attachment_of_debar_letter
			if issue_of_debar_letter!=None and attachment_of_debar_letter: 
				indisciplinary_complaint_registration_id=doc.indisciplinary_complaint_registration_id
				info=frappe.db.sql("""SELECT `allotment_number` from `tabIndisciplinary Complaint Registration Student` WHERE `parent`="%s" """%\
												(indisciplinary_complaint_registration_id))	
				type_of_suspension="Debar Letter"													
				for t in range(len(info)):
					frappe.db.sql("""UPDATE `tabRoom Allotment` SET `allotment_type`="%s" WHERE `name`="%s" """%(type_of_suspension,info[t][0]))
				pass
			else:
				frappe.throw("Kindly provide 'Date of Letter Issue' and 'Debar Letter'")
		elif type_of_decision=="Parents Call Letter":

			pass
		else:
			frappe.throw("No field selected")
	@frappe.whitelist()		
	def on_update(doc):
		type_of_decision=doc.type_of_decision
		if type_of_decision=="Disciplinary Committee":
			ia_id = doc.name
			in_doc_info=frappe.db.sql("""SELECT * FROM `tabIndisciplinary Actions` where  name="%s" """%(ia_id))
			if len(in_doc_info)!=0:
				ia = frappe.get_doc("Indisciplinary Actions",ia_id)
				emp_df = pd.DataFrame({
					'Emp_no':[]
				})
				for al in ia.dc_member:
					s = pd.Series([al.emp_id],index = ['Emp_no'])
					emp_df = emp_df.append(s,ignore_index = True)
				duplicate = emp_df[emp_df.duplicated()].reset_index()
				if len(duplicate) == 0:
					pass
				else:
					b=""
					for t in range(len(duplicate)):
						a="%s  "%(duplicate['Emp_no'][t])
						b=b+a
					frappe.throw("Duplicate value found on Employee ID "+b)
			else:
				pass 

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def status_query(doctype, txt, searchfield, start, page_len, filters):
	return frappe.db.sql("""
		SELECT `name` FROM `tabIndisciplinary Complaint Registration` WHERE `status` = "Open"
	"""
	)