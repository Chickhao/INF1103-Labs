from abc import ABC, abstractmethod
from Supplier import Supplier


class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, history: list[int] =None) -> None:
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock
        self.__history: list[int] = ([stock] if history is None else history)
        self.__supplier: Supplier = supplier    

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def update_stock(self, quantity):
        self.__stock = quantity
        self.__history.append(self.__stock)

    @abstractmethod
    def get_fulfilment_info(self):
        pass

    def display_information(self):
        print(
            f"Product ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}"
        )

    def to_dict(self):
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "history": self.__history,
        }

    def get_supplier(self) -> Supplier:
        return self.__supplier

    