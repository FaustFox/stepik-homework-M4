from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_should_see_login_link(browser):
    page = MainPage(browser, MainPage.link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MainPage.link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

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
