from __future__ import unicode_literals
import frappe
from frappe import _
import frappe.model
import frappe.utils
import json, os
from frappe.utils import get_safe_filters
from frappe.desk.reportview import validate_args
from frappe.model.db_query import check_parent_permission
from datetime import date

from six import iteritems, string_types, integer_types

@frappe.whitelist()
def get(name=None, filters=None, parent=None):
    print("\n\n\n\n\n\n")
    print(name)
    '''Returns a document by name or filters

    :param doctype: DocType of the document to be returned
    :param name: return document of this `name`
    :param filters: If name is not set, filter by these values and return the first match'''
	# if frappe.is_table(doctype):
	# 	check_parent_permission(parent, doctype)

	# if filters and not name:
	# 	name = frappe.db.get_value(doctype, json.loads(filters))
	# 	if not name:
	# 		frappe.throw(_("No document found for given filters"))

	# doc = frappe.get_doc(doctype, name)
	# if not doc.has_permission("read"):
	# 	raise frappe.PermissionError

	# return frappe.get_doc(doctype, name).as_dict()
    room_allotment_data=frappe.get_all("Room Allotment",filters=[["student","=",name],["start_date","<=",date.today()],["end_date",">=",date.today()]],
                                        fields=['hostel_id','room_number','room_id','room_type'])
    return room_allotment_data
    