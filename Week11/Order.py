from OrderLine import OrderLine
from Product import Product
from DiscountStrategy import DiscountStrategy, NoDiscount


class Order:
    def __init__(
        self,
        order_id: str,
        discount: DiscountStrategy | None = None
    ) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []
        self.__discount: DiscountStrategy = (
            discount if discount is not None else NoDiscount()
        )

    def get_order_id(self) -> str:
        return self.__order_id

    def get_order_lines(self) -> list[OrderLine]:
        return self.__order_lines.copy()

    def add_order_line(
        self,
        product: Product,
        quantity: int
    ) -> None:
        self.__order_lines.append(OrderLine(product, quantity))

    def remove_order_line(self, index: int) -> None:
        del self.__order_lines[index]

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.__discount = discount

    def calculate_total(self) -> float:
        subtotal = sum(
            (
                line.calculate_subtotal()
                for line in self.__order_lines
            ),
            0.0,
        )
        return self.__discount.apply(subtotal)