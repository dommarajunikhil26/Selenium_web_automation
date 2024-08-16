from base.baseClass import BaseClass
import utils.customLogger as cl
import random

class LoginPage(BaseClass):
    log = cl.customLogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    _verifyLoginPage = 'div[class="login_logo"]' # CSS Selector
    _enterUsername = "user-name" # id
    _enterPassword = "password" # id
    _clickLoginBtn = "login-button" # name
    _getUsernames = "//div[@id='login_credentials']" # xpath
    _getPassword = "//div[@class='login_password']" # xpath
    _verifyLoginSuccess = "title" # class name

    def verifyLoginPage(self):
        assert self.isElementDisplayed(self._verifyLoginPage, "css_selector")
    
    def enterUsername(self):
        username_element = self.getElement(self._getUsernames, "xpath")
        usernames = username_element.text.splitlines()[1:]  
        self.log.info("Usernames: %s", usernames)
        username = usernames[0]
        self.log.info("Selected username: %s", username)
        self.sendKeys(username, self._enterUsername, "id")

    def enterPassword(self):
        password_element = self.getElement("//div[@class='login_password']", "xpath")
        password = password_element.text.splitlines()[1]
        self.log.info("Entering the password: %s", password)
        self.sendKeys(password, self._enterPassword, "id")
    
    def clickLoginBtn(self):
        self.clickElement(self._clickLoginBtn, "name")
    
    def verifyLoginSuccess(self):
        assert self.isElementDisplayed(self._verifyLoginSuccess, "classname")
    