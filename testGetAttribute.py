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

# driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

# Firefox
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager

# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# IE
# from selenium.webdriver.ie.service import Service as IEService
# from webdriver_manager.microsoft import IEDriverManager

# driver = webdriver.Ie(service=IEService(IEDriverManager().install()))

# Edge
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager

# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


class GoogleTestCases(unittest.TestCase):
    def setUp(self) -> None:
        global driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # driver.implicitly_wait(15)
        driver.get("http://clouditeducation.com/pruebas/")

    def test_a_dropdown(self):
        '''Print element class'''
        # deselect_all()
        # deselect_by_index(index)
        # deselect_by_value(value)
        # deselect_by_visible_text(text)
        # select_by_index(index)
        # select_by_value(value)
        # select_by_visible_text(text)
        driver.get("http://clouditeducation.com/pruebas/")
        ingredientes = driver.find_element(By.NAME, "ingrediente")
        content = driver.find_element(By.CLASS_NAME, "content")
        if ingredientes is not None:
            ingredienteSel = Select(ingredientes)
            ingredienteSel.select_by_value("cebolla")
            print(ingredientes.get_attribute("name"))
            time.sleep(1)
        if content is not None:
            print("Class : ", content.get_attribute("class"))

    def test_obtener_atributo_o_texto(self):
        driver.get("http://clouditeducation.com/pruebas/")
        webElement1 = driver.find_element(By.XPATH, "//tr[@id='noImportante']/td[2]")
        if webElement1 is not None:
            print("Texto: " + webElement1.text)  # Obteniendo el texto

        webElement2 = driver.find_element(By.ID, "importante")
        if webElement2 is not None:
            print("Nombre de la clase: " + webElement2.get_attribute("class"))
        time.sleep(5)

    def testActionChains(self):
        driver.get("http://clouditeducation.com/pruebas/")
        botonMenu = driver.find_element(By.CLASS_NAME, "dropbtn")
        if botonMenu is not None:
            acciones = ActionChains(driver)
            acciones.move_to_element(botonMenu).perform()
            # The menu shows
            liga = driver.find_element(By.LINK_TEXT, "Link 1")
            acciones.move_to_element(liga)
            acciones.click()
            acciones.perform()
            time.sleep(3)

    def testExplicitWait(self):
        espera = WebDriverWait(driver, 10)  # Espera explícita, 10 segundos para conseguir la condición deseada
        driver.get("http://clouditeducation.com/pruebas/")
        window_title = driver.title
        print(window_title)
        boton = espera.until(EC.element_to_be_clickable((By.ID, "proceed")))
        if boton is not None:
            boton.click()

        time.sleep(3)

    def tearDown(self) -> None:
        driver.quit()


if __name__ == '__main__':
    unittest.main()
