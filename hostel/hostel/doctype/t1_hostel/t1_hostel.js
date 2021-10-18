// Copyright (c) 2021, SOUL and contributors
// For license information, please see license.txt

frappe.ui.form.on('T1 Hostel', "sample", function(frm) {
		document.getElementById('generate').onclick = function() {

			var values = ["dog", "cat", "parrot", "rabbit"];
		  
			var select = document.createElement("generate");
			select.frm.doc.name = "pets";
			select.frm.doc.id = "pets"
		  
			for (const val of values) {
			  var option = document.createElement("option");
			  option.value = val;
			  option.text = val.charAt(0).toUpperCase() + val.slice(1);
			  select.appendChild(option);
			}
		  
			var label = document.createElement("label");
			label.innerHTML = "Choose your pets: "
			label.htmlFor = "pets";
		  
			document.getElementById("generate").appendChild(label).appendChild(select);
		  }
});
