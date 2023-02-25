from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from pathlib import Path
try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.CSS_SELECTOR, "[name='firstname']").send_keys("check")
    browser.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys("check")
    browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("check")
    print("filled fields")
    file_path = str(Path(__file__).parent.parent) + "/test_data/text.txt"
    browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)
    print("uploaded file")
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    print("clicked submit")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
