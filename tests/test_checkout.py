import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage


@pytest.mark.smoke
def test_complete_checkout(page):

    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    checkout_page = CheckoutPage(page)

    login_page.navigate()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    products_page.add_backpack_to_cart()

    products_page.open_cart()

    checkout_page.checkout()

    checkout_page.enter_customer_details(
        "Sri",
        "Lekha",
        "500001"
    )

    checkout_page.continue_checkout()

    checkout_page.finish_order()

    assert "Thank you" in checkout_page.get_success_message()