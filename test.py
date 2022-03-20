import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import cashier


class ContainersTestCase(unittest.TestCase):
    def setUp(self):
        self.response = io.StringIO()

    def test_add_two_items(self):
        items = [
            {"name": "kale", "price": 10, "quantity": 4},
            {"name": "apple", "price": 3, "quantity": 4},
        ]
        total = 0
        user_input = []
        for item in items:
            user_input.append(item["name"])
            user_input.append(item["price"])
            user_input.append(item["quantity"])
            total += item["price"] * item["quantity"]
        user_input.append("done")

        with redirect_stdout(self.response):
            with patch("builtins.input", side_effect=user_input):
                cashier.main()
                total = 0
                for item in items:
                    self.assertTrue(item["name"] in self.response.getvalue())
                    self.assertTrue(
                        str(item["price"] * item["quantity"])
                        in self.response.getvalue()
                    )

                self.assertTrue(str(total) in self.response.getvalue())

    def test_add_one_item(self):
        user_input = ["haha", 2, 5, "done"]
        with redirect_stdout(self.response):
            with patch("builtins.input", side_effect=user_input):
                cashier.main()
                self.assertTrue("haha" in self.response.getvalue())
                self.assertTrue("10" in self.response.getvalue())


if __name__ == "__main__":
    unittest.main()
