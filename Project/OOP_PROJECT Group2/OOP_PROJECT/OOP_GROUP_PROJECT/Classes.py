from tkinter import messagebox
import tkinter as Tk

# Class Hospital---------------------------------------------------------------------------------
# Encapsulates 2 methods add_to_system and displayRecords
class Hospital:
    def __init__(self):
        pass
    def add_to_system(self): 
        pass
    def displayRecords(self):
        pass

# Class Patient---------------------------------------------------------------------------------
# Encapsulates 2 methods add_to_system and displayRecords
# The Patient class inherits from the Hospital class
class Patient(Hospital): # Inheritance``
    Patient_records = {}# Patients_records for storing the patient information
    def __init__(self,name,age,gender,phone_number,PatientID,MedicalIssues): # Initializing the object attributes for a Patient object
        super().__init__()

        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__phone_number = phone_number
        self.__PatientID = PatientID
        self.__PatientMedical = MedicalIssues

    @property # property decorator which is method of abstraction
    def add_to_system(self):# Applying polymorphism on the add_to_system method. For adding a PatientID as the key in the Doc_records
        if self.__PatientID in self.Patient_records:
            messagebox.showinfo("Alert","PATIENT ID ALREADY IN SYSTEM")
        else:
            self.Patient_records[self.__PatientID] = [self.__name,self.__gender,self.__age,self.__phone_number,self.__PatientMedical]
            messagebox.showinfo("Complete","PATIENT ID ADDED TO SYSTEM")
    
    @property
    def displayRecords(self):
        for key,value in records.items():# Applying polymorphism on the displayRecords method. For iterating through Patient_records and display the records
            if len(self.Patient_records) == 0:
                print("\nNo patient records available\n")
                print('------------------------------------------')
            else:
                for key, patient in self.Patient_records.items():
                    print(f'\nPatient ID: {key}')
                    print(f'Patient name: {patient[0]}')
                    print(f'Patient gender: {patient[1]}')
                    print(f'Patient age: {patient[2]}')
                    print(f"Patient Medical Issues: {patient[4]}")
                    print(f'Patient Phone number: {patient[3]}')
                    print('------------------------------------------')

#Class Doctor--------------------------------------------------------------------------
# Encapsulates 2 methods add_to_system and displayRecords
# The Doctor class inherits from the Hospital class
class Doctor(Hospital):# Inheritance
    Doc_records = {} # Doc_records for storing the doctor information
    def __init__(self,name,gender,phone_number,DocID):
        super().__init__()

        self.__name = name
        self.__gender = gender
        self.__phone_number = phone_number
        self.__DocID = DocID
        
    @property # property decorator which is method of abstraction
    def add_to_system(self):# Applying polymorphism on the add_to_system method. For adding a DocID as the key in the Doc_records
        if self.__DocID in self.Doc_records:
            print("\nDoctor already exists in the system\n")
            messagebox.showinfo("Alert","Doctor already exists in the system")
        else:
            self.Doc_records[self.__DocID] = [self.__name,self.__gender,self.__phone_number]
            print('\nDoctor added to System\n')
            messagebox.showinfo("COMPLETE","Doctor added to System")    
        print('------------------------------------------')

    @property # property decorator which is method of abstraction
    def displayRecords(self):# Applying polymorphism on the displayRecords method. For iterating through Doc_records and display the records
        if len(self.Doc_records) == 0:
            print("\nNo Doctor records available\n")
        else:
            for key, doctor in self.Doc_records.items():
                print(f'\nDoctor ID: {key}')
                print(f'Doctor name: {doctor[0]}')
                print(f'Doctor gender: {doctor[1]}')
                print(f'Doctor Phone number: {doctor[2]}')
        print('------------------------------------------')

#Class Appointment-------------------------------------------------------------
# Encapsulates 2 methods appointment_scheduling and appointments_display
class Appointments:
    appointments = {} # class attribute appointments which is a dictionary used to store the appointment details
    def __init__(self, date, time, docname, DocID, Patientname, AppoID):
        super().__init__()

        self.__date = date
        self.__time = time
        self.__docname = docname
        self.__DocID = DocID
        self.__Patientname = Patientname
        self.__AppoID = AppoID
    
    @property# property decorator which is method of abstraction
    def appointment_scheduling(self): # Method for checking and adding the appointment ID as the key in the appointments dictionary
        if self.__AppoID in self.appointments and self.__DocID in self.appointments and self.__date in self.appointments:
            print("Appointment already set")
        else:
            self.appointments[self.__AppoID] = [self.__date, self.__time, self.__Patientname, self.__docname, self.__DocID]
            print('\nAppointment scheduled\n')
        print('------------------------------------------')

    @property# property decorator which is method of abstraction
    def appointments_display(self):# For iterating through Doc_records and display the records
        if len(self.appointments) == 0:
            print("\nNo appointments Scheduled\n")
        else:
            for key, appointment in self.appointments.items():
                print(f'\nDoctor ID: {key}')
                print(f'Patient ID: {appointment[2]}')
                print(f'Appointment date: {appointment[0]}')
                print(f'Appointment time: {appointment[1]}')
        print('------------------------------------------')

#Class Room-----------------------------------------------------------------------------
# Encapsulates 1 methods assign_room 
class Room:
    room_records = {} # class attribute room_records which is a dictionary used to store the room details
    def __init__(self, RoomNumber, PatientID):
        self.__room_number = RoomNumber
        self.__roomPatient = PatientID

    @property
    def assign_room(self): # method for assigning a room to a patient
        if self.__room_number in self.room_records or self.__roomPatient in self.room_records:
            print("The room is already occupied")
            messagebox.showinfo("Alert", "The room is already occupied")
        else:
            self.room_records[self.__room_number] = [self.__roomPatient]
            print("Room added to system")
            messagebox.showinfo("COMPLETE", "Patient assigned room")
        print('------------------------------------------')


#Class Bill------------------------------------------------------------------------------
# Encapsulates 1 methods bill_patient 
class Bill:
    bill_records = {} # class attribute bill_records which is a dictionary used to store the bill details
    def __init__(self, PatientName, PatientID,services, TotalCharges):
        self.__PatientName = PatientName
        self.__PatientID = PatientID
        self.__services = services
        self.__TotalCharges = TotalCharges

    @property
    def bill_patient(self): # method that bill the specified patient
        if self.__PatientID in self.bill_records:
            print("Patient already billed")
            messagebox.showinfo("Alert","Patient already billed")
            print('------------------------------------------')
        else:
            print("PATIENT BILLED")
            self.bill_records[self.__PatientID] = [self.__PatientName, self.__services, self.__TotalCharges]
            messagebox.showinfo("COMPLETE","PATIENT BILLED ✔️")
            print('------------------------------------------')



start = '*'*20
print(f'\n{start}WELCOME TO THE HOSPITAL MANAGEMENT SYSTEM🏥{start}\n')

