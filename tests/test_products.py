from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_add_product_to_cart(page):

    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.navigate()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    products_page.add_backpack_to_cart()

    products_page.open_cart()

    assert "cart.html" in page.url