from selenium.webdriver.common.by import By
import time
import pytest


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    time.sleep(30)

    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")

    assert button is not None, "Add to basket button is not present"