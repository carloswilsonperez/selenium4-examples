import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Paso 1 asegurate estos dos directorios (pruebas y paginas) estan en el path de tu computadora
from PageObjects.paginas.login_pagina import LoginPage
from PageObjects.paginas.pagina2 import Page2
import time

# Selenium 4 - Chrome Driver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class ClickSendKeys(unittest.TestCase):

   def setUp(self):
        global driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("http://clouditeducation.com/pruebas/loginTest.html")

   def testId(self):

        # Paso 2 solo creas una pagina LoginPage y llamas al metodo login.
        # todas tus pruebas
        paginaLogin = LoginPage(driver)
        paginaLogin.login("Gabriel", "Secreta")
        time.sleep(5)

        pagina2 = Page2(driver)
        pagina2.meterNombre("Juan")

        # no necesario, solo para que aprecies tu trabajo.      
        time.sleep(2)

   def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    unittest.main()
