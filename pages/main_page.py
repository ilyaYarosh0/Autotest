from .base_page import BasePage
from .locators import MainPageLocators, BasketLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        login_link = self.browser.find_element(*BasketLocators.ADD_BUTTON)
        login_link.click()
