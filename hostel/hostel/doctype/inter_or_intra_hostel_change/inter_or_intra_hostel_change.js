// Copyright (c) 2021, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('Inter or Intra Hostel Change', {
	setup: function (frm) {
		frm.set_query("allotment_no", function() {
			return {
				query: "hostel.hostel.doctype.room_change.room_change.ra_query"
			};
		});
		frm.set_query("second_allotment_no", function() {
			return {
				query: "hostel.hostel.doctype.room_change.room_change.ra_query"
			};
		});
	}
});
