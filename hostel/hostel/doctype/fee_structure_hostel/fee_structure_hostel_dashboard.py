from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'transactions': [
			{
				'label': _('Fee'),
				'items': ['Hostel Fees', 'Hostel Fee Schedule']
			}
		]
	}