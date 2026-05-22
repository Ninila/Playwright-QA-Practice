import re
from playwright.sync_api import Page, expect


# Test for the visibility of the checkbox on the desired page
def test_checkbox_visibility(page: Page):
    page.goto("https://www.qa-practice.com/elements/checkbox/single_checkbox")
    expect(page.get_by_role("checkbox", name="Select me or not")).to_be_visible

# Test that the checkbox can be selected
def test_checkbox_select(page: Page):
    page.goto("https://www.qa-practice.com/elements/checkbox/single_checkbox")
    page.get_by_role("checkbox", name="Select me or not").check()

# Test the result after clicking the submit button with the checkbox checked/unchecked
def test_checkbox_submit(page: Page):
    # Checking the box
    page.goto("https://www.qa-practice.com/elements/checkbox/single_checkbox")
    page.get_by_role("checkbox", name="Select me or not").check()

    # Testing the result after clicking submit
    expect(page.get_by_role("button", name="Submit")).to_be_visible()
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Selected checkboxes")).to_be_visible()
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Selected checkboxes")).not_to_be_visible()

def test_multiple_checkboxes_visibility(page: Page):
    # Navigating to the target page and Checking to see if there are 3 checkboxes on te page
    page.goto("https://www.qa-practice.com/elements/checkbox/mult_checkbox")
    expect(page.get_by_role("checkbox", name="one")).to_be_visible()
    expect(page.get_by_role("checkbox", name="two")).to_be_visible()
    expect(page.get_by_role("checkbox", name="three")).to_be_visible()

def test_multiple_checkboxes_check(page: Page):
    # Testing if multiple checkboxes can be checked without issues
    page.goto("https://www.qa-practice.com/elements/checkbox/mult_checkbox")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Selected checkboxes")).not_to_be_visible()

    page.get_by_role("checkbox", name="One").click()
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Selected checkboxes: one")).to_be_visible()

    page.get_by_role("checkbox", name="Two").click()
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Selected checkboxes: two")).to_be_visible()

    page.get_by_role("checkbox", name="Three").click()
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Selected checkboxes: three")).to_be_visible()
    

# Completed ^_^