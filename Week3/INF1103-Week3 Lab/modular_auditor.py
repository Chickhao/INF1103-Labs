"""
Delivery Tracking System
-------------------------
Continuously accepts stock delivery quantities from the user, tracks the
running inventory total, calculates tax per delivery, and reports summary
statistics when the user types 'quit'.
"""

TAX_RATE = 0.10  # 10% tax on each delivery


def get_valid_input():
    """
    Prompt the user for a delivery quantity.

    Returns:
        int   -> a valid, non-negative delivery quantity
        "quit"-> signal that the user wants to end the program
        None  -> signal that the entry was invalid (so the caller can
                 count it as a failed/rejected attempt)
    """
    user_input = input("Enter delivery quantity (or 'quit' to exit): ").strip()

    if user_input.lower() == "quit":
        return "quit"

    try:
        value = int(user_input)
    except ValueError:
        print("  -> Invalid entry: please enter a whole number.\n")
        return None

    if value <= 0:
        print("  -> Invalid entry: quantity cannot be zero or negative.\n")
        return None

    return value


def process_delivery(current_total, new_value):
    """Add the new delivery amount to the running inventory total."""
    return current_total + new_value


def calculate_tax(amount):
    """Return the tax owed on a single delivery amount (10%)."""
    return amount * TAX_RATE


def generate_report(total_units, failed_attempts, total_inventory=None, total_tax=None):
    """
    Print the final summary report.

    total_units      -> count of deliveries successfully processed
    failed_attempts  -> count of rejected/invalid entries
    total_inventory  -> (optional) sum of all units received
    total_tax        -> (optional) sum of all tax collected
    """
    print("\n" + "=" * 42)
    print("          DELIVERY SUMMARY REPORT")
    print("=" * 42)
    print(f"Total Deliveries Processed:        {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")
    if total_inventory is not None:
        print(f"Total Inventory Received:          {total_inventory} units")
    if total_tax is not None:
        print(f"Total Tax Collected:               ${total_tax:.2f}")
    print("=" * 42)


def main():
    inventory_total = 0
    total_tax_collected = 0.0
    deliveries_count = 0
    failed_attempts = 0

    print("=== Delivery Tracking System ===")
    print("Type a whole number for each delivery, or 'quit' to finish.\n")

    while True:
        result = get_valid_input()

        if result == "quit":
            break
        elif result is None:
            failed_attempts += 1
            continue
        else:
            inventory_total = process_delivery(inventory_total, result)
            tax = calculate_tax(result)
            total_tax_collected += tax
            deliveries_count += 1
            print(
                f"  -> Recorded {result} units | Tax: ${tax:.2f} "
                f"| Running Inventory: {inventory_total}\n"
            )

    generate_report(deliveries_count, failed_attempts, inventory_total, total_tax_collected)


if __name__ == "__main__":
    main()