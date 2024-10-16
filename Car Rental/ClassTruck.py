#class truck
class Truck(vehicle):
    def __init__(self,color, trailer=False):
        super().__init__(color)
        self.trailer = trailer
    def to_string(self):
        return f" {super().to_string()}\n Truck has a trailer: {self.trailer}"

# The implementation
truck1 = Truck("red", )
print(truck1.to_string())    
    