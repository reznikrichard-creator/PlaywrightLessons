import pytest
from playwright.sync_api import Page
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.CheckoutPage import CheckoutPage


def test_fill_out_page_is_visible(page: Page):
    login_page = LoginPage(page)
    inventory_page = login_page.login_standard_user()
    inventory_page.add_item_to_cart("sauce-labs-backpack")
    inventory_page = inventory_page.go_to_cart()
    inventory_page.checkout_button.click()

    checkout_page = CheckoutPage(page)
    
    assert checkout_page.get_page_title().text_content() == "Checkout: Your Information"


def test_all_information(page: Page):
    login_page = LoginPage(page)
    inventory_page = login_page.login_standard_user()
    inventory_page.add_item_to_cart("sauce-labs-backpack")
    inventory_page = inventory_page.go_to_cart()
    inventory_page.checkout_button.click()

    checkout_page = CheckoutPage(page)

    checkout_page.form_fill_out()
    checkout_page.continue_button.click()


    assert checkout_page.get_page_title().text_content() == "Checkout: Overview"
    assert checkout_page.item_item.is_visible()
    assert checkout_page.payment_info.is_visible()
    assert checkout_page.shipping_info.is_visible()
    assert checkout_page.price_total.is_visible()


def test_verify_thank_you_message(page: Page):
    # Click Finish
    login_page = LoginPage(page)
    inventory_page = login_page.login_standard_user()
    inventory_page.add_item_to_cart("sauce-labs-backpack")
    inventory_page = inventory_page.go_to_cart()
    inventory_page.checkout_button.click()

    checkout_page = CheckoutPage(page)

    checkout_page.form_fill_out()
    checkout_page.continue_button.click()
    checkout_page.finish_checkout.click()
    # Assert the Message
    assert checkout_page.complete_text.text_content() == "Thank you for your order!"
    assert checkout_page.complete_logo.is_visible()