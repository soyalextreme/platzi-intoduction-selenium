import unittest
from selenium import webdriver

class SearchTest(unittest.TestCase):

    
    def setUp(self):
        self.driver = webdriver.Chrome("./chromedriver")
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        driver.maximize_window()
        driver.implicitly_wait(15)


    def test_search_cart(self):
        drivre = self.driver
        
        search_field = drivre.find_element_by_id("search_query_top")
        search_field.clear()
        search_field.send_keys('Faded Short Sleeve T-shirts')
        
        search_field.submit()


    def test_search_cart_salr(self):
        drivre = self.driver
       
        search_field = drivre.find_element_by_id("search_query_top")
        search_field.clear()
        search_field.send_keys('PRINTED CHIFFON')
        search_field.submit()

        products = drivre.find_elements_by_xpath('//*[@id="center_column"]/ul/li[1]/div/div[1]/div/a[1]/img')
        self.assertEqual(1, len(products))


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity = 2)