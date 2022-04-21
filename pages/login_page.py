

from .base_page import BasePage
from .locators import LoginPageLocators, BasketLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Login form is not presented"


    def add_to_basket(self):
        assert self.is_element_present(*BasketLocators.ADD_BUTTON), "Button is not presented"
        button = self.browser.find_element(*BasketLocators.ADD_BUTTON)
        button.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
