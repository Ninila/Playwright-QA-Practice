# Here I'm experimenting with simple buttons
# I'm getting better

import re
from playwright.sync_api import Page, expect

# We check if the page has a button and we click on it
def test_simple_buttons(page: Page):
    page.goto("https://www.qa-practice.com/")

    expect(page.get_by_role("link", name="Simple button")).to_be_visible()
    page.get_by_role("link", name="Simple button").click()

    # Checking if there is a Click button, then we click it and check if the "Submitted" result appears
    expect(page.get_by_role("button", name="Click")).to_be_visible()
    page.get_by_role("button", name="Click").click()
    expect(page.get_by_text("Submitted")).to_be_visible()

# Check the "Looks like a button" tab which has a button that has actually the role of a link, not a button :)
def test_looks_like_a_button(page: Page):
    page.goto("https://www.qa-practice.com/")
    page.get_by_role("link", name="Simple button").click()

    expect(page.get_by_role("link", name="Looks like a button")).to_be_visible()
    page.get_by_role("link", name="Looks like a button").click()

    expect(page.get_by_role("link", name="Click")).to_be_visible()
    page.get_by_role("link", name="Click").click()
    expect(page.get_by_text("Submitted")).to_be_visible()

# Check the Enabled/Disabled State, their results after clicking submit and some edge cases
def test_disabled(page: Page):
    page.goto("https://www.qa-practice.com/")
    page.get_by_role("link", name="Simple button").click()

    expect(page.get_by_role("link", name="Disabled")).to_be_visible()
    page.get_by_role("link", name="Disabled").click()

    expect(page.get_by_text("Select state Disabled Enabled Submit")).to_be_visible()
    try:
        page.get_by_role("button", name="Submit").click(timeout=3000)
    except: 
        pass
    expect(page.get_by_text("Submitted")).not_to_be_visible()
    
    expect(page.get_by_label("Select state")).to_be_visible()
    page.get_by_label("Select state").select_option("enabled")
    expect(page.get_by_role("button", name="Submit")).to_be_visible()
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Submitted")).to_be_visible()



# Almost Complete ~ can be improved