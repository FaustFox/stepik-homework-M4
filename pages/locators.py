from selenium.webdriver.common.by import By 


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FORM_NAME_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_FORM_PASS_INPUT = (By.CSS_SELECTOR, "#id_login-password")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_FORM_NAME_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REG_FORM_PASS1_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_FORM_PASS2_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
