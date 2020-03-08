from .pages.product_page import ProductPage 
from .pages.login_page import LoginPage
import pytest
from .pages.locators import Links
from .pages.basket_page import BasketPage
import faker 

f = faker.Faker()

@pytest.mark.user
class TestUserAddToBasketFromProductPage():
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		login_page = LoginPage(browser, Links.LOGIN_PAGE)
		login_page.open()
		login_page.should_be_login_page()		
		email = f.email()
		password = email + email
		login_page.register_new_user(email, password)
		login_page.should_be_authorized_user()

	def test_user_cant_see_success_message(self, browser):
		page = ProductPage(browser, Links.PRODUCT_PAGE)
		page.open()
		page.should_not_be_success_message()

	@pytest.mark.need_review
	def test_user_can_add_product_to_basket(self, browser):
		page = ProductPage(browser, Links.PRODUCT_PAGE)
		page.open()
		page.add_product_to_basket()
		page.should_be_product_name_in_popup()
		page.item_price_should_match_basket_total()

@pytest.mark.negative
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):	
	page = ProductPage(browser, Links.PRODUCT_PAGE)
	page.open()
	page.add_product_to_basket()
	page.should_not_be_success_message()

@pytest.mark.negative
def test_guest_cant_see_success_message(browser):
	page = ProductPage(browser, Links.PRODUCT_PAGE)
	page.open()
	page.should_not_be_success_message()

@pytest.mark.negative
def test_message_disappeared_after_adding_product_to_basket(browser):
	page = ProductPage(browser, Links.PRODUCT_PAGE)
	page.open()
	page.add_product_to_basket()
	page.success_msg_should_disappear()

@pytest.mark.login
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
@pytest.mark.login
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()
	login_page = LoginPage(browser, browser.current_url)
	login_page.should_be_login_page()

@pytest.mark.need_review
@pytest.mark.empty_basket_check
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	page = ProductPage(browser, Links.PRODUCT_PAGE)
	page.open()
	page.go_to_basket_page()
	basket_page = BasketPage(browser, browser.current_url)
	basket_page.should_be_no_items()
	basket_page.should_be_text_your_basket_is_empty()

@pytest.mark.need_review
@pytest.mark.add_to_basket
#@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='additional word in book name')) for i in range(10)]) Параметризация. найти в каком из офером баг(доп слово в  теге strong)
def test_guest_can_add_product_to_basket(browser):#, promo_offer):
	#link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
	page = ProductPage(browser, Links.PRODUCT_PAGE)#link)
	page.open()
	page.add_product_to_basket()
	#page.solve_quiz_and_get_code()
	page.should_be_product_name_in_popup()
	page.item_price_should_match_basket_total()