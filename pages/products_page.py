from utils.logger import logger


class ProductsPage:

    def __init__(self, page):
        self.page = page

        self.products_title = page.locator(".title")
        self.cart = page.locator(".shopping_cart_link")
        self.add_backpack = page.locator("#add-to-cart-sauce-labs-backpack")

    def is_products_page_visible(self):

        logger.info("Checking whether products page is visible")

        return self.products_title.is_visible()

    def add_backpack_to_cart(self):

        logger.info("Adding Sauce Labs Backpack to cart")

        self.add_backpack.click()

    def open_cart(self):

        logger.info("Opening shopping cart")

        self.cart.click()