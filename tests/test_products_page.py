import unittest
import pytest
from pages.loginPage import LoginPage
from pages.productsPage import ProductsPage

@pytest.mark.usefixtures("setUpClass")
class TestLoginPage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def set_up_class_objects(self):
        self.pp = ProductsPage(self.driver)
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_get_products(self):
        self.lp.enterUsername()
        self.lp.enterPassword()
        self.lp.clickLoginBtn()
        self.pp.getProducts()