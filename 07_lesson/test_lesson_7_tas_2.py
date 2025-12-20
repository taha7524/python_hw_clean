from selenium import webdriver
from authorization import Authorization
from inventory import Inventory
from cart import Cart
from checkout_step_one import CheckoutStepOne
from checkout_step_two import CheckoutStepTwo


def test_internet_shop():
    username = "standard_user"
    password = "secret_sauce"
    first_name = "John"
    last_name = "Smith"
    zip_code = "33701-4313"

    browser = webdriver.Firefox()

    authorization_page = Authorization(browser)
    authorization_page.authorization(username, password)

    inventory_page = Inventory(browser)
    inventory_page.add_to_cart()
    inventory_page.go_to_cart()

    cart_page = Cart(browser)
    cart_page.checkout()

    checkout_step_one_page = CheckoutStepOne(browser)
    checkout_step_one_page.filling_form(first_name, last_name, zip_code)
    checkout_step_one_page.click_continue()

    checkout_step_two_page = CheckoutStepTwo(browser)
    total = checkout_step_two_page.read_total()

    assert total[total.find("$"):] == "$58.29"

    browser.quit()