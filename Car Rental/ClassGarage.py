class Garage:
    def __init__(self):
        self.parked_vehicle = None

    def set_vehicle(self, vehicle):
        self.parked_vehicle = vehicle

    def to_string(self):
        return f"Description of the vehicle:\n{self.parked_vehicle.to_string()}" if self.parked_vehicle else "Garage is empty."

#The implementation
garage = Garage()

car1 = Car("blue", True)
garage.set_vehicle(car1)
print(garage.to_string())

garage.set_vehicle(None)
print(garage.to_string())

truck1 = Truck("red", True)
garage.set_vehicle(truck1)
print(garage.to_string())