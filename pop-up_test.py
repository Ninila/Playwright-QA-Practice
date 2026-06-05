from playwright.sync_api import Page, expect

url = "https://www.qa-practice.com/elements/popup/modal"

# Check the "Launch Pop-Up" button visibility
def test_popup_visibility(page: Page):
    page.goto(url)
    launch_popup = page.get_by_role("button", name="Launch Pop-Up")
    expect(launch_popup).to_be_visible()

# Launching the Pop-Up by clicking it
def test_popup_click(page: Page):
    page.goto(url)
    launch_popup = page.get_by_role("button", name="Launch Pop-Up")

    # Get popup after a specific action (Click())
    launch_popup.click()

    expect(page.get_by_text("Close")).to_be_visible()
    expect(page.get_by_role("button", name="Send")).to_be_visible()
    expect(page.get_by_role("checkbox", name="Select me or not")).to_be_visible()
    
# Test what happens when interacting with the "Close", "Send", and "Checkbox" buttons work and what are their outcomes 
def test_popup_elements(page: Page):
    page.goto(url)
    launch_popup = page.get_by_role("button", name="Launch Pop-Up")

    launch_popup.click()

    # We use get_by_text for the Close buutton because the X button also has a "Close" tag and Playwright doesn't know which one I'm reffering to
    cancel = page.get_by_text("Close")
    send = page.get_by_role("button", name="Send")
    checkbox = page.get_by_role("checkbox", name="Select me or not")

    
    cancel.click()
    expect(page.get_by_text("Selected checkboxes:")).not_to_be_visible()

    launch_popup.click()
    
    send.click()
    expect(page.get_by_text("Selected checkboxes: None")).to_be_visible()

    launch_popup.click()

    checkbox.click()
    send.click()
    expect(page.get_by_text("Selected checkboxes: select me or not")).to_be_visible()

    