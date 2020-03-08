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
    WebDriverWait(browser, 5).until(ec.element_to_be_clickable((By.TAG_NAME, "textarea")))
    browser.find_element_by_css_selector("textarea").send_keys(str(answer))
    browser.find_element_by_css_selector("button").click()
    WebDriverWait(browser, 5).until(ec.presence_of_element_located((By.TAG_NAME, "pre")))
    result = browser.find_element_by_css_selector(".smart-hints__hint").text    
    assert result == "Correct!", f"expected 'Correct', got {result}"

    