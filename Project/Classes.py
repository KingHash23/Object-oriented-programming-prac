from tkinter import messagebox
import tkinter as Tk

# Class Hospital---------------------------------------------------------------------------------
class Hospital:
    def __init__(self):
        pass
    def add_to_system(self):
        pass
    def displayRecords(self):
        pass

# Class Patient---------------------------------------------------------------------------------
class Patient(Hospital):
    Patient_records = {}
    def __init__(self,name,age,gender,phone_number,PatientID,MedicalIssues):
        super().__init__()

        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__phone_number = phone_number
        self.__PatientID = PatientID
        self.__PatientMedical = MedicalIssues

    @property
    def add_to_system(self):
        if self.__PatientID in self.Patient_records:
            messagebox.showinfo("Alert","PATIENT ID ALREADY IN SYSTEM")
        else:
            self.Patient_records[self.__PatientID] = [self.__name,self.__gender,self.__age,self.__phone_number,self.__PatientMedical]
            messagebox.showinfo("Complete","PATIENT ID ADDED TO SYSTEM")
    
    @property
    def displayRecords(self):
        for key,value in records.items():
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
class Doctor(Hospital):
    Doc_records = {}
    def __init__(self,name,gender,phone_number,DocID):
        super().__init__()

        self.__name = name
        self.__gender = gender
        self.__phone_number = phone_number
        self.__DocID = DocID
        
    @property
    def add_to_system(self):
        if self.__DocID in self.Doc_records:
            print("\nDoctor already exists in the system\n")
            messagebox.showinfo("Alert","Doctor already exists in the system")
        else:
            self.Doc_records[self.__DocID] = [self.__name,self.__gender,self.__phone_number]
            print('\nDoctor added to System\n')
            messagebox.showinfo("COMPLETE","Doctor added to System")    
        print('------------------------------------------')

    @property
    def displayRecords(self):
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
class Appointments:
    appointments = {}
    def __init__(self, date, time, docname, DocID, Patientname, AppoID):
        super().__init__()

        self.__date = date
        self.__time = time
        self.__docname = docname
        self.__DocID = DocID
        self.__Patientname = Patientname
        self.__AppoID = AppoID
    
    @property
    def appointment_scheduling(self):
        if self.__AppoID in self.appointments and self.__DocID in self.appointments and self.__date in self.appointments:
            print("Appointment already set")
        else:
            self.appointments[self.__AppoID] = [self.__date, self.__time, self.__Patientname, self.__docname, self.__DocID]
            print('\nAppointment scheduled\n')
        print('------------------------------------------')

    @property
    def appointments_display(self):
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
class Room:
    room_records = {}
    def __init__(self, RoomNumber, PatientID):
        self.__room_number = RoomNumber
        self.__roomPatient = PatientID

    @property
    def assign_room(self):
        if self.__room_number in self.room_records or self.__roomPatient in self.room_records:
            print("The room is already occupied")
            messagebox.showinfo("Alert", "The room is already occupied")
        else:
            self.room_records[self.__room_number] = [self.__roomPatient]
            print("Room added to system")
            messagebox.showinfo("COMPLETE", "Patient assigned room")
        print('------------------------------------------')


#Class Bill------------------------------------------------------------------------------
class Bill:
    bill_records = {}
    def __init__(self, PatientName, PatientID,services, TotalCharges):
        self.__PatientName = PatientName
        self.__PatientID = PatientID
        self.__services = services
        self.__TotalCharges = TotalCharges

    @property
    def bill_patient(self):
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

# new_patient = Patient()
# new_Doc = Doctor()
# new_appointment = Appointment()
# new_room = Room()

# while True:
#     option = input('\nPlease select an option from the following :\n a) Add a patient to the System\n b) View Patient records\n c) Add a Doctor to the System\n d) Schedule Appointment\n e) View scheduled appointments\n f) Add a room to the system\n g) Assign a Patient a room\n \nENTER YOUR OPTION: ')
#     print('------------------------------------------')

#     if option == 'a':
#         new_patient.create_patient
#         new_patient.add

#     if option == 'b':
#         new_patient.patient_records

#     if option == 'c':
#         new_Doc.create_Doc
#         new_Doc.add_Doc

#     if option == 'd':
#         new_appointment.appointment_scheduling
#         new_appointment.add_appointments

#     if option == 'e':
#         new_appointment.appointments_display

#     if option == 'f':
#         new_room.create_room
#         new_room.store_room

#     if option == 'g':
#         Occupied_room = input("\nEnter room to assign to patient: ")
#         Occupant = input("\nEnter patient to occupy room: ")
#         new_room.assign_room(Occupant,Occupied_room)