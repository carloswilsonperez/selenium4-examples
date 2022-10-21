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


class TestSendKeys(unittest.TestCase):
    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://clouditeducation.com/pruebas/")

    def testActions(self):
        # This shows how to click on a link element
        liga = driver.find_element(By.XPATH, "//a[contains(text(), 'Pagina 2')]")
        if liga is not None:
            liga.click()

        # This shows how to enter a value in an input element
        nombre = driver.find_element(By.XPATH, "//input[@id='Segundo']")
        if nombre is not None:
            nombre.send_keys("Juan")
        time.sleep(5)

    def tearDown(self):
        driver.quit()


if __name__ == '__main__':
    unittest.main()
