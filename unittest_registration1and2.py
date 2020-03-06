from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

browser = webdriver.Chrome()

class TestAbs(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"    
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector(".first_block .first").send_keys("check")
        browser.find_element_by_css_selector(".first_block .second").send_keys("check")
        browser.find_element_by_css_selector(".first_block .third").send_keys("check")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        WebDriverWait(browser, 5).until(ec.presence_of_element_located((By.TAG_NAME, "h1")))
        welcome_text = browser.find_element_by_tag_name("h1").text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 
            f"expected 'Congratulations! You have successfully registered!', got {welcome_text}")
        
    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"    
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector(".first_block .first").send_keys("check")
        browser.find_element_by_css_selector(".first_block .second").send_keys("check")
        browser.find_element_by_css_selector(".first_block .third").send_keys("check")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        WebDriverWait(browser, 5).until(ec.presence_of_element_located((By.TAG_NAME, "h1")))
        welcome_text = browser.find_element_by_tag_name("h1").text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 
            f"expected 'Congratulations! You have successfully registered!', got {welcome_text}")
        

if __name__ == "__main__":
    unittest.main()

