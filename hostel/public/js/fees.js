frappe.ui.form.on('Fees', {
    setup: function (frm) {
		frm.set_query("hostel_fee_structure", function () {
			return {
				filters: [
					["Fee Structure Hostel", "programs", "=", frm.doc.programs],
					["Fee Structure Hostel", "academic_year", "=", frm.doc.academic_year],
				]
			}
		});
	},
    hostel_fee_structure: function(frm) {
		frm.set_value("components" ,"");
		if (frm.doc.hostel_fee_structure) {
			frappe.call({
				method: "hostel.hostel.validations.fees.get_fee_components",              
				args: {
					"hostel_fee_structure": frm.doc.hostel_fee_structure
				},
				callback: function(r) {
					if (r.message) {
						$.each(r.message, function(i, d) {
							var row = frappe.model.add_child(frm.doc, "Fee Component", "components");
							row.fees_category = d.fees_category;
							row.receivable_account=d.receivable_account;
							row.income_account = d.income_account;
							row.description = d.description;
							row.amount = d.amount;
							row.receivable_account=d.receivable_account;
                            row.grand_fee_amount=d.grand_fee_amount;
                            row.outstanding_fees=d.outstanding_fees;
						});
					}
					refresh_field("components");
					frm.trigger("calculate_total_amount");
				}
			});
		}
	},
});