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

def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

def display_all(inventory):
    print("\nCurrent Inventory\n") 
    print("-" * 48)
    for item in inventory:
        print(f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']:.2f} | Stock: {item['stock']}") 
    print("-" * 48)

def add_product(inventory):
    print("\nAdd New Product\n")
    prod_id = input("Product ID: ")
    name = input("Product Name: ")
    
    try:
        price = float(input("Price: "))
        initial_stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Error: Price must be a number and Quantity must be a whole number.\n")
        return

    new_product = {
        "id": prod_id,
        "name": name,
        "price": price,
        "stock": initial_stock,
        "history": [initial_stock]
    }
    
    inventory.append(new_product)
    print("\nProduct added successfully!\n")

def update_stock(inventory):
    print("\nUpdate Stock")
    prod_id = input("Enter Product ID: ")
    
    for item in inventory:
        if item["id"] == prod_id:
            print("Product Found:\n")
            print(f"Name: {item['name']}\n")
            print(f"Current Stock: {item['stock']}\n")
            
            try:
                new_stock = int(input("New Stock Quantity: "))
            except ValueError:
                print("Error: Quantity must be a whole number.\n")
                return
            
            # Replaces the old stock value with the new one
            item["stock"] = new_stock
            item["history"].append(new_stock)
            
            print("Stock updated successfully!\n")
            return
            
    print("Product not found.\n")

def search_product(inventory):
    print("\nSearch Product\n")
    search_term = input("Enter Product ID: ")
    
    for item in inventory:
        if item["id"] == search_term:
            print("Product Found\n")
            print("-" * 48)
            print(f"ID: {item['id']}")
            print(f"Name: {item['name']}")
            print(f"Price: ${item['price']:.2f}")
            print(f"Stock: {item['stock']}")
            print("-" * 48)
            return
            
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
        
        if choice == '1':
            display_all(inventory)
        elif choice == '2':
            add_product(inventory)
        elif choice == '3':
            update_stock(inventory)
        elif choice == '4':
            search_product(inventory)
        elif choice == '5':
            print("Saving inventory...\n")
            save_inventory(inventory)
            print("Inventory saved successfully to inventory.json.\n")
        elif choice == '6':
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