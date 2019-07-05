from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

    def register_new_user(self, email, password="111111119"):
        self.browser.find_element(
            *LoginPageLocators.REG_FORM_NAME_INPUT
            ).send_keys(email)
        self.browser.find_element(
            *LoginPageLocators.REG_FORM_PASS1_INPUT
            ).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.REG_FORM_PASS2_INPUT
            ).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.REG_FORM_BUTTON
            ).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Page not found"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
        "Login form not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), \
        "Registration form not found"
