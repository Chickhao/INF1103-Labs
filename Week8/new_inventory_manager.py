class Product:
    def __init__(self, product_id, name, price, stock, history=None):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.history = [stock] if history is None else history

    def get_product_id(self):
        return self.product_id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_stock(self):
        return self.stock

    def update_stock(self, quantity):
        self.stock = quantity
        self.history.append(self.stock)

    def display_information(self):
        print(
            f"Product ID: {self.product_id} | Name: {self.name} | Price: ${self.price:.2f} | Stock: {self.stock}"
        )

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "history": self.history,
        }


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def search_product(self, product_id):
        for product in self.products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self):
        print("\nCurrent Inventory\n")
        print("-" * 48)
        for product in self.products:
            product.display_information()
        print("-" * 48)

    def get_products(self):
        return self.products.copy()