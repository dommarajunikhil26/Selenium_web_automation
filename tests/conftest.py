import pytest
from base.baseClass import BaseClass
from base.driverClass import Driver
from pages.loginPage import LoginPage
from pages.productsPage import ProductsPage

@pytest.fixture(scope='class')
def setUpClass(request):
    print("Before Class")
    driver_instance = Driver()
    driver = driver_instance.get_driver("chrome")
    bp = BaseClass(driver)
    bp.launchWebPage('https://www.saucedemo.com/')
    lp = LoginPage(driver)
    lp.enterUsername()
    lp.enterPassword()
    lp.clickLoginBtn()
    pp = ProductsPage(driver)
    if request.cls is not None:
        request.cls.driver = driver
        request.cls.lp = lp
        request.cls.pp = pp
    yield driver
    lp.logout()
    driver.quit()
    print("After Class")

