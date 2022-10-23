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


class ChangeFocusToIframe(unittest.TestCase):

    def setUp(self) -> None:
        global driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # driver.implicitly_wait(15)
        driver.get("http://clouditeducation.com/pruebas/")

    def test1(self):
        iFrameID = driver.find_element(By.ID, "pruebas-iframe")
        if iFrameID is not None:
            driver.switch_to.frame(iFrameID)  # Switch to IFrame

        # Next, locate element within IFrame
        nombre = driver.find_element(By.ID, "Segundo")

        # Finally, send text to element
        if nombre is not None:
            nombre.send_keys("Juan")

        time.sleep(3)

    def tearDown(self) -> None:
        driver.quit()


if __name__ == '__main__':
    unittest.main()
