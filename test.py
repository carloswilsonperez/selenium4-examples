import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Chromium
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

# driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

# Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# IE
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.microsoft import IEDriverManager

# driver = webdriver.Ie(service=IEService(IEDriverManager().install()))

# Edge
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
class findByIdName(unittest.TestCase):
    def setUp(self) -> None:
        global driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def testCloudItEducation(self):
        driver.get("http://www.clouditeducation.com/pruebas/")
        element = driver.find_element(By.CLASS_NAME, "content")
        if element is not None:
            print("El elemento fue encontrado")

    def testPythonSite(self):
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element(By.NAME, "q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self) -> None:
        driver.close()


if __name__ == '__main__':
    unittest.main()
