import os

class Product:
    """Class representing a product in the inventory."""
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name.lower()  # Convert name to lowercase
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount: int):
        """Update the product quantity."""
        assert amount >= 0, "Quantity cannot be negative."
        self.quantity = amount

    def __str__(self):
        return f"{self.name.capitalize()}: ${self.price} | Stock: {self.quantity}"


class Inventory:
    """Class representing the inventory system."""
    def __init__(self):
        self.products = {}

    def add_product(self, name: str, price: float, quantity: int):
        """Add or update a product in the inventory."""
        name = name.lower()  # Convert name to lowercase
        if name in self.products:
            self.products[name].update_quantity(self.products[name].quantity + quantity)
        else:
            self.products[name] = Product(name, price, quantity)

    def update_product_quantity(self, name: str, quantity: int):
        """Update the quantity of an existing product."""
        name = name.lower()  # Convert name to lowercase
        if name in self.products:
            new_quantity = self.products[name].quantity + quantity
            if new_quantity < 0:
                print("Error: Cannot reduce quantity below zero.")
            else:
                self.products[name].update_quantity(new_quantity)
                print(f"{abs(quantity)} items {'added' if quantity > 0 else 'removed'}.")
                print(f"Updated {name.capitalize()} stock to {new_quantity}.")
        else:
            print("Product not found.")

    def search_product(self, name: str):
        """Search for a product."""
        return self.products.get(name.lower(), None)

    def list_products(self):
        """List all products."""
        for product in self.products.values():
            print(product)


def clear_terminal():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    """Pause the screen until the user presses Enter."""
    input("\nPress Enter to continue...")

# Using the Inventory System
inventory = Inventory()

# Sample product additions
inventory.add_product("Laptop", 1200.99, 10)
inventory.add_product("Phone", 799.49, 25)

# Main user interaction
while True:
    clear_terminal()
    print("\nCurrent Inventory:")
    inventory.list_products()
    
    print("\nSelect an option:")
    print("1. Add a new product")
    print("2. Add stock to an existing product")
    print("3. Remove stock from an existing product")
    print("4. Run outer_function()")
    print("5. Write to inventory_log.txt")
    print("6. Exit")
    
    action = input("Enter your choice (1/2/3/4/5/6): ").strip()
    
    if action == "6":
        break
    
    if action == "1":
        product_name = input("Enter the new product name: ").strip()
        try:
            price = float(input("Enter the price of the product: "))
            quantity = int(input("Enter the initial stock quantity: "))
            inventory.add_product(product_name, price, quantity)
            clear_terminal()
            print(f"Added new product: {product_name.capitalize()} - ${price} | Stock: {quantity}")
            pause()
        except ValueError:
            print("Invalid input. Please enter valid numbers for price and quantity.")
        continue
    
    if action in ["2", "3"]:
        product_name = input("Enter the product name: ").strip()
        try:
            quantity = int(input("Enter the quantity: "))
            if action == "3":
                quantity = -quantity
            inventory.update_product_quantity(product_name, quantity)
            pause()
        except ValueError:
            print("Invalid quantity. Please enter a number.")
        continue
    
    if action == "4":
        def outer_function():
            global global_var
            global_var = "I am global"
            
            def inner_function():
                global global_var  # Corrected: Use global instead of nonlocal
                global_var = "Modified in inner"
            
            inner_function()
            print(global_var)
        
        outer_function()
        pause()
        continue
    
    if action == "5":
        with open("inventory_log.txt", "w") as file:
            file.write("Inventory system executed successfully.")
        print("inventory_log.txt has been updated.")
        pause()
        continue
    
    print("Invalid selection. Please enter a valid number.")

# Raising an exception
try:
    raise ValueError("This is a sample exception.")
except ValueError as e:
    print(f"Caught an exception: {e}")