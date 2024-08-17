import shutil
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
            chrome_service_path = shutil.which('chromedriver')
            if chrome_service_path is None:
                raise ValueError("Chromedriver not found in PATH")
            chrome_service = Service(chrome_service_path)
            driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
            self.log.info("Initializing Chrome driver")
        elif platform == "safari":
            driver = webdriver.Safari()
            self.log.info("Initializing Safari driver")
        else:
            self.log.error(f"The webdriver for the platform {platform} does not exist")
            driver = None
        return driver