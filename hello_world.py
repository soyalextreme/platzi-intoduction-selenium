import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class HelloWorld(unittest.TestCase):

    @classmethod
    # prepara el entorno de la prueba misma
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="./chromedriver")
        driver = cls.driver
        driver.get("https://www.platzi.com")

    # caso de prueba

    @classmethod
    def test_hello_world(cls):
        driver = cls.driver
        driver.implicity_wait(10)

    def test_visit_wikipedia(cls):
        cls.driver.get("https://wikipedia.com")

    @classmethod
    # acciones al terminar la prua
    def tearDown(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output="reportes", report_name="hello-world-report"))
