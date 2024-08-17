import unittest
import pytest
from pages.loginPage import LoginPage

@pytest.mark.usefixtures("setUpClass")
class TestLoginPage(unittest.TestCase):
    
    @pytest.fixture(autouse=True)
    def set_up_class_objects(self):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=1)
    def test_login(self):
        self.lp.verifyLoginSuccess()