from Product import Product
from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct


class ProductFactory:
    @staticmethod
    def create(
        product_type: str,
        product_id: str,
        name: str,
        price: float,
        stock_quantity: int,
        supplier: Supplier,
        weight: float = 0.0,
        file_size: float = 0.0,
        history: list[int] | None = None
    ) -> Product:
        product_type = product_type.strip().lower()

        if product_type == "physical":
            return PhysicalProduct(
                product_id=product_id,
                name=name,
                price=price,
                stock=stock_quantity,
                weight=weight,
                supplier=supplier,
                history=history,
            )

        if product_type == "digital":
            return DigitalProduct(
                product_id=product_id,
                name=name,
                price=price,
                stock=stock_quantity,
                file_size=file_size,
                supplier=supplier,
                history=history,
            )

        raise ValueError(
            f"Unknown product type: {product_type}"
        )