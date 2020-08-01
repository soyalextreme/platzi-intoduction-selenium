import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

class NabigationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver")
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get("https://google.com/")

    def test_browser_navigation(self):
        driver = self.driver
        search_bar = driver.find_element_by_name("q")
        search_bar.clear()
        search_bar.send_keys('platzi')
        search_bar.submit()
        # slee lo usa en segundos
        sleep(3)
        driver.back()
        sleep(3)
        driver.forward()
        sleep(3)





    def tearDown(self):
        self.driver.quit()


    
if __name__ == "__main__":
    unittest.main(verbosity=2)