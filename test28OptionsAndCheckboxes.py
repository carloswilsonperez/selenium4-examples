import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Selenium 4 - Chrome Driver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TestOptionsAndCheckboxes(unittest.TestCase):
    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://clouditeducation.com/pruebas/")

    def test1(self):
        print("radio")
        buton1 = driver.find_element_by_id("RadioGroup1_0")
        if buton1 is not None:
            buton1.click()

        time.sleep(5)

        buton2 = driver.find_element_by_id("RadioGroup1_1")
        if buton2 is not None:
            buton2.click()

        time.sleep(5)

    def test2(self):
        print("check")
        buton1 = driver.find_element_by_id("CheckboxGroup1_0")
        if buton1 is not None:
            buton1.click()

        time.sleep(5)

        buton2 = driver.find_element_by_id("CheckboxGroup1_1")
        if buton2 is not None:
            buton2.click()

        time.sleep(5)

    def tearDown(self):
        driver.quit()


if __name__ == '__main__':
    unittest.main()
