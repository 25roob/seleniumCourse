import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service = Service('./chromedriver.exe'))
        driver = self.driver
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('How many elements do you want to add?: '))
        elements_remover = int(input('How many elements do you want to remove?: '))
        total_elements = elements_added - elements_remover

        add_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')

        sleep(3)

        for _ in range(elements_added):
            add_button.click()

        for _ in range(elements_remover):
            try:
                delete_button = driver.find_element(By.CLASS_NAME, 'added-manually')
                delete_button.click()
            except:
                print('You are trying to eliminate more buttons than the number of existing ones')
                break

        if total_elements > 0:
            print(f'There are {total_elements} on screen.')
        
        else:
            print('There are 0 elements on screen.')

        sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)