#class customer
class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def to_string(self):
        return f"Customer Name: {self.name}\nCustomer Address: {self.address}"

# Impementation
customer1 = Customer("Obba Mark Calvin", "Kissasi-Bukoto road")
print(customer1.to_string())