from selenium.webdriver.common.by import By

class Links():
	MAIN_PAGE = "http://selenium1py.pythonanywhere.com/"
	PRODUCT_PAGE = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	LOGIN_PAGE = "http://selenium1py.pythonanywhere.com/accounts/login/"
	
class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	BASKET_TOTAL = (By.CSS_SELECTOR, ".basket-mini")
	BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
	REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
	REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
	REGISTER_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")

class ProductPageLocators():
	ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
	NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main > h1")
	ITEM_NAME_IN_SUCCESS_POPUP = (By.CSS_SELECTOR, "#messages :first-child strong")
	ITEM_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages :first-child")

class BasketPageLocators():
	BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
	TEXT_ABOUT_EMPTINESS = (By.CSS_SELECTOR, "#content_inner")