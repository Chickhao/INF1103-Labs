from CanBeShipped import CanBeShipped
from Product import Product

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight, history=None):
        super().__init__(product_id, name, price, stock, history)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self):
        return f"This product requires physical shipping."

    def calculate_shipping_cost(self):
        return self.__weight * 5.00  # Example: $5 per kg

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Physical"
        data["weight"] = self.__weight
        return data