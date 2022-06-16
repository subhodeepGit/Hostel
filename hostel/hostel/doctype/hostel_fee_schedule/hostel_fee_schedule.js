// Copyright (c) 2022, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on("Hostel Fee Schedule", {
    get_students:function(frm){
        frm.clear_table("student_room_alloted");
        frappe.call({
            method: "hostel.hostel.doctype.hostel_fee_schedule.hostel_fee_schedule.get_students",
            args:{
                programs: frm.doc.programs,
                program: frm.doc.program,
                academic_term: frm.doc.academic_term,
                academic_year: frm.doc.academic_year,
                room_type: frm.doc.room_type

            },
        
            callback: function(r) {
                (r.message).forEach(element => {
                    var row = frm.add_child("student_room_alloted")
                    row.room_allotment_id=element.room_allotment
                    row.hostel_registration_no=element.hostel_registration_no
                });
                frm.refresh_field("student_room_alloted")
                frm.save();
            }
        });
        frappe.realtime.on('fee_schedule_progress', function(data) {
			if (data.reload && data.reload === 1) {
				frm.reload_doc();
			}
			if (data.progress) {
				let progress_bar = $(cur_frm.dashboard.progress_area.body).find('.progress-bar');
				if (progress_bar) {
					$(progress_bar).removeClass('progress-bar-danger').addClass('progress-bar-success progress-bar-striped');
					$(progress_bar).css('width', data.progress+'%');
				}
			}
		});

		erpnext.accounts.dimensions.setup_dimension_filters(frm, frm.doctype);
	},
// Dashboard and Custom Button and Accounting Ledger
    refresh: function(frm) {
		if (!frm.doc.__islocal && frm.doc.__onload && frm.doc.__onload.dashboard_info &&
			frm.doc.fee_creation_status === 'Successful') {
			var info = frm.doc.__onload.dashboard_info;
			frm.dashboard.add_indicator(__('Total Collected: {0}', [format_currency(info.total_paid,
				info.currency)]), 'blue');
			frm.dashboard.add_indicator(__('Total Outstanding: {0}', [format_currency(info.total_unpaid,
				info.currency)]), info.total_unpaid ? 'orange' : 'green');
		}
		if (frm.doc.fee_creation_status === 'In Process') {
			frm.dashboard.add_progress('Fee Creation Status', '0');
		}
		if( frappe.user.has_role(["Accounts User","Student"]) && !frappe.user.has_role(["Education Administrator"])){
			frm.remove_custom_button(__("Create Fees"));
		}
		else if (frm.doc.docstatus === 1 && !frm.doc.fee_creation_status || frm.doc.fee_creation_status === 'Failed') {
			frm.add_custom_button(__('Create Fees'), function() {
				frappe.call({
					method: 'create_fees',
					doc: frm.doc,
					callback: function() {
						frm.refresh();
					}
				});
			}).addClass('btn-primary');;
		}
		else {
		}
		if (frm.doc.fee_creation_status === 'Successful') {
			frm.add_custom_button(__('View Fees Records'), function() {
				frappe.route_options = {
					fee_schedule: frm.doc.name
				};
				frappe.set_route('List', 'Hostel Fees');
			});
		}
        if (frm.doc.fee_creation_status === 'Successful') {
			frm.add_custom_button(__('Accounting Ledger'), function() {
				frappe.route_options = {
                    voucher_no: frm.doc.name,
					from_date: frm.doc.posting_date,
					to_date: moment(frm.doc.modified).format('YYYY-MM-DD'),
					company: frm.doc.company,
					group_by: '',
					show_cancelled_entries: frm.doc.docstatus === 2
				};
				frappe.set_route("query-report", "Hostel fee schedule General ledger");
			});
		}
    }
});
// child table Fetch from "Fee Structure Hostel"
frappe.ui.form.on("Hostel Fee Schedule", "fee_structure", function(frm){
    frappe.model.with_doc("Fee Structure Hostel", frm.doc.fee_structure, function(){
        var tabletransfer = frappe.model.get_doc("Fee Structure Hostel", frm.doc.fee_structure);
        $.each(tabletransfer.components, function(index, row){
            var d = frappe.model.add_child(cur_frm.doc, "Fee Component", "componentss");
            d.fees_category = row.fees_category;
            d.description = row.description;
            d.amount = row.amount;
            d.waiver_type = row.waiver_type;
            d.percentage = row.percentage;
            d.waiver_amount = row.waiver_amount;
            d.total_waiver_amount = row.total_waiver_amount;
            d.receivable_account = row.receivable_account;
            d.income_account = row.income_account;
            d.company = row.company;
            d.grand_fee_amount = row.grand_fee_amount;
            d.outstanding_fees = row.outstanding_fees;

            cur_frm.refresh_field("componentss");
        });
    });
    
});
// "Hostel Fee Schedule Student" Child table length are calculated
// frappe.ui.form.on("Hostel Fee Schedule", {
//     refresh:function(frm){
//         a=0;
//         a=frm.doc.student_room_alloted.length;
//         frm.set_value("total_student", a);
//         refresh_field("total_student");
//     }
// });

// frappe.ui.form.on('Hostel Fee Schedule', {
//     onsubmit:function(frm) {
// 		if(frappe.user.has_role(["Accounts User"]) && !frappe.user.has_role(["Education Administrator"])){
//   			frm.remove_custom_button('Create Fees');
//         }
// 	}
// }


// );

