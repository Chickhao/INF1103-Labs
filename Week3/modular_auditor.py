def manage_inventory():
    total_inventory = 0
    failed_entries = 0
    
    print("--- Inventory Management System ---")
    print("Type 'quit' at any time to exit.\n")

    while True:
        user_input = input("Enter stock quantity: ").strip()

        # 2. Check for quit condition
        if user_input.lower() == 'quit':
            break

        # 4. Handle invalid string input (Hint: using .isdigit())
        # We use lstrip('-') so we can still catch and gracefully reject negative numbers in the next step, 
        # rather than just treating them as arbitrary text.
        if not user_input.lstrip('-').isdigit():
            print("Error: Invalid input. Please enter a numeric value (e.g., not 'ten').")
            failed_entries += 1
            continue

        # 3. Accept stock values as integers
        stock_quantity = int(user_input)

        # 5. Enforce business rules: Reject negative numbers
        if stock_quantity < 0:
            print("Error: Stock quantity cannot be negative.")
            failed_entries += 1
            continue

        # 6. Manage State: Running total
        total_inventory += stock_quantity
        print(f"Success! Current inventory is now: {total_inventory}")

        # 7. Trigger Overstock Alert
        if total_inventory > 500:
            print("\nOVERSTOCK ALERT: Total inventory has exceeded 500 units. Halting input.")
            break

    # 8. Reporting
    print("\n=== Session Summary ===")
    print(f"Total Units Processed (Inventory): {total_inventory}")
    print(f"Number of Failed/Rejected Entries: {failed_entries}")

# Run the program
if __name__ == "__main__":
    manage_inventory()