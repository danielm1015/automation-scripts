#!/usr/bin/env python
'''
    File name: sel.py
    Author: Daniel Martinez
    Date created: 8/14/20193
    Date last modified: 8/16/2019
    Python 3.6.8, Selenium 3.141.0
'''
import json
import time
import unittest
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, InvalidSessionIdException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


with open('config.json') as json_data_file:
    config_data = json.load(json_data_file)

class SelloWorld(unittest.TestCase):

    def test_hellopage(self):
        driver = HelloPage().driver

        # Test Hello world Tag exists
        # h1 = driver.find_element_by_tag_name('h1')
        # print("h1, driver has: " ,h1.text)
        self.assertEqual("Hello World!", driver.find_element_by_tag_name('h1').text, "Not Hello World!")

    def test_hellobutton(self):
        driver = HelloPage().driver
        
        # selecting button tag
        button = driver.find_element_by_xpath("/html/body/div/button")
        button.click()
        # check if button date matches current date
        self.assertEqual(str(datetime.now().strftime("%m/%d/%Y")).strip("0"), driver.find_element_by_id('datetime').text, "Incorrect datetime!")
        driver.close()

        
class HelloPage(object):

        def __init__(self):
            self.driver = webdriver.Chrome(config_data["environment"]["lin_selenium_driver_path"])
            self.est_con = self.driver.get(config_data["environment"]["helloworld_url"])
            try:
                element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Hello World!')]")))
            except TimeoutException:
               print("Timeout, Hello World! not found!")
            finally:
               print("Connection is good")
                

if __name__ == '__main__':
    unittest.main()
