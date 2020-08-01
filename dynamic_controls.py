import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DynamicControls(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver")
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text("Dynamic Controls").click()
        driver.maximize_window()

    def test_dynamic_elements(self):
        driver = self.driver
        check_box = driver.find_element_by_xpath('//*[@id="checkbox"]/input')
        check_box.click()
        sleep(5)
        button_remove = driver.find_element_by_xpath(
            '//*[@id="checkbox-example"]/button').click()
        sleep(6)
        button_add = driver.find_element_by_xpath(
            '//*[@id="checkbox-example"]/button').click()
        sleep(6)

    def test_dynamic_elemnts_solution(self):
        driver = self.driver
        check_box = driver.find_element_by_xpath('//*[@id="checkbox"]/input')
        check_box.click()
        button_add_remove = driver.find_element_by_xpath(
            '//*[@id="checkbox-example"]/button')
        button_add_remove.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="checkbox-example"]/button')))
        button_add_remove.click()

        enable_disable_button = driver.find_element_by_css_selector(
            "#input-example > button")
        enable_disable_button.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#input-example > button")))

        input_text = driver.find_element_by_css_selector(
            "#input-example > input[type=text]")
        input_text.send_keys("Platzi")

        enable_disable_button.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
