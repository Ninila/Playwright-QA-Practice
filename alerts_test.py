from playwright.sync_api import Page, expect

url = "https://www.qa-practice.com/elements/alert/alert#"

def test_alert_box(page: Page):
    page.goto(url)
    
    # 1. Create a container to store the alert text
    alert_data = {}

    # 2. Tell Playwright: "Listen for an alert. When it pops up, save its message and accept it."
    def handle_dialog(dialog):
        alert_data["text"] = dialog.message
        dialog.accept()  # This clicks "OK" on the alert

    page.on("dialog", handle_dialog)

    # 3. Perform the click that triggers the alert
    expect(page.get_by_role("link", name="Click")).to_be_visible()
    page.get_by_role("link", name="Click").click()

    # 4. Assert that we actually caught the alert message!
    assert "I am an alert!" in alert_data.get("text", "")


def test_confirmation_box_cancel(page: Page):
    page.goto(url)
    page.get_by_role("link", name="Confirmation box").click()  

    alert_data = {}

    def handle_dialog(dialog):
        alert_data["text"] = dialog.message
        assert dialog.type == 'confirm'
        dialog.dismiss()

    page.on("dialog", handle_dialog) 

    expect(page.get_by_role("link", name="Click")).to_be_visible()
    page.get_by_role("link", name="Click").click()

    expect(page.get_by_text("You selected Cancel")).to_be_visible()

    assert "Select Ok or Cancel" in alert_data.get("text", "")

    
def test_confirmation_box_cancel(page: Page):
    page.goto(url)
    page.get_by_role("link", name="Confirmation box").click()  

    def handle_dialog_2(dialog):
        assert dialog.type == 'confirm'
        dialog.accept()
    
    page.on("dialog", handle_dialog_2)

    expect(page.get_by_role("link", name="Click")).to_be_visible()
    page.get_by_role("link", name="Click").click()

    expect(page.get_by_text("You selected Ok")).to_be_visible()

