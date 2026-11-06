from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Inventory import Inventory


supplier = Supplier(
    "S001", "Test Supplier", "sales@example.com"
)

physical_product = PhysicalProduct(
    "P001", "Physical Product", 19.99, 100, 2.5,
    supplier=supplier,
)

digital_product = DigitalProduct(
    "D001", "Digital Product", 9.99, 50, 1.5,
    supplier=supplier,
)

inventory = Inventory()
inventory.add_product(physical_product)
inventory.add_product(digital_product)

for product in inventory.get_products():
    product.display_information()
    print(product.get_fulfilment_info())
    print()