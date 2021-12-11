import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service = Service('./chromedriver.exe'))
        driver = self.driver
        driver.maximize_window()
        driver.get('https://www.bing.com/')
        driver.implicitly_wait(30)

    def test_browser_navigation(self):
        driver = self.driver
        
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys('gatitos')
        search_field.submit()

        driver.back()
        sleep(3)
        driver.forward()
        sleep(3)
        driver.refresh()
        sleep(3)
    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)