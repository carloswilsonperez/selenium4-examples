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


class TestWithExplicitWaits(unittest.TestCase):
    """
    En una Espera Explícita, el WebDriver define
    un tiempo de espera para que ocurra una condición
    específica. Cuando la condición ocurre antes de que el
    tiepo especificado termine, WebDriver continúa con
    el código.

    Cuando la condición no ocurre en el tiempo
    predeterminado, se aroja una excepción.
    
    El método solo necesita llamarse una sola vez por sesión, 
    es decir, hasta que el WebDriver cierre.

    Condiciones que pueden validarse con una espera
    explícita:

    element_to_be_clickable -> Espera por un elemento y espera que sea visible y habilitado para darle click
    element_to_be_selected -> Espera a que el elemento se seleccione
    presence_of_element_located -> Espera hasta que el elemento esté disponible en el DOM
    title_contains -> Espera a que el título de la página contenga una cadena de caracteres
    visibility_of -> Localiza el elemento y espera que este sea visible y su tamaño sea mayor a cero
    text_to_be_present_in_element -> localiza el elemento y espera que contenga un texto
    alert_is_present -> espera que una alerta exista

    """
    def setUp(self) -> None:
        global driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("http://clouditeducation.com/pruebas/")

    def test1(self):
        # Esperar hasta 10 segundos para conseguir la condición deseada...
        espera = WebDriverWait(driver, 10)

        # Next, define the desired condition
        boton = espera.until(EC.element_to_be_clickable((By.ID, "proceed")))
        if boton is not None:
            boton.click()

        time.sleep(3)

    def tearDown(self) -> None:
        driver.quit()


if __name__ == '__main__':
    unittest.main()
