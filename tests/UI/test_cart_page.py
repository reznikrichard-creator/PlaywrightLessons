import pytest
from playwright.sync_api import Page

from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage


def test_cart_page_load(inventory_page: InventoryPage):
    cart_page = inventory_page.open_cart()

    # Verify title
    assert cart_page.get_page_title().text_content() == "Your Cart"
    # Verify checkoput is visible
    assert cart_page.get_checkout_button().is_visible()

# Paramaterize Later
def test_add_item_to_cart(inventory_page: InventoryPage):
    inventory_page.add_item_to_cart("sauce-labs-backpack")

    cart_page = inventory_page.open_cart()

    # assert the item count went up
    assert cart_page.get_item_count() == 1
    # assert the item name is correct
    assert "Sauce Labs Backpack" in cart_page.get_item_name()