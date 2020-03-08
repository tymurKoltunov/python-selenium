from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element_by_css_selector("[name='firstname']").send_keys("check")
    browser.find_element_by_css_selector("[name='lastname']").send_keys("check")
    browser.find_element_by_css_selector("[name='email']").send_keys("check")
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'commands.txt')
    browser.find_element_by_css_selector("[type='file']").send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()