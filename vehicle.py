class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
class Car(Vehicle):
    def __init__(self, make, model , year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
    def drive(self, distance):
        print(f"Driving the car {distance} km")
    def refuel(self, amount):
        self.fuel_type += amount
        print(f"Refueled the car with {amount} units of fuel")
    def display_info(self): #also the fuel levels
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Fuel_level: {self.fuel_type}")
#create a car object and simulate driving it and refueling it
car1 = Car("Toyota", "Camry", 2015, 50)
car1.drive(100)
car1.refuel(20)
car1.display_info()
