// Copyright (c) 2021, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on("Disciplinary Committee Meeting", "indisciplinary_complaint_registration_id", function(frm){
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
	// frappe.model.with_doc("Indisciplinary Actions", frm.doc.indisciplinary_action, function(){
	// 	var tabletransfer = frappe.model.get_doc("Indisciplinary Actions", frm.doc.indisciplinary_action);
	// 	//cur_frm.doc.indisciplinary_action = "";
	// 	cur_frm.doc.dc_members = "";
	// 	cur_frm.refresh_field("dc_members");
	// 	$.each(tabletransfer.dc_member, function(index, row){
	// 		var d = frappe.model.add_child(cur_frm.doc, "DC Members", "dc_members");
	// 		d.emp_id = row.emp_id;
	// 		d.employee_name = row.employee_name;
	// 		d.designation = row.designation;
	// 		d.contact_number = row.contact_number;
	// 		cur_frm.refresh_field("dc_members");
	// 	});
	// });
});


frappe.ui.form.on("Disciplinary Committee Meeting", "indisciplinary_complaint_registration_id", function(frm){
	frappe.model.with_doc("Indisciplinary Actions", frm.doc.indisciplinary_action, function(){
		var tabletransfer = frappe.model.get_doc("Indisciplinary Actions", frm.doc.indisciplinary_action);
		//cur_frm.doc.indisciplinary_action = "";
		cur_frm.doc.dc_members = "";
		cur_frm.refresh_field("dc_members");
		$.each(tabletransfer.dc_member, function(index, row){
			var d = frappe.model.add_child(cur_frm.doc, "DC Members", "dc_members");
			d.emp_id = row.emp_id;
			d.employee_name = row.employee_name;
			d.designation = row.designation;
			d.contact_number = row.contact_number;
			cur_frm.refresh_field("dc_members");
		});
	});
});


frappe.ui.form.on('Disciplinary Committee Meeting', {
	setup: function (frm) {
		frm.set_query("indisciplinary_action", function() {
			return {
				query: "hostel.hostel.doctype.disciplinary_committee_meeting.disciplinary_committee_meeting.status_query"
			};
		});
	}
})


