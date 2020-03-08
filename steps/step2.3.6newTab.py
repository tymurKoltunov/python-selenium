from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

        button = browser.find_element_by_css_selector("button.btn")
        button.click()    
        browser.switch_to.window(browser.window_handles[1])
        assert "Math is real magic!" == browser.find_element_by_css_selector("#simple_text").text
        answer = calc(browser.find_element_by_css_selector("#input_value").text)
        browser.find_element_by_css_selector("#answer").send_keys(answer)    
        browser.find_element_by_css_selector("button.btn").click()
    
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()