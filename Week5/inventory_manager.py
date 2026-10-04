import json

def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)
            print("inventory.json found.") 
            print("Inventory loaded successfully.\n") 
            return data
    except FileNotFoundError:
        print("inventory.json not found.")
        print("Inventory initialized with default products.\n")
        return [
            {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15, "history": [15]}, 
            {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40, "history": [40]}, 
            {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25, "history": [25]} 
        ]

def display_all(inventory):
    print("\nCurrent Inventory") 
    print("----------------------------------------")
    for item in inventory:
        print(f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']:.2f} | Stock: {item['stock']}") 
    print("----------------------------------------\n")

def add_product(inventory):
    print("\n--- Add New Product ---")
    prod_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    try:
        price = float(input("Enter Product Price: "))
        initial_stock = int(input("Enter Initial Quantity: "))
    except ValueError:
        print("Error: Price must be a number and Quantity must be a whole number.")
        return
    inventory.append({"id": prod_id, "name": name, "price": price, "stock": initial_stock, "history": [initial_stock]})
    print(f"Success: Added '{name}' to inventory.")

def update_stock(inventory):
    print("\n--- Update Stock ---")
    prod_id = input("Enter Product ID to update: ")
    for item in inventory:
        if item["id"] == prod_id:
            try:
                transaction = int(input(f"Enter transaction amount for '{item['name']}': "))
            except ValueError:
                print("Error: Transaction must be a whole number.")
                return
            item["stock"] += transaction
            item["history"].append(transaction)
            print(f"Success: Stock updated. New total for '{item['name']}' is {item['stock']}.")
            return
    print("Error: Product ID not found.")

def search_product(inventory):
    print("\n--- Search Product ---")
    search_term = input("Enter Product Name or ID: ").lower()
    for item in inventory:
        if item["id"].lower() == search_term or item["name"].lower() == search_term:
            print("\n--- Search Result ---")
            print(f"ID:      {item['id']}")
            print(f"Name:    {item['name']}")
            print(f"Price:   ${item['price']:.2f}")
            print(f"Stock:   {item['stock']}")
            return
    print("No matching product found.")

def main():
    print("========================================") 
    print("INVENTORY MANAGEMENT SYSTEM") 
    print("========================================") 
    print()
    
    # Phase B: Now calling the load function instead of a hardcoded list
    inventory = load_inventory()

    while True:
        print("----------- MENU -----------") 
        print("1. Display All Products") 
        print("2. Add Product") 
        print("3. Update Stock") 
        print("4. Search Product") 
        print("5. Save Inventory") 
        print("6. Exit") 
        print("----------------------------") 
        
        choice = input("\nEnter option: ") 
        
        if choice == '1': display_all(inventory)
        elif choice == '2': add_product(inventory)
        elif choice == '3': update_stock(inventory)
        elif choice == '4': search_product(inventory)
        elif choice == '5': print("\n[Notice] Save function will be built in Phase C.")
        elif choice == '6': 
            print("\nExiting program...")
            break
        else: print("\nInvalid selection. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()