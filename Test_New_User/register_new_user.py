import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver")
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get("http://automationpractice.com/index.php")


    def test_new_user(self):
        driver = self.driver
        create_acount_button = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        self.assertTrue(create_acount_button.is_displayed() and create_acount_button.is_enabled())
        create_acount_button.click()
        self.assertEqual("Login - My Store", self.driver.title)
        input_email = driver.find_element_by_id("email_create")
        input_email.clear()
        input_email.send_keys("alex.anso.17@gmail.com")
        input_email.submit()

        #radio
        title = driver.find_element_by_id("id_gender1").click()
        news_letter_subscribe = driver.find_element_by_id("newsletter").click()
        
        # input texts
        first_name_custumer = driver.find_element_by_id("customer_firstname").send_keys("Alejandro")
        last_name_custumer = driver.find_element_by_id("customer_firstname").send_keys("Soriano")
        email = driver.find_element_by_name("email").send_keys("alexito@gmail.com")
        password = driver.find_element_by_name("passwd").send_keys("Test_Password")

        #listas    
        day = driver.find_element_by_name("days")
        months = driver.find_element_by_name("months")
        years = driver.find_element_by_name("years")
        #input text
        first_name = driver.find_element_by_id("firstname").send_keys("David")
        last_name = driver.find_element_by_id("lastname").send_keys("Aroesti")
        company = driver.find_element_by_id("company").send_keys("Google")
        address = driver.find_element_by_id("address1").send_keys("Direccion Prueba")
        address_line_two = driver.find_element_by_id("address2").send_keys("Al lado de google")
        city = driver.find_element_by_id("city").send_keys("Mexiiiico")
        #listas
        state = Select(driver.find_element_by_id('id_state')).select_by_value("2")
        country = Select(driver.find_element_by_id("id_country"))
        # input text
        cp = driver.find_element_by_name("postcode").send_keys("50213")
        additional_info = driver.find_element_by_id("other").send_keys("Un negocio importante con selenium")
        home_phone = driver.find_element_by_name("phone").send_keys("777342743")
        mobile_phone = driver.find_element_by_name("phone_mobile").send_keys("1293123213")
        adress_alias = driver.find_element_by_name('alias').send_keys("No se que poner")


        # faltan validacion de activo las listas
        self.assertTrue(
            first_name_custumer.is_enabled()
            and last_name_custumer.is_enabled()
            and email.is_enabled()
            and password.is_enabled()
            and first_name.is_enabled()
            and last_name.is_enabled()
            and company.is_enabled()
            and address.is_enabled()
            and address_line_two.is_enabled()
            and city.is_enabled()
            and cp.is_enabled()
            and additional_info.is_enabled()
            and home_phone.is_enabled()
            and mobile_phone.is_enabled()
            and adress_alias.is_enabled()
            )

        exp_options = ["United States",""]
        act_options = []
        select_country = Select(country)
        self.assertEqual(2, len(select_country.options))

        for option in select_country.options:
            act_options.append(option.text)

        # self.assertListEqual(exp_options, act_options)

        self.assertEqual("United States" , select_country.first_selected_option.text)        

        select_country.select_by_index(1)
        select_day = Select(day).select_by_index(28)
        select_month = Select(months).select_by_index(5)
        select_year = Select(years).select_by_value("1998")
        driver.implicitly_wait(100)

    def tearDown(self):
        self.driver.quit()


    
if __name__ == "__main__":
    unittest.main(verbosity=2)