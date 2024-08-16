from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import utils.customLogger as cl



class Driver:
    log = cl.customLogger()

    def get_driver(self, platform):
        platform = platform.lower()
        if platform == "chrome":
            chrome_options = Options()
            chrome_options.add_argument('--start-maximized')
            chrome_service = Service('/opt/homebrew/bin/chromedriver')
            driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
            self.log.info("Initializing Chrome driver")
        elif platform == "safari":
            driver = webdriver.Safari()
            self.log.info("Initializing Safari driver")
        else:
            self.log.error(f"The webdriver for the platform {platform} does not exist")
            driver = None
        return driver