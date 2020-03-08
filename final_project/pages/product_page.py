from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
	def add_product_to_basket(self):
		self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

	def should_be_product_name_in_popup(self):
		assert self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text == \
		       self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_SUCCESS_POPUP).text, \
		       "Product name in 'has been added to your basket.' popup does not match actual product"

	def item_price_should_match_basket_total(self):
		assert float(self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text[1:]) == \
		           self.get_basket_total(), \
		           "Price of item does not match Basket total"

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
		       "Success message is presented, but should not be"

	def success_msg_should_disappear(self):
		assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
               "Success message is not disappeared, but should "


