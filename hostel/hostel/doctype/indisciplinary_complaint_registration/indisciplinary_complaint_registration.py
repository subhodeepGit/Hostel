# Copyright (c) 2021, SOUL and contributors
# For license information, please see license.txt

from re import I
import frappe
from frappe.model.document import Document
import pandas as pd

class IndisciplinaryComplaintRegistration(Document):
    @frappe.whitelist()
    def on_update(self):
        icr_id = self.name
        in_doc_info=frappe.db.sql("""select * from `tabIndisciplinary Complaint Registration` where  name="%s" """%(icr_id))
        if len(in_doc_info)!=0:
            icr = frappe.get_doc("Indisciplinary Complaint Registration",icr_id)
            stu_df = pd.DataFrame({
                'Al_no':[]
            })
            for al in icr.student:
                s = pd.Series([al.allotment_number],index = ['Al_no'])
                stu_df = stu_df.append(s,ignore_index = True)
            duplicate = stu_df[stu_df.duplicated()].reset_index()
            if len(duplicate) == 0:
                pass
            else:
                b=""
                for t in range(len(duplicate)):
                    a="%s  "%(duplicate['Al_no'][t])
                    b=b+a
                frappe.throw("Duplicate value found on allotment number "+b)
        else:
            pass  





@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def ra_query(doctype, txt, searchfield, start, page_len, filters):
    return frappe.db.sql("""
        SELECT `name`,`student`,`student_name` FROM `tabRoom Allotment` WHERE `start_date` <= now() AND `end_date` >= now() 
    """
    )   