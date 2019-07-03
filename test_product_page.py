import pytest

from pages.product_page import ProductPage


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_should_see_button_add_to_basket(browser):
    page = ProductPage(browser, ProductPage.link)
    page.open()
    page.should_be_button_add_to_basket()

def test_could_add_product_with_button_add_to_basket(browser):
    page = ProductPage(browser, ProductPage.link)
    page.open()
    page.click_button_add_to_basket()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, ProductPage.link)
    page.open()
    page.should_not_be_success_message()
