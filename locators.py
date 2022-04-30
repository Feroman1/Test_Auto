from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = ("http://selenium1py.pythonanywhere.com/ru/accounts/login/")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ShopPageLocators():
    ADD_PRODUCT = (By.XPATH, ('//button[text() = "Добавить в корзину"]'))
    BOOK_NAME = (By.XPATH, ('//div[@class="col-sm-6 product_main"]/h1'))
    BOOK_NAME_LAST = (By.XPATH, ('//div[@id="messages"]//strong'))
    BOOK_PRICE = (By.XPATH, ('//p[@class="price_color"]'))
    BOOK_PRICE_LAST = (By.XPATH, ('//p/strong'))
    SUCCESS_MESSAGE = (By.ID, ('messages'))

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")