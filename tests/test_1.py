from playwright.sync_api import Page, expect

def test_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    print("Entered", page.title(), "page.")

    # # Login sequence
    # page.fill("input[id='user-name']", "standard_user")
    # page.fill("input[id='password']", "secret_sauce")
    # page.click("input[id='login-button']")