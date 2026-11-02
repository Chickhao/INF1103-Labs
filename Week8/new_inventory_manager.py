import json

class Product:
    def __init__(self, product_id, name, price, stock, history=None):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.history = [stock] if history is None else history

    def get_product_id(self):
        return self.product_id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_stock(self):
        return self.stock

    def update_stock(self, quantity):
        self.stock = quantity
        self.history.append(self.stock)

    def display_information(self):
        print(
            f"Product ID: {self.product_id} | Name: {self.name} | Price: ${self.price:.2f} | Stock: {self.stock}"
        )

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "history": self.history,
        }


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def search_product(self, product_id):
        for product in self.products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self):
        print("\nCurrent Inventory\n")
        print("-" * 48)
        for product in self.products:
            product.display_information()
        print("-" * 48)

    def get_products(self):
        return self.products.copy()


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
            {"product_id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15, "history": [15]},
            {"product_id": "P002", "name": "Mouse", "price": 25.50, "stock": 40, "history": [40]},
            {"product_id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25, "history": [25]}
        ]

    inventory = Inventory()
    for item in data:
        product = Product(
            item["product_id"], item["name"], item["price"], item["stock"], item["history"],
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

    try:
        price = float(input("Price: "))
        quantity = int(input("Stock Quantity: "))
    except ValueError:
        print("Error: Price must be a number and Quantity must be a whole number.\n")
        return

    new_product = Product(product_id, name, price, quantity)
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
        print(f"Stock History: {product.history}\n")
    else:
        print("Product not found.\n")

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