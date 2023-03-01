from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_reg(browser):
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    loading = browser.find_element(By.CSS_SELECTOR, ".stepik-loader__icon")
    WebDriverWait(browser, 10).until(ec.staleness_of(loading))
    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.ID, "ember33").click()
    browser.find_element(By.ID, "id_login_email").send_keys("tymur.koltunov@nure.ua")
    browser.find_element(By.ID, "id_login_password").send_keys("3mmwdA,gL$4.7Sx")
    login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    # Отправляем заполненную форму
    WebDriverWait(browser, 10).until(ec.staleness_of(login_button))
    WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.CSS_SELECTOR, "[data-type='string-quiz']")))

