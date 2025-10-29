import time
from playwright.sync_api import Page


def test_playwrightBasic(playwright):

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://facebook.com")


def test_playwrightShortcut(page:Page):
    page.goto("https://google.com")

def test_CoreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("NourojAmin")
    page.get_by_label("Password:").fill("Password101")
    page.get_by_role("combobox").select_option("stud")
    page.locator("#terms").check()
    page.get_by_role("button",name="Sign In").click()

    time.sleep(5)



