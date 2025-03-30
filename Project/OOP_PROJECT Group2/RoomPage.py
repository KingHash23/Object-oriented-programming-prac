import customtkinter as ctk
from customtkinter import *
from PIL import Image
from tkinter import messagebox
import tkinter as Tk
from Classes import Room

class RoomPage:
    def __init__(self,holder):
        self.RPframe = CTkFrame(holder,fg_color="#FFFFF0",bg_color="black",corner_radius=20,height=30)
        self.RPframe.pack(side="top",expand=True,fill="both",pady=(10,5),padx=(10,10),ipadx=20)

        self.widgets()
        self.show_room()

    def widgets(self):
        self.AssignRoom_frame = CTkFrame(self.RPframe, bg_color="#FFFFF0", fg_color="#FFFFF0", corner_radius=20, height=25, width=50, border_width=2, border_color="grey")
        self.AssignRoom_frame.pack(side=LEFT, padx=(5,5), pady=(10,10), fill="both")

        self.showRooms_frame = CTkScrollableFrame(self.RPframe, bg_color="#FFFFF0", fg_color="#FFFFF0", corner_radius=20, height=25, border_width=2, border_color="grey")
        self.showRooms_frame.pack(side=LEFT, padx=(5,5), pady=(10,10), fill="both", expand=True)

        self.head = CTkLabel(self.AssignRoom_frame, font=("rockwell",15), corner_radius=20, text="ASSIGN A ROOM TO A PATIENT", text_color="black", fg_color="#AFEEEE", bg_color="#FFFFF0",
                                    width=300, height=35)
        self.head.pack(side=TOP, padx=50, fill="x", pady=(10,50))

        self.room = CTkLabel(self.AssignRoom_frame, text="", corner_radius=20,fg_color="#DCDCDC", width=100, height=100, image=CTkImage(Image.open("iMAGES/hospitalRoom.png"),size=(30,30)))
        self.room.pack(side=TOP, pady=(15,5))

        self.RoomNumber_entry = CTkEntry(self.AssignRoom_frame, font=("rockwell",15), corner_radius=20, text_color="white", placeholder_text="Enter the room number",
                                    width=300, height=35)
        self.RoomNumber_entry.pack(side=TOP, padx=50, fill="x", pady=(15,0))

        self.AssignedPatient_entry = CTkEntry(self.AssignRoom_frame, font=("rockwell",15), corner_radius=20, text_color="white", placeholder_text="Enter the Patient's ID",
                                    width=300, height=35)
        self.AssignedPatient_entry.pack(side=TOP, padx=50, fill="x", pady=(25,0))

        self.assignRoom_button = CTkButton(self.AssignRoom_frame, text="Assign Room", width=100, corner_radius=20, command=self.assignRoom)
        self.assignRoom_button.pack(side=TOP, padx=50, pady=(20,20),fill="x")

    def assignRoom(self):
        RoomNumber = self.RoomNumber_entry.get()
        AssignedPatient = self.AssignedPatient_entry.get()

        if RoomNumber == "" or AssignedPatient == "":
            messagebox.showinfo("ALERT","PLEASE FILL IN ALL THE FIELDS")
        
        else:
            newRoom = Room(RoomNumber, AssignedPatient)
            newRoom.assign_room

            self.RoomNumber_entry.delete(0, "end")
            self.AssignedPatient_entry.delete(0, "end")

            for widgets in self.showRooms_frame.winfo_children():
                widgets.destroy()
            self.show_room()

    def show_room(self):
        records = Room.room_records

        if len(records) == 0:
            self.card1 = CTkFrame(self.showRooms_frame,fg_color="#AFEEEE",width=800, border_color="black", border_width=1.5)
            self.card1.pack(side=TOP, expand=True, fill="both", pady=(10,10))

            self.note = CTkLabel(self.card1, text="NO ROOMS HAVE BEEN ASSIGNED", font=("rockwell",20,"bold"), fg_color="#AFEEEE", width=800, text_color="black")
            self.note.pack(expand=True, fill="both", pady=(10,10))
        else:
            for key,value in records.items():
                self.card = CTkFrame(self.showRooms_frame,fg_color="#AFEEEE",width=800, border_color="black", border_width=1.5)
                self.card.pack(side=TOP, expand=True, fill="both", pady=(10,10))

                CTkLabel(self.card,text=f"  Room Number: \t\t{key}", font=("rockwell",15,"bold"),text_color="black", justify=LEFT, anchor=W).pack(side=TOP,pady=(10,10), fill="x")
                CTkLabel(self.card,text=f"  Occupant: \t\t{value[0]}", font=("rockwell",15),text_color="black", justify=LEFT, anchor=W).pack(side=TOP,pady=(10,10), fill="x")

