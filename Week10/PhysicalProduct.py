from CanBeShipped import CanBeShipped
from Product import Product
from Supplier import Supplier

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float, supplier: Supplier, history: list[int] | None = None) -> None:
        super().__init__(product_id, name, price, stock, supplier, history)
        self.__weight: float = weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self) -> str:
        return f"This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return self.__weight * 5.00  # Example: $5 per kg

    def to_dict(self) -> dict[str, object]:
        data = super().to_dict()
        data["type"] = "Physical"
        data["weight"] = self.__weight
        return data