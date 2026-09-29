def load_inventory():
    try:
        # 'r' stands for read mode
        with open("inventory.txt", "r") as file:
            lines = file.readlines()

            # If the file exist but is completely empty
            if not lines:
                return 0, []

            # The first line is our total
            saved_total = int(lines[0].strip())

            # The rest of the lines are our trasaction history
            saved_history = []
            for line in lines[1:]:
                saved_history.append(int(line.strip()))

            print(f"[System] Loaded previous inventory: {saved_total} units.")
            return saved_total, saved_history

    except FileNotFoundError:
        # If the file doesn't exist yet, we start fresh without crashing
        print("[System] No previous save foud, Starting fresh.")
        return 0, []


def save_inventory(total, history):
    # 'w' stands for write mode (this will create or overwrite the file)
    with open("inventory.txt", "w") as file:
        file.write(f"{total}\n") # Save total in line 1

        for item in history:
            file.write(f"{item}\n") # Save transaction history on a new line

    print(f"[System] Data Successfully saved to inventory.txt")                



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


def generate_report(total_units, failed_attempts, history_list):
    print ("\n=== End of Day Report ===")
    print(f"Total Units in Inventory: {total_units}")
    print(f"Total Deliveries Processed Today: {len(history_list)}")
    print(f"Failed/Rejected Entries: {failed_attempts}")  
    print(f"Trasanction History Log: {history_list}")


total_inventory, transaction_history = load_inventory()
failed_entries = 0

print("--- Persistent Inventory Auditor Started ---")
print("Enter Delivery Quantity. Type 'quit' to exit. \n")

while True:
    result = get_valid_input()

    if result == "quit":
        break

    elif result == "invalid":
        failed_entries += 1

    else:
        total_inventory = process_delivery(total_inventory, result)
        transaction_history.append(result)

        print(f"Delivery of {result} accepted.")    
        print(f"Current Inventory: {total_inventory}\n")    

generate_report(total_inventory, failed_entries, transaction_history) 
save_inventory(total_inventory, transaction_history)       