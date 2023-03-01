from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

links = ["registration2", "registration1"]


@pytest.mark.parametrize("link", links)
def test_reg(browser, link):
    link = f"http://suninjuly.github.io/{link}.html"
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
    assert welcome_text == "Congratulations! You have successfully registered!", f"expected 'Congratulations! You have successfully registered!', got {welcome_text}"
