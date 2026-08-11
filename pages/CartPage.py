from playwright.sync_api import Page
from pages.CheckoutPage import CheckoutPage

class CartPage:
    # POM for Cart Page
    def __init__(self, page:Page) -> None:
        #Locators
        self.page = page
        self.page_title = page.locator("[data-test=\"title\"]")
        self.inventory_item = page.locator("[data-test=\"inventory-item\"]")
        self.item_name = page.locator("[data-test=\"inventory-item-name\"]")
        self.item_description = page.locator("[data-test=\"inventory-item-desc\"]")
        self.invetory_price = page.locator("[data-test=\"inventory-item-price\"]")
        self.checkout_button = page.locator("[data-test=\"checkout\"]")
        self.continue_shopping = page.locator("[data-test=\"continue-shopping\"]")

        self.remove_item = page.locator("[data-test=\"remove-sauce-labs-backpack\"]")

    # Methods
    def start_checkout(self) -> CheckoutPage:
        self.checkout_button.click()
        return CheckoutPage(self.page)

    def continue_shopping(self):
        # Navigates back to the inventory page.
        # The import is INSIDE the method to avoid a circular import
        # (InventoryPage imports CartPage at the top of its file).
        from pages.InventoryPage import InventoryPage

        self.continue_shopping_button.click()
        return InventoryPage(self.page)

    def remove_item(self, item_id: str):
        # item_id looks like "sauce-labs-backpack".
        # The remove button changes per product, so we build the locator here
        # instead of in __init__.
        self.page.locator(f"[data-test=\"remove-{item_id}\"]").click()
        # We stay on the SAME screen, so we return self. That lets us chain calls:
        # cart_page.remove_item("a").remove_item("b")
        return self

    def logout(self):
        # Same circular-import escape: LoginPage -> InventoryPage -> CartPage -> LoginPage
        # would be a loop if this import sat at the top of the file.
        # Importing here means it runs when the method is CALLED, not at import time.
        from pages.LoginPage import LoginPage

        self.menu_button.click()
        self.logout_link.click()
        return LoginPage(self.page)

    # Getters
    def get_page_title(self):
        return self.page_title

    def get_checkout_button(self):
        return self.checkout_button

    def get_item_count(self):
        return self.inventory_item.count()

    def get_item_name(self):
        return self.item_name.all_text_contents()
    