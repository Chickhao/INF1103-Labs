import json
from Product import Product
from PhysicalProduct import PhysicalProduct
from Inventory import Inventory
from DigitalProduct import DigitalProduct
from CanBeShipped import CanBeShipped




def load_inventory() -> Inventory:
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

def save_inventory(inventory) -> None:
    data = []
    for product in inventory.get_products():
        data.append(product.to_dict())
    
    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)


def add_product(inventory) -> None:
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

def update_stock(inventory) -> None:
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

def search_product(inventory) -> None:
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")

    product = inventory.search_product(product_id)
    if product:
        print("Product Found:\n")
        product.display_information()
        print(f"Stock History: {product._Product__history}\n")
    else:
        print("Product not found.\n")

def main() -> None:
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
