from playwright.sync_api import Dialog, Page, expect
import pytest
from playwright.sync_api import Page
def test_opens_the_shop(page: Page):
    page.goto("https://www.saucedemo.com/")