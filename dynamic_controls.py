import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicControls(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(service = Service('./chromedriver.exe'))
        driver = cls.driver
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Dynamic Controls').click()

    def test_remove_button(self):
        driver = self.driver
        get_remove_button = driver.find_element(By.XPATH, '//*[@id="checkbox-example"]/button')
        get_remove_button.click()
        WebDriverWait(driver, 15).until(EC.invisibility_of_element_located((By.ID, 'checkbox')))
        get_remove_button.click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.ID, 'checkbox')))
        driver.find_element(By.ID, 'checkbox').click()
        sleep(5)

    def test_enable_button(self):
        driver = self.driver
        get_enable_button = driver.find_element(By.XPATH, '//*[@id="input-example"]/button')
        get_enable_button.click()
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/form[2]/input')))
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/form[2]/input').send_keys("por favor que funcione!")
        sleep(5)

    def tearDown(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)