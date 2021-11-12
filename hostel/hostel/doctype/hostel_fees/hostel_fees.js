// Copyright (c) 2021, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('Hostel Fees', {
	setup: function (frm) {
		frm.set_query("fee_structure", "fee_structure", function () {
			return {
				filters: [
					["Fee Structure Hostel", "room_type", "=", frm.doc.room_type]
				]
			}
		});
	}
})
