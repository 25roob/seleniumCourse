from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

class MercadoPage(object):
    def __init__(self, driver):
        self._driver = driver
        self._url = 'https://www.mercadolibre.com/'
        self.search_locator = 'as_word'

    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.NAME, 'as_word')))
        return True

    @property
    def keyword(self):
        input_field = self._driver.find_element(By.NAME, 'as_word')
        return input_field.get_attribute('value')

    def open(self):
        self._driver.get(self._url)

    def search(self, keyword):
        input_field = self._driver.find_element(By.NAME, 'as_word')
        input_field.send_keys(keyword)

    def click_submit(self):
        input_field = self._driver.find_element(By.NAME, 'as_word')
        input_field.submit()

    def select_country(self, country_ID):
        country_button = self._driver.find_element(By.ID, country_ID)
        country_button.click()