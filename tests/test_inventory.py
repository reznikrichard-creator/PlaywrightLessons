from playwright.sync_api import Page
import pytest

from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage

def test_sort_dropdown_visible(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    inventory_page = login_page.login_standard_user()

    assert inventory_page.get_sort_dropdown().is_visible

def test_product_sort(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    inventory_page = login_page.login_standard_user()

    # inventory_page = InventoryPage(page)
    inventory_page.sort_products_by("za")
 
    assert inventory_page.get_selected_sort() == "za"

@pytest.mark.parametrize(
    "options",
    [
        ("az"),
        ("za"),
        ("lohi"),
        ("hilo"),
    ],
)    

def test_sort_options(page: Page, options):
    login_page = LoginPage(page)
    login_page.open()
    inventory_page = login_page.login_standard_user()

    inventory_page.sort_products_by(options)

    assert inventory_page .get_selected_sort() == options

