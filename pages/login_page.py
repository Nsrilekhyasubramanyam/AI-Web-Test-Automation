from utils.logger import logger
from utils.config import BASE_URL


class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")

    def navigate(self):
        logger.info("Opening SauceDemo login page")
        self.page.goto(BASE_URL)

    def login(self, username, password):

        logger.info(f"Attempting login with username: {username}")

        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

        logger.info("Login button clicked")

    def get_error_message(self):

        logger.info("Retrieving login error message")

        return self.error_message.text_content()