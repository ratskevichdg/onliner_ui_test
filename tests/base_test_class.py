import unittest
from selenium import webdriver


class BaseTestClass(unittest.TestCase):
    DRIVER_LOCATION = "./chromedriver"
    BASE_URL = "https://www.onliner.by"

    def setUp(self):
        self.options = webdriver.ChromeOptions() 
        self.driver = webdriver.Chrome(
            executable_path=self.DRIVER_LOCATION,
            chrome_options=self.options
        )
        self.driver.implicitly_wait(3)
        self.driver.get(self.BASE_URL)

    def tearDown(self):
        self.driver.quit()