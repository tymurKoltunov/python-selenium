from selenium import webdriver
import time
import pytest
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_busket_button_present(chrome):
    chrome.get(link)
    chrome.find_element_by_css_selector(".btn-add-to-basket").click()
    WebDriverWait(chrome, 5).until(ec.presence_of_element_located((By.ID, "messages")))
    text = chrome.find_element_by_css_selector("#messages :first-child").text    
    assert "Coders at Work" in text, f"expected 'Coders at Work' in substring, got '{text}'"

    