#!/usr/bin/env python

import argparse
import sys
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class EvilCorpSiteNavigationTest(unittest.TestCase):

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
        driver = self.driver
        driver.get("https://evil-corp.carrd.co")
        self.wait_for(seconds=2)
        # driver.find_element_by_id('text04').click()

        driver.find_element_by_css_selector("#buttons02 .n01").click()
        self.wait_for(seconds=3)
        driver.find_element_by_css_selector("#buttons03 .button").click()
        self.wait_for(seconds=3)
        driver.find_element_by_css_selector("li:nth-child(2) > .button").click()
        self.wait_for(seconds=3)
        driver.find_element_by_css_selector("#buttons05 .label").click()
        self.wait_for(seconds=3)
        driver.find_element_by_css_selector("li:nth-child(3) > .button").click()
        self.wait_for(seconds=3)
        driver.find_element_by_css_selector("#buttons01 svg").click()
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
