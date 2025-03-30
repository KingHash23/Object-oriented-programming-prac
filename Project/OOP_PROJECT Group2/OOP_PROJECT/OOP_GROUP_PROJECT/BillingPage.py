import customtkinter as ctk
from customtkinter import *
from PIL import Image
from tkinter import messagebox
import tkinter as Tk
from Classes import Bill

class Billing:
    def __init__(self,holder):
        self.BPframe = CTkFrame(holder,fg_color="#FFFFF0",bg_color="black",corner_radius=20,height=30)
        self.BPframe.pack(side="top",expand=True,fill="both",pady=(10,5),padx=(10,10),ipadx=20)

        self.widgets()
        self.showBill_records()

    def widgets(self):
        self.billing_frame = CTkFrame(self.BPframe, bg_color="#FFFFF0", fg_color="#FFFFF0", corner_radius=20, height=25, width=50, border_width=2, border_color="grey")
        self.billing_frame.pack(side=LEFT, padx=(5,5), pady=(10,10), fill="both")

        self.ShowBills_frame = CTkScrollableFrame(self.BPframe, bg_color="#FFFFF0", fg_color="#FFFFF0", corner_radius=20, height=25, border_width=2, border_color="grey")
        self.ShowBills_frame.pack(side=LEFT, padx=(5,5), pady=(10,10), fill="both", expand=True)

        self.head = CTkLabel(self.billing_frame, font=("rockwell",15), corner_radius=20, text="BILL PATIENT", text_color="black", fg_color="#AFEEEE", bg_color="#FFFFF0",
                                    width=300, height=35)
        self.head.pack(side=TOP, padx=50, fill="x", pady=(10,30))

        self.room = CTkLabel(self.billing_frame, text="", corner_radius=20,fg_color="#DCDCDC", width=100, height=100, image=CTkImage(Image.open("iMAGES/file_settings.png"),size=(60,60)))
        self.room.pack(side=TOP, pady=(15,5))

        self.Patientname_entry = CTkEntry(self.billing_frame, font=("rockwell",15), corner_radius=20, text_color="white", placeholder_text="Enter Patient's Name",
                                    width=300, height=35)
        self.Patientname_entry.pack(side=TOP, padx=50, pady=(10,0), fill="x")

        self.PatientID_entry = CTkEntry(self.billing_frame, font=("rockwell",15), corner_radius=20, text_color="white", placeholder_text="Enter PatientID",
                                        width=300, height=35)
        self.PatientID_entry.pack(side=TOP, padx=50, pady=(15,0), fill="x")

        self.services_entry = CTkEntry(self.billing_frame, font=("rockwell",15), corner_radius=20, text_color="white", placeholder_text="Enter Services offered",
                                            width=300, height=35)
        self.services_entry.pack(side=TOP, padx=50, pady=(15,0), fill="x")

        self.totalCharges_entry = CTkEntry(self.billing_frame, font=("rockwell",15), corner_radius=20, text_color="white", placeholder_text="Total Charges",
                                                        width=300, height=35)
        self.totalCharges_entry.pack(side=TOP, padx=50, pady=10, fill="x")

        self.add_bill_button = CTkButton(self.billing_frame, text="Bill Patient", width=100, corner_radius=20,command=self.bill)
        self.add_bill_button.pack(side=TOP, padx=50, pady=(15,20),fill="x")

    
    def bill(self):
        PatientName = self.Patientname_entry.get()
        PatientID = self.PatientID_entry.get()
        services = self.services_entry.get()
        totalCharges = self.totalCharges_entry.get()

        if PatientName == "" or PatientID == "" or services == "" or totalCharges == "":
            messagebox.showinfo("ALERT","PLEASE FILL IN ALL THE FIELDS")
        else:
            newBill = Bill(PatientName, PatientID, services, totalCharges)
            newBill.bill_patient

            self.Patientname_entry.delete(0, "end")
            self.PatientID_entry.delete(0, "end")
            self.services_entry.delete(0, "end")
            self.totalCharges_entry.delete(0, "end")

            for widgets in self.ShowBills_frame.winfo_children():
                widgets.destroy()
            self.showBill_records()
    
    def showBill_records(self):

        records = Bill.bill_records

        if len(records) == 0:
            self.card1 = CTkFrame(self.ShowBills_frame,fg_color="#AFEEEE",width=800, border_color="black", border_width=1.5)
            self.card1.pack(side=TOP, expand=True, fill="both", pady=(10,10))

            self.note = CTkLabel(self.card1, text="NO BILLING RECORDS AVAILABLE", font=("rockwell",20,"bold"), fg_color="#AFEEEE", width=800, text_color="black")
            self.note.pack(expand=True, fill="both", pady=(10,10))
        else:
            for key,value in records.items():
                self.card = CTkFrame(self.ShowBills_frame,fg_color="#AFEEEE",width=800, border_color="black", border_width=1.5)
                self.card.pack(side=TOP, expand=True, fill="both", pady=(10,10))

                CTkLabel(self.card,text=f"  Patient ID: \t{key}", font=("rockwell",15,"bold"),text_color="black", justify=LEFT, anchor=W).pack(side=TOP,pady=(10,10), fill="x")
                CTkLabel(self.card,text=f"  Patient name: \t{value[0]}", font=("rockwell",15),text_color="black", justify=LEFT, anchor=W).pack(side=TOP,pady=(10,10), fill="x")
                CTkLabel(self.card,text=f"  Services: \t{value[1]}", font=("rockwell",15),text_color="black", justify=LEFT, anchor=W).pack(side=TOP,pady=(10,10), fill="x")
                CTkLabel(self.card,text=f"  Total Charges: \t{value[2]}", font=("rockwell",15),text_color="black", justify=LEFT, anchor=W).pack(side=TOP,pady=(10,10), fill="x")