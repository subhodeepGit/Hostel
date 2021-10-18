// Copyright (c) 2021, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('Room Allotment', {
	setup: function (frm) {
		frm.set_query("room_id", function () {
			return {
				filters: [
					["Room Masters", "hostel_id", "=", frm.doc.hostel_id]
				]
			}
		});
		frm.set_query("hostel_id", function() {
			return {
				query: "hostel.hostel.doctype.room_allotment.room_allotment.test_query"
			};
		});
	}
})