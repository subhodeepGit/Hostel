# Copyright (c) 2021, SOUL and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import pandas as pd


class RoomMasters(Document):
	@frappe.whitelist()
	def validate(doc):
		hostel_id=doc.hostel_id
		room_number=doc.room_number
		Room_id=doc.name

		info=''' RM WHERE RM.hostel_id="%s" and RM.room_number="%s" and RM.validity="Approved" '''%(hostel_id,room_number) 
		Type="General"
		Ck_df=Room_master_sql(info,Type) # cheacking for same room no and hostel is present 

		info=''' WHERE `name`="%s" '''%(Room_id)
		Type="General"
		hostel_df=Room_master_sql(info,Type) # checking room id is present or not

		if len(hostel_df)==0 and len(Ck_df)==0:
			pass
		else:
			if len(hostel_df)!=0:
				if hostel_id==hostel_df['hostel_id'][0] and hostel_df['room_number'][0]==room_number:
					pass
				else:
					frappe.throw("Hostel Name or Room Number can't be changed")
			elif len(hostel_df)==0 and len(Ck_df)!=0:
				frappe.throw("Issue in updating Record")	
			else:
				frappe.throw("Hostel Name or Room Number can't be changed")						


# def update_test(hostel_df,AC_room_type,Ac_Room_capacity,Floor_Number,room_description,validity,actual_room_type,actual_capacity,block,hostel_id):	
# 	Hostel_room=frappe.get_doc("Room Masters",hostel_df)
# 	if Hostel_room.hostel_id==hostel_id:
# 		Hostel_room.room_type_id=AC_room_type
# 		Hostel_room.room_capacity=Ac_Room_capacity
# 		Hostel_room.floor_number=Floor_Number
# 		Hostel_room.room_description=room_description
# 		Hostel_room.validity=validity
# 		Hostel_room.actual_room_type=actual_room_type
# 		Hostel_room.actual_capacity=actual_capacity
# 		Hostel_room.block=block
# 		Hostel_room.save(    ignore_permissions=True, # ignore write permissions during insert
#     						ignore_version=True # do not create a version record	
# 						)							
# 		frappe.db.commit()	
# 	else:
# 		frappe.throw("Issue in updating")			

def Room_master_sql(info,Type):
		if Type=="General":
			Hostel=frappe.db.sql(""" SELECT `name`,`hostel_id`,`room_type_id`,`room_number`,`room_capacity`,`floor_number`,`room_description`,
											`validity`,`actual_room_type`,`actual_capacity`,`block`  from `tabRoom Masters` """ + info)							
			hostel_df=pd.DataFrame({
				'Room_doc_id':[],'hostel_id':[],'Acc_room_type':[],'room_number':[],
				'Acc_room_capacity':[],'floor_number':[],'room_description':[],'validity':[],
				'actual_room_type':[],'actual_capacity':[],'block':[]
			})
			for t in range(len(Hostel)):
				s=pd.Series([Hostel[t][0],Hostel[t][1],Hostel[t][2],Hostel[t][3],Hostel[t][4],Hostel[t][5],
							Hostel[t][6],Hostel[t][7],Hostel[t][8],Hostel[t][9],Hostel[t][10]],
									index=['Room_doc_id','hostel_id','Acc_room_type','room_number',
											'Acc_room_capacity','floor_number','room_description','validity',
											'actual_room_type','actual_capacity','block'])
				hostel_df=hostel_df.append(s,ignore_index=True)	
			return hostel_df