from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'transactions': [
			{
				'label': _('Fee'),
				'items': ['Fees', 'Payment Entry', 'Hostel Fees']
			},
            {
                'label': _('Room'),
				'items': ['Room Allotment']
            },
            {
                'label': _('Indisciplinary'),
				'items': ['Indisciplinary Actions']
            }
		]
	}