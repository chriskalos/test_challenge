from playwright.sync_api import Page, expect

def test_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    # Login sequence
    page.locator('id=user-name').fill('standard_user')
    page.locator('id=password').fill('secret_sauce')
    page.locator('id=login-button').click()

    # Check that we reached the products page
    expect(page.locator('id=page_wrapper')).to_be_enabled

    # Find the backpack, add it to cart
    page.locator('id=add-to-cart-sauce-labs-backpack').click()
    # Go to the cart page
    page.locator('data-test=shopping-cart-link').click()
    
    # Check that the item was actually added to the cart
    expect(page.locator('data-test=inventory-item')).to_be_enabled
    expect(page.locator('data-test=inventory-item-name')).to_contain_text('Sauce Labs Backpack')

    # Press the Checkout button
    page.locator('id=checkout').click()

    # Check that we reached the checkout page
    expect(page.locator('id=checkout_info_container')).to_be_enabled

    # Click the Checkout button before filling in any containers
    page.locator('id=continue').click()

    # Expect an error message every time an argument is not filled
    expect(page.locator('data-test=error')).to_be_enabled

    # page.locator('id=first-name').fill('FirstName')
