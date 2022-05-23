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

frappe.ui.form.on("Student Hostel Admission", "student", function(frm){
	frappe.model.with_doc("Student", frm.doc.student, function(){
		var tabletransfer = frappe.model.get_doc("Student", frm.doc.student);
		cur_frm.doc.current_education = "";
		cur_frm.refresh_field("current_education");
		$.each(tabletransfer.current_education, function(index, row){
			var d = frappe.model.add_child(cur_frm.doc, "Current Educational Details", "current_education_fetch");
			d.programs = row.programs;
			d.semesters = row.semesters;
			d.academic_year = row.academic_year;
			d.academic_term = row.academic_term;
			cur_frm.refresh_field("current_education_fetch");
		});
	});
});
