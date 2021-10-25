// Copyright (c) 2021, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('Indisciplinary Complaint Registration', {
    setup: function (cur_frm) {
        cur_frm.set_query("allotment_number", "student", function() {
            return {
                query: "hostel.hostel.doctype.indisciplinary_complaint_registration.indisciplinary_complaint_registration.ra_query"
            };
        });
    }
})