import unittest
from selenium import webdriver
from google_page import GooglePage


class GoogleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="./chomedriver")

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search("porno nalgonas")
        self.assertEqual("porno nalgonas", google.keyword)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
