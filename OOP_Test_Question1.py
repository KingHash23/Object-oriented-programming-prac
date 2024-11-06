# # OBBA MARK CALVIN B24277 S23B23\047

# A. Creating Character and Vehicle Classes (Encapsulation)
# Creating Character class
class Character:
    def __init__(self, name, health, position):
        self.__name = name       # Private attribute for encapsulation
        self.__health = health
        self.__position = position
        self.__in_vehicle = None  # Tracks if the character is in a vehicle

    def move(self, new_position):  # Method to move the character
        if self.__in_vehicle:
            print(f"{self.__name} cannot move independently while in a vehicle!")
        else:
            self.__position = new_position
            print(f"{self.__name} moved to position {self.__position}.")

    def attack(self, target):      # Method for the character to attack
        print(f"{self.__name} attacks {target}!")

    def interact(self, item):      # Method for interaction (e.g., interacting with objects or other characters)
        print(f"{self.__name} interacts with {item}.")

    def get_name(self):            # Getter for name (demonstrating encapsulation)
        return self.__name

# Creating Vehicle class
class Vehicle:
    def __init__(self, vehicle_type, speed, fuel_level):
        self.__type = vehicle_type       # Private attribute for encapsulation
        self.__speed = speed
        self.__fuel_level = fuel_level

    def drive(self, distance):           # Method to drive the vehicle
        fuel_needed = distance // 10
        if self.__fuel_level >= fuel_needed:
            self.__fuel_level -= fuel_needed
            print(f"{self.__type} drove {distance} units. Remaining fuel: {self.__fuel_level}.")
        else:
            print(f"Not enough fuel to drive {distance} units. Please refuel.")

    def refuel(self, amount):            # Method to refuel the vehicle
        self.__fuel_level += amount
        print(f"{self.__type} refueled. Current fuel level: {self.__fuel_level}.")

    def stop(self):                      # Method to stop the vehicle
        print(f"{self.__type} has stopped.")

    def get_type(self):  # Getter for vehicle type
        return self.__type

#  B: Creating a subclass CharacterInteractingWithVehicle that inherits Character
class CharacterInteractingWithVehicle(Character):
    def __init__(self, name, health, position):
        super().__init__(name, health, position)
        self.__in_vehicle = None  # Tracks if the character is in a vehicle

    def get_in(self, vehicle):     # Method for interacting with a vehicle
        if self.__in_vehicle:
            print(f"{self.get_name()} is already in a vehicle!")
        else:
            self.__in_vehicle = vehicle
            print(f"{self.get_name()} got into the {vehicle.get_type()}.")

    def get_out(self):
        if self.__in_vehicle:
            print(f"{self.get_name()} got out of the {self.__in_vehicle.get_type()}.")
            self.__in_vehicle = None
        else:
            print(f"{self.get_name()} is not in a vehicle!")

    def drive_vehicle(self, distance):
        if self.__in_vehicle:
            self.__in_vehicle.drive(distance)
        else:
            print(f"{self.get_name()} is not in a vehicle to drive!")

# C. Specialized Character Abilities using Inheritance
class HeroCharacter(Character):
    def __init__(self, name, health, position, power_level):
        super().__init__(name, health, position)
        self.__power_level = power_level

    def double_jump(self):                  # Special ability: double jump
        print(f"{self.get_name()} performed a double jump!")
    
    def fast_run(self):                     # Special ability: fast run
        print(f"{self.get_name()} is running at super speed!")
    
    def instant_healing(self):              # Special ability: instant healing
        print(f"{self.get_name()} is healed in 1ms!")
        
    def unlimited_weapons(self):            # Special ability: unlimited weapons
        print(f"{self.get_name()} has unlimited weapons!")

# D. Handling Different Types of Objects (Polymorphism)
# Example of polymorphism in character interactions
characters = [Character("Calvin", 100, (0, 0)), HeroCharacter("AwesomeCalvin", 120, (0, 0), 80)]
for char in characters:
    char.move((10, 10))  # Both Character and HeroCharacter can use move()
    if isinstance(char, HeroCharacter):
        char.double_jump()  # Only HeroCharacter can double jump

# E. Simple Game Scenario
def mission_scenario():
    # Create a CharacterInteractingWithVehicle and a Vehicle
    character = CharacterInteractingWithVehicle("Calvin", 100, (0, 0))
    car = Vehicle("Car", 150, 80)
    character.move((10, 15))                # Character moves to a new position
    character.get_in(car)                   # Character gets into the car
    character.drive_vehicle(50)             # Character tries to drive the car
    character.get_out()                     # Character encounters an obstacle and gets out of the car
    character.attack("enemy")               # Character attacks an enemy
    character.move((60, 56))                # Character completes the mission by moving to the final position 
    print("Mission Accomplished!")
    
# Demonstrations
print("###### Character and Vehicle Demonstration ######")
character = Character("Calvin", 100, (0, 0))
vehicle = Vehicle("Car", 120, 50)
character.move((10, 15))
character.attack("enemy")
character.interact("a mysterious object")
vehicle.drive(30)
vehicle.refuel(34)
vehicle.stop()

print("\n###### Vehicle Interaction Demonstration (Part b) ######")
character_with_vehicle = CharacterInteractingWithVehicle("Calvin", 100, (0, 0))
character_with_vehicle.get_in(vehicle)
character_with_vehicle.drive_vehicle(50)
character_with_vehicle.get_out()

print("\n###### Specialized Abilities Demonstration ######")
hero = HeroCharacter("AwesomeCalvin", 120, (0, 0), 80)
hero.instant_healing()
hero.double_jump()
hero.unlimited_weapons()
hero.fast_run()

print("\n###### Mission Scenario ######")
mission_scenario()
