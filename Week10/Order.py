from Product import Product
from Orderline import OrderLine

class Order:
    def __init__(self, order_id: str) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def get_order_lines(self) -> list[OrderLine]:
        return self.__order_lines.copy()

    def remove_order_line(self, index: int) -> None:
        del self.__order_lines[index]

    def calculate_total(self) -> float:
        return sum((line.calculate_subtotal() for line in self.__order_lines), 0.0)
     