# Test Code for PhysicalProduct and DigitalProduct classes:
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Product import Product

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