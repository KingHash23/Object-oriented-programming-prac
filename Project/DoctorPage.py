import customtkinter as ctk
from customtkinter import *
from PIL import Image
from tkinter import messagebox
import tkinter as Tk
from Classes import Patient
from Classes import Doctor

class DoctorPage:
    def __init__(self,holder):
        self.DPframe = CTkFrame(holder,fg_color="#FFFFF0",bg_color="black",corner_radius=20,height=30)
        self.DPframe.pack(side="top",expand=True,fill="both",pady=(10,5),padx=(10,10),ipadx=20)

        self.widgets()
        self.create_and_saveDoc(self.addDoc_frame)
        self.showDoc_records()

    def widgets(self):
        self.addDoc_frame = CTkFrame(self.DPframe, bg_color="#FFFFF0", fg_color="#FFFFF0", corner_radius=20, height=25, width=50, border_width=2, border_color="grey")
        self.addDoc_frame.pack(side=LEFT, padx=(5,5), pady=(10,10), fill="both")

        self.Docrecords_frame = CTkScrollableFrame(self.DPframe, bg_color="#FFFFF0", fg_color="#FFFFF0", corner_radius=20, height=25, border_width=2, border_color="grey")
        self.Docrecords_frame.pack(side=LEFT, padx=(5,5), pady=(10,10), fill="both", expand=True)


    def create_and_saveDoc(self,holder):

        self.patient = CTkLabel(holder, text="", corner_radius=20,fg_color="#FFFFF0", width=100, height=100, image=CTkImage(Image.open("iMAGES/main_frame.jpg"),size=(50,50)))
        self.patient.pack(side=TOP, pady=(15,5))

        self.name_entry = CTkEntry(holder, font=("rockwell",15), corner_radius=20, text_color="white", placeholder_text="Enter Doctor's Name",
                                    width=300, height=35)
        self.name_entry.pack(side=TOP, padx=50, pady=(10,0), fill="x")

        self.gender_entry = CTkEntry(holder, font=("rockwell",15), corner_radius=20, text_color="white", placeholder_text="Enter Doctor's Gender",
                                        width=300, height=35)
        self.gender_entry.pack(side=TOP, padx=50, pady=(15,0), fill="x")

        self.phone_number_entry = CTkEntry(holder, font=("rockwell",15), corner_radius=20, text_color="white", placeholder_text="Enter Doctor's Phone Number",
                                            width=300, height=35)
        self.phone_number_entry.pack(side=TOP, padx=50, pady=(15,0), fill="x")

        self.doc_id_entry = CTkEntry(holder, font=("rockwell",15), corner_radius=20, text_color="white", placeholder_text="Enter Doctor's ID",
                                                        width=300, height=35)
        self.doc_id_entry.pack(side=TOP, padx=50, pady=10, fill="x")

        self.add_doc_button = CTkButton(holder, text="Add Doctor", width=100, corner_radius=20,command=self.save_doc)
        self.add_doc_button.pack(side=TOP, padx=50, pady=(15,20),fill="x")
    
    def save_doc(self):
        DocName = self.name_entry.get().title()
        DocGender = self.gender_entry.get()
        DocPhone_number = self.phone_number_entry.get()
        Doc_id = self.doc_id_entry.get()

        if DocName == "" or DocGender == "" or DocPhone_number == "" or Doc_id == "":
            messagebox.showinfo("ALERT","PLEASE FILL IN ALL THE FIELDS")
        else:
            newDoc = Doctor(DocName,DocGender,DocPhone_number,Doc_id)
            newDoc.add_to_system

            self.name_entry.delete(0, "end")
            self.gender_entry.delete(0, "end")
            self.phone_number_entry.delete(0, "end")
            self.doc_id_entry.delete(0, "end")

            for widgets in self.Docrecords_frame.winfo_children():
                widgets.destroy()
            self.showDoc_records()


    def showDoc_records(self):
        records = Doctor.Doc_records

        if len(records) == 0:
            self.card1 = CTkFrame(self.Docrecords_frame,fg_color="#AFEEEE",width=800, border_color="black", border_width=1.5)
            self.card1.pack(side=TOP, expand=True, fill="both", pady=(10,10))

            self.note = CTkLabel(self.card1, text="NO DOCTOR RECORDS AVAILABLE", font=("rockwell",20,"bold"), fg_color="#AFEEEE", width=800, text_color="black")
            self.note.pack(expand=True, fill="both", pady=(10,10))
        else:
            for key,value in records.items():
                self.card = CTkFrame(self.Docrecords_frame,fg_color="#AFEEEE",width=800, border_color="black", border_width=1.5)
                self.card.pack(side=TOP, expand=True, fill="both", pady=(10,10))

                CTkLabel(self.card,text=f"  Doctor's ID:\t\t{key}", font=("rockwell",15,"bold"),text_color="black", justify=LEFT, anchor=W).pack(side=TOP,pady=(10,10), fill="x")
                CTkLabel(self.card,text=f"  Doctor's name:\t\t{value[0]}", font=("rockwell",15),text_color="black", justify=LEFT, anchor=W).pack(side=TOP,pady=(10,10), fill="x")
                CTkLabel(self.card,text=f"  Gender:\t\t{value[1]}", font=("rockwell",15),text_color="black", justify=LEFT, anchor=W).pack(side=TOP,pady=(10,10), fill="x")
                CTkLabel(self.card,text=f"  Doctors's phone number: \t{value[2]}", font=("rockwell",15),text_color="black", justify=LEFT, anchor=W).pack(side=TOP,pady=(10,10), fill="x")
