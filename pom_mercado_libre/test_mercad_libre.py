import unittest
from selenium import webdriver
from time import sleep


class MercadoLibre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../../chromedriver")
        driver = self.driver
        driver.get("https://www.mercadolibre.com/")
        driver.maximize_window()

    def test_challenge_mercado_libre(self):
        driver = self.driver
        country = driver.find_element_by_id("CO")
        country.click()
        search_bar = driver.find_element_by_name("as_word")
        search_bar.click()
        search_bar.clear()
        search_bar.send_keys("Playstation 4")
        search_bar.submit()
        sleep(3)
        location = driver.find_element_by_xpath(
            '//*[@id="root-app"]/div/div/aside/section[2]/dl[8]/dd[1]/a/span[1]')

        location.click()
        sleep(3)

        condition = driver.find_element_by_xpath(
            '//*[@id="root-app"]/div/div/aside/section[3]/dl[6]/dd[1]/a/span[1]')
        condition.click()
        sleep(3)

        filter_menu = driver.find_element_by_class_name(
            "andes-dropdown__trigger")
        filter_menu.click()

        higher_price = driver.find_element_by_xpath(
            '//*[@id="root-app"]/div/div/aside/section[2]/div[2]/div[1]/div/div/div/ul/li[3]/div/div/a')

        higher_price.click()
        sleep(3)

        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element_by_xpath(
                f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
            articles.append(article_name)
            article_price = driver.find_element_by_xpath(
                f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div/div/span[1]/span[2]').text
            prices.append(article_price)
        print(articles)
        print(prices)

    def tearDown():
        self.driver.close()
