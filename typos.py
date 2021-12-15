import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Typos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service = Service('./chromedriver.exe'))
        driver = self.driver
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Typos').click()

    def test_find_typo(self):
        driver = self.driver

        paragraph_to_check = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)')
        text_to_check = paragraph_to_check.text
        self.assertTrue(text_to_check)
        print(text_to_check)
        
        tries = 1
        correct_text = "Sometimes you'll see a typo, other times you won't."

        while text_to_check != correct_text:
            paragraph_to_check = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)')
            text_to_check = paragraph_to_check.text
            tries += 1
            driver.refresh()

        self.assertEqual(text_to_check, correct_text)

        print(f'It took {tries} tries to find the typo')
        driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)