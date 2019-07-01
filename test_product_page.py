from pages.product_page import ProductPage

def test_should_see_button_add_to_basket(browser):
    page = ProductPage(browser, ProductPage.link)
    page.open()
    page.should_be_button_add_to_basket()

def test_could_add_product_with_button_add_to_basket(browser):
    page = ProductPage(browser, ProductPage.link)
    page.open()
    page.click_button_add_to_basket()
