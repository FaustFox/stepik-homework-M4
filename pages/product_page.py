from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    def click_button_add_to_basket(self):
        button = self.browser.find_element(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET
            )
        button.click()

        self.solve_quiz_and_get_code()

        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
            ).text
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
            ).text
        basket_product_name = self.browser.find_element(
            *ProductPageLocators.ADDED_TO_BASKET_PRODUCT_NAME
            ).text
        basket_product_price = self.browser.find_element(
            *ProductPageLocators.ADDED_TO_BASKET_PRODUCT_PRICE
            ).text

        assert product_name == basket_product_name, \
            "Product name do not match product name in the basket"
        assert product_price == basket_product_price, \
            "Product price do not match product price in the basket"

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET
            ), "Button is not present"
