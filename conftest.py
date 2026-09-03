import os

import pytest
from playwright.sync_api import sync_playwright


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)


@pytest.fixture
def page(request):

    with sync_playwright() as p:

        headless = os.getenv("CI", "false").lower() == "true"

        browser = p.chromium.launch(headless=headless)

        page = browser.new_page()

        yield page

        # Take screenshot if the test fails
        if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:

            os.makedirs("screenshots", exist_ok=True)

            screenshot_name = request.node.name.replace("/", "_")

            screenshot_path = f"screenshots/{screenshot_name}.png"

            page.screenshot(
                path=screenshot_path,
                full_page=True
            )

            print(f"\nScreenshot saved: {screenshot_path}")

        browser.close()