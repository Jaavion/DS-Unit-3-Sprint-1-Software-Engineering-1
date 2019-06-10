import unittest
from acme import product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):

    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""

        prod = product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_stealability(self):
        prod = product('Test stealablility', 15, 27, .5)
        self.assertEqual(prod.stealability_(), 'not so stealable...')

        # test is suppose to fail

        prod2 = product('test very stealable', 1000, 2, .5)
        self.assertEqual(prod2.stealability_(), 'Kinda stealable.')

    def test_explode(self):

        # this test is suppose to fail

        prod = product('Test explode')
        self.assertEqual(prod.explode_(), '....BABOOM!')
        self.assertEqual(prod.explode_(), '...fizzle')


class AcmeReportTests(unittest.TestCase):

    def test_generate_report(self):
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        productList = generate_products()
        for product in productList:
            myWords = product.name.split()
            self.assertIn(myWords[1], NOUNS)
            self.assertIn(myWords[0], ADJECTIVES)


if __name__ == '__main__':
    unittest.main()