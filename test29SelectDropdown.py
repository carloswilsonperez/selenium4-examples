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


class TestDropdown(unittest.TestCase):
    # deselect_all()
    # deselect_by_index(index)
    # deselect_by_value(value)
    # deselect_by_visible_text(text)
    # select_by_index(index)
    # select_by_value(value)
    # select_by_visible_text(text)

    def setUp(self) -> None:
        global driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("http://clouditeducation.com/pruebas/")

    def test1(self):
        ingredients = driver.find_element_by_name("ingrediente")
        if ingredients is not None:
            ingredienteSel = Select(ingredients)
            ingredienteSel.select_by_value("cebolla")
        time.sleep(5)

    def test2(self):
        frutas = driver.find_element_by_name("Select1")
        if frutas is not None:
            frutasSel = Select(frutas)
            frutasSel.select_by_index(1)
            frutasSel.select_by_visible_text("Sandia")
        time.sleep(5)

    def tearDown(self) -> None:
        driver.quit()


if __name__ == '__main__':
    unittest.main()
