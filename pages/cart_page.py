from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_should_have_product(self):
        goods = self.is_element_present(*BasketPageLocators.GOODS_IN_BASKET)
        assert goods, "Basket empty, but should not"

    def basket_should_not_have_product(self):
        goods = self.is_not_element_present(*BasketPageLocators.GOODS_IN_BASKET)
        assert goods, "Basket should be empty"

    def basket_with_product_should_not_have_message_of_emptyness(self):
        message = self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY)
        assert message, "Basket with goods should not have message of empty basket"

    def basket_without_product_should_have_message_of_emptyness(self):
        message = self.is_element_present(*BasketPageLocators.BASKET_EMPTY)
        assert message, "Empty basket should have message that its empty"
