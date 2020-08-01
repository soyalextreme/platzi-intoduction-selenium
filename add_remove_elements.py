import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver")
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text("Add/Remove Elements").click()


    def test_add_remove(self):
        driver = self.driver
        elements_added = int(input("How many elements will you add:  "))
        elements_remove = int(input("How many elements will you remove:  "))
        total_elements = elements_added - elements_remove


        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')

        sleep(3)

        for i in range(elements_added):
            add_button.click();

        for i in range(elements_remove):
            try:
                delete_button = driver.find_element_by_xpath('//*[@id="elements"]/button')
                delete_button.click()
            except:
                print("Youre trying to delete mor elements than existing")
                break

        if total_elements > 0:
            print(f"There are {total_elements} elements in the scree")
        else:
            print("They are no elements in the page")
        sleep(3)

    def tearDown(self):
        self.driver.quit()


    
if __name__ == "__main__":
    unittest.main(verbosity=2)