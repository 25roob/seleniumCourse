import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep

class MercadoLibre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service = Service('./chromedriver.exe'))
        driver = self.driver
        driver.maximize_window()
        driver.get('https://www.mercadolibre.com/')
        driver.find_element(By.ID, 'CO').click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'as_word')))

    def test_scrap_prices(self):
        driver = self.driver
                
        search_bar = driver.find_element(By.NAME, 'as_word')
        search_bar.clear()
        search_bar.send_keys('playstation 4')
        search_bar.submit()
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root-app"]/div/div/aside/section/div[11]/ul/li[1]/a')))

        driver.find_element(By.ID, 'newCookieDisclaimerButton').click()

        bogota_button = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div/aside/section/div[11]/ul/li[1]/a')
        bogota_button.click()
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root-app"]/div/div/aside/section[1]/a/div/div')))

        nuevos_button = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div/aside/section[2]/div[6]/ul/li[1]/a/span[1]')
        nuevos_button.click()
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root-app"]/div/div/aside/section[1]/a[2]/div/div')))

        sort_select_button = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div/section/div[1]/div/div/div/div[2]/div/div/button')
        sort_select_button.click()

        select_mayor_precio = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div/section/div[1]/div/div/div/div[2]/div/div/div/ul/a[2]')
        select_mayor_precio.click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="root-app"]/div/div/section/div[1]/div/div/div/div[2]/div/div/button/span'), 'Mayor precio'))
        driver.implicitly_wait(3)

        table_data = [[] for _ in range(5)]
        for i in range(5):
            name_product = driver.find_element(By.XPATH, f'//*[@id="root-app"]/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a/h2')
            table_data[i].append(name_product.text)

            price_tag = driver.find_element(By.XPATH, f'//*[@id="root-app"]/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/span[1]/span[2]/span[1]')

            price_value = driver.find_element(By.XPATH, f'//*[@id="root-app"]/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/span[1]/span[2]/span[2]')

            full_price = price_tag.text + ' ' + price_value.text

            table_data[i].append(full_price)
        
        print(table_data)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)