// Copyright (c) 2021, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('Room Change', {
	setup: function (frm) {
		frm.set_query("preferred_room", function () {
			return {
				filters: [
					["Room Masters", "hostel_id", "=", frm.doc.preferred_hostel]
				]
			}
		});
		// frm.set_query("allotment_number", function() {
		// 	return {
		// 		query: "hostel.hostel.doctype.room_change.room_change.ra_query"
		// 	};
		// });
	}
})

