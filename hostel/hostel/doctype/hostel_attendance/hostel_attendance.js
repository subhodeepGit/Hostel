// Copyright (c) 2021, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('Hostel Attendance', {
	setup: function (frm) {
		frm.set_query("room_allotment_no", function() {
			return {
				query: "hostel.hostel.doctype.hostel_attendance.hostel_attendance.ra_query"
			};
		});
	}
})