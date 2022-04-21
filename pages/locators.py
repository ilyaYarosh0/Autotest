from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class BasketLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1)")
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    BOOK_NAME_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
    BOOK_PRICE_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(3) strong")

class BasePageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")

