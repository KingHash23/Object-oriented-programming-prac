# Define the Vehicle class
class Vehicle:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def to_string(self):
        return f"Vehicle color is {self.color}"


# Define the Car class
class Car(Vehicle):
    def __init__(self, color, winter_tires=False):
        super().__init__(color)
        self.winter_tires = winter_tires

    def to_string(self):
        return f"{super().to_string()}\nVehicle has winter tires: {self.winter_tires}"


# Define the Truck class
class Truck(Vehicle):
    def __init__(self, color, trailer=False):
        super().__init__(color)
        self.trailer = trailer

    def to_string(self):
        return f"{super().to_string()}\nTruck has a trailer: {self.trailer}"


# Define the Garage class
class Garage:
    def __init__(self):
        self.parked_vehicle = None

    def set_vehicle(self, vehicle):
        self.parked_vehicle = vehicle

    def to_string(self):
        return f"Description of the vehicle:\n{self.parked_vehicle.to_string()}" if self.parked_vehicle else "Garage is empty."


# Define the GarageTester class
class GarageTester:
    def getExample(self):
        # Create a Truck object with color black and no trailer
        truck = Truck("black", trailer=False)
        
        # Create a Garage object
        garage = Garage()
        
        # Put the Truck into the Garage
        garage.set_vehicle(truck)
        
        # Print the description of the vehicle in the garage
        print(garage.to_string())


# Define the Customer class
class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def to_string(self):
        return f"Customer Name: {self.name}\nCustomer Address: {self.address}"


# Example usage
if __name__ == "__main__":
    # Create a Garage object and park a Car and a Truck
    garage = Garage()
    car1 = Car("blue", True)
    garage.set_vehicle(car1)
    print(garage.to_string())

    garage.set_vehicle(None)
    print(garage.to_string())

    truck1 = Truck("red", True)
    garage.set_vehicle(truck1)
    print(garage.to_string())

    # Create a GarageTester object and get an example
    tester = GarageTester()
    print("\nGarageTester Example:")
    tester.getExample()

    # Create a Customer object
    customer1 = Customer("John Doe", "123 Main St")
    print("\nCustomer Details:")
    print(customer1.to_string())