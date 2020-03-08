from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
	def should_be_no_items(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
		       "Items list is not empty"
	
	def should_be_text_your_basket_is_empty(self):
		assert "Your basket is empty." in \
		       self.browser.find_element(*BasketPageLocators.TEXT_ABOUT_EMPTINESS).text, \
		       "There is no 'Your basket is empty.' text"