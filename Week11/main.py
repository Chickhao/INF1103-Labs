import json, csv
from Product import Product
from PhysicalProduct import PhysicalProduct
from Inventory import Inventory
from DigitalProduct import DigitalProduct
from CanBeShipped import CanBeShipped
from Supplier import Supplier
from ProductFactory import ProductFactory


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
            {"product_id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15, "history": [15], "type": "Physical", "weight": 2.0,},
            {"product_id": "P002", "name": "Mouse", "price": 25.50, "stock": 40, "history": [40], "type": "Physical", "weight": 0.1,},
            {"product_id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25, "history": [25], "type": "Physical", "weight": 0.8,}
        ]

    inventory = Inventory()
    suppliers: dict[str, Supplier] = {}

    for item in data:
        supplier_data = item.get("supplier") or {
            "supplier_id": "S000",
            "name": "Supplier not recorded",
            "contact_email": "",
        }
        supplier_id = supplier_data["supplier_id"]

        if supplier_id not in suppliers:
            suppliers[supplier_id] = Supplier(
                supplier_id,
                supplier_data["name"],
                supplier_data["contact_email"],
            )

        supplier = suppliers[supplier_id]

        product = ProductFactory.create(
            product_type=item["type"],
            product_id=item["product_id"],
            name=item["name"],
            price=item["price"],
            stock_quantity=item["stock"],
            supplier=supplier,
            weight=item.get("weight", 0.0),
            file_size=item.get("file_size", 0.0),
            history=item.get("history"),
        )

        inventory.add_product(product)
    return inventory


def save_inventory(inventory: Inventory) -> None:
    data = []
    for product in inventory.get_products():
        data.append(product.to_dict())
    
    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)


def add_product(inventory: Inventory) -> None:
    print("\nAdd New Product\n")
    product_id = input("Product ID: ")
    name = input("Product Name: ")
    product_type = input("Product Type (1. Physical, 2. Digital): ")

    if product_type not in ("1", "2"):
        print("Invalid Product Type. \n")
        return

    try:
        price = get_positive_float("Price: ")
        quantity = get_nonnegative_int("Stock Quantity: ")

        suppliers = {product.get_supplier().get_supplier_id(): product.get_supplier() for product in inventory.get_products()}
        supplier_id = input("Supplier ID: ")

        if supplier_id in suppliers:
            supplier = suppliers[supplier_id]
        else:
            supplier = Supplier(supplier_id, input("Supplier Name: "), input("Supplier Email: "),)

        if product_type == "1":
            weight = float(input("Weight (kg): "))
            new_product = ProductFactory.create(
                "physical",
                product_id,
                name,
                price,
                quantity,
                supplier,
                weight=weight,
            )
        else:
            file_size = float(input("File Size (MB): "))
            new_product = ProductFactory.create(
                "digital",
                product_id,
                name,
                price,
                quantity,
                supplier,
                file_size=file_size,
            )
    except ValueError:
        print("Error: Price must be a number and Quantity must be a whole number.\n")
        return

    inventory.add_product(new_product)
    print("\nProduct added successfully!\n")

def update_stock(inventory: Inventory) -> None:
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ")

    product = inventory.search_product(product_id)
    if product:
        print("Product Found:\n")
        print(f"Name: {product.get_name()}\n")
        try:
            new_quantity = get_nonnegative_int("Enter new stock quantity: ")
            product.update_stock(new_quantity)
            print("\nStock updated successfully!\n")
        except ValueError:
            print("Error: Quantity must be a whole number.\n")
    else:
        print("Product not found.\n")

def search_product(inventory: Inventory) -> None:
    print("\nSearch Product")
    product_id = input("Enter Product ID: ")

    product = inventory.search_product(product_id)
    if product:
        print("Product Found:\n")
        product.display_information()
        product.get_supplier().display_information()
        print(f"Stock History: {product.get_history()}\n")
    else:
        print("Product not found.\n")

def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print(
                    "Please enter a number greater than zero."
                )
                continue

            return value

        except ValueError:
            print(
                "Please enter a valid number, e.g. 12.50"
            )

def get_nonnegative_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))

            if value < 0:
                print(
                    "Please enter zero or a positive whole number."
                )
                continue

            return value

        except ValueError:
            print("Please enter a valid whole number.")

def load_products(
    path: str,
    inventory: Inventory,
    supplier: Supplier
) -> None:
    try:
        file = open(path, newline="", encoding="utf-8")

    except FileNotFoundError:
        print(f"Products file not found: {path}")

    else:
        loaded = 0

        with file:
            reader = csv.reader(file)
            next(reader, None)  # Skip the header.

            for row_number, row in enumerate(reader, start=2):
                try:
                    if len(row) != 5:
                        raise ValueError(
                            "Expected five CSV fields."
                        )

                    (
                        product_type,
                        product_id,
                        name,
                        price_text,
                        stock_text,
                    ) = row

                    product = ProductFactory.create(
                        product_type=product_type,
                        product_id=product_id,
                        name=name,
                        price=float(price_text),
                        stock_quantity=int(stock_text),
                        supplier=supplier,
                    )

                    inventory.add_product(product)
                    loaded += 1

                except ValueError as error:
                    print(
                        f"Skipping row {row_number}: {error}"
                    )

        print(f"{loaded} products loaded.")

    finally:
        print("Load attempt finished.")

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
