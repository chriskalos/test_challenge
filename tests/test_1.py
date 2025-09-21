from playwright.sync_api import Page, expect
from itertools import product

# todo: Logging and standardize across tests

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
    expect(page.locator('id=cart_contents_container')).to_be_enabled()
    
    # Check that the item was actually added to the cart
    expect(page.locator('data-test=inventory-item')).to_be_enabled
    expect(page.locator('data-test=inventory-item-name')).to_contain_text('Sauce Labs Backpack')

    # Press the Checkout button
    page.locator('id=checkout').click()

    # Check that we reached the next checkout page
    expect(page.locator('.checkout_info')).to_be_enabled

    # Find all the form_group elements and count them
    form_inputs = page.locator('.form_group input')
    count = form_inputs.count()

    # Fill and unfill fields in a binary manner to test all possible combinations
    for combo in product([0,1], repeat=count):
        for i, fill_flag in enumerate(combo):
            if fill_flag:
                form_inputs.nth(i).fill('Test')
            else:
                form_inputs.nth(i).fill('')
        
        # Click the Continue button
        page.locator('id=continue').click()

        if all(combo):
            # All fields were filled so we expect the next page to appear
            expect(page.locator('id=checkout_summary_container')).to_be_enabled
        else:
            # Expect an error message every time an argument is not filled
            expect(page.locator('data-test=error')).to_be_enabled

    # Finish test by completing the whole checkout process
    page.locator('id=finish').click()