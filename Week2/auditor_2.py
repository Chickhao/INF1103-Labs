total_inventory = 0
failed_entries = 0

print("--- Inventory Auditor Started ---")
print("Enter Delivery Quantity. Type 'quit' to exit. \n")

# 2. Run in a continuous loop to accept user input
while True:
    user_input = input("Enter Stock Quantity: ")

    #Check for the quit condition first
    if user_input.lower() == 'quit':
        break

    #Enforce Business Rule: Reject negative numbers
    #We check if it starts with a minus sign, and if the rest is a number
    elif user_input.startswith('-') and user_input[1:].isdigit():
        print("Error: Cannot accpet negative stock values.")
        failed_entries += 1


    #4. Handle invalide input: Reject text
    elif not user_input.isdigit():
        print("Error: Invalid input. Please enter a whole number.")
        failed_entries += 1

    #3. Accept Stock Value as Integers (if it didn't trigger the errors above)
    else:
        stock_quantity = int(user_input)

        #6. Manage State: Add to the running total
        total_inventory += stock_quantity
        print(f"Accepted {stock_quantity} units. Current Inventory: {total_inventory}")

        #7. Trigger Overstock Alert
        if total_inventory > 500:
            print("\n ALERT: Storage capacity exceeded! (Over 500 units)")
            break


print ("\n=== End of Day Report ===")
print(f"Total Units Processed: {total_inventory}")
print(f"Failed/Rejected Entries: {failed_entries}")    