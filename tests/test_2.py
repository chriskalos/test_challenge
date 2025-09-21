from playwright.sync_api import Page, expect

# todo: Logging

def test_products(page: Page):
    page.goto("https://www.saucedemo.com/")

    # Login sequence
    page.locator('id=user-name').fill('standard_user')
    page.locator('id=password').fill('secret_sauce')
    page.locator('id=login-button').click()

    # Check that we reached the products page
    expect(page.locator('id=page_wrapper')).to_be_enabled

    # Add two random products to the cart
    # find inventory_list and count all its inventory_item items
    # pick two inventory_item at random
    # put each item's relevant data in variables to track
    # and find the <button> within and press it
    # go to cart
    # check that two items are in cart and that they are the same items as before
    # complete form
    # check again that the two items are correct