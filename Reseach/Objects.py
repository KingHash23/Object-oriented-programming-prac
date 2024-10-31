# class Coordinate():
#     def __init__(self, other):
#         self.x = X
#         self.y = y
#     def distance(self, other):
#         x_diff_sq = (self.x-other.x)**2
#         y_diff_sq = (self.y-other.x)**2 
#         return (x_diff_sq + y_diff_sp)**0.5

# point1 = Coordinate(3,4)
# point2 = Coordinate(2,1)
# print(point1.distance(point2))   
# print(Coordinate.distance(point1, point2))
# 2 class Car
class car (vehicle):
    def __init__(self, color, winter_tires = false):
        super().__init__(color)   #calling the constructor of the parent class (vehicle) which is" __init__(color)" to set the color
        self.winter_tires = winter_tires
    def to_string (self):
        vehicle_color = super().to_string()
        winter_tire_info = f"vehicle has winter tires: {self.winter_tires}"
        return f"{vehicle_color} \n{winter_tire_info} "
car1 = car("blue", True)
print(car1.to_string())   
        