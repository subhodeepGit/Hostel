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
                    // if(in_list(student_list, element.student)) {
                    var row = frm.add_child("student_room_alloted")
                    row.room_allotment_id=element.room_allotment
                });
                frm.refresh_field("student_room_alloted")
                frm.save();
                // a=frm.doc.student_room_alloted.length;
                // frm.set_value("total_student", a);
                // frm.set_value("total_enrolled_student",(r.message).length)
            }
        });
    },  
    
 
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
frappe.ui.form.on("Hostel Fee Schedule", {
    refresh:function(frm){
    a=frm.doc.student_room_alloted.length;
    frm.set_value("total_student", a);
    refresh_field("total_student");
    }
});

