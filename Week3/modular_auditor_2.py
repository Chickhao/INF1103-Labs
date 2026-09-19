def get_valid_input():
    user_input = input("Enter Stock quantity: ")

    if user_input.lower() == "quit":
        return "quit"
    
    elif user_input.startswith("-") and user_input[1:].isdigit():
        print("Error: Cannot accept negative stock value")
        return "invalid"

    elif not user_input.isdigit():
        print("Error: Invalid Input. Please enter a whole number.")
        return "invalid"

    else:
        # If if passes all checks, convert and return it as an integer
        return int(user_input)

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.10

def generate_report(total_deliveries, total_units, failed_attempts):
    print ("\n=== End of Day Report ===")
    print(f"Total Deliveries Processed: {total_deliveries}")
    print(f"Total Units Processed: {total_units}")
    print(f"Failed/Rejected Entries: {failed_attempts}")  


total_inventory = 0
failed_entries  =0
delivery_count = 0

print("--- Inventory Auditor Started ---")
print("Enter Delivery Quantity. Type 'quit' to exit. \n")

while True:
    result = get_valid_input()

    if result == "quit":
        break

    elif result == "invalid":
        failed_entries += 1

    else:
        total_inventory = process_delivery(total_inventory, result)
        tax_amount = calculate_tax(result)
        delivery_count += 1

        print(f"Delivery Accepted. Tax: {tax_amount: .2f}")    
        print(f"Current Inventory: {total_inventory}\n")    

generate_report(delivery_count, total_inventory, failed_entries)        