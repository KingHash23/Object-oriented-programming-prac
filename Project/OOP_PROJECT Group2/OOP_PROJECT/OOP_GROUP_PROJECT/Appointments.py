import customtkinter as ctk
from customtkinter import *
from PIL import Image
from tkinter import messagebox
import tkinter as Tk
from Classes import Patient
from Classes import Appointments

class AppointmentsPage:
    def __init__(self,holder):
        self.APframe = CTkFrame(holder,fg_color="#FFFFF0",bg_color="black",corner_radius=20,height=30)
        self.APframe.pack(side="top",expand=True,fill="both",pady=(10,5),padx=(10,10),ipadx=20)

        self.widgets()
        self.show_appointments()

    def widgets(self):
        self.scheduleAppointments_frame = CTkFrame(self.APframe, bg_color="#FFFFF0", fg_color="#FFFFF0", corner_radius=20, height=25, width=50, border_width=2, border_color="grey")
        self.scheduleAppointments_frame.pack(side=LEFT, padx=(5,5), pady=(10,10), fill="both")

        self.showAppointments_frame = CTkScrollableFrame(self.APframe, bg_color="#FFFFF0", fg_color="#FFFFF0", corner_radius=20, height=25, border_width=2, border_color="grey")
        self.showAppointments_frame.pack(side=LEFT, padx=(5,5), pady=(10,10), fill="both", expand=True)

        self.head = CTkLabel(self.scheduleAppointments_frame, font=("rockwell",15), corner_radius=20, text="SCHEDULE APPOINTMENT", text_color="black", fg_color="#AFEEEE", bg_color="#FFFFF0",
                                    width=300, height=35)
        self.head.pack(side=TOP, padx=50, fill="x", pady=(10,30))

        self.date_entry = CTkEntry(self.scheduleAppointments_frame, font=("rockwell",15), corner_radius=20, text_color="white", placeholder_text="Enter the date for the appointment",
                                    width=300, height=35)
        self.date_entry.pack(side=TOP, padx=50, fill="x", pady=(15,0))

        self.time_entry = CTkEntry(self.scheduleAppointments_frame, font=("rockwell",15), corner_radius=20, text_color="white", placeholder_text="Enter the time for the appointment",
                                    width=300, height=35)
        self.time_entry.pack(side=TOP, padx=50, fill="x", pady=(15,0))

        self.DocName_entry = CTkEntry(self.scheduleAppointments_frame, font=("rockwell",15), corner_radius=20, text_color="white", placeholder_text="Enter the Doc's name",
                                    width=300, height=35)
        self.DocName_entry.pack(side=TOP, padx=50, fill="x", pady=(15,0))

        self.DocID_entry = CTkEntry(self.scheduleAppointments_frame, font=("rockwell",15), corner_radius=20, text_color="white", placeholder_text="Enter the Doctor's ID",
                                    width=300, height=35)
        self.DocID_entry.pack(side=TOP, padx=50, fill="x", pady=(15,0))

        self.PatientName_entry = CTkEntry(self.scheduleAppointments_frame, font=("rockwell",15), corner_radius=20, text_color="white", placeholder_text="Enter the Patient's name",
                                    width=300, height=35)
        self.PatientName_entry.pack(side=TOP, padx=50, fill="x", pady=(15,0))

        self.AppoID_entry = CTkEntry(self.scheduleAppointments_frame, font=("rockwell",15), corner_radius=20, text_color="white", placeholder_text="Assign an appointmentID",
                                    width=300, height=35)
        self.AppoID_entry.pack(side=TOP, padx=50, fill="x", pady=(15,0))

        self.add_doc_button = CTkButton(self.scheduleAppointments_frame, text="Schedule Appointment", width=100, corner_radius=20, command=self.save_Appointment)
        self.add_doc_button.pack(side=TOP, padx=50, pady=(20,20),fill="x")

    def save_Appointment(self):
        Appo_ID = self.AppoID_entry.get()
        Appo_date = self.date_entry.get()
        Appo_time = self.time_entry.get()
        Appo_Doc = self.DocName_entry.get()
        Appo_DocID =  self.DocID_entry.get()
        Appo_PatientName = self.PatientName_entry.get()

        if Appo_ID == "" or Appo_date == "" or Appo_time == "" or Appo_Doc == "" or Appo_PatientName == "":
            messagebox.showinfo("ALERT","PLEASE FILL IN ALL THE FIELDS")
        
        else:
            newAppo = Appointments(Appo_date, Appo_time, Appo_Doc, Appo_DocID, Appo_PatientName, Appo_ID)
            newAppo.appointment_scheduling

            self.AppoID_entry.delete(0, "end")
            self.date_entry.delete(0, "end")
            self.time_entry.delete(0, "end")
            self.DocName_entry.delete(0, "end")
            self.DocID_entry.delete(0, "end")
            self.PatientName_entry.delete(0, "end")

            for widgets in self.showAppointments_frame.winfo_children():
                widgets.destroy()
            self.show_appointments()

    def show_appointments(self):
        records = Appointments.appointments

        if len(records) == 0:
            self.card1 = CTkFrame(self.showAppointments_frame,fg_color="#AFEEEE",width=800, border_color="black", border_width=1.5)
            self.card1.pack(side=TOP, expand=True, fill="both", pady=(10,10))

            self.note = CTkLabel(self.card1, text="NO SCHEDULED APPOINTMENTS", font=("rockwell",20,"bold"), fg_color="#AFEEEE", width=800, text_color="black")
            self.note.pack(expand=True, fill="both", pady=(10,10))
        else:
            for key,value in records.items():
                self.card = CTkFrame(self.showAppointments_frame,fg_color="#AFEEEE",width=800, border_color="black", border_width=1.5)
                self.card.pack(side=TOP, expand=True, fill="both", pady=(10,10))

                CTkLabel(self.card,text=f"  Appointment ID:\t{key}", font=("rockwell",15,"bold"),text_color="black", justify=LEFT, anchor=W).pack(side=TOP,pady=(10,10), fill="x")
                CTkLabel(self.card,text=f"  Date: \t\t\t{value[0]}", font=("rockwell",15),text_color="black", justify=LEFT, anchor=W).pack(side=TOP,pady=(10,10), fill="x")
                CTkLabel(self.card,text=f"  Time: \t\t\t{value[1]}", font=("rockwell",15),text_color="black", justify=LEFT, anchor=W).pack(side=TOP,pady=(10,10), fill="x")
                CTkLabel(self.card,text=f"  Patient's Name: \t\t{value[2]}", font=("rockwell",15),text_color="black", justify=LEFT, anchor=W).pack(side=TOP,pady=(10,10), fill="x")
                CTkLabel(self.card,text=f"  Doctors's Name: \t\t{value[3]}", font=("rockwell",15),text_color="black", justify=LEFT, anchor=W).pack(side=TOP,pady=(10,10), fill="x")

