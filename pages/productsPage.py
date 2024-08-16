import random
from base.baseClass import BaseClass
from selenium.webdriver.common.by import By

class ProductsPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    _getProductsList = "inventory_list" # classname

    def addProductsToCart(self):
        product_items = self.getElements("inventory_item", "classname")
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
                self.log.info(f"Clicked on add to cart button")
                products[item_name] = item_price
            else:
                break
        return products

        
        


