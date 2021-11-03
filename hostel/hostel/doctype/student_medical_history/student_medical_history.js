// Copyright (c) 2021, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('Student Medical History', {
	setup: function (frm) {
		frm.set_query("allotment_number", function() {
			return {
				query: "hostel.hostel.doctype.room_change.room_change.ra_query"
			};
		});
	}
});
