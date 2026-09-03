import json
import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


with open("test_data/users.json", "r") as file:
    users = json.load(file)


@pytest.mark.smoke
def test_valid_login(page):

    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.navigate()

    login_page.login(
        users["valid_user"]["username"],
        users["valid_user"]["password"]
    )

    assert products_page.is_products_page_visible()


@pytest.mark.parametrize(
    "username,password",
    [
        ("wrong_user", "secret_sauce"),
        ("standard_user", "wrong_password"),
        ("", "secret_sauce"),
        ("standard_user", "")
    ]
)
def test_invalid_login(page, username, password):

    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.navigate()

    login_page.login(username, password)

    assert not products_page.is_products_page_visible()


def test_locked_user(page):

    login_page = LoginPage(page)

    login_page.navigate()

    login_page.login(
        users["locked_user"]["username"],
        users["locked_user"]["password"]
    )

    error = login_page.get_error_message()

    assert "locked out" in error.lower()