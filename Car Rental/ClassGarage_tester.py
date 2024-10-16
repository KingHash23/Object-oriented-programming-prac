#class GarageTester
class GarageTester:
    def getExample(self):
        truck = Truck("black", trailer=False)
        garage = Garage()
        garage.set_vehicle(truck)
        # Print the description of the vehicle in the garage
        print(garage.to_string())
# Implementation
tester = GarageTester()
tester.getExample()