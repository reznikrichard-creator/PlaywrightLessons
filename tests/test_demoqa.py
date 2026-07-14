from playwright.sync_api import Page, expect


def test_practice_form(page: Page):
    page.goto("https://demoqa.com/automation-practice-form")
    page.get_by_role("textbox", name="First Name").click()
    page.get_by_role("textbox", name="First Name").fill("rich")
    page.get_by_role("textbox", name="Last Name").click()
    page.get_by_role("textbox", name="Last Name").fill("rez")
    page.get_by_role("textbox", name="name@example.com").click()
    page.get_by_role("textbox", name="name@example.com").fill("richrez@gmail.com")
    page.get_by_role("radio", name="Male", exact=True).check()
    page.get_by_role("radio", name="Female").check()
    page.get_by_role("radio", name="Other").check()
    page.get_by_role("textbox", name="Mobile Number").click()
    page.get_by_role("textbox", name="Mobile Number").fill("6436436478")
    page.get_by_text("Sports").click()
    page.get_by_text("Reading").click()
    page.get_by_role("button", name="Choose File").click()
    page.get_by_role("button", name="Choose File").set_input_files("test_data/resume.txt")
    page.get_by_role("button", name="Submit").click()
    page.get_by_text("Thanks for submitting the form").click()
    page.get_by_role("cell", name="rich rez").click()

    actual_text = page.locator("#example-modal-sizes-title-lg").text_content()
    expected_text = "Thanks for submitting the form"
    assert expected_text in actual_text

    