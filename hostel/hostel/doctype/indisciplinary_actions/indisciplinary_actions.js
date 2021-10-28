// Copyright (c) 2021, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on("Indisciplinary Actions", "indisciplinary_complaint_registration_id", function(frm){
	frappe.model.with_doc("Indisciplinary Complaint Registration", frm.doc.indisciplinary_complaint_registration_id, function(){
		var tabletransfer = frappe.model.get_doc("Indisciplinary Complaint Registration", frm.doc.indisciplinary_complaint_registration_id);
		cur_frm.doc.student_fetch = "";
		cur_frm.refresh_field("student_fetch");
		$.each(tabletransfer.student, function(index, row){
			var d = frappe.model.add_child(cur_frm.doc, "Indisciplinary Complaint Registration Student", "student_fetch");
			d.allotment_number = row.allotment_number;
			d.student = row.student;
			d.student_name = row.student_name;
			d.allotment_type = row.allotment_type;
			d.room_number = row.room_number;
			d.room_type = row.room_type;
			cur_frm.refresh_field("student_fetch");
		});
	});
});
