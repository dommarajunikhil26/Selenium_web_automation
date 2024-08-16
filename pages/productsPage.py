import random
from base.baseClass import BaseClass
from selenium.webdriver.common.by import By
import utils.customLogger as cl

class ProductsPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    _getProductsList = "inventory_item" # classname
    _shoppingCartLink = "shopping_cart_link" # classname
    _verifyCartPage = "title" # classname
    _getCartItems = "cart_item" # classname
    _clickCheckoutBtn = "checkout" # id
    _checkoutInfoTitle = "checkout_info_container" # id
    _enterFirstName = "first-name" # id
    _enterLastName = "last-name" # id
    _enterZip = "postal-code" # id
    _clickContinue = "continue" # name
    _clickFinish = "finish" # id
    _verifyOrderPlaced = "complete-header" # classname

    def addProductsToCart(self):
        product_items = self.getElements(self._getProductsList, "classname")
        products = {}
        number_of_products = random.randint(2, 6)
        for product in product_items:
            if number_of_products > 0:
                item_name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
                self.log.info(f"Located item_name: {item_name}")
                item_price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
                self.log.info(f"Located item_price: {item_price}")
                add_to_cart_btn = product.find_element(By.CSS_SELECTOR, ".btn.btn_primary.btn_small.btn_inventory")
                add_to_cart_btn.click()
                cl.allureLogs("Adding items to cart")
                products[item_name] = item_price # added this for future usage
            else:
                break
        return products

    def clickCartBtn(self):
        self.clickElement(self._shoppingCartLink, "classname")
        cl.allureLogs("Clicked on cart")
        
    
    def verifyCartPage(self):
        assert self.isElementDisplayed(self._verifyCartPage, "classname")
        cl.allureLogs("Cart page verified")
    
    def clickRemoveBtn(self):
        try:
            cart_items = self.getElements(self._getCartItems, "classname")
            remove_btn = cart_items[1].find_element(By.CSS_SELECTOR, ".btn.btn_secondary.btn_small.cart_button")
            remove_btn.click()
            cl.allureLogs("Clicked on remove item button")
        except Exception as e:
            self.log.error(f"The following error occured: {e}")
    
    def clickCheckoutBtn(self):
        self.clickElement(self._clickCheckoutBtn, "id")
        cl.allureLogs("Clicked on checkout button")
    
    def verifyCheckoutInfo(self):
        assert self.isElementDisplayed(self._checkoutInfoTitle, "id")
        cl.allureLogs("Verified checkout page")
    
    def enterFirstName(self):
        self.sendKeys("Test", self._enterFirstName, "id")
        cl.allureLogs("Entered first name")
    
    def enterLastName(self):
        self.sendKeys("Name", self._enterLastName, "id")
        cl.allureLogs("Entered Last name")
    
    def enterZip(self):
        self.sendKeys(52065, self._enterZip, "id")
        cl.allureLogs("Entered Postal Code")

    def clickContinue(self):
        self.clickElement(self._clickContinue, "name")
        cl.allureLogs("Clicked on continure button")

    def clickFinishBtn(self):
        self.clickElement(self._clickFinish, "id")
        cl.allureLogs("Clicked on Finish button")

    def verifyOrderPlaced(self):
        assert "Thank you for your order!" in self.getElement(self._verifyOrderPlaced, "classname").text
        cl.allureLogs("Verfied Order placed page")