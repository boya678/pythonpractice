from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pageobjects.home import Home
from pageobjects.login import Login
from pageobjects.checkout import Checkout


def set_browser(url):
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.implicitly_wait(20)
    browser.maximize_window()
    browser.delete_all_cookies()
    browser.get(url)
    return browser

def close_browser(browser):
    browser.quit()

def test_validate_selected_list_IOS():
    browser=set_browser("https://bstackdemo.com/")
    Home(browser).select_brand("Apple")
    for brand in Home(browser).get_selected_products():
        assert "iPhone" in brand
    close_browser(browser)

def test_validate_checkout():
    browser=set_browser("https://bstackdemo.com/")
    Home(browser).select_brand("Apple")
    for brand in Home(browser).get_selected_products():
        assert "iPhone" in brand
    price=Home(browser).get_price_by_reference('iPhone 12 Mini').replace("$", "")
    Home(browser).add_to_cart_by_reference('iPhone 12 Mini')
    detail=Home(browser).get_checkout_detail('iPhone 12 Mini')
    assert price in detail
    assert 'iPhone 12 Mini' in detail
    assert 'Quantity: 1' in detail
    assert 'Apple' in detail
    Home(browser).click_checkout()
    Login(browser).set_username("demouser")
    Login(browser).set_password("testingisfun99")
    Login(browser).click_login()
    total_price=Checkout(browser).get_total_price().replace("$", "")
    assert price in Checkout(browser).get_total_price().replace("$", "")
    close_browser(browser)