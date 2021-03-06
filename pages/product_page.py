from .base_page import BasePage
from .locators import BasketLocators, BasePageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_basket(self):
        assert self.is_element_present(*BasketLocators.ADD_BUTTON), "Button is not presented"
        button = self.browser.find_element(*BasketLocators.ADD_BUTTON)
        button.click()

    def should_be_book_price(self):
            book_price = self.browser.find_element(*BasketLocators.BOOK_PRICE).text
            basket_price = self.browser.find_element(*BasketLocators.BOOK_PRICE_BASKET).text
            assert book_price == basket_price, "Price is not same"

    def should_be_book_name(self):
            book_name = self.browser.find_element(*BasketLocators.BOOK_NAME).text
            book_basket = self.browser.find_element(*BasketLocators.BOOK_NAME_BASKET).text
            assert book_name == book_basket, "Name is not same"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def is_dissappeared(self):
        assert self.is_disappeared(*BasketLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

