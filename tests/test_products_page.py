import unittest
import pytest
from pages.productsPage import ProductsPage

@pytest.mark.usefixtures("setUpClass")
class TestLoginPage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def set_up_class_objects(self):
        self.pp = ProductsPage(self.driver)

    @pytest.mark.run(order=2)
    def test_add_products(self):
        self.pp.addProductsToCart()
    
    # def test_click_cart(self):