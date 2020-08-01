import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class AlertTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver")
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get("http://127.0.0.1:5500/scripts/text.html")

    def test_alert(self):
        driver = self.driver
        button = driver.find_element_by_name("button-alert")
        button.click()
        alert  = driver.switch_to_alert()
        alert_text = alert.text

        #verificar si el texto es el que queremos
        self.assertEqual("Una alerta uwu", alert_text)
        driver.implicitly_wait(2000)
        alert.accept()


    def tearDown(self):
        self.driver.quit()


    
if __name__ == "__main__":
    unittest.main(verbosity=2)