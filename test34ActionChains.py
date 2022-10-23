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


class TestActionChains(unittest.TestCase):
    """
    Action chain example:

    ActionChains(driver).move_to_element(dropdown).click(dynamic_option).perform()
    """
    def setUp(self) -> None:
        global driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # driver.implicitly_wait(15)
        driver.get("http://clouditeducation.com/pruebas/")

    def test1(self):
        # First, find the button with the on hover menu
        botonMenu = driver.find_element(By.CLASS_NAME, "dropbtn")
        if botonMenu is not None:
            acciones = ActionChains(driver)

            # Second, hover over the element
            acciones.move_to_element(botonMenu).perform()
            # Next, the dynamic menu shows

            # Finally, move to Link 1 and click the menu option
            liga = driver.find_element(By.LINK_TEXT, "Link 1")
            acciones.move_to_element(liga).click().perform()
            time.sleep(3)

    def tearDown(self) -> None:
        driver.quit()


if __name__ == '__main__':
    unittest.main()
