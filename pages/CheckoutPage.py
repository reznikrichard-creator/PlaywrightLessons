from playwright.sync_api import Page
# from pages.CheckoutPage import CheckoutPage

class CheckoutPage:

    def __init__(self, page:Page) -> None:
        #Locators

        #Page 1
        self.page_title = page.locator("[data-test=\"title\"]")
        self.first_name = page.locator("[data-test=\"firstName\"]")
        self.last_name = page.locator("[data-test=\"lastName\"]")
        self.postal_code = page.locator("[data-test=\"postalCode\"]")
        self.cancel = page.locator("[data-test=\"cancel\"]")
        self.continue_button = page.locator("[data-test=\"continue\"]")

        #Page 2
        self.item_item = page.locator("[data-test=\"inventory-item\"]")
        self.payment_info = page.locator("[data-test=\"payment-info-value\"]")
        self.shipping_info = page.locator("[data-test=\"shipping-info-value\"]")
        self.price_total = page.locator("[data-test=\"shipping-info-value\"]")
        self.finish_checkout = page.locator("[data-test=\"finish\"]")

        #Page 3
        self.complete_text = page.locator("[data-test=\"complete-header\"]")
        self.complete_logo = page.locator("[data-test=\"pony-express\"]")

        # Methods
    def go_to_checkout(self):
        self.checkout_button.click()
        return CheckoutPage(self.page)
    
    def form_fill_out(self):
        self.first_name.fill("asdf")
        self.last_name.fill("df")
        self.postal_code.fill("47284")
        


        #Getters
        
    def get_page_title(self):
        return self.page_title

    