class Product:
    def __init__(self, product_id, name, price, stock, history=None):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__history = [stock] if history is None else history

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