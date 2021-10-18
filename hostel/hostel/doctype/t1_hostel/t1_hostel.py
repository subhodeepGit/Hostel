# Copyright (c) 2021, SOUL and contributors
# For license information, please see license.txt

from frappe.model.document import Document
"""build query for doclistview and return results"""
import frappe, json
import frappe.permissions
from frappe.model.db_query import DatabaseQuery
from frappe import _

class T1Hostel(Document):
	@frappe.whitelist()
	def get():
		return compress(execute(**get_form_params()))
		
	def validate(doc):
		a=frappe.db.get_list('Allotment Type Flag')
		print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n\n")
		print(a)

		"""Stringify GET request parameters."""
		data = frappe._dict(frappe.local.form_dict)
		print("\n\n\n\n\n")
		print(data)
		return data
	def compress(data):
		"""separate keys and values"""
		if not data: return data
		values = []
		keys = data[0].keys()
		for row in data:
			new_row = []
			for key in keys:
				new_row.append(row[key])
			values.append(new_row)

		print(data)	
