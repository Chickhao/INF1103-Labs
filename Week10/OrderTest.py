from Order import Order
from AssociationTest import physical_product, digital_product


order_a = Order("O001")
order_a.add_order_line(physical_product, 2)
order_a.add_order_line(digital_product, 1)


for line in order_a.get_order_lines():
    print(line.get_product().get_name, line.get_quantity(), f"${line.calculate_subtotal():.2f}")
    print(f"Total: ${order_a.calculate_total():.2f}")

