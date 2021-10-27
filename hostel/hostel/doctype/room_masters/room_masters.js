// Copyright (c) 2021, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('Room Masters', {
	setup: function (frm) {
		frm.set_query("room_type_id", function () {
			return {
				query: "hostel.hostel.doctype.room_masters.room_masters.room_type_query",
			}
		});
		frm.set_query("actual_room_type", function() {
			return {
				query: "hostel.hostel.doctype.room_masters.room_masters.room_type_query"
			};
		});
		frm.set_query("room_description", function() {
			return {
				query: "hostel.hostel.doctype.room_masters.room_masters.room_description_query"
			};
		});
	}
})
