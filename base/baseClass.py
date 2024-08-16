import utils.customLogger as cl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException
import allure
from allure_commons.types import AttachmentType 

class BaseClass:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver
    
    def launchWebPage(self, url):
        try:
            self.driver.get(url)
            self.log.info(f"Opened the web page with url: {url}")
        except Exception as e:
            self.log.error(f"Could not open the web page with {url}")
            self.log.error(f"The following exception occurred: {e}")
    
    def getLocatorType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "tag":
            return By.TAG_NAME
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "link_text":
            return By.LINK_TEXT
        elif locatorType == "partial_link_text":
            return By.PARTIAL_LINK_TEXT
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css_selector":
            return By.CSS_SELECTOR
        else:
            self.log.error(f"Locator Type: {locatorType} does not exist")
            self.takeScreenShot(locatorType)
            return None
    
    def waitForElement(self, locatorValue, locatorType="id"):
        locatorByType = self.getLocatorType(locatorType)
        wait = WebDriverWait(self.driver, 20, 1, ignored_exceptions=[NoSuchElementException, ElementNotSelectableException])
        element = None
        if locatorByType is None:
            self.log.error(f"Locator Type: {locatorType} does not exist")
        else:
            element = wait.until(EC.presence_of_element_located((locatorByType, locatorValue)))
            self.takeScreenShot(locatorType)
        return element

    def clickElement(self, locatorValue, locatorType="id"):
        try:
            element = self.waitForElement(locatorValue, locatorType)
            element.click()
            self.log.info(f"Clicked on element with LocatorType: {locatorType} and LocatorValue: {locatorValue}")
        except Exception as e:
            self.log.error(f"Not able to click on element with LocatorType: {locatorType} and LocatorValue: {locatorValue}")
            self.log.error(f"The following exception occurred: {e}")
            self.takeScreenShot(locatorType)
    
    def sendKeys(self, text, locatorValue, locatorType="id"):
        try:
            element = self.waitForElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info(f"Sent text: {text} to element with LocatorType: {locatorType} and LocatorValue: {locatorValue}")
        except Exception as e:
            self.log.error(f"Not able to send text: {text} to element with LocatorType: {locatorType} and LocatorValue: {locatorValue}")
            self.log.error(f"The following exception occurred: {e}")
    
    def isElementDisplayed(self, locatorValue, locatorType="id"):
        flag = False
        try:
            element = self.waitForElement(locatorValue, locatorType)
            flag = element.is_displayed()
            self.log.info(f"Displayed element with LocatorType: {locatorType} and LocatorValue: {locatorValue}")
        except Exception as e:
            self.log.error(f"Not able to display element with LocatorType: {locatorType} and LocatorValue: {locatorValue}")
            self.log.error(f"The following exception occurred: {e}")
            self.takeScreenShot(locatorType)
        return flag

    def getElements(self, locatorValue, locatorType="id"):
        locatorByType = self.getLocatorType(locatorType)
        wait = WebDriverWait(self.driver, 15, 1, ignored_exceptions=[NoSuchElementException, ElementNotSelectableException])
        elements = None
        if locatorByType is None:
            self.log.error(f"Locator Type: {locatorType} does not exist")
        else:
            elements = wait.until(EC.presence_of_all_elements_located((locatorByType, locatorValue)))
            self.log.info(f"Got element with LocatorType: {locatorType} and LocatorValue: {locatorValue}")
            self.takeScreenShot(locatorType)
        return elements

    def getElement(self, locatorValue, locatorType="id"):
        locatorByType = self.getLocatorType(locatorType)
        wait = WebDriverWait(self.driver, 15, 1, ignored_exceptions=[NoSuchElementException, ElementNotSelectableException])
        element = None
        if locatorByType is None:
            self.log.error(f"Locator Type: {locatorType} does not exist")
        else:
            element = wait.until(EC.presence_of_element_located((locatorByType, locatorValue)))
            self.log.info(f"Got element with LocatorType: {locatorType} and LocatorValue: {locatorValue}")
            self.takeScreenShot(locatorType)
        return element
    
    def takeScreenShot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)