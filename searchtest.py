import unittest
from selenium import webdriver

class HomePageTest(unittest.TestCase):

    
    def setUp(self):
        self.driver = webdriver.Chrome("./chromedriver")
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        driver.maximize_window()
        driver.implicitly_wait(15)

    
    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_elements_by_class_name("row")

    # def test_search_text_by_name(self):
    #     search_text_by_name = self.driver.find_element_by_name()

    def test_search_text_by_id(self):
        search_text = self.driver.find_element_by_id("contact-link")


    def test_search_button_enable(self):
        button = self.driver.find_element_by_name("submit_search")


    def test_count_of_span_in_home_page(self):
        items = self.driver.find_element_by_class_name("ajax_cart_product_txt unvisible")
        spans = self.driver.find_element_by_tag_name("span")
        self.assertEqual(4, len(spans))

    def test_header(self):
        header = self.driver.find_element_by_xpath('//*[@id="header"]')

    def test_css_selector(self):
        cart = self.driver.find_elements_by_css_selector("div.shopping_cart a")


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2)