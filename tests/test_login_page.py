import unittest
import pytest

from pages.loginPage import LoginPage

@pytest.mark.usefixtures("setUpClass", "setUpMethod")
class TestLoginPage(unittest.TestCase):
    
    @pytest.fixture(autouse=True)
    def set_up_class_objects(self):
        self.lp = LoginPage(self.driver)
    
    @pytest.mark.run(order=1)
    def test_verify_login_page_open(self):
        self.lp.verifyLoginPage()
    
    @pytest.mark.run(order=2)
    def test_enter_login_credentials(self):
        self.lp.enterUsername()
        self.lp.enterPassword()
    
    @pytest.mark.run(order=3)
    def test_click_login_btn(self):
        self.lp.clickLoginBtn()
        self.lp.verifyLoginSuccess()