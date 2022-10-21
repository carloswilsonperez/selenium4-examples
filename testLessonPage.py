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

"""Para cambiarse a una página, Selenium webdriver ofrece
las siguientes propiedades:

current_url -> url de la página
current_window_handle -> Referencia manejada por el sistema para cada ventana
name -> nombre del navegador
orientation -> orientación del dispositivo
page_source -> código de la página
title -> título de la página
window_handles -> Los handles de todas las ventanas en la sesión actual

Para cambiarnos a una página, alert o frame, tenemos los siguiente métodos:

switch_to.window()
switch_to.alert()
switch_to.frame()


EJEMPLO:
"""



class ChangePageTestCases(unittest.TestCase):
    def setUp(self) -> None:
        global driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # driver.implicitly_wait(15)

    def testSendInputToAnotherWindows(self):
        driver.get("http://clouditeducation.com/pruebas/")

        # encuentra la ventana actual
        parent_handle = driver.current_window_handle
        print("Handle principal: ", parent_handle)

        # encuentra el button submit y dale clic
        driver.find_element(By.ID, "Buton1").click()
        time.sleep(3)

        # todos los handles
        todos_handles = driver.window_handles
        print("Todos los handles", todos_handles)

        for handle in todos_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)

        elemento = driver.find_element(By.ID, "Segundo")
        if elemento is not None:
            elemento.send_keys("Juan")
        time.sleep(3)

    def testChangeFocusToAlert(self):
        driver.get("http://clouditeducation.com/pruebas/")

        elemento = driver.find_element(By.XPATH, "//div[@id='center']/button")
        if elemento is not None:
            elemento.click()
        alerta = driver.switch_to.alert
        time.sleep(3)
        alerta.accept()
        time.sleep(5)

    def tearDown(self) -> None:
        driver.quit()

if __name__ == '__main__':
    unittest.main()
