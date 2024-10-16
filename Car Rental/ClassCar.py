# 2 class Car
class Car (vehicle):
    def __init__(self, color, winter_tires=False):
        self.winter_tires = winter_tires
        super().__init__(color)   #calling the constructor of the parent class (vehicle) which is" __init__(color)" to set the color
    def to_string (self):
        return f" {super().to_string()} \n Vehicle has winter tires:{self.winter_tires} "
       
#The implemetation to check if it executes(output)
car1 = Car("blue", True)
print(car1.to_string())
        