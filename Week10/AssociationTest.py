from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct

supplier = Supplier("S001", "Test Supplier", "sales@emai.com")
physical_product = PhysicalProduct("P001", "Test Physical Product", 19.99, 100, 2.5, supplier=supplier)
digital_product = DigitalProduct("D001", "Test Digital Product", 9.99, 50, 1.5, supplier=supplier)

physical_product.get_supplier().display_information()
digital_product.get_supplier().display_information()

assert physical_product.get_supplier() is digital_product.get_supplier()


'''
"Predict First" Explanation:

Product stores a reference to an independently created Supplier. This is association because neither object is an owned componenet of the other.

'''

del supplier
physical_product.get_supplier().display_information()
digital_product.get_supplier().display_information()