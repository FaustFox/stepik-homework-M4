from selenium.webdriver.common.by import By 


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_BAD = (By.CSS_SELECTOR, "#login_link_bad")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:

    GOODS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FORM_NAME_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_FORM_PASS_INPUT = (By.CSS_SELECTOR, "#id_login-password")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_FORM_NAME_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REG_FORM_PASS1_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_FORM_PASS2_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_FORM_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADDED_TO_BASKET_PRODUCT_NAME = (
        By.CSS_SELECTOR, 
        ".alert:nth-child(1) .alertinner strong"
        )
    ADDED_TO_BASKET_PRODUCT_PRICE = (
        By.CSS_SELECTOR, 
        ".alert:nth-child(3) .alertinner strong"
        )
