import unittest
from pyunitreport import HTMLTestRunner
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
        cls.driver.maximize_window()
    
    def test_search(self):
        mercado = MercadoPage(self.driver)
        mercado.open()
        mercado.select_country('MX')
        self.assertTrue(mercado.is_loaded)
       
        mercado.search('ropa de bebé')
        self.assertEqual('ropa de bebé', mercado.keyword)

        mercado.click_submit()
        self.assertEqual('ropa de bebé', mercado.word_searched)

        # mercado.close_coockiedisclaimer()

        mercado.see_all_locations()
        mercado.select_location_guerrero()

        mercado.select_condition_nuevo()

        self.driver.implicitly_wait(10)

        

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(20)
        cls.driver.quit()
        
if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output = 'reports', report_name = 'mercado_libre_report'))