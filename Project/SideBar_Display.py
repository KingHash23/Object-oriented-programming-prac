import customtkinter as ctk
from customtkinter import *
from PIL import Image
from PatientsPage import PatientPage
from DoctorPage import DoctorPage
from Appointments import AppointmentsPage
from RoomPage import RoomPage
from BillingPage import Billing

class Menu:
    def __init__(self,parent):

        self.frame = CTkFrame(parent,fg_color="black",corner_radius=50)
        self.frame.pack(side="left",fill="y",pady=10,padx=10)
        self.createBtns()
        self.Btn_layout()

        self.display_frame = CTkFrame(parent,fg_color="black",corner_radius=20,bg_color="#C0C0C0")
        self.display_frame.pack(side="right",expand=True,fill="both",pady=10,padx=5)

        self.image_label = CTkLabel(self.display_frame,text="",fg_color="#FFFFFF",corner_radius=20,
                                    image=CTkImage(Image.open("iMAGES/main_frame.jpg"),size=(300,300)))
        self.welcome_label = CTkLabel(self.image_label,text="WELCOME",text_color="black",fg_color="#FFFFF0",width=800,height=50,
                                      font=("rockwell",50,"bold"))

        self.image_label.pack(expand=True,fill="both",padx=5,pady=5)
        self.welcome_label.place(anchor="center",relx=0.5,rely=0.1)

    def createBtns(self):
        self.Pateints_Btn = CTkButton(self.frame,image=CTkImage(Image.open("iMAGES/patients.webp"),size=(20,20)),
                                        text="Patients",font=("rockwell",15),text_color="black",fg_color="#C0C0C0",width=170,
                                        hover_color="#FFFFF0",corner_radius=20,compound=LEFT,anchor=W,command=lambda: self.eraser(self.PatientPage))

        self.Doctors_Btn = CTkButton(self.frame,image=CTkImage(Image.open("iMAGES/profile.png"),size=(20,20)),
                                        text="Doctors",font=("rockwell",15),text_color="black",fg_color="#C0C0C0",width=170,
                                        hover_color="#FFFFF0",corner_radius=20,compound=LEFT,anchor=W, command=lambda: self.eraser(self.DoctorPage))

        self.Appointments_Btn = CTkButton(self.frame,image=CTkImage(Image.open("iMAGES/signupsign_inscribirs_2798.ico"),size=(20,20)),
                                        text="Appointments",font=("rockwell",15),text_color="black",fg_color="#C0C0C0",width=170,
                                        hover_color="#FFFFF0",corner_radius=20,compound=LEFT,anchor=W, command= lambda: self.eraser(self.AppointmentsPage))

        self.Rooms_Btn = CTkButton(self.frame,image=CTkImage(Image.open("iMAGES/hospitalRoom.png"),size=(20,20)),
                                        text="Rooms",font=("rockwell",15),text_color="black",fg_color="#C0C0C0",width=170,
                                        hover_color="#FFFFF0",corner_radius=20,compound=LEFT,anchor=W, command= lambda: self.eraser(self.RoomPage))

        self.Billing_Btn = CTkButton(self.frame,image=CTkImage(Image.open("iMAGES/file_settings.png"),size=(20,20)),
                                        text="Billing",font=("rockwell",15),text_color="black",fg_color="#C0C0C0",width=170,
                                        hover_color="#FFFFF0",corner_radius=20,compound=LEFT,anchor=W, command= lambda: self.eraser(self.BillingPage))    
    
    def Btn_layout(self):
        self.Pateints_Btn.pack(padx=20,pady=(50,10))
        self.Doctors_Btn.pack(padx=20,pady=(0,10))
        self.Appointments_Btn.pack(padx=20,pady=(0,10))
        self.Rooms_Btn.pack(padx=20,pady=(0,10))
        self.Billing_Btn.pack(padx=20,pady=(0,10))

    def PatientPage(self):
        PatientPage(self.display_frame)

    def DoctorPage(self):
        DoctorPage(self.display_frame)

    def AppointmentsPage(self):
        AppointmentsPage(self.display_frame)
        
    def RoomPage(self):
        RoomPage(self.display_frame)

    def BillingPage(self):
        Billing(self.display_frame)

    def eraser(self, active_method):
        for widgets in self.display_frame.winfo_children():
            widgets.destroy()
        active_method()
        
