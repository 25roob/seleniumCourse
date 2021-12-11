import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service

class LanguageOptions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service = Service('./chromedriver.exe')) # Acces the driver
        driver = self.driver # Shortener
        driver.maximize_window() 
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.implicitly_wait(30) # Wait 30 seconds to observe

    def test_select_language(self):
        exp_options = ['English', 'French', 'German']
        act_options = []
        
        select_language = Select(self.driver.find_element(By.ID, 'select-language'))

        self.assertEqual(3, len(select_language.options)) # Assert that there are just 3 lang options
        for option in select_language.options: 
            act_options.append(option.text) # Put all the options ina list

        self.assertListEqual(exp_options, act_options) 

        self.assertEqual('English', select_language.first_selected_option.text)

        select_language.select_by_visible_text('German')

        self.assertTrue('store=german' in self.driver.current_url)

        select_language = Select(self.driver.find_element(By.ID, 'select-language'))
        select_language.select_by_index(0)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)