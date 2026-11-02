import json
from abc import ABC, abstractmethod

class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass

class Product(ABC):
    def __init__(self, product_id, name, price, stock, history=None):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__history = [stock] if history is None else history

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def update_stock(self, quantity):
        self.__stock = quantity
        self.__history.append(self.__stock)

    @abstractmethod
    def get_fulfilment_info(self):
        pass

    def display_information(self):
        print(
            f"Product ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}"
        )

    def to_dict(self):
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "history": self.__history,
        }


class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self):
        print("\nCurrent Inventory\n")
        print("-" * 48)
        for product in self.__products:
            product.display_information()
        print("-" * 48)

    def get_products(self):
        return self.__products.copy()

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight, history=None):
        super().__init__(product_id, name, price, stock, history)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self):
        return f"This product requires physical shipping."

    def calculate_shipping_cost(self):
        return self.__weight * 5.00  # Example: $5 per kg

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Physical"
        data["weight"] = self.__weight
        return data


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, file_size, history=None):
        super().__init__(product_id, name, price, stock, history)
        self.__file_size = file_size

    def display_information(self):
        super().display_information()
        print(f"File Size: {self.__file_size} MB")

    def get_fulfilment_info(self):
        return f"This product is delievered digitally."

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Digital"
        data["file_size"] = self.__file_size
        return data


def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)
            print("inventory.json found.")
            print("Invenotry loaded successfully. \n")

    except FileNotFoundError:
        print("inventory.json not found.")
        print("Inventory initialized with default products.\n")
        data = [
            {"product_id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15, "history": [15], "type": "Physical", "weight": 2.0},
            {"product_id": "P002", "name": "Mouse", "price": 25.50, "stock": 40, "history": [40], "type": "Physical", "weight": 0.1},
            {"product_id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25, "history": [25], "type": "Physical", "weight": 0.8}
        ]

    inventory = Inventory()

    for item in data:
        if item["type"] == "Physical":
            product = PhysicalProduct(
                item["product_id"], item["name"], item["price"], item["stock"], item["weight"], item["history"],
            )
        else:
            product = DigitalProduct(
                item["product_id"], item["name"], item["price"], item["stock"], item["file_size"], item["history"],
            )

        inventory.add_product(product)

    return inventory

def save_inventory(inventory):
    data = []
    for product in inventory.get_products():
        data.append(product.to_dict())
    
    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)


def add_product(inventory):
    print("\nAdd New Product\n")
    product_id = input("Product ID: ")
    name = input("Product Name: ")
    product_type = input("Product Type (1. Physical, 2. Digital): ")

    if product_type not in ("1", "2"):
        print("Invalid Product Type. \n")
        return

    try:
        price = float(input("Price: "))
        quantity = int(input("Stock Quantity: "))

        if product_type == "1":
            weight = float(input("Weight (kg): "))
            new_product = PhysicalProduct(product_id, name, price, quantity, weight)
        else:
            file_size = float(input("File Size (MB): "))
            new_product = DigitalProduct(product_id, name, price, quantity, file_size)
    except ValueError:
        print("Error: Price must be a number and Quantity must be a whole number.\n")
        return

    inventory.add_product(new_product)
    print("\nProduct added successfully!\n")

def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ")

    product = inventory.search_product(product_id)
    if product:
        print("Product Found:\n")
        print(f"Name: {product.get_name()}\n")
        try:
            new_quantity = int(input("Enter new stock quantity: "))
            product.update_stock(new_quantity)
            print("\nStock updated successfully!\n")
        except ValueError:
            print("Error: Quantity must be a whole number.\n")
    else:
        print("Product not found.\n")

def search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")

    product = inventory.search_product(product_id)
    if product:
        print("Product Found:\n")
        product.display_information()
        print(f"Stock History: {product._Product__history}\n")
    else:
        print("Product not found.\n")

''' 
Test Code for PhysicalProduct and DigitalProduct classes:

physical = PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.0)
digital = DigitalProduct("D001", "E-book", 12.00, 100, 50.0)

physical.display_information()
digital.display_information()

print(physical.get_fulfilment_info())
print(digital.get_fulfilment_info())

try:
    Product("P000", "Generic Product", 10.00, 1)
except TypeError as error:
    print(f"Error: {error}")

light_product = PhysicalProduct("P002", "Lightweight Item", 10.00, 1, 1.0)
heavy_product = PhysicalProduct("P003", "Heavy Item", 10.00, 1, 3.0)

print(light_product.calculate_shipping_cost())  # Output: 5.0
print(heavy_product.calculate_shipping_cost())  # Output: 5.0
'''

def main():
    print("========================================") 
    print("INVENTORY MANAGEMENT SYSTEM") 
    print("========================================") 
    print()

    inventory = load_inventory()

    while True:
        print("\n----------- MENU -----------") 
        print("1. Display All Products") 
        print("2. Add Product") 
        print("3. Update Stock") 
        print("4. Search Product") 
        print("5. Save Inventory") 
        print("6. Exit") 
        print("----------------------------") 
        
        choice = input("Enter option: ") 

        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_product(inventory)
            save_inventory(inventory)
        elif choice == "3":
            update_stock(inventory)
            save_inventory(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            save_inventory(inventory)
            print("Inventory saved successfully.")
        elif choice == "6":
            print("Saving inventory before exit...\n")
            save_inventory(inventory)
            print("Inventory saved successfully.")
            print("Thank you for using Inventory Management System.\n")
            print("Program terminated.\n")
            break
        else:
            print("Invalid selection.\n")


if __name__ == "__main__":
    main()
