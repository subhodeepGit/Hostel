frappe.ui.form.on("Student", "onload", function(frm) 
{ 
	// if(frm.doc.room_allotment!=undefined)
	// {
        alert(frm.doc.name)
        frappe.call({
            "method": "hostel.room_allotment.get",
            args: {
                // doctype: "Room Allotment",
                name: frm.doc.name
            },
            callback: function (data) {
            frm.add_custom_button(__('Hostel Details'), function(){
                alert(JSON.stringify(data))
                // var msg = 'Student Name : ' + data.message.student_name+'<br/>';
				var msg ='Hostel : ' + data.message.hostel_id+'<br/>';
				msg = msg + 'Room ID : ' + data.message.room_id+'<br/>';
				msg = msg + 'Room Number : ' + data.message.room_number + '<br/>';
                msg = msg + 'Room Type : ' + data.message.room_type + '<br/>';
				msgprint(__(msg));
				});
            }
        })
    //  }
});