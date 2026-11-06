from Product import Product

class Inventory:
    def __init__(self) -> None:
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def search_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def remove_proiduct(self, product_id: str) -> None:
        product = self.search_product(product_id)
        
        if product is None:
            raise ValueError("Product Not Found.")
        self.__products.remove(product)
            

    def display_all(self) -> None:
        print("\nCurrent Inventory\n")
        print("-" * 48)
        for product in self.__products:
            product.display_information()
        print("-" * 48)

    def get_products(self) -> list[Product]:
        return self.__products.copy()
