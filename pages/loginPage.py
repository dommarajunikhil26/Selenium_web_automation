from base.baseClass import BaseClass
import utils.customLogger as cl
import random

class LoginPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    _verifyLoginPage = 'div[class="login_logo"]' # CSS Selector
    _enterUsername = "user-name" # id
    _enterPassword = "password" # id
    _clickLoginBtn = "login-button" # name
    _getUsernames = "//div[@id='login_credentials']" # xpath
    _getPassword = "//div[@class='login_password']" # xpath
    _verifyLoginSuccess = "title" # classname
    _clickSideBar = "react-burger-menu-btn" # id
    _clickLogoutbtn = "Logout" # Link Text

    def verifyLoginPage(self):
        assert self.isElementDisplayed(self._verifyLoginPage, "css_selector")
    
    def enterUsername(self):
        username_element = self.getElement(self._getUsernames, "xpath")
        usernames = username_element.text.splitlines()[1:]  
        username = usernames[0]
        self.sendKeys(username, self._enterUsername, "id")
        cl.allureLogs(f"Entered username: {username}")

    def enterPassword(self):
        password_element = self.getElement("//div[@class='login_password']", "xpath")
        password = password_element.text.splitlines()[1]
        self.sendKeys(password, self._enterPassword, "id")
        cl.allureLogs(f"Entered password: {password}")
    
    def clickLoginBtn(self):
        self.clickElement(self._clickLoginBtn, "name")
        cl.allureLogs("Clicked on Login Button")

    def verifyLoginSuccess(self):
        assert self.isElementDisplayed(self._verifyLoginSuccess, "classname")
        cl.allureLogs("Verified User Login")
    
    def logout(self):
        self.clickElement(self._clickSideBar, "id")
        self.clickElement(self._clickLogoutbtn, "link_text")