// Copyright (c) 2021, SOUL and contributors
// For license information, please see license.txt
frappe.ui.form.on('test3', {
	refresh: function(frm) {
		document.getElementById('generate').onclick = function() {

			var values = ["dog", "cat", "parrot", "rabbit"];
		  
			var select = document.createElement("select");
			select.name = "pets";
			select.id = "pets"
		  
			for (const val of values) {
			  var option = document.createElement("option");
			  option.value = val;
			  option.text = val.charAt(0).toUpperCase() + val.slice(1);
			  select.appendChild(option);
			}
		  
			var label = document.createElement("label");
			label.innerHTML = "Choose your pets: "
			label.htmlFor = "pets";
		  
			document.getElementById("container").appendChild(label).appendChild(select);
		  }
		}
});
