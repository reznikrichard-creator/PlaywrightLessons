#test_internet.py
from playwright.sync_api import Dialog, Page, expect
import pytest

def test_click_action(page: Page):
    add_element_button = page.get_by_role("button", name="Add Element")
    delete_button = page.get_by_role("button", name="Delete")
    #go to the page
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    add_element_button.click()
    add_element_button.click()

    delete_button.first.click()

    expect(delete_button).to_be_visible()
    assert delete_button.is_visible()


def test_fill_and_press(page: Page):
    # 1. Go to Page
    page.goto("https://the-internet.herokuapp.com/login")
    username_field = page.get_by_label("Username")
    password_field = page.get_by_label("Password")

    username_field.fill("tomsmith")
    username_field.press("Tab")
    password_field.fill("SuperSecretPassword!")
    password_field.press("Enter")
  # Store the text from the page as actual restult THEN compare against Expected Result in assert statement
    actual_text = page.get_by_role("heading", name="Welcome to the Secure Area.").text_content()
    expected_text = "Welcome to the Secure Area. When you are done click logout below."
    assert expected_text in actual_text

def test_check_box(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    boxes = page.get_by_role("checkbox")

    boxes.first.check()
    boxes.last.uncheck()

    assert boxes.first.is_checked()
    assert not boxes.last.is_checked()

def test_dropdown(page: Page):
    page.goto("https://the-internet.herokuapp.com/dropdown")
    dropdown = page.locator("#dropdown")

    dropdown.select_option("2")
    dropdown.select_option(label= "Option 1")
    dropdown.select_option(index = 2)

def test_hovers(page: Page):
    page.goto("https://the-internet.herokuapp.com/hovers")

    images = page.locator(".figure").first
    images.hover()

def test_upload(page: Page):
    page.goto("https://the-internet.herokuapp.com/upload")
    page.locator("#file-upload").set_input_files("test_data/resume.txt") 
    page.locator("#file-submit").click()

def test_drag_and_drop(page: Page):
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")
    a = page.locator("#column-a")
    b = page.locator("#column-b")

    a.drag_to(b)
    b.drag_to(a)

# def test_context_menu(page: Page):
#     page.goto("https://the-internet.herokuapp.com/context_menu")
#     page.once("dialog", lambda dialog: dialog.accept())
#     page.locator("#hot-spot").click(button="right")
#     d_value = dialog.info_value

@pytest.mark.parametrize("link", ["random_data.txt","sample.txt"],)
def test_download (page: Page, link: str):
    page.goto("https://the-internet.herokuapp.com/download")
    with page.expect_download() as download_info:
        page.get_by_role("link", name=link).click()
    download = download_info.value
    assert link in str(download)

def test_hidden_ad (page: Page):
    page.goto("https://the-internet.herokuapp.com/entry_ad")
    modal = page.locator ("#modal")
    page.get_by_text("Close", exact=True).click()
    modal.wait_for(state = "hidden")
    assert not modal.is_visible()
