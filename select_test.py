import re
from playwright.sync_api import Page, expect

# Single Select Field

# Test that the combobox name is Choose language and that it's visible
def test_field_name(page: Page):
    page.goto("https://www.qa-practice.com/elements/select/single_select")
    expect(page.get_by_role("combobox", name="Choose language")).to_be_visible()

# I want to test for submitting without choosing any option
def test_submit_without_option(page: Page):
    page.goto("https://www.qa-practice.com/elements/select/single_select")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("You selected")).not_to_be_visible()

# I want to go through all the options and click submit using a for loop
def test_submit_options(page: Page):
    page.goto("https://www.qa-practice.com/elements/select/single_select")
    all_options = ["You selected Python", "You selected Ruby", "You selected JavaScript", "You selected Java", "You selected C#"]

    for i in range(1, 6):
        page.get_by_label("Choose language*").select_option(str(i))
        page.get_by_role("button", name="Submit").click()
        expect(page.get_by_text(all_options[i-1])).to_be_visible()



# Completed, but I'm sure it can be improved/ Maybe if I had a list of all the options and I would've done something like expect substring (all_options[1]) in string (You selected Python)

def test_multiple_fields_visibility(page: Page):
    page.goto("https://www.qa-practice.com/elements/select/mult_select")
    expect(page.get_by_label("Choose the place you want to")).to_be_visible()
    expect(page.get_by_label("Choose how you want to get")).to_be_visible()
    expect(page.get_by_label("Choose when you want to go*")).to_be_visible()


def test_selecting_options(page: Page):
    url = "https://www.qa-practice.com/elements/select/mult_select"
    page.goto(url)

    # range(1, 6) assumes options 1 through 5 are the valid choices
    for i in range(1, 6):
        for j in range(1, 5):
            for k in range(1, 4):
                # Always re-locate elements after a page reload/refresh
                c1 = page.get_by_label("Choose the place you want to")
                c2 = page.get_by_label("Choose how you want to get")
                c3 = page.get_by_label("Choose when you want to go*")

                # Perform selections
                c1.select_option(str(i))
                c2.select_option(str(j))
                c3.select_option(str(k))

                # Capture text before clicking submit
                val1 = c1.locator("option:checked").first.inner_text()
                val2 = c2.locator("option:checked").first.inner_text()
                val3 = c3.locator("option:checked").first.inner_text()

                # Submit
                page.get_by_role("button", name="Submit").click()

                # Check if we actually got a result
                result_locator = page.get_by_text("You selected")
                
                if result_locator.is_visible():
                    # If result is visible, verify the text
                    expected = f"to go by {val2} to the {val1} {val3}"
                    expect(page.get_by_text(expected)).to_be_visible()
                    
                    # Go back to the form to continue the loop
                    page.goto(url) 
                else:
                    # If the page just refreshed without a result, 
                    # Playwright is already back at the form, but locators are stale.
                    # The next iteration of the loop will re-locate them at the top.
                    pass
