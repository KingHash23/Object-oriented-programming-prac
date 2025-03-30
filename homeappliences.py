class Device:
    def __init__(self, device_name, model, status):
        self.device_name = device_name
        self.model = model
        self.status = status


class Smartphone(Device):
    def __init__(self, device_name, model, status, battery_level, storage_capacity):
        super().__init__(device_name, model, status)
        self.battery_level = battery_level
        self.storage_capacity = storage_capacity

    def turn_on(self):
        if self.status == "on":
            print("Device is already turned on.")
        else:
            self.status = "on"
            print("Device turned on.")

    def turn_off(self):
        if self.status == "off":
            print("Device is already turned off.")
        else:
            self.status = "off"
            print("Device turned off.")

    def display_device_info(self):
        print(f"Device Name: {self.device_name}")
        print(f"Model: {self.model}")
        print(f"Status: {self.status}")
        print(f"Battery Level: {self.battery_level}%")
        print(f"Storage Capacity: {self.storage_capacity}GB")


# Creating a smartphone object
smartphone = Smartphone("iPhone", "13", "off", 80, 512)

# Turning the device on
smartphone.turn_on()

# Displaying device information
smartphone.display_device_info()

# Turning the device off
smartphone.turn_off()

# Displaying device information
smartphone.display_device_info()

# Turning the device on again
smartphone.turn_on()

# Displaying device information
smartphone.display_device_info()
