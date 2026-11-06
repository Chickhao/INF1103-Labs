from Inventory import Inventory
from AssociationTest import physical_product

inventory_a = Inventory()
inventory_b = Inventory()

inventory_a.add_product(physical_product)
inventory_a.remove_product("P001")

physical_product.display_information()

inventory_b.add_product(physical_product)

assert inventory_a.search_product("P001") is None
assert inventory_b.search_product("P001") is physical_product