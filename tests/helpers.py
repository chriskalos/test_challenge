from playwright.sync_api import Page

def login(page: Page):
    page.goto("https://www.saucedemo.com/")

    # Login sequence
    page.locator('id=user-name').fill('standard_user')
    page.locator('id=password').fill('secret_sauce')
    page.locator('id=login-button').click()