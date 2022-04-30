from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ShopPageLocators
class Login2Page(BasePage):
    def should_be_login_page(self):
        self.should_be_alert()

    def should_not_be_success(self):
        assert self.is_not_element_present(*ShopPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"