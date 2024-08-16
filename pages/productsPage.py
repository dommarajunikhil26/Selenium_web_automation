import time
from base.baseClass import BaseClass
from selenium.webdriver.common.by import By

class ProductsPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    _getProductsList = "inventory_list" # classname

    def getProducts(self):
        product_items = self.getElements("inventory_item", "classname")
        products = {}
        for product in product_items:
            item_name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            item_price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
            products[item_name] = item_price
        self.log.info("Products:")
        for product, price in products.items():
            self.log.info(f"{product}: {price}")
        return products
