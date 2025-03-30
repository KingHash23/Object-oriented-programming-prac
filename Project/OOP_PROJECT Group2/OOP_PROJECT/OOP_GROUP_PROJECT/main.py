import customtkinter as ctk
from customtkinter import *
from PIL import Image
from tkinter import messagebox
import tkinter as Tk
from SideBar_Display import Menu

class System(ctk.CTk):
    def __init__(self,title,size,icon):
        super().__init__()
        self.title(title)
        self.iconbitmap(icon)
        self.geometry(f"{size[0]}x{size[1]}+{size[2]}+{size[3]}")
        self.minsize(600,600)
        self.configure(fg_color="#C0C0C0")
        self.configure(bg_color="#C0C0C0")

        menu = Menu(self)

        self.mainloop()
System("HOSPITAL MANAGEMENT SYSTEM",(1600,650,-10,0),("C:/Users/UNETS COMPUTERS/OneDrive/Desktop/Work/Year 2/Object oriented Programming/Object-oriented-programming-prac/Project/OOP_PROJECT Group2/OOP_PROJECT/OOP_GROUP_PROJECT/iMAGES"))
