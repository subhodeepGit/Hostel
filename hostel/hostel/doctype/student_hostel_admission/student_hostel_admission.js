// Copyright (c) 2021, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('Student Hostel Admission', {
	setup: function (frm) {
		frm.set_query("fee_structure", "fee_structure", function () {
			return {
				filters: [
					["Fee Structure Hostel", "room_type", "=", frm.doc.room_type]
				]
			}
		});
		frm.set_query("hostel", function() {
			return {
				query: "hostel.hostel.doctype.student_hostel_admission.student_hostel_admission.hostel_query"
			};
		});
		frm.set_query("room_type", function() {
			return {
				query: "hostel.hostel.doctype.student_hostel_admission.student_hostel_admission.room_query"
			};
		});
	}
})