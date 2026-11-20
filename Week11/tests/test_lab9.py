import io
import unittest
from unittest.mock import patch

from Supplier import Supplier
from Inventory import Inventory
from Order import Order
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from ProductFactory import ProductFactory
from DiscountStrategy import (
    BulkDiscount,
    PercentageDiscount,
    StudentDiscount,
)
from main import get_positive_float, load_products


CSV_TEXT = """product_type,product_id,name,price,stock_quantity
physical,P001,Desk Lamp,25.00,10
digital,D001,Photo Editor,49.90,100
service,S001,Installation,30.00,5
physical,P002,Office Chair,abc,3
physical,P003,Monitor Stand,39.50,7
"""


class Lab09Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.supplier = Supplier(
            "S001", "Test Supplier", "test@example.com"
        )

    def make_product(
        self,
        kind: str = "physical",
        price: float = 250.0,
        stock: int = 10
    ):
        return ProductFactory.create(
            kind,
            "PTEST",
            "Test Product",
            price,
            stock,
            self.supplier,
            weight=1.0,
            file_size=5.0,
        )

    def test_discount_switching(self) -> None:
        order = Order("O001")
        order.add_order_line(self.make_product(), 1)

        self.assertAlmostEqual(order.calculate_total(), 250.0)

        order.set_discount(BulkDiscount(200, 20))
        self.assertAlmostEqual(order.calculate_total(), 230.0)

        order.set_discount(PercentageDiscount(10))
        self.assertAlmostEqual(order.calculate_total(), 225.0)

        order.set_discount(StudentDiscount())
        self.assertAlmostEqual(order.calculate_total(), 237.5)

    def test_bulk_boundary(self) -> None:
        discount = BulkDiscount(200, 20)

        self.assertAlmostEqual(discount.apply(199), 199)
        self.assertAlmostEqual(discount.apply(200), 180)

    def test_factory_returns_types(self) -> None:
        self.assertIsInstance(
            self.make_product("physical"),
            PhysicalProduct,
        )
        self.assertIsInstance(
            self.make_product("digital"),
            DigitalProduct,
        )

    def test_unknown_type(self) -> None:
        with self.assertRaisesRegex(
            ValueError, "Unknown product type: service"
        ):
            self.make_product("service")

    def test_product_validation_and_stock_update(self) -> None:
        for kind in ("physical", "digital"):
            for price in (0, -10):
                with self.subTest(kind=kind, price=price):
                    with self.assertRaises(ValueError):
                        self.make_product(kind, price=price)

            with self.subTest(kind=kind, stock=-1):
                with self.assertRaises(ValueError):
                    self.make_product(kind, stock=-1)

            product = self.make_product(kind)
            previous_history = product.get_history()

            with self.assertRaises(ValueError):
                product.update_stock(-1)

            self.assertEqual(product.get_stock(), 10)
            self.assertEqual(
                product.get_history(), previous_history
            )

    def test_order_quantity(self) -> None:
        order = Order("O002")

        for quantity in (0, -1):
            with self.subTest(quantity=quantity):
                with self.assertRaises(ValueError):
                    order.add_order_line(
                        self.make_product(), quantity
                    )

        self.assertEqual(order.get_order_lines(), [])

    def test_input_retry(self) -> None:
        with patch(
            "builtins.input",
            side_effect=["abc", "-5", "12.50"],
        ):
            with patch(
                "sys.stdout", new_callable=io.StringIO
            ) as output:
                result = get_positive_float("Price: ")

        self.assertEqual(result, 12.5)
        self.assertEqual(
            output.getvalue().splitlines(),
            [
                "Please enter a valid number, e.g. 12.50",
                "Please enter a number greater than zero.",
            ],
        )

    def test_csv_skips_bad_rows(self) -> None:
        inventory = Inventory()

        with patch(
            "builtins.open",
            return_value=io.StringIO(CSV_TEXT),
        ):
            with patch(
                "sys.stdout", new_callable=io.StringIO
            ) as output:
                load_products(
                    "products.csv", inventory, self.supplier
                )

        self.assertEqual(
            [
                product.get_product_id()
                for product in inventory.get_products()
            ],
            ["P001", "D001", "P003"],
        )
        self.assertIn("Skipping row 4:", output.getvalue())
        self.assertIn("Skipping row 5:", output.getvalue())
        self.assertIn("3 products loaded.", output.getvalue())
        self.assertTrue(
            output.getvalue().endswith(
                "Load attempt finished.\n"
            )
        )

    def test_missing_csv(self) -> None:
        inventory = Inventory()

        with patch(
            "builtins.open",
            side_effect=FileNotFoundError,
        ):
            with patch(
                "sys.stdout", new_callable=io.StringIO
            ) as output:
                load_products(
                    "missing.csv", inventory, self.supplier
                )

        self.assertEqual(inventory.get_products(), [])
        self.assertEqual(
            output.getvalue().splitlines(),
            [
                "Products file not found: missing.csv",
                "Load attempt finished.",
            ],
        )


if __name__ == "__main__":
    unittest.main()