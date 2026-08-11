import pytest
from playwright.sync_api import Page

from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.CheckoutPage import CheckoutPage

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Fixture to login the user"""
    login_page = LoginPage(page)
    login_page.open()
    return login_page


@pytest.fixture
def inventory_page(login_page: LoginPage) -> InventoryPage:
    return login_page.login_standard_user()

@pytest.fixture
def checkout_started(inventory_page: InventoryPage) -> CheckoutPage:
    inventory_page.add_item_to_cart("sauce-labs-backpack")
    #          Inventory.open_cart() - > CartPage : CartPage.start_checkout() ->CheckoutPage
    return inventory_page.open_cart().start_checkout()

@pytest.fixture
def completed_order(checkout_started: CheckoutPage) -> CheckoutPage:
    return checkout_started.form_fill_out("Solid", "Snake", "00001").finish()


