from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    n1 = browser.find_element_by_css_selector("#num1")
    n2 = browser.find_element_by_css_selector("#num2")
    y = int(n1.text) + int(n2.text)
    print(y)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(y))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()