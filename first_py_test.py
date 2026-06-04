# This are my first tests created using the Playwight official documentation from "https://playwright.dev/"
import re
from playwright.sync_api import Page, expect

# Checking the page title
def test_has_title(page: Page):

    # Navigate to any page via URL
    page.goto("https://playwright.dev/")

    # Expecting the title to cointain a substring
    expect(page).to_have_title(re.compile("Playwright"))

# Clicking and verifying the output
def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
    


# Completed ^_^