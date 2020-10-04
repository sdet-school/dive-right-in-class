import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class GoogleSearchMacTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Safari()

        # If you are on Windows, delete the line above and uncomment the one below :)
        # self.driver = webdriver.Chrome("C:\chromedriver.exe")
        
    def test_search_returns_expected_result(self):
        driver = self.driver
        driver.get("http://www.google.com")

        search_text_field = driver.find_element_by_name("q")
        search_text_field.send_keys("Let me google that for you")

        self.wait_for(seconds=3)

        search_text_field.send_keys(Keys.RETURN)

        self.wait_for(seconds=3)

        expected_result = "LMGTFY - Search Made Easy"

        assert expected_result in driver.page_source

    def wait_for(self, seconds=0):
        time.sleep(seconds)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
