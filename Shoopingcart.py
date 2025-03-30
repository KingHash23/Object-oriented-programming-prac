# #shpping cart .py
# class Item:
#     def __init__(self, name, price, quantity):
#         self._name = name
#         self._price = price
#         self._quantity = quantity   

#     def get_name(self):
#         return self._name
    
#     def get_price(self):
#         return self._price
    
#     def get_quantity(self):
#         return self._quantity  
    
#     def set_quantity(self, quantity):
#         self._quantity = quantity

#     def __str__(self):
#         return f"{self._name} - {self._price} - {self._quantity}"   

# class ClothingItem(Item):
#     def __init__(self, name, price, quantity, size):
#         super().__init__(name, price, quantity)
#         self._size = size

#     def __str__(self):
#         return f"{super().__str__()}, Size: {self._size}"

# class ElectronicItem(Item):
#     def __init__(self, name, price, quantity, brand):
#         super().__init__(name, price, quantity)
#         self._brand = brand

#     def __str__(self):
#         return f"{super().__str__()}, Brand: {self._brand}"

# class ShoppingCart:
#     def __init__(self):
#         self._items = []

#     def add_item(self, item):
#         self._items.append(item)
#         if item in self._items:
#             raise TypeError(f"Item '{item.get_name()}' is already in cart.")
#         print(f"{item.get_name()} added to cart.")

#     def remove_item(self, item_name):
#         for item in self._items:
#             if item.get_name() == item_name:
#                 self._items.remove(item)
#                 print(f"{item_name} removed from cart.")
#                 return
#         raise ValueError(f"Item '{item_name}' not found in cart.")
    
#     def display_cart(self):
#         print("Your Cart:")
#         for item in self._items:
#             print(item)

#         total_price = sum(item.get_price() * item.get_quantity() for item in self._items)
#         print(f"Total Price: ${total_price:.2f}")

#     def clear_cart(self):
#         self._items = []
#         print("Cart cleared.")
# #example usage 
# cart = ShoppingCart()

# while True:    
#     print("\n1. Add Item")
#     print("2. Remove Item")
#     print("3. Display Cart")
#     print("4. Clear Cart")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":    
#         name = input("Enter item name: ")
#         price = float(input("Enter item price: "))
#         quantity = int(input("Enter item quantity: "))
#         item = Item(name, price, quantity)
#         cart.add_item(item)
#     elif choice == "2":
#         item_name = input("Enter item name to remove: ")
#         cart.remove_item(item_name)
#     elif choice == "3":
#         cart.display_cart()
#     elif choice == "4":
#         cart.clear_cart()
#     elif choice == "5":
#         break
#     else:
#         print("Invalid choice. Please try again.")
class Item:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, quantity):
        self._quantity = quantity

    def __str__(self):
        return f"{self._name} - {self._price:.2f} - {self._quantity}"


class ClothingItem(Item):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self._size = size

    def __str__(self):
        return f"{super().__str__()}, Size: {self._size}"


class ElectronicItem(Item):
    def __init__(self, name, price, quantity, brand):
        super().__init__(name, price, quantity)
        self._brand = brand

    def __str__(self):
        return f"{super().__str__()}, Brand: {self._brand}"


class ShoppingCart:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)
        print(f"{item.get_name()} added to cart.")

    def remove_item(self, item_name):
        for item in self._items:
            if item.get_name() == item_name:
                self._items.remove(item)
                print(f"{item_name} removed from cart.")
                return
        print(f"Item '{item_name}' not found in cart.")

    def display_cart(self):
        print("\nYour Cart:")
        if not self._items:
            print("Cart is empty.")
        else:
            for item in self._items:
                print(item)

        total_price = sum(item.get_price() * item.get_quantity() for item in self._items)
        print(f"Total Price: ${total_price:.2f}")

    def clear_cart(self):
        self._items = []
        print("Cart cleared.")


# Example usage without user input
cart = ShoppingCart()

# Create various items
item1 = Item("Laptop", 999.99, 1)
item2 = ClothingItem("T-Shirt", 19.99, 2, "M")
item3 = ElectronicItem("Smartphone", 699.99, 1, "BrandX")
item4 = Item("Book", 12.49, 3)

# Add items to the cart
cart.add_item(item1)
cart.add_item(item2)
cart.add_item(item3)
cart.add_item(item4)

# Display the cart
cart.display_cart()

# Remove an item
cart.remove_item("Book")

# Display the cart after removing an item
cart.display_cart()

# Clear the cart
cart.clear_cart()

# Display the cart after clearing
cart.display_cart()
     