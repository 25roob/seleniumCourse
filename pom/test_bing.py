import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bing_page import BingPage

class BingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service = Service('../chromedriver.exe'))

    def test_search(self):
        bing = BingPage(self.driver)
        bing.open()
        bing.search('gatitos')

        self.assertEqual('gatitos', bing.keyword)

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(20)
        cls.driver.quit()
        

if __name__ == '__main__':
    unittest.main(verbosity=2)