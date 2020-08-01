import unittest
from selenium import webdriver
# excepcion para los asertions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class AssertionTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./chromedriver")
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, "controller"))


    def test_search_field_id(self):
        self.assertTrue(self.is_element_present(By.ID, "searchbox"))

    def tearDown(self):
        self.driver.quit()


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what )
        except NoSuchElementException as variable:
            return False
        return True

if __name__ == "__main__":
    unittest.main(verbosity = 2)