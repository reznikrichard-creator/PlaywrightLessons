from playwright.sync_api import Page
# from pages.CheckoutPage import CheckoutPage

class CheckoutPage:

    def __init__(self, page:Page) -> None:
        #Locators
        self.page = page
        #Page 1
        self.page_title = page.locator("[data-test=\"title\"]")

        self.first_name = page.locator("[data-test=\"firstName\"]")
        self.last_name = page.locator("[data-test=\"lastName\"]")
        self.postal_code = page.locator("[data-test=\"postalCode\"]")
        self.cancel_button = page.locator("[data-test=\"cancel\"]")
        self.continue_button = page.locator("[data-test=\"continue\"]")
        self.error_message = page.locator("[data-test=\"error\"]")
        self.continue_button = page.locator("[data-test=\"continue\"]")

        #Page 2
        self.item_names = page.locator("[data-test=\"inventory-item-name\"]")
        self.subtotal_label = page.locator("[data-test=\"subtotal-label\"]")
        self.total_label = page.locator("[data-test=\"total-label\"]")
        self.payment_info = page.locator("[data-test=\"payment-info-value\"]")
        self.shipping_info = page.locator("[data-test=\"shipping-info-value\"]")
        self.price_total = page.locator("[data-test=\"shipping-info-value\"]")
        self.finish_checkout = page.locator("[data-test=\"finish\"]")

        #Page 3
        self.complete_text = page.locator("[data-test=\"complete-header\"]")
        self.complete_logo = page.locator("[data-test=\"pony-express\"]")
        self.complete_header = page.locator("[data-test=\"complete-header\"]")
        self.back_home_button = page.locator("[data-test=\"back-to-products\"]")

        # Methods
    
    def form_fill_out(self, first_name: str, last_name: str, postal_code: str):
        # Fills the form and clicks Continue.
        # NOTE: no assert in here. If the form is invalid we stay on step one and
        # the test can check the error itself. One method serves happy AND sad path.
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)
        self.continue_button.click()
        # Still inside the same checkout flow, so return self and keep chaining.
        return self

    def finish(self):
        # Confirms the order and lands on the "complete" screen.
        self.finish_checkout.click()
        return self

    def cancel(self):
        # Cancel takes us back out of checkout.
        from pages.InventoryPage import InventoryPage

        self.cancel_button.click()
        return InventoryPage(self.page)

    def back_home(self):
        # Only available on the final "Thank you" screen.
        # Local import again: it breaks the import loop between the page files.
        from pages.InventoryPage import InventoryPage

        self.back_home_button.click()
        return InventoryPage(self.page)
        


        #Getters
        
    def get_page_title(self):
        return self.page_title

    def get_error_message(self):
        return self.error_message

    def get_complete_header(self):
        return self.complete_header

    def get_complete_text(self):
        return self.complete_text

    def get_item_names(self):
        return self.item_names.all_text_contents()

    def get_item_count(self):
        return self.item_names.count()

    def get_total_label(self):
        return self.total_label

    def get_total(self):
        # "Total: $32.39" -> 32.39
        total_text = self.total_label.text_content()
        return float(total_text.split("$")[1])

    def get_subtotal(self):
        # "Item total: $29.99" -> 29.99
        subtotal_text = self.subtotal_label.text_content()
        return float(subtotal_text.split("$")[1])

    