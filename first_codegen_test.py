import re
from playwright.sync_api import Playwright, sync_playwright, expect


# Change this:
def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

# To this:
def test_run(page):
    # Now you can jump straight to page.goto()
    page.goto("https://www.qa-practice.com/")
    page.get_by_role("link", name="Text input").click()
    expect(page.get_by_role("link", name="Text input")).to_be_visible

    expect(page.get_by_role("textbox", name="Text string*")).to_be_visible()
    page.get_by_role("textbox", name="Text string*").click()
    page.get_by_role("textbox", name="Text string*").fill("Inputting the text in the text field")
    page.get_by_role("textbox", name="Text string*").press("Enter")
    page.get_by_role("textbox", name="Text string*").click()
    page.get_by_text("Please enter no more than 25").click()
    page.get_by_text("Enter a valid string").click()
    expect(page.get_by_role("button", name="Requirements:")).to_be_visible()
    page.get_by_role("button", name="Requirements:").click()
    page.get_by_role("textbox", name="Text string*").click()
    page.get_by_role("textbox", name="Text string*").fill("Inputting the text ")
    page.get_by_role("textbox", name="Text string*").press("Enter")
    page.get_by_role("textbox", name="Text string*").click()
    page.get_by_role("textbox", name="Text string*").fill("InputtingTheText")
    page.get_by_role("textbox", name="Text string*").press("Enter")
    page.get_by_text("Your input was: InputtingTheText").click()
    page.get_by_role("link", name="Email field").click()
    page.get_by_role("textbox", name="Email*").click()
    page.get_by_role("textbox", name="Email*").fill("Alexandru.Test@gmail.com")
    page.get_by_role("textbox", name="Email*").press("Enter")
    
    # Testing the failure of non existent locator
    #expect(page.get_by_role("link", name="THIS DOES NOT EXIST")).to_be_visible()

    page.get_by_text("Alexandru.Test@gmail.com").click()
    page.get_by_text("Your input was:").click()
    page.get_by_text("Your input was: Alexandru.").click()
    page.get_by_text("Your input was: Alexandru.").click()
    page.get_by_role("link", name="Password field").click()
    page.get_by_role("textbox", name="Password*").click()
    page.get_by_role("textbox", name="Password*").fill("Cicaraua123")
    page.get_by_role("textbox", name="Password*").fill("Cicaraua1234$")
    
    # ---------------------
  

