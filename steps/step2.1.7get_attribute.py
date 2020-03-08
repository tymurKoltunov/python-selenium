from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element_by_css_selector("[valuex]").get_attribute("valuex")
    y = calc(x)
    browser.find_element_by_css_selector("#answer").send_keys(y)
    
    browser.find_element_by_css_selector("#robotCheckbox").click()
    browser.find_element_by_css_selector("#robotsRule").click()


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()