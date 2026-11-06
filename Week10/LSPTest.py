from Product import Product
from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


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

for product in (physical_product, digital_product):
    show_product_details(product)

    product.update_stock(8)
    assert product.get_stock() == 8

print("LSP tests passed.")