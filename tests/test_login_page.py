import unittest
import pytest
from pages.loginPage import LoginPage
from pages.productsPage import ProductsPage

@pytest.mark.usefixtures("setUpClass")
class TestLoginPage(unittest.TestCase):
    
    @pytest.fixture(autouse=True)
    def set_up_class_objects(self, setUpClass):
        self.pp = ProductsPage(self.driver)
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=1)
    def test_login(self):
        self.lp.verifyLoginSuccess()