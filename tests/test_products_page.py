import unittest
import pytest
from pages.productsPage import ProductsPage

@pytest.mark.usefixtures("setUpClass")
class TestProductsPage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def set_up_class_objects(self):
        self.pp = ProductsPage(self.driver)

    @pytest.mark.run(order=2)
    def test_add_products(self):
        self.pp.addProductsToCart()
    
    @pytest.mark.run(order=3)
    def test_click_cart(self):
        self.pp.clickCartBtn()
        self.pp.verifyCartPage()
    
    @pytest.mark.run(order=4)
    def test_remove_and_checkout_btn(self):
        self.pp.clickRemoveBtn()
        self.pp.clickCheckoutBtn()
        self.pp.verifyCheckoutInfo() 
    
    @pytest.mark.run(order=5)
    def test_enter_user_details(self):
        self.pp.enterFirstName()
        self.pp.enterLastName()
        self.pp.enterZip()
    
    @pytest.mark.run(order=6)
    def test_verify_order(self):
        self.pp.clickContinue()
        self.pp.clickFinishBtn()
        self.pp.verifyOrderPlaced()