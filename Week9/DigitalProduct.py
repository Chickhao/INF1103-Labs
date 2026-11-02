from Product import Product

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, file_size, history=None):
        super().__init__(product_id, name, price, stock, history)
        self.__file_size = file_size

    def display_information(self):
        super().display_information()
        print(f"File Size: {self.__file_size} MB")

    def get_fulfilment_info(self):
        return f"This product is delievered digitally."

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Digital"
        data["file_size"] = self.__file_size
        return data