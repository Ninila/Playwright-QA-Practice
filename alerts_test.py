# Working with dialog alerts, accepting, declining and filling in text fields for these.
# This one was challenging, but who doesn't love a challenge?

from playwright.sync_api import Page, expect

url = "https://www.qa-practice.com/elements/alert/alert#"


# This test is for a simple alert message where "OK" is the only option
def test_alert_box(page: Page):
    page.goto(url)
    
    # Create a container to store the alert text
    alert_data = {}

    # Tell Playwright: "Listen for an alert. When it pops up, save its message and accept it."
    def handle_dialog(dialog):
        alert_data["text"] = dialog.message
        dialog.accept()  # This clicks "OK" on the alert

    page.on("dialog", handle_dialog)

    # Perform the click that triggers the alert
    expect(page.get_by_role("link", name="Click")).to_be_visible()
    page.get_by_role("link", name="Click").click()

    # Assert that we actually caught the alert message!
    assert "I am an alert!" in alert_data.get("text", "")


# This tests a confirmation box, which has the "OK" and "Cancel" options and we choose "Cancel"
def test_confirmation_box_cancel(page: Page):
    page.goto(url)
    page.get_by_role("link", name="Confirmation box").click()  

    # Create a container to verify the Confirmation box text
    alert_data = {}

    # This is the way to handle the dialog: When the alert pops up, store the text and cancel it with dialog.dismiss()
    def handle_dialog(dialog):
        alert_data["text"] = dialog.message
        assert dialog.type == 'confirm'
        dialog.dismiss()

    page.on("dialog", handle_dialog) 

    # Click the button that initiates the alert
    expect(page.get_by_role("link", name="Click")).to_be_visible()
    page.get_by_role("link", name="Click").click()

    # Expect the result of canceling the alert to be visible :)
    expect(page.get_by_text("You selected Cancel")).to_be_visible()

    # Assert the Confirmation box text is correct
    assert "Select Ok or Cancel" in alert_data.get("text", "")


# This tests a confirmation box, which has the "OK" and "Cancel" options and we choose "OK"
def test_confirmation_box_ok(page: Page):
    page.goto(url)
    page.get_by_role("link", name="Confirmation box").click()  
    
    # This is the way to handle the dialog: When the alert pops up, we select the "OK" option using dialog.accept()
    def handle_dialog_2(dialog):
        assert dialog.type == 'confirm'
        dialog.accept()
    
    page.on("dialog", handle_dialog_2)

    # We intiate the alert by clicking a button named "Click"
    expect(page.get_by_role("link", name="Click")).to_be_visible()
    page.get_by_role("link", name="Click").click()

    # We check the result of our selection is displayed on the page after clicking "OK"
    expect(page.get_by_text("You selected Ok")).to_be_visible()


# Testing the prompt alert with the cancel option
def test_prompt_alert_cancel(page: Page):
    page.goto(url)
    page.get_by_role("link", name="Prompt box").click()

    # Handling the alert listener
    def handle_dialog(dialog):
        assert dialog.type == 'prompt'
        dialog.dismiss()

    page.on("dialog", handle_dialog)

    # Assert that clicking cancel will display the "You canceled the prompt" message
    page.get_by_role("link", name="Click").click()
    expect(page.get_by_text("You canceled the prompt")).to_be_visible()


# Testing the prompt alert using the "OK" option, but without completing the text field
def test_prompt_alert_ok_notext(page: Page):
    page.goto(url)
    page.get_by_role("link", name="Prompt box").click()

    # Handling the alert listener
    def handle_dialog(dialog):
        assert dialog.type == 'prompt'
        dialog.accept()

    page.on("dialog", handle_dialog)

    # Assert that clicking cancel will display the "You entered nothing" message
    page.get_by_role("link", name="Click").click()
    expect(page.get_by_text("You entered nothing")).to_be_visible()


# Testing the prompt alert using the "OK" option and completing the text field
def test_prompt_alert_ok_withtext(page: Page):
    page.goto(url)
    page.get_by_role("link", name="Prompt box").click()
    prompt_input = "Joe Dane"

    # Handling the alert listener
    def handle_dialog(dialog):
        assert dialog.type == 'prompt'
        dialog.accept(prompt_input)

    page.on("dialog", handle_dialog)

    # Assert that clicking cancel will display the text "You entered nothing"
    page.get_by_role("link", name="Click").click()
    expect(page.get_by_text(f"You entered {prompt_input}")).to_be_visible()
