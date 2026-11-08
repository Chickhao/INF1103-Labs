# Test Code for PhysicalProduct and DigitalProduct classes:
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Product import Product
from Supplier import Supplier
from Inventory import Inventory
from Order import Order

'''
physical = PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.0)
digital = DigitalProduct("D001", "E-book", 12.00, 100, 50.0)

physical.display_information()
digital.display_information()

print(physical.get_fulfilment_info())
print(digital.get_fulfilment_info())

try:
    Product("P000", "Generic Product", 10.00, 1)
except TypeError as error:
    print(f"Error: {error}")

light_product = PhysicalProduct("P002", "Lightweight Item", 10.00, 1, 1.0)
heavy_product = PhysicalProduct("P003", "Heavy Item", 10.00, 1, 3.0)

print(light_product.calculate_shipping_cost())  # Output: 5.0
print(heavy_product.calculate_shipping_cost())  # Output: 5.0

'''

## Association
supplier = Supplier("S001", "Tech Supply", "sales@example.com",)

physical = PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.0, supplier=supplier,)
digital = DigitalProduct("D001", "E-book", 12.00, 100, 50.0, supplier=supplier,)

assert physical.get_supplier() is supplier
assert digital.get_supplier() is supplier

physical.get_supplier().display_information()
digital.get_supplier().display_information()


del supplier

physical.get_supplier().display_information()
digital.get_supplier().display_information()


## Aggregation
inventory_a = Inventory()
inventory_b = Inventory()

inventory_a.add_product(physical)
inventory_a.remove_product("P001")

assert inventory_a.find_product("P001") is None
physical.display_information()

inventory_b.add_product(physical)
assert inventory_b.find_product("P001") is physical

## Composition
order_a = Order("O001")
order_a.add_order_line(physical, 2)
order_a.add_order_line(digital, 3)

for line in order_a.get_order_lines():
    print(
        f"{line.get_product().get_name()} "
        f"x {line.get_quantity()}: "
        f"{line.calculate_subtotal():.2f}"
    )

print(f"Order total: {order_a.calculate_total():.2f}")

order_b = Order("O002")
order_b.add_order_line(physical, 1)

line_a = order_a.get_order_lines()[0]
line_b = order_b.get_order_lines()[0]

assert line_a is not line_b
assert line_a.get_product() is line_b.get_product()

order_b.remove_order_line(0)

assert order_b.calculate_total() == 0.0
assert inventory_b.find_product("P001") is physical


## Liskov Substitution Principle
def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


show_product_details(physical)
show_product_details(digital)


for product in (physical, digital):
    previous_history = product.get_history()

    product.update_stock(7)

    assert product.get_stock() == 7
    assert product.get_history() == previous_history + [7]