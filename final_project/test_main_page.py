from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import Links
import pytest

def test_guest_can_go_to_login_page(browser): 
   page = MainPage(browser, Links.MAIN_PAGE)
   page.open()
   page.go_to_login_page()
   login_page = LoginPage(browser, browser.current_url)
   login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, Links.MAIN_PAGE)
    page.open()
    page.should_be_login_link()

@pytest.mark.empty_basket_check
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
	page = MainPage(browser, Links.MAIN_PAGE)
	page.open()
	page.go_to_basket_page()
	basket_page = BasketPage(browser, browser.current_url)
	basket_page.should_be_no_items()
	basket_page.should_be_text_your_basket_is_empty()