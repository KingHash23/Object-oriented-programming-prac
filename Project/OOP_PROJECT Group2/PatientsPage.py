import customtkinter as ctk
from customtkinter import *
from PIL import Image
from tkinter import messagebox
import tkinter as Tk
from Classes import Patient

class PatientPage:
    def __init__(self,holder):

        self.PPframe = CTkFrame(holder,fg_color="#FFFFF0",bg_color="black",corner_radius=20,height=30)
        self.PPframe.pack(side="top",expand=True,fill="both",pady=(10,5),padx=(10,10),ipadx=20)
        self.widgets()
        self.addPatient()

    def widgets(self):
        self.navigator_frame = CTkFrame(self.PPframe, width=800, height=50,corner_radius=50, fg_color="#FFFFF0")
        self.navigator_frame.pack(side=TOP, pady=(10,10))

        self.Patient_frame = CTkFrame(self.PPframe, width=900, height=800, corner_radius=20, fg_color="#FFFFF0")
        self.Patient_frame.pack(side=TOP, padx=(5,5), pady=(10,10))

        self.add_patient_btn = CTkButton(self.navigator_frame, text="Add Patient Details",font=("rockwell",15), text_color="black", fg_color="#C0C0C0", hover_color="#DCDCDC", 
                                            corner_radius=50, command=lambda : self.eraser(self.addPatient))
        self.add_patient_btn.pack(side=LEFT, padx=(10,10), pady=(10,0))

        self.patient_records_btn = CTkButton(self.navigator_frame, text="Patient Records", font=("rockwell",15), text_color="black", fg_color="#C0C0C0", hover_color="#DCDCDC", 
                                                corner_radius=50, command=lambda : self.eraser(self.patientRecords))
        self.patient_records_btn.pack(side=LEFT, padx=(10,10), pady=(10,0))



    def addPatient(self):
        AddPatient(self.Patient_frame)
    def patientRecords(self):
        PatientRecords(self.Patient_frame)
    
    def eraser(self,active_method):
        for widget in self.Patient_frame.winfo_children():
            widget.destroy()
        active_method()

