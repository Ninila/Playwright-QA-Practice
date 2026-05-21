import re
from playwright.sync_api import Page, expect

def test_text_area_visibility(page: Page):
    page.goto("https://www.qa-practice.com/elements/textarea/single")
    text_field = page.get_by_role("textbox", name="Text area")
    expect(text_field).to_be_visible()

def test_text_area_required_field(page: Page):
    page.goto("https://www.qa-practice.com/elements/textarea/single")
    expect(page.get_by_role("button", name="Submit")).to_be_visible()
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("You entered")).not_to_be_visible()
    page.get_by_role("textbox", name="Text area").click()
    page.get_by_role("textbox", name="Text area").fill("Yoooy")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("You entered Yoooy")).to_be_visible()

def test_text_area_multiple_visibility(page: Page):
    page.goto("https://www.qa-practice.com/elements/textarea/textareas")
    chapter_1 = page.get_by_role("textbox", name="First chapter")
    chapter_2 = page.get_by_role("textbox", name="Second chapter")
    chapter_3 = page.get_by_role("textbox", name="Third chapter")
    submit = page.get_by_role("button", name="Submit")

    expect(chapter_1).to_be_visible()
    expect(chapter_2).to_be_visible()
    expect(chapter_3).to_be_visible()
    expect(submit).to_be_visible()

    chapter_1_value = page.get_by_role("textbox", name="First chapter").input_value()

    if chapter_1_value == "":
        chapter_2.click()
        chapter_2.fill("2")
        submit.click()
        expect(page.get_by_text("You entered")).not_to_be_visible()

        chapter_3.click()
        chapter_3.fill("3")
        submit.click()
        expect(page.get_by_text("You entered")).not_to_be_visible()

        chapter_2.click()
        chapter_2.fill("2")
        chapter_3.click()
        chapter_3.fill("3")
        submit.click()
        expect(page.get_by_text("You entered")).not_to_be_visible()

    chapter_1.click()
    chapter_1.fill("Jon")
    chapter_2.click()
    chapter_2.fill("Snow")
    chapter_3.click()
    chapter_3.fill("Lives")
    submit.click()

    expect(page.get_by_text("You entered")).to_be_visible()
    expect(page.get_by_text("Jon")).to_be_visible()
    expect(page.get_by_text("Snow")).to_be_visible()
    expect(page.get_by_text("Lives")).to_be_visible()