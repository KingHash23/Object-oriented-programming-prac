class Shopitems:
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
class Electronics(Shopitems):
    def __init__(self, name, price, stock_quantity, warranty_period):
        super().__init__(name, price, stock_quantity)
        self.warranty_period = warranty_period
    def sell_items(self,quantity):
        #hnadle cases where stock quantity becomes negative
        if self.stock_quantity < quantity:
            print("Not enough stock.")  
            return
        self.stock_quantity -= quantity
        print(f"{quantity} {self.name} sold.")
    
    def display_info(self):
        print(f"Name: {self.name}, Price: {self.price}, Stock Quantity: {self.stock_quantity}, Warranty Period: {self.warranty_period}")
        
#two electronics objects and sell some quantities, show how stock changes
electronics1 = Electronics("Laptop", 1000, 10, 2)
electronics2 = Electronics("Smartphone", 800, 5, 1)
electronics1.sell_items(3)
electronics2.sell_items(2) 

electronics1.display_info()
electronics2.display_info()
