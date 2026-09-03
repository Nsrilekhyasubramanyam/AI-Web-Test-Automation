from utils.logger import logger


class CheckoutPage:

    def __init__(self, page):
        self.page = page

        self.checkout_button = page.locator("#checkout")
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.success_message = page.locator(".complete-header")

    def checkout(self):

        logger.info("Starting checkout")

        self.checkout_button.click()

    def enter_customer_details(
        self,
        first_name,
        last_name,
        postal_code
    ):

        logger.info("Entering customer checkout details")

        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def continue_checkout(self):

        logger.info("Continuing checkout")

        self.continue_button.click()

    def finish_order(self):

        logger.info("Finishing order")

        self.finish_button.click()

    def get_success_message(self):

        logger.info("Retrieving checkout success message")

        return self.success_message.text_content()