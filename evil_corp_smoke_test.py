#!/usr/bin/env python3

import argparse
import sys
import time
import unittest
from enum import Enum
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

"""
    A test that verifies that Evil Corp's user is able to navigate through
    the company website (https://evil-corp.carrd.co).

    Typical usage example:

    From command line, run `python evil_corp_smoke_test.py --platform Mac`
    Note that you need to pass in `--platform Windows` if you are on Windows.
"""
class Element(Enum):
    """
    Enum containing the elements on the pages of the site.
    """
    # Home page
    WHAT_WE_DO_BUTTON = "#buttons02 .n01"
    ABOUT_BUTTON = "li:nth-child(2) > .button"
    CONTACT_BUTTON = "li:nth-child(3) > .button"

    # What we do page
    WHAT_WE_DO_PAGE_BACK_BUTTON = "#buttons03 .button"

    # About page
    ABOUT_PAGE_BACK_BUTTON = "#buttons05 .label"

    # Contact page
    CONTACT_PAGE_BACK_BUTTON = "#buttons01 svg"

    def __str__(self):
        return str(self.value)

class EvilCorpSmokeTest(unittest.TestCase):
    """
    Class containing the tests.
    """
    
    def setUp(self):
        if run_on_ci:
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--headless")
            self.driver = webdriver.Chrome(options=chrome_options)

        if platform == "Mac" and not run_on_ci:
            self.driver = webdriver.Safari()
        elif platform == "Windows":
            self.driver = webdriver.Chrome("C:\chromedriver.exe")

    def tearDown(self):
        self.driver.close()
        
    def test_evil_corp_site_navigation(self):
        self.navigate_through_site()

    def test_user_is_taken_to_homepage_after_site_navigation(self):
        self.navigate_through_site()
        self.assertEquals(self.driver.current_url, "https://evil-corp.carrd.co/#", 
                            "Failed to verify user was on home page")

    def navigate_through_site(self):
        self.driver.get("https://evil-corp.carrd.co")
        self.wait_for(seconds=2)
        self.driver.find_element_by_css_selector(str(Element.WHAT_WE_DO_BUTTON)).click()
        self.wait_for(seconds=3)
        self.driver.find_element_by_css_selector(str(Element.WHAT_WE_DO_PAGE_BACK_BUTTON)).click()
        self.wait_for(seconds=3)
        self.driver.find_element_by_css_selector(str(Element.ABOUT_BUTTON)).click()
        self.wait_for(seconds=3)
        self.driver.find_element_by_css_selector(str(Element.ABOUT_PAGE_BACK_BUTTON)).click()
        self.wait_for(seconds=3)
        self.driver.find_element_by_css_selector(str(Element.CONTACT_BUTTON)).click()
        self.wait_for(seconds=3)
        self.driver.find_element_by_css_selector(str(Element.CONTACT_PAGE_BACK_BUTTON)).click()
        self.wait_for(seconds=3)

    def wait_for(self, seconds=0):
        time.sleep(seconds)

if __name__ == "__main__":
    global run_on_ci
    global platform

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--run-on-ci', action='store_true')
    parser.add_argument('--platform', choices=['Windows', 'Mac'], default='Mac')
    options, args = parser.parse_known_args()

    run_on_ci = options.run_on_ci
    platform = options.platform
    unittest.main(argv=sys.argv[:1] + args)
