#Car Rental
# 1 Class vehichle
class vehicle:
    def __init__(self,color):
        self.color = color
    def get_color(self):
        return self.color
    def to_string(self):   #to_string method will return the color of the vehicle after calling self.color
         return f"Vehicle color is {self.color}"
       
#The implemetation to check if it executes(output)
Vehicle_one = vehicle("red")
print(Vehicle_one.to_string())  
