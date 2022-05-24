import frappe
from frappe.model.document import Document

def validate(self,method):
    print("\n\n\n\n\n")
    print("ok")
    for d in self.get("references"):
        hostel_fee_info=frappe.get_all("Hostel Fees",filters=[["fees_id","=",d.reference_name]],fields=['name','outstanding_amount'])
        print(hostel_fee_info)
        if len(hostel_fee_info)>0:
            print(d.reference_name)
            print(d.fees_category)
            hostel_fee_comp=frappe.get_all("Fee Component",{"parent":hostel_fee_info[0]['name'],'fees_category':d.fees_category},["name","grand_fee_amount","outstanding_fees","fees_category"])
            print(hostel_fee_comp)

            # frappe.db.set_value("Fee Component",t['name'], "outstanding_fees",d.outstanding_amount) 
            pass
