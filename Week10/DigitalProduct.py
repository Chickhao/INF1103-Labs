from Product import Product
from Supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, file_size: float, supplier: Supplier, history: list[int] | None = None) -> None:
        super().__init__(product_id, name, price, stock, supplier, history)
        self.__file_size: float = file_size

    def display_information(self) -> None:
        super().display_information()
        print(f"File Size: {self.__file_size} MB")

    def get_fulfilment_info(self) -> str:
        return f"This product is delievered digitally."

    def to_dict(self) -> dict[str, object]:
        data = super().to_dict()
        data["type"] = "Digital"
        data["file_size"] = self.__file_size
        return data