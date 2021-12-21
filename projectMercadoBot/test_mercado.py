import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mercado_page import MercadoPage

class MercadoTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service = Service('../chromedriver.exe'))
    
    def test_search(self):
        mercado = MercadoPage(self.driver)
        mercado.open()
        mercado.select_country('MX')
        mercado.search('ropa de bebé')

        self.assertEqual('ropa de bebé', mercado.keyword)

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(20)
        cls.driver.quit()
        
if __name__ == '__main__':
    unittest.main(verbosity=2)