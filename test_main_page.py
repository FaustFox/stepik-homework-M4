from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.cart_page import BasketPage
from pages.product_page import ProductPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_empty_message_in_basket_from_main_page(browser):
    page = ProductPage(browser, ProductPage.link)
    page.open()
    page.click_button_add_to_basket()
    link = "http://selenium1py.pythonanywhere.com"
    basket_page = BasketPage(browser, link)
    basket_page.open()
    basket_page.go_to_basket_page()
    basket_page.basket_should_have_product()
    basket_page.basket_with_product_should_not_have_message_of_emptyness()

def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.basket_should_not_have_product()
    page.basket_without_product_should_have_message_of_emptyness()
    
def test_should_be_login_page_direct_link(browser):
    page = LoginPage(browser, LoginPage.link)
    page.open()
    page.should_be_login_url()

def test_should_be_login_form_direct_link(browser):
    page = LoginPage(browser, LoginPage.link)
    page.open()
    page.should_be_login_form()

def test_should_be_register_form_direct_link(browser):
    page = LoginPage(browser, LoginPage.link)
    page.open()
    page.should_be_register_form()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
