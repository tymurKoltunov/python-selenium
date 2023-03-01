from selenium import webdriver
import time
import pytest
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]


@pytest.mark.parametrize("link", links)
def test_reg(browser, link, answer):
    browser.get(link)
    loading = browser.find_element(By.CSS_SELECTOR, ".stepik-loader__icon")
    WebDriverWait(browser, 20).until(ec.staleness_of(loading))
    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.ID, "ember33").click()
    time.sleep(5)
    browser.find_element(By.ID, "id_login_email").send_keys("tymur.koltunov@nure.ua")
    time.sleep(5)
    browser.find_element(By.ID, "id_login_password").send_keys("3mmwdA,gL$4.7Sx")
    time.sleep(5)
    login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    time.sleep(5)
    login_button.click()
    # Отправляем заполненную форму
    WebDriverWait(browser, 20).until(ec.staleness_of(login_button))
    WebDriverWait(browser, 20).until(ec.presence_of_element_located((By.CSS_SELECTOR, "[data-type='string-quiz']")))

    WebDriverWait(browser, 15).until(ec.element_to_be_clickable((By.TAG_NAME, "textarea")))
    browser.find_element(By.CSS_SELECTOR, "textarea").clear()
    browser.find_element(By.CSS_SELECTOR, "textarea").send_keys(str(answer))
    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
    time.sleep(5)
    WebDriverWait(browser, 20).until(ec.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    result = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
    assert result == "Correct!", f"expected 'Correct', got {result}"