class AddPatient:
    def __init__(self,holder):
        self.AddPatient_Frame = CTkFrame(holder,fg_color="#FFFFF0", bg_color="#FFFFF0", height=900, width=1000,
                                          corner_radius=20, border_width=1.5, border_color="black")
        self.AddPatient_Frame.pack(side="top",expand=True,fill="both",padx=(20,20))

        self.widgets()

    def widgets(self):
        self.patient = CTkLabel(self.AddPatient_Frame, text="", corner_radius=20,fg_color="#DCDCDC", width=100, height=100, image=CTkImage(Image.open("iMAGES/user.png"),size=(30,30)))
        self.patient.pack(side=TOP, pady=(15,5))

        self.name_entry = CTkEntry(self.AddPatient_Frame, font=("rockwell",15), corner_radius=20, text_color="white", placeholder_text="Enter Patient Name",
                                    width=300, height=35)
        self.name_entry.pack(side=TOP, padx=(10,10), pady=(15,0))

        self.age_entry = CTkEntry(self.AddPatient_Frame, font=("rockwell",15), corner_radius=20, text_color="white", placeholder_text="Enter Patient Age",
                                    width=300, height=35)
        self.age_entry.pack(side=TOP, padx=(10,10), pady=(15,0))

        self.gender_entry = CTkEntry(self.AddPatient_Frame, font=("rockwell",15), corner_radius=20, text_color="white", placeholder_text="Enter Patient Gender",
                                        width=300, height=35)
        self.gender_entry.pack(side=TOP, padx=(10,10), pady=(15,0))

        self.phone_number_entry = CTkEntry(self.AddPatient_Frame, font=("rockwell",15), corner_radius=20, text_color="white", placeholder_text="Enter Patient Phone Number",
                                            width=300, height=35)
        self.phone_number_entry.pack(side=TOP, padx=(10,10), pady=(15,0))

        self.patient_id_entry = CTkEntry(self.AddPatient_Frame, font=("rockwell",15), corner_radius=20, text_color="white", placeholder_text="Enter Patient ID",
                                                        width=300, height=35)
        self.patient_id_entry.pack(side=TOP, padx=(10,10), pady=(15,0))

        self.medical_issues_entry = CTkEntry(self.AddPatient_Frame, font=("rockwell",15), corner_radius=20, text_color="white", placeholder_text="Enter Patient Medical Issues",
                                                width=300, height=35)
        self.medical_issues_entry.pack(side=TOP, padx=(10,10), pady=(15,20))

        self.add_patient_button = CTkButton(self.AddPatient_Frame, text="Add Patient",command=self.create_and_save_patient)
        self.add_patient_button.pack(side=TOP, padx=(10,10), pady=(15,20))


    def create_and_save_patient(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        gender = self.gender_entry.get()
        phone_number = self.phone_number_entry.get()
        patient_id = self.patient_id_entry.get()
        medical_issues = self.medical_issues_entry.get()

        if name == "" or gender == "" or phone_number == "" or patient_id == "" or medical_issues == "":
            messagebox.showinfo("ALERT","PLEASE FILL IN ALL THE FIELDS")
        else:
            newPatient = Patient(name,age,gender,phone_number,patient_id,medical_issues)
            newPatient.add_to_system

            self.name_entry.delete(0, "end")
            self.age_entry.delete(0, "end")
            self.gender_entry.delete(0, "end")
            self.phone_number_entry.delete(0, "end")
            self.patient_id_entry.delete(0, "end")
            self.medical_issues_entry.delete(0, "end")


class PatientRecords:
    def __init__(self,holder):
        self.PatientRecords_Frame = CTkScrollableFrame(holder,fg_color="#FFFFF0", bg_color="#FFFFF0", height=900, width=900,
                                          corner_radius=20)
        self.PatientRecords_Frame.pack(side="top",expand=True,fill="both")

        self.show_records()

    def show_records(self):
        records = Patient.Patient_records

        if len(records) == 0:
            self.card1 = CTkFrame(self.PatientRecords_Frame,fg_color="#AFEEEE",width=800)
            self.card1.pack(side=TOP, expand=True, fill="both", pady=(10,10))

            self.note = CTkLabel(self.card1, text="NO PATIENT RECORDS AVAILABLE", font=("rockwell",20,"bold"), fg_color="#AFEEEE", width=800, text_color="black")
            self.note.pack(expand=True, fill="both", pady=(10,10))

        else:
            for key,value in records.items():
                self.card = CTkFrame(self.PatientRecords_Frame,fg_color="#AFEEEE",width=800, border_color="black", border_width=1.5)
                self.card.pack(side=TOP, expand=True, fill="both", pady=(10,10))

                CTkLabel(self.card,text=f"  PatientID: \t\t{key}", font=("rockwell",15,"bold"),text_color="black", justify=LEFT, anchor=W).pack(side=TOP,pady=(10,10), fill="x")
                CTkLabel(self.card,text=f"  Patient's Name: \t\t{value[0]}", font=("rockwell",15),text_color="black", justify=LEFT, anchor=W).pack(side=TOP,pady=(10,10), fill="x")
                CTkLabel(self.card,text=f"  Patient's gender: \t\t{value[1]}", font=("rockwell",15),text_color="black", justify=LEFT, anchor=W).pack(side=TOP,pady=(10,10), fill="x")
                CTkLabel(self.card,text=f"  Patient's age: \t\t{value[2]}", font=("rockwell",15),text_color="black", justify=LEFT, anchor=W).pack(side=TOP,pady=(10,10), fill="x")
                CTkLabel(self.card,text=f"  Patient's phone number: \t{value[3]}", font=("rockwell",15),text_color="black", justify=LEFT, anchor=W).pack(side=TOP,pady=(10,10), fill="x")
                CTkLabel(self.card,text=f"  Patient's Medical Issue: \t{value[4]}", font=("rockwell",15),text_color="black", justify=LEFT, anchor=W).pack(side=TOP,pady=(10,10), fill="x")

