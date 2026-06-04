# Here I verify an iframe and it's elements functionalities
# I'm really confident in my Playwright abilities now

from playwright.sync_api import Page, expect

url = "https://www.qa-practice.com/elements/iframe/iframe_page"

# Checking for iframe visibility
def test_iframe_visibility(page: Page):
    page.goto(url)
    iframe = page.locator("iframe")
    expect(iframe).to_be_visible()

# Checking the headin title of the page inside the iframe
def test_iframe_element_title(page: Page):
    page.goto(url)
    iframe = page.frame_locator("iframe")
    expect(iframe.get_by_role("heading", name="Album example")).to_be_visible()

# Checking the toggle button and the Social Media links inside the iframe
def test_iframe_element_social_links(page: Page):
    page.goto(url)
    iframe = page.frame_locator("iframe")
    toggle_button = iframe.get_by_role("button", name="Toggle navigation")

    # Making sure the social links are not visible before clicking the toggle button
    expect(iframe.get_by_role("link", name="Follow on Twitter")).not_to_be_visible()
    expect(iframe.get_by_role("link", name="Like on Facebook")).not_to_be_visible()
    expect(iframe.get_by_role("link", name="Email me")).not_to_be_visible()

    # Clicking the toggle button and verifying Social Links visibility
    expect(toggle_button).to_be_visible()
    toggle_button.click()
    expect(iframe.get_by_role("link", name="Follow on Twitter")).to_be_visible()
    expect(iframe.get_by_role("link", name="Like on Facebook")).to_be_visible()
    expect(iframe.get_by_role("link", name="Email me")).to_be_visible()

# Testing the 2 main buttons inside the iframe "Main call to action" and "Secondary action"
def test_iframe_main_buttons(page: Page):
    page.goto(url)
    iframe = page.frame_locator("iframe")
    main_button = iframe.get_by_role("link", name="Main call to action")
    secondary_button = iframe.get_by_role("link", name="Secondary action")

    expect(main_button).to_be_visible()
    expect(secondary_button).to_be_visible()

    main_button.click()
    secondary_button.click()
    # Nothing should modify after running the above code, if it did, we would use expect to verify the content updated

# We'll be testing the footer buttons functionality
def test_iframe_footer_buttons(page: Page):
    page.goto(url)
    iframe = page.frame_locator("iframe")
    home_button = iframe.get_by_role("link", name="Visit the homepage")
    getting_started_guide = iframe.get_by_role("link", name="getting started guide")
    back_top = iframe.get_by_role("link", name="Back to top")

    # Checking visibility
    expect(home_button).to_be_visible()
    expect(getting_started_guide).to_be_visible()
    expect(back_top).to_be_visible()

    # Checking button's functionality

    # Home
    home_button.click()
    expect(iframe.get_by_text("Hello!")).to_be_visible()
    page.goto(url)

    # Getting started guide
    getting_started_guide.click()
    expect(iframe.get_by_role("heading", name="Not Found")).to_be_visible()
    page.goto(url)

    # Back to top
    back_top.click()
    expect(iframe.get_by_role("heading", name="Album example")).to_be_in_viewport()
